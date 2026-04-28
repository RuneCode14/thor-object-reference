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

### MASK JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `mask` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `user.readable` | boolean | |  |
| `user.writable` | boolean | |  |
| `user.executable` | boolean | |  |
| `group.readable` | boolean | |  |
| `group.writable` | boolean | |  |
| `group.executable` | boolean | |  |
| `world.readable` | boolean | |  |
| `world.writable` | boolean | |  |
| `world.executable` | boolean | |  |

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
