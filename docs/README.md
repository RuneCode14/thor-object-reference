# THOR Object Type Reference

Source: THOR `--describe-object-type all` (89 object types)

This reference maps every THOR object type to its available fields, types, and required status.
Use it when writing custom Sigma rules with `product: THOR`.

**Field naming convention:**
- In THOR JSON output: **lowercase** with underscores (e.g., `run_as_user`)
- In Sigma rules: **UPPERCASE** (e.g., `RUN_AS_USER`)
- Nested fields use **pipe notation** in Sigma (e.g., `IMAGE|PATH`, `UNIT|HASHES|SHA256`)

## Platform

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [AIX platform information](docs/aix-platform-information.md) | 9 | `product: THOR, service: "AIX platform information"` |
| [Linux platform information](docs/linux-platform-information.md) | 6 | `product: THOR, service: "Linux platform information"` |
| [MacOS platform information](docs/macos-platform-information.md) | 7 | `product: THOR, service: "MacOS platform information"` |
| [Windows platform information](docs/windows-platform-information.md) | 8 | `product: THOR, service: "Windows platform information"` |

## Execution History

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [AmCache entry](docs/amcache-entry.md) | 9 | `product: THOR, service: "AmCache entry"` |
| [web download](docs/web-download.md) | 4 | `product: THOR, service: "web download"` |
| [web page visit](docs/web-page-visit.md) | 4 | `product: THOR, service: "web page visit"` |

## Network

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [DNS cache entry](docs/dns-cache-entry.md) | 3 | `product: THOR, service: "DNS cache entry"` |
| [MS Office connection cache entry](docs/ms-office-connection-cache-entry.md) | 4 | `product: THOR, service: "MS Office connection cache entry"` |
| [firewall rule](docs/firewall-rule.md) | 11 | `product: THOR, service: "firewall rule"` |
| [network session](docs/network-session.md) | 7 | `product: THOR, service: "network session"` |
| [network share](docs/network-share.md) | 4 | `product: THOR, service: "network share"` |
| [raw firewall rule](docs/raw-firewall-rule.md) | 2 | `product: THOR, service: "raw firewall rule"` |

## Logs & Events

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [DetectionAdd MPLog entry](docs/detectionadd-mplog-entry.md) | 4 | `product: THOR, service: "DetectionAdd MPLog entry"` |
| [EMS detection MPLog entry](docs/ems-detection-mplog-entry.md) | 4 | `product: THOR, service: "EMS detection MPLog entry"` |
| [EstimatedImpact MPLog entry](docs/estimatedimpact-mplog-entry.md) | 5 | `product: THOR, service: "EstimatedImpact MPLog entry"` |
| [SDN query MPLog entry](docs/sdn-query-mplog-entry.md) | 5 | `product: THOR, service: "SDN query MPLog entry"` |
| [audit log entry](docs/audit-log-entry.md) | 2 | `product: THOR, service: "audit log entry"` |
| [eventlog entry](docs/eventlog-entry.md) | 2 | `product: THOR, service: "eventlog entry"` |
| [journal log entry](docs/journal-log-entry.md) | 3 | `product: THOR, service: "journal log entry"` |
| [log line](docs/log-line.md) | 3 | `product: THOR, service: "log line"` |

## Identity & Auth

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [DoublePulsar Handshake](docs/doublepulsar-handshake.md) | 3 | `product: THOR, service: "DoublePulsar Handshake"` |
| [LSA session](docs/lsa-session.md) | 8 | `product: THOR, service: "LSA session"` |
| [Tomcat user](docs/tomcat-user.md) | 2 | `product: THOR, service: "Tomcat user"` |
| [Unix user](docs/unix-user.md) | 9 | `product: THOR, service: "Unix user"` |
| [User Access Log Entry](docs/user-access-log-entry.md) | 12 | `product: THOR, service: "User Access Log Entry"` |
| [Windows user](docs/windows-user.md) | 12 | `product: THOR, service: "Windows user"` |
| [authorized_keys entry](docs/authorized_keys-entry.md) | 5 | `product: THOR, service: "authorized_keys entry"` |
| [groups.xml user](docs/groups.xml-user.md) | 3 | `product: THOR, service: "groups.xml user"` |
| [logged in user](docs/logged-in-user.md) | 5 | `product: THOR, service: "logged in user"` |

## Other

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [KnowledgeDB entry](docs/knowledgedb-entry.md) | 6 | `product: THOR, service: "KnowledgeDB entry"` |
| [PowerShell module analysis cache module entry](docs/powershell-module-analysis-cache-module-entry.md) | 3 | `product: THOR, service: "PowerShell module analysis cache module entry"` |
| [SRUM Resource Usage Entry](docs/srum-resource-usage-entry.md) | 14 | `product: THOR, service: "SRUM Resource Usage Entry"` |
| [THOR assessment](docs/thor-assessment.md) | 10 | `product: THOR, service: "THOR assessment"` |
| [THOR invocation information](docs/thor-invocation-information.md) | 17 | `product: THOR, service: "THOR invocation information"` |
| [THOR message](docs/thor-message.md) | 5 | `product: THOR, service: "THOR message"` |
| [TeamViewer password](docs/teamviewer-password.md) | 3 | `product: THOR, service: "TeamViewer password"` |
| [TestObject](docs/testobject.md) | 7 | `product: THOR, service: "TestObject"` |
| [USN entry](docs/usn-entry.md) | 4 | `product: THOR, service: "USN entry"` |
| [Unix permissions](docs/unix-permissions.md) | 4 | `product: THOR, service: "Unix permissions"` |
| [Windows permissions](docs/windows-permissions.md) | 3 | `product: THOR, service: "Windows permissions"` |
| [eBPF program](docs/ebpf-program.md) | 13 | `product: THOR, service: "eBPF program"` |
| [end of life report](docs/end-of-life-report.md) | 3 | `product: THOR, service: "end of life report"` |
| [environment variable](docs/environment-variable.md) | 3 | `product: THOR, service: "environment variable"` |
| [event](docs/event.md) | 2 | `product: THOR, service: "event"` |
| [hotfix summary](docs/hotfix-summary.md) | 2 | `product: THOR, service: "hotfix summary"` |
| [multiChoiceA](docs/multichoicea.md) | 2 | `product: THOR, service: "multiChoiceA"` |
| [quarantine event](docs/quarantine-event.md) | 6 | `product: THOR, service: "quarantine event"` |
| [reason](docs/reason.md) | 4 | `product: THOR, service: "reason"` |
| [registered debugger](docs/registered-debugger.md) | 3 | `product: THOR, service: "registered debugger"` |
| [rootkit](docs/rootkit.md) | 1 | `product: THOR, service: "rootkit"` |
| [shellbag entry](docs/shellbag-entry.md) | 4 | `product: THOR, service: "shellbag entry"` |
| [sparse data](docs/sparse-data.md) | 3 | `product: THOR, service: "sparse data"` |
| [structured data from plugin](docs/structured-data-from-plugin.md) | 3 | `product: THOR, service: "structured data from plugin"` |
| [system information](docs/system-information.md) | 12 | `product: THOR, service: "system information"` |

## Persistence & System

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [Linux kernel module](docs/linux-kernel-module.md) | 15 | `product: THOR, service: "Linux kernel module"` |
| [WMI element](docs/wmi-element.md) | 7 | `product: THOR, service: "WMI element"` |
| [WMI startup command](docs/wmi-startup-command.md) | 4 | `product: THOR, service: "WMI startup command"` |
| [Windows service](docs/windows-service.md) | 11 | `product: THOR, service: "Windows service"` |
| [at job](docs/at-job.md) | 2 | `product: THOR, service: "at job"` |
| [autorun entry](docs/autorun-entry.md) | 8 | `product: THOR, service: "autorun entry"` |
| [cron job](docs/cron-job.md) | 4 | `product: THOR, service: "cron job"` |
| [init.d service](docs/init.d-service.md) | 2 | `product: THOR, service: "init.d service"` |
| [registry scheduled task](docs/registry-scheduled-task.md) | 9 | `product: THOR, service: "registry scheduled task"` |
| [scheduled task](docs/scheduled-task.md) | 13 | `product: THOR, service: "scheduled task"` |
| [systemd service](docs/systemd-service.md) | 6 | `product: THOR, service: "systemd service"` |

## File System

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [MFT entry](docs/mft-entry.md) | 11 | `product: THOR, service: "MFT entry"` |
| [file](docs/file.md) | 19 | `product: THOR, service: "file"` |
| [file chunk](docs/file-chunk.md) | 5 | `product: THOR, service: "file chunk"` |
| [hosts file entry](docs/hosts-file-entry.md) | 3 | `product: THOR, service: "hosts file entry"` |
| [jump list entry](docs/jump-list-entry.md) | 11 | `product: THOR, service: "jump list entry"` |
| [prefetch info](docs/prefetch-info.md) | 5 | `product: THOR, service: "prefetch info"` |
| [shim cache](docs/shim-cache.md) | 3 | `product: THOR, service: "shim cache"` |
| [shim cache entry](docs/shim-cache-entry.md) | 4 | `product: THOR, service: "shim cache entry"` |
| [shim database entry](docs/shim-database-entry.md) | 2 | `product: THOR, service: "shim database entry"` |
| [user profile](docs/user-profile.md) | 4 | `product: THOR, service: "user profile"` |

## Security & Kernel

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [antivirus exclusion](docs/antivirus-exclusion.md) | 3 | `product: THOR, service: "antivirus exclusion"` |
| [antivirus product](docs/antivirus-product.md) | 5 | `product: THOR, service: "antivirus product"` |
| [mutex](docs/mutex.md) | 2 | `product: THOR, service: "mutex"` |
| [named pipe](docs/named-pipe.md) | 2 | `product: THOR, service: "named pipe"` |
| [pipe list](docs/pipe-list.md) | 2 | `product: THOR, service: "pipe list"` |

## Process & Memory

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [network connecting thread](docs/network-connecting-thread.md) | 5 | `product: THOR, service: "network connecting thread"` |
| [process](docs/process.md) | 16 | `product: THOR, service: "process"` |
| [process connection](docs/process-connection.md) | 7 | `product: THOR, service: "process connection"` |
| [process handle](docs/process-handle.md) | 4 | `product: THOR, service: "process handle"` |
| [process start](docs/process-start.md) | 3 | `product: THOR, service: "process start"` |
| [thread](docs/thread.md) | 3 | `product: THOR, service: "thread"` |

## Registry

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [registry key](docs/registry-key.md) | 4 | `product: THOR, service: "registry key"` |
| [registry value](docs/registry-value.md) | 5 | `product: THOR, service: "registry value"` |
