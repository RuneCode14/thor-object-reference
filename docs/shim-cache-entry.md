# shim cache entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/shim-cache-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ShimCacheEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `exec_flag` | boolean | ✅ |  |
| `path` | string | ✅ |  |
| `timestamp` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "shim cache entry"

detection:
    selection:
        EXEC_FLAG: null
    condition: selection
```
