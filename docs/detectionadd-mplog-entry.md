# DetectionAdd MPLog entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/detection-add-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `DetectionAddEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `detected` | object (string) | ✅ |  |
| `threat_name` | string | ✅ |  |
| `time` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "DetectionAdd MPLog entry"

detection:
    selection:
        DETECTED: null
    condition: selection
```
