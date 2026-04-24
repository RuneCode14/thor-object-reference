# KnowledgeDB entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/knowledge-db-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `KnowledgeDBEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `created` | string (date-time) | ✅ |  |
| `duration` | integer | ✅ |  |
| `entry` | string | ✅ |  |
| `primary_key` | integer | ✅ |  |
| `started` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "KnowledgeDB entry"

detection:
    selection:
        CREATED: null
    condition: selection
```
