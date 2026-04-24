# web page visit

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/web-page-visit` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WebPageVisit`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `time` | string (date-time) | ✅ |  |
| `title` | string | ✅ |  |
| `type` | string | ✅ |  |
| `url` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "web page visit"

detection:
    selection:
        TIME: null
    condition: selection
```
