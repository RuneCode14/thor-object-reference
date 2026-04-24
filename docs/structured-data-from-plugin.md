# structured data from plugin

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/plugin-structured-data` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PluginStructuredData`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object (string) | ✅ |  |
| `plugin` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "structured data from plugin"

detection:
    selection:
        DATA: null
    condition: selection
```
