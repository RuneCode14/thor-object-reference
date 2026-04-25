# groups.xml user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/groups-xml-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `GroupsXmlUser`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `PASSWORD` | `password` | string | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |
| `USER` | `user` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "groups.xml user"

detection:
    selection:
        TYPE: 'relevant_type'
    filter_legitimate:
        USER|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
