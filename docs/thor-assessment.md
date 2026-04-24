# THOR assessment

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/assessment` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Assessment`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `context` | array | null | ✅ |  |
| `issues` | array of object |  | nested: `affected`: string; `category`: string; `description`: string |
| `log_version` | string | ✅ |  |
| `message` | string | ✅ |  |
| `meta` | object | ✅ | nested: `time`: string (date-time); `level`: string; `module`: string; `scan_id`: string; `event_id`: string; `hostname`: string |
| `reason_count` | integer |  |  |
| `reasons` | array of object | ✅ | nested: `type`: string; `summary`: string; `signature`: object; `matched`: array | null |
| `score` | integer | ✅ |  |
| `subject` | any | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "THOR assessment"

detection:
    selection:
        CONTEXT: null
    condition: selection
```
