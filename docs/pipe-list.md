# pipe list

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-pipe-list` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsPipeList`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `pipes` | array of string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "pipe list"

detection:
    selection:
        PIPES: null
    condition: selection
```
