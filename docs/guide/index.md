# User guide

| Page | You will learn |
|------|----------------|
| [Numbers in words](words.md) | `words`: whole numbers, case, مئة or مائة, negatives |
| [Currencies and amounts](currencies.md) | Currency files, amounts with fractions, cheques |
| [Reading words back](parse.md) | `words --parse`: from words to a number |
| [Money and numbers in digits](formatting.md) | `money` and `number`: digits, separators, places, percent |
| [Digits](digits.md) | `digits`: Latin, Arabic and Persian digits |
| [Normalizing and sorting](text.md) | `normalize` and `sort` |
| [Ordinals](ordinals.md) | `ordinal`: الأول، الحادية عشرة، أولًا |
| [Dates and Hijri dates](dates.md) | `date`: Arabic month names, ordinal days, Umm al-Qura |
| [Many values and pipes](pipes.md) | Many arguments, stdin, UTF-8, exit codes in scripts |

## The commands

| Command | Alias | Does |
|---------|-------|------|
| `words` | `w` | Numbers or amounts in words; `--parse` reads words back into a number |
| `money` | `m` | Amounts in digits with the currency symbol |
| `number` | `n` | Format numbers given in any digit set; `--percent` |
| `digits` | `d` | Convert digits between Latin, Arabic and Persian |
| `normalize` | `norm` | Fold letters, drop tashkeel and tatweel |
| `sort` | `s` | Sort lines in Arabic alphabetical order |
| `ordinal` | `o` | Ordinals and list markers |
| `date` | `dt` | Write ISO dates (default: today) in Arabic, Gregorian or Hijri |

`arapy <command> --help` lists every option.

## Reading the examples

The comment after a command is its output:

```bash
arapy words 21  # واحد وعشرون
```

When there are several lines of output, they follow as `#` lines:

```bash
arapy words 1 2
# واحد
# اثنان
```

## Two rules arapy never breaks

1. **Nothing is rounded.** Amounts are exact decimals. `0.125` dollars is not quietly
   turned into 13 cents.
2. **Nothing is guessed.** `1,250` could be one thousand two hundred and fifty, or one
   and a quarter. arapy refuses it and asks you to write it unambiguously. See
   [Ambiguous numbers](formatting.md#ambiguous-numbers).
