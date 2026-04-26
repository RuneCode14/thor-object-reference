# PowerShell module analysis cache module entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ps-mac-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PSMacEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `COMMAND` | `command` | string | ✅ |  |  |
| `PATH` | `path` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "PowerShell module analysis cache module entry"

detection:
    selection:
        PATH|contains:
            - '/suspicious/'
            - '/tmp/'
        COMMAND|contains|all:
            - 'powershell'
            - '-encodedcommand'
        TYPE: 'relevant_type'
    condition: selection
```
