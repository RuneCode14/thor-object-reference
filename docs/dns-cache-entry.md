# DNS cache entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/dns-cache-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `DnsCacheEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `HOST` | `host` | string | ✅ |  |  |
| `IP` | `ip` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "DNS cache entry"

detection:
    selection:
        TYPE: 'relevant_type'
        IP|contains:
            - '192.168.'
            - '10.'
    condition: selection
```
