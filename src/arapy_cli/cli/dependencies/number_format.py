"""Digits and separators for `number` and `money`; unset options keep arapy's defaults."""

from enum import StrEnum
from typing import Annotated, Any

import typer
from typer_di import Depends

_PANEL = "Formatting"


class Digits(StrEnum):
    LATIN = "latin"
    ARABIC = "arabic"
    PERSIAN = "persian"


def _get_number_format(
    digits: Annotated[
        Digits | None,
        typer.Option("--digits", show_default=False, help="Digit set", rich_help_panel=_PANEL),
    ] = None,
    grouping: Annotated[
        str | None,
        typer.Option(
            "--grouping",
            show_default=False,
            help="Thousands separator; '' for none",
            rich_help_panel=_PANEL,
        ),
    ] = None,
    decimal: Annotated[
        str | None,
        typer.Option("--decimal", show_default=False, help="Decimal mark", rich_help_panel=_PANEL),
    ] = None,
    places: Annotated[
        int | None,
        typer.Option(
            "--places",
            min=0,
            show_default=False,
            help="Decimal places (pads, never rounds)",
            rich_help_panel=_PANEL,
        ),
    ] = None,
) -> dict[str, Any]:
    given = {
        "digits": None if digits is None else digits.value,
        "grouping": grouping,
        "decimal": decimal,
        "places": places,
    }

    kwargs: dict[str, Any] = {name: value for name, value in given.items() if value is not None}

    if grouping == "":
        kwargs["grouping"] = None

    return kwargs


NumberFormatDI = Annotated[dict[str, Any], Depends(_get_number_format)]
"""Injects the formatting keywords given on the command line, for `format_number` & co."""
