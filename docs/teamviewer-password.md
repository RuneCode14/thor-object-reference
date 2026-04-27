# TeamViewer password

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/team-viewer-password` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `TeamViewerPassword`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `NAME` | `name` | string | ✅ |  |  |
| `PASSWORD` | `password` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "TeamViewer password"

detection:
    selection:
        NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
