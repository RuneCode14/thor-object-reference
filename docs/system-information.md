# system information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/host-info` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `HostInfo`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cpu_count` | integer | ✅ |  |
| `domain` | string | ✅ |  |
| `hostname` | string | ✅ |  |
| `interfaces` | array of object | ✅ | nested: `name`: string; `ip_address`: string; `ipv6_address`: string; `mac_address`: string |
| `language` | string | ✅ |  |
| `memory` | integer | ✅ |  |
| `mount_points` | array of object | ✅ | nested: `fs_type`: string; `source`: string; `target`: string; `class`: string |
| `platform` | any | ✅ |  |
| `system_type` | string | ✅ |  |
| `timezone` | string | ✅ |  |
| `type` | string | ✅ |  |
| `uptime` | integer | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "system information"

detection:
    selection:
        CPU_COUNT: null
    condition: selection
```
