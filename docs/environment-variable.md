# environment variable

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/environment-variable` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `EnvironmentVariable`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | ✅ |  |
| `value` | string | ✅ |  |
| `variable` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "environment variable"

detection:
    selection:
        TYPE: null
    condition: selection
```
