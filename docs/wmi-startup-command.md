# WMI startup command

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/wmi-startup-command` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WmiStartupCommand`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `CAPTION` | `caption` | string | ✅ |  |  |
| `COMMAND` | `command` | string | ✅ |  |  |
| `LOCATION` | `location` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "WMI startup command"

detection:
    selection:
        COMMAND|contains: 'suspicious_command'
    condition: selection

level: medium
```
