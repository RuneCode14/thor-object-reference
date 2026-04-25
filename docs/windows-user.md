# Windows user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsUser`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `ACTIVE` | `active` | boolean | ✅ |  |
| `BAD_PASSWORD_COUNT` | `bad_password_count` | integer | ✅ |  |
| `COMMENT` | `comment` | string | ✅ |  |
| `FULL_NAME` | `full_name` | string | ✅ |  |
| `IS_ADMIN` | `is_admin` | boolean | ✅ |  |
| `LAST_LOGON` | `last_logon` | string (date-time) | ✅ |  |
| `LOCKED` | `locked` | boolean | ✅ |  |
| `NO_EXPIRE` | `no_expire` | boolean | ✅ |  |
| `NUM_LOGONS` | `num_logons` | integer | ✅ |  |
| `PASS_AGE` | `pass_age` | integer | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |
| `USER` | `user` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Windows user"

detection:
    selection:
        FULL_NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    filter_legitimate:
        USER|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
