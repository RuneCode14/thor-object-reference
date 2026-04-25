# firewall rule

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/firewall-rule` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `FirewallRule`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `ALLOW` | `allow` | boolean | ✅ |  |
| `ENABLED` | `enabled` | boolean | ✅ |  |
| `INBOUND` | `inbound` | boolean | ✅ |  |
| `LOCAL_IPS` | `local_ips` | array | null | ✅ |  |
| `LOCAL_PORTS` | `local_ports` | array | null | ✅ |  |
| `NAME` | `name` | string | ✅ |  |
| `PATH` | `path` | string | ✅ |  |
| `PROTOCOL` | `protocol` | string | ✅ |  |
| `REMOTE_IPS` | `remote_ips` | array | null | ✅ |  |
| `REMOTE_PORTS` | `remote_ports` | array | null | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "firewall rule"

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
