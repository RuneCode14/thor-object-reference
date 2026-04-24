# eBPF program

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/ebpf-program` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `EBPFProgram`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `attach_target` | object | ✅ | nested: `path`: string; `pid`: integer; `symbols`: array of string; `interface`: string; `object_id`: integer; `protocol`: string; `hook`: string; `priority`: integer |
| `content` | object |  | nested: `type`: string; `elements`: array | null; `length`: integer |
| `functions` | array of string | ✅ |  |
| `link_type` | string | ✅ |  |
| `load_time` | string (date-time) | ✅ |  |
| `maps` | array of string | ✅ |  |
| `memory_locked` | integer | ✅ |  |
| `name` | string | ✅ |  |
| `program_type` | string | ✅ |  |
| `size` | integer | ✅ |  |
| `tag` | string | ✅ |  |
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "eBPF program"

detection:
    selection:
        ATTACH_TARGET: null
    condition: selection
```
