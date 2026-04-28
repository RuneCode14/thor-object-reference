# thread

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/thread` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Thread`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ID` | `id` | integer | ✅ |  |  |
| `STACK` | `stack` | array | null | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

This is a passive object type. The `ID` and `STACK` fields are not useful for
standard threat detection rules. Use this service to explicitly select thread
objects in correlation or forensic analysis rules.

```yaml
logsource:
    product: THOR
    service: thread

detection:
    selection:
        TYPE: 'thread'
    condition: selection

level: low
```
