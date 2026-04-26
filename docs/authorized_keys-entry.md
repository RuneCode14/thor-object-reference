# authorized_keys entry

**Schema ID:** `https://github.com/NextronSystems/jsonlog/thorlog/v3/authorized-keys-entry` | **JSON Schema:** `https://json-schema.org/draft/2020-12/schema` | **Definition:** `AuthorizedKeysEntry`

## Fields

Field names are shown in **UPPERCASE** as used in Sigma rules.
The lowercase JSON name is shown in parentheses for reference.

| Sigma Field | JSON Name | Type | Required | Description | Example Values |
|-------------|-----------|------|----------|-------------|----------------|
| `COMMENT` | `comment` | string | ✅ |  | `user@laptop`, `florian@desktop`, `backup-key` |
| `KEY` | `key` | string | ✅ |  | `ssh-rsa AAAAB3NzaC1yc2E...`, `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5...` |
| `KEY_TYPE` | `key_type` | string | ✅ |  |  |
| `LINE` | `line` | string | ✅ |  |  |
| `TYPE` | `type` | string | ✅ |  | `ssh-rsa`, `ssh-ed25519`, `ecdsa-sha2-nistp256` |

### Nested Field Reference (Sigma Pipe Notation)

Complex types like `File` have nested fields accessed with `|` in Sigma:

_No nested fields in this type._

## Sigma Rule Template

```yaml
logsource:
    product: THOR
    service: "authorized_keys entry"

detection:
    selection:
        TYPE: 'relevant_type'
    condition: selection
```
