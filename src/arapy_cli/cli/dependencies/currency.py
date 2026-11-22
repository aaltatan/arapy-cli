"""The `--currency` option: a JSON file defining one currency (arapy ships none)."""

import json
from pathlib import Path
from typing import Annotated, Any

import typer
from arapy import Currency, Gender, Noun
from typer_di import Depends


def load_currency(path: Path) -> Currency:
    """Build a `Currency` from a JSON file; the keys are `Currency.create`'s arguments."""
    try:
        spec: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))

        subunit = spec.pop("subunit")

        gender = Gender(spec.pop("gender"))

        subunit_gender = Gender(subunit.pop("gender"))

        return Currency.create(
            **spec,
            gender=gender,
            subunit=Noun.create(**subunit, gender=subunit_gender),
        )

    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        msg = f"Currency file '{path.name}' is not valid JSON: {error}"

        raise typer.BadParameter(msg) from error

    except (KeyError, TypeError, ValueError, AttributeError) as error:
        msg = f"Currency file '{path.name}' is missing or has a wrong key: {error}"

        raise typer.BadParameter(msg) from error


def _get_currency(
    path: Annotated[
        Path | None,
        typer.Option(
            "-c",
            "--currency",
            help="Currency JSON file, see examples/syp.json",
            exists=True,
            dir_okay=False,
            resolve_path=True,
            show_default=False,
        ),
    ] = None,
) -> Currency | None:
    return None if path is None else load_currency(path)


CurrencyDI = Annotated[Currency | None, Depends(_get_currency)]
"""Injects the `--currency` file, or None."""
