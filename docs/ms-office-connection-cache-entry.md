# MS Office connection cache entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ms-office-connection-cache-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `MsOfficeConnectionCacheEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entry` | string | ✅ |  |
| `key` | string | ✅ |  |
| `modified` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "MS Office connection cache entry"

detection:
    selection:
        ENTRY: null
    condition: selection
```
