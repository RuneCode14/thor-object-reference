# jump list entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/jumplist-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `JumplistEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ACCESS_COUNT` | `access_count` | integer | ✅ |  |  |
| `BIRTH_VOLUME_ID` | `birth_volume_id` | array of integer | ✅ |  |  |
| `CHECKSUM` | `checksum` | integer | ✅ |  |  |
| `ENTRY_ID` | `entry_id` | integer | ✅ |  |  |
| `LAST_ACCESS` | `last_access` | string (date-time) | ✅ |  |  |
| `NETBIOS_NAME` | `netbios_name` | string | ✅ |  |  |
| `OBJECT_ID` | `object_id` | array of integer | ✅ |  |  |
| `PATH` | `path` | string | ✅ |  |  |
| `PINNED` | `pinned` | boolean | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `VOLUME_ID` | `volume_id` | array of integer | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "jump list entry"

detection:
    selection:
        PATH|contains: 'suspicious_path'
    condition: selection

level: medium
```
