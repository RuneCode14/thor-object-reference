# process connection

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/process-connection-object` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ProcessConnectionObject`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `IP` | `ip` | string | ✅ |  |  |
| `PORT` | `port` | integer | ✅ |  |  |
| `PROTOCOL` | `protocol` | string |  |  |  |
| `REMOTE_IP` | `remote_ip` | string |  |  |  |
| `REMOTE_PORT` | `remote_port` | integer |  |  |  |
| `STATUS` | `status` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "process connection"

detection:
    selection:
        TYPE: 'relevant_type'
        IP|contains:
            - '192.168.'
            - '10.'
    condition: selection
```
