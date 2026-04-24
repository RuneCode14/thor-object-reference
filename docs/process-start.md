# process start

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/eventlog-process-start` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `EventlogProcessStart`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `process` | string | ✅ |  |
| `start_times` | array of string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "process start"

detection:
    selection:
        PROCESS: null
    condition: selection
```
