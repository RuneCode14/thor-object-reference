# User Access Log Entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ual-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `UALEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ACCESSES_BY_DAY` | `accesses_by_day` | object | ✅ |  |  |
| `ADDRESS` | `address` | string | ✅ |  |  |
| `AUTHENTICATED_USER_NAME` | `authenticated_user_name` | string | ✅ |  |  |
| `CLIENT_NAME` | `client_name` | string |  |  |  |
| `INSERT_DATE` | `insert_date` | string (date-time) | ✅ |  |  |
| `LAST_ACCESS` | `last_access` | string (date-time) | ✅ |  |  |
| `PRODUCT_NAME` | `product_name` | string |  |  |  |
| `ROLE_GUID` | `role_guid` | array of integer | ✅ |  |  |
| `ROLE_NAME` | `role_name` | string |  |  |  |
| `TENANT_ID` | `tenant_id` | array of integer | ✅ |  |  |
| `TOTAL_ACCESSES` | `total_accesses` | integer | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "User Access Log Entry"

detection:
    selection:
        CLIENT_NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    filter_legitimate:
        AUTHENTICATED_USER_NAME|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
