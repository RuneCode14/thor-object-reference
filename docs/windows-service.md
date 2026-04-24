# Windows service

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-service` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsService`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | string | ✅ |  |
| `failure_command` | string | ✅ |  |
| `image` | object | ✅ | nested: `type`: string; `path`: string; `exists`: string; `extension`: string; `magic_header`: string; `hashes`: object; `first_bytes`: object; `file_times`: object; `size`: integer; `permissions`: True; `pe_info`: object; `target`: string; `unpack_source`: array | null; `link_info`: object; `recycle_bin_info`: object; `wer_info`: object; `content`: object; `beacon_config`: object; `virustotal`: object |
| `key` | string | ✅ |  |
| `key_name` | string | ✅ |  |
| `modified` | string (date-time) | ✅ |  |
| `service_name` | string | ✅ |  |
| `service_type` | string | ✅ |  |
| `start_type` | string | ✅ |  |
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Windows service"

detection:
    selection:
        DESCRIPTION: null
    condition: selection
```
