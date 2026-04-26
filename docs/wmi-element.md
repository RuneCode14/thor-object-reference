# WMI element

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/wmi-element` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WmiElement`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `EVENT_CONSUMER` | `event_consumer` | string | ✅ |  |  |
| `EVENT_CONSUMER_NAME` | `event_consumer_name` | string | ✅ |  |  |
| `EVENT_FILTER` | `event_filter` | string | ✅ |  |  |
| `EVENT_FILTER_NAME` | `event_filter_name` | string | ✅ |  |  |
| `FILTER_TYPE` | `filter_type` | string | ✅ |  |  |
| `KEY` | `key` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "WMI element"

detection:
    selection:
        EVENT_CONSUMER_NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
