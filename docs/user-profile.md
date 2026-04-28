# user profile

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/profile-folder` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ProfileFolder`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `CREATED` | `created` | string (date-time) |  |  |  |
| `MODIFIED` | `modified` | string (date-time) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `USER` | `user` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "user profile"

detection:
    selection:
        USER|contains: 'suspicious_string'
    condition: selection

level: medium
```
