# system information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/host-info` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `HostInfo`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `CPU_COUNT` | `cpu_count` | integer | ✅ |  |  |
| `DOMAIN` | `domain` | string | ✅ |  |  |
| `HOSTNAME` | `hostname` | string | ✅ |  |  |
| `INTERFACES` | `interfaces` | array of object | ✅ |  |  |
| `LANGUAGE` | `language` | string | ✅ |  |  |
| `MEMORY` | `memory` | integer | ✅ |  |  |
| `MOUNT_POINTS` | `mount_points` | array of object | ✅ |  |  |
| `PLATFORM` | `platform` | any | ✅ |  |  |
| `SYSTEM_TYPE` | `system_type` | string | ✅ |  |  |
| `TIMEZONE` | `timezone` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `UPTIME` | `uptime` | integer | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "system information"

detection:
    selection:
        HOSTNAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
