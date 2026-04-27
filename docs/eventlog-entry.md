# eventlog entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-eventlog-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsEventlogEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ENTRY` | `entry` | object (string) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  | `eventlog entry` |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "eventlog entry"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
