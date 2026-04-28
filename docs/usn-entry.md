# USN entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/usn-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `UsnEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `EVENT_TIME` | `event_time` | string (date-time) | ✅ |  |  |
| `FILENAME` | `filename` | string | ✅ |  |  |
| `REASONS` | `reasons` | array of string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "USN entry"

detection:
    selection:
        FILENAME: 'suspicious_value'
    condition: selection

level: medium
```
