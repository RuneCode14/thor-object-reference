# named pipe

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-pipe` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsPipe`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `pipe` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "named pipe"

detection:
    selection:
        PIPE: null
    condition: selection
```
