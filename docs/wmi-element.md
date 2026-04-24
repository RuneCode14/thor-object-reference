# WMI element

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/wmi-element` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WmiElement`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `event_consumer` | string | ✅ |  |
| `event_consumer_name` | string | ✅ |  |
| `event_filter` | string | ✅ |  |
| `event_filter_name` | string | ✅ |  |
| `filter_type` | string | ✅ |  |
| `key` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "WMI element"

detection:
    selection:
        EVENT_CONSUMER: null
    condition: selection
```
