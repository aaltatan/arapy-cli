# Numbers in words

`words` writes whole numbers in Arabic words. It accepts any digit set.

```bash
arapy words 0  # صفر
arapy words 11  # أحد عشر
arapy words 12  # اثنا عشر
arapy words 21  # واحد وعشرون
arapy words 125000  # مئة وخمسة وعشرون ألفًا
arapy words 3000000  # ثلاثة ملايين
arapy words 1002003004  # مليار ومليونان وثلاثة آلاف وأربعة
arapy words ٩٩٩  # تسعمئة وتسعة وتسعون
```

## Hundreds, thousands, millions

The counted words follow Arabic number grammar:

```bash
arapy words 100 200 1000 2000 1000000
# مئة
# مئتان
# ألف
# ألفان
# مليون
arapy words 1500 2500000
# ألف وخمسمئة
# مليونان وخمسمئة ألف
```

| Count | Form | Example |
|-------|------|---------|
| 1 | singular | ألف، مليون |
| 2 | dual | ألفان، مليونان |
| 3 to 10 | plural | ثلاثة آلاف، ثلاثة ملايين |
| 11 to 99 | accusative singular (التمييز) | خمسة وعشرون ألفًا |
| 100 and up | singular | مئة ألف |

## Negative numbers

```bash
arapy words -- -15  # سالب خمسة عشر
```

`--` before a negative number stops it from being read as an option.

## مئة or مائة

Modern spelling is مئة. `--alef` writes the older مائة, still common on official
documents:

```bash
arapy words 300  # ثلاثمئة
arapy words 300 --alef  # ثلاثمائة
```

## Grammatical case

Numbers change their ending with their place in the sentence. `--case` picks it:

| `--case` | Arabic | Use after |
|----------|--------|-----------|
| `nominative` (default) | الرفع | a subject: «المبلغ ...» |
| `accusative` | النصب | a verb's object: «دفعتُ ...» |
| `genitive` | الجر | a preposition: «بمبلغ ...» |

```bash
arapy words 12  # اثنا عشر
arapy words 12 --case accusative  # اثني عشر
arapy words 22 --case genitive  # اثنين وعشرين
```

The case mostly shows in 2 and 12 (اثنان، اثني) and in the tens (عشرون، عشرين).
Other numbers keep the same spelling, since short vowels are not written.

## Fractions need a currency

A number with decimals only makes sense in a unit:

```text
$ arapy words 1.5
Error in '1.5': A fraction needs a currency unit: '1.5'
```

Give a currency file to write it, see [Currencies and amounts](currencies.md):

```bash
arapy words 1.5 -c usd.json  # دولار أمريكي واحد وخمسون سنتًا
```

## Next

- Amounts in a currency: [Currencies and amounts](currencies.md).
- The other direction: [Reading words back](parse.md).
- Every grammar rule, with sources: the arapy library's
  [Words guide](https://aaltatan.github.io/arapy/guide/words/).
