# TestObject

**Schema ID:** `https://git.bsk/thorx/lib/features/truncate/testobject/test-object` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `TestObject`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `FieldDirect` | string | ✅ |  |
| `Interface` | any | ✅ |  |
| `Map` | object (string) | ✅ |  |
| `PointedStruct` | object | ✅ | nested: `Field`: string |
| `Slice` | array of object | ✅ | nested: `Field`: string |
| `SubStruct` | object | ✅ | nested: `Field`: string |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "TestObject"

detection:
    selection:
        FIELDDIRECT: null
    condition: selection
```
