# network connecting thread

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/network-connecting-thread` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `NetworkConnectingThread`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `CALLBACK_INTERVAL` | `callback_interval` | integer | ✅ |  |  |
| `CONNECTIONS` | `connections` | array of object | ✅ |  |  |
| `PROCESS` | `process` | object | ✅ | Object, see [PROCESS Nested Fields](#process-nested-fields) below |  |
| `THREAD_ID` | `thread_id` | integer | ✅ |  |  |
| `TYPE` | `type` | string | ✅ | Object type identifier. | `network connecting thread` |

### PROCESS Nested Fields

Nested fields within `process` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `PROCESS.TYPE` | `type` | string | |  |
| `PROCESS.PID` | `pid` | integer | |  | `544` 
| `PROCESS.DEAD` | `dead` | boolean | |  |
| `PROCESS.NAME` | `name` | string | |  | `svchost.exe` 
| `PROCESS.COMMAND` | `command` | string | |  | `C:\WINDOWS\system32\svchost.exe -k DcomLaunch -p` 
| `PROCESS.OWNER` | `owner` | string | |  | `NT AUTHORITY\SYSTEM` 
| `PROCESS.IMAGE.TYPE` | `image.type` | string | |  |
| `PROCESS.IMAGE.PATH` | `image.path` | string | |  | `C:\Windows\System32\svchost.exe` 
| `PROCESS.IMAGE.EXISTS` | `image.exists` | string | |  | `yes` 
| `PROCESS.IMAGE.EXTENSION` | `image.extension` | string | |  | `.exe` 
| `PROCESS.IMAGE.MAGIC_HEADER` | `image.magic_header` | string | |  | `EXE` 
| `PROCESS.IMAGE.HASHES.MD5` | `image.hashes.md5` | any | |  | `b1c5636ec08026fd0f8ccbff49ed7e59` 
| `PROCESS.IMAGE.HASHES.SHA1` | `image.hashes.sha1` | any | |  | `d87367d5078c476b109dc3312b62781513330055` 
| `PROCESS.IMAGE.HASHES.SHA256` | `image.hashes.sha256` | any | |  | `44fd6f9347ceed5798a25c47167f335ef085ae4648a81f775dd4bdc6240d8189` 
| `PROCESS.IMAGE.FIRST_BYTES.HEX` | `image.first_bytes.hex` | any | |  | `4d5a90000300000004000000ffff0000b8000000` 
| `PROCESS.IMAGE.FIRST_BYTES.ASCII` | `image.first_bytes.ascii` | any | |  | `MZ` 
| `PROCESS.IMAGE.FILE_TIMES.MODIFIED` | `image.file_times.modified` | any | |  | `2026-02-11T12:23:09.7277473+01:00` 
| `PROCESS.IMAGE.FILE_TIMES.ACCESSED` | `image.file_times.accessed` | any | |  | `2026-04-28T01:43:13.1994933+02:00` 
| `PROCESS.IMAGE.FILE_TIMES.CHANGED` | `image.file_times.changed` | any | |  |
| `PROCESS.IMAGE.FILE_TIMES.CREATED` | `image.file_times.created` | any | |  | `2026-02-11T12:23:09.7256107+01:00` 
| `PROCESS.IMAGE.FILE_TIMES.USN_CHANGE_TIME` | `image.file_times.usn_change_time` | any | |  |
| `PROCESS.IMAGE.FILE_TIMES.MFT_FILE_NAME_MODIFIED` | `image.file_times.mft_file_name_modified` | any | |  |
| `PROCESS.IMAGE.FILE_TIMES.MFT_FILE_NAME_ACCESSED` | `image.file_times.mft_file_name_accessed` | any | |  |
| `PROCESS.IMAGE.FILE_TIMES.MFT_FILE_NAME_CHANGED` | `image.file_times.mft_file_name_changed` | any | |  |
| `PROCESS.IMAGE.FILE_TIMES.MFT_FILE_NAME_CREATED` | `image.file_times.mft_file_name_created` | any | |  |
| `PROCESS.IMAGE.SIZE` | `image.size` | integer | |  | `88232` 
| `PROCESS.IMAGE.PE_INFO.COMPANY` | `image.pe_info.company` | any | |  | `Microsoft Corporation` 
| `PROCESS.IMAGE.PE_INFO.DESCRIPTION` | `image.pe_info.description` | any | |  | `Host Process for Windows Services` 
| `PROCESS.IMAGE.PE_INFO.LEGAL_COPYRIGHT` | `image.pe_info.legal_copyright` | any | |  | `© Microsoft Corporation. All rights reserved.` 
| `PROCESS.IMAGE.PE_INFO.PRODUCT` | `image.pe_info.product` | any | |  | `Microsoft® Windows® Operating System` 
| `PROCESS.IMAGE.PE_INFO.ORIGINAL_NAME` | `image.pe_info.original_name` | any | |  | `svchost.exe` 
| `PROCESS.IMAGE.PE_INFO.INTERNAL_NAME` | `image.pe_info.internal_name` | any | |  | `svchost.exe` 
| `PROCESS.IMAGE.PE_INFO.SIGNED` | `image.pe_info.signed` | any | |  | `true` 
| `PROCESS.IMAGE.PE_INFO.SIGNATURES` | `image.pe_info.signatures` | any | |  |
| `PROCESS.IMAGE.PE_INFO.IMPHASH` | `image.pe_info.imphash` | any | |  | `de43bd45cc98c143357416c7519eccfd` 
| `PROCESS.IMAGE.PE_INFO.RICH_HEADER_HASH` | `image.pe_info.rich_header_hash` | any | |  | `c589b6e795e70d6871a1575609b3d2bd` 
| `PROCESS.IMAGE.PE_INFO.CREATION_TIMESTAMP` | `image.pe_info.creation_timestamp` | any | |  | `2050-10-02T11:40:39+02:00` 
| `PROCESS.IMAGE.TARGET` | `image.target` | string | |  |
| `PROCESS.IMAGE.UNPACK_SOURCE` | `image.unpack_source` | any | null | |  |
| `PROCESS.IMAGE.LINK_INFO.TARGET` | `image.link_info.target` | any | |  |
| `PROCESS.IMAGE.LINK_INFO.ARGUMENTS` | `image.link_info.arguments` | any | |  |
| `PROCESS.IMAGE.LINK_INFO.COMMAND_LINE` | `image.link_info.command_line` | any | |  |
| `PROCESS.IMAGE.LINK_INFO.CREATED` | `image.link_info.created` | any | |  |
| `PROCESS.IMAGE.LINK_INFO.MODIFIED` | `image.link_info.modified` | any | |  |
| `PROCESS.IMAGE.LINK_INFO.ACCESSED` | `image.link_info.accessed` | any | |  |
| `PROCESS.IMAGE.RECYCLE_BIN_INFO.ORIGINAL_FILE_NAME` | `image.recycle_bin_info.original_file_name` | any | |  |
| `PROCESS.IMAGE.RECYCLE_BIN_INFO.DELETION_TIME` | `image.recycle_bin_info.deletion_time` | any | |  |
| `PROCESS.IMAGE.RECYCLE_BIN_INFO.ORIGINAL_FILE_SIZE` | `image.recycle_bin_info.original_file_size` | any | |  |
| `PROCESS.IMAGE.WER_INFO.TYPE` | `image.wer_info.type` | any | |  |
| `PROCESS.IMAGE.WER_INFO.EVENT_NAME` | `image.wer_info.event_name` | any | |  |
| `PROCESS.IMAGE.WER_INFO.EVENT_TYPE` | `image.wer_info.event_type` | any | |  |
| `PROCESS.IMAGE.WER_INFO.DATE` | `image.wer_info.date` | any | |  |
| `PROCESS.IMAGE.WER_INFO.APP_PATH` | `image.wer_info.app_path` | any | |  |
| `PROCESS.IMAGE.WER_INFO.APP_NAME` | `image.wer_info.app_name` | any | |  |
| `PROCESS.IMAGE.WER_INFO.EXE` | `image.wer_info.exe` | any | |  |
| `PROCESS.IMAGE.WER_INFO.ERROR` | `image.wer_info.error` | any | |  |
| `PROCESS.IMAGE.WER_INFO.FAULT_IN_MODULE` | `image.wer_info.fault_in_module` | any | |  |
| `PROCESS.IMAGE.CONTENT.TYPE` | `image.content.type` | any | |  | `sparse data` 
| `PROCESS.IMAGE.CONTENT.ELEMENTS` | `image.content.elements` | any | |  |
| `PROCESS.IMAGE.CONTENT.LENGTH` | `image.content.length` | any | |  | `206` 
| `PROCESS.IMAGE.BEACON_CONFIG.BEACON_TYPE` | `image.beacon_config.beacon_type` | any | |  |
| `PROCESS.IMAGE.BEACON_CONFIG.C2` | `image.beacon_config.c2` | any | |  |
| `PROCESS.IMAGE.BEACON_CONFIG.PORT` | `image.beacon_config.port` | any | |  |
| `PROCESS.IMAGE.BEACON_CONFIG.SPAWN_TO` | `image.beacon_config.spawn_to` | any | |  |
| `PROCESS.IMAGE.BEACON_CONFIG.INJECTION_PROCESS` | `image.beacon_config.injection_process` | any | |  |
| `PROCESS.IMAGE.BEACON_CONFIG.PIPE_NAME` | `image.beacon_config.pipe_name` | any | |  |
| `PROCESS.IMAGE.BEACON_CONFIG.USER_AGENT` | `image.beacon_config.user_agent` | any | |  |
| `PROCESS.IMAGE.BEACON_CONFIG.PROXY` | `image.beacon_config.proxy` | any | |  |
| `PROCESS.IMAGE.BEACON_CONFIG.FULL_CONFIG` | `image.beacon_config.full_config` | any | |  |
| `PROCESS.IMAGE.BEACON_CONFIG.CIPHER_PARAMETERS` | `image.beacon_config.cipher_parameters` | any | |  |
| `PROCESS.IMAGE.VIRUSTOTAL.RESULT` | `image.virustotal.result` | any | |  |
| `PROCESS.IMAGE.VIRUSTOTAL.POSITIVE_VERDICTS` | `image.virustotal.positive_verdicts` | any | |  |
| `PROCESS.IMAGE.VIRUSTOTAL.TOTAL_VERDICTS` | `image.virustotal.total_verdicts` | any | |  |
| `PROCESS.IMAGE.VIRUSTOTAL.HISTORY` | `image.virustotal.history` | any | |  |
| `PROCESS.PARENT_INFO.PID` | `parent_info.pid` | integer | |  | `932` 
| `PROCESS.PARENT_INFO.EXE` | `parent_info.exe` | string | |  | `C:\Windows\System32\services.exe` 
| `PROCESS.PARENT_INFO.COMMAND` | `parent_info.command` | string | |  |
| `PROCESS.TREE` | `tree` | array | null | |  |
| `PROCESS.CREATED` | `created` | string (date-time) | |  | `2026-04-28T00:43:06+02:00` 
| `PROCESS.SESSION` | `session` | string | |  | `Services` 
| `PROCESS.LISTEN_PORTS` | `listen_ports` | array | null | | `[49665]` |
| `PROCESS.CONNECTIONS` | `connections` | array | null | |  |
| `PROCESS.SECTIONS` | `sections` | array of object | |  |
| `PROCESS.BEACON_CONFIG.BEACON_TYPE` | `beacon_config.beacon_type` | string | |  |
| `PROCESS.BEACON_CONFIG.C2` | `beacon_config.c2` | string | |  |
| `PROCESS.BEACON_CONFIG.PORT` | `beacon_config.port` | string | |  |
| `PROCESS.BEACON_CONFIG.SPAWN_TO` | `beacon_config.spawn_to` | string | |  |
| `PROCESS.BEACON_CONFIG.INJECTION_PROCESS` | `beacon_config.injection_process` | string | |  |
| `PROCESS.BEACON_CONFIG.PIPE_NAME` | `beacon_config.pipe_name` | string | |  |
| `PROCESS.BEACON_CONFIG.USER_AGENT` | `beacon_config.user_agent` | string | |  |
| `PROCESS.BEACON_CONFIG.PROXY` | `beacon_config.proxy` | string | |  |
| `PROCESS.BEACON_CONFIG.FULL_CONFIG` | `beacon_config.full_config` | object | |  |
| `PROCESS.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODED` | `beacon_config.cipher_parameters.xaf_encoded` | any | |  |
| `PROCESS.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODING_ANCHOR` | `beacon_config.cipher_parameters.xaf_encoding_anchor` | any | |  |
| `PROCESS.BEACON_CONFIG.CIPHER_PARAMETERS.XOR_KEY` | `beacon_config.cipher_parameters.xor_key` | any | |  |
| `PROCESS.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_OFFSET` | `beacon_config.cipher_parameters.beacon_offset` | any | |  |
| `PROCESS.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_LENGTH` | `beacon_config.cipher_parameters.beacon_length` | any | |  |
| `PROCESS.BEACON_CONFIG.CIPHER_PARAMETERS.BLOCK_START` | `beacon_config.cipher_parameters.block_start` | any | |  |
| `PROCESS.BEACON_CONFIG.CIPHER_PARAMETERS.PAIRWISE_SWAPPED` | `beacon_config.cipher_parameters.pairwise_swapped` | any | |  |
| `PROCESS.PE_SIEVE.SUSPICIOUS_SECTIONS` | `pe_sieve.suspicious_sections` | integer | |  |
| `PROCESS.PE_SIEVE.REPLACED` | `pe_sieve.replaced` | integer | |  |
| `PROCESS.PE_SIEVE.HDR_MOD` | `pe_sieve.hdr_mod` | integer | |  |
| `PROCESS.PE_SIEVE.UNREACHABLE_FILE` | `pe_sieve.unreachable_file` | integer | |  |
| `PROCESS.PE_SIEVE.PATCHED` | `pe_sieve.patched` | integer | |  |
| `PROCESS.PE_SIEVE.IAT_HOOKED` | `pe_sieve.iat_hooked` | integer | |  |
| `PROCESS.PE_SIEVE.IMPLANTED` | `pe_sieve.implanted` | integer | |  |
| `PROCESS.PE_SIEVE.OTHER` | `pe_sieve.other` | integer | |  |
| `PROCESS.PE_SIEVE.SKIPPED` | `pe_sieve.skipped` | integer | |  |
| `PROCESS.PE_SIEVE.ERRORS` | `pe_sieve.errors` | integer | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "network connecting thread"

detection:
    selection:
        PROCESS.NAME|contains: 'powershell'
    condition: selection

level: medium
```
