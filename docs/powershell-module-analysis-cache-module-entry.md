# PowerShell module analysis cache module entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ps-mac-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PSMacEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `command` | string | ✅ |  |
| `path` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "PowerShell module analysis cache module entry"

detection:
    selection:
        COMMAND: null
    condition: selection
```
