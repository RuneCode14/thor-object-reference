# sparse data

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/sparse-data` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `SparseData`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `elements` | array | null | ✅ |  |
| `length` | integer | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "sparse data"

detection:
    selection:
        ELEMENTS: null
    condition: selection
```
