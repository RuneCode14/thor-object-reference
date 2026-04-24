# MFT entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/mft-file-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `MftFileEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `accessed` | string (date-time) | ✅ |  |
| `changed` | string (date-time) | ✅ |  |
| `created` | string (date-time) | ✅ |  |
| `deleted` | boolean |  |  |
| `dir` | boolean | ✅ |  |
| `filename` | string | ✅ |  |
| `flags` | integer |  |  |
| `modified` | string (date-time) | ✅ |  |
| `path` | string | ✅ |  |
| `size` | integer | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "MFT entry"

detection:
    selection:
        ACCESSED: null
    condition: selection
```
