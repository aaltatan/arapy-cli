# Money and numbers in digits

## Money

`money` writes an amount in digits with the currency symbol. Arabic digits and
separators (٬ for thousands, ٫ for decimals) are the default, and the decimals always
match the subunit:

```bash
arapy money 12500 -c syp.json  # ١٢٬٥٠٠ ل.س
arapy money 1250.5 -c syp.json  # ١٬٢٥٠٫٥٠ ل.س
arapy money 1.5 -c kwd.json  # ١٫٥٠٠ د.ك
arapy money 1000000 -c usd.json  # ١٬٠٠٠٬٠٠٠ $
```

Latin digits and separators, for an English invoice:

```bash
arapy money 99.9 -c usd.json --digits latin --grouping , --decimal .  # 99.90 $
```

!!! note "Each option changes one thing"
    `--digits latin` changes the **digits** only; the separators stay Arabic:

    ```bash
    arapy money 0.5 -c usd.json --digits latin  # 0٫50 $
    ```

    Give `--grouping` and `--decimal` too for a fully Latin number.

`money` needs a currency:

```text
$ arapy money 5
Invalid value: money needs -c / --currency
```

## Numbers

`number` reads a number in any digit set and writes it with the digits, separators and
decimal places you choose. Latin digits with `,` and `.` are the default.

```bash
arapy number 1250000  # 1,250,000
arapy number ١٢٥٬٠٠٠٫٥  # 125,000.5
arapy number 1,250.75  # 1,250.75
arapy number 1250.5 --digits arabic --grouping ٬ --decimal ٫  # ١٬٢٥٠٫٥
arapy number ١٢٣ --digits persian  # ۱۲۳
```

### Decimal places

`--places` **pads** with zeros. It never rounds, so it refuses to drop digits:

```bash
arapy number 12 --places 2  # 12.00
arapy number 1250.5 --places 2 --grouping ""  # 1250.50
```

`--grouping ""` writes no thousands separator.

### Percent

`--percent` multiplies by 100 and adds the Arabic percent sign ٪:

```bash
arapy number 0.25 --percent --digits arabic  # ٢٥٪
arapy number 0.5 --percent --places 2  # 50.00٪
```

## Options

| Option | Default for `money` | Default for `number` | Meaning |
|--------|---------------------|----------------------|---------|
| `--digits` | `arabic` | `latin` | `latin`, `arabic` or `persian` |
| `--grouping` | `٬` | `,` | Thousands separator; `""` for none |
| `--decimal` | `٫` | `.` | Decimal mark |
| `--places` | the subunit's (2, or 3 for a ratio of 1000) | as given | Decimal places, padded with zeros |

## Ambiguous numbers

arapy reads `.` and `,` both as a decimal mark **and** as a thousands separator, so that
numbers from any source work. When a number has **one** separator followed by exactly
**three** digits, it could be either, and arapy refuses it instead of guessing:

```text
$ arapy number 1.250
Error in '1.250': Ambiguous number '1.250': '.' may be a decimal mark or a thousands separator. Pass decimal=... to say which.

$ arapy words 1,250
Error in '1,250': Ambiguous number '1,250': ',' may be a decimal mark or a thousands separator. Pass decimal=... to say which.
```

Write it so that only one reading is possible:

| Meant | Write |
|-------|-------|
| one thousand two hundred and fifty | `1250` or `1,250.00` |
| one and a quarter | `1.25` or `1.2500` |

```bash
arapy number 1.2500  # 1.2500
arapy words 1250  # ألف ومئتان وخمسون
```

A currency with a `ratio` of 1000 (Kuwaiti and Jordanian dinars) has three decimals, so
there `1.250` is read as one dinar and 250 fils.
