# process

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/process` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Process`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `BEACON_CONFIG` | `beacon_config` | object |  | nested: `BEACON_TYPE`: string; `C2`: string; `PORT`: string; `SPAWN_TO`: string; `INJECTION_PROCESS`: string; `PIPE_NAME`: string; `USER_AGENT`: string; `PROXY`: string; `FULL_CONFIG`: object; `CIPHER_PARAMETERS|XAF_ENCODED`: boolean; `CIPHER_PARAMETERS|XAF_ENCODING_ANCHOR`: integer; `CIPHER_PARAMETERS|XOR_KEY`: integer; `CIPHER_PARAMETERS|BEACON_OFFSET`: integer; `CIPHER_PARAMETERS|BEACON_LENGTH`: integer; `CIPHER_PARAMETERS|BLOCK_START|HEX`: any; `CIPHER_PARAMETERS|BLOCK_START|ASCII`: any; `CIPHER_PARAMETERS|PAIRWISE_SWAPPED`: boolean |  |
| `COMMAND` | `command` | string | ✅ |  | `/usr/lib/systemd/systemd --switched-root...`, `/tmp/stub-server -port 19992 -tls-genera...`, `/usr/bin/python3 -m http.server 19993` |
| `CONNECTIONS` | `connections` | array | null | ✅ |  |  |
| `CREATED` | `created` | string (date-time) | ✅ |  | `2026-02-25T20:03:04+01:00`, `2026-04-26T11:55:48+02:00` |
| `DEAD` | `dead` | boolean |  |  | `false`, `true` |
| `IMAGE` | `image` | object | ✅ | nested: `TYPE`: string; `PATH`: string; `EXISTS`: string; `EXTENSION`: string; `MAGIC_HEADER`: string; `HASHES|MD5`: string; `HASHES|SHA1`: string; `HASHES|SHA256`: string; `FIRST_BYTES|HEX`: string; `FIRST_BYTES|ASCII`: string; `FILE_TIMES|MODIFIED`: string (date-time); `FILE_TIMES|ACCESSED`: string (date-time); `FILE_TIMES|CHANGED`: string (date-time); `FILE_TIMES|CREATED`: string (date-time); `FILE_TIMES|USN_CHANGE_TIME`: string (date-time); `FILE_TIMES|MFT_FILE_NAME_MODIFIED`: string (date-time); `FILE_TIMES|MFT_FILE_NAME_ACCESSED`: string (date-time); `FILE_TIMES|MFT_FILE_NAME_CHANGED`: string (date-time); `FILE_TIMES|MFT_FILE_NAME_CREATED`: string (date-time); `SIZE`: integer; `PE_INFO|COMPANY`: string; `PE_INFO|DESCRIPTION`: string; `PE_INFO|LEGAL_COPYRIGHT`: string; `PE_INFO|PRODUCT`: string; `PE_INFO|ORIGINAL_NAME`: string; `PE_INFO|INTERNAL_NAME`: string; `PE_INFO|SIGNED`: boolean; `PE_INFO|SIGNATURES`: array | null; `PE_INFO|IMPHASH`: string; `PE_INFO|RICH_HEADER_HASH`: string; `PE_INFO|CREATION_TIMESTAMP`: string (date-time); `TARGET`: string; `UNPACK_SOURCE`: array | null; `LINK_INFO|TARGET`: string; `LINK_INFO|ARGUMENTS`: string; `LINK_INFO|COMMAND_LINE`: string; `LINK_INFO|CREATED`: string (date-time); `LINK_INFO|MODIFIED`: string (date-time); `LINK_INFO|ACCESSED`: string (date-time); `RECYCLE_BIN_INFO|ORIGINAL_FILE_NAME`: string; `RECYCLE_BIN_INFO|DELETION_TIME`: string (date-time); `RECYCLE_BIN_INFO|ORIGINAL_FILE_SIZE`: integer; `WER_INFO|TYPE`: string; `WER_INFO|EVENT_NAME`: string; `WER_INFO|EVENT_TYPE`: string; `WER_INFO|DATE`: string (date-time); `WER_INFO|APP_PATH`: string; `WER_INFO|APP_NAME`: string; `WER_INFO|EXE`: string; `WER_INFO|ERROR`: string; `WER_INFO|FAULT_IN_MODULE`: string; `CONTENT|TYPE`: string; `CONTENT|ELEMENTS`: array | null; `CONTENT|LENGTH`: integer; `BEACON_CONFIG|BEACON_TYPE`: string; `BEACON_CONFIG|C2`: string; `BEACON_CONFIG|PORT`: string; `BEACON_CONFIG|SPAWN_TO`: string; `BEACON_CONFIG|INJECTION_PROCESS`: string; `BEACON_CONFIG|PIPE_NAME`: string; `BEACON_CONFIG|USER_AGENT`: string; `BEACON_CONFIG|PROXY`: string; `BEACON_CONFIG|FULL_CONFIG`: object; `BEACON_CONFIG|CIPHER_PARAMETERS|XAF_ENCODED`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|XAF_ENCODING_ANCHOR`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|XOR_KEY`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|BEACON_OFFSET`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|BEACON_LENGTH`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|BLOCK_START`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|PAIRWISE_SWAPPED`: any; `VIRUSTOTAL|RESULT`: string; `VIRUSTOTAL|POSITIVE_VERDICTS`: integer; `VIRUSTOTAL|TOTAL_VERDICTS`: integer; `VIRUSTOTAL|HISTORY|NAMES`: any; `VIRUSTOTAL|HISTORY|TAGS`: any; `VIRUSTOTAL|HISTORY|SUBMISSIONS`: any; `VIRUSTOTAL|HISTORY|FIRST_SUBMISSION`: any; `VIRUSTOTAL|HISTORY|LAST_SUBMISSION`: any |  |
| `LISTEN_PORTS` | `listen_ports` | array | null | ✅ |  | `22`, `80`, `443` |
| `NAME` | `name` | string | ✅ |  | `stub-server`, `thunderstorm-stub-server`, `bash` |
| `OWNER` | `owner` | string | ✅ |  | `root`, `neo`, `sssd` |
| `PARENT_INFO` | `parent_info` | object |  | nested: `PID`: integer; `EXE`: string; `COMMAND`: string |  |
| `PE_SIEVE` | `pe_sieve` | object |  | nested: `SUSPICIOUS_SECTIONS`: integer; `REPLACED`: integer; `HDR_MOD`: integer; `UNREACHABLE_FILE`: integer; `PATCHED`: integer; `IAT_HOOKED`: integer; `IMPLANTED`: integer; `OTHER`: integer; `SKIPPED`: integer; `ERRORS`: integer |  |
| `PID` | `pid` | integer | ✅ |  | `1`, `214681`, `2801945` |
| `SECTIONS` | `sections` | array of object |  |  |  |
| `SESSION` | `session` | string | ✅ |  | ``, `neo` |
| `TREE` | `tree` | array | null | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

**BEACON_CONFIG** (`beacon_config` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `BEACON_TYPE` | `beacon_type` | string |
| `C2` | `c2` | string |
| `PORT` | `port` | string |
| `SPAWN_TO` | `spawn_to` | string |
| `INJECTION_PROCESS` | `injection_process` | string |
| `PIPE_NAME` | `pipe_name` | string |
| `USER_AGENT` | `user_agent` | string |
| `PROXY` | `proxy` | string |
| `FULL_CONFIG` | `full_config` | object |
| `CIPHER_PARAMETERS|XAF_ENCODED` | `cipher_parameters.xaf_encoded` | boolean |
| `CIPHER_PARAMETERS|XAF_ENCODING_ANCHOR` | `cipher_parameters.xaf_encoding_anchor` | integer |
| `CIPHER_PARAMETERS|XOR_KEY` | `cipher_parameters.xor_key` | integer |
| `CIPHER_PARAMETERS|BEACON_OFFSET` | `cipher_parameters.beacon_offset` | integer |
| `CIPHER_PARAMETERS|BEACON_LENGTH` | `cipher_parameters.beacon_length` | integer |
| `CIPHER_PARAMETERS|BLOCK_START|HEX` | `cipher_parameters.block_start.hex` | any |
| `CIPHER_PARAMETERS|BLOCK_START|ASCII` | `cipher_parameters.block_start.ascii` | any |
| `CIPHER_PARAMETERS|PAIRWISE_SWAPPED` | `cipher_parameters.pairwise_swapped` | boolean |

**IMAGE** (`image` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `TYPE` | `type` | string |
| `PATH` | `path` | string |
| `EXISTS` | `exists` | string |
| `EXTENSION` | `extension` | string |
| `MAGIC_HEADER` | `magic_header` | string |
| `HASHES|MD5` | `hashes.md5` | string |
| `HASHES|SHA1` | `hashes.sha1` | string |
| `HASHES|SHA256` | `hashes.sha256` | string |
| `FIRST_BYTES|HEX` | `first_bytes.hex` | string |
| `FIRST_BYTES|ASCII` | `first_bytes.ascii` | string |
| `FILE_TIMES|MODIFIED` | `file_times.modified` | string (date-time) |
| `FILE_TIMES|ACCESSED` | `file_times.accessed` | string (date-time) |
| `FILE_TIMES|CHANGED` | `file_times.changed` | string (date-time) |
| `FILE_TIMES|CREATED` | `file_times.created` | string (date-time) |
| `FILE_TIMES|USN_CHANGE_TIME` | `file_times.usn_change_time` | string (date-time) |
| `FILE_TIMES|MFT_FILE_NAME_MODIFIED` | `file_times.mft_file_name_modified` | string (date-time) |
| `FILE_TIMES|MFT_FILE_NAME_ACCESSED` | `file_times.mft_file_name_accessed` | string (date-time) |
| `FILE_TIMES|MFT_FILE_NAME_CHANGED` | `file_times.mft_file_name_changed` | string (date-time) |
| `FILE_TIMES|MFT_FILE_NAME_CREATED` | `file_times.mft_file_name_created` | string (date-time) |
| `SIZE` | `size` | integer |
| `PE_INFO|COMPANY` | `pe_info.company` | string |
| `PE_INFO|DESCRIPTION` | `pe_info.description` | string |
| `PE_INFO|LEGAL_COPYRIGHT` | `pe_info.legal_copyright` | string |
| `PE_INFO|PRODUCT` | `pe_info.product` | string |
| `PE_INFO|ORIGINAL_NAME` | `pe_info.original_name` | string |
| `PE_INFO|INTERNAL_NAME` | `pe_info.internal_name` | string |
| `PE_INFO|SIGNED` | `pe_info.signed` | boolean |
| `PE_INFO|SIGNATURES` | `pe_info.signatures` | array | null |
| `PE_INFO|IMPHASH` | `pe_info.imphash` | string |
| `PE_INFO|RICH_HEADER_HASH` | `pe_info.rich_header_hash` | string |
| `PE_INFO|CREATION_TIMESTAMP` | `pe_info.creation_timestamp` | string (date-time) |
| `TARGET` | `target` | string |
| `UNPACK_SOURCE` | `unpack_source` | array | null |
| `LINK_INFO|TARGET` | `link_info.target` | string |
| `LINK_INFO|ARGUMENTS` | `link_info.arguments` | string |
| `LINK_INFO|COMMAND_LINE` | `link_info.command_line` | string |
| `LINK_INFO|CREATED` | `link_info.created` | string (date-time) |
| `LINK_INFO|MODIFIED` | `link_info.modified` | string (date-time) |
| `LINK_INFO|ACCESSED` | `link_info.accessed` | string (date-time) |
| `RECYCLE_BIN_INFO|ORIGINAL_FILE_NAME` | `recycle_bin_info.original_file_name` | string |
| `RECYCLE_BIN_INFO|DELETION_TIME` | `recycle_bin_info.deletion_time` | string (date-time) |
| `RECYCLE_BIN_INFO|ORIGINAL_FILE_SIZE` | `recycle_bin_info.original_file_size` | integer |
| `WER_INFO|TYPE` | `wer_info.type` | string |
| `WER_INFO|EVENT_NAME` | `wer_info.event_name` | string |
| `WER_INFO|EVENT_TYPE` | `wer_info.event_type` | string |
| `WER_INFO|DATE` | `wer_info.date` | string (date-time) |
| `WER_INFO|APP_PATH` | `wer_info.app_path` | string |
| `WER_INFO|APP_NAME` | `wer_info.app_name` | string |
| `WER_INFO|EXE` | `wer_info.exe` | string |
| `WER_INFO|ERROR` | `wer_info.error` | string |
| `WER_INFO|FAULT_IN_MODULE` | `wer_info.fault_in_module` | string |
| `CONTENT|TYPE` | `content.type` | string |
| `CONTENT|ELEMENTS` | `content.elements` | array | null |
| `CONTENT|LENGTH` | `content.length` | integer |
| `BEACON_CONFIG|BEACON_TYPE` | `beacon_config.beacon_type` | string |
| `BEACON_CONFIG|C2` | `beacon_config.c2` | string |
| `BEACON_CONFIG|PORT` | `beacon_config.port` | string |
| `BEACON_CONFIG|SPAWN_TO` | `beacon_config.spawn_to` | string |
| `BEACON_CONFIG|INJECTION_PROCESS` | `beacon_config.injection_process` | string |
| `BEACON_CONFIG|PIPE_NAME` | `beacon_config.pipe_name` | string |
| `BEACON_CONFIG|USER_AGENT` | `beacon_config.user_agent` | string |
| `BEACON_CONFIG|PROXY` | `beacon_config.proxy` | string |
| `BEACON_CONFIG|FULL_CONFIG` | `beacon_config.full_config` | object |
| `BEACON_CONFIG|CIPHER_PARAMETERS|XAF_ENCODED` | `beacon_config.cipher_parameters.xaf_encoded` | any |
| `BEACON_CONFIG|CIPHER_PARAMETERS|XAF_ENCODING_ANCHOR` | `beacon_config.cipher_parameters.xaf_encoding_anchor` | any |
| `BEACON_CONFIG|CIPHER_PARAMETERS|XOR_KEY` | `beacon_config.cipher_parameters.xor_key` | any |
| `BEACON_CONFIG|CIPHER_PARAMETERS|BEACON_OFFSET` | `beacon_config.cipher_parameters.beacon_offset` | any |
| `BEACON_CONFIG|CIPHER_PARAMETERS|BEACON_LENGTH` | `beacon_config.cipher_parameters.beacon_length` | any |
| `BEACON_CONFIG|CIPHER_PARAMETERS|BLOCK_START` | `beacon_config.cipher_parameters.block_start` | any |
| `BEACON_CONFIG|CIPHER_PARAMETERS|PAIRWISE_SWAPPED` | `beacon_config.cipher_parameters.pairwise_swapped` | any |
| `VIRUSTOTAL|RESULT` | `virustotal.result` | string |
| `VIRUSTOTAL|POSITIVE_VERDICTS` | `virustotal.positive_verdicts` | integer |
| `VIRUSTOTAL|TOTAL_VERDICTS` | `virustotal.total_verdicts` | integer |
| `VIRUSTOTAL|HISTORY|NAMES` | `virustotal.history.names` | any |
| `VIRUSTOTAL|HISTORY|TAGS` | `virustotal.history.tags` | any |
| `VIRUSTOTAL|HISTORY|SUBMISSIONS` | `virustotal.history.submissions` | any |
| `VIRUSTOTAL|HISTORY|FIRST_SUBMISSION` | `virustotal.history.first_submission` | any |
| `VIRUSTOTAL|HISTORY|LAST_SUBMISSION` | `virustotal.history.last_submission` | any |

**PARENT_INFO** (`parent_info` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `PID` | `pid` | integer |
| `EXE` | `exe` | string |
| `COMMAND` | `command` | string |

**PE_SIEVE** (`pe_sieve` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `SUSPICIOUS_SECTIONS` | `suspicious_sections` | integer |
| `REPLACED` | `replaced` | integer |
| `HDR_MOD` | `hdr_mod` | integer |
| `UNREACHABLE_FILE` | `unreachable_file` | integer |
| `PATCHED` | `patched` | integer |
| `IAT_HOOKED` | `iat_hooked` | integer |
| `IMPLANTED` | `implanted` | integer |
| `OTHER` | `other` | integer |
| `SKIPPED` | `skipped` | integer |
| `ERRORS` | `errors` | integer |

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
