from pathlib import Path

import pytest
from typer.testing import CliRunner

from arapy_cli.cli.app import app

EXAMPLES = Path(__file__).parents[1] / "examples"

SYP = str(EXAMPLES / "syp.json")


def run(*args: str, input: str | None = None) -> tuple[int, str]:  # noqa: A002
    result = CliRunner().invoke(app, list(args), input=input)

    return result.exit_code, result.output


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        (["words", "2026"], "ألفان وستة وعشرون\n"),
        (
            ["w", "1250.50", "-c", SYP, "--prefix", "فقط", "--suffix", "لا غير"],
            "فقط ألف ومئتان وخمسون ليرةً سوريةً وخمسون قرشًا لا غير\n",
        ),
        (["w", "300", "--alef"], "ثلاثمائة\n"),
        (["w", "--parse", "مائة وخمسة وعشرون"], "125\n"),
        (["money", "12500", "-c", SYP], "١٢٬٥٠٠ ل.س\n"),
        (["number", "١٢٥٠٠٠٫٥", "--grouping", ""], "125000.5\n"),
        (["n", "0.25", "--percent", "--digits", "arabic"], "٢٥٪\n"),
        (["digits", "2026", "--to", "persian"], "۲۰۲۶\n"),
        (["norm", "عبدالله  أبوبكر", "--names"], "عبد الله ابو بكر\n"),
        (["o", "1", "11", "-f"], "الأولى\nالحادية عشرة\n"),
        (["o", "1", "2", "--adverb"], "أولًا\nثانيًا\n"),
        (["dt", "2026-01-05", "-f", "%A %O من %B %Y"], "الاثنين الخامس من كانون الثاني 2026\n"),
        (["dt", "2026-01-05", "--hijri", "--digits", "arabic"], "الاثنين ١٦ رجب ١٤٤٧\n"),
    ],
)
def test_commands(args: list[str], expected: str) -> None:
    assert run(*args) == (0, expected)


def test_values_from_stdin() -> None:
    assert run("sort", input="يوسف\n\nأحمد\nزينب\n") == (0, "أحمد\nزينب\nيوسف\n")


@pytest.mark.parametrize(
    ("args", "message"),
    [
        (["w", "10.5"], "A fraction needs a currency unit"),
        (["o", "x"], "'x' is not a whole number"),
        (["dt", "nope"], "'nope' is not an ISO date"),
    ],
)
def test_arapy_errors_exit_1(args: list[str], message: str) -> None:
    code, output = run(*args)

    assert code == 1

    assert message in output


@pytest.mark.parametrize(
    "args",
    [
        ["money", "5"],
        ["o", "1", "--adverb", "-f"],
        ["dt", "2026-01-05", "--hijri", "--months", "egyptian"],
    ],
)
def test_bad_option_combinations_exit_2(args: list[str]) -> None:
    assert run(*args)[0] == 2


def test_bad_currency_file(tmp_path: Path) -> None:
    path = tmp_path / "bad.json"

    path.write_text('{"code": "X"}', encoding="utf-8")

    code, output = run("w", "1", "-c", str(path))

    assert code == 2

    assert "bad.json" in output
