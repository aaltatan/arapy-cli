# Errors and exit codes

| Exit | Meaning |
|------|---------|
| `0` | Every value was converted |
| `1` | A value was wrong: the message names it, in red, on stderr |
| `2` | A bad option, or options that do not go together |

The run stops at the first bad value; lines for the values before it are already
printed.

## Values (exit code 1)

| Message | Fix |
|---------|-----|
| `Error in '1.5': A fraction needs a currency unit: '1.5'` | Give `-c` with a currency file |
| `Error in '1,250': Ambiguous number '1,250': ',' may be a decimal mark or a thousands separator. ...` | Write `1250`, `1,250.00` or `1.25`: see [Ambiguous numbers](../guide/formatting.md#ambiguous-numbers) |
| `Error in '10.0051': '10.0051' has more decimal places than USD subunits allow` | The subunit has 2 decimals (3 for a ratio of 1000) |
| `Error in 'abc': Not a valid number: 'abc'` | A number in any digit set |
| `Error in '1.25': '1.25' has more than 1 decimal places` | `--places` pads, it never rounds: give more places |
| `Error in 'شيء': Unknown word 'شيء' in 'شيء'` | `--parse` only reads number and currency words; add `--prefix` / `--suffix` for the rest |
| `Error in '101': Ordinals are supported from 1 to 100, not 101` | Ordinals go from 1 to 100 |
| `Error: 'x' is not a whole number` | `ordinal` takes whole numbers |
| `Error: '05/01/2026' is not an ISO date (YYYY-MM-DD)` | Write `2026-01-05`; also for impossible dates like `2026-02-30` |
| `Error in '2026-01-05': Unsupported directive %y in '%y'` | Hijri dates do not take `%y` |

## Options (exit code 2)

| Message | Fix |
|---------|-----|
| `Invalid value: money needs -c / --currency` | `money` always needs a currency |
| `Invalid value: --adverb does not take --feminine, --indefinite or --case` | List markers have one form |
| `Invalid value: --months does not work with --hijri (Hijri months have one set of names)` | Drop `--months` |
| `Invalid value: Give one or more values, or pipe them in, one per line` | Nothing was given and nothing piped in |
| `Invalid value: Currency file 'x.json' is not valid JSON: ...` | Fix the JSON |
| `Invalid value: Currency file 'x.json' is missing or has a wrong key: ...` | See [Currency files](currency-files.md) |
| `No such option: -1` | Put `--` before a negative number: `arapy words -- -15` |
