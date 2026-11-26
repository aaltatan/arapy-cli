# Digits

Arabic text uses three digit sets:

| Set | Digits | Used in |
|-----|--------|---------|
| `latin` | 0123456789 | the Maghreb, and most software and spreadsheets |
| `arabic` | ٠١٢٣٤٥٦٧٨٩ | the Levant, Egypt, the Gulf, Iraq |
| `persian` | ۰۱۲۳۴۵۶۷۸۹ | Iran, Afghanistan, Pakistan |

`digits` converts every digit in the text and leaves everything else alone. Arabic is
the default target:

```bash
arapy digits 2026-01-05  # ٢٠٢٦-٠١-٠٥
arapy digits 2026 --to persian  # ۲۰۲۶
arapy digits "٢٠٢٦ / ۲۰۲۶" --to latin  # 2026 / 2026
arapy digits "هاتف: 0933 123 456"  # هاتف: ٠٩٣٣ ١٢٣ ٤٥٦
```

Use it for:

- **printing** phone numbers, dates and reference numbers in Arabic digits;
- **cleaning** data typed with mixed digits before importing it (`--to latin`): Excel
  and databases only read Latin digits as numbers.

Every other command already **reads** any digit set, so there is no need to convert
first: `arapy words ٩٩٩` works.
