# cron job

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/cron-job` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `CronJob`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `command` | string | ✅ |  |
| `schedule` | string | ✅ |  |
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "cron job"

detection:
    selection:
        COMMAND: null
    condition: selection
```
