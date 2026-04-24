# registry key

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/registry-key` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `RegistryKey`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `key` | string | ✅ |  |
| `modified` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |
| `values` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "registry key"

detection:
    selection:
        KEY: null
    condition: selection
```
