# Unix permissions

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/unix-permissions` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `UnixPermissions`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `group` | string | ✅ |  |
| `mask` | object | ✅ | nested: `user`: object; `group`: object; `world`: object |
| `owner` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Unix permissions"

detection:
    selection:
        GROUP: null
    condition: selection
```
