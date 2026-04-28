# Windows service

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-service` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsService`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `DESCRIPTION` | `description` | string | ✅ |  | `1394 OpenHCI Driver` |
| `FAILURE_COMMAND` | `failure_command` | string | ✅ |  |  |
| `IMAGE` | `image` | object | ✅ | Object, see [IMAGE Nested Fields](#image-nested-fields) below | `C:\Windows\System32\svchost.exe -k netsv...`, `C:\Program Files\Windows Defender\MsMpEn...`, `C:\Users\Public\malware.exe` |
| `KEY` | `key` | string | ✅ |  | `System\CurrentControlSet\Services\1394ohci` |
| `KEY_NAME` | `key_name` | string | ✅ |  | `1394ohci` |
| `MODIFIED` | `modified` | string (date-time) | ✅ |  | `2024-04-01T09:25:50.6070029+02:00` |
| `SERVICE_NAME` | `service_name` | string | ✅ |  | `@1394.inf,%PCI\CC_0C0010.DeviceDesc%;1394 OHCI Compliant Host Controller` |
| `SERVICE_TYPE` | `service_type` | string | ✅ |  | `Device Driver` |
| `START_TYPE` | `start_type` | string | ✅ |  | `ONDEMAND_START` |
| `TYPE` | `type` | string | ✅ |  | `windows service` |
| `USER` | `user` | string | ✅ |  | `LocalSystem` |

### IMAGE Nested Fields

Nested fields within `image` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `IMAGE.TYPE` | `type` | string | | `windows service` |
| `IMAGE.PATH` | `path` | string | |  | `C:\Windows\System32\svchost.exe` 
| `IMAGE.EXISTS` | `exists` | string | |  | `yes` 
| `IMAGE.EXTENSION` | `extension` | string | |  | `.exe` 
| `IMAGE.MAGIC_HEADER` | `magic_header` | string | |  | `EXE` 
| `IMAGE.HASHES.MD5` | `hashes.md5` | string | |  | `b1c5636ec08026fd0f8ccbff49ed7e59` 
| `IMAGE.HASHES.SHA1` | `hashes.sha1` | string | |  | `d87367d5078c476b109dc3312b62781513330055` 
| `IMAGE.HASHES.SHA256` | `hashes.sha256` | string | |  | `44fd6f9347ceed5798a25c47167f335ef085ae4648a81f775dd4bdc6240d8189` 
| `IMAGE.FIRST_BYTES.HEX` | `first_bytes.hex` | string | |  | `4d5a90000300000004000000ffff0000b8000000` 
| `IMAGE.FIRST_BYTES.ASCII` | `first_bytes.ascii` | string | |  | `MZ` 
| `IMAGE.FILE_TIMES.MODIFIED` | `file_times.modified` | string (date-time) | |  | `2026-02-11T12:23:09.7277473+01:00` 
| `IMAGE.FILE_TIMES.ACCESSED` | `file_times.accessed` | string (date-time) | |  | `2026-04-28T01:43:13.1994933+02:00` 
| `IMAGE.FILE_TIMES.CHANGED` | `file_times.changed` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.CREATED` | `file_times.created` | string (date-time) | |  | `2026-02-11T12:23:09.7256107+01:00` 
| `IMAGE.FILE_TIMES.USN_CHANGE_TIME` | `file_times.usn_change_time` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.MFT_FILE_NAME_MODIFIED` | `file_times.mft_file_name_modified` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.MFT_FILE_NAME_ACCESSED` | `file_times.mft_file_name_accessed` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.MFT_FILE_NAME_CHANGED` | `file_times.mft_file_name_changed` | string (date-time) | |  |
| `IMAGE.FILE_TIMES.MFT_FILE_NAME_CREATED` | `file_times.mft_file_name_created` | string (date-time) | |  |
| `IMAGE.SIZE` | `size` | integer | |  | `88232` 
| `IMAGE.PE_INFO.COMPANY` | `pe_info.company` | string | |  | `Microsoft Corporation` 
| `IMAGE.PE_INFO.DESCRIPTION` | `pe_info.description` | string | |  | `Host Process for Windows Services` 
| `IMAGE.PE_INFO.LEGAL_COPYRIGHT` | `pe_info.legal_copyright` | string | |  | `© Microsoft Corporation. All rights reserved.` 
| `IMAGE.PE_INFO.PRODUCT` | `pe_info.product` | string | |  | `Microsoft® Windows® Operating System` 
| `IMAGE.PE_INFO.ORIGINAL_NAME` | `pe_info.original_name` | string | |  | `svchost.exe` 
| `IMAGE.PE_INFO.INTERNAL_NAME` | `pe_info.internal_name` | string | |  | `svchost.exe` 
| `IMAGE.PE_INFO.SIGNED` | `pe_info.signed` | boolean | |  | `true` 
| `IMAGE.PE_INFO.SIGNATURES` | `pe_info.signatures` | array | null | |  |
| `IMAGE.PE_INFO.IMPHASH` | `pe_info.imphash` | string | |  | `de43bd45cc98c143357416c7519eccfd` 
| `IMAGE.PE_INFO.RICH_HEADER_HASH` | `pe_info.rich_header_hash` | string | |  | `c589b6e795e70d6871a1575609b3d2bd` 
| `IMAGE.PE_INFO.CREATION_TIMESTAMP` | `pe_info.creation_timestamp` | string (date-time) | |  | `2050-10-02T11:40:39+02:00` 
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
| `IMAGE.CONTENT.TYPE` | `content.type` | string | |  | `sparse data` 
| `IMAGE.CONTENT.ELEMENTS` | `content.elements` | array | null | |  |
| `IMAGE.CONTENT.LENGTH` | `content.length` | integer | |  | `206` 
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
        FAILURE_COMMAND|contains: 'suspicious_command'
    condition: selection

level: medium
```
