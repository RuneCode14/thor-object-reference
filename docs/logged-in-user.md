# logged in user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/logged-in-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `LoggedInUser`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `DOMAIN` | `domain` | string |  |  |  |
| `OTHER_DOMAINS` | `other_domains` | string |  |  |  |
| `SERVER` | `server` | string |  |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `USER` | `user` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "logged in user"

detection:
    selection:
        DOMAIN|contains: 'suspicious_string'
    condition: selection

level: medium
```
