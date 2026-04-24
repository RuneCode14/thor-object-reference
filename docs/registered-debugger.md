# registered debugger

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/registered-debugger` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `RegisteredDebugger`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `debugger` | string | ✅ |  |
| `executable` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "registered debugger"

detection:
    selection:
        DEBUGGER: null
    condition: selection
```
