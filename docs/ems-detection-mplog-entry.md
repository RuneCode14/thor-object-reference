# EMS detection MPLog entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ems-detection-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `EmsDetectionEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `PID` | `pid` | integer | ✅ |  |  |
| `THREAT_NAME` | `threat_name` | string | ✅ |  |  |
| `TIME` | `time` | string (date-time) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "EMS detection MPLog entry"

detection:
    selection:
        THREAT_NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
