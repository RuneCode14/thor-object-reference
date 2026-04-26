# file chunk

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/deep-dive-chunk` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `DeepDiveChunk`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `BEACON_CONFIG` | `beacon_config` | object |  | nested: `BEACON_TYPE`: string; `C2`: string; `PORT`: string; `SPAWN_TO`: string; `INJECTION_PROCESS`: string; `PIPE_NAME`: string; `USER_AGENT`: string; `PROXY`: string; `FULL_CONFIG`: object; `CIPHER_PARAMETERS|XAF_ENCODED`: boolean; `CIPHER_PARAMETERS|XAF_ENCODING_ANCHOR`: integer; `CIPHER_PARAMETERS|XOR_KEY`: integer; `CIPHER_PARAMETERS|BEACON_OFFSET`: integer; `CIPHER_PARAMETERS|BEACON_LENGTH`: integer; `CIPHER_PARAMETERS|BLOCK_START|HEX`: any; `CIPHER_PARAMETERS|BLOCK_START|ASCII`: any; `CIPHER_PARAMETERS|PAIRWISE_SWAPPED`: boolean |  |
| `CHUNK_END` | `chunk_end` | integer | ✅ |  |  |
| `CHUNK_OFFSET` | `chunk_offset` | integer | ✅ |  |  |
| `CONTENT` | `content` | object | ✅ | nested: `TYPE`: string; `ELEMENTS`: array | null; `LENGTH`: integer |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

**BEACON_CONFIG** (`beacon_config` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `BEACON_TYPE` | `beacon_type` | string |
| `C2` | `c2` | string |
| `PORT` | `port` | string |
| `SPAWN_TO` | `spawn_to` | string |
| `INJECTION_PROCESS` | `injection_process` | string |
| `PIPE_NAME` | `pipe_name` | string |
| `USER_AGENT` | `user_agent` | string |
| `PROXY` | `proxy` | string |
| `FULL_CONFIG` | `full_config` | object |
| `CIPHER_PARAMETERS|XAF_ENCODED` | `cipher_parameters.xaf_encoded` | boolean |
| `CIPHER_PARAMETERS|XAF_ENCODING_ANCHOR` | `cipher_parameters.xaf_encoding_anchor` | integer |
| `CIPHER_PARAMETERS|XOR_KEY` | `cipher_parameters.xor_key` | integer |
| `CIPHER_PARAMETERS|BEACON_OFFSET` | `cipher_parameters.beacon_offset` | integer |
| `CIPHER_PARAMETERS|BEACON_LENGTH` | `cipher_parameters.beacon_length` | integer |
| `CIPHER_PARAMETERS|BLOCK_START|HEX` | `cipher_parameters.block_start.hex` | any |
| `CIPHER_PARAMETERS|BLOCK_START|ASCII` | `cipher_parameters.block_start.ascii` | any |
| `CIPHER_PARAMETERS|PAIRWISE_SWAPPED` | `cipher_parameters.pairwise_swapped` | boolean |

**CONTENT** (`content` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `TYPE` | `type` | string |
| `ELEMENTS` | `elements` | array | null |
| `LENGTH` | `length` | integer |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "file chunk"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
