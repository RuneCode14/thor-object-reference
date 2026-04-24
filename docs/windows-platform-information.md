# Windows platform information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/platform-info-windows` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PlatformInfoWindows`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `arch` | string | ✅ |  |
| `build_number` | string | ✅ |  |
| `installed_on` | string (date-time) | ✅ |  |
| `name` | string | ✅ |  |
| `os_type` | string | ✅ |  |
| `proc` | string | ✅ |  |
| `type` | string | ✅ |  |
| `version` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Windows platform information"

detection:
    selection:
        ARCH: null
    condition: selection
```
