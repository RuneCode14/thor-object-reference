# AIX platform information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/platform-info-aix` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PlatformInfoAIX`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `BUILD_SEQUENCE_ID` | `build_sequence_id` | integer | ✅ |  |  |
| `MODEL` | `model` | string | ✅ |  |  |
| `OS_BUILD_TIME` | `os_build_time` | string (date-time) | ✅ |  |  |
| `PROC` | `proc` | string | ✅ |  |  |
| `SERVICE_PACK` | `service_pack` | integer | ✅ |  |  |
| `TECHNOLOGY_LEVEL` | `technology_level` | integer | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `VCPUS` | `vcpus` | integer | ✅ |  |  |
| `VERSION` | `version` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "AIX platform information"

detection:
    selection:
        MODEL|contains: 'suspicious_string'
    condition: selection

level: medium
```
