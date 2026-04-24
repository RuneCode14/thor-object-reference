# Unix user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/unix-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `UnixUser`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `access_files` | array | null | ✅ |  |
| `crontab` | string | ✅ |  |
| `full_name` | string | ✅ |  |
| `gid` | string | ✅ |  |
| `home` | string | ✅ |  |
| `name` | string | ✅ |  |
| `shell` | string | ✅ |  |
| `type` | string | ✅ |  |
| `uid` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Unix user"

detection:
    selection:
        ACCESS_FILES: null
    condition: selection
```
