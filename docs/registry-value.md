# registry value

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/registry-value` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `RegistryValue`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `KEY` | `key` | string | ✅ |  | `SYSTEM\ControlSet001\Control\Lsa\Security Packages` |
| `MODIFIED` | `modified` | string (date-time) | ✅ |  | `2026-04-28T00:43:06.8527937+02:00` |
| `SIZE` | `size` | integer | ✅ |  | `8` |
| `TYPE` | `type` | string | ✅ |  | `registry value` |
| `VALUE` | `value` | string | ✅ |  | `""` |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "registry value"

detection:
    selection:
        KEY|contains: 'suspicious_string'
    condition: selection

level: medium
```
