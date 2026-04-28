# groups.xml user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/groups-xml-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `GroupsXmlUser`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `PASSWORD` | `password` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `USER` | `user` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "groups.xml user"

detection:
    selection:
        PASSWORD|contains: 'suspicious_string'
    condition: selection

level: medium
```
