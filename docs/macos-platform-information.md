# MacOS platform information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/platform-info-macos` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PlatformInfoMacos`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `arch` | string | ✅ |  |
| `kernel_name` | string | ✅ |  |
| `kernel_version` | string | ✅ |  |
| `name` | string | ✅ |  |
| `proc` | string | ✅ |  |
| `type` | string | ✅ |  |
| `version` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "MacOS platform information"

detection:
    selection:
        ARCH: null
    condition: selection
```
