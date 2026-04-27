# process

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/process` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Process`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `BEACON_CONFIG` | `beacon_config` | object |  | Object, see [BEACON_CONFIG Nested Fields](#beacon_config-nested-fields) below |  |
| `COMMAND` | `command` | string | ✅ |  | `/usr/lib/systemd/systemd --switched-root...`, `/tmp/stub-server -port 19992 -tls-genera...`, `/usr/bin/python3 -m http.server 19993` |
| `CONNECTIONS` | `connections` | array | null | ✅ |  |  |
| `CREATED` | `created` | string (date-time) | ✅ |  | `2026-02-25T20:03:04+01:00`, `2026-04-26T11:55:48+02:00` |
| `DEAD` | `dead` | boolean |  |  | `false`, `true` |
| `IMAGE` | `image` | object | ✅ | Object, see [IMAGE Nested Fields](#image-nested-fields) below |  |
| `LISTEN_PORTS` | `listen_ports` | array | null | ✅ |  | `22`, `80`, `443` |
| `NAME` | `name` | string | ✅ |  | `stub-server`, `thunderstorm-stub-server`, `bash` |
| `OWNER` | `owner` | string | ✅ |  | `root`, `neo`, `sssd` |
| `PARENT_INFO` | `parent_info` | object |  | Object, see [PARENT_INFO Nested Fields](#parent_info-nested-fields) below |  |
| `PE_SIEVE` | `pe_sieve` | object |  | Object, see [PE_SIEVE Nested Fields](#pe_sieve-nested-fields) below |  |
| `PID` | `pid` | integer | ✅ |  | `1`, `214681`, `2801945` |
| `SECTIONS` | `sections` | array of object |  |  |  |
| `SESSION` | `session` | string | ✅ |  | ``, `neo` |
| `TREE` | `tree` | array | null | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### BEACON_CONFIG Nested Fields

Nested fields within `beacon_config` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `BEACON_CONFIG.BEACON_TYPE` | `beacon_type` | string | |  |
| `BEACON_CONFIG.C2` | `c2` | string | |  |
| `BEACON_CONFIG.PORT` | `port` | string | |  |
| `BEACON_CONFIG.SPAWN_TO` | `spawn_to` | string | |  |
| `BEACON_CONFIG.INJECTION_PROCESS` | `injection_process` | string | |  |
| `BEACON_CONFIG.PIPE_NAME` | `pipe_name` | string | |  |
| `BEACON_CONFIG.USER_AGENT` | `user_agent` | string | |  |
| `BEACON_CONFIG.PROXY` | `proxy` | string | |  |
| `BEACON_CONFIG.FULL_CONFIG` | `full_config` | object | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODED` | `cipher_parameters.xaf_encoded` | boolean | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODING_ANCHOR` | `cipher_parameters.xaf_encoding_anchor` | integer | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.XOR_KEY` | `cipher_parameters.xor_key` | integer | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_OFFSET` | `cipher_parameters.beacon_offset` | integer | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_LENGTH` | `cipher_parameters.beacon_length` | integer | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.BLOCK_START.HEX` | `cipher_parameters.block_start.hex` | any | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.BLOCK_START.ASCII` | `cipher_parameters.block_start.ascii` | any | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.PAIRWISE_SWAPPED` | `cipher_parameters.pairwise_swapped` | boolean | |  |


### IMAGE Nested Fields

Nested fields within `image` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `IMAGE.TYPE` | `type` | string | |  |
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


### PARENT_INFO Nested Fields

Nested fields within `parent_info` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `PARENT_INFO.PID` | `pid` | integer | | `1`, `214681`, `2801945` |
| `PARENT_INFO.EXE` | `exe` | string | |  |
| `PARENT_INFO.COMMAND` | `command` | string | | `/usr/lib/systemd/systemd --switched-root...`, `/tmp/stub-server -port 19992 -tls-genera...`, `/usr/bin/python3 -m http.server 19993` |


### PE_SIEVE Nested Fields

Nested fields within `pe_sieve` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `PE_SIEVE.SUSPICIOUS_SECTIONS` | `suspicious_sections` | integer | |  |
| `PE_SIEVE.REPLACED` | `replaced` | integer | |  |
| `PE_SIEVE.HDR_MOD` | `hdr_mod` | integer | |  |
| `PE_SIEVE.UNREACHABLE_FILE` | `unreachable_file` | integer | |  |
| `PE_SIEVE.PATCHED` | `patched` | integer | |  |
| `PE_SIEVE.IAT_HOOKED` | `iat_hooked` | integer | |  |
| `PE_SIEVE.IMPLANTED` | `implanted` | integer | |  |
| `PE_SIEVE.OTHER` | `other` | integer | |  |
| `PE_SIEVE.SKIPPED` | `skipped` | integer | |  |
| `PE_SIEVE.ERRORS` | `errors` | integer | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "process"

detection:
    selection:
        PATH|contains:
            - '/tmp/'
            - '/dev/shm/'
            - '\\Temp\\'
        COMMAND|contains|all:
            - 'powershell'
            - '-encodedcommand'
        NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    filter_legitimate:
        PE_INFO|SIGNED: 'true'
    condition: selection and not filter_legitimate
```
