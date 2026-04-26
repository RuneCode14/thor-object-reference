# hosts file entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/hosts-file-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `HostsFileEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `HOST` | `host` | string | ✅ |  |  |
| `IP` | `ip` | string | ✅ |  | `127.0.0.1`, `192.168.1.100`, `0.0.0.0` |
| `TYPE` | `type` | string | ✅ |  | `hosts file entry` |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "hosts file entry"

detection:
    selection:
        TYPE: 'relevant_type'
        IP|contains:
            - '192.168.'
            - '10.'
    condition: selection
```
