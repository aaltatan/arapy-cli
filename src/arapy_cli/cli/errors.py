"""Report runtime failures as a red message and exit code 1, never as a traceback."""

from collections.abc import Iterator
from contextlib import contextmanager
from typing import NoReturn

import typer
from arapy import ArapyError


def fail(message: str) -> NoReturn:
    """Print `message` in red on stderr and exit with code 1."""
    typer.secho(message, fg="red", err=True)

    raise typer.Exit(1)


@contextmanager
def reported(value: str) -> Iterator[None]:
    """Turn arapy errors (bad number, date, out of range) into `fail`, naming the input."""
    try:
        yield

    except ArapyError as error:
        fail(f"Error in '{value}': {error}")
