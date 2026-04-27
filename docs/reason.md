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

### SIGNATURE Nested Fields

Nested fields within `signature` (type: object):

| Full Sigma Field | JSON Path | Type | Description | Example Values |
|------------------|-----------|------|-------------|----------------|
| `SIGNATURE.SCORE` | `score` | integer | |  |
| `SIGNATURE.REFERENCE` | `reference` | array | null | |  |
| `SIGNATURE.ORIGIN` | `origin` | string | |  |
| `SIGNATURE.KIND` | `kind` | string | |  |
| `SIGNATURE.DATE` | `date` | string | |  |
| `SIGNATURE.TAGS` | `tags` | array | null | |  |
| `SIGNATURE.RULE_NAME` | `rule_name` | string | |  |
| `SIGNATURE.DESCRIPTION` | `description` | string | |  |
| `SIGNATURE.AUTHOR` | `author` | string | |  |
| `SIGNATURE.ID` | `id` | string | |  |
| `SIGNATURE.FALSE_POSITIVES` | `false_positives` | array | null | |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "reason"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
