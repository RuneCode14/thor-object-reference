# THOR assessment

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/assessment` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Assessment`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `CONTEXT` | `context` | array | null | ✅ |  |  |
| `ISSUES` | `issues` | array of object |  |  |  |
| `LOG_VERSION` | `log_version` | string | ✅ |  |  |
| `MESSAGE` | `message` | string | ✅ |  |  |
| `META` | `meta` | object | ✅ | Object, see [META Nested Fields](#meta-nested-fields) below |  |
| `REASON_COUNT` | `reason_count` | integer |  |  |  |
| `REASONS` | `reasons` | array of object | ✅ |  |  |
| `SCORE` | `score` | integer | ✅ |  |  |
| `SUBJECT` | `subject` | any | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### META Nested Fields

Nested fields within `meta` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `META.TIME` | `time` | string (date-time) | |  |
| `META.LEVEL` | `level` | string | |  |
| `META.MODULE` | `module` | string | |  |
| `META.SCAN_ID` | `scan_id` | string | |  |
| `META.EVENT_ID` | `event_id` | string | |  |
| `META.HOSTNAME` | `hostname` | string | |  |

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
