# DoublePulsar Handshake

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/double-pulsar-handshake` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `DoublePulsarHandshake`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `handshake_type` | string | ✅ |  |
| `key` | integer |  |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "DoublePulsar Handshake"

detection:
    selection:
        HANDSHAKE_TYPE: null
    condition: selection
```
