# authorized_keys entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/authorized-keys-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AuthorizedKeysEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `COMMENT` | `comment` | string | ✅ |  |
| `KEY` | `key` | string | ✅ |  |
| `KEY_TYPE` | `key_type` | string | ✅ |  |
| `LINE` | `line` | string | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "authorized_keys entry"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
