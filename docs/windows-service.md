# Windows service

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-service` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsService`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `DESCRIPTION` | `description` | string | ✅ |  | `Helps protect users from malware and oth...`, `` |
| `FAILURE_COMMAND` | `failure_command` | string | ✅ |  |  |
| `IMAGE` | `image` | object | ✅ | Object, see [IMAGE Nested Fields](#image-nested-fields) below | `C:\Windows\System32\svchost.exe -k netsv...`, `C:\Program Files\Windows Defender\MsMpEn...`, `C:\Users\Public\malware.exe` |
| `KEY` | `key` | string | ✅ |  |  |
| `KEY_NAME` | `key_name` | string | ✅ |  |  |
| `MODIFIED` | `modified` | string (date-time) | ✅ |  |  |
| `SERVICE_NAME` | `service_name` | string | ✅ |  | `WinDefend`, `wuauserv`, `BITS` |
| `SERVICE_TYPE` | `service_type` | string | ✅ |  |  |
| `START_TYPE` | `start_type` | string | ✅ |  | `auto`, `demand`, `disabled` |
| `TYPE` | `type` | string | ✅ |  | `windows service` |
| `USER` | `user` | string | ✅ |  |  |

### IMAGE Nested Fields

Nested fields within `image` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `IMAGE.TYPE` | `type` | string | | `windows service` |
| `IMAGE.PATH` | `path` | string | |  |
| `IMAGE.EXISTS` | `exists` | string | |  |
| `IMAGE.EXTENSION` | `extension` | string | |  |
| `IMAGE.MAGIC_HEADER` | `magic_header` | string | |  |
| `IMAGE.HASHES.MD5` | `hashes.md5` | string | |  |
| `IMAGE.HASHES.SHA1` | `hashes.sha1` | string | |  |
| `IMAGE.HASHES.SHA256` | `hashes.sha256` | string | |  |
| `IMAGE.FIRST_BYTES.HEX` | `first_bytes.hex` | string | |  |
| `IMAGE.FIRST_BYTES.ASCII` | `first_bytes.ascii` | string | |  |
| `IMAGE.FILE_TIMES.MODIFIED` | `file_times.modified` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.ACCESSED` | `file_times.accessed` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.CHANGED` | `file_times.changed` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.CREATED` | `file_times.created` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.USN_CHANGE_TIME` | `file_times.usn_change_time` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.MFT_FILE_NAME_MODIFIED` | `file_times.mft_file_name_modified` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.MFT_FILE_NAME_ACCESSED` | `file_times.mft_file_name_accessed` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.MFT_FILE_NAME_CHANGED` | `file_times.mft_file_name_changed` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.MFT_FILE_NAME_CREATED` | `file_times.mft_file_name_created` | string (date-time) | |  |
| `IMAGE.SIZE` | `size` | integer | |  |
| `IMAGE.PE_INFO.COMPANY` | `pe_info.company` | string | |  |
| `IMAGE.PE_INFO.DESCRIPTION` | `pe_info.description` | string | |  |
| `IMAGE.PE_INFO.LEGAL_COPYRIGHT` | `pe_info.legal_copyright` | string | |  |
| `IMAGE.PE_INFO.PRODUCT` | `pe_info.product` | string | |  |
| `IMAGE.PE_INFO.ORIGINAL_NAME` | `pe_info.original_name` | string | |  |
| `IMAGE.PE_INFO.INTERNAL_NAME` | `pe_info.internal_name` | string | |  |
| `IMAGE.PE_INFO.SIGNED` | `pe_info.signed` | boolean | |  |
| `IMAGE.PE_INFO.SIGNATURES` | `pe_info.signatures` | array | null | |  |
| `IMAGE.PE_INFO.IMPHASH` | `pe_info.imphash` | string | |  |
| `IMAGE.PE_INFO.RICH_HEADER_HASH` | `pe_info.rich_header_hash` | string | |  |
| `IMAGE.PE_INFO.CREATION_TIMESTAMP` | `pe_info.creation_timestamp` | string (date-time) | |  |
| `IMAGE.TARGET` | `target` | string | |  |
| `IMAGE.UNPACK_SOURCE` | `unpack_source` | array | null | |  |
| `IMAGE.LINK_INFO.TARGET` | `link_info.target` | string | |  |
| `IMAGE.LINK_INFO.ARGUMENTS` | `link_info.arguments` | string | |  |
| `IMAGE.LINK_INFO.COMMAND_LINE` | `link_info.command_line` | string | |  |
| `IMAGE.LINK_INFO.CREATED` | `link_info.created` | string (date-time) | |  |
| `IMAGE.LINK_INFO.MODIFIED` | `link_info.modified` | string (date-time) | |  |
| `IMAGE.LINK_INFO.ACCESSED` | `link_info.accessed` | string (date-time) | |  |
| `IMAGE.RECYCLE_BIN_INFO.ORIGINAL_FILE_NAME` | `recycle_bin_info.original_file_name` | string | |  |
| `IMAGE.RECYCLE_BIN_INFO.DELETION_TIME` | `recycle_bin_info.deletion_time` | string (date-time) | |  |
| `IMAGE.RECYCLE_BIN_INFO.ORIGINAL_FILE_SIZE` | `recycle_bin_info.original_file_size` | integer | |  |
| `IMAGE.WER_INFO.TYPE` | `wer_info.type` | string | |  |
| `IMAGE.WER_INFO.EVENT_NAME` | `wer_info.event_name` | string | |  |
| `IMAGE.WER_INFO.EVENT_TYPE` | `wer_info.event_type` | string | |  |
| `IMAGE.WER_INFO.DATE` | `wer_info.date` | string (date-time) | |  |
| `IMAGE.WER_INFO.APP_PATH` | `wer_info.app_path` | string | |  |
| `IMAGE.WER_INFO.APP_NAME` | `wer_info.app_name` | string | |  |
| `IMAGE.WER_INFO.EXE` | `wer_info.exe` | string | |  |
| `IMAGE.WER_INFO.ERROR` | `wer_info.error` | string | |  |
| `IMAGE.WER_INFO.FAULT_IN_MODULE` | `wer_info.fault_in_module` | string | |  |
| `IMAGE.CONTENT.TYPE` | `content.type` | string | |  |
| `IMAGE.CONTENT.ELEMENTS` | `content.elements` | array | null | |  |
| `IMAGE.CONTENT.LENGTH` | `content.length` | integer | |  |
| `IMAGE.BEACON_CONFIG.BEACON_TYPE` | `beacon_config.beacon_type` | string | |  |
| `IMAGE.BEACON_CONFIG.C2` | `beacon_config.c2` | string | |  |
| `IMAGE.BEACON_CONFIG.PORT` | `beacon_config.port` | string | |  |
| `IMAGE.BEACON_CONFIG.SPAWN_TO` | `beacon_config.spawn_to` | string | |  |
| `IMAGE.BEACON_CONFIG.INJECTION_PROCESS` | `beacon_config.injection_process` | string | |  |
| `IMAGE.BEACON_CONFIG.PIPE_NAME` | `beacon_config.pipe_name` | string | |  |
| `IMAGE.BEACON_CONFIG.USER_AGENT` | `beacon_config.user_agent` | string | |  |
| `IMAGE.BEACON_CONFIG.PROXY` | `beacon_config.proxy` | string | |  |
| `IMAGE.BEACON_CONFIG.FULL_CONFIG` | `beacon_config.full_config` | object | |  |
| `IMAGE.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODED` | `beacon_config.cipher_parameters.xaf_encoded` | any | |  |
| `IMAGE.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODING_ANCHOR` | `beacon_config.cipher_parameters.xaf_encoding_anchor` | any | |  |
| `IMAGE.BEACON_CONFIG.CIPHER_PARAMETERS.XOR_KEY` | `beacon_config.cipher_parameters.xor_key` | any | |  |
| `IMAGE.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_OFFSET` | `beacon_config.cipher_parameters.beacon_offset` | any | |  |
| `IMAGE.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_LENGTH` | `beacon_config.cipher_parameters.beacon_length` | any | |  |
| `IMAGE.BEACON_CONFIG.CIPHER_PARAMETERS.BLOCK_START` | `beacon_config.cipher_parameters.block_start` | any | |  |
| `IMAGE.BEACON_CONFIG.CIPHER_PARAMETERS.PAIRWISE_SWAPPED` | `beacon_config.cipher_parameters.pairwise_swapped` | any | |  |
| `IMAGE.VIRUSTOTAL.RESULT` | `virustotal.result` | string | |  |
| `IMAGE.VIRUSTOTAL.POSITIVE_VERDICTS` | `virustotal.positive_verdicts` | integer | |  |
| `IMAGE.VIRUSTOTAL.TOTAL_VERDICTS` | `virustotal.total_verdicts` | integer | |  |
| `IMAGE.VIRUSTOTAL.HISTORY.NAMES` | `virustotal.history.names` | any | |  |
| `IMAGE.VIRUSTOTAL.HISTORY.TAGS` | `virustotal.history.tags` | any | |  |
| `IMAGE.VIRUSTOTAL.HISTORY.SUBMISSIONS` | `virustotal.history.submissions` | any | |  |
| `IMAGE.VIRUSTOTAL.HISTORY.FIRST_SUBMISSION` | `virustotal.history.first_submission` | any | |  |
| `IMAGE.VIRUSTOTAL.HISTORY.LAST_SUBMISSION` | `virustotal.history.last_submission` | any | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Windows service"

detection:
    selection:
        PATH|contains:
            - '/tmp/'
            - '/dev/shm/'
            - '\\Temp\\'
        FAILURE_COMMAND|contains|all:
            - 'powershell'
            - '-encodedcommand'
        KEY_NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
        DESCRIPTION|contains:
            - '192.168.'
            - '10.'
    filter_legitimate:
        PE_INFO|SIGNED: 'true'
        USER|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
