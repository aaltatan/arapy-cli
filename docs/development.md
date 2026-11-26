# Development

```text
git clone https://github.com/aaltatan/arapy-cli
cd arapy-cli
uv sync
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run mypy --strict src tests
```

arapy-cli is a thin shell around the [arapy](https://aaltatan.github.io/arapy/) library:
the grammar, the digits, the calendars and the number parsing all live there. A change
to how something is written goes into arapy first.

## Project structure

```text
src/arapy_cli/
├── __init__.py              # main()
├── __main__.py              # python -m arapy_cli
└── cli/
    ├── app.py               # the commands
    ├── errors.py            # fail(), reported(): arapy errors -> exit 1
    └── dependencies/
        ├── currency.py      # -c / --currency: load_currency
        └── number_format.py # --digits, --grouping, --decimal, --places
examples/                    # the currency files every documented command uses
tests/
├── test_app.py
└── test_readme.py           # runs every command in README.md and docs/, checking outputs
```

## Documentation

This site is built with [MkDocs](https://www.mkdocs.org) and
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). The pages are in
`docs/`, and the navigation in `mkdocs.yml`.

```text
uv run --group docs mkdocs serve          # live preview on http://127.0.0.1:8000
uv run --group docs mkdocs build --strict # what CI runs: broken links fail the build
```

Every push to `main` builds the site and publishes it to GitHub Pages
(`.github/workflows/docs.yml`).

### Outputs in the docs are tested

`tests/test_readme.py` runs every `arapy` command in the ` ```bash ` blocks of
`README.md` and `docs/**/*.md`, from the `examples/` folder, and compares the output
with the one shown:

- the comment after the command: `arapy words 2  # اثنان`;
- or the `# ` lines right below it, for several lines of output;
- a command with neither only has to succeed (like `arapy date`, which prints today).

So a ` ```bash ` block must only hold commands that work from `examples/`. Pipes, other
shells and failing commands go in ` ```text ` or ` ```powershell ` blocks, which are not
run.

## Releasing

Push a `v*` tag. The release workflow builds the package, publishes it to PyPI with
trusted publishing, and creates a GitHub release.
