# EstimatedImpact MPLog entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/estimated-impact-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `EstimatedImpactEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `file` | string | ✅ |  |
| `image` | string | ✅ |  |
| `pid` | integer | ✅ |  |
| `time` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "EstimatedImpact MPLog entry"

detection:
    selection:
        FILE: null
    condition: selection
```
