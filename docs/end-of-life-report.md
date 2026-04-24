# end of life report

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/end-of-life-report` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `EndOfLifeReport`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `end_of_life` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |
| `version` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "end of life report"

detection:
    selection:
        END_OF_LIFE: null
    condition: selection
```
