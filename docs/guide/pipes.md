# Many values and pipes

## Many arguments

Every command takes several values, and prints one result per line, in order:

```bash
arapy words 1 2 3 -c syp.json
# ليرة سورية واحدة
# ليرتان سوريتان
# ثلاث ليرات سورية
```

## stdin

With **no** values, a command reads them from stdin, one per line. Blank lines are
skipped, and spaces around each line are trimmed.

=== "PowerShell"

    ```powershell
    Get-Content amounts.txt | arapy words -c syp.json --prefix فقط --suffix "لا غير"
    Get-Content names.txt | arapy sort > sorted.txt
    Get-Clipboard | arapy words -c usd.json | Set-Clipboard
    ```

=== "bash"

    ```text
    arapy words -c syp.json --prefix فقط --suffix "لا غير" < amounts.txt
    arapy sort < names.txt > sorted.txt
    cut -d, -f3 invoices.csv | arapy money -c usd.json
    ```

The `Get-Clipboard` line converts a column copied from Excel and puts the words back on
the clipboard, ready to paste into the next column.

`date` with no values and nothing on stdin writes today. The other commands then ask
for values:

```text
Invalid value: Give one or more values, or pipe them in, one per line
```

## UTF-8

Input and output are always **UTF-8**, also in Windows pipes and redirects, so Arabic
survives `> file.txt` and `| Set-Clipboard`. Files you pipe in must be UTF-8 too: in
Excel, save as **CSV UTF-8**; in Notepad, pick **UTF-8** when saving.

## In scripts

| Exit code | Meaning |
|-----------|---------|
| `0` | Every value was converted |
| `1` | A value was wrong; the message names it |
| `2` | A bad option, or options that do not go together |

The run stops at the **first** bad value. The lines before it are already printed, so
when a whole file must convert, check the exit code:

```powershell
Get-Content amounts.txt | arapy words -c syp.json > words.txt
if ($LASTEXITCODE -ne 0) { throw "arapy failed" }
```
