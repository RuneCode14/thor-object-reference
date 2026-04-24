# at job

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/at-job` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AtJob`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `command` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "at job"

detection:
    selection:
        COMMAND: null
    condition: selection
```
