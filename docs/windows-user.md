# Windows user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsUser`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ACTIVE` | `active` | boolean | ✅ |  | `True` |
| `BAD_PASSWORD_COUNT` | `bad_password_count` | integer | ✅ |  | `0` |
| `COMMENT` | `comment` | string | ✅ |  | `` |
| `FULL_NAME` | `full_name` | string | ✅ |  | `Built-in account for administering the c...`, ``, `Florian Roth` |
| `IS_ADMIN` | `is_admin` | boolean | ✅ |  | `True`, `False` |
| `LAST_LOGON` | `last_logon` | string (date-time) | ✅ |  | `2026-04-26T10:30:00Z`, `never`, `2026-04-26T14:28:12+02:00` |
| `LOCKED` | `locked` | boolean | ✅ |  | `False` |
| `NO_EXPIRE` | `no_expire` | boolean | ✅ |  | `True` |
| `NUM_LOGONS` | `num_logons` | integer | ✅ |  | `1203`, `0` |
| `PASS_AGE` | `pass_age` | integer | ✅ |  | `6539359000000000`, `2390831000000000` |
| `TYPE` | `type` | string | ✅ |  | `windows user` |
| `USER` | `user` | string | ✅ |  | `Administrator`, `Guest` |

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
