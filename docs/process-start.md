# process start

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/eventlog-process-start` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `EventlogProcessStart`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `PROCESS` | `process` | string | ✅ |  | `C:\Windows\SystemTemp\A01DF562-5405-4537...`, `C:\Windows\SoftwareDistribution\Download...`, `C:\Windows\System32\la57setup.exe` |
| `START_TIMES` | `start_times` | array of string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "process start"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
