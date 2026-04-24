# systemd service

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/systemd-service` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `SystemdService`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `command` | string | ✅ |  |
| `image` | object | ✅ | nested: `type`: string; `path`: string; `exists`: string; `extension`: string; `magic_header`: string; `hashes`: object; `first_bytes`: object; `file_times`: object; `size`: integer; `permissions`: True; `pe_info`: object; `target`: string; `unpack_source`: array | null; `link_info`: object; `recycle_bin_info`: object; `wer_info`: object; `content`: object; `beacon_config`: object; `virustotal`: object |
| `run_as_group` | string | ✅ |  |
| `run_as_user` | string | ✅ |  |
| `type` | string | ✅ |  |
| `unit` | object | ✅ | nested: `type`: string; `path`: string; `exists`: string; `extension`: string; `magic_header`: string; `hashes`: object; `first_bytes`: object; `file_times`: object; `size`: integer; `permissions`: True; `pe_info`: object; `target`: string; `unpack_source`: array | null; `link_info`: object; `recycle_bin_info`: object; `wer_info`: object; `content`: object; `beacon_config`: object; `virustotal`: object |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "systemd service"

detection:
    selection:
        COMMAND: null
    condition: selection
```
