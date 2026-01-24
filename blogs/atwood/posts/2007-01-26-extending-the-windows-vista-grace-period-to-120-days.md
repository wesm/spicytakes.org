---
title: "Extending The Windows Vista Grace Period to 120 Days"
date: 2007-01-26
url: https://blog.codinghorror.com/extending-the-windows-vista-grace-period-to-120-days/
slug: extending-the-windows-vista-grace-period-to-120-days
word_count: 667
---

If you’re on the fence about the impending release of Windows Vista, I recommend trying before you buy. Every Vista DVD includes **the ability to install any edition of Vista without a product key.** When you install without a product key, you get an automatic 30 day evaluation period.* This probably isn’t news to anyone.


What may be news to you, however, is that **you can easily extend the 30-day Windows Vista grace period to 120 days.** No hacks required. This is an official, supported operation directly from Microsoft.


To extend the grace period another 30 days, simply start a command prompt as Administrator, and issue this command:

kg-card-begin: html

slmgr -rearm


kg-card-end: html
Reboot for the change to take effect, and voila, you have 30 more days. You can only extend three times, so the total grace period for a Vista evaluation is 120 days. You do, however, need to be careful that you’ve installed the correct edition of Vista. At the end of that 120 day grace period, you’ll have to **pony up a license fee for the edition of Vista you’ve installed**. Now that the OEM editions are out, the pricing breaks down like so, at least at Newegg:Vista Home Basic OEM - $100Vista Home Premium OEM - $120Vista Business OEM - $150Vista Ultimate OEM - $200Microsoft is semi-officially supporting the OEM versions for resale to end users, but the bad news is that there’s not much savings at the low-end. The pricing for the basic OEM editions are nearly identical to the full retail upgrades. The primary difference is that the OEM copies will support full install as well as upgrade install. If you’re looking for deeper Vista discounts, you may be interested in the Vista Family Pack, which includes the option to buy two $49 copies of Vista Home Premium, provided you pay full retail price for a copy of Vista Ultimate.Now that we’ve gotten the sticky matter of pricing out of the way, let’s take a deeper look at this little utility Microsoft provides. It’s actually a Windows Script Host file, slmgr.vbs. First, let’s **switch our default WSH handler to the command-line version** so we aren’t dealing with aggravating window popups from the command line.
kg-card-begin: html


cscript /H:Cscript


kg-card-end: html
If you run slmgr without any parameters, you’ll get the help.
kg-card-begin: html


Windows Software Licensing Management Tool
Usage: slmgr.vbs [MachineName [User Password]] [<Option>]
MachineName: Name of remote machine
User:        Account with required privilege
Password:    password for account
Global Options:
-ipk <Product Key>
Install product key (replaces existing key)
-upk
Uninstall product key
-ato
Activate Windows
-dli [Activation ID | All]
Display license information (default: current license)
-dlv [Activation ID | All]
Display detailed license information (default: current license)
-xpr
Expiration date for current license state
Advanced Options:
-cpky
Clear product key from the registry (prevents disclosure attacks)
-ilc <License file>
Install license
-rilc
Re-install system license files
-rearm
Reset the licensing status of the machine
-dti
Display Installation ID for offline activation
-atp <Confirmation ID>
Activate product with user-provided Confirmation ID


kg-card-end: html
I just re-armed tonight and re-booted, and I can verify that the grace period extension worked via the -dli command:
kg-card-begin: html


C:UsersJeff>slmgr -dli
Name: Windows(TM) Vista, Ultimate edition
Description: Windows Operating System - Vista, RETAIL channel
Partial Product Key: RP8F7
License Status: Initial grace period
Time remaining: 43100 minute(s) (29 day(s))


kg-card-end: html
This is my third and final grace period extension. I now have 29 days to decide if I want Ultimate edition or not.(update: Ed Bott posted how to set up a scheduled task so you [rearm automatically after 30 days](https://web.archive.org/web/20070303144944/http://blogs.zdnet.com/Bott/?p=224). I set mine up to run monthly for 3 months rather than setting up 3 individual tasks as Ed suggests.)*Note that this does *not* apply to the Enterprise edition of Vista, which only allows a 3 day grace period. The enterprise edition has an entirely different activation scheme; it uses a local volume license key server.

[windows](https://blog.codinghorror.com/tag/windows/)
[vista](https://blog.codinghorror.com/tag/vista/)
[operating system](https://blog.codinghorror.com/tag/operating-system/)
[activation](https://blog.codinghorror.com/tag/activation/)
[evaluation](https://blog.codinghorror.com/tag/evaluation/)
