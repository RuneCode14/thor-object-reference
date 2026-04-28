# init.d service

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/initd-service` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `InitdService`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `FILE` | `file` | object | ✅ | Object, see [FILE Nested Fields](#file-nested-fields) below |  |
| `TYPE` | `type` | string | ✅ |  |  |

### FILE JSON Sub-Fields

> ⚠️ **These nested fields are JSON structure reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules.
> Object null-check syntax (`FIELD: null`) exists but matched **all objects** in THOR v11.0.0 testing — verify behavior before relying on it.

Nested JSON structure within `file` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `type` | string | |  |
| `path` | string | |  |
| `exists` | string | |  |
| `extension` | string | |  |
| `magic_header` | string | |  |
| `hashes.md5` | string | |  |
| `hashes.sha1` | string | |  |
| `hashes.sha256` | string | |  |
| `first_bytes.hex` | string | |  |
| `first_bytes.ascii` | string | |  |
| `file_times.modified` | string (date-time) | |  |
| `file_times.accessed` | string (date-time) | |  |
| `file_times.changed` | string (date-time) | |  |
| `file_times.created` | string (date-time) | |  |
| `file_times.usn_change_time` | string (date-time) | |  |
| `file_times.mft_file_name_modified` | string (date-time) | |  |
| `file_times.mft_file_name_accessed` | string (date-time) | |  |
| `file_times.mft_file_name_changed` | string (date-time) | |  |
| `file_times.mft_file_name_created` | string (date-time) | |  |
| `size` | integer | |  |
| `pe_info.company` | string | |  |
| `pe_info.description` | string | |  |
| `pe_info.legal_copyright` | string | |  |
| `pe_info.product` | string | |  |
| `pe_info.original_name` | string | |  |
| `pe_info.internal_name` | string | |  |
| `pe_info.signed` | boolean | |  |
| `pe_info.signatures` | array | null | |  |
| `pe_info.imphash` | string | |  |
| `pe_info.rich_header_hash` | string | |  |
| `pe_info.creation_timestamp` | string (date-time) | |  |
| `target` | string | |  |
| `unpack_source` | array | null | |  |
| `link_info.target` | string | |  |
| `link_info.arguments` | string | |  |
| `link_info.command_line` | string | |  |
| `link_info.created` | string (date-time) | |  |
| `link_info.modified` | string (date-time) | |  |
| `link_info.accessed` | string (date-time) | |  |
| `recycle_bin_info.original_file_name` | string | |  |
| `recycle_bin_info.deletion_time` | string (date-time) | |  |
| `recycle_bin_info.original_file_size` | integer | |  |
| `wer_info.type` | string | |  |
| `wer_info.event_name` | string | |  |
| `wer_info.event_type` | string | |  |
| `wer_info.date` | string (date-time) | |  |
| `wer_info.app_path` | string | |  |
| `wer_info.app_name` | string | |  |
| `wer_info.exe` | string | |  |
| `wer_info.error` | string | |  |
| `wer_info.fault_in_module` | string | |  |
| `content.type` | string | |  |
| `content.elements` | array | null | |  |
| `content.length` | integer | |  |
| `beacon_config.beacon_type` | string | |  |
| `beacon_config.c2` | string | |  |
| `beacon_config.port` | string | |  |
| `beacon_config.spawn_to` | string | |  |
| `beacon_config.injection_process` | string | |  |
| `beacon_config.pipe_name` | string | |  |
| `beacon_config.user_agent` | string | |  |
| `beacon_config.proxy` | string | |  |
| `beacon_config.full_config` | object | |  |
| `beacon_config.cipher_parameters.xaf_encoded` | any | |  |
| `beacon_config.cipher_parameters.xaf_encoding_anchor` | any | |  |
| `beacon_config.cipher_parameters.xor_key` | any | |  |
| `beacon_config.cipher_parameters.beacon_offset` | any | |  |
| `beacon_config.cipher_parameters.beacon_length` | any | |  |
| `beacon_config.cipher_parameters.block_start` | any | |  |
| `beacon_config.cipher_parameters.pairwise_swapped` | any | |  |
| `virustotal.result` | string | |  |
| `virustotal.positive_verdicts` | integer | |  |
| `virustotal.total_verdicts` | integer | |  |
| `virustotal.history.names` | any | |  |
| `virustotal.history.tags` | any | |  |
| `virustotal.history.submissions` | any | |  |
| `virustotal.history.first_submission` | any | |  |
| `virustotal.history.last_submission` | any | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "init.d service"

detection:
    selection:
        FILE.PATH|contains: 'suspicious'
    condition: selection

level: medium
```
