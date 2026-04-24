# autorun entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/autorun-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AutorunEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `arguments` | string | ✅ |  |
| `autorun_type` | string | ✅ |  |
| `entry` | string | ✅ |  |
| `image` | object | ✅ | nested: `type`: string; `path`: string; `exists`: string; `extension`: string; `magic_header`: string; `hashes`: object; `first_bytes`: object; `file_times`: object; `size`: integer; `permissions`: True; `pe_info`: object; `target`: string; `unpack_source`: array | null; `link_info`: object; `recycle_bin_info`: object; `wer_info`: object; `content`: object; `beacon_config`: object; `virustotal`: object |
| `launch_string` | string | ✅ |  |
| `location` | string | ✅ |  |
| `old_md5` | string |  |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "autorun entry"

detection:
    selection:
        ARGUMENTS: null
    condition: selection
```
