# AmCache entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/amcache-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AmcacheEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `company` | string | ✅ |  |
| `created` | string (date-time) | ✅ |  |
| `desc` | string | ✅ |  |
| `file` | object | ✅ | nested: `type`: string; `path`: string; `exists`: string; `extension`: string; `magic_header`: string; `hashes`: object; `first_bytes`: object; `file_times`: object; `size`: integer; `permissions`: True; `pe_info`: object; `target`: string; `unpack_source`: array | null; `link_info`: object; `recycle_bin_info`: object; `wer_info`: object; `content`: object; `beacon_config`: object; `virustotal`: object |
| `first_run` | string (date-time) | ✅ |  |
| `product` | string | ✅ |  |
| `sha1` | string | ✅ |  |
| `size` | integer | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "AmCache entry"

detection:
    selection:
        COMPANY: null
    condition: selection
```
