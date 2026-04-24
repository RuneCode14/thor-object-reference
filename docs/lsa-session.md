# LSA session

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/lsa-session` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `LsaSession`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `auth_package` | string | ✅ |  |
| `domain` | string | ✅ |  |
| `logon_time` | string (date-time) | ✅ |  |
| `lsa_session` | string | ✅ |  |
| `server` | string | ✅ |  |
| `session_type` | string | ✅ |  |
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "LSA session"

detection:
    selection:
        AUTH_PACKAGE: null
    condition: selection
```
