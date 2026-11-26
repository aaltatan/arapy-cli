# Dates and Hijri dates

`date` takes ISO dates (`YYYY-MM-DD`, in any digit set) and writes them in Arabic. With
no date, it writes **today**.

```bash
arapy date 2026-01-05  # الاثنين 05 كانون الثاني 2026
arapy date 2026-01-05 -f "%A %O من %B %Y"  # الاثنين الخامس من كانون الثاني 2026
arapy date 2026-01-05 --digits arabic  # الاثنين ٠٥ كانون الثاني ٢٠٢٦
arapy date 2026-01-05 -f %d/%m/%Y --digits persian  # ۰۵/۰۱/۲۰۲۶
arapy date
```

## Formats

`-f, --format` takes `strftime`-style directives. The default is `%A %d %B %Y`.

| Directive | Meaning | Example |
|-----------|---------|---------|
| `%A`, `%a` | weekday name | الاثنين |
| `%B`, `%b` | month name | كانون الثاني |
| `%d` | day, two digits | 05 |
| `%O` | ordinal day | الخامس |
| `%m` | month, two digits | 01 |
| `%Y` / `%y` | year, four / two digits | 2026 / 26 |
| `%j` | day of the year | 005 |

```bash
arapy date 2026-03-20 -f "%A %O %B %Y"  # الجمعة العشرون آذار 2026
arapy date 2026-03-20 -f "%d %b %y"  # 20 آذار 26
arapy date 2026-03-20 -f %j  # 079
```

Any other text in the format is kept: `-f "حلب في %d/%m/%Y"`.

## Month names

The Arab world uses several sets of month names. `--months` picks one, `levant` by
default:

| `--months` | January | Used in |
|------------|---------|---------|
| `levant` | كانون الثاني | Syria, Lebanon, Jordan, Palestine, Iraq |
| `egyptian` | يناير | Egypt, the Gulf, Sudan |
| `maghreb` | جانفي | Algeria, Tunisia |
| `levant_with_egyptian` | كانون الثاني (يناير) | documents read across the region |

```bash
arapy date 2026-01-05 -f %B --months egyptian  # يناير
arapy date 2026-01-05 -f %B --months maghreb  # جانفي
arapy date 2026-01-05 -f %B --months levant_with_egyptian  # كانون الثاني (يناير)
```

## Hijri dates

`--hijri` converts to the Hijri calendar, **Umm al-Qura**, the official calendar of
Saudi Arabia, used for most Hijri dates on documents:

```bash
arapy date 2026-01-05 --hijri -f "%A %d %B %Y هـ"  # الاثنين 16 رجب 1447 هـ
arapy date 2026-01-05 --hijri -f "%O من %B %Y" --digits arabic  # السادس عشر من رجب ١٤٤٧
arapy date ٢٠٢٦-٠٢-١٨ --hijri  # الأربعاء 01 رمضان 1447
arapy date 2026-03-20 --hijri -f "%d/%m/%Y"  # 01/10/1447
arapy date 2026-03-20 --hijri -f "%B"  # شوال
arapy date --hijri
```

- The same directives work, with Hijri months (محرم، صفر، ربيع الأول، ...), except `%y`.
- Hijri months have one set of names, so `--months` does not go with `--hijri`.
- Umm al-Qura covers 1343 to 1500 AH (1924 to 2077).

!!! note "The start of the month"
    Umm al-Qura is a computed calendar. The start of Ramadan or Shawwal announced by
    moon sighting in your country can differ by a day.

## Invalid dates

```text
$ arapy date 05/01/2026
Error: '05/01/2026' is not an ISO date (YYYY-MM-DD)

$ arapy date 2026-02-30
Error: '2026-02-30' is not an ISO date (YYYY-MM-DD)
```

Convert other formats to ISO first: Excel's `=TEXT(A2,"yyyy-mm-dd")`, or PowerShell's
`Get-Date -Format yyyy-MM-dd`.
