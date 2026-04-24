# log line

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/log-line` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `LogLine`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `line` | string | ✅ |  |
| `line_index` | integer | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "log line"

detection:
    selection:
        LINE: null
    condition: selection
```
