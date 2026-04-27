# MFT entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/mft-file-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `MftFileEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ACCESSED` | `accessed` | string (date-time) | ✅ |  | `2026-04-26T10:05:00Z`, `2026-04-20T09:00:00Z` |
| `CHANGED` | `changed` | string (date-time) | ✅ |  |  |
| `CREATED` | `created` | string (date-time) | ✅ |  | `2026-01-15T08:30:00Z`, `2025-12-01T00:00:00Z` |
| `DELETED` | `deleted` | boolean |  |  |  |
| `DIR` | `dir` | boolean | ✅ |  |  |
| `FILENAME` | `filename` | string | ✅ |  |  |
| `FLAGS` | `flags` | integer |  |  | `FILE_ATTRIBUTE_ARCHIVE`, `FILE_ATTRIBUTE_SYSTEM`, `FILE_ATTRIBUTE_HIDDEN` |
| `MODIFIED` | `modified` | string (date-time) | ✅ |  | `2026-04-26T10:00:00Z`, `2026-04-25T15:30:00Z` |
| `PATH` | `path` | string | ✅ |  | `C:\Windows\System32\svchost.exe`, `C:\Users\neo\Documents\secret.docx`, `C:\Temp\evil.dll` |
| `SIZE` | `size` | integer | ✅ |  | `1502072`, `1234`, `1048576` |
| `TYPE` | `type` | string | ✅ |  | `mft entry` |

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
