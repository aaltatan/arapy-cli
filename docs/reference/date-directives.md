# Date directives

`arapy date -f` takes these directives. Everything else in the format is kept as it is.

| Directive | Meaning | Gregorian example | Hijri example |
|-----------|---------|-------------------|---------------|
| `%A` | weekday name | الاثنين | الاثنين |
| `%a` | weekday name (same as `%A`) | الاثنين | الاثنين |
| `%B` | month name | كانون الثاني | رجب |
| `%b` | month name (same as `%B`) | كانون الثاني | رجب |
| `%d` | day, two digits | 05 | 16 |
| `%O` | ordinal day | الخامس | السادس عشر |
| `%m` | month, two digits | 01 | 07 |
| `%Y` | year, four digits | 2026 | 1447 |
| `%y` | year, two digits | 26 | not supported |
| `%j` | day of the year, three digits | 005 | 194 |

Hijri dates do not take `%y`: a two-digit Hijri year is not used on documents.

Examples for 5 January 2026:

```bash
arapy date 2026-01-05  # الاثنين 05 كانون الثاني 2026
arapy date 2026-01-05 -f "%A %O من %B %Y"  # الاثنين الخامس من كانون الثاني 2026
arapy date 2026-01-05 --hijri -f "%A %d %B %Y هـ"  # الاثنين 16 رجب 1447 هـ
```

## Month names

| Month | `levant` | `egyptian` | `maghreb` |
|-------|----------|------------|-----------|
| 1 | كانون الثاني | يناير | جانفي |
| 2 | شباط | فبراير | فيفري |
| 3 | آذار | مارس | مارس |
| 4 | نيسان | أبريل | أفريل |
| 5 | أيار | مايو | ماي |
| 6 | حزيران | يونيو | جوان |
| 7 | تموز | يوليو | جويلية |
| 8 | آب | أغسطس | أوت |
| 9 | أيلول | سبتمبر | سبتمبر |
| 10 | تشرين الأول | أكتوبر | أكتوبر |
| 11 | تشرين الثاني | نوفمبر | نوفمبر |
| 12 | كانون الأول | ديسمبر | ديسمبر |

`levant_with_egyptian` writes both: «كانون الثاني (يناير)».

## Hijri months

محرم، صفر، ربيع الأول، ربيع الآخر، جمادى الأولى، جمادى الآخرة، رجب، شعبان، رمضان، شوال،
ذو القعدة، ذو الحجة.

## Weekdays

الأحد، الاثنين، الثلاثاء، الأربعاء، الخميس، الجمعة، السبت.
