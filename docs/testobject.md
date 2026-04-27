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

### POINTEDSTRUCT Nested Fields

Nested fields within `PointedStruct` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `POINTEDSTRUCT.FIELD` | `Field` | string | |  |


### SUBSTRUCT Nested Fields

Nested fields within `SubStruct` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `SUBSTRUCT.FIELD` | `Field` | string | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "TestObject"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
