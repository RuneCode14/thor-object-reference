# rootkit

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/rootkit` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Rootkit`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "rootkit"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
