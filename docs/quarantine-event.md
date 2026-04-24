# quarantine event

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/quarantine-event` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `QuarantineEvent`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `event_type` | string | ✅ |  |
| `id` | string | ✅ |  |
| `name` | string | ✅ |  |
| `timestamp` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |
| `url` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "quarantine event"

detection:
    selection:
        EVENT_TYPE: null
    condition: selection
```
