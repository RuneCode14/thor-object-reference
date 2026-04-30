# Linux kernel module

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/linux-kernel-module` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `LinuxKernelModule`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `AUTHOR` | `author` | string | ✅ |  |  |
| `DESCRIPTION` | `description` | array of string | ✅ |  |  |
| `FILE_PATH` | `file.path` | string |  | Flattened file path for Sigma matching | `/lib/modules/6.8.0-101-generic/kernel/drivers/firmware/efi/efi-pstore.ko.zst` |
| `FILE` | `file` | object | ✅ | Object, see [FILE Nested Fields](#file-nested-fields) below | `/lib/modules/6.18.6-200.fc43.x86_64/kern...`, `null` |
| `IN_PROC_MODULES` | `in_proc_modules` | boolean | ✅ |  |  |
| `IN_SYS_MODULE` | `in_sys_module` | boolean | ✅ |  |  |
| `IN_VMALLOCINFO` | `in_vmallocinfo` | boolean | ✅ |  |  |
| `INCLUDED_IN_KERNEL` | `included_in_kernel` | boolean | ✅ |  | `true`, `false` |
| `LOAD_STATE` | `load_state` | string |  |  |  |
| `NAME` | `name` | string | ✅ |  | `nf_conntrack`, `nvme`, `hid_generic` |
| `PARAMETERS` | `parameters` | object (string) |  |  |  |
| `REF_COUNT` | `ref_count` | integer | ✅ |  |  |
| `SIZE` | `size` | integer |  |  | `123456`, `0` |
| `TYPE` | `type` | string | ✅ |  | `linux kernel module` |
| `USED_BY` | `used_by` | array of string | ✅ |  |  |
| `VERSION` | `version` | string | ✅ |  |  |

### FILE JSON Sub-Fields

> ⚠️ **These nested fields are JSON structure reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules.
> Object null-check syntax (`FIELD: null`) exists but matched **all objects** in THOR v11.0.0 testing — verify behavior before relying on it.
> 
> For matching on the module's `.ko` file path, use the top-level **`FILE_PATH`** field (which maps from `file.path`) rather than the nested `FILE` object.

Nested JSON structure within `file` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `type` | string | | `linux kernel module` |
| `path` | string | |  |
| `exists` | string | |  |
| `extension` | string | |  |
| `magic_header` | string | |  |
| `hashes.md5` | string | |  |
| `hashes.sha1` | string | |  |
| `hashes.sha256` | string | |  |
| `first_bytes.hex` | string | |  |
| `first_bytes.ascii` | string | |  |
| `file_times.modified` | string (date-time) | |  |
| `file_times.accessed` | string (date-time) | |  |
| `file_times.changed` | string (date-time) | |  |
| `file_times.created` | string (date-time) | |  |
| `file_times.usn_change_time` | string (date-time) | |  |
| `file_times.mft_file_name_modified` | string (date-time) | |  |
| `file_times.mft_file_name_accessed` | string (date-time) | |  |
| `file_times.mft_file_name_changed` | string (date-time) | |  |
| `file_times.mft_file_name_created` | string (date-time) | |  |
| `size` | integer | | `123456`, `0` |
| `pe_info.company` | string | |  |
| `pe_info.description` | string | |  |
| `pe_info.legal_copyright` | string | |  |
| `pe_info.product` | string | |  |
| `pe_info.original_name` | string | |  |
| `pe_info.internal_name` | string | |  |
| `pe_info.signed` | boolean | |  |
| `pe_info.signatures` | array | null | |  |
| `pe_info.imphash` | string | |  |
| `pe_info.rich_header_hash` | string | |  |
| `pe_info.creation_timestamp` | string (date-time) | |  |
| `target` | string | |  |
| `unpack_source` | array | null | |  |
| `link_info.target` | string | |  |
| `link_info.arguments` | string | |  |
| `link_info.command_line` | string | |  |
| `link_info.created` | string (date-time) | |  |
| `link_info.modified` | string (date-time) | |  |
| `link_info.accessed` | string (date-time) | |  |
| `recycle_bin_info.original_file_name` | string | |  |
| `recycle_bin_info.deletion_time` | string (date-time) | |  |
| `recycle_bin_info.original_file_size` | integer | |  |
| `wer_info.type` | string | |  |
| `wer_info.event_name` | string | |  |
| `wer_info.event_type` | string | |  |
| `wer_info.date` | string (date-time) | |  |
| `wer_info.app_path` | string | |  |
| `wer_info.app_name` | string | |  |
| `wer_info.exe` | string | |  |
| `wer_info.error` | string | |  |
| `wer_info.fault_in_module` | string | |  |
| `content.type` | string | |  |
| `content.elements` | array | null | |  |
| `content.length` | integer | |  |
| `beacon_config.beacon_type` | string | |  |
| `beacon_config.c2` | string | |  |
| `beacon_config.port` | string | |  |
| `beacon_config.spawn_to` | string | |  |
| `beacon_config.injection_process` | string | |  |
| `beacon_config.pipe_name` | string | |  |
| `beacon_config.user_agent` | string | |  |
| `beacon_config.proxy` | string | |  |
| `beacon_config.full_config` | object | |  |
| `beacon_config.cipher_parameters.xaf_encoded` | any | |  |
| `beacon_config.cipher_parameters.xaf_encoding_anchor` | any | |  |
| `beacon_config.cipher_parameters.xor_key` | any | |  |
| `beacon_config.cipher_parameters.beacon_offset` | any | |  |
| `beacon_config.cipher_parameters.beacon_length` | any | |  |
| `beacon_config.cipher_parameters.block_start` | any | |  |
| `beacon_config.cipher_parameters.pairwise_swapped` | any | |  |
| `virustotal.result` | string | |  |
| `virustotal.positive_verdicts` | integer | |  |
| `virustotal.total_verdicts` | integer | |  |
| `virustotal.history.names` | any | |  |
| `virustotal.history.tags` | any | |  |
| `virustotal.history.submissions` | any | |  |
| `virustotal.history.first_submission` | any | |  |
| `virustotal.history.last_submission` | any | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Linux kernel module"

detection:
    selection:
        FILE_PATH|contains: 'suspicious'
    condition: selection

level: medium
```
