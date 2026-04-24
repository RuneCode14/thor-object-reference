# Windows user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsUser`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `active` | boolean | ✅ |  |
| `bad_password_count` | integer | ✅ |  |
| `comment` | string | ✅ |  |
| `full_name` | string | ✅ |  |
| `is_admin` | boolean | ✅ |  |
| `last_logon` | string (date-time) | ✅ |  |
| `locked` | boolean | ✅ |  |
| `no_expire` | boolean | ✅ |  |
| `num_logons` | integer | ✅ |  |
| `pass_age` | integer | ✅ |  |
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Windows user"

detection:
    selection:
        ACTIVE: null
    condition: selection
```
