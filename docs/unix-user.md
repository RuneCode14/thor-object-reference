# Unix user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/unix-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `UnixUser`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `ACCESS_FILES` | `access_files` | array | null | ✅ |  |
| `CRONTAB` | `crontab` | string | ✅ |  |
| `FULL_NAME` | `full_name` | string | ✅ |  |
| `GID` | `gid` | string | ✅ |  |
| `HOME` | `home` | string | ✅ |  |
| `NAME` | `name` | string | ✅ |  |
| `SHELL` | `shell` | string | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |
| `UID` | `uid` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Unix user"

detection:
    selection:
        FULL_NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
