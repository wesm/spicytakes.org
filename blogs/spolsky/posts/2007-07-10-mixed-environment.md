---
title: "Mixed environment"
date: 2007-07-10
url: https://www.joelonsoftware.com/2007/07/10/mixed-environment/
word_count: 236
---


Mike P. asks:


> “On your [recent post](https://www.joelonsoftware.com/items/2007/07/09.html) you mention that FogBugz is now going to be hosted and that you hired a sysadmin who converted your systems from NetBSD to Linux. Then you go on to say that you bought a Dell server, W2K3 and W2K5 SQL Server. I don’t understand. Are you or are you not runing FBOD with the LAMP stack?”


I was not very clear. We have a lot of servers. Some of them were running NetBSD, and are now running Linux. Others are running Windows Server 2003. The Linux servers tend to be used for routers and assorted network services like DNS. The Windows servers are either working as web front ends (IIS) or database back ends (MS SQL 2005).


[FogBugz On Demand](http://www.fogcreek.com/fogbugz) is, indeed, on the Windows servers. We try very hard to stick to a single hardware architecture so any server can be swapped with any other in case of problems, and parts can be moved hither and yon as needed. We weren’t really able to do this perfectly because Dell switched from SCSI to SAS hard drives when they went from the 8th generation to the 9th generation servers, but mostly we use a common platform so it’s easy to keep spare parts on hand. (In fact, one backup server even has an extra NIC in it so it can replace the router if it comes to that).
