# TestObject

**Schema ID:** `https://git.bsk/thorx/lib/features/truncate/testobject/test-object` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `TestObject`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `FIELDDIRECT` | `FieldDirect` | string | ✅ |  |  |
| `INTERFACE` | `Interface` | any | ✅ |  |  |
| `MAP` | `Map` | object (string) | ✅ |  |  |
| `POINTEDSTRUCT` | `PointedStruct` | object | ✅ | Object, see [POINTEDSTRUCT Nested Fields](#pointedstruct-nested-fields) below |  |
| `SLICE` | `Slice` | array of object | ✅ |  |  |
| `SUBSTRUCT` | `SubStruct` | object | ✅ | Object, see [SUBSTRUCT Nested Fields](#substruct-nested-fields) below |  |
| `TYPE` | `type` | string | ✅ |  |  |

### POINTEDSTRUCT JSON Sub-Fields

> ⚠️ **These nested fields are JSON structure reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules.
> Object null-check syntax (`FIELD: null`) exists but matched **all objects** in THOR v11.0.0 testing — verify behavior before relying on it.

Nested JSON structure within `PointedStruct` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `Field` | string | |  |


### SUBSTRUCT JSON Sub-Fields

> ⚠️ **These nested fields are JSON structure reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules.
> Object null-check syntax (`FIELD: null`) exists but matched **all objects** in THOR v11.0.0 testing — verify behavior before relying on it.

Nested JSON structure within `SubStruct` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `Field` | string | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "TestObject"

detection:
    selection:
        FIELDDIRECT|contains: 'suspicious_string'
    condition: selection

level: medium
```
