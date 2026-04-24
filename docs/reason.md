# reason

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/reason` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Reason`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `matched` | array | null | ✅ |  |
| `signature` | object | ✅ | nested: `score`: integer; `reference`: array | null; `origin`: string; `kind`: string; `date`: string; `tags`: array | null; `rule_name`: string; `description`: string; `author`: string; `id`: string; `false_positives`: array | null |
| `summary` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "reason"

detection:
    selection:
        MATCHED: null
    condition: selection
```
