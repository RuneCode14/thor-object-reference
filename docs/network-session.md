# network session

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/network-session` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `NetworkSession`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `ACTIVE` | `active` | integer | ✅ |  |
| `CLIENT` | `client` | string | ✅ |  |
| `CLIENT_TYPE` | `client_type` | string | ✅ |  |
| `IDLE` | `idle` | integer | ✅ |  |
| `NUM_OPENS` | `num_opens` | integer | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |
| `USER_NAME` | `user_name` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "network session"

detection:
    selection:
        TYPE: 'relevant_type'
    filter_legitimate:
        USER_NAME|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
