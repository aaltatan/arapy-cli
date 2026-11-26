# Currency files

A currency file is a JSON object. Its keys are the arguments of the arapy library's
`Currency.create`.

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

## Keys

| Key | Required | Type | Meaning |
|-----|----------|------|---------|
| `code` | yes | text | ISO 4217 code; `money` shows it when there is no `symbol` |
| `singular` | yes | text | One unit, with its adjective: «دينار كويتي» |
| `dual` | yes | text | Two units: «ديناران كويتيان» |
| `plural` | yes | text | 3 to 10 units: «دنانير كويتية» |
| `gender` | yes | `masculine` / `feminine` | The noun's gender; the numbers agree with it |
| `subunit` | yes | object | The subunit's `singular`, `dual`, `plural` and `gender` |
| `ratio` | no | integer | Subunits per unit; `100` by default |
| `symbol` | no | text | Shown by `money`: «د.ك» |
| `many` | no | text | The form after 11 to 99 (التمييز), when adding tanween to `singular` is not right |

The `subunit` object takes the same `singular`, `dual`, `plural` and `gender` keys, and
`many` when needed.

## Writing one

1. Write the noun **with** its adjective, in the three forms people use:
   «ليرة لبنانية», «ليرتان لبنانيتان», «ليرات لبنانية».
2. Set the gender of the **noun**: ليرة is feminine; دينار، درهم، ريال، جنيه are
   masculine. The subunit has its own: قرش and فلس are masculine, هللة is feminine.
3. Set `ratio` to 1000 for currencies with 1000 subunits (Kuwaiti, Jordanian, Bahraini
   and Iraqi dinars, Omani rial).
4. Check it:

    ```text
    arapy words 1 2 3 11 100 1250.5 -c lbp.json
    ```

    and compare 11 with the form you expect after 11 to 99. If adding tanween is wrong
    for the noun (a foreign word like يورو), set `many`.

## The example files

| File | `singular` | `gender` | Subunit | `ratio` |
|------|------------|----------|---------|---------|
| `syp.json` | ليرة سورية | feminine | قرش | 100 |
| `usd.json` | دولار أمريكي | masculine | سنت | 100 |
| `eur.json` | يورو (`many`: يورو) | masculine | سنت | 100 |
| `sar.json` | ريال سعودي | masculine | هللة (feminine) | 100 |
| `aed.json` | درهم إماراتي | masculine | فلس | 100 |
| `egp.json` | جنيه مصري | masculine | قرش | 100 |
| `jod.json` | دينار أردني | masculine | فلس | 1000 |
| `kwd.json` | دينار كويتي | masculine | فلس | 1000 |

## Errors

```text
Invalid value: Currency file 'x.json' is not valid JSON: ...
Invalid value: Currency file 'x.json' is missing or has a wrong key: 'subunit'
```

A wrong `gender` value (anything but `masculine` or `feminine`) is reported the same
way.
