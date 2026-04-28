# THOR invocation information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/scan-info` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ScanInfo`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ACTIVE_FEATURES` | `active_features` | array of string | ✅ |  |  |
| `ACTIVE_MODULES` | `active_modules` | array of string | ✅ |  |  |
| `ARGUMENTS` | `arguments` | array of string | ✅ |  |  |
| `CPU_LIMIT` | `cpu_limit` | integer | ✅ |  |  |
| `ELEVATED` | `elevated` | boolean | ✅ |  |  |
| `FILE_SIZE_LIMIT` | `file_size_limit` | integer | ✅ |  |  |
| `FP_FILTERS` | `fp_filters` | array of string | ✅ |  |  |
| `FREE_MEMORY_LIMIT` | `free_memory_limit` | integer | ✅ |  |  |
| `LICENSE` | `license` | object | ✅ | Object, see [LICENSE Nested Fields](#license-nested-fields) below |  |
| `OUTPUTS` | `outputs` | array of object | ✅ |  |  |
| `SCAN_ID` | `scan_id` | string | ✅ |  |  |
| `THOR_DIR` | `thor_dir` | string | ✅ |  |  |
| `THREADS` | `threads` | integer | ✅ |  |  |
| `TIMEOUT` | `timeout` | integer | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `USER` | `user` | string | ✅ |  |  |
| `VERSIONS` | `versions` | object | ✅ | Object, see [VERSIONS Nested Fields](#versions-nested-fields) below |  |

### LICENSE JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `license` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `owner` | string | |  |
| `license_type` | string | |  |
| `starts` | string | |  |
| `expires` | string | |  |
| `scanner` | string | |  |
| `hash` | string | |  |


### VERSIONS JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `versions` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `thor` | string | |  |
| `build` | string | |  |
| `signatures` | string | |  |
| `sigma_rules` | string | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "THOR invocation information"

detection:
    selection:
        FILE_SIZE_LIMIT: 'suspicious_value'
    condition: selection

level: medium
```
