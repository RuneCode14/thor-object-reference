# groups.xml user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/groups-xml-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `GroupsXmlUser`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `password` | string | ✅ |  |
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "groups.xml user"

detection:
    selection:
        PASSWORD: null
    condition: selection
```
