# Ordinals

`ordinal` writes ordinal numbers from 1 to 100: the first, the eleventh, the
twenty-first.

```bash
arapy ordinal 1  # الأول
arapy ordinal 10  # العاشر
arapy ordinal 12  # الثاني عشر
arapy ordinal 21  # الحادي والعشرون
arapy ordinal 100  # المئة
```

## Feminine

`--feminine` (`-f`) agrees with a feminine noun: «المادة الثالثة», «الدورة الحادية
عشرة»:

```bash
arapy ordinal 2 --feminine  # الثانية
arapy ordinal 3 --feminine  # الثالثة
arapy ordinal 11 --feminine  # الحادية عشرة
arapy ordinal 12 --feminine  # الثانية عشرة
```

## Case and definiteness

```bash
arapy ordinal 20 --case genitive  # العشرين
arapy ordinal 3 --indefinite  # ثالث
arapy ordinal 3 --indefinite --case accusative  # ثالثًا
```

| Option | Meaning |
|--------|---------|
| `--case nominative\|accusative\|genitive` | The grammatical case, as for [words](words.md#grammatical-case) |
| `--indefinite` | Without «ال»: ثالث instead of الثالث |

## List markers

`--adverb` writes the markers used for numbered points in letters, contracts and
minutes:

```bash
arapy ordinal 1 2 3 4 --adverb
# أولًا
# ثانيًا
# ثالثًا
# رابعًا
```

`--adverb` has one form, so it does not take `--feminine`, `--indefinite` or `--case`:

```text
$ arapy ordinal 5 --adverb --feminine
Invalid value: --adverb does not take --feminine, --indefinite or --case
```

## Range

Ordinals are written from 1 to 100:

```text
$ arapy ordinal 101
Error in '101': Ordinals are supported from 1 to 100, not 101
```
