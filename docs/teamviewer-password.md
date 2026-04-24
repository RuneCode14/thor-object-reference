# TeamViewer password

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/team-viewer-password` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `TeamViewerPassword`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ |  |
| `password` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "TeamViewer password"

detection:
    selection:
        NAME: null
    condition: selection
```
