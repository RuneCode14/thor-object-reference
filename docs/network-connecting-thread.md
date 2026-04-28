# network connecting thread

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/network-connecting-thread` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `NetworkConnectingThread`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `CALLBACK_INTERVAL` | `callback_interval` | integer | ✅ |  |  |
| `CONNECTIONS` | `connections` | array of object | ✅ |  |  |
| `PROCESS` | `process` | object | ✅ | Object, see [PROCESS Nested Fields](#process-nested-fields) below |  |
| `THREAD_ID` | `thread_id` | integer | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### PROCESS JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `process` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `type` | string | |  |
| `pid` | integer | |  |
| `dead` | boolean | |  |
| `name` | string | |  |
| `command` | string | |  |
| `owner` | string | |  |
| `image.type` | string | |  |
| `image.path` | string | |  |
| `image.exists` | string | |  |
| `image.extension` | string | |  |
| `image.magic_header` | string | |  |
| `image.hashes.md5` | any | |  |
| `image.hashes.sha1` | any | |  |
| `image.hashes.sha256` | any | |  |
| `image.first_bytes.hex` | any | |  |
| `image.first_bytes.ascii` | any | |  |
| `image.file_times.modified` | any | |  |
| `image.file_times.accessed` | any | |  |
| `image.file_times.changed` | any | |  |
| `image.file_times.created` | any | |  |
| `image.file_times.usn_change_time` | any | |  |
| `image.file_times.mft_file_name_modified` | any | |  |
| `image.file_times.mft_file_name_accessed` | any | |  |
| `image.file_times.mft_file_name_changed` | any | |  |
| `image.file_times.mft_file_name_created` | any | |  |
| `image.size` | integer | |  |
| `image.pe_info.company` | any | |  |
| `image.pe_info.description` | any | |  |
| `image.pe_info.legal_copyright` | any | |  |
| `image.pe_info.product` | any | |  |
| `image.pe_info.original_name` | any | |  |
| `image.pe_info.internal_name` | any | |  |
| `image.pe_info.signed` | any | |  |
| `image.pe_info.signatures` | any | |  |
| `image.pe_info.imphash` | any | |  |
| `image.pe_info.rich_header_hash` | any | |  |
| `image.pe_info.creation_timestamp` | any | |  |
| `image.target` | string | |  |
| `image.unpack_source` | any | null | |  |
| `image.link_info.target` | any | |  |
| `image.link_info.arguments` | any | |  |
| `image.link_info.command_line` | any | |  |
| `image.link_info.created` | any | |  |
| `image.link_info.modified` | any | |  |
| `image.link_info.accessed` | any | |  |
| `image.recycle_bin_info.original_file_name` | any | |  |
| `image.recycle_bin_info.deletion_time` | any | |  |
| `image.recycle_bin_info.original_file_size` | any | |  |
| `image.wer_info.type` | any | |  |
| `image.wer_info.event_name` | any | |  |
| `image.wer_info.event_type` | any | |  |
| `image.wer_info.date` | any | |  |
| `image.wer_info.app_path` | any | |  |
| `image.wer_info.app_name` | any | |  |
| `image.wer_info.exe` | any | |  |
| `image.wer_info.error` | any | |  |
| `image.wer_info.fault_in_module` | any | |  |
| `image.content.type` | any | |  |
| `image.content.elements` | any | |  |
| `image.content.length` | any | |  |
| `image.beacon_config.beacon_type` | any | |  |
| `image.beacon_config.c2` | any | |  |
| `image.beacon_config.port` | any | |  |
| `image.beacon_config.spawn_to` | any | |  |
| `image.beacon_config.injection_process` | any | |  |
| `image.beacon_config.pipe_name` | any | |  |
| `image.beacon_config.user_agent` | any | |  |
| `image.beacon_config.proxy` | any | |  |
| `image.beacon_config.full_config` | any | |  |
| `image.beacon_config.cipher_parameters` | any | |  |
| `image.virustotal.result` | any | |  |
| `image.virustotal.positive_verdicts` | any | |  |
| `image.virustotal.total_verdicts` | any | |  |
| `image.virustotal.history` | any | |  |
| `parent_info.pid` | integer | |  |
| `parent_info.exe` | string | |  |
| `parent_info.command` | string | |  |
| `tree` | array | null | |  |
| `created` | string (date-time) | |  |
| `session` | string | |  |
| `listen_ports` | array | null | |  |
| `connections` | array | null | |  |
| `sections` | array of object | |  |
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
| `pe_sieve.suspicious_sections` | integer | |  |
| `pe_sieve.replaced` | integer | |  |
| `pe_sieve.hdr_mod` | integer | |  |
| `pe_sieve.unreachable_file` | integer | |  |
| `pe_sieve.patched` | integer | |  |
| `pe_sieve.iat_hooked` | integer | |  |
| `pe_sieve.implanted` | integer | |  |
| `pe_sieve.other` | integer | |  |
| `pe_sieve.skipped` | integer | |  |
| `pe_sieve.errors` | integer | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "network connecting thread"

detection:
    selection:
        TYPE: 'network connecting thread'
    condition: selection

level: medium
```
