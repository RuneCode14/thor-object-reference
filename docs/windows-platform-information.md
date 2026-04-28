# Windows platform information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/platform-info-windows` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PlatformInfoWindows`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ARCH` | `arch` | string | ✅ |  |  |
| `BUILD_NUMBER` | `build_number` | string | ✅ |  |  |
| `INSTALLED_ON` | `installed_on` | string (date-time) | ✅ |  |  |
| `NAME` | `name` | string | ✅ |  |  |
| `OS_TYPE` | `os_type` | string | ✅ |  |  |
| `PROC` | `proc` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `VERSION` | `version` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Windows platform information"

detection:
    selection:
        NAME|contains: 'suspicious_name'
    condition: selection

level: medium
```
