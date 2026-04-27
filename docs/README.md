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
| [AIX platform information](aix-platform-information.md) | 9 | `product: THOR, service: "AIX platform information"` |
| [Linux platform information](linux-platform-information.md) | 6 | `product: THOR, service: "Linux platform information"` |
| [MacOS platform information](macos-platform-information.md) | 7 | `product: THOR, service: "MacOS platform information"` |
| [Windows platform information](windows-platform-information.md) | 8 | `product: THOR, service: "Windows platform information"` |

## Execution History

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [AmCache entry](amcache-entry.md) | 9 | `product: THOR, service: "AmCache entry"` |
| [web download](web-download.md) | 4 | `product: THOR, service: "web download"` |
| [web page visit](web-page-visit.md) | 4 | `product: THOR, service: "web page visit"` |

## Network

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [DNS cache entry](dns-cache-entry.md) | 3 | `product: THOR, service: "DNS cache entry"` |
| [MS Office connection cache entry](ms-office-connection-cache-entry.md) | 4 | `product: THOR, service: "MS Office connection cache entry"` |
| [firewall rule](firewall-rule.md) | 11 | `product: THOR, service: "firewall rule"` |
| [network session](network-session.md) | 7 | `product: THOR, service: "network session"` |
| [network share](network-share.md) | 4 | `product: THOR, service: "network share"` |
| [raw firewall rule](raw-firewall-rule.md) | 2 | `product: THOR, service: "raw firewall rule"` |

## Logs & Events

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [DetectionAdd MPLog entry](detectionadd-mplog-entry.md) | 4 | `product: THOR, service: "DetectionAdd MPLog entry"` |
| [EMS detection MPLog entry](ems-detection-mplog-entry.md) | 4 | `product: THOR, service: "EMS detection MPLog entry"` |
| [EstimatedImpact MPLog entry](estimatedimpact-mplog-entry.md) | 5 | `product: THOR, service: "EstimatedImpact MPLog entry"` |
| [SDN query MPLog entry](sdn-query-mplog-entry.md) | 5 | `product: THOR, service: "SDN query MPLog entry"` |
| [audit log entry](audit-log-entry.md) | 2 | `product: THOR, service: "audit log entry"` |
| [eventlog entry](eventlog-entry.md) | 2 | `product: THOR, service: "eventlog entry"` |
| [journal log entry](journal-log-entry.md) | 3 | `product: THOR, service: "journal log entry"` |
| [log line](log-line.md) | 3 | `product: THOR, service: "log line"` |

## Identity & Auth

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [DoublePulsar Handshake](doublepulsar-handshake.md) | 3 | `product: THOR, service: "DoublePulsar Handshake"` |
| [LSA session](lsa-session.md) | 8 | `product: THOR, service: "LSA session"` |
| [Tomcat user](tomcat-user.md) | 2 | `product: THOR, service: "Tomcat user"` |
| [Unix user](unix-user.md) | 9 | `product: THOR, service: "Unix user"` |
| [User Access Log Entry](user-access-log-entry.md) | 12 | `product: THOR, service: "User Access Log Entry"` |
| [Windows user](windows-user.md) | 12 | `product: THOR, service: "Windows user"` |
| [authorized_keys entry](authorized_keys-entry.md) | 5 | `product: THOR, service: "authorized_keys entry"` |
| [groups.xml user](groups.xml-user.md) | 3 | `product: THOR, service: "groups.xml user"` |
| [logged in user](logged-in-user.md) | 5 | `product: THOR, service: "logged in user"` |

## Other

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [KnowledgeDB entry](knowledgedb-entry.md) | 6 | `product: THOR, service: "KnowledgeDB entry"` |
| [PowerShell module analysis cache module entry](powershell-module-analysis-cache-module-entry.md) | 3 | `product: THOR, service: "PowerShell module analysis cache module entry"` |
| [SRUM Resource Usage Entry](srum-resource-usage-entry.md) | 14 | `product: THOR, service: "SRUM Resource Usage Entry"` |
| [THOR assessment](thor-assessment.md) | 10 | `product: THOR, service: "THOR assessment"` |
| [THOR invocation information](thor-invocation-information.md) | 17 | `product: THOR, service: "THOR invocation information"` |
| [THOR message](thor-message.md) | 5 | `product: THOR, service: "THOR message"` |
| [TeamViewer password](teamviewer-password.md) | 3 | `product: THOR, service: "TeamViewer password"` |
| [TestObject](testobject.md) | 7 | `product: THOR, service: "TestObject"` |
| [USN entry](usn-entry.md) | 4 | `product: THOR, service: "USN entry"` |
| [Unix permissions](unix-permissions.md) | 4 | `product: THOR, service: "Unix permissions"` |
| [Windows permissions](windows-permissions.md) | 3 | `product: THOR, service: "Windows permissions"` |
| [eBPF program](ebpf-program.md) | 13 | `product: THOR, service: "eBPF program"` |
| [end of life report](end-of-life-report.md) | 3 | `product: THOR, service: "end of life report"` |
| [environment variable](environment-variable.md) | 3 | `product: THOR, service: "environment variable"` |
| [event](event.md) | 2 | `product: THOR, service: "event"` |
| [hotfix summary](hotfix-summary.md) | 2 | `product: THOR, service: "hotfix summary"` |
| [multiChoiceA](multichoicea.md) | 2 | `product: THOR, service: "multiChoiceA"` |
| [quarantine event](quarantine-event.md) | 6 | `product: THOR, service: "quarantine event"` |
| [reason](reason.md) | 4 | `product: THOR, service: "reason"` |
| [registered debugger](registered-debugger.md) | 3 | `product: THOR, service: "registered debugger"` |
| [rootkit](rootkit.md) | 1 | `product: THOR, service: "rootkit"` |
| [shellbag entry](shellbag-entry.md) | 4 | `product: THOR, service: "shellbag entry"` |
| [sparse data](sparse-data.md) | 3 | `product: THOR, service: "sparse data"` |
| [structured data from plugin](structured-data-from-plugin.md) | 3 | `product: THOR, service: "structured data from plugin"` |
| [system information](system-information.md) | 12 | `product: THOR, service: "system information"` |

## Persistence & System

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [Linux kernel module](linux-kernel-module.md) | 15 | `product: THOR, service: "Linux kernel module"` |
| [WMI element](wmi-element.md) | 7 | `product: THOR, service: "WMI element"` |
| [WMI startup command](wmi-startup-command.md) | 4 | `product: THOR, service: "WMI startup command"` |
| [Windows service](windows-service.md) | 11 | `product: THOR, service: "Windows service"` |
| [at job](at-job.md) | 2 | `product: THOR, service: "at job"` |
| [autorun entry](autorun-entry.md) | 8 | `product: THOR, service: "autorun entry"` |
| [cron job](cron-job.md) | 4 | `product: THOR, service: "cron job"` |
| [init.d service](init.d-service.md) | 2 | `product: THOR, service: "init.d service"` |
| [registry scheduled task](registry-scheduled-task.md) | 9 | `product: THOR, service: "registry scheduled task"` |
| [scheduled task](scheduled-task.md) | 13 | `product: THOR, service: "scheduled task"` |
| [systemd service](systemd-service.md) | 6 | `product: THOR, service: "systemd service"` |

## File System

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [MFT entry](mft-entry.md) | 11 | `product: THOR, service: "MFT entry"` |
| [file](file.md) | 19 | `product: THOR, service: "file"` |
| [file chunk](file-chunk.md) | 5 | `product: THOR, service: "file chunk"` |
| [hosts file entry](hosts-file-entry.md) | 3 | `product: THOR, service: "hosts file entry"` |
| [jump list entry](jump-list-entry.md) | 11 | `product: THOR, service: "jump list entry"` |
| [prefetch info](prefetch-info.md) | 5 | `product: THOR, service: "prefetch info"` |
| [shim cache](shim-cache.md) | 3 | `product: THOR, service: "shim cache"` |
| [shim cache entry](shim-cache-entry.md) | 4 | `product: THOR, service: "shim cache entry"` |
| [shim database entry](shim-database-entry.md) | 2 | `product: THOR, service: "shim database entry"` |
| [user profile](user-profile.md) | 4 | `product: THOR, service: "user profile"` |

## Security & Kernel

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [antivirus exclusion](antivirus-exclusion.md) | 3 | `product: THOR, service: "antivirus exclusion"` |
| [antivirus product](antivirus-product.md) | 5 | `product: THOR, service: "antivirus product"` |
| [mutex](mutex.md) | 2 | `product: THOR, service: "mutex"` |
| [named pipe](named-pipe.md) | 2 | `product: THOR, service: "named pipe"` |
| [pipe list](pipe-list.md) | 2 | `product: THOR, service: "pipe list"` |

## Process & Memory

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [network connecting thread](network-connecting-thread.md) | 5 | `product: THOR, service: "network connecting thread"` |
| [process](process.md) | 16 | `product: THOR, service: "process"` |
| [process connection](process-connection.md) | 7 | `product: THOR, service: "process connection"` |
| [process handle](process-handle.md) | 4 | `product: THOR, service: "process handle"` |
| [process start](process-start.md) | 3 | `product: THOR, service: "process start"` |
| [thread](thread.md) | 3 | `product: THOR, service: "thread"` |

## Registry

| Object Type | Fields | Sigma Service |
|-------------|--------|---------------|
| [registry key](registry-key.md) | 4 | `product: THOR, service: "registry key"` |
| [registry value](registry-value.md) | 5 | `product: THOR, service: "registry value"` |
