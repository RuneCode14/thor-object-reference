# TestObject

**Schema ID:** `https://git.bsk/thorx/lib/features/truncate/testobject/test-object` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `TestObject`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `FIELDDIRECT` | `FieldDirect` | string | ✅ |  |
| `INTERFACE` | `Interface` | any | ✅ |  |
| `MAP` | `Map` | object (string) | ✅ |  |
| `POINTEDSTRUCT` | `PointedStruct` | object | ✅ | nested: `FIELD`: string |
| `SLICE` | `Slice` | array of object | ✅ |  |
| `SUBSTRUCT` | `SubStruct` | object | ✅ | nested: `FIELD`: string |
| `TYPE` | `type` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

**POINTEDSTRUCT** (`PointedStruct` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `FIELD` | `Field` | string |

**SUBSTRUCT** (`SubStruct` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `FIELD` | `Field` | string |

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
