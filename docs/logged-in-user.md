# logged in user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/logged-in-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `LoggedInUser`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | string |  |  |
| `other_domains` | string |  |  |
| `server` | string |  |  |
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "logged in user"

detection:
    selection:
        DOMAIN: null
    condition: selection
```
