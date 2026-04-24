# antivirus product

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/anti-virus-product` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AntiVirusProduct`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ |  |
| `path` | string | ✅ |  |
| `signature_status` | string | ✅ |  |
| `status` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "antivirus product"

detection:
    selection:
        NAME: null
    condition: selection
```
