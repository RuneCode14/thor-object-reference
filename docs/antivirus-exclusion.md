# antivirus exclusion

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/anti-virus-exclude` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AntiVirusExclude`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `exclusion` | string | ✅ |  |
| `exclusion_type` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "antivirus exclusion"

detection:
    selection:
        EXCLUSION: null
    condition: selection
```
