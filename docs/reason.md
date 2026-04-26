# reason

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/reason` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `Reason`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `MATCHED` | `matched` | array | null | ✅ |  |  |
| `SIGNATURE` | `signature` | object | ✅ | nested: `SCORE`: integer; `REFERENCE`: array \| null; `ORIGIN`: string; `KIND`: string; `DATE`: string; `TAGS`: array \| null; `RULE_NAME`: string; `DESCRIPTION`: string; `AUTHOR`: string; `ID`: string; `FALSE_POSITIVES`: array \| null |  |
| `SUMMARY` | `summary` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

**SIGNATURE** (`signature` — object):

| Sigma Field | JSON Path | Type |
|-------------|-----------|------|
| `SCORE` | `score` | integer |
| `REFERENCE` | `reference` | array | null |
| `ORIGIN` | `origin` | string |
| `KIND` | `kind` | string |
| `DATE` | `date` | string |
| `TAGS` | `tags` | array | null |
| `RULE_NAME` | `rule_name` | string |
| `DESCRIPTION` | `description` | string |
| `AUTHOR` | `author` | string |
| `ID` | `id` | string |
| `FALSE_POSITIVES` | `false_positives` | array | null |

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
