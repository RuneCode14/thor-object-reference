# prefetch info

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/prefetch-info` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PrefetchInfo`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ACCESSED_FILES` | `accessed_files` | array of string | ✅ |  |  |
| `EXECUTABLE` | `executable` | object | ✅ | Object, see [EXECUTABLE Nested Fields](#executable-nested-fields) below |  |
| `EXECUTION_COUNT` | `execution_count` | integer | ✅ |  |  |
| `EXECUTION_TIMES` | `execution_times` | array of string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### EXECUTABLE Nested Fields

Nested fields within `executable` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `EXECUTABLE.TYPE` | `type` | string | |  |
| `EXECUTABLE.PATH` | `path` | string | |  |
| `EXECUTABLE.EXISTS` | `exists` | string | |  |
| `EXECUTABLE.EXTENSION` | `extension` | string | |  |
| `EXECUTABLE.MAGIC_HEADER` | `magic_header` | string | |  |
| `EXECUTABLE.HASHES.MD5` | `hashes.md5` | string | |  |
| `EXECUTABLE.HASHES.SHA1` | `hashes.sha1` | string | |  |
| `EXECUTABLE.HASHES.SHA256` | `hashes.sha256` | string | |  |
| `EXECUTABLE.FIRST_BYTES.HEX` | `first_bytes.hex` | string | |  |
| `EXECUTABLE.FIRST_BYTES.ASCII` | `first_bytes.ascii` | string | |  |
| `EXECUTABLE.FILE_TIMES.MODIFIED` | `file_times.modified` | string (date-time) | |  |
| `EXECUTABLE.FILE_TIMES.ACCESSED` | `file_times.accessed` | string (date-time) | |  |
| `EXECUTABLE.FILE_TIMES.CHANGED` | `file_times.changed` | string (date-time) | |  |
| `EXECUTABLE.FILE_TIMES.CREATED` | `file_times.created` | string (date-time) | |  |
| `EXECUTABLE.FILE_TIMES.USN_CHANGE_TIME` | `file_times.usn_change_time` | string (date-time) | |  |
| `EXECUTABLE.FILE_TIMES.MFT_FILE_NAME_MODIFIED` | `file_times.mft_file_name_modified` | string (date-time) | |  |
| `EXECUTABLE.FILE_TIMES.MFT_FILE_NAME_ACCESSED` | `file_times.mft_file_name_accessed` | string (date-time) | |  |
| `EXECUTABLE.FILE_TIMES.MFT_FILE_NAME_CHANGED` | `file_times.mft_file_name_changed` | string (date-time) | |  |
| `EXECUTABLE.FILE_TIMES.MFT_FILE_NAME_CREATED` | `file_times.mft_file_name_created` | string (date-time) | |  |
| `EXECUTABLE.SIZE` | `size` | integer | |  |
| `EXECUTABLE.PE_INFO.COMPANY` | `pe_info.company` | string | |  |
| `EXECUTABLE.PE_INFO.DESCRIPTION` | `pe_info.description` | string | |  |
| `EXECUTABLE.PE_INFO.LEGAL_COPYRIGHT` | `pe_info.legal_copyright` | string | |  |
| `EXECUTABLE.PE_INFO.PRODUCT` | `pe_info.product` | string | |  |
| `EXECUTABLE.PE_INFO.ORIGINAL_NAME` | `pe_info.original_name` | string | |  |
| `EXECUTABLE.PE_INFO.INTERNAL_NAME` | `pe_info.internal_name` | string | |  |
| `EXECUTABLE.PE_INFO.SIGNED` | `pe_info.signed` | boolean | |  |
| `EXECUTABLE.PE_INFO.SIGNATURES` | `pe_info.signatures` | array | null | |  |
| `EXECUTABLE.PE_INFO.IMPHASH` | `pe_info.imphash` | string | |  |
| `EXECUTABLE.PE_INFO.RICH_HEADER_HASH` | `pe_info.rich_header_hash` | string | |  |
| `EXECUTABLE.PE_INFO.CREATION_TIMESTAMP` | `pe_info.creation_timestamp` | string (date-time) | |  |
| `EXECUTABLE.TARGET` | `target` | string | |  |
| `EXECUTABLE.UNPACK_SOURCE` | `unpack_source` | array | null | |  |
| `EXECUTABLE.LINK_INFO.TARGET` | `link_info.target` | string | |  |
| `EXECUTABLE.LINK_INFO.ARGUMENTS` | `link_info.arguments` | string | |  |
| `EXECUTABLE.LINK_INFO.COMMAND_LINE` | `link_info.command_line` | string | |  |
| `EXECUTABLE.LINK_INFO.CREATED` | `link_info.created` | string (date-time) | |  |
| `EXECUTABLE.LINK_INFO.MODIFIED` | `link_info.modified` | string (date-time) | |  |
| `EXECUTABLE.LINK_INFO.ACCESSED` | `link_info.accessed` | string (date-time) | |  |
| `EXECUTABLE.RECYCLE_BIN_INFO.ORIGINAL_FILE_NAME` | `recycle_bin_info.original_file_name` | string | |  |
| `EXECUTABLE.RECYCLE_BIN_INFO.DELETION_TIME` | `recycle_bin_info.deletion_time` | string (date-time) | |  |
| `EXECUTABLE.RECYCLE_BIN_INFO.ORIGINAL_FILE_SIZE` | `recycle_bin_info.original_file_size` | integer | |  |
| `EXECUTABLE.WER_INFO.TYPE` | `wer_info.type` | string | |  |
| `EXECUTABLE.WER_INFO.EVENT_NAME` | `wer_info.event_name` | string | |  |
| `EXECUTABLE.WER_INFO.EVENT_TYPE` | `wer_info.event_type` | string | |  |
| `EXECUTABLE.WER_INFO.DATE` | `wer_info.date` | string (date-time) | |  |
| `EXECUTABLE.WER_INFO.APP_PATH` | `wer_info.app_path` | string | |  |
| `EXECUTABLE.WER_INFO.APP_NAME` | `wer_info.app_name` | string | |  |
| `EXECUTABLE.WER_INFO.EXE` | `wer_info.exe` | string | |  |
| `EXECUTABLE.WER_INFO.ERROR` | `wer_info.error` | string | |  |
| `EXECUTABLE.WER_INFO.FAULT_IN_MODULE` | `wer_info.fault_in_module` | string | |  |
| `EXECUTABLE.CONTENT.TYPE` | `content.type` | string | |  |
| `EXECUTABLE.CONTENT.ELEMENTS` | `content.elements` | array | null | |  |
| `EXECUTABLE.CONTENT.LENGTH` | `content.length` | integer | |  |
| `EXECUTABLE.BEACON_CONFIG.BEACON_TYPE` | `beacon_config.beacon_type` | string | |  |
| `EXECUTABLE.BEACON_CONFIG.C2` | `beacon_config.c2` | string | |  |
| `EXECUTABLE.BEACON_CONFIG.PORT` | `beacon_config.port` | string | |  |
| `EXECUTABLE.BEACON_CONFIG.SPAWN_TO` | `beacon_config.spawn_to` | string | |  |
| `EXECUTABLE.BEACON_CONFIG.INJECTION_PROCESS` | `beacon_config.injection_process` | string | |  |
| `EXECUTABLE.BEACON_CONFIG.PIPE_NAME` | `beacon_config.pipe_name` | string | |  |
| `EXECUTABLE.BEACON_CONFIG.USER_AGENT` | `beacon_config.user_agent` | string | |  |
| `EXECUTABLE.BEACON_CONFIG.PROXY` | `beacon_config.proxy` | string | |  |
| `EXECUTABLE.BEACON_CONFIG.FULL_CONFIG` | `beacon_config.full_config` | object | |  |
| `EXECUTABLE.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODED` | `beacon_config.cipher_parameters.xaf_encoded` | any | |  |
| `EXECUTABLE.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODING_ANCHOR` | `beacon_config.cipher_parameters.xaf_encoding_anchor` | any | |  |
| `EXECUTABLE.BEACON_CONFIG.CIPHER_PARAMETERS.XOR_KEY` | `beacon_config.cipher_parameters.xor_key` | any | |  |
| `EXECUTABLE.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_OFFSET` | `beacon_config.cipher_parameters.beacon_offset` | any | |  |
| `EXECUTABLE.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_LENGTH` | `beacon_config.cipher_parameters.beacon_length` | any | |  |
| `EXECUTABLE.BEACON_CONFIG.CIPHER_PARAMETERS.BLOCK_START` | `beacon_config.cipher_parameters.block_start` | any | |  |
| `EXECUTABLE.BEACON_CONFIG.CIPHER_PARAMETERS.PAIRWISE_SWAPPED` | `beacon_config.cipher_parameters.pairwise_swapped` | any | |  |
| `EXECUTABLE.VIRUSTOTAL.RESULT` | `virustotal.result` | string | |  |
| `EXECUTABLE.VIRUSTOTAL.POSITIVE_VERDICTS` | `virustotal.positive_verdicts` | integer | |  |
| `EXECUTABLE.VIRUSTOTAL.TOTAL_VERDICTS` | `virustotal.total_verdicts` | integer | |  |
| `EXECUTABLE.VIRUSTOTAL.HISTORY.NAMES` | `virustotal.history.names` | any | |  |
| `EXECUTABLE.VIRUSTOTAL.HISTORY.TAGS` | `virustotal.history.tags` | any | |  |
| `EXECUTABLE.VIRUSTOTAL.HISTORY.SUBMISSIONS` | `virustotal.history.submissions` | any | |  |
| `EXECUTABLE.VIRUSTOTAL.HISTORY.FIRST_SUBMISSION` | `virustotal.history.first_submission` | any | |  |
| `EXECUTABLE.VIRUSTOTAL.HISTORY.LAST_SUBMISSION` | `virustotal.history.last_submission` | any | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "prefetch info"

detection:
    selection:
        ACCESSED_FILES: 'suspicious_value'
    condition: selection

level: medium
```
