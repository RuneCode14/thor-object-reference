# THOR Object Type Reference

Auto-generated reference documentation for all THOR object types derived from `thor --describe-object-type all`.

## What Is This?

THOR v11 supports custom Sigma rules that match on **THOR's own scan objects** (not just Windows Event Logs). This project converts THOR's internal JSON schema definitions into a human-readable reference for detection engineers.

## Usage

Browse the [`docs/`](docs/) directory for per-type Markdown documentation, or search for the object type you need.

### Quick Start for Detection Engineers

Every object type documentation includes:
- **Available fields** with types and required status
- **Sigma rule template** with the correct `logsource` header
- **Nested field references** for complex objects

Example for `systemd service`:

```yaml
title: Suspicious systemd service from /tmp
logsource:
    product: THOR
    service: "systemd service"
detection:
    selection:
        IMAGE|contains: '/tmp/'
    condition: selection
level: high
```

## Generating the Reference

### Prerequisites

- Python 3.9+
- THOR v11+ binary (`thor-linux-64` or equivalent)

### Steps

```bash
# 1. Generate THOR object types JSON
./thor-linux-64 --describe-object-type all > thor-object-types.json

# 2. Run the generator
python3 generate_reference.py thor-object-types.json --output-dir docs --format both

# 3. The docs/ directory now contains Markdown + YAML per type + README.md index
```

## Repository Layout

```
.
├── generate_reference.py      # The conversion script
├── docs/                      # Generated reference docs
│   ├── README.md              # Index page with all object types
│   ├── linux-kernel-module.md # Per-type documentation
│   ├── systemd-service.md
│   └── ... (89 object types)
├── examples/                  # Example Sigma rules
├── .github/workflows/         # CI/CD workflows
└── README.md                  # This file
```

## Releasing

The project ships with a GitHub Actions workflow that:
1. Accepts a THOR binary URL or runs on schedule
2. Generates the object reference
3. Commits updated docs back to the repository

Trigger manually via workflow dispatch, or on a THOR release to regenerate.

## Contributing

- **Script improvements:** PRs to `generate_reference.py` are welcome.
- **New THOR version:** Run the generator with the new THOR binary and open a PR with updated docs.
- **Example rules:** Add useful example Sigma rules to `examples/`.

## License

MIT License — feel free to fork and adapt for your organization's needs.
