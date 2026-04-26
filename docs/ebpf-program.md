# eBPF program

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ebpf-program` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `EBPFProgram`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ATTACH_TARGET` | `attach_target` | object | ✅ | nested: `PATH`: string; `PID`: integer; `SYMBOLS`: array of string; `INTERFACE`: string; `OBJECT_ID`: integer; `PROTOCOL`: string; `HOOK`: string; `PRIORITY`: integer |  |
| `CONTENT` | `content` | object |  | nested: `TYPE`: string; `ELEMENTS`: array \| null; `LENGTH`: integer |  |
| `FUNCTIONS` | `functions` | array of string | ✅ |  |  |
| `LINK_TYPE` | `link_type` | string | ✅ |  |  |
| `LOAD_TIME` | `load_time` | string (date-time) | ✅ |  |  |
| `MAPS` | `maps` | array of string | ✅ |  |  |
| `MEMORY_LOCKED` | `memory_locked` | integer | ✅ |  |  |
| `NAME` | `name` | string | ✅ |  |  |
| `PROGRAM_TYPE` | `program_type` | string | ✅ |  |  |
| `SIZE` | `size` | integer | ✅ |  |  |
| `TAG` | `tag` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `USER` | `user` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

**ATTACH_TARGET** (`attach_target` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `PATH` | `path` | string |
| `PID` | `pid` | integer |
| `SYMBOLS` | `symbols` | array of string |
| `INTERFACE` | `interface` | string |
| `OBJECT_ID` | `object_id` | integer |
| `PROTOCOL` | `protocol` | string |
| `HOOK` | `hook` | string |
| `PRIORITY` | `priority` | integer |

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
    service: "eBPF program"

detection:
    selection:
        NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    filter_legitimate:
        USER|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
