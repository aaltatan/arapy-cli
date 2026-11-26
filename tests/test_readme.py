"""Run every `arapy` command in the README's and docs' bash blocks and check their output.

The output is the comment after the command (`arapy words 2  # اثنان`), or the `# ` lines
right below it; a command with neither only has to succeed.
"""

import re
import shlex
import textwrap
from pathlib import Path

import pytest
from typer.testing import CliRunner

from arapy_cli.cli.app import app

ROOT = Path(__file__).parent.parent

PAGES = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]

# docs indent code blocks inside tabs and admonitions, so the fence may be indented
FENCE = re.compile(r"^([ \t]*)```bash\n(.*?)^\1```", re.DOTALL | re.MULTILINE)

BLOCKS = [
    textwrap.dedent(block)
    for page in PAGES
    for _, block in FENCE.findall(page.read_text(encoding="utf-8"))
]


def examples() -> list[tuple[str, list[str]]]:
    found: list[tuple[str, list[str]]] = []

    for block in BLOCKS:
        for line in block.splitlines():
            if line.startswith("arapy"):
                command, _, output = line.partition("  # ")

                found.append((command, [output] if output else []))

            elif line.startswith("# ") and found:
                found[-1][1].append(line.removeprefix("# "))

    return found


EXAMPLES = examples()


def test_the_readme_has_examples() -> None:
    assert len(EXAMPLES) > 60


@pytest.mark.parametrize(("command", "output"), EXAMPLES, ids=[c[:60] for c, _ in EXAMPLES])
def test_readme_example(command: str, output: list[str], monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(ROOT / "examples")

    result = CliRunner().invoke(app, shlex.split(command)[1:])

    assert result.exit_code == 0, result.output

    if output:
        assert result.output == "".join(f"{line}\n" for line in output)
