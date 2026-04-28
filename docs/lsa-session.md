# LSA session

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/lsa-session` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `LsaSession`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `AUTH_PACKAGE` | `auth_package` | string | ✅ |  |  |
| `DOMAIN` | `domain` | string | ✅ |  |  |
| `LOGON_TIME` | `logon_time` | string (date-time) | ✅ |  |  |
| `LSA_SESSION` | `lsa_session` | string | ✅ |  |  |
| `SERVER` | `server` | string | ✅ |  |  |
| `SESSION_TYPE` | `session_type` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `USER` | `user` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "LSA session"

detection:
    selection:
        AUTH_PACKAGE|contains: 'suspicious_string'
    condition: selection

level: medium
```
