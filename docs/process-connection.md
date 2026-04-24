# process connection

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/process-connection-object` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ProcessConnectionObject`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ip` | string | ✅ |  |
| `port` | integer | ✅ |  |
| `protocol` | string |  |  |
| `remote_ip` | string |  |  |
| `remote_port` | integer |  |  |
| `status` | string | ✅ |  |
| `type` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "process connection"

detection:
    selection:
        IP: null
    condition: selection
```
