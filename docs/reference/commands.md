# Commands and options

```text
arapy [--version] [--help] <command> [VALUES...] [options]
```

Every command takes **values** as arguments, or one per line on stdin when none are
given ([Many values and pipes](../guide/pipes.md)), and prints one result per line.

| Global option | Meaning |
|---------------|---------|
| `-V, --version` | Print the arapy-cli and arapy versions |
| `--install-completion` | Install tab completion for the current shell |
| `--show-completion` | Print the completion script |
| `--help` | Show help; also after a command: `arapy words --help` |

## `words` (`w`)

Numbers or amounts in words, or `--parse` to read words back. [Guide](../guide/words.md)

| Option | Default | Meaning |
|--------|---------|---------|
| `-c, --currency FILE` | none | A [currency file](currency-files.md); needed for fractions |
| `--case` | `nominative` | `nominative`, `accusative` or `genitive` |
| `--alef` | off | Spell hundreds مائة instead of مئة |
| `--prefix TEXT` | none | Text before the words, e.g. فقط |
| `--suffix TEXT` | none | Text after the words, e.g. لا غير |
| `--parse` | off | Read words back into a number |

## `money` (`m`)

Amounts in digits with the currency symbol. [Guide](../guide/formatting.md#money)

| Option | Default | Meaning |
|--------|---------|---------|
| `-c, --currency FILE` | required | A [currency file](currency-files.md) |
| `--digits` | `arabic` | `latin`, `arabic` or `persian` |
| `--grouping` | `٬` | Thousands separator; `""` for none |
| `--decimal` | `٫` | Decimal mark |
| `--places` | the subunit's | Decimal places, padded with zeros, never rounded |

## `number` (`n`)

Format numbers given in any digit set. [Guide](../guide/formatting.md#numbers)

| Option | Default | Meaning |
|--------|---------|---------|
| `--digits` | `latin` | `latin`, `arabic` or `persian` |
| `--grouping` | `,` | Thousands separator; `""` for none |
| `--decimal` | `.` | Decimal mark |
| `--places` | as given | Decimal places, padded with zeros, never rounded |
| `--percent` | off | Write `0.25` as `25٪` |

## `digits` (`d`)

Convert digits between digit sets; everything else is kept. [Guide](../guide/digits.md)

| Option | Default | Meaning |
|--------|---------|---------|
| `--to` | `arabic` | `latin`, `arabic` or `persian` |

## `normalize` (`norm`)

Fold letters, drop tashkeel and tatweel, for search and matching. [Guide](../guide/text.md)

| Option | Default | Meaning |
|--------|---------|---------|
| `--names` | off | The name preset: also splits عبدالله into عبد الله |

## `sort` (`s`)

Sort the values in Arabic alphabetical order. [Guide](../guide/text.md#sort)

| Option | Default | Meaning |
|--------|---------|---------|
| `-r, --reverse` | off | Descending |

## `ordinal` (`o`)

Ordinals from 1 to 100, and list markers. [Guide](../guide/ordinals.md)

| Option | Default | Meaning |
|--------|---------|---------|
| `-f, --feminine` | off | الأولى instead of الأول |
| `--case` | `nominative` | `nominative`, `accusative` or `genitive` |
| `--indefinite` | off | ثالث instead of الثالث |
| `--adverb` | off | List markers: أولًا، ثانيًا. Not with the three options above. |

## `date` (`dt`)

Write ISO dates in Arabic; today when no date is given. [Guide](../guide/dates.md)

| Option | Default | Meaning |
|--------|---------|---------|
| `-f, --format` | `%A %d %B %Y` | [Directives](date-directives.md): `%A %d %O %B %m %Y %j` |
| `--months` | `levant` | `levant`, `egyptian`, `maghreb`, `levant_with_egyptian`. Not with `--hijri`. |
| `--digits` | `latin` | `latin`, `arabic` or `persian` |
| `--hijri` | off | Write the Hijri date (Umm al-Qura) |
