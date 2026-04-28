# hotfix summary

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/hotfix-summary` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `HotfixSummary`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `LAST_HOTFIX` | `last_hotfix` | string (date-time) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "hotfix summary"

detection:
    selection:
        LAST_HOTFIX|contains: '2020'
    condition: selection

level: medium
```
