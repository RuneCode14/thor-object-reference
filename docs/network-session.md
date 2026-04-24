# network session

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/network-session` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `NetworkSession`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `active` | integer | ✅ |  |
| `client` | string | ✅ |  |
| `client_type` | string | ✅ |  |
| `idle` | integer | ✅ |  |
| `num_opens` | integer | ✅ |  |
| `type` | string | ✅ |  |
| `user_name` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "network session"

detection:
    selection:
        ACTIVE: null
    condition: selection
```
