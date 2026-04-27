# network share

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/network-share` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `NetworkShare`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `NAME` | `name` | string | ✅ |  |  |
| `PATH` | `path` | string | ✅ |  |  |
| `PERMISSIONS` | `permissions` | array of object | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "network share"

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
