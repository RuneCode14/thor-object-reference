# shim cache entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/shim-cache-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ShimCacheEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `EXEC_FLAG` | `exec_flag` | boolean | ✅ |  |  |
| `PATH` | `path` | string | ✅ |  |  |
| `TIMESTAMP` | `timestamp` | string (date-time) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "shim cache entry"

detection:
    selection:
        PATH|contains:
            - '/suspicious/'
            - '/tmp/'
        TYPE: 'relevant_type'
    condition: selection
```
