# raw firewall rule

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/raw-firewall-rule` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `RawFirewallRule`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `rule` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "raw firewall rule"

detection:
    selection:
        RULE: null
    condition: selection
```
