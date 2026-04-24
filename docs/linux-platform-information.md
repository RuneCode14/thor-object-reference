# Linux platform information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/platform-info-linux` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PlatformInfoLinux`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `arch` | string | ✅ |  |
| `kernel_name` | string | ✅ |  |
| `kernel_version` | string | ✅ |  |
| `name` | string | ✅ |  |
| `proc` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Linux platform information"

detection:
    selection:
        ARCH: null
    condition: selection
```
