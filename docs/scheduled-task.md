# scheduled task

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/scheduled-task` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `ScheduledTask`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `COM_HANDLERS` | `com_handlers` | array of string |  |  |  |
| `COMMANDS` | `commands` | array of string | ✅ |  | `C:\Windows\System32\svchost.exe -k netsv...`, `powershell -Command Update-Help`, `C:\Users\Public\update.exe` |
| `ENABLED` | `enabled` | boolean | ✅ |  | `true`, `false` |
| `LAST_RUN` | `last_run` | string (date-time) | ✅ |  | `2026-04-26T03:00:00Z`, `never` |
| `LOGON_TYPE` | `logon_type` | string | ✅ |  |  |
| `NAME` | `name` | string | ✅ |  | `\Microsoft\Windows\Defender\Windows Defe...`, `\MyApp\BackupTask`, `\Malware\Persistence` |
| `NEXT_RUN` | `next_run` | string (date-time) | ✅ |  | `2026-04-27T03:00:00Z`, `never` |
| `PATH` | `path` | string | ✅ |  |  |
| `PRIVILEGES` | `privileges` | array of string |  |  |  |
| `RUN_LEVEL` | `run_level` | string | ✅ |  | `highest`, `limited` |
| `TRIGGERS` | `triggers` | array of string |  |  |  |
| `TYPE` | `type` | string | ✅ |  | `scheduled task` |
| `USER` | `user` | string | ✅ |  | `SYSTEM`, `neo`, `NT AUTHORITY\SYSTEM` |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "scheduled task"

detection:
    selection:
        COMMANDS|contains: 'suspicious_command'
    condition: selection

level: medium
```
