# shellbag entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/shellbag-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ShellbagEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `DATE_ACCESS` | `date_access` | string (date-time) | ✅ |  |  |
| `NAME` | `name` | string | ✅ |  |  |
| `PATH` | `path` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "shellbag entry"

detection:
    selection:
        PATH|contains: 'suspicious_path'
    condition: selection

level: medium
```
