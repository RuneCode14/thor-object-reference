# EMS detection MPLog entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ems-detection-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `EmsDetectionEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `pid` | integer | ✅ |  |
| `threat_name` | string | ✅ |  |
| `time` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "EMS detection MPLog entry"

detection:
    selection:
        PID: null
    condition: selection
```
