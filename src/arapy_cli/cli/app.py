"""The arapy command line application."""

import sys
from datetime import date
from importlib.metadata import version
from typing import Annotated

import arapy
import typer
from arapy import NAMES, SEARCH, ArDate, Case, Gender, MonthNames, Tafqeet
from typer_di import TyperDI
from typer_swissknife import command

from arapy_cli.cli.dependencies.currency import CurrencyDI
from arapy_cli.cli.dependencies.number_format import Digits, NumberFormatDI
from arapy_cli.cli.errors import fail, reported

app = TyperDI(
    name="arapy",
    help="Arabic numbers, words, digits, text and dates, from the command line.",
    no_args_is_help=True,
    rich_markup_mode="rich",
)

# a plain alias: typer does not unwrap a `type X = ...` alias
Values = Annotated[
    list[str] | None,
    typer.Argument(help="Values; one per line on stdin when none are given", show_default=False),
]


def _values(values: list[str] | None, default: list[str] | None = None) -> list[str]:
    """Return the arguments, else the non-empty lines piped on stdin, else `default`."""
    if values:
        return values

    # a terminal would wait for typing, so stdin is read only when piped
    lines = [] if sys.stdin.isatty() else [line.strip() for line in sys.stdin if line.strip()]

    if lines:
        return lines

    if default is not None:
        return default

    msg = "Give one or more values, or pipe them in, one per line"

    raise typer.BadParameter(msg)


def _int(value: str) -> int:
    try:
        return int(arapy.to_latin_digits(value))

    except ValueError:
        fail(f"Error: '{value}' is not a whole number")


def _version(value: bool) -> None:
    if value:
        typer.echo(f"arapy-cli {version('arapy-cli')} (arapy {version('arapy')})")

        raise typer.Exit


@app.callback()
def _main(
    _: Annotated[
        bool,
        typer.Option("--version", "-V", callback=_version, is_eager=True, help="Show the version"),
    ] = False,
) -> None:
    """Arabic numbers, words, digits, text and dates, from the command line."""


# -----------------------
# words
# -----------------------


@command(app, name="words", aliases=("w",), help="Numbers or amounts in Arabic words (تفقيط)")
def words(
    currency: CurrencyDI,
    values: Values = None,
    case: Annotated[Case, typer.Option("--case", help="Grammatical case")] = Case.NOMINATIVE,
    alef: Annotated[bool, typer.Option("--alef", help="Spell hundreds مائة, not مئة")] = False,
    prefix: Annotated[str, typer.Option("--prefix", help="Text before, e.g. فقط")] = "",
    suffix: Annotated[str, typer.Option("--suffix", help="Text after, e.g. لا غير")] = "",
    parse: Annotated[
        bool,
        typer.Option("--parse", help="Read words back into a number instead"),
    ] = False,
) -> None:
    tafqeet = Tafqeet(hundreds="مائة" if alef else "مئة", case=case, prefix=prefix, suffix=suffix)

    for value in _values(values):
        with reported(value):
            typer.echo(tafqeet.parse(value, currency) if parse else tafqeet(value, currency))


# -----------------------
# money / number / digits
# -----------------------


@command(app, name="money", aliases=("m",), help="Amounts in digits with the currency symbol")
def money(currency: CurrencyDI, number_format: NumberFormatDI, values: Values = None) -> None:
    if currency is None:
        msg = "money needs -c / --currency"

        raise typer.BadParameter(msg)

    for value in _values(values):
        with reported(value):
            typer.echo(arapy.format_money(value, currency, **number_format))


@command(app, name="number", aliases=("n",), help="Format numbers given in any digit set")
def number(
    number_format: NumberFormatDI,
    values: Values = None,
    percent: Annotated[bool, typer.Option("--percent", help="Write 0.25 as 25٪")] = False,
) -> None:
    write = arapy.format_percent if percent else arapy.format_number

    for value in _values(values):
        with reported(value):
            typer.echo(write(value, **number_format))


@command(app, name="digits", aliases=("d",), help="Convert digits between Latin, Arabic, Persian")
def digits(
    values: Values = None,
    to: Annotated[Digits, typer.Option("--to", help="Target digit set")] = Digits.ARABIC,
) -> None:
    convert = {
        Digits.LATIN: arapy.to_latin_digits,
        Digits.ARABIC: arapy.to_arabic_digits,
        Digits.PERSIAN: arapy.to_persian_digits,
    }[to]

    for value in _values(values):
        typer.echo(convert(value))


# -----------------------
# normalize / sort
# -----------------------


@command(app, name="normalize", aliases=("norm",), help="Fold letters, drop tashkeel and tatweel")
def normalize(
    values: Values = None,
    names: Annotated[
        bool,
        typer.Option("--names", help="Name preset: also splits عبدالله into عبد الله"),
    ] = False,
) -> None:
    normalizer = NAMES if names else SEARCH

    for value in _values(values):
        typer.echo(normalizer(value))


@command(app, name="sort", aliases=("s",), help="Sort lines in Arabic alphabetical order")
def sort(
    values: Values = None,
    reverse: Annotated[bool, typer.Option("--reverse", "-r", help="Descending")] = False,
) -> None:
    for value in arapy.ar_sorted(_values(values), reverse=reverse):
        typer.echo(value)


# -----------------------
# ordinal
# -----------------------


@command(app, name="ordinal", aliases=("o",), help="Ordinals: الأول، الحادية عشرة، أولًا")
def ordinal(
    values: Values = None,
    feminine: Annotated[bool, typer.Option("--feminine", "-f", help="الأولى, not الأول")] = False,
    case: Annotated[Case, typer.Option("--case", help="Grammatical case")] = Case.NOMINATIVE,
    indefinite: Annotated[bool, typer.Option("--indefinite", help="ثالث, not الثالث")] = False,
    adverb: Annotated[bool, typer.Option("--adverb", help="List markers: أولًا، ثانيًا")] = False,
) -> None:
    if adverb and (feminine or indefinite or case != Case.NOMINATIVE):
        msg = "--adverb does not take --feminine, --indefinite or --case"

        raise typer.BadParameter(msg)

    gender = Gender.FEMININE if feminine else Gender.MASCULINE

    for value in _values(values):
        n = _int(value)

        with reported(value):
            if adverb:
                typer.echo(arapy.ordinal_adverb(n))

            else:
                typer.echo(arapy.ordinal(n, gender, definite=not indefinite, case=case))


# -----------------------
# date
# -----------------------


@command(app, name="date", aliases=("dt",), help="Write ISO dates (default: today) in Arabic")
def format_date(
    values: Annotated[
        list[str] | None,
        typer.Argument(help=r"ISO dates: 2026-01-05 \[default: today, or stdin lines]"),
    ] = None,
    fmt: Annotated[
        str,
        typer.Option("--format", "-f", help="Directives: %A %d %O %B %m %Y %j"),
    ] = "%A %d %B %Y",
    months: Annotated[
        MonthNames | None,
        typer.Option("--months", help=r"Month names \[default: levant]", show_default=False),
    ] = None,
    to: Annotated[Digits, typer.Option("--digits", help="Digit set")] = Digits.LATIN,
    hijri: Annotated[
        bool, typer.Option("--hijri", help="Write the Hijri date (Umm al-Qura)")
    ] = False,
) -> None:
    if hijri and months is not None:
        msg = "--months does not work with --hijri (Hijri months have one set of names)"

        raise typer.BadParameter(msg)

    today = date.today().isoformat()  # noqa: DTZ011 - the local date is the one wanted

    for value in _values(values, default=[today]):
        try:
            day = ArDate.fromisoformat(arapy.to_latin_digits(value))

        except ValueError:
            fail(f"Error: '{value}' is not an ISO date (YYYY-MM-DD)")

        with reported(value):
            if hijri:
                typer.echo(day.to_hijri().format(fmt, digits=to.value))

            else:
                typer.echo(day.format(fmt, months=months or MonthNames.LEVANT, digits=to.value))


def main() -> None:
    """Run the arapy application, with UTF-8 in and out so Arabic survives pipes."""
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")

    app()
