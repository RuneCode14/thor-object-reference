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

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "LSA session"

detection:
    selection:
        TYPE: 'relevant_type'
    filter_legitimate:
        USER|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
