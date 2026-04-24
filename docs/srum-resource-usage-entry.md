# SRUM Resource Usage Entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/srum-resource-usage-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `SRUMResourceUsageEntry`

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `app_info` | string | ✅ |  |
| `background_bytes_read` | integer | ✅ |  |
| `background_bytes_written` | integer | ✅ |  |
| `background_num_read_operations` | integer | ✅ |  |
| `background_num_write_operations` | integer | ✅ |  |
| `face_time` | integer | ✅ |  |
| `foreground_bytes_read` | integer | ✅ |  |
| `foreground_bytes_written` | integer | ✅ |  |
| `foreground_num_read_operations` | integer | ✅ |  |
| `foreground_num_write_operations` | integer | ✅ |  |
| `timestamp` | string (date-time) | ✅ |  |
| `type` | string | ✅ |  |
| `user_name` | string |  |  |
| `user_sid` | string | ✅ |  |

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "SRUM Resource Usage Entry"

detection:
    selection:
        APP_INFO: null
    condition: selection
```
