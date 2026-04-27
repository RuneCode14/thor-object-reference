# file

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/file` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `File`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `BEACON_CONFIG` | `beacon_config` | object |  | Object, see [BEACON_CONFIG Nested Fields](#beacon_config-nested-fields) below |  |
| `CONTENT` | `content` | object |  | Object, see [CONTENT Nested Fields](#content-nested-fields) below |  |
| `EXISTS` | `exists` | string | ✅ |  | `yes`, `no` |
| `EXTENSION` | `extension` | string | ✅ |  | ``, `sh`, `exe` |
| `FILE_TIMES` | `file_times` | object |  | Object, see [FILE_TIMES Nested Fields](#file_times-nested-fields) below |  |
| `FIRST_BYTES` | `first_bytes` | object |  | Object, see [FIRST_BYTES Nested Fields](#first_bytes-nested-fields) below |  |
| `HASHES` | `hashes` | object |  | Object, see [HASHES Nested Fields](#hashes-nested-fields) below |  |
| `LINK_INFO` | `link_info` | object |  | Object, see [LINK_INFO Nested Fields](#link_info-nested-fields) below |  |
| `MAGIC_HEADER` | `magic_header` | string |  |  | `ASCII text`, `ELF`, `PE32` |
| `PATH` | `path` | string | ✅ |  | `/etc/passwd`, `/etc/shadow`, `/tmp/malware.sh` |
| `PE_INFO` | `pe_info` | object |  | Object, see [PE_INFO Nested Fields](#pe_info-nested-fields) below |  |
| `PERMISSIONS` | `permissions` | any |  |  |  |
| `RECYCLE_BIN_INFO` | `recycle_bin_info` | object |  | Object, see [RECYCLE_BIN_INFO Nested Fields](#recycle_bin_info-nested-fields) below |  |
| `SIZE` | `size` | integer |  |  | `1234`, `0`, `1048576` |
| `TARGET` | `target` | string |  |  |  |
| `TYPE` | `type` | string | ✅ |  | `file` |
| `UNPACK_SOURCE` | `unpack_source` | array | null |  |  |  |
| `VIRUSTOTAL` | `virustotal` | object |  | Object, see [VIRUSTOTAL Nested Fields](#virustotal-nested-fields) below |  |
| `WER_INFO` | `wer_info` | object |  | Object, see [WER_INFO Nested Fields](#wer_info-nested-fields) below |  |

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


### CONTENT Nested Fields

Nested fields within `content` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `CONTENT.TYPE` | `type` | string | | `file` |
| `CONTENT.ELEMENTS` | `elements` | array | null | |  |
| `CONTENT.LENGTH` | `length` | integer | |  |


### FILE_TIMES Nested Fields

Nested fields within `file_times` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `FILE_TIMES.MODIFIED` | `modified` | string (date-time) | |  |
| `FILE_TIMES.ACCESSED` | `accessed` | string (date-time) | |  |
| `FILE_TIMES.CHANGED` | `changed` | string (date-time) | |  |
| `FILE_TIMES.CREATED` | `created` | string (date-time) | |  |
| `FILE_TIMES.USN_CHANGE_TIME` | `usn_change_time` | string (date-time) | |  |
| `FILE_TIMES.MFT_FILE_NAME_MODIFIED` | `mft_file_name_modified` | string (date-time) | |  |
| `FILE_TIMES.MFT_FILE_NAME_ACCESSED` | `mft_file_name_accessed` | string (date-time) | |  |
| `FILE_TIMES.MFT_FILE_NAME_CHANGED` | `mft_file_name_changed` | string (date-time) | |  |
| `FILE_TIMES.MFT_FILE_NAME_CREATED` | `mft_file_name_created` | string (date-time) | |  |


### FIRST_BYTES Nested Fields

Nested fields within `first_bytes` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `FIRST_BYTES.HEX` | `hex` | string | |  |
| `FIRST_BYTES.ASCII` | `ascii` | string | |  |


### HASHES Nested Fields

Nested fields within `hashes` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `HASHES.MD5` | `md5` | string | |  |
| `HASHES.SHA1` | `sha1` | string | |  |
| `HASHES.SHA256` | `sha256` | string | |  |


### LINK_INFO Nested Fields

Nested fields within `link_info` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `LINK_INFO.TARGET` | `target` | string | |  |
| `LINK_INFO.ARGUMENTS` | `arguments` | string | |  |
| `LINK_INFO.COMMAND_LINE` | `command_line` | string | |  |
| `LINK_INFO.CREATED` | `created` | string (date-time) | |  |
| `LINK_INFO.MODIFIED` | `modified` | string (date-time) | |  |
| `LINK_INFO.ACCESSED` | `accessed` | string (date-time) | |  |


### PE_INFO Nested Fields

Nested fields within `pe_info` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `PE_INFO.COMPANY` | `company` | string | |  |
| `PE_INFO.DESCRIPTION` | `description` | string | |  |
| `PE_INFO.LEGAL_COPYRIGHT` | `legal_copyright` | string | |  |
| `PE_INFO.PRODUCT` | `product` | string | |  |
| `PE_INFO.ORIGINAL_NAME` | `original_name` | string | |  |
| `PE_INFO.INTERNAL_NAME` | `internal_name` | string | |  |
| `PE_INFO.SIGNED` | `signed` | boolean | |  |
| `PE_INFO.SIGNATURES` | `signatures` | array | null | |  |
| `PE_INFO.IMPHASH` | `imphash` | string | |  |
| `PE_INFO.RICH_HEADER_HASH` | `rich_header_hash` | string | |  |
| `PE_INFO.CREATION_TIMESTAMP` | `creation_timestamp` | string (date-time) | |  |


### RECYCLE_BIN_INFO Nested Fields

Nested fields within `recycle_bin_info` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `RECYCLE_BIN_INFO.ORIGINAL_FILE_NAME` | `original_file_name` | string | |  |
| `RECYCLE_BIN_INFO.DELETION_TIME` | `deletion_time` | string (date-time) | |  |
| `RECYCLE_BIN_INFO.ORIGINAL_FILE_SIZE` | `original_file_size` | integer | |  |


### VIRUSTOTAL Nested Fields

Nested fields within `virustotal` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `VIRUSTOTAL.RESULT` | `result` | string | |  |
| `VIRUSTOTAL.POSITIVE_VERDICTS` | `positive_verdicts` | integer | |  |
| `VIRUSTOTAL.TOTAL_VERDICTS` | `total_verdicts` | integer | |  |
| `VIRUSTOTAL.HISTORY.NAMES` | `history.names` | any | null | |  |
| `VIRUSTOTAL.HISTORY.TAGS` | `history.tags` | any | null | |  |
| `VIRUSTOTAL.HISTORY.SUBMISSIONS` | `history.submissions` | integer | |  |
| `VIRUSTOTAL.HISTORY.FIRST_SUBMISSION` | `history.first_submission` | string (date-time) | |  |
| `VIRUSTOTAL.HISTORY.LAST_SUBMISSION` | `history.last_submission` | string (date-time) | |  |


### WER_INFO Nested Fields

Nested fields within `wer_info` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `WER_INFO.TYPE` | `type` | string | | `file` |
| `WER_INFO.EVENT_NAME` | `event_name` | string | |  |
| `WER_INFO.EVENT_TYPE` | `event_type` | string | |  |
| `WER_INFO.DATE` | `date` | string (date-time) | |  |
| `WER_INFO.APP_PATH` | `app_path` | string | |  |
| `WER_INFO.APP_NAME` | `app_name` | string | |  |
| `WER_INFO.EXE` | `exe` | string | |  |
| `WER_INFO.ERROR` | `error` | string | |  |
| `WER_INFO.FAULT_IN_MODULE` | `fault_in_module` | string | |  |

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
