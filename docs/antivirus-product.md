# antivirus product

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/anti-virus-product` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AntiVirusProduct`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `NAME` | `name` | string | ✅ |  |
| `PATH` | `path` | string | ✅ |  |
| `SIGNATURE_STATUS` | `signature_status` | string | ✅ |  |
| `STATUS` | `status` | string | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "antivirus product"

detection:
    selection:
        PATH|contains:
            - '/suspicious/'
            - '/tmp/'
        NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
