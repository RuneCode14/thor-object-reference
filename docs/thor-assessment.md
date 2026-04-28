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

### META JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `meta` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `time` | string (date-time) | |  |
| `level` | string | |  |
| `module` | string | |  |
| `scan_id` | string | |  |
| `event_id` | string | |  |
| `hostname` | string | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "THOR assessment"

detection:
    selection:
        LOG_VERSION|contains: 'suspicious_string'
    condition: selection

level: medium
```
