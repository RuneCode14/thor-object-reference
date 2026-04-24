# THOR Object Reference

Auto-generated from THOR `--describe-object-type all` output.

**Object types:** 89  
**Generated:** 2026-04-24  
**THOR version:** 11.0.0-dev.260424092217

---

This reference maps every THOR object type to its available fields, types, and required status.
Use it when writing custom Sigma rules with `product: THOR`. Fields are **UPPERCASE** in Sigma.

## Platform

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [AIX platform information](aix-platform-information.md) | 9 | `product: THOR, service: "AIX platform information"` |
| [Linux platform information](linux-platform-information.md) | 6 | `product: THOR, service: "Linux platform information"` |
| [MacOS platform information](macos-platform-information.md) | 7 | `product: THOR, service: "MacOS platform information"` |
| [Windows platform information](windows-platform-information.md) | 8 | `product: THOR, service: "Windows platform information"` |

## Execution History

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [AmCache entry](amcache-entry.md) | 5 | `product: THOR, service: "AmCache entry"` |
| [web download](web-download.md) | 3 | `product: THOR, service: "web download"` |
| [web page visit](web-page-visit.md) | 4 | `product: THOR, service: "web page visit"` |

## Network

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [DNS cache entry](dns-cache-entry.md) | 3 | `product: THOR, service: "DNS cache entry"` |
| [firewall rule](firewall-rule.md) | 6 | `product: THOR, service: "firewall rule"` |
| [hosts file entry](hosts-file-entry.md) | 2 | `product: THOR, service: "hosts file entry"` |
| [network session](network-session.md) | 12 | `product: THOR, service: "network session"` |
| [network share](network-share.md) | 8 | `product: THOR, service: "network share"` |
| [process connection](process-connection.md) | 10 | `product: THOR, service: "process connection"` |

## Persistence & System

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [at job](at-job.md) | 5 | `product: THOR, service: "at job"` |
| [autorun entry](autorun-entry.md) | 6 | `product: THOR, service: "autorun entry"` |
| [cron job](cron-job.md) | 5 | `product: THOR, service: "cron job"` |
| [init.d service](init.d-service.md) | 5 | `product: THOR, service: "init.d service"` |
| [Linux kernel module](linux-kernel-module.md) | 13 | `product: THOR, service: "Linux kernel module"` |
| [scheduled task](scheduled-task.md) | 8 | `product: THOR, service: "scheduled task"` |
| [systemd service](systemd-service.md) | 6 | `product: THOR, service: "systemd service"` |
| [WMI startup command](wmi-startup-command.md) | 5 | `product: THOR, service: "WMI startup command"` |
| [Windows service](windows-service.md) | 8 | `product: THOR, service: "Windows service"` |

## File System

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [file](file.md) | 16 | `product: THOR, service: "file"` |
| [jump list entry](jump-list-entry.md) | 6 | `product: THOR, service: "jump list entry"` |
| [MFT entry](mft-entry.md) | 32 | `product: THOR, service: "MFT entry"` |
| [prefetch info](prefetch-info.md) | 9 | `product: THOR, service: "prefetch info"` |
| [shim cache entry](shim-cache-entry.md) | 5 | `product: THOR, service: "shim cache entry"` |

## Registry

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [registry key](registry-key.md) | 5 | `product: THOR, service: "registry key"` |
| [registry value](registry-value.md) | 5 | `product: THOR, service: "registry value"` |

## Identity & Auth

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [authorized_keys entry](authorized_keys-entry.md) | 5 | `product: THOR, service: "authorized_keys entry"` |
| [logged in user](logged-in-user.md) | 4 | `product: THOR, service: "logged in user"` |
| [LSA session](lsa-session.md) | 6 | `product: THOR, service: "LSA session"` |
| [Unix user](unix-user.md) | 8 | `product: THOR, service: "Unix user"` |
| [Windows user](windows-user.md) | 9 | `product: THOR, service: "Windows user"` |

## Process & Memory

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [process](process.md) | 16 | `product: THOR, service: "process"` |
| [process handle](process-handle.md) | 7 | `product: THOR, service: "process handle"` |
| [thread](thread.md) | 9 | `product: THOR, service: "thread"` |

## Logs & Events

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [audit log entry](audit-log-entry.md) | 6 | `product: THOR, service: "audit log entry"` |
| [eventlog entry](eventlog-entry.md) | 8 | `product: THOR, service: "eventlog entry"` |
| [journal log entry](journal-log-entry.md) | 6 | `product: THOR, service: "journal log entry"` |
| [log line](log-line.md) | 5 | `product: THOR, service: "log line"` |

## Security & Kernel

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [antivirus exclusion](antivirus-exclusion.md) | 4 | `product: THOR, service: "antivirus exclusion"` |
| [eBPF program](ebpf-program.md) | 8 | `product: THOR, service: "eBPF program"` |
| [mutex](mutex.md) | 4 | `product: THOR, service: "mutex"` |
| [named pipe](named-pipe.md) | 6 | `product: THOR, service: "named pipe"` |
