# registry value

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/registry-value` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `RegistryValue`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `key` | string | ✅ |  |
| `modified` | string (date-time) | ✅ |  |
| `size` | integer | ✅ |  |
| `type` | string | ✅ |  |
| `value` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "registry value"

detection:
    selection:
        KEY: null
    condition: selection
```
