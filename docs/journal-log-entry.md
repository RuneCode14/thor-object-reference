# journal log entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/journald-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `JournaldEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `details` | object (string) | ✅ |  |
| `time` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "journal log entry"

detection:
    selection:
        DETAILS: null
    condition: selection
```
