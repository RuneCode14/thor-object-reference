# AmCache entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/amcache-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AmcacheEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `COMPANY` | `company` | string | ✅ |  | `Microsoft Corporation`, `Simon Tatham`, `` |
| `CREATED` | `created` | string (date-time) | ✅ |  |  |
| `DESC` | `desc` | string | ✅ |  |  |
| `FILE` | `file` | object | ✅ | Object, see [FILE Nested Fields](#file-nested-fields) below |  |
| `FIRST_RUN` | `first_run` | string (date-time) | ✅ |  | `2026-01-15T08:30:00Z`, `2026-04-20T14:22:00Z` |
| `PRODUCT` | `product` | string | ✅ |  | `Microsoft® Windows® Operating System`, `PuTTY suite`, `` |
| `SHA1` | `sha1` | string | ✅ |  | `DEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEF`, `00001C50A088E12B8F4D53BAAE118E1C13D07C61` |
| `SIZE` | `size` | integer | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  | `amcache entry` |

### FILE Nested Fields

Nested fields within `file` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `FILE.TYPE` | `type` | string | | `amcache entry` |
| `FILE.PATH` | `path` | string | | `C:\Windows\System32\svchost.exe`, `C:\Users\neo\Downloads\putty.exe`, `C:\Program Files\Common Files\malware.ex...` |
| `FILE.EXISTS` | `exists` | string | |  |
| `FILE.EXTENSION` | `extension` | string | |  |
| `FILE.MAGIC_HEADER` | `magic_header` | string | |  |
| `FILE.HASHES.MD5` | `hashes.md5` | string | |  |
| `FILE.HASHES.SHA1` | `hashes.sha1` | string | |  |
| `FILE.HASHES.SHA256` | `hashes.sha256` | string | |  |
| `FILE.FIRST_BYTES.HEX` | `first_bytes.hex` | string | |  |
| `FILE.FIRST_BYTES.ASCII` | `first_bytes.ascii` | string | |  |
| `FILE.FILE_TIMES.MODIFIED` | `file_times.modified` | string (date-time) | |  |
| `FILE.FILE_TIMES.ACCESSED` | `file_times.accessed` | string (date-time) | |  |
| `FILE.FILE_TIMES.CHANGED` | `file_times.changed` | string (date-time) | |  |
| `FILE.FILE_TIMES.CREATED` | `file_times.created` | string (date-time) | |  |
| `FILE.FILE_TIMES.USN_CHANGE_TIME` | `file_times.usn_change_time` | string (date-time) | |  |
| `FILE.FILE_TIMES.MFT_FILE_NAME_MODIFIED` | `file_times.mft_file_name_modified` | string (date-time) | |  |
| `FILE.FILE_TIMES.MFT_FILE_NAME_ACCESSED` | `file_times.mft_file_name_accessed` | string (date-time) | |  |
| `FILE.FILE_TIMES.MFT_FILE_NAME_CHANGED` | `file_times.mft_file_name_changed` | string (date-time) | |  |
| `FILE.FILE_TIMES.MFT_FILE_NAME_CREATED` | `file_times.mft_file_name_created` | string (date-time) | |  |
| `FILE.SIZE` | `size` | integer | |  |
| `FILE.PE_INFO.COMPANY` | `pe_info.company` | string | |  |
| `FILE.PE_INFO.DESCRIPTION` | `pe_info.description` | string | |  |
| `FILE.PE_INFO.LEGAL_COPYRIGHT` | `pe_info.legal_copyright` | string | |  |
| `FILE.PE_INFO.PRODUCT` | `pe_info.product` | string | |  |
| `FILE.PE_INFO.ORIGINAL_NAME` | `pe_info.original_name` | string | |  |
| `FILE.PE_INFO.INTERNAL_NAME` | `pe_info.internal_name` | string | |  |
| `FILE.PE_INFO.SIGNED` | `pe_info.signed` | boolean | |  |
| `FILE.PE_INFO.SIGNATURES` | `pe_info.signatures` | array | null | |  |
| `FILE.PE_INFO.IMPHASH` | `pe_info.imphash` | string | |  |
| `FILE.PE_INFO.RICH_HEADER_HASH` | `pe_info.rich_header_hash` | string | |  |
| `FILE.PE_INFO.CREATION_TIMESTAMP` | `pe_info.creation_timestamp` | string (date-time) | |  |
| `FILE.TARGET` | `target` | string | |  |
| `FILE.UNPACK_SOURCE` | `unpack_source` | array | null | |  |
| `FILE.LINK_INFO.TARGET` | `link_info.target` | string | |  |
| `FILE.LINK_INFO.ARGUMENTS` | `link_info.arguments` | string | |  |
| `FILE.LINK_INFO.COMMAND_LINE` | `link_info.command_line` | string | |  |
| `FILE.LINK_INFO.CREATED` | `link_info.created` | string (date-time) | |  |
| `FILE.LINK_INFO.MODIFIED` | `link_info.modified` | string (date-time) | |  |
| `FILE.LINK_INFO.ACCESSED` | `link_info.accessed` | string (date-time) | |  |
| `FILE.RECYCLE_BIN_INFO.ORIGINAL_FILE_NAME` | `recycle_bin_info.original_file_name` | string | |  |
| `FILE.RECYCLE_BIN_INFO.DELETION_TIME` | `recycle_bin_info.deletion_time` | string (date-time) | |  |
| `FILE.RECYCLE_BIN_INFO.ORIGINAL_FILE_SIZE` | `recycle_bin_info.original_file_size` | integer | |  |
| `FILE.WER_INFO.TYPE` | `wer_info.type` | string | |  |
| `FILE.WER_INFO.EVENT_NAME` | `wer_info.event_name` | string | |  |
| `FILE.WER_INFO.EVENT_TYPE` | `wer_info.event_type` | string | |  |
| `FILE.WER_INFO.DATE` | `wer_info.date` | string (date-time) | |  |
| `FILE.WER_INFO.APP_PATH` | `wer_info.app_path` | string | |  |
| `FILE.WER_INFO.APP_NAME` | `wer_info.app_name` | string | |  |
| `FILE.WER_INFO.EXE` | `wer_info.exe` | string | |  |
| `FILE.WER_INFO.ERROR` | `wer_info.error` | string | |  |
| `FILE.WER_INFO.FAULT_IN_MODULE` | `wer_info.fault_in_module` | string | |  |
| `FILE.CONTENT.TYPE` | `content.type` | string | |  |
| `FILE.CONTENT.ELEMENTS` | `content.elements` | array | null | |  |
| `FILE.CONTENT.LENGTH` | `content.length` | integer | |  |
| `FILE.BEACON_CONFIG.BEACON_TYPE` | `beacon_config.beacon_type` | string | |  |
| `FILE.BEACON_CONFIG.C2` | `beacon_config.c2` | string | |  |
| `FILE.BEACON_CONFIG.PORT` | `beacon_config.port` | string | |  |
| `FILE.BEACON_CONFIG.SPAWN_TO` | `beacon_config.spawn_to` | string | |  |
| `FILE.BEACON_CONFIG.INJECTION_PROCESS` | `beacon_config.injection_process` | string | |  |
| `FILE.BEACON_CONFIG.PIPE_NAME` | `beacon_config.pipe_name` | string | |  |
| `FILE.BEACON_CONFIG.USER_AGENT` | `beacon_config.user_agent` | string | |  |
| `FILE.BEACON_CONFIG.PROXY` | `beacon_config.proxy` | string | |  |
| `FILE.BEACON_CONFIG.FULL_CONFIG` | `beacon_config.full_config` | object | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODED` | `beacon_config.cipher_parameters.xaf_encoded` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODING_ANCHOR` | `beacon_config.cipher_parameters.xaf_encoding_anchor` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.XOR_KEY` | `beacon_config.cipher_parameters.xor_key` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_OFFSET` | `beacon_config.cipher_parameters.beacon_offset` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_LENGTH` | `beacon_config.cipher_parameters.beacon_length` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.BLOCK_START` | `beacon_config.cipher_parameters.block_start` | any | |  |
| `FILE.BEACON_CONFIG.CIPHER_PARAMETERS.PAIRWISE_SWAPPED` | `beacon_config.cipher_parameters.pairwise_swapped` | any | |  |
| `FILE.VIRUSTOTAL.RESULT` | `virustotal.result` | string | |  |
| `FILE.VIRUSTOTAL.POSITIVE_VERDICTS` | `virustotal.positive_verdicts` | integer | |  |
| `FILE.VIRUSTOTAL.TOTAL_VERDICTS` | `virustotal.total_verdicts` | integer | |  |
| `FILE.VIRUSTOTAL.HISTORY.NAMES` | `virustotal.history.names` | any | |  |
| `FILE.VIRUSTOTAL.HISTORY.TAGS` | `virustotal.history.tags` | any | |  |
| `FILE.VIRUSTOTAL.HISTORY.SUBMISSIONS` | `virustotal.history.submissions` | any | |  |
| `FILE.VIRUSTOTAL.HISTORY.FIRST_SUBMISSION` | `virustotal.history.first_submission` | any | |  |
| `FILE.VIRUSTOTAL.HISTORY.LAST_SUBMISSION` | `virustotal.history.last_submission` | any | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "AmCache entry"

detection:
    selection:
        FILE.PATH|contains: 'suspicious'
    condition: selection

level: medium
```

## Notes

### FILE Field Behavior for Deleted Files

When the file referenced by an AmCache entry has been **deleted from disk**, only the following `FILE.*` fields are expected to be populated:

| Field | Value | Source |
|-------|-------|--------|
| `FILE.PATH` | Original path (e.g. `C:\Perflogs\abc.exe`) | AmCache hive |
| `FILE.EXISTS` | `"no"` | THOR file existence check |

All other `FILE.*` sub-fields (`FILE.HASHES.MD5`, `FILE.MAGIC_HEADER`, `FILE.PE_INFO.SIGNED`, `FILE.SIZE`, etc.) are expected to be `null` or empty, since THOR cannot read file properties from a non-existent file.

The top-level fields `SHA1` and `SIZE` are still populated because they come directly from the AmCache hive data, independent of the file's current presence on disk.

> ⚠️ This behavior is inferred from the AmCache hive structure. Empirical verification with THOR v11 on a system with a deleted AmCache entry is pending.
