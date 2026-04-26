# antivirus exclusion

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/anti-virus-exclude` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AntiVirusExclude`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `EXCLUSION` | `exclusion` | string | ✅ |  |  |
| `EXCLUSION_TYPE` | `exclusion_type` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "antivirus exclusion"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
