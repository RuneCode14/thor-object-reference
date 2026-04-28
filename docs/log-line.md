# log line

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/log-line` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `LogLine`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `LINE` | `line` | string | ✅ |  |  |
| `LINE_INDEX` | `line_index` | integer | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "log line"

detection:
    selection:
        LINE|contains: 'suspicious_string'
    condition: selection

level: medium
```
