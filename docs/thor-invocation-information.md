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
| `LICENSE` | `license` | object | ✅ | nested: `OWNER`: string; `LICENSE_TYPE`: string; `STARTS`: string; `EXPIRES`: string; `SCANNER`: string; `HASH`: string |  |
| `OUTPUTS` | `outputs` | array of object | ✅ |  |  |
| `SCAN_ID` | `scan_id` | string | ✅ |  |  |
| `THOR_DIR` | `thor_dir` | string | ✅ |  |  |
| `THREADS` | `threads` | integer | ✅ |  |  |
| `TIMEOUT` | `timeout` | integer | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `USER` | `user` | string | ✅ |  |  |
| `VERSIONS` | `versions` | object | ✅ | nested: `THOR`: string; `BUILD`: string; `SIGNATURES`: string; `SIGMA_RULES`: string |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

**LICENSE** (`license` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `OWNER` | `owner` | string |
| `LICENSE_TYPE` | `license_type` | string |
| `STARTS` | `starts` | string |
| `EXPIRES` | `expires` | string |
| `SCANNER` | `scanner` | string |
| `HASH` | `hash` | string |

**VERSIONS** (`versions` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `THOR` | `thor` | string |
| `BUILD` | `build` | string |
| `SIGNATURES` | `signatures` | string |
| `SIGMA_RULES` | `sigma_rules` | string |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "THOR invocation information"

detection:
    selection:
        TYPE: 'relevant_type'
    filter_legitimate:
        USER|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
