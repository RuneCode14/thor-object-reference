# registered debugger

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/registered-debugger` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `RegisteredDebugger`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `DEBUGGER` | `debugger` | string | ✅ |  |  |
| `EXECUTABLE` | `executable` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "registered debugger"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
