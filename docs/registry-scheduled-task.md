# registry scheduled task

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/registry-scheduled-task` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `RegistryScheduledTask`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `created` | string (date-time) | ✅ |  |
| `guid` | string | ✅ |  |
| `last_result` | string | ✅ |  |
| `last_run` | string (date-time) | ✅ |  |
| `last_stopped` | string (date-time) | ✅ |  |
| `path` | string | ✅ |  |
| `status` | string | ✅ |  |
| `type` | string | ✅ |  |
| `version` | integer | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "registry scheduled task"

detection:
    selection:
        CREATED: null
    condition: selection
```
