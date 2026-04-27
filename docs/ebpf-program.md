# eBPF program

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ebpf-program` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `EBPFProgram`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ATTACH_TARGET` | `attach_target` | object | ✅ | Object, see [ATTACH_TARGET Nested Fields](#attach_target-nested-fields) below |  |
| `CONTENT` | `content` | object |  | Object, see [CONTENT Nested Fields](#content-nested-fields) below |  |
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

### ATTACH_TARGET Nested Fields

Nested fields within `attach_target` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `ATTACH_TARGET.PATH` | `path` | string | |  |
| `ATTACH_TARGET.PID` | `pid` | integer | |  |
| `ATTACH_TARGET.SYMBOLS` | `symbols` | array of string | |  |
| `ATTACH_TARGET.INTERFACE` | `interface` | string | |  |
| `ATTACH_TARGET.OBJECT_ID` | `object_id` | integer | |  |
| `ATTACH_TARGET.PROTOCOL` | `protocol` | string | |  |
| `ATTACH_TARGET.HOOK` | `hook` | string | |  |
| `ATTACH_TARGET.PRIORITY` | `priority` | integer | |  |


### CONTENT Nested Fields

Nested fields within `content` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `CONTENT.TYPE` | `type` | string | |  |
| `CONTENT.ELEMENTS` | `elements` | array | null | |  |
| `CONTENT.LENGTH` | `length` | integer | |  |

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
