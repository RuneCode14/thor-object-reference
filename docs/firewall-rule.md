# firewall rule

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/firewall-rule` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `FirewallRule`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `allow` | boolean | ✅ |  |
| `enabled` | boolean | ✅ |  |
| `inbound` | boolean | ✅ |  |
| `local_ips` | array | null | ✅ |  |
| `local_ports` | array | null | ✅ |  |
| `name` | string | ✅ |  |
| `path` | string | ✅ |  |
| `protocol` | string | ✅ |  |
| `remote_ips` | array | null | ✅ |  |
| `remote_ports` | array | null | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "firewall rule"

detection:
    selection:
        ALLOW: null
    condition: selection
```
