# process handle

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/process-handle` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ProcessHandle`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `HANDLE` | `handle` | integer | ✅ |  |
| `HANDLE_TYPE` | `handle_type` | string |  |  |
| `NAME` | `name` | string | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "process handle"

detection:
    selection:
        NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
