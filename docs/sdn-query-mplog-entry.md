# SDN query MPLog entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/sdn-query-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `SdnQueryEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `file` | string | ✅ |  |
| `sha1` | string | ✅ |  |
| `sha256` | string | ✅ |  |
| `time` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "SDN query MPLog entry"

detection:
    selection:
        FILE: null
    condition: selection
```
