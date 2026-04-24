# hotfix summary

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/hotfix-summary` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `HotfixSummary`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `last_hotfix` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "hotfix summary"

detection:
    selection:
        LAST_HOTFIX: null
    condition: selection
```
