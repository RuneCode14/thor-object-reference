# Unix user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/unix-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `UnixUser`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ACCESS_FILES` | `access_files` | array | null | ✅ |  |  |
| `CRONTAB` | `crontab` | string | ✅ |  | ``, `/var/spool/cron/neo` |
| `FULL_NAME` | `full_name` | string | ✅ |  | `root`, `neo`, `System User` |
| `GID` | `gid` | string | ✅ |  | `0`, `1000`, `990` |
| `HOME` | `home` | string | ✅ |  | `/root`, `/home/neo`, `/` |
| `NAME` | `name` | string | ✅ |  | `root`, `neo`, `sssd` |
| `SHELL` | `shell` | string | ✅ |  | `/bin/bash`, `/usr/sbin/nologin`, `/bin/false` |
| `TYPE` | `type` | string | ✅ |  | `unix user` |
| `UID` | `uid` | string | ✅ |  | `0`, `1000`, `996` |

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
