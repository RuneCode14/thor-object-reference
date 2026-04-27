# Linux kernel module

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/linux-kernel-module` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `LinuxKernelModule`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `AUTHOR` | `author` | string | ✅ |  |  |
| `DESCRIPTION` | `description` | array of string | ✅ |  |  |
| `FILE` | `file` | object | ✅ | Object, see [FILE Nested Fields](#file-nested-fields) below | `/lib/modules/6.18.6-200.fc43.x86_64/kern...`, `null` |
| `IN_PROC_MODULES` | `in_proc_modules` | boolean | ✅ |  |  |
| `IN_SYS_MODULE` | `in_sys_module` | boolean | ✅ |  |  |
| `IN_VMALLOCINFO` | `in_vmallocinfo` | boolean | ✅ |  |  |
| `INCLUDED_IN_KERNEL` | `included_in_kernel` | boolean | ✅ |  | `true`, `false` |
| `LOAD_STATE` | `load_state` | string |  |  |  |
| `NAME` | `name` | string | ✅ |  | `nf_conntrack`, `nvme`, `hid_generic` |
| `PARAMETERS` | `parameters` | object (string) |  |  |  |
| `REF_COUNT` | `ref_count` | integer | ✅ |  |  |
| `SIZE` | `size` | integer |  |  | `123456`, `0` |
| `TYPE` | `type` | string | ✅ |  | `linux kernel module` |
| `USED_BY` | `used_by` | array of string | ✅ |  |  |
| `VERSION` | `version` | string | ✅ |  |  |

### FILE Nested Fields

Nested fields within `file` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `FILE.TYPE` | `type` | string | | `linux kernel module` |
| `FILE.PATH` | `path` | string | |  |
| `FILE.EXISTS` | `exists` | string | |  |
| `FILE.EXTENSION` | `extension` | string | |  |
| `FILE.MAGIC_HEADER` | `magic_header` | string | |  |
| `FILE.HASHES.MD5` | `hashes.md5` | string | |  |
| `FILE.HASHES.SHA1` | `hashes.sha1` | string | |  |
| `FILE.HASHES.SHA256` | `hashes.sha256` | string | |  |
| `FILE.FIRST_BYTES.HEX` | `first_bytes.hex` | string | |  |
| `FILE.FIRST_BYTES.ASCII` | `first_bytes.ascii` | string | |  |
| `FILE.FILE_TIMES.MODIFIED` | `file_times.modified` | string (date-time) | |  |
| `FILE.FILE_TIMES.ACCESSED` | `file_times.accessed` | string (date-time) | |  |
| `FILE.FILE_TIMES.CHANGED` | `file_times.changed` | string (date-time) | |  |
| `FILE.FILE_TIMES.CREATED` | `file_times.created` | string (date-time) | |  |
| `FILE.FILE_TIMES.USN_CHANGE_TIME` | `file_times.usn_change_time` | string (date-time) | |  |
| `FILE.FILE_TIMES.MFT_FILE_NAME_MODIFIED` | `file_times.mft_file_name_modified` | string (date-time) | |  |
| `FILE.FILE_TIMES.MFT_FILE_NAME_ACCESSED` | `file_times.mft_file_name_accessed` | string (date-time) | |  |
| `FILE.FILE_TIMES.MFT_FILE_NAME_CHANGED` | `file_times.mft_file_name_changed` | string (date-time) | |  |
| `FILE.FILE_TIMES.MFT_FILE_NAME_CREATED` | `file_times.mft_file_name_created` | string (date-time) | |  |
| `FILE.SIZE` | `size` | integer | | `123456`, `0` |
| `FILE.PE_INFO.COMPANY` | `pe_info.company` | string | |  |
| `FILE.PE_INFO.DESCRIPTION` | `pe_info.description` | string | |  |
| `FILE.PE_INFO.LEGAL_COPYRIGHT` | `pe_info.legal_copyright` | string | |  |
| `FILE.PE_INFO.PRODUCT` | `pe_info.product` | string | |  |
| `FILE.PE_INFO.ORIGINAL_NAME` | `pe_info.original_name` | string | |  |
| `FILE.PE_INFO.INTERNAL_NAME` | `pe_info.internal_name` | string | |  |
| `FILE.PE_INFO.SIGNED` | `pe_info.signed` | boolean | |  |
| `FILE.PE_INFO.SIGNATURES` | `pe_info.signatures` | array | null | |  |
| `FILE.PE_INFO.IMPHASH` | `pe_info.imphash` | string | |  |
| `FILE.PE_INFO.RICH_HEADER_HASH` | `pe_info.rich_header_hash` | string | |  |
| `FILE.PE_INFO.CREATION_TIMESTAMP` | `pe_info.creation_timestamp` | string (date-time) | |  |
| `FILE.TARGET` | `target` | string | |  |
| `FILE.UNPACK_SOURCE` | `unpack_source` | array | null | |  |
| `FILE.LINK_INFO.TARGET` | `link_info.target` | string | |  |
| `FILE.LINK_INFO.ARGUMENTS` | `link_info.arguments` | string | |  |
| `FILE.LINK_INFO.COMMAND_LINE` | `link_info.command_line` | string | |  |
| `FILE.LINK_INFO.CREATED` | `link_info.created` | string (date-time) | |  |
| `FILE.LINK_INFO.MODIFIED` | `link_info.modified` | string (date-time) | |  |
| `FILE.LINK_INFO.ACCESSED` | `link_info.accessed` | string (date-time) | |  |
| `FILE.RECYCLE_BIN_INFO.ORIGINAL_FILE_NAME` | `recycle_bin_info.original_file_name` | string | |  |
| `FILE.RECYCLE_BIN_INFO.DELETION_TIME` | `recycle_bin_info.deletion_time` | string (date-time) | |  |
| `FILE.RECYCLE_BIN_INFO.ORIGINAL_FILE_SIZE` | `recycle_bin_info.original_file_size` | integer | |  |
| `FILE.WER_INFO.TYPE` | `wer_info.type` | string | |  |
| `FILE.WER_INFO.EVENT_NAME` | `wer_info.event_name` | string | |  |
| `FILE.WER_INFO.EVENT_TYPE` | `wer_info.event_type` | string | |  |
| `FILE.WER_INFO.DATE` | `wer_info.date` | string (date-time) | |  |
| `FILE.WER_INFO.APP_PATH` | `wer_info.app_path` | string | |  |
| `FILE.WER_INFO.APP_NAME` | `wer_info.app_name` | string | |  |
| `FILE.WER_INFO.EXE` | `wer_info.exe` | string | |  |
| `FILE.WER_INFO.ERROR` | `wer_info.error` | string | |  |
| `FILE.WER_INFO.FAULT_IN_MODULE` | `wer_info.fault_in_module` | string | |  |
| `FILE.CONTENT.TYPE` | `content.type` | string | |  |
| `FILE.CONTENT.ELEMENTS` | `content.elements` | array | null | |  |
| `FILE.CONTENT.LENGTH` | `content.length` | integer | |  |
| `FILE.BEACON_CONFIG.BEACON_TYPE` | `beacon_config.beacon_type` | string | |  |
| `FILE.BEACON_CONFIG.C2` | `beacon_config.c2` | string | |  |
| `FILE.BEACON_CONFIG.PORT` | `beacon_config.port` | string | |  |
| `FILE.BEACON_CONFIG.SPAWN_TO` | `beacon_config.spawn_to` | string | |  |
| `FILE.BEACON_CONFIG.INJECTION_PROCESS` | `beacon_config.injection_process` | string | |  |
| `FILE.BEACON_CONFIG.PIPE_NAME` | `beacon_config.pipe_name` | string | |  |
| `FILE.BEACON_CONFIG.USER_AGENT` | `beacon_config.user_agent` | string | |  |
| `FILE.BEACON_CONFIG.PROXY` | `beacon_config.proxy` | string | |  |
| `FILE.BEACON_CONFIG.FULL_CONFIG` | `beacon_config.full_config` | object | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODED` | `beacon_config.cipher_parameters.xaf_encoded` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODING_ANCHOR` | `beacon_config.cipher_parameters.xaf_encoding_anchor` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.XOR_KEY` | `beacon_config.cipher_parameters.xor_key` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_OFFSET` | `beacon_config.cipher_parameters.beacon_offset` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_LENGTH` | `beacon_config.cipher_parameters.beacon_length` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.BLOCK_START` | `beacon_config.cipher_parameters.block_start` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.PAIRWISE_SWAPPED` | `beacon_config.cipher_parameters.pairwise_swapped` | any | |  |
| `FILE.VIRUSTOTAL.RESULT` | `virustotal.result` | string | |  |
| `FILE.VIRUSTOTAL.POSITIVE_VERDICTS` | `virustotal.positive_verdicts` | integer | |  |
| `FILE.VIRUSTOTAL.TOTAL_VERDICTS` | `virustotal.total_verdicts` | integer | |  |
| `FILE.VIRUSTOTAL.HISTORY.NAMES` | `virustotal.history.names` | any | |  |
| `FILE.VIRUSTOTAL.HISTORY.TAGS` | `virustotal.history.tags` | any | |  |
| `FILE.VIRUSTOTAL.HISTORY.SUBMISSIONS` | `virustotal.history.submissions` | any | |  |
| `FILE.VIRUSTOTAL.HISTORY.FIRST_SUBMISSION` | `virustotal.history.first_submission` | any | |  |
| `FILE.VIRUSTOTAL.HISTORY.LAST_SUBMISSION` | `virustotal.history.last_submission` | any | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Linux kernel module"

detection:
    selection:
        PATH|contains:
            - '/tmp/'
            - '/dev/shm/'
            - '\\Temp\\'
        NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    filter_legitimate:
        PE_INFO|SIGNED: 'true'
    condition: selection and not filter_legitimate
```
