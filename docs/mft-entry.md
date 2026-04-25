# MFT entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/mft-file-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `MftFileEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `ACCESSED` | `accessed` | string (date-time) | ✅ |  |
| `CHANGED` | `changed` | string (date-time) | ✅ |  |
| `CREATED` | `created` | string (date-time) | ✅ |  |
| `DELETED` | `deleted` | boolean |  |  |
| `DIR` | `dir` | boolean | ✅ |  |
| `FILENAME` | `filename` | string | ✅ |  |
| `FLAGS` | `flags` | integer |  |  |
| `MODIFIED` | `modified` | string (date-time) | ✅ |  |
| `PATH` | `path` | string | ✅ |  |
| `SIZE` | `size` | integer | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "MFT entry"

detection:
    selection:
        PATH|contains:
            - '/suspicious/'
            - '/tmp/'
        FILENAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
