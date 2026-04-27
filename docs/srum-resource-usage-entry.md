# SRUM Resource Usage Entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/srum-resource-usage-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `SRUMResourceUsageEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `APP_INFO` | `app_info` | string | ✅ |  |  |
| `BACKGROUND_BYTES_READ` | `background_bytes_read` | integer | ✅ |  |  |
| `BACKGROUND_BYTES_WRITTEN` | `background_bytes_written` | integer | ✅ |  |  |
| `BACKGROUND_NUM_READ_OPERATIONS` | `background_num_read_operations` | integer | ✅ |  |  |
| `BACKGROUND_NUM_WRITE_OPERATIONS` | `background_num_write_operations` | integer | ✅ |  |  |
| `FACE_TIME` | `face_time` | integer | ✅ |  |  |
| `FOREGROUND_BYTES_READ` | `foreground_bytes_read` | integer | ✅ |  |  |
| `FOREGROUND_BYTES_WRITTEN` | `foreground_bytes_written` | integer | ✅ |  |  |
| `FOREGROUND_NUM_READ_OPERATIONS` | `foreground_num_read_operations` | integer | ✅ |  |  |
| `FOREGROUND_NUM_WRITE_OPERATIONS` | `foreground_num_write_operations` | integer | ✅ |  |  |
| `TIMESTAMP` | `timestamp` | string (date-time) | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  |  |
| `USER_NAME` | `user_name` | string |  |  |  |
| `USER_SID` | `user_sid` | string | ✅ |  |  |

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "SRUM Resource Usage Entry"

detection:
    selection:
        TYPE: 'relevant_type'
    filter_legitimate:
        USER_NAME|contains:
            - 'root'
            - 'system'
    condition: selection and not filter_legitimate
```
