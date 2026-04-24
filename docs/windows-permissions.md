# Windows permissions

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-permissions` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsPermissions`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `acl` | array | null | ✅ |  |
| `owner` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Windows permissions"

detection:
    selection:
        ACL: null
    condition: selection
```
