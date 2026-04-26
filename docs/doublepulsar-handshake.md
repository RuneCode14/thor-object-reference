# DoublePulsar Handshake

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/double-pulsar-handshake` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `DoublePulsarHandshake`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `HANDSHAKE_TYPE` | `handshake_type` | string | ✅ |  |  |
| `KEY` | `key` | integer |  |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "DoublePulsar Handshake"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
