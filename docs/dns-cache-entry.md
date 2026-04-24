# DNS cache entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/dns-cache-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `DnsCacheEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `host` | string | ✅ |  |
| `ip` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "DNS cache entry"

detection:
    selection:
        HOST: null
    condition: selection
```
