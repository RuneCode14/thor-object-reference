# MacOS platform information

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/platform-info-macos` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `PlatformInfoMacos`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `ARCH` | `arch` | string | ✅ |  |  |
| `KERNEL_NAME` | `kernel_name` | string | ✅ |  |  |
| `KERNEL_VERSION` | `kernel_version` | string | ✅ |  |  |
| `NAME` | `name` | string | ✅ |  |  |
| `PROC` | `proc` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `VERSION` | `version` | string | ✅ |  |  |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "MacOS platform information"

detection:
    selection:
        KERNEL_NAME|contains:
            - 'suspicious'
            - 'malware'
        TYPE: 'relevant_type'
    condition: selection
```
