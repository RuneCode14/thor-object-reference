# eventlog entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-eventlog-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsEventlogEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entry` | object (string) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "eventlog entry"

detection:
    selection:
        ENTRY: null
    condition: selection
```
