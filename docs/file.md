# file

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/file` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `File`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `beacon_config` | object |  | nested: `beacon_type`: string; `c2`: string; `port`: string; `spawn_to`: string; `injection_process`: string; `pipe_name`: string; `user_agent`: string; `proxy`: string; `full_config`: object; `cipher_parameters`: object |
| `content` | object |  | nested: `type`: string; `elements`: array | null; `length`: integer |
| `exists` | string | ✅ |  |
| `extension` | string | ✅ |  |
| `file_times` | object |  | nested: `modified`: string (date-time); `accessed`: string (date-time); `changed`: string (date-time); `created`: string (date-time); `usn_change_time`: string (date-time); `mft_file_name_modified`: string (date-time); `mft_file_name_accessed`: string (date-time); `mft_file_name_changed`: string (date-time); `mft_file_name_created`: string (date-time) |
| `first_bytes` | object |  | nested: `hex`: string; `ascii`: string |
| `hashes` | object |  | nested: `md5`: string; `sha1`: string; `sha256`: string |
| `link_info` | object |  | nested: `target`: string; `arguments`: string; `command_line`: string; `created`: string (date-time); `modified`: string (date-time); `accessed`: string (date-time) |
| `magic_header` | string |  |  |
| `path` | string | ✅ |  |
| `pe_info` | object |  | nested: `company`: string; `description`: string; `legal_copyright`: string; `product`: string; `original_name`: string; `internal_name`: string; `signed`: boolean; `signatures`: array | null; `imphash`: string; `rich_header_hash`: string; `creation_timestamp`: string (date-time) |
| `permissions` | any |  |  |
| `recycle_bin_info` | object |  | nested: `original_file_name`: string; `deletion_time`: string (date-time); `original_file_size`: integer |
| `size` | integer |  |  |
| `target` | string |  |  |
| `type` | string | ✅ |  |
| `unpack_source` | array | null |  |  |
| `virustotal` | object |  | nested: `result`: string; `positive_verdicts`: integer; `total_verdicts`: integer; `history`: object |
| `wer_info` | object |  | nested: `type`: string; `event_name`: string; `event_type`: string; `date`: string (date-time); `app_path`: string; `app_name`: string; `exe`: string; `error`: string; `fault_in_module`: string |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "file"

detection:
    selection:
        BEACON_CONFIG: null
    condition: selection
```
