# structured data from plugin

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/plugin-structured-data` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PluginStructuredData`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `DATA` | `data` | object (string) | ✅ |  |  |
| `PLUGIN` | `plugin` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "structured data from plugin"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
