# hosts file entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/hosts-file-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `HostsFileEntry`

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
    service: "hosts file entry"

detection:
    selection:
        HOST: null
    condition: selection
```
