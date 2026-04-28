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

### ATTACH_TARGET JSON Sub-Fields

> ⚠️ **These nested fields are JSON structure reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules.
> Object null-check syntax (`FIELD: null`) exists but matched **all objects** in THOR v11.0.0 testing — verify behavior before relying on it.

Nested JSON structure within `attach_target` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `path` | string | |  |
| `pid` | integer | |  |
| `symbols` | array of string | |  |
| `interface` | string | |  |
| `object_id` | integer | |  |
| `protocol` | string | |  |
| `hook` | string | |  |
| `priority` | integer | |  |


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
    service: "eBPF program"

detection:
    selection:
        NAME|contains: 'suspicious_name'
    condition: selection

level: medium
```
