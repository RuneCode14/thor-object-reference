# THOR v11: Write Sigma Rules on Any Scan Object

THOR v11 introduces a powerful new capability for detection engineers: **custom Sigma rules that match on THOR's own scan output**. Every element THOR observes — processes, users, kernel modules, services, files — is now a first-class object you can write detections against using the open Sigma standard.

## What's New

In THOR v11, every observed element is represented as a structured JSON object with a well-defined schema. Rather than keeping this data internal, THOR now exposes these objects to Sigma matching. This means you can:

- **Detect suspicious processes** by matching on command lines, image paths, or parent-child relationships
- **Find persistence mechanisms** in cron jobs, systemd services, autorun entries, or scheduled tasks
- **Spot rootkits** by looking at kernel modules without associated files
- **Hunt for malicious users** by checking UID ranges, shell assignments, or home directories
- **Write detections on any of the 90+ object types** THOR produces

And you do it all with standard Sigma syntax — the same format used for Windows Event Logs, but now applied to THOR's internal scan objects.

## How It Works

### Logsource Format

To match on THOR objects, use `product: THOR` and set `service` to the **object type name**:

```yaml
logsource:
    product: THOR
    service: "process"
```

The `service` field must match the object type name exactly. THOR includes 90+ object types — here are the most commonly used for detection:

| Category | Object Types |
|----------|-------------|
| **Process & Memory** | `process`, `process connection`, `process handle`, `thread` |
| **Persistence** | `autorun entry`, `cron job`, `scheduled task`, `systemd service`, `Windows service`, `WMI startup command` |
| **File System** | `file`, `MFT entry`, `prefetch info`, `shim cache entry` |
| **Users & Auth** | `Windows user`, `Unix user`, `authorized_keys entry`, `logged in user` |
| **Security & Kernel** | `Linux kernel module`, `eBPF program`, `antivirus exclusion` |
| **Network** | `DNS cache entry`, `firewall rule`, `hosts file entry` |
| **Logs & Events** | `eventlog entry`, `log line`, `journal log entry`, `audit log entry` |
| **Execution History** | `AmCache entry`, `web page visit`, `web download` |

> **Full list:** Run `./thor-linux-64 --describe-object-type all` or browse the [`docs/`](docs/) directory in this repo.

### Field Naming Convention

Fields from the JSON schema are converted to **UPPERCASE** in Sigma rules:

| JSON Schema Field | Sigma Field |
|-------------------|-------------|
| `command` | `COMMAND` |
| `name` | `NAME` |
| `pid` | `PID` |
| `service_name` | `SERVICE_NAME` |
| `included_in_kernel` | `INCLUDED_IN_KERNEL` |

Standard Sigma modifiers work as expected: `|contains`, `|endswith`, `|startswith`, `|re`.

To match null or empty fields:

```yaml
detection:
    selection:
        FILE: null
```

## Workflow for Detection Engineers

### Step 1: Discover Available Object Types

```bash
# List all object types with their JSON schemas
./thor-linux-64 --describe-object-type all

# View schema for a specific type
./thor-linux-64 --describe-object-type "Unix user"
```

### Step 2: Inspect Real Objects

Run THOR against a single module and log the objects to see what fields and values are actually present on your target system:

```bash
# Log up to 50 Unix user objects during a scan
./thor-linux-64 --module Users --log-object "Unix user:50" --console-json

# Log process objects (great for understanding available fields)
./thor-linux-64 --module ProcessCheck --log-object "process:10" --console-json
```

### Step 3: Write Your Sigma Rule

Based on what you observed, write a rule using UPPERCASE field names:

```yaml
title: Non-Standard User with Shell Access
logsource:
    product: THOR
    service: "Unix user"
detection:
    selection_low_uid:
        UID|lt: '500'
    selection_shell:
        SHELL|endswith: '/bash'
    filter_root:
        NAME: 'root'
    condition: selection_low_uid and selection_shell and not filter_root
level: medium
```

### Step 4: Deploy and Test

1. Save your rule as a `.yml` file
2. Copy to `custom-signatures/sigma/` in your THOR directory:
   ```bash
   cp my-rule.yml /path/to/thor/custom-signatures/sigma/
   ```
3. Verify it loaded:
   ```bash
   ./thor-linux-64 --list-signatures | grep "my-rule"
   ```
4. Run a targeted scan to test:
   ```bash
   ./thor-linux-64 --module Users --deep
   ```

> **Note on severity levels:** By default, only `critical` and `high` level Sigma rules produce detections. Use `--deep` to include `medium` level rules, or `--sigma-threshold low` to include all levels.

## Detection Examples

### Process with Encoded PowerShell

```yaml
title: Process with Encoded PowerShell Execution
logsource:
    product: THOR
    service: process
detection:
    selection:
        COMMAND|contains:
            - ' -enc '
            - ' -EncodedCommand '
        NAME|endswith:
            - 'powershell.exe'
            - 'pwsh.exe'
    condition: selection
level: high
```

### Linux Kernel Module Without File (Rootkit)

```yaml
title: Kernel Module Without File
logsource:
    product: THOR
    service: "Linux kernel module"
detection:
    selection:
        FILE: null
        INCLUDED_IN_KERNEL: false
    condition: selection
level: medium
```

### Suspicious Cron Job

```yaml
title: Cron Job with Suspicious Download Command
logsource:
    product: THOR
    service: "cron job"
detection:
    selection_download:
        COMMAND|contains:
            - 'wget '
            - 'curl '
    selection_pipe:
        COMMAND|contains:
            - '| bash'
            - '| sh'
    condition: selection_download and selection_pipe
level: medium
```

### Autorun Entry from Suspicious Location

```yaml
title: Autorun Entry from Suspicious Location
logsource:
    product: THOR
    service: "autorun entry"
detection:
    selection_path:
        LAUNCH_STRING|contains:
            - '\\AppData\\Roaming\\'
            - '\\Users\\Public\\'
            - '\\Temp\\'
    selection_script:
        LAUNCH_STRING|contains:
            - '.vbs'
            - '.hta'
            - 'powershell'
    condition: selection_path and selection_script
level: high
```

## Object Type Reference

This repository contains auto-generated reference documentation for **all 89 THOR object types**. Each type has:

- **Markdown doc** with full field listings, types, and descriptions
- **YAML file** with a ready-to-use Sigma rule template
- **Nested field breakdown** for complex objects

Browse the [`docs/`](docs/) directory or search for the object type you need.

### Quick Reference: Common Object Types

| Use Case | Object Type | Key Fields |
|----------|-------------|------------|
| Process monitoring | `process` | `COMMAND`, `NAME`, `OWNER`, `PID` |
| Linux persistence | `cron job` | `COMMAND`, `USER`, `SCHEDULE` |
| Windows persistence | `scheduled task` | `COMMANDS`, `USER`, `RUN_LEVEL` |
| Autoruns | `autorun entry` | `LAUNCH_STRING`, `LOCATION` |
| Windows services | `Windows service` | `SERVICE_NAME`, `IMAGE` |
| Linux services | `systemd service` | `COMMAND`, `RUN_AS_USER` |
| Kernel rootkits | `Linux kernel module` | `FILE`, `INCLUDED_IN_KERNEL` |
| File hashes | `file` | `MD5`, `SHA1`, `SHA256`, `PATH` |
| Execution history | `AmCache entry` | `SHA1`, `PATH`, `PRODUCT` |

## Generating the Reference

The docs in this repo were generated from THOR's `--describe-object-type all` output. To regenerate for a new THOR version:

```bash
# 1. Export object type schemas
./thor-linux-64 --describe-object-type all > thor-object-types.json

# 2. Run the generator
python3 generate_reference_v3.py thor-object-types.json --output-dir docs

# 3. Commit updated docs
git add docs/ && git commit -m "Update object reference for THOR vX.Y.Z"
```

## CI/CD

The repo includes a GitHub Actions workflow that regenerates the reference on schedule or via manual trigger. See [`.github/workflows/generate.yml`](.github/workflows/generate.yml).

## Contributing

- **Script improvements:** PRs to `generate_reference_v3.py` welcome
- **New THOR version:** Run the generator and open a PR with updated docs
- **Example rules:** Add useful Sigma rules to `examples/`

## License

MIT License — feel free to fork and adapt for your organization's needs.

---

*This reference is auto-generated from THOR v11's `--describe-object-type all` output. For the authoritative THOR documentation, see the [THOR User Manual](https://thor-manual.nextron-systems.com/en/v11/signatures/sigma.html).*
