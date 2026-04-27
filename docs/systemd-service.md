# systemd service

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/systemd-service` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `SystemdService`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `COMMAND` | `command` | string | ✅ |  | `/usr/sbin/sshd -D`, `/usr/local/bin/ollama serve`, `bash -c exec /opt/aurora-linux/aurora` |
| `IMAGE` | `image` | object | ✅ | Object, see [IMAGE Nested Fields](#image-nested-fields) below |  |
| `RUN_AS_GROUP` | `run_as_group` | string | ✅ |  | `root`, `ollama`, `` |
| `RUN_AS_USER` | `run_as_user` | string | ✅ |  | `root`, `ollama`, `` |
| `TYPE` | `type` | string | ✅ |  | `systemd service` |
| `UNIT` | `unit` | object | ✅ | Object, see [UNIT Nested Fields](#unit-nested-fields) below |  |

### IMAGE Nested Fields

Nested fields within `image` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `IMAGE.TYPE` | `type` | string | | `systemd service` |
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


### UNIT Nested Fields

Nested fields within `unit` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `UNIT.TYPE` | `type` | string | | `systemd service` |
| `UNIT.PATH` | `path` | string | |  |
| `UNIT.EXISTS` | `exists` | string | |  |
| `UNIT.EXTENSION` | `extension` | string | |  |
| `UNIT.MAGIC_HEADER` | `magic_header` | string | |  |
| `UNIT.HASHES.MD5` | `hashes.md5` | string | |  |
| `UNIT.HASHES.SHA1` | `hashes.sha1` | string | |  |
| `UNIT.HASHES.SHA256` | `hashes.sha256` | string | |  |
| `UNIT.FIRST_BYTES.HEX` | `first_bytes.hex` | string | |  |
| `UNIT.FIRST_BYTES.ASCII` | `first_bytes.ascii` | string | |  |
| `UNIT.FILE_TIMES.MODIFIED` | `file_times.modified` | string (date-time) | |  |
| `UNIT.FILE_TIMES.ACCESSED` | `file_times.accessed` | string (date-time) | |  |
| `UNIT.FILE_TIMES.CHANGED` | `file_times.changed` | string (date-time) | |  |
| `UNIT.FILE_TIMES.CREATED` | `file_times.created` | string (date-time) | |  |
| `UNIT.FILE_TIMES.USN_CHANGE_TIME` | `file_times.usn_change_time` | string (date-time) | |  |
| `UNIT.FILE_TIMES.MFT_FILE_NAME_MODIFIED` | `file_times.mft_file_name_modified` | string (date-time) | |  |
| `UNIT.FILE_TIMES.MFT_FILE_NAME_ACCESSED` | `file_times.mft_file_name_accessed` | string (date-time) | |  |
| `UNIT.FILE_TIMES.MFT_FILE_NAME_CHANGED` | `file_times.mft_file_name_changed` | string (date-time) | |  |
| `UNIT.FILE_TIMES.MFT_FILE_NAME_CREATED` | `file_times.mft_file_name_created` | string (date-time) | |  |
| `UNIT.SIZE` | `size` | integer | |  |
| `UNIT.PE_INFO.COMPANY` | `pe_info.company` | string | |  |
| `UNIT.PE_INFO.DESCRIPTION` | `pe_info.description` | string | |  |
| `UNIT.PE_INFO.LEGAL_COPYRIGHT` | `pe_info.legal_copyright` | string | |  |
| `UNIT.PE_INFO.PRODUCT` | `pe_info.product` | string | |  |
| `UNIT.PE_INFO.ORIGINAL_NAME` | `pe_info.original_name` | string | |  |
| `UNIT.PE_INFO.INTERNAL_NAME` | `pe_info.internal_name` | string | |  |
| `UNIT.PE_INFO.SIGNED` | `pe_info.signed` | boolean | |  |
| `UNIT.PE_INFO.SIGNATURES` | `pe_info.signatures` | array | null | |  |
| `UNIT.PE_INFO.IMPHASH` | `pe_info.imphash` | string | |  |
| `UNIT.PE_INFO.RICH_HEADER_HASH` | `pe_info.rich_header_hash` | string | |  |
| `UNIT.PE_INFO.CREATION_TIMESTAMP` | `pe_info.creation_timestamp` | string (date-time) | |  |
| `UNIT.TARGET` | `target` | string | |  |
| `UNIT.UNPACK_SOURCE` | `unpack_source` | array | null | |  |
| `UNIT.LINK_INFO.TARGET` | `link_info.target` | string | |  |
| `UNIT.LINK_INFO.ARGUMENTS` | `link_info.arguments` | string | |  |
| `UNIT.LINK_INFO.COMMAND_LINE` | `link_info.command_line` | string | |  |
| `UNIT.LINK_INFO.CREATED` | `link_info.created` | string (date-time) | |  |
| `UNIT.LINK_INFO.MODIFIED` | `link_info.modified` | string (date-time) | |  |
| `UNIT.LINK_INFO.ACCESSED` | `link_info.accessed` | string (date-time) | |  |
| `UNIT.RECYCLE_BIN_INFO.ORIGINAL_FILE_NAME` | `recycle_bin_info.original_file_name` | string | |  |
| `UNIT.RECYCLE_BIN_INFO.DELETION_TIME` | `recycle_bin_info.deletion_time` | string (date-time) | |  |
| `UNIT.RECYCLE_BIN_INFO.ORIGINAL_FILE_SIZE` | `recycle_bin_info.original_file_size` | integer | |  |
| `UNIT.WER_INFO.TYPE` | `wer_info.type` | string | |  |
| `UNIT.WER_INFO.EVENT_NAME` | `wer_info.event_name` | string | |  |
| `UNIT.WER_INFO.EVENT_TYPE` | `wer_info.event_type` | string | |  |
| `UNIT.WER_INFO.DATE` | `wer_info.date` | string (date-time) | |  |
| `UNIT.WER_INFO.APP_PATH` | `wer_info.app_path` | string | |  |
| `UNIT.WER_INFO.APP_NAME` | `wer_info.app_name` | string | |  |
| `UNIT.WER_INFO.EXE` | `wer_info.exe` | string | |  |
| `UNIT.WER_INFO.ERROR` | `wer_info.error` | string | |  |
| `UNIT.WER_INFO.FAULT_IN_MODULE` | `wer_info.fault_in_module` | string | |  |
| `UNIT.CONTENT.TYPE` | `content.type` | string | |  |
| `UNIT.CONTENT.ELEMENTS` | `content.elements` | array | null | |  |
| `UNIT.CONTENT.LENGTH` | `content.length` | integer | |  |
| `UNIT.BEACON_CONFIG.BEACON_TYPE` | `beacon_config.beacon_type` | string | |  |
| `UNIT.BEACON_CONFIG.C2` | `beacon_config.c2` | string | |  |
| `UNIT.BEACON_CONFIG.PORT` | `beacon_config.port` | string | |  |
| `UNIT.BEACON_CONFIG.SPAWN_TO` | `beacon_config.spawn_to` | string | |  |
| `UNIT.BEACON_CONFIG.INJECTION_PROCESS` | `beacon_config.injection_process` | string | |  |
| `UNIT.BEACON_CONFIG.PIPE_NAME` | `beacon_config.pipe_name` | string | |  |
| `UNIT.BEACON_CONFIG.USER_AGENT` | `beacon_config.user_agent` | string | |  |
| `UNIT.BEACON_CONFIG.PROXY` | `beacon_config.proxy` | string | |  |
| `UNIT.BEACON_CONFIG.FULL_CONFIG` | `beacon_config.full_config` | object | |  |
| `UNIT.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODED` | `beacon_config.cipher_parameters.xaf_encoded` | any | |  |
| `UNIT.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODING_ANCHOR` | `beacon_config.cipher_parameters.xaf_encoding_anchor` | any | |  |
| `UNIT.BEACON_CONFIG.CIPHER_PARAMETERS.XOR_KEY` | `beacon_config.cipher_parameters.xor_key` | any | |  |
| `UNIT.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_OFFSET` | `beacon_config.cipher_parameters.beacon_offset` | any | |  |
| `UNIT.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_LENGTH` | `beacon_config.cipher_parameters.beacon_length` | any | |  |
| `UNIT.BEACON_CONFIG.CIPHER_PARAMETERS.BLOCK_START` | `beacon_config.cipher_parameters.block_start` | any | |  |
| `UNIT.BEACON_CONFIG.CIPHER_PARAMETERS.PAIRWISE_SWAPPED` | `beacon_config.cipher_parameters.pairwise_swapped` | any | |  |
| `UNIT.VIRUSTOTAL.RESULT` | `virustotal.result` | string | |  |
| `UNIT.VIRUSTOTAL.POSITIVE_VERDICTS` | `virustotal.positive_verdicts` | integer | |  |
| `UNIT.VIRUSTOTAL.TOTAL_VERDICTS` | `virustotal.total_verdicts` | integer | |  |
| `UNIT.VIRUSTOTAL.HISTORY.NAMES` | `virustotal.history.names` | any | |  |
| `UNIT.VIRUSTOTAL.HISTORY.TAGS` | `virustotal.history.tags` | any | |  |
| `UNIT.VIRUSTOTAL.HISTORY.SUBMISSIONS` | `virustotal.history.submissions` | any | |  |
| `UNIT.VIRUSTOTAL.HISTORY.FIRST_SUBMISSION` | `virustotal.history.first_submission` | any | |  |
| `UNIT.VIRUSTOTAL.HISTORY.LAST_SUBMISSION` | `virustotal.history.last_submission` | any | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "systemd service"

detection:
    selection:
        PATH|contains:
            - '/tmp/'
            - '/dev/shm/'
            - '\\Temp\\'
        COMMAND|contains|all:
            - 'powershell'
            - '-encodedcommand'
        TYPE: 'relevant_type'
    filter_legitimate:
        PE_INFO|SIGNED: 'true'
        RUN_AS_USER|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
