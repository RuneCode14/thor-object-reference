# thread

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/thread` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Thread`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | integer | ✅ |  |
| `stack` | array | null | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "thread"

detection:
    selection:
        ID: null
    condition: selection
```
