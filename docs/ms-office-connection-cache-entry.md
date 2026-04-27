# MS Office connection cache entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ms-office-connection-cache-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `MsOfficeConnectionCacheEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ENTRY` | `entry` | string | ✅ |  |  |
| `KEY` | `key` | string | ✅ |  |  |
| `MODIFIED` | `modified` | string (date-time) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "MS Office connection cache entry"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
