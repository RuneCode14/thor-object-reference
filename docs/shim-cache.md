# shim cache

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/shim-cache` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ShimCache`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entries` | integer | ✅ |  |
| `last_known_entries` | integer | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "shim cache"

detection:
    selection:
        ENTRIES: null
    condition: selection
```
