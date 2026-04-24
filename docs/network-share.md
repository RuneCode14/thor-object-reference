# network share

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/network-share` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `NetworkShare`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ |  |
| `path` | string | ✅ |  |
| `permissions` | array of object | ✅ | nested: `group`: string; `access`: string |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "network share"

detection:
    selection:
        NAME: null
    condition: selection
```
