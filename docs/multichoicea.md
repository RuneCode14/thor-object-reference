# multiChoiceA

**Schema ID:** `https://git.bsk/thorx/lib/features/truncate/testobject/multi-choice-object-a` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `MultiChoiceObjectA`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `FieldA` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "multiChoiceA"

detection:
    selection:
        FIELDA: null
    condition: selection
```
