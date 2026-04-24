# network connecting thread

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/network-connecting-thread` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `NetworkConnectingThread`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `callback_interval` | integer | ✅ |  |
| `connections` | array of object | ✅ | nested: `protocol`: string; `server`: string |
| `process` | object | ✅ | nested: `type`: string; `pid`: integer; `dead`: boolean; `name`: string; `command`: string; `owner`: string; `image`: object; `parent_info`: object; `tree`: array | null; `created`: string (date-time); `session`: string; `listen_ports`: array | null; `connections`: array | null; `sections`: array of object; `beacon_config`: object; `pe_sieve`: object |
| `thread_id` | integer | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "network connecting thread"

detection:
    selection:
        CALLBACK_INTERVAL: null
    condition: selection
```
