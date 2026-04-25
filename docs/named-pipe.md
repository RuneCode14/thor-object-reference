# named pipe

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-pipe` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsPipe`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `PIPE` | `pipe` | string | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "named pipe"

detection:
    selection:
        TYPE: 'relevant_type'
        PIPE|contains:
            - '192.168.'
            - '10.'
    condition: selection
```
