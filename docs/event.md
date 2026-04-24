# event

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-event` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsEvent`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `event` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "event"

detection:
    selection:
        EVENT: null
    condition: selection
```
