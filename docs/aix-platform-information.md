# AIX platform information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/platform-info-aix` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PlatformInfoAIX`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `build_sequence_id` | integer | ✅ |  |
| `model` | string | ✅ |  |
| `os_build_time` | string (date-time) | ✅ |  |
| `proc` | string | ✅ |  |
| `service_pack` | integer | ✅ |  |
| `technology_level` | integer | ✅ |  |
| `type` | string | ✅ |  |
| `vcpus` | integer | ✅ |  |
| `version` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "AIX platform information"

detection:
    selection:
        BUILD_SEQUENCE_ID: null
    condition: selection
```
