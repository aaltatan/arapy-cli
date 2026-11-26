# Currencies and amounts

arapy ships **no currencies**: every country, and every company, writes its money a
little differently. You define the ones you use once, in a small JSON file, and pass it
with `-c`.

## A currency file

[`examples/syp.json`](https://github.com/aaltatan/arapy-cli/blob/main/examples/syp.json):

```json
{
    "code": "SYP",
    "singular": "ليرة سورية",
    "dual": "ليرتان سوريتان",
    "plural": "ليرات سورية",
    "gender": "feminine",
    "symbol": "ل.س",
    "subunit": {"singular": "قرش", "dual": "قرشان", "plural": "قروش", "gender": "masculine"}
}
```

| Key | Required | Meaning |
|-----|----------|---------|
| `code` | yes | ISO code; shown by `money` when there is no `symbol` |
| `singular`, `dual`, `plural` | yes | The noun with its adjective: ليرة سورية، ليرتان سوريتان، ليرات سورية |
| `gender` | yes | `masculine` or `feminine`: the numbers agree with it |
| `subunit` | yes | The subunit's `singular`, `dual`, `plural` and `gender` (قرش، سنت، فلس، هللة) |
| `ratio` | no | Subunits per unit, `100` by default; `1000` for dinars with فلس |
| `symbol` | no | ل.س، $، د.ك |
| `many` | no | The form after 11 to 99, when the derived one is not right (see [Euro](#the-many-key)) |

The full list is in [Currency files](../reference/currency-files.md).

## Amounts in words

```bash
arapy words 1 -c syp.json  # ليرة سورية واحدة
arapy words 2 -c syp.json  # ليرتان سوريتان
arapy words 3 -c syp.json  # ثلاث ليرات سورية
arapy words 15 -c syp.json  # خمس عشرة ليرةً سوريةً
arapy words 100 -c usd.json  # مئة دولار أمريكي
arapy words 1250.50 -c syp.json  # ألف ومئتان وخمسون ليرةً سوريةً وخمسون قرشًا
arapy words 0.75 -c usd.json  # خمسة وسبعون سنتًا
```

What arapy does for you:

| Rule | Example |
|------|---------|
| 1 and 2 follow the noun, as adjectives | ليرة سورية واحدة، ليرتان سوريتان |
| 3 to 10 take the **opposite** gender of the noun | ثلاث ليرات (feminine noun), ثلاثة دولارات (masculine noun) |
| 3 to 10 take the plural noun | ثلاث ليرات سورية |
| 11 to 99 take the accusative singular, with tanween | خمس عشرة ليرةً سوريةً |
| 100 and up take the genitive singular | مئة دولار أمريكي |
| The fraction is written in the subunit, with its own gender | وخمسون قرشًا، وخمس وعشرون هللةً |
| No units, only subunits | خمسة وسبعون سنتًا |

The case works with currencies too:

```bash
arapy words 2 -c syp.json --case genitive  # ليرتين سوريتين
```

## More currencies

The [`examples/`](https://github.com/aaltatan/arapy-cli/tree/main/examples) folder has
eight ready files:

=== "Saudi riyal"

    ```bash
    arapy words 1750.25 -c sar.json  # ألف وسبعمئة وخمسون ريالًا سعوديًا وخمس وعشرون هللةً
    arapy words 3 -c sar.json  # ثلاثة ريالات سعودية
    ```

    The subunit هللة is feminine, so 25 is «خمس وعشرون».

=== "UAE dirham"

    ```bash
    arapy words 1750.25 -c aed.json  # ألف وسبعمئة وخمسون درهمًا إماراتيًا وخمسة وعشرون فلسًا
    arapy words 3 -c aed.json  # ثلاثة دراهم إماراتية
    ```

=== "Egyptian pound"

    ```bash
    arapy words 1750.25 -c egp.json  # ألف وسبعمئة وخمسون جنيهًا مصريًا وخمسة وعشرون قرشًا
    arapy words 2 -c egp.json  # جنيهان مصريان
    ```

=== "Jordanian dinar"

    ```bash
    arapy words 1750.25 -c jod.json  # ألف وسبعمئة وخمسون دينارًا أردنيًا ومئتان وخمسون فلسًا
    arapy words 0.5 -c jod.json  # خمسمئة فلس
    ```

    `"ratio": 1000`: half a dinar is 500 fils.

=== "Kuwaiti dinar"

    ```bash
    arapy words 1.500 -c kwd.json  # دينار كويتي واحد وخمسمئة فلس
    ```

=== "Euro"

    ```bash
    arapy words 1 2 3 15 -c eur.json
    # يورو واحد
    # يوروان
    # ثلاثة يوروهات
    # خمسة عشر يورو
    ```

### The `many` key

After 11 to 99, Arabic uses the accusative singular: «خمسة عشر دولارًا». arapy builds it
from `singular` by adding tanween. Some nouns do not take it, like the foreign word
يورو, so [`eur.json`](https://github.com/aaltatan/arapy-cli/blob/main/examples/eur.json)
gives the form itself:

```json
{"singular": "يورو", "dual": "يوروان", "plural": "يوروهات", "many": "يورو", "...": "..."}
```

## Cheques and payment orders

`--prefix` and `--suffix` wrap the words, as on cheques, receipts and payment orders:

```bash
arapy words 7500 --prefix فقط --suffix "لا غير"  # فقط سبعة آلاف وخمسمئة لا غير
arapy words 1250.50 -c syp.json --prefix فقط --suffix "لا غير"  # فقط ألف ومئتان وخمسون ليرةً سوريةً وخمسون قرشًا لا غير
```

Quote a prefix or suffix with a space in it.

## Exact amounts

Amounts are exact decimals, never rounded. More decimal places than the subunit has is
an error, not a rounding:

```text
$ arapy words 10.0051 -c usd.json
Error in '10.0051': '10.0051' has more decimal places than USD subunits allow
```

Exactly **three** decimals are refused for 100-subunit currencies, because `1.250`
could also be one thousand two hundred and fifty (see
[Ambiguous numbers](formatting.md#ambiguous-numbers)). With a ratio of 1000, three
decimals are the subunit, so they are read as decimals:

```bash
arapy words 1.250 -c kwd.json  # دينار كويتي واحد ومئتان وخمسون فلسًا
arapy words 10.05 -c usd.json  # عشرة دولارات أمريكية وخمسة سنتات
```
