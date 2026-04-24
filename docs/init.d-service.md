# init.d service

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/initd-service` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `InitdService`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `file` | object | ✅ | nested: `type`: string; `path`: string; `exists`: string; `extension`: string; `magic_header`: string; `hashes`: object; `first_bytes`: object; `file_times`: object; `size`: integer; `permissions`: True; `pe_info`: object; `target`: string; `unpack_source`: array | null; `link_info`: object; `recycle_bin_info`: object; `wer_info`: object; `content`: object; `beacon_config`: object; `virustotal`: object |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "init.d service"

detection:
    selection:
        FILE: null
    condition: selection
```
