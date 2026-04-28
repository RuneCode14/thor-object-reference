# audit log entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/audit-log-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AuditLogEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ENTRY` | `entry` | object (string) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "audit log entry"

detection:
    selection:
        ENTRY|contains: 'execve'
    condition: selection

level: medium
```
