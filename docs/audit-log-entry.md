# audit log entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/audit-log-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AuditLogEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entry` | object (string) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "audit log entry"

detection:
    selection:
        ENTRY: null
    condition: selection
```
