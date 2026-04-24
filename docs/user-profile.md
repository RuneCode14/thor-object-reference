# user profile

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/profile-folder` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ProfileFolder`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `created` | string (date-time) |  |  |
| `modified` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "user profile"

detection:
    selection:
        CREATED: null
    condition: selection
```
