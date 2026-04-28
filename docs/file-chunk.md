# file chunk

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/deep-dive-chunk` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `DeepDiveChunk`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `BEACON_CONFIG` | `beacon_config` | object |  | Object, see [BEACON_CONFIG Nested Fields](#beacon_config-nested-fields) below |  |
| `CHUNK_END` | `chunk_end` | integer | ✅ |  |  |
| `CHUNK_OFFSET` | `chunk_offset` | integer | ✅ |  |  |
| `CONTENT` | `content` | object | ✅ | Object, see [CONTENT Nested Fields](#content-nested-fields) below |  |
| `TYPE` | `type` | string | ✅ |  |  |

### BEACON_CONFIG JSON Sub-Fields

> ⚠️ **These nested fields are JSON structure reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules.
> Object null-check syntax (`FIELD: null`) exists but matched **all objects** in THOR v11.0.0 testing — verify behavior before relying on it.

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

> ⚠️ **These nested fields are JSON structure reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules.
> Object null-check syntax (`FIELD: null`) exists but matched **all objects** in THOR v11.0.0 testing — verify behavior before relying on it.

Nested JSON structure within `content` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `type` | string | |  |
| `elements` | array | null | |  |
| `length` | integer | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "file chunk"

detection:
    selection:
        TYPE: 'file chunk'
    condition: selection

level: medium
```
