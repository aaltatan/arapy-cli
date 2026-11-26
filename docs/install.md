# Installation

arapy-cli needs **Python 3.12 or newer**. Install it as a tool:

=== "uv"

    ```text
    uv tool install arapy-cli
    ```

=== "pipx"

    ```text
    pipx install arapy-cli
    ```

=== "pip"

    ```text
    pip install arapy-cli
    ```

This installs the `arapy` command, with Hijri date support included.

```text
$ arapy --version
arapy-cli 0.1.0 (arapy 0.1.0)
```

## Shell completion

```text
arapy --install-completion
```

Restart the shell after installing it.

## Upgrade and uninstall

=== "uv"

    ```text
    uv tool upgrade arapy-cli
    uv tool uninstall arapy-cli
    ```

=== "pipx"

    ```text
    pipx upgrade arapy-cli
    pipx uninstall arapy-cli
    ```

## Arabic in the terminal

arapy reads and writes **UTF-8** everywhere, including Windows pipes and redirects.
How Arabic **looks** depends on your terminal:

- **Windows Terminal** and most Linux and macOS terminals draw Arabic letters joined.
  Right-to-left lines may still show in left-to-right order; the text itself is correct,
  and pastes correctly into Word, Excel or a browser.
- The old Windows console (`conhost`) may show boxes. Use Windows Terminal, or redirect
  to a file (`> out.txt`) and open it in an editor.

## The example files

The commands in this documentation run from the
[`examples/`](https://github.com/aaltatan/arapy-cli/tree/main/examples) folder, where the
currency files are:

```text
git clone https://github.com/aaltatan/arapy-cli
cd arapy-cli/examples
```

| File | Currency |
|------|----------|
| `syp.json` | Syrian pound: ليرة سورية، قرش |
| `usd.json` | US dollar: دولار أمريكي، سنت |
| `eur.json` | Euro: يورو، سنت |
| `sar.json` | Saudi riyal: ريال سعودي، هللة |
| `aed.json` | UAE dirham: درهم إماراتي، فلس |
| `egp.json` | Egyptian pound: جنيه مصري، قرش |
| `jod.json` | Jordanian dinar: دينار أردني، فلس (1000 per dinar) |
| `kwd.json` | Kuwaiti dinar: دينار كويتي، فلس (1000 per dinar) |

Every command shown with its output (`arapy words 2  # اثنان`) is run by the test suite,
and the output is checked.
