# THOR message

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/message` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Message`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `FIELDS` | `fields` | null | object | ✅ |  |  |
| `LOG_VERSION` | `log_version` | string | ✅ |  |  |
| `MESSAGE` | `message` | string | ✅ |  |  |
| `META` | `meta` | object | ✅ | nested: `TIME`: string (date-time); `LEVEL`: string; `MODULE`: string; `SCAN_ID`: string; `EVENT_ID`: string; `HOSTNAME`: string |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

**META** (`meta` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `TIME` | `time` | string (date-time) |
| `LEVEL` | `level` | string |
| `MODULE` | `module` | string |
| `SCAN_ID` | `scan_id` | string |
| `EVENT_ID` | `event_id` | string |
| `HOSTNAME` | `hostname` | string |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "THOR message"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
