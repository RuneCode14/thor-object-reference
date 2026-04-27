# quarantine event

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/quarantine-event` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `QuarantineEvent`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `EVENT_TYPE` | `event_type` | string | ✅ |  |  |
| `ID` | `id` | string | ✅ |  |  |
| `NAME` | `name` | string | ✅ |  |  |
| `TIMESTAMP` | `timestamp` | string (date-time) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `URL` | `url` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "quarantine event"

detection:
    selection:
        NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
