# Linux kernel module

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/linux-kernel-module` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `LinuxKernelModule`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `author` | string | ✅ |  |
| `description` | array of string | ✅ |  |
| `file` | object | ✅ | nested: `type`: string; `path`: string; `exists`: string; `extension`: string; `magic_header`: string; `hashes`: object; `first_bytes`: object; `file_times`: object; `size`: integer; `permissions`: True; `pe_info`: object; `target`: string; `unpack_source`: array | null; `link_info`: object; `recycle_bin_info`: object; `wer_info`: object; `content`: object; `beacon_config`: object; `virustotal`: object |
| `in_proc_modules` | boolean | ✅ |  |
| `in_sys_module` | boolean | ✅ |  |
| `in_vmallocinfo` | boolean | ✅ |  |
| `included_in_kernel` | boolean | ✅ |  |
| `load_state` | string |  |  |
| `name` | string | ✅ |  |
| `parameters` | object (string) |  |  |
| `ref_count` | integer | ✅ |  |
| `size` | integer |  |  |
| `type` | string | ✅ |  |
| `used_by` | array of string | ✅ |  |
| `version` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Linux kernel module"

detection:
    selection:
        AUTHOR: null
    condition: selection
```
