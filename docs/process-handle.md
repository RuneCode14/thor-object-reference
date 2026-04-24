# process handle

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/process-handle` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ProcessHandle`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `handle` | integer | ✅ |  |
| `handle_type` | string |  |  |
| `name` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "process handle"

detection:
    selection:
        HANDLE: null
    condition: selection
```
