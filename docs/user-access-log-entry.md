# User Access Log Entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ual-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `UALEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `accesses_by_day` | object | ✅ |  |
| `address` | string | ✅ |  |
| `authenticated_user_name` | string | ✅ |  |
| `client_name` | string |  |  |
| `insert_date` | string (date-time) | ✅ |  |
| `last_access` | string (date-time) | ✅ |  |
| `product_name` | string |  |  |
| `role_guid` | array of integer | ✅ |  |
| `role_name` | string |  |  |
| `tenant_id` | array of integer | ✅ |  |
| `total_accesses` | integer | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "User Access Log Entry"

detection:
    selection:
        ACCESSES_BY_DAY: null
    condition: selection
```
