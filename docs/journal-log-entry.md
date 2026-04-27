# journal log entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/journald-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `JournaldEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `DETAILS` | `details` | object (string) | ✅ |  |  |
| `TIME` | `time` | string (date-time) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "journal log entry"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
