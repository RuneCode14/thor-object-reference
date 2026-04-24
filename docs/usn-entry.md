# USN entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/usn-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `UsnEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `event_time` | string (date-time) | ✅ |  |
| `filename` | string | ✅ |  |
| `reasons` | array of string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "USN entry"

detection:
    selection:
        EVENT_TIME: null
    condition: selection
```
