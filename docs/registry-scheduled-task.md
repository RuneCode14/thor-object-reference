# registry scheduled task

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/registry-scheduled-task` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `RegistryScheduledTask`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `CREATED` | `created` | string (date-time) | ✅ |  |  |
| `GUID` | `guid` | string | ✅ |  |  |
| `LAST_RESULT` | `last_result` | string | ✅ |  |  |
| `LAST_RUN` | `last_run` | string (date-time) | ✅ |  |  |
| `LAST_STOPPED` | `last_stopped` | string (date-time) | ✅ |  |  |
| `PATH` | `path` | string | ✅ |  |  |
| `STATUS` | `status` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `VERSION` | `version` | integer | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "registry scheduled task"

detection:
    selection:
        PATH|contains:
            - '/suspicious/'
            - '/tmp/'
        TYPE: 'relevant_type'
    condition: selection
```
