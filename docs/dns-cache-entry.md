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

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "DNS cache entry"

detection:
    selection:
        IP: '192.168.1.100'
    condition: selection

level: medium
```
