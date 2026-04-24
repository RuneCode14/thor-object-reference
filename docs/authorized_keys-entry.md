# authorized_keys entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/authorized-keys-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AuthorizedKeysEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `comment` | string | ✅ |  |
| `key` | string | ✅ |  |
| `key_type` | string | ✅ |  |
| `line` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "authorized_keys entry"

detection:
    selection:
        COMMENT: null
    condition: selection
```
