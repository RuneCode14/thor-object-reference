# rootkit

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/rootkit` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Rootkit`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "rootkit"

detection:
    selection:
        TYPE: null
    condition: selection
```
