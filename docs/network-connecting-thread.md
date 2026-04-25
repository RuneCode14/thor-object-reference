# network connecting thread

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/network-connecting-thread` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `NetworkConnectingThread`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `CALLBACK_INTERVAL` | `callback_interval` | integer | ✅ |  |
| `CONNECTIONS` | `connections` | array of object | ✅ |  |
| `PROCESS` | `process` | object | ✅ | nested: `TYPE`: string; `PID`: integer; `DEAD`: boolean; `NAME`: string; `COMMAND`: string; `OWNER`: string; `IMAGE|TYPE`: string; `IMAGE|PATH`: string; `IMAGE|EXISTS`: string; `IMAGE|EXTENSION`: string; `IMAGE|MAGIC_HEADER`: string; `IMAGE|HASHES|MD5`: any; `IMAGE|HASHES|SHA1`: any; `IMAGE|HASHES|SHA256`: any; `IMAGE|FIRST_BYTES|HEX`: any; `IMAGE|FIRST_BYTES|ASCII`: any; `IMAGE|FILE_TIMES|MODIFIED`: any; `IMAGE|FILE_TIMES|ACCESSED`: any; `IMAGE|FILE_TIMES|CHANGED`: any; `IMAGE|FILE_TIMES|CREATED`: any; `IMAGE|FILE_TIMES|USN_CHANGE_TIME`: any; `IMAGE|FILE_TIMES|MFT_FILE_NAME_MODIFIED`: any; `IMAGE|FILE_TIMES|MFT_FILE_NAME_ACCESSED`: any; `IMAGE|FILE_TIMES|MFT_FILE_NAME_CHANGED`: any; `IMAGE|FILE_TIMES|MFT_FILE_NAME_CREATED`: any; `IMAGE|SIZE`: integer; `IMAGE|PE_INFO|COMPANY`: any; `IMAGE|PE_INFO|DESCRIPTION`: any; `IMAGE|PE_INFO|LEGAL_COPYRIGHT`: any; `IMAGE|PE_INFO|PRODUCT`: any; `IMAGE|PE_INFO|ORIGINAL_NAME`: any; `IMAGE|PE_INFO|INTERNAL_NAME`: any; `IMAGE|PE_INFO|SIGNED`: any; `IMAGE|PE_INFO|SIGNATURES`: any; `IMAGE|PE_INFO|IMPHASH`: any; `IMAGE|PE_INFO|RICH_HEADER_HASH`: any; `IMAGE|PE_INFO|CREATION_TIMESTAMP`: any; `IMAGE|TARGET`: string; `IMAGE|UNPACK_SOURCE`: any | null; `IMAGE|LINK_INFO|TARGET`: any; `IMAGE|LINK_INFO|ARGUMENTS`: any; `IMAGE|LINK_INFO|COMMAND_LINE`: any; `IMAGE|LINK_INFO|CREATED`: any; `IMAGE|LINK_INFO|MODIFIED`: any; `IMAGE|LINK_INFO|ACCESSED`: any; `IMAGE|RECYCLE_BIN_INFO|ORIGINAL_FILE_NAME`: any; `IMAGE|RECYCLE_BIN_INFO|DELETION_TIME`: any; `IMAGE|RECYCLE_BIN_INFO|ORIGINAL_FILE_SIZE`: any; `IMAGE|WER_INFO|TYPE`: any; `IMAGE|WER_INFO|EVENT_NAME`: any; `IMAGE|WER_INFO|EVENT_TYPE`: any; `IMAGE|WER_INFO|DATE`: any; `IMAGE|WER_INFO|APP_PATH`: any; `IMAGE|WER_INFO|APP_NAME`: any; `IMAGE|WER_INFO|EXE`: any; `IMAGE|WER_INFO|ERROR`: any; `IMAGE|WER_INFO|FAULT_IN_MODULE`: any; `IMAGE|CONTENT|TYPE`: any; `IMAGE|CONTENT|ELEMENTS`: any; `IMAGE|CONTENT|LENGTH`: any; `IMAGE|BEACON_CONFIG|BEACON_TYPE`: any; `IMAGE|BEACON_CONFIG|C2`: any; `IMAGE|BEACON_CONFIG|PORT`: any; `IMAGE|BEACON_CONFIG|SPAWN_TO`: any; `IMAGE|BEACON_CONFIG|INJECTION_PROCESS`: any; `IMAGE|BEACON_CONFIG|PIPE_NAME`: any; `IMAGE|BEACON_CONFIG|USER_AGENT`: any; `IMAGE|BEACON_CONFIG|PROXY`: any; `IMAGE|BEACON_CONFIG|FULL_CONFIG`: any; `IMAGE|BEACON_CONFIG|CIPHER_PARAMETERS`: any; `IMAGE|VIRUSTOTAL|RESULT`: any; `IMAGE|VIRUSTOTAL|POSITIVE_VERDICTS`: any; `IMAGE|VIRUSTOTAL|TOTAL_VERDICTS`: any; `IMAGE|VIRUSTOTAL|HISTORY`: any; `PARENT_INFO|PID`: integer; `PARENT_INFO|EXE`: string; `PARENT_INFO|COMMAND`: string; `TREE`: array | null; `CREATED`: string (date-time); `SESSION`: string; `LISTEN_PORTS`: array | null; `CONNECTIONS`: array | null; `SECTIONS`: array of object; `BEACON_CONFIG|BEACON_TYPE`: string; `BEACON_CONFIG|C2`: string; `BEACON_CONFIG|PORT`: string; `BEACON_CONFIG|SPAWN_TO`: string; `BEACON_CONFIG|INJECTION_PROCESS`: string; `BEACON_CONFIG|PIPE_NAME`: string; `BEACON_CONFIG|USER_AGENT`: string; `BEACON_CONFIG|PROXY`: string; `BEACON_CONFIG|FULL_CONFIG`: object; `BEACON_CONFIG|CIPHER_PARAMETERS|XAF_ENCODED`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|XAF_ENCODING_ANCHOR`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|XOR_KEY`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|BEACON_OFFSET`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|BEACON_LENGTH`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|BLOCK_START`: any; `BEACON_CONFIG|CIPHER_PARAMETERS|PAIRWISE_SWAPPED`: any; `PE_SIEVE|SUSPICIOUS_SECTIONS`: integer; `PE_SIEVE|REPLACED`: integer; `PE_SIEVE|HDR_MOD`: integer; `PE_SIEVE|UNREACHABLE_FILE`: integer; `PE_SIEVE|PATCHED`: integer; `PE_SIEVE|IAT_HOOKED`: integer; `PE_SIEVE|IMPLANTED`: integer; `PE_SIEVE|OTHER`: integer; `PE_SIEVE|SKIPPED`: integer; `PE_SIEVE|ERRORS`: integer |
| `THREAD_ID` | `thread_id` | integer | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

**PROCESS** (`process` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `TYPE` | `type` | string |
| `PID` | `pid` | integer |
| `DEAD` | `dead` | boolean |
| `NAME` | `name` | string |
| `COMMAND` | `command` | string |
| `OWNER` | `owner` | string |
| `IMAGE|TYPE` | `image.type` | string |
| `IMAGE|PATH` | `image.path` | string |
| `IMAGE|EXISTS` | `image.exists` | string |
| `IMAGE|EXTENSION` | `image.extension` | string |
| `IMAGE|MAGIC_HEADER` | `image.magic_header` | string |
| `IMAGE|HASHES|MD5` | `image.hashes.md5` | any |
| `IMAGE|HASHES|SHA1` | `image.hashes.sha1` | any |
| `IMAGE|HASHES|SHA256` | `image.hashes.sha256` | any |
| `IMAGE|FIRST_BYTES|HEX` | `image.first_bytes.hex` | any |
| `IMAGE|FIRST_BYTES|ASCII` | `image.first_bytes.ascii` | any |
| `IMAGE|FILE_TIMES|MODIFIED` | `image.file_times.modified` | any |
| `IMAGE|FILE_TIMES|ACCESSED` | `image.file_times.accessed` | any |
| `IMAGE|FILE_TIMES|CHANGED` | `image.file_times.changed` | any |
| `IMAGE|FILE_TIMES|CREATED` | `image.file_times.created` | any |
| `IMAGE|FILE_TIMES|USN_CHANGE_TIME` | `image.file_times.usn_change_time` | any |
| `IMAGE|FILE_TIMES|MFT_FILE_NAME_MODIFIED` | `image.file_times.mft_file_name_modified` | any |
| `IMAGE|FILE_TIMES|MFT_FILE_NAME_ACCESSED` | `image.file_times.mft_file_name_accessed` | any |
| `IMAGE|FILE_TIMES|MFT_FILE_NAME_CHANGED` | `image.file_times.mft_file_name_changed` | any |
| `IMAGE|FILE_TIMES|MFT_FILE_NAME_CREATED` | `image.file_times.mft_file_name_created` | any |
| `IMAGE|SIZE` | `image.size` | integer |
| `IMAGE|PE_INFO|COMPANY` | `image.pe_info.company` | any |
| `IMAGE|PE_INFO|DESCRIPTION` | `image.pe_info.description` | any |
| `IMAGE|PE_INFO|LEGAL_COPYRIGHT` | `image.pe_info.legal_copyright` | any |
| `IMAGE|PE_INFO|PRODUCT` | `image.pe_info.product` | any |
| `IMAGE|PE_INFO|ORIGINAL_NAME` | `image.pe_info.original_name` | any |
| `IMAGE|PE_INFO|INTERNAL_NAME` | `image.pe_info.internal_name` | any |
| `IMAGE|PE_INFO|SIGNED` | `image.pe_info.signed` | any |
| `IMAGE|PE_INFO|SIGNATURES` | `image.pe_info.signatures` | any |
| `IMAGE|PE_INFO|IMPHASH` | `image.pe_info.imphash` | any |
| `IMAGE|PE_INFO|RICH_HEADER_HASH` | `image.pe_info.rich_header_hash` | any |
| `IMAGE|PE_INFO|CREATION_TIMESTAMP` | `image.pe_info.creation_timestamp` | any |
| `IMAGE|TARGET` | `image.target` | string |
| `IMAGE|UNPACK_SOURCE` | `image.unpack_source` | any | null |
| `IMAGE|LINK_INFO|TARGET` | `image.link_info.target` | any |
| `IMAGE|LINK_INFO|ARGUMENTS` | `image.link_info.arguments` | any |
| `IMAGE|LINK_INFO|COMMAND_LINE` | `image.link_info.command_line` | any |
| `IMAGE|LINK_INFO|CREATED` | `image.link_info.created` | any |
| `IMAGE|LINK_INFO|MODIFIED` | `image.link_info.modified` | any |
| `IMAGE|LINK_INFO|ACCESSED` | `image.link_info.accessed` | any |
| `IMAGE|RECYCLE_BIN_INFO|ORIGINAL_FILE_NAME` | `image.recycle_bin_info.original_file_name` | any |
| `IMAGE|RECYCLE_BIN_INFO|DELETION_TIME` | `image.recycle_bin_info.deletion_time` | any |
| `IMAGE|RECYCLE_BIN_INFO|ORIGINAL_FILE_SIZE` | `image.recycle_bin_info.original_file_size` | any |
| `IMAGE|WER_INFO|TYPE` | `image.wer_info.type` | any |
| `IMAGE|WER_INFO|EVENT_NAME` | `image.wer_info.event_name` | any |
| `IMAGE|WER_INFO|EVENT_TYPE` | `image.wer_info.event_type` | any |
| `IMAGE|WER_INFO|DATE` | `image.wer_info.date` | any |
| `IMAGE|WER_INFO|APP_PATH` | `image.wer_info.app_path` | any |
| `IMAGE|WER_INFO|APP_NAME` | `image.wer_info.app_name` | any |
| `IMAGE|WER_INFO|EXE` | `image.wer_info.exe` | any |
| `IMAGE|WER_INFO|ERROR` | `image.wer_info.error` | any |
| `IMAGE|WER_INFO|FAULT_IN_MODULE` | `image.wer_info.fault_in_module` | any |
| `IMAGE|CONTENT|TYPE` | `image.content.type` | any |
| `IMAGE|CONTENT|ELEMENTS` | `image.content.elements` | any |
| `IMAGE|CONTENT|LENGTH` | `image.content.length` | any |
| `IMAGE|BEACON_CONFIG|BEACON_TYPE` | `image.beacon_config.beacon_type` | any |
| `IMAGE|BEACON_CONFIG|C2` | `image.beacon_config.c2` | any |
| `IMAGE|BEACON_CONFIG|PORT` | `image.beacon_config.port` | any |
| `IMAGE|BEACON_CONFIG|SPAWN_TO` | `image.beacon_config.spawn_to` | any |
| `IMAGE|BEACON_CONFIG|INJECTION_PROCESS` | `image.beacon_config.injection_process` | any |
| `IMAGE|BEACON_CONFIG|PIPE_NAME` | `image.beacon_config.pipe_name` | any |
| `IMAGE|BEACON_CONFIG|USER_AGENT` | `image.beacon_config.user_agent` | any |
| `IMAGE|BEACON_CONFIG|PROXY` | `image.beacon_config.proxy` | any |
| `IMAGE|BEACON_CONFIG|FULL_CONFIG` | `image.beacon_config.full_config` | any |
| `IMAGE|BEACON_CONFIG|CIPHER_PARAMETERS` | `image.beacon_config.cipher_parameters` | any |
| `IMAGE|VIRUSTOTAL|RESULT` | `image.virustotal.result` | any |
| `IMAGE|VIRUSTOTAL|POSITIVE_VERDICTS` | `image.virustotal.positive_verdicts` | any |
| `IMAGE|VIRUSTOTAL|TOTAL_VERDICTS` | `image.virustotal.total_verdicts` | any |
| `IMAGE|VIRUSTOTAL|HISTORY` | `image.virustotal.history` | any |
| `PARENT_INFO|PID` | `parent_info.pid` | integer |
| `PARENT_INFO|EXE` | `parent_info.exe` | string |
| `PARENT_INFO|COMMAND` | `parent_info.command` | string |
| `TREE` | `tree` | array | null |
| `CREATED` | `created` | string (date-time) |
| `SESSION` | `session` | string |
| `LISTEN_PORTS` | `listen_ports` | array | null |
| `CONNECTIONS` | `connections` | array | null |
| `SECTIONS` | `sections` | array of object |
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
| `PE_SIEVE|SUSPICIOUS_SECTIONS` | `pe_sieve.suspicious_sections` | integer |
| `PE_SIEVE|REPLACED` | `pe_sieve.replaced` | integer |
| `PE_SIEVE|HDR_MOD` | `pe_sieve.hdr_mod` | integer |
| `PE_SIEVE|UNREACHABLE_FILE` | `pe_sieve.unreachable_file` | integer |
| `PE_SIEVE|PATCHED` | `pe_sieve.patched` | integer |
| `PE_SIEVE|IAT_HOOKED` | `pe_sieve.iat_hooked` | integer |
| `PE_SIEVE|IMPLANTED` | `pe_sieve.implanted` | integer |
| `PE_SIEVE|OTHER` | `pe_sieve.other` | integer |
| `PE_SIEVE|SKIPPED` | `pe_sieve.skipped` | integer |
| `PE_SIEVE|ERRORS` | `pe_sieve.errors` | integer |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "network connecting thread"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
