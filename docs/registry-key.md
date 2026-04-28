# registry key

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/registry-key` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `RegistryKey`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `KEY` | `key` | string | ✅ |  | `SOFTWARE\Classes\CLSID\{E15E1D68-0D1C-49F7-BEB8-812B1E00FA60}\InProcServer32` |
| `MODIFIED` | `modified` | string (date-time) | ✅ |  | `2026-03-29T12:10:29.5119743+02:00` |
| `TYPE` | `type` | string | ✅ |  | `registry key` |
| `VALUES` | `values` | string | ✅ |  | `SOFTWARE\Classes\CLSID\{E15E1D68-0D1C-49F7-BEB8-812B1E00FA60}\InProcServer32;(Default);C:\Program Files (x86)\WinSCP\DragExt64.dll` |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "registry key"

detection:
    selection:
        KEY|contains: 'suspicious_string'
    condition: selection

level: medium
```
