# mutex

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/windows-mutex` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `WindowsMutex`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `mutex` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "mutex"

detection:
    selection:
        MUTEX: null
    condition: selection
```
