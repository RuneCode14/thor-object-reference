# Unix permissions

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/unix-permissions` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `UnixPermissions`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `GROUP` | `group` | string | ✅ |  |  |
| `MASK` | `mask` | object | ✅ | Object, see [MASK Nested Fields](#mask-nested-fields) below |  |
| `OWNER` | `owner` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### MASK Nested Fields

Nested fields within `mask` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `MASK.USER.READABLE` | `user.readable` | boolean | |  |
| `MASK.USER.WRITABLE` | `user.writable` | boolean | |  |
| `MASK.USER.EXECUTABLE` | `user.executable` | boolean | |  |
| `MASK.GROUP.READABLE` | `group.readable` | boolean | |  |
| `MASK.GROUP.WRITABLE` | `group.writable` | boolean | |  |
| `MASK.GROUP.EXECUTABLE` | `group.executable` | boolean | |  |
| `MASK.WORLD.READABLE` | `world.readable` | boolean | |  |
| `MASK.WORLD.WRITABLE` | `world.writable` | boolean | |  |
| `MASK.WORLD.EXECUTABLE` | `world.executable` | boolean | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Unix permissions"

detection:
    selection:
        GROUP|contains: 'suspicious_string'
    condition: selection

level: medium
```
