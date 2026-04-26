# Unix permissions

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/unix-permissions` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `UnixPermissions`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `GROUP` | `group` | string | ✅ |  |  |
| `MASK` | `mask` | object | ✅ | nested: `USER\|READABLE`: boolean; `USER\|WRITABLE`: boolean; `USER\|EXECUTABLE`: boolean; `GROUP\|READABLE`: boolean; `GROUP\|WRITABLE`: boolean; `GROUP\|EXECUTABLE`: boolean; `WORLD\|READABLE`: boolean; `WORLD\|WRITABLE`: boolean; `WORLD\|EXECUTABLE`: boolean |  |
| `OWNER` | `owner` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

**MASK** (`mask` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `USER|READABLE` | `user.readable` | boolean |
| `USER|WRITABLE` | `user.writable` | boolean |
| `USER|EXECUTABLE` | `user.executable` | boolean |
| `GROUP|READABLE` | `group.readable` | boolean |
| `GROUP|WRITABLE` | `group.writable` | boolean |
| `GROUP|EXECUTABLE` | `group.executable` | boolean |
| `WORLD|READABLE` | `world.readable` | boolean |
| `WORLD|WRITABLE` | `world.writable` | boolean |
| `WORLD|EXECUTABLE` | `world.executable` | boolean |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Unix permissions"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
