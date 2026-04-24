# Tomcat user

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/tomcat-user` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `TomcatUser`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | ✅ |  |
| `user` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "Tomcat user"

detection:
    selection:
        TYPE: null
    condition: selection
```
