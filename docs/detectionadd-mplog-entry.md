# DetectionAdd MPLog entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/detection-add-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `DetectionAddEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `DETECTED` | `detected` | object (string) | ✅ |  |
| `THREAT_NAME` | `threat_name` | string | ✅ |  |
| `TIME` | `time` | string (date-time) | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "DetectionAdd MPLog entry"

detection:
    selection:
        THREAT_NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
