# multiChoiceA

**Schema ID:** `https://git.bsk/thorx/lib/features/truncate/testobject/multi-choice-object-a` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `MultiChoiceObjectA`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `FIELDA` | `FieldA` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "multiChoiceA"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
