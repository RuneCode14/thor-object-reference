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

### BEACON_CONFIG Nested Fields

Nested fields within `beacon_config` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `BEACON_CONFIG.BEACON_TYPE` | `beacon_type` | string | |  |
| `BEACON_CONFIG.C2` | `c2` | string | |  |
| `BEACON_CONFIG.PORT` | `port` | string | |  |
| `BEACON_CONFIG.SPAWN_TO` | `spawn_to` | string | |  |
| `BEACON_CONFIG.INJECTION_PROCESS` | `injection_process` | string | |  |
| `BEACON_CONFIG.PIPE_NAME` | `pipe_name` | string | |  |
| `BEACON_CONFIG.USER_AGENT` | `user_agent` | string | |  |
| `BEACON_CONFIG.PROXY` | `proxy` | string | |  |
| `BEACON_CONFIG.FULL_CONFIG` | `full_config` | object | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODED` | `cipher_parameters.xaf_encoded` | boolean | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.XAF_ENCODING_ANCHOR` | `cipher_parameters.xaf_encoding_anchor` | integer | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.XOR_KEY` | `cipher_parameters.xor_key` | integer | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_OFFSET` | `cipher_parameters.beacon_offset` | integer | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.BEACON_LENGTH` | `cipher_parameters.beacon_length` | integer | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.BLOCK_START.HEX` | `cipher_parameters.block_start.hex` | any | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.BLOCK_START.ASCII` | `cipher_parameters.block_start.ascii` | any | |  |
| `BEACON_CONFIG.CIPHER_PARAMETERS.PAIRWISE_SWAPPED` | `cipher_parameters.pairwise_swapped` | boolean | |  |


### CONTENT Nested Fields

Nested fields within `content` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `CONTENT.TYPE` | `type` | string | |  |
| `CONTENT.ELEMENTS` | `elements` | array | null | |  |
| `CONTENT.LENGTH` | `length` | integer | |  |

## Sigma Rule Template

This is primarily a passive metadata object. Real detection value comes from
`BEACON_CONFIG` sub-fields (Cobalt Strike configuration extraction). Use this
service to select all file chunks, or target `BEACON_CONFIG.*` fields for
specific detections.

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
