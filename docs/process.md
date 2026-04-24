# process

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/process` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Process`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `beacon_config` | object |  | nested: `beacon_type`: string; `c2`: string; `port`: string; `spawn_to`: string; `injection_process`: string; `pipe_name`: string; `user_agent`: string; `proxy`: string; `full_config`: object; `cipher_parameters`: object |
| `command` | string | ✅ |  |
| `connections` | array | null | ✅ |  |
| `created` | string (date-time) | ✅ |  |
| `dead` | boolean |  |  |
| `image` | object | ✅ | nested: `type`: string; `path`: string; `exists`: string; `extension`: string; `magic_header`: string; `hashes`: object; `first_bytes`: object; `file_times`: object; `size`: integer; `permissions`: True; `pe_info`: object; `target`: string; `unpack_source`: array | null; `link_info`: object; `recycle_bin_info`: object; `wer_info`: object; `content`: object; `beacon_config`: object; `virustotal`: object |
| `listen_ports` | array | null | ✅ |  |
| `name` | string | ✅ |  |
| `owner` | string | ✅ |  |
| `parent_info` | object |  | nested: `pid`: integer; `exe`: string; `command`: string |
| `pe_sieve` | object |  | nested: `suspicious_sections`: integer; `replaced`: integer; `hdr_mod`: integer; `unreachable_file`: integer; `patched`: integer; `iat_hooked`: integer; `implanted`: integer; `other`: integer; `skipped`: integer; `errors`: integer |
| `pid` | integer | ✅ |  |
| `sections` | array of object |  | nested: `name`: string; `address`: integer; `size`: integer; `offset`: integer; `sparse_data`: object; `permissions`: object |
| `session` | string | ✅ |  |
| `tree` | array | null | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "process"

detection:
    selection:
        BEACON_CONFIG: null
    condition: selection
```
