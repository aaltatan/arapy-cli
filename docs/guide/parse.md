# Reading words back

`words --parse` turns Arabic number words into a number: to check a cheque, to read an
amount typed in words in a form, or to import old documents.

```bash
arapy words --parse "مائة وخمسة وعشرون"  # 125
arapy words --parse "خمسة عشر"  # 15
arapy words --parse "ثَلَاثَةُ آلَافٍ"  # 3000
```

It accepts:

- مئة **and** مائة;
- every case: اثنا عشر، اثني عشر، اثنين وعشرين;
- tashkeel, or none;
- amounts in a currency, with `-c`: the unit and subunit words are read too;
- the same `--prefix` and `--suffix` as when writing.

```bash
arapy words --parse "ليرتان سوريتان" -c syp.json  # 2
arapy words --parse "سبعة وخمسون دولارًا أمريكيًا" -c usd.json  # 57
arapy words --parse "ألف ومئتان وخمسون ليرةً سوريةً وخمسون قرشًا" -c syp.json  # 1250.5
arapy words --parse "فقط سبعة آلاف وخمسمئة لا غير" --prefix فقط --suffix "لا غير"  # 7500
```

The result is in Latin digits, with a `.` for the decimal mark, ready for Excel or a
script.

A word it does not know is an error naming it:

```text
$ arapy words --parse "شيء"
Error in 'شيء': Unknown word 'شيء' in 'شيء'
```

## Round trip

Writing a number and reading it back gives the same number, so `--parse` is a good
check on words someone typed by hand:

```bash
arapy words 1002003004  # مليار ومليونان وثلاثة آلاف وأربعة
arapy words --parse "مليار ومليونان وثلاثة آلاف وأربعة"  # 1002003004
```
