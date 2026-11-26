---
hide:
  - navigation
---

# arapy-cli

**Arabic numbers, words and dates, from the command line.**

Amounts in words (تفقيط) with correct gender, dual, plural and case; Arabic and Persian
digits; number and money formatting; text normalization; Arabic alphabetical sorting;
ordinals; and Gregorian and Hijri dates.

```bash
arapy words 1250.50 -c syp.json --prefix فقط --suffix "لا غير"  # فقط ألف ومئتان وخمسون ليرةً سوريةً وخمسون قرشًا لا غير
arapy date 2026-01-05 --hijri -f "%A %d %B %Y هـ"  # الاثنين 16 رجب 1447 هـ
arapy money 12500 -c syp.json  # ١٢٬٥٠٠ ل.س
```

A thin front end for the [arapy](https://aaltatan.github.io/arapy/) library: the same
exact `Decimal` arithmetic (nothing is ever rounded) and the same grammar.

## Why arapy-cli

<div class="grid cards" markdown>

-   :material-cash-check: **تفقيط that reads right**

    ---

    The number agrees with the currency's gender, 1 and 2 follow the noun, 11 to 99
    take the accusative singular, and fractions are written in the subunit.

-   :material-swap-horizontal: **Both ways**

    ---

    `--parse` reads words back into a number: مئة or مائة, any case, with or without
    tashkeel.

-   :material-numeric: **Every digit set**

    ---

    Read and write Latin, Arabic (٠١٢) and Persian (۰۱۲) digits, with your own
    separators.

-   :material-sort-alphabetical-ascending: **Arabic order**

    ---

    Sort names the way a dictionary does, and normalize spellings (أ إ آ، ة ه) for
    search and de-duplication.

-   :material-calendar-month-outline: **Gregorian and Hijri**

    ---

    Levantine, Egyptian or Maghrebi month names, ordinal days, and the Umm al-Qura
    Hijri calendar.

-   :material-pipe: **Made for pipes**

    ---

    Every command takes many values, or one per line on stdin, so a whole Excel column
    converts in one go. UTF-8 in and out, also on Windows.

</div>

## A taste

=== "Cheques"

    ```bash
    arapy words 7500 --prefix فقط --suffix "لا غير"  # فقط سبعة آلاف وخمسمئة لا غير
    ```

=== "Many currencies"

    ```bash
    arapy words 1750.25 -c sar.json  # ألف وسبعمئة وخمسون ريالًا سعوديًا وخمس وعشرون هللةً
    arapy words 15 -c eur.json  # خمسة عشر يورو
    ```

=== "Sorting"

    ```bash
    arapy sort يوسف أحمد زينب آمنة
    # أحمد
    # آمنة
    # زينب
    # يوسف
    ```

=== "Ordinals"

    ```bash
    arapy ordinal 1 2 3 --adverb
    # أولًا
    # ثانيًا
    # ثالثًا
    ```

## Where to go next

- New here? [Install it](install.md), then follow the [user guide](guide/index.md).
- Have a job to do? See the [recipes](recipes.md): cheques, a column of amounts from
  Excel, payroll certificates, de-duplicating names, dated letters, numbered clauses.
- Looking something up? The [reference](reference/index.md) lists every command,
  option, currency key, date directive and error.
- Writing Python? Use the [arapy library](https://aaltatan.github.io/arapy/) directly.
