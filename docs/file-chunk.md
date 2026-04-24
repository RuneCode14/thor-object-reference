# file chunk

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/deep-dive-chunk` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `DeepDiveChunk`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `beacon_config` | object |  | nested: `beacon_type`: string; `c2`: string; `port`: string; `spawn_to`: string; `injection_process`: string; `pipe_name`: string; `user_agent`: string; `proxy`: string; `full_config`: object; `cipher_parameters`: object |
| `chunk_end` | integer | ✅ |  |
| `chunk_offset` | integer | ✅ |  |
| `content` | object | ✅ | nested: `type`: string; `elements`: array | null; `length`: integer |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "file chunk"

detection:
    selection:
        BEACON_CONFIG: null
    condition: selection
```
