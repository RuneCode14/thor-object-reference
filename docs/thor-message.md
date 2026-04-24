# THOR message

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/message` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Message`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `fields` | null | object | ✅ |  |
| `log_version` | string | ✅ |  |
| `message` | string | ✅ |  |
| `meta` | object | ✅ | nested: `time`: string (date-time); `level`: string; `module`: string; `scan_id`: string; `event_id`: string; `hostname`: string |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "THOR message"

detection:
    selection:
        FIELDS: null
    condition: selection
```
