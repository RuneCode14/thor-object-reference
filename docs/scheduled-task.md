# scheduled task

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/scheduled-task` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ScheduledTask`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `com_handlers` | array of string |  |  |
| `commands` | array of string | ✅ |  |
| `enabled` | boolean | ✅ |  |
| `last_run` | string (date-time) | ✅ |  |
| `logon_type` | string | ✅ |  |
| `name` | string | ✅ |  |
| `next_run` | string (date-time) | ✅ |  |
| `path` | string | ✅ |  |
| `privileges` | array of string |  |  |
| `run_level` | string | ✅ |  |
| `triggers` | array of string |  |  |
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "scheduled task"

detection:
    selection:
        COM_HANDLERS: null
    condition: selection
```
