# arapy-cli

Arabic numbers, words and dates from the command line: amounts in words (تفقيط), Arabic and
Persian digits, number formatting, text normalization, alphabetical sorting, ordinals, and
Gregorian and Hijri dates.

A thin front end for the [arapy](https://pypi.org/project/arapy/) library: the same exact
`Decimal` arithmetic (nothing is ever rounded) and the same grammar (gender agreement, dual and
plural forms, case endings and tanween).

```text
uv tool install arapy-cli
pipx install arapy-cli
```

## Contents

- [Commands](#commands)
- [Amounts in words (تفقيط)](#amounts-in-words-تفقيط)
  - [Numbers](#numbers)
  - [Money](#money)
  - [Cheques](#cheques)
  - [Reading words back into numbers](#reading-words-back-into-numbers)
- [Currencies](#currencies)
- [Formatting money](#formatting-money)
- [Formatting numbers](#formatting-numbers)
- [Digits](#digits)
- [Normalization](#normalization)
- [Sorting](#sorting)
- [Ordinals](#ordinals)
- [Dates](#dates)
  - [Hijri dates](#hijri-dates)
- [Many values at once](#many-values-at-once)
- [Errors](#errors)
- [Development](#development)

## Commands

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

`arapy <command> --help` lists every option. The comment after each command below is its output;
the examples run from the [examples](examples) folder, where the currency files live, and the test
suite checks them all.

## Amounts in words (تفقيط)

### Numbers

`words` takes whole numbers in any digit set:

```bash
arapy words 0  # صفر
arapy words 11  # أحد عشر
arapy words 12  # اثنا عشر
arapy words 21  # واحد وعشرون
arapy words 125000  # مئة وخمسة وعشرون ألفًا
arapy words 3000000  # ثلاثة ملايين
arapy words 1002003004  # مليار ومليونان وثلاثة آلاف وأربعة
arapy words ٩٩٩  # تسعمئة وتسعة وتسعون
arapy words -- -15  # سالب خمسة عشر
```

`--` before a negative number stops it being read as an option.

Choose the hundreds spelling and the grammatical case:

```bash
arapy words 300 --alef  # ثلاثمائة
arapy words 12 --case accusative  # اثني عشر
arapy words 22 --case genitive  # اثنين وعشرين
```

### Money

Give a [currency file](#currencies) with `-c`. Number words agree with the currency's gender, 1 and
2 follow the noun as adjectives, and fractions are written in subunit words:

```bash
arapy words 1 -c syp.json  # ليرة سورية واحدة
arapy words 2 -c syp.json  # ليرتان سوريتان
arapy words 3 -c syp.json  # ثلاث ليرات سورية
arapy words 15 -c syp.json  # خمس عشرة ليرةً سوريةً
arapy words 100 -c usd.json  # مئة دولار أمريكي
arapy words 1250.50 -c syp.json  # ألف ومئتان وخمسون ليرةً سوريةً وخمسون قرشًا
arapy words 0.75 -c usd.json  # خمسة وسبعون سنتًا
arapy words 1.500 -c kwd.json  # دينار كويتي واحد وخمسمئة فلس
arapy words 2 -c syp.json --case genitive  # ليرتين سوريتين
```

### Cheques

`--prefix` and `--suffix` wrap the words, as on cheques and payment orders:

```bash
arapy words 7500 --prefix فقط --suffix "لا غير"  # فقط سبعة آلاف وخمسمئة لا غير
arapy words 1250.50 -c syp.json --prefix فقط --suffix "لا غير"  # فقط ألف ومئتان وخمسون ليرةً سوريةً وخمسون قرشًا لا غير
```

### Reading words back into numbers

`--parse` accepts مئة and مائة, every case, tashkeel, and the same prefix and suffix:

```bash
arapy words --parse "مائة وخمسة وعشرون"  # 125
arapy words --parse "ثَلَاثَةُ آلَافٍ"  # 3000
arapy words --parse "ألف ومئتان وخمسون ليرةً سوريةً وخمسون قرشًا" -c syp.json  # 1250.5
arapy words --parse "فقط سبعة آلاف وخمسمئة لا غير" --prefix فقط --suffix "لا غير"  # 7500
```

## Currencies

arapy ships no currencies: you define the ones you use once, in a JSON file, and pass it with
`-c`. The keys are the arguments of arapy's `Currency.create`. Three ready files are in
[examples](examples): [syp.json](examples/syp.json), [usd.json](examples/usd.json) and
[kwd.json](examples/kwd.json).

```json
{
    "code": "KWD",
    "singular": "دينار كويتي",
    "dual": "ديناران كويتيان",
    "plural": "دنانير كويتية",
    "gender": "masculine",
    "ratio": 1000,
    "symbol": "د.ك",
    "subunit": {"singular": "فلس", "dual": "فلسان", "plural": "فلوس", "gender": "masculine"}
}
```

| Key | Required | Meaning |
|-----|----------|---------|
| `code` | yes | Shown by `money` when there is no `symbol` |
| `singular`, `dual`, `plural` | yes | The noun with its adjective: ليرة سورية، ليرتان سوريتان، ليرات سورية |
| `gender` | yes | `masculine` or `feminine` |
| `subunit` | yes | `singular`, `dual`, `plural` and `gender` of the subunit (قرش، سنت، فلس) |
| `ratio` | no | Subunits per unit, default `100` |
| `symbol` | no | ل.س، $، د.ك |
| `many` | no | The form after 11–99 (التمييز) when the derived one («ليرةً سوريةً») is not right |

## Formatting money

`money` writes the amount in digits with the currency symbol. Arabic digits and separators are the
default:

```bash
arapy money 12500 -c syp.json  # ١٢٬٥٠٠ ل.س
arapy money 1250.5 -c syp.json  # ١٬٢٥٠٫٥٠ ل.س
arapy money 1.5 -c kwd.json  # ١٫٥٠٠ د.ك
arapy money 99.9 -c usd.json --digits latin --grouping , --decimal .  # 99.90 $
```

## Formatting numbers

`number` reads a number in any digit set and writes it with the digits, separators and decimal
places you choose. It pads, but never rounds:

```bash
arapy number 1250000  # 1,250,000
arapy number ١٢٥٬٠٠٠٫٥  # 125,000.5
arapy number 1,250.75  # 1,250.75
arapy number 1250.5 --digits arabic --grouping ٬ --decimal ٫  # ١٬٢٥٠٫٥
arapy number 1250.5 --places 2 --grouping ""  # 1250.50
arapy number 0.25 --percent --digits arabic  # ٢٥٪
arapy number 0.5 --percent --places 2  # 50.00٪
```

`--grouping ""` writes no thousands separator.

## Digits

`digits` converts every digit in the text and leaves the rest alone. Arabic is the default target:

```bash
arapy digits 2026-01-05  # ٢٠٢٦-٠١-٠٥
arapy digits 2026 --to persian  # ۲۰۲۶
arapy digits "٢٠٢٦ / ۲۰۲۶" --to latin  # 2026 / 2026
```

## Normalization

`normalize` folds the letters people write in different ways (أ إ آ ← ا، ة ← ه، ؤ ← و), and
removes tashkeel, tatweel, invisible characters and extra spaces, ready for search and matching.
`--names` also splits compound names:

```bash
arapy normalize "أَحْمَدُ   الطَّيِّبَة"  # احمد الطيبه
arapy normalize "إسـلام مؤمن ٢٠٢٦"  # اسلام مومن 2026
arapy normalize "عبدالله  أبوبكر" --names  # عبد الله ابو بكر
```

## Sorting

`sort` follows Arabic alphabetical order, not code point order, which puts آمنة before أحمد:

```bash
arapy sort يوسف أحمد زينب آمنة باسل إياد
# أحمد
# آمنة
# إياد
# باسل
# زينب
# يوسف

arapy sort يوسف أحمد زينب --reverse
# يوسف
# زينب
# أحمد
```

## Ordinals

```bash
arapy ordinal 1  # الأول
arapy ordinal 10  # العاشر
arapy ordinal 21  # الحادي والعشرون
arapy ordinal 100  # المئة
arapy ordinal 3 --feminine  # الثالثة
arapy ordinal 11 --feminine  # الحادية عشرة
arapy ordinal 20 --case genitive  # العشرين
arapy ordinal 3 --indefinite  # ثالث
arapy ordinal 3 --indefinite --case accusative  # ثالثًا
```

`--adverb` writes list markers:

```bash
arapy ordinal 1 2 3 4 --adverb
# أولًا
# ثانيًا
# ثالثًا
# رابعًا
```

## Dates

`date` takes ISO dates (`YYYY-MM-DD`, in any digit set) and writes them in Arabic. With no date it
writes today:

```bash
arapy date 2026-01-05  # الاثنين 05 كانون الثاني 2026
arapy date 2026-01-05 -f "%A %O من %B %Y"  # الاثنين الخامس من كانون الثاني 2026
arapy date 2026-01-05 --digits arabic  # الاثنين ٠٥ كانون الثاني ٢٠٢٦
arapy date 2026-01-05 -f %d/%m/%Y --digits persian  # ۰۵/۰۱/۲۰۲۶
arapy date
```

Four month-name styles, `levant` by default:

```bash
arapy date 2026-01-05 -f %B --months egyptian  # يناير
arapy date 2026-01-05 -f %B --months maghreb  # جانفي
arapy date 2026-01-05 -f %B --months levant_with_egyptian  # كانون الثاني (يناير)
```

| Directive | Meaning | Example |
|-----------|---------|---------|
| `%A`, `%a` | weekday name | الاثنين |
| `%B`, `%b` | month name | كانون الثاني |
| `%d` | day, two digits | 05 |
| `%O` | ordinal day | الخامس |
| `%m` | month, two digits | 01 |
| `%Y` / `%y` | year, four / two digits | 2026 / 26 |
| `%j` | day of the year | 005 |

### Hijri dates

`--hijri` converts to the Umm al-Qura calendar:

```bash
arapy date 2026-01-05 --hijri -f "%A %d %B %Y هـ"  # الاثنين 16 رجب 1447 هـ
arapy date 2026-01-05 --hijri -f "%O من %B %Y" --digits arabic  # السادس عشر من رجب ١٤٤٧
arapy date ٢٠٢٦-٠٢-١٨ --hijri  # الأربعاء 01 رمضان 1447
arapy date --hijri
```

## Many values at once

Every command takes several values and prints one result per line:

```bash
arapy words 1 2 3 -c syp.json
# ليرة سورية واحدة
# ليرتان سوريتان
# ثلاث ليرات سورية
```

With no values, it reads them from stdin, one per line (blank lines are skipped). Copy a column
from Excel into a file, or pipe it from another tool:

```text
arapy sort < names.txt > sorted.txt
cat amounts.txt | arapy words -c syp.json --prefix فقط --suffix "لا غير"
Get-Content dates.txt | arapy date --hijri          # PowerShell
```

Input and output are always UTF-8, also in Windows pipes and redirects.

## Errors

Bad input stops with a red message naming the value, and exit code 1; a bad option, or two that do
not go together, exit with code 2:

```text
$ arapy words 10.5
Error in '10.5': A fraction needs a currency unit: '10.5'

$ arapy date 05/01/2026
Error: '05/01/2026' is not an ISO date (YYYY-MM-DD)

$ arapy money 5
Invalid value: money needs -c / --currency
```

arapy never guesses: `0.125` or `1,250` could be a decimal or a number with a thousands separator,
so it refuses them. Write `0.1250` or `1250` instead.

## Development

```text
uv sync
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run mypy --strict src tests
```
