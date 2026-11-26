# Normalizing and sorting

## Normalize

The same Arabic word can be typed in many ways: أحمد or احمد, فاطمة or فاطمه, with or
without tashkeel, with tatweel (ـ) for stretching. To a computer they are all different.
`normalize` folds them into one form, ready for **search, matching and
de-duplication**:

```bash
arapy normalize "أَحْمَدُ   الطَّيِّبَة"  # احمد الطيبه
arapy normalize "إسـلام مؤمن ٢٠٢٦"  # اسلام مومن 2026
arapy normalize "مُحَمَّدٌ"  # محمد
arapy normalize "أبو الفضل"  # ابو الفضل
```

| Change | Example |
|--------|---------|
| أ إ آ → ا | أحمد → احمد |
| ة → ه | الطيبة → الطيبه |
| ؤ → و | مؤمن → مومن |
| tashkeel removed | مُحَمَّدٌ → محمد |
| tatweel removed | إسـلام → اسلام |
| Arabic and Persian digits → Latin | ٢٠٢٦ → 2026 |
| invisible characters removed, spaces collapsed | `أحمد   الطيبة` → `احمد الطيبه` |

!!! warning "For comparing, not for printing"
    The normalized text is a **key** to compare and search with. Keep the original for
    display: «مومن» is not how the name is written.

### Names

`--names` also splits compound names, so «عبدالله» and «عبد الله» match:

```bash
arapy normalize "عبدالله  أبوبكر" --names  # عبد الله ابو بكر
arapy normalize "فاطمة الزهراء" --names  # فاطمه الزهراء
```

## Sort

`sort` follows **Arabic alphabetical order**, not the order of the characters' codes.
Sorting by code puts all the hamza forms in odd places; a dictionary puts آمنة with
أحمد:

```bash
arapy sort يوسف أحمد زينب آمنة باسل إياد
# أحمد
# آمنة
# إياد
# باسل
# زينب
# يوسف
```

```bash
arapy sort "عمر" "علي" "عائشة" "أسامة" "إبراهيم"
# إبراهيم
# أسامة
# عائشة
# علي
# عمر
```

`--reverse` (`-r`) sorts descending:

```bash
arapy sort يوسف أحمد زينب --reverse
# يوسف
# زينب
# أحمد
```

To sort a file, one name per line:

```text
arapy sort < names.txt > sorted.txt
```

See [Many values and pipes](pipes.md), and the
[de-duplication recipe](../recipes.md#de-duplicate-a-list-of-names).
