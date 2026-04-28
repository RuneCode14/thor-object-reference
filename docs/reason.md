# reason

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/reason` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Reason`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `MATCHED` | `matched` | array | null | ✅ |  |  |
| `SIGNATURE` | `signature` | object | ✅ | Object, see [SIGNATURE Nested Fields](#signature-nested-fields) below |  |
| `SUMMARY` | `summary` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### SIGNATURE JSON Sub-Fields

> ⚠️ **These nested fields are for JSON reference only.** THOR's Sigma backend matches on **top-level fields only**. You cannot use `IMAGE.PATH`, `IMAGE_PATH`, or `PARENT_INFO.PID` in Sigma rules. Object fields like `IMAGE` and `PARENT_INFO` can be checked with `FIELD: null` for fileless/orphan detection.

Nested JSON structure within `signature` (type: object):

| JSON Path | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| `score` | integer | |  |
| `reference` | array | null | |  |
| `origin` | string | |  |
| `kind` | string | |  |
| `date` | string | |  |
| `tags` | array | null | |  |
| `rule_name` | string | |  |
| `description` | string | |  |
| `author` | string | |  |
| `id` | string | |  |
| `false_positives` | array | null | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "reason"

detection:
    selection:
        SUMMARY|contains: 'suspicious_string'
    condition: selection

level: medium
```
