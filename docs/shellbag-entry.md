# shellbag entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/shellbag-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ShellbagEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `date_access` | string (date-time) | ✅ |  |
| `name` | string | ✅ |  |
| `path` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "shellbag entry"

detection:
    selection:
        DATE_ACCESS: null
    condition: selection
```
