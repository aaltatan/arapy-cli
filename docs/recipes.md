# Recipes

Real-world jobs. Commands with their output shown are run by the test suite from the
[`examples/`](https://github.com/aaltatan/arapy-cli/tree/main/examples) folder.

## Write a cheque

**Job:** the amount in words for a cheque or payment order, with «فقط ... لا غير» so
nothing can be added before or after it.

```bash
arapy words 1250.50 -c syp.json --prefix فقط --suffix "لا غير"  # فقط ألف ومئتان وخمسون ليرةً سوريةً وخمسون قرشًا لا غير
arapy money 1250.50 -c syp.json  # ١٬٢٥٠٫٥٠ ل.س
```

Many offices still write مائة on cheques:

```bash
arapy words 300 -c usd.json --alef --prefix فقط --suffix "لا غير"  # فقط ثلاثمائة دولار أمريكي لا غير
```

Check an amount someone wrote by hand by reading it back:

```bash
arapy words --parse "فقط ألف ومئتان وخمسون ليرةً سوريةً وخمسون قرشًا لا غير" -c syp.json --prefix فقط --suffix "لا غير"  # 1250.5
```

## A column of amounts from Excel

**Job:** an invoice sheet has a column of totals, and the next column needs them in
words.

1. Select the totals in Excel and copy them (++ctrl+c++).
2. Run:

    ```powershell
    Get-Clipboard | arapy words -c usd.json --prefix فقط --suffix "لا غير" | Set-Clipboard
    ```

3. Click the first cell of the next column and paste (++ctrl+v++).

Each total becomes one line, in the same order, so the rows stay aligned. Excel copies
numbers as you see them, so format the column without thousands separators, or with two
decimals (`1,250.00`), to avoid [ambiguous numbers](guide/formatting.md#ambiguous-numbers).

## Salary certificates

**Job:** a «شهادة راتب» states the salary in digits and in words.

```bash
arapy money 1500000 -c syp.json  # ١٬٥٠٠٬٠٠٠ ل.س
arapy words 1500000 -c syp.json --prefix فقط --suffix "لا غير"  # فقط مليون وخمسمئة ألف ليرة سورية لا غير
```

For a certificate per employee, [templify](https://aaltatan.github.io/templify/) fills a
Word or Markdown template from an Excel sheet, and has the same words in its templates:
`{{ salary | ar.to_words }}`.

## A letter dated in both calendars

**Job:** official letters in the Levant and the Gulf carry the Gregorian and the Hijri
date.

```bash
arapy date 2026-01-05 -f "%d %B %Y م"  # 05 كانون الثاني 2026 م
arapy date 2026-01-05 --hijri -f "%d %B %Y هـ"  # 16 رجب 1447 هـ
```

For today's letter, leave the date out:

```text
arapy date -f "%d %B %Y م"
arapy date --hijri -f "%d %B %Y هـ"
```

In Egypt and the Gulf, use the month names people there know:

```bash
arapy date 2026-01-05 -f "%d %B %Y م" --months egyptian  # 05 يناير 2026 م
```

## Numbered clauses

**Job:** a contract or the minutes of a meeting lists its points as أولًا، ثانيًا، ...

```bash
arapy ordinal 1 2 3 4 5 --adverb
# أولًا
# ثانيًا
# ثالثًا
# رابعًا
# خامسًا
```

For articles: «المادة الأولى، المادة الثانية»:

```bash
arapy ordinal 1 2 11 --feminine
# الأولى
# الثانية
# الحادية عشرة
```

## De-duplicate a list of names

**Job:** a contact list was typed by several people: «أحمد» and «احمد», «عبدالله» and
«عبد الله». Find the names that are really the same person.

`normalize --names` gives each name a **key**; names with the same key match.

```bash
arapy normalize --names "عبدالله" "عبد الله" "أحمد" "احمد"
# عبد الله
# عبد الله
# احمد
# احمد
```

For a whole file, in PowerShell:

```powershell
$names = Get-Content names.txt
$keys = $names | arapy normalize --names
0..($names.Count - 1) |
    ForEach-Object { [pscustomobject]@{ Key = $keys[$_]; Name = $names[$_] } } |
    Group-Object Key | Where-Object Count -gt 1 |
    ForEach-Object { $_.Group.Name -join "  =  " }
```

Each output line lists the spellings of one name. Keep one, and fix the others.

## Sort a class list

```bash
arapy sort يوسف أحمد زينب آمنة باسل إياد
# أحمد
# آمنة
# إياد
# باسل
# زينب
# يوسف
```

From a file, keeping the result:

```text
arapy sort < students.txt > students-sorted.txt
```

## Arabic digits for printing

**Job:** a price list or a phone number in Arabic digits, for a sign or a printed
form.

```bash
arapy digits "هاتف: 0933 123 456"  # هاتف: ٠٩٣٣ ١٢٣ ٤٥٦
arapy number 1250000 --digits arabic --grouping ٬  # ١٬٢٥٠٬٠٠٠
```

And the other way, before importing typed data into Excel or a database:

```bash
arapy digits "٠٩٣٣١٢٣٤٥٦" --to latin  # 0933123456
```

## Many currencies on one invoice

**Job:** a regional invoice shows the total in the customer's currency.

```bash
arapy words 1750.25 -c sar.json  # ألف وسبعمئة وخمسون ريالًا سعوديًا وخمس وعشرون هللةً
arapy words 1750.25 -c aed.json  # ألف وسبعمئة وخمسون درهمًا إماراتيًا وخمسة وعشرون فلسًا
arapy words 1750.25 -c egp.json  # ألف وسبعمئة وخمسون جنيهًا مصريًا وخمسة وعشرون قرشًا
arapy words 1750.25 -c jod.json  # ألف وسبعمئة وخمسون دينارًا أردنيًا ومئتان وخمسون فلسًا
```

A currency that is not in `examples/` takes five minutes to add: see
[Currency files](reference/currency-files.md).
