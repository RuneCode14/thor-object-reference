# shim database entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/sdb-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `SdbEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entry` | object (string) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "shim database entry"

detection:
    selection:
        ENTRY: null
    condition: selection
```
