# jump list entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/jumplist-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `JumplistEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `access_count` | integer | ✅ |  |
| `birth_volume_id` | array of integer | ✅ |  |
| `checksum` | integer | ✅ |  |
| `entry_id` | integer | ✅ |  |
| `last_access` | string (date-time) | ✅ |  |
| `netbios_name` | string | ✅ |  |
| `object_id` | array of integer | ✅ |  |
| `path` | string | ✅ |  |
| `pinned` | boolean | ✅ |  |
| `type` | string | ✅ |  |
| `volume_id` | array of integer | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "jump list entry"

detection:
    selection:
        ACCESS_COUNT: null
    condition: selection
```
