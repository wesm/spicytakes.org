---
title: "Let’s stop talking about “backups”"
date: 2009-12-14
url: https://www.joelonsoftware.com/2009/12/14/lets-stop-talking-about-backups/
word_count: 262
---


Is your desktop backed up?


Did you backup that server?


Are your backups on a different machine?


Do you have offsite backups?


All good questions, all best practices.


But let’s stop talking about “backups.” Doing a backup is too low a bar. Any experienced system administrator will tell you that they have a great backup plan, the trouble comes when you have to *restore*.


And that’s when you discover that:

- The backed-up files were encrypted with a cryptographically-secure key, the only copy of which was on the machine that was lost
- The server had enormous amounts of configuration information stored in the IIS metabase which wasn’t backed up
- The backup files were being copied to a FAT partition and were silently being truncated to 2GB
- Your backups were on an LTO drive which was lost with the data center, and you can’t get another LTO drive for three days
- And a million other things that can go wrong even when you “have” “backups.”


The minimum bar for a reliable service is not that you have done a backup, but that you have done a *restore*. If you’re running a web service, you need to be able to show me that you can build a reasonably recent copy of the entire site, in a reasonable amount of time, on a new server or servers without ever accessing anything that was in the original data center. The bar is that you’ve done a *restore*.


Let’s stop asking people if they’re doing backups, and start asking if they’re doing restores.
