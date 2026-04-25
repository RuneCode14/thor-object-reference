# event

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-event` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsEvent`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `EVENT` | `event` | string | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "event"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
