# SDN query MPLog entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/sdn-query-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `SdnQueryEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `FILE` | `file` | string | ✅ |  |  |
| `SHA1` | `sha1` | string | ✅ |  |  |
| `SHA256` | `sha256` | string | ✅ |  |  |
| `TIME` | `time` | string (date-time) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "SDN query MPLog entry"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
