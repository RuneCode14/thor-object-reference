# prefetch info

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/prefetch-info` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PrefetchInfo`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `accessed_files` | array of string | ✅ |  |
| `executable` | object | ✅ | nested: `type`: string; `path`: string; `exists`: string; `extension`: string; `magic_header`: string; `hashes`: object; `first_bytes`: object; `file_times`: object; `size`: integer; `permissions`: True; `pe_info`: object; `target`: string; `unpack_source`: array | null; `link_info`: object; `recycle_bin_info`: object; `wer_info`: object; `content`: object; `beacon_config`: object; `virustotal`: object |
| `execution_count` | integer | ✅ |  |
| `execution_times` | array of string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "prefetch info"

detection:
    selection:
        ACCESSED_FILES: null
    condition: selection
```
