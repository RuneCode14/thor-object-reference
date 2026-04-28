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

### BEACON_CONFIG JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `beacon_config` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `beacon_type` | string | |  |
| `c2` | string | |  |
| `port` | string | |  |
| `spawn_to` | string | |  |
| `injection_process` | string | |  |
| `pipe_name` | string | |  |
| `user_agent` | string | |  |
| `proxy` | string | |  |
| `full_config` | object | |  |
| `cipher_parameters.xaf_encoded` | boolean | |  |
| `cipher_parameters.xaf_encoding_anchor` | integer | |  |
| `cipher_parameters.xor_key` | integer | |  |
| `cipher_parameters.beacon_offset` | integer | |  |
| `cipher_parameters.beacon_length` | integer | |  |
| `cipher_parameters.block_start.hex` | any | |  |
| `cipher_parameters.block_start.ascii` | any | |  |
| `cipher_parameters.pairwise_swapped` | boolean | |  |


### CONTENT JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `content` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `type` | string | | `file` |
| `elements` | array | null | |  |
| `length` | integer | |  |


### FILE_TIMES JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `file_times` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `modified` | string (date-time) | |  |
| `accessed` | string (date-time) | |  |
| `changed` | string (date-time) | |  |
| `created` | string (date-time) | |  |
| `usn_change_time` | string (date-time) | |  |
| `mft_file_name_modified` | string (date-time) | |  |
| `mft_file_name_accessed` | string (date-time) | |  |
| `mft_file_name_changed` | string (date-time) | |  |
| `mft_file_name_created` | string (date-time) | |  |


### FIRST_BYTES JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `first_bytes` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `hex` | string | |  |
| `ascii` | string | |  |


### HASHES JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `hashes` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `md5` | string | |  |
| `sha1` | string | |  |
| `sha256` | string | |  |


### LINK_INFO JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `link_info` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `target` | string | |  |
| `arguments` | string | |  |
| `command_line` | string | |  |
| `created` | string (date-time) | |  |
| `modified` | string (date-time) | |  |
| `accessed` | string (date-time) | |  |


### PE_INFO JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `pe_info` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `company` | string | |  |
| `description` | string | |  |
| `legal_copyright` | string | |  |
| `product` | string | |  |
| `original_name` | string | |  |
| `internal_name` | string | |  |
| `signed` | boolean | |  |
| `signatures` | array | null | |  |
| `imphash` | string | |  |
| `rich_header_hash` | string | |  |
| `creation_timestamp` | string (date-time) | |  |


### RECYCLE_BIN_INFO JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `recycle_bin_info` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `original_file_name` | string | |  |
| `deletion_time` | string (date-time) | |  |
| `original_file_size` | integer | |  |


### VIRUSTOTAL JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `virustotal` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `result` | string | |  |
| `positive_verdicts` | integer | |  |
| `total_verdicts` | integer | |  |
| `history.names` | any | null | |  |
| `history.tags` | any | null | |  |
| `history.submissions` | integer | |  |
| `history.first_submission` | string (date-time) | |  |
| `history.last_submission` | string (date-time) | |  |


### WER_INFO JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `wer_info` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `type` | string | | `file` |
| `event_name` | string | |  |
| `event_type` | string | |  |
| `date` | string (date-time) | |  |
| `app_path` | string | |  |
| `app_name` | string | |  |
| `exe` | string | |  |
| `error` | string | |  |
| `fault_in_module` | string | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "file"

detection:
    selection:
        PATH|contains: 'suspicious_path'
    condition: selection

level: medium
```
