---
title: "Remotely Managing Remote Desktop"
date: 2005-02-25
url: https://blog.codinghorror.com/remotely-managing-remote-desktop/
slug: remotely-managing-remote-desktop
word_count: 256
---

Some of my coworkers have an annoying habit of remoting into our Win2k servers and never logging out. They also like to do this in pairs, which means nobody else can remote into the machines due to Microsoft’s default [two-user administrative mode](https://web.archive.org/web/20050303011114/http://www.microsoft.com/windows2000/techinfo/administration/terminal/tsremote.asp) Terminal Services limit. Yeah, I could rclient in, or use remote MMC snap-ins, but sometimes it’s just faster to manipulate the GUI via Remote Desktop.


There’s a tool to remotely manage remote desktop connections in Win2k, but I couldn’t find any equivalent in XP. A little searching turned up Microsoft’s Windows Server [2003 Administration Tools Pack](https://web.archive.org/web/20051206073803/http://www.microsoft.com/downloads/details.aspx?FamilyID=c16ae515-c8f4-47ef-a1e4-a8dcbacff8e3&displaylang=en) which *provides server management tools that allow administrators to remotely manage Windows 2000 Servers & Windows Server 2003 family servers*. And indeed it does!


The kit installs the following tools, which appear under the Start, Programs, Administrative Tools menu:

- Active Directory Domains and Trusts
- Active Directory Management
- Active Directory Sites and Services
- Active Directory Users and Computers
- Authorization Manager
- Cluster Administrator
- Connection Manager Administration Kit
- DHCP
- Distributed File System
- DNS
- IP Address Management
- Network Load Balancing Manager
- Public Key Management
- Remote Desktops
- Remote Storage
- Telephony
- Terminal Server Licensing
- Terminal Services Manager
- UDDI Services
- WINS


All this for the low, low price of nothing. The only part I care about is the **Terminal** **Services Manager**, which lets me terminate idle remote desktop sessions from target servers. Take that coworkers!

[remote desktop](https://blog.codinghorror.com/tag/remote-desktop/)
[windows server](https://blog.codinghorror.com/tag/windows-server/)
[administrative tools](https://blog.codinghorror.com/tag/administrative-tools/)
[terminal services](https://blog.codinghorror.com/tag/terminal-services/)
[remote management](https://blog.codinghorror.com/tag/remote-management/)
