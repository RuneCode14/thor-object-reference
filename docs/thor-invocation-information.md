# THOR invocation information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/scan-info` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ScanInfo`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `active_features` | array of string | ✅ |  |
| `active_modules` | array of string | ✅ |  |
| `arguments` | array of string | ✅ |  |
| `cpu_limit` | integer | ✅ |  |
| `elevated` | boolean | ✅ |  |
| `file_size_limit` | integer | ✅ |  |
| `fp_filters` | array of string | ✅ |  |
| `free_memory_limit` | integer | ✅ |  |
| `license` | object | ✅ | nested: `owner`: string; `license_type`: string; `starts`: string; `expires`: string; `scanner`: string; `hash`: string |
| `outputs` | array of object | ✅ | nested: `kind`: string; `output`: string |
| `scan_id` | string | ✅ |  |
| `thor_dir` | string | ✅ |  |
| `threads` | integer | ✅ |  |
| `timeout` | integer | ✅ |  |
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |
| `versions` | object | ✅ | nested: `thor`: string; `build`: string; `signatures`: string; `sigma_rules`: string |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "THOR invocation information"

detection:
    selection:
        ACTIVE_FEATURES: null
    condition: selection
```
