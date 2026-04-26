# registry value

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/registry-value` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `RegistryValue`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `KEY` | `key` | string | ✅ |  |  |
| `MODIFIED` | `modified` | string (date-time) | ✅ |  |  |
| `SIZE` | `size` | integer | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  | `registry value` |
| `VALUE` | `value` | string | ✅ |  | `%windir%\system32\SecurityHealthSystray....`, `C:\Users\neo\AppData\Local\Microsoft\One...`, `powershell -enc ...` |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "registry value"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
