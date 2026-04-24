# WMI startup command

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/wmi-startup-command` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WmiStartupCommand`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `caption` | string | ✅ |  |
| `command` | string | ✅ |  |
| `location` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "WMI startup command"

detection:
    selection:
        CAPTION: null
    condition: selection
```
