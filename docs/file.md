# file

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/file` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `File`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `BEACON_CONFIG` | `beacon_config` | object |  | nested: `BEACON_TYPE`: string; `C2`: string; `PORT`: string; `SPAWN_TO`: string; `INJECTION_PROCESS`: string; `PIPE_NAME`: string; `USER_AGENT`: string; `PROXY`: string; `FULL_CONFIG`: object; `CIPHER_PARAMETERS\|XAF_ENCODED`: boolean; `CIPHER_PARAMETERS\|XAF_ENCODING_ANCHOR`: integer; `CIPHER_PARAMETERS\|XOR_KEY`: integer; `CIPHER_PARAMETERS\|BEACON_OFFSET`: integer; `CIPHER_PARAMETERS\|BEACON_LENGTH`: integer; `CIPHER_PARAMETERS\|BLOCK_START\|HEX`: any; `CIPHER_PARAMETERS\|BLOCK_START\|ASCII`: any; `CIPHER_PARAMETERS\|PAIRWISE_SWAPPED`: boolean |  |
| `CONTENT` | `content` | object |  | nested: `TYPE`: string; `ELEMENTS`: array \| null; `LENGTH`: integer |  |
| `EXISTS` | `exists` | string | ✅ |  | `yes`, `no` |
| `EXTENSION` | `extension` | string | ✅ |  | ``, `sh`, `exe` |
| `FILE_TIMES` | `file_times` | object |  | nested: `MODIFIED`: string (date-time); `ACCESSED`: string (date-time); `CHANGED`: string (date-time); `CREATED`: string (date-time); `USN_CHANGE_TIME`: string (date-time); `MFT_FILE_NAME_MODIFIED`: string (date-time); `MFT_FILE_NAME_ACCESSED`: string (date-time); `MFT_FILE_NAME_CHANGED`: string (date-time); `MFT_FILE_NAME_CREATED`: string (date-time) |  |
| `FIRST_BYTES` | `first_bytes` | object |  | nested: `HEX`: string; `ASCII`: string |  |
| `HASHES` | `hashes` | object |  | nested: `MD5`: string; `SHA1`: string; `SHA256`: string |  |
| `LINK_INFO` | `link_info` | object |  | nested: `TARGET`: string; `ARGUMENTS`: string; `COMMAND_LINE`: string; `CREATED`: string (date-time); `MODIFIED`: string (date-time); `ACCESSED`: string (date-time) |  |
| `MAGIC_HEADER` | `magic_header` | string |  |  | `ASCII text`, `ELF`, `PE32` |
| `PATH` | `path` | string | ✅ |  | `/etc/passwd`, `/etc/shadow`, `/tmp/malware.sh` |
| `PE_INFO` | `pe_info` | object |  | nested: `COMPANY`: string; `DESCRIPTION`: string; `LEGAL_COPYRIGHT`: string; `PRODUCT`: string; `ORIGINAL_NAME`: string; `INTERNAL_NAME`: string; `SIGNED`: boolean; `SIGNATURES`: array \| null; `IMPHASH`: string; `RICH_HEADER_HASH`: string; `CREATION_TIMESTAMP`: string (date-time) |  |
| `PERMISSIONS` | `permissions` | any |  |  |  |
| `RECYCLE_BIN_INFO` | `recycle_bin_info` | object |  | nested: `ORIGINAL_FILE_NAME`: string; `DELETION_TIME`: string (date-time); `ORIGINAL_FILE_SIZE`: integer |  |
| `SIZE` | `size` | integer |  |  | `1234`, `0`, `1048576` |
| `TARGET` | `target` | string |  |  |  |
| `TYPE` | `type` | string | ✅ |  | `file` |
| `UNPACK_SOURCE` | `unpack_source` | array | null |  |  |  |
| `VIRUSTOTAL` | `virustotal` | object |  | nested: `RESULT`: string; `POSITIVE_VERDICTS`: integer; `TOTAL_VERDICTS`: integer; `HISTORY\|NAMES`: any \| null; `HISTORY\|TAGS`: any \| null; `HISTORY\|SUBMISSIONS`: integer; `HISTORY\|FIRST_SUBMISSION`: string (date-time); `HISTORY\|LAST_SUBMISSION`: string (date-time) |  |
| `WER_INFO` | `wer_info` | object |  | nested: `TYPE`: string; `EVENT_NAME`: string; `EVENT_TYPE`: string; `DATE`: string (date-time); `APP_PATH`: string; `APP_NAME`: string; `EXE`: string; `ERROR`: string; `FAULT_IN_MODULE`: string |  |

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

**CONTENT** (`content` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `TYPE` | `type` | string |
| `ELEMENTS` | `elements` | array | null |
| `LENGTH` | `length` | integer |

**FILE_TIMES** (`file_times` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `MODIFIED` | `modified` | string (date-time) |
| `ACCESSED` | `accessed` | string (date-time) |
| `CHANGED` | `changed` | string (date-time) |
| `CREATED` | `created` | string (date-time) |
| `USN_CHANGE_TIME` | `usn_change_time` | string (date-time) |
| `MFT_FILE_NAME_MODIFIED` | `mft_file_name_modified` | string (date-time) |
| `MFT_FILE_NAME_ACCESSED` | `mft_file_name_accessed` | string (date-time) |
| `MFT_FILE_NAME_CHANGED` | `mft_file_name_changed` | string (date-time) |
| `MFT_FILE_NAME_CREATED` | `mft_file_name_created` | string (date-time) |

**FIRST_BYTES** (`first_bytes` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `HEX` | `hex` | string |
| `ASCII` | `ascii` | string |

**HASHES** (`hashes` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `MD5` | `md5` | string |
| `SHA1` | `sha1` | string |
| `SHA256` | `sha256` | string |

**LINK_INFO** (`link_info` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `TARGET` | `target` | string |
| `ARGUMENTS` | `arguments` | string |
| `COMMAND_LINE` | `command_line` | string |
| `CREATED` | `created` | string (date-time) |
| `MODIFIED` | `modified` | string (date-time) |
| `ACCESSED` | `accessed` | string (date-time) |

**PE_INFO** (`pe_info` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `COMPANY` | `company` | string |
| `DESCRIPTION` | `description` | string |
| `LEGAL_COPYRIGHT` | `legal_copyright` | string |
| `PRODUCT` | `product` | string |
| `ORIGINAL_NAME` | `original_name` | string |
| `INTERNAL_NAME` | `internal_name` | string |
| `SIGNED` | `signed` | boolean |
| `SIGNATURES` | `signatures` | array | null |
| `IMPHASH` | `imphash` | string |
| `RICH_HEADER_HASH` | `rich_header_hash` | string |
| `CREATION_TIMESTAMP` | `creation_timestamp` | string (date-time) |

**RECYCLE_BIN_INFO** (`recycle_bin_info` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `ORIGINAL_FILE_NAME` | `original_file_name` | string |
| `DELETION_TIME` | `deletion_time` | string (date-time) |
| `ORIGINAL_FILE_SIZE` | `original_file_size` | integer |

**VIRUSTOTAL** (`virustotal` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `RESULT` | `result` | string |
| `POSITIVE_VERDICTS` | `positive_verdicts` | integer |
| `TOTAL_VERDICTS` | `total_verdicts` | integer |
| `HISTORY|NAMES` | `history.names` | any | null |
| `HISTORY|TAGS` | `history.tags` | any | null |
| `HISTORY|SUBMISSIONS` | `history.submissions` | integer |
| `HISTORY|FIRST_SUBMISSION` | `history.first_submission` | string (date-time) |
| `HISTORY|LAST_SUBMISSION` | `history.last_submission` | string (date-time) |

**WER_INFO** (`wer_info` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `TYPE` | `type` | string |
| `EVENT_NAME` | `event_name` | string |
| `EVENT_TYPE` | `event_type` | string |
| `DATE` | `date` | string (date-time) |
| `APP_PATH` | `app_path` | string |
| `APP_NAME` | `app_name` | string |
| `EXE` | `exe` | string |
| `ERROR` | `error` | string |
| `FAULT_IN_MODULE` | `fault_in_module` | string |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "file"

detection:
    selection:
        PATH|contains:
            - '/suspicious/'
            - '/tmp/'
        SHA256: 'known_bad_hash_sha256'
        TYPE: 'relevant_type'
    filter_legitimate:
        EXISTS: 'true'
    condition: selection and not filter_legitimate
```
