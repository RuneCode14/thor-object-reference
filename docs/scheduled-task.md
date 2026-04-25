# scheduled task

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/scheduled-task` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ScheduledTask`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description |
|-------------|-----------|------|----------|-------------|
| `COM_HANDLERS` | `com_handlers` | array of string |  |  |
| `COMMANDS` | `commands` | array of string | ✅ |  |
| `ENABLED` | `enabled` | boolean | ✅ |  |
| `LAST_RUN` | `last_run` | string (date-time) | ✅ |  |
| `LOGON_TYPE` | `logon_type` | string | ✅ |  |
| `NAME` | `name` | string | ✅ |  |
| `NEXT_RUN` | `next_run` | string (date-time) | ✅ |  |
| `PATH` | `path` | string | ✅ |  |
| `PRIVILEGES` | `privileges` | array of string |  |  |
| `RUN_LEVEL` | `run_level` | string | ✅ |  |
| `TRIGGERS` | `triggers` | array of string |  |  |
| `TYPE` | `type` | string | ✅ |  |
| `USER` | `user` | string | ✅ |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "scheduled task"

detection:
    selection:
        PATH|contains:
            - '/suspicious/'
            - '/tmp/'
        NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    filter_legitimate:
        USER|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
