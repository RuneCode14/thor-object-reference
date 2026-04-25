# THOR assessment

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/assessment` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Assessment`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `CONTEXT` | `context` | array | null | ✅ |  |
| `ISSUES` | `issues` | array of object |  |  |
| `LOG_VERSION` | `log_version` | string | ✅ |  |
| `MESSAGE` | `message` | string | ✅ |  |
| `META` | `meta` | object | ✅ | nested: `TIME`: string (date-time); `LEVEL`: string; `MODULE`: string; `SCAN_ID`: string; `EVENT_ID`: string; `HOSTNAME`: string |
| `REASON_COUNT` | `reason_count` | integer |  |  |
| `REASONS` | `reasons` | array of object | ✅ |  |
| `SCORE` | `score` | integer | ✅ |  |
| `SUBJECT` | `subject` | any | ✅ |  |
| `TYPE` | `type` | string | ✅ |  |

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
    service: "THOR assessment"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
