---
title: "DCOM, XP SP2, and Remote Debugging"
date: 2004-08-12
url: https://blog.codinghorror.com/dcom-xp-sp2-and-remote-debugging/
slug: dcom-xp-sp2-and-remote-debugging
word_count: 530
---

I debug remotely at home, mostly because I prefer not using the crippleware version of IIS. It's kind of a pain to get it running, because you have to be more careful with permissions and configuration, but basically it works. At least, it worked until I installed XP SP2, anyway. There's a decent [set of documentation](https://web.archive.org/web/20040603140138/http://msdn.microsoft.com/security/productinfo/xpsp2/default.aspx?pull=%2Flibrary%2Fen-us%2Fdnwxp%2Fhtml%2Fxpsp2remotedebug.asp) on how to get Remote Debugging working under SP2, but I could not get it to work – and I have the XP firewall completely disabled! Over and over, any attempt to remotely debug an ASP.NET app resulted in this exciting dialog box message:


> **Error while trying to run project: Unable to start debugging on the web server. Access is denied.**


I ran through all the usual troubleshooting, and then some:

- I have the same account/password on both client and server
- the website is using NTLM authentication
- there is an IIS application for the website
- I am a member of the Administrators and Debugger Users group on both boxes.
- the website loads fine if I run with CTRL+F5, e.g., no debugger
- The security event log shows me logging in just fine on the server
- Remote Debugging support is properly installed on the server


After three hours of intense frustration, I started to feel like that Doom3 zombie – the one mindlessly pounding his head against a bloody wall over and over. Eventually you get to that desperate point where you'll try anything, no matter how crazy. Sometimes this pays off, and sometimes it doesn't. Luckily this is one of those times where the headbanging paid off. **I finally got remote debugging to work with XP SP2 by granting “Remote Access” to the ANONYMOUS LOGON account in dcomcnfg.exe on the client computer**. Specifically, in:


> dcomcnfg.exe -> Component Services -> Computers -> My Computer -> Properties -> COM Security -> Access Permissions -> Edit Limits.


Now, the documentation does mention setting stuff in Edit Limits, but it says you have to add *your *account in there, and only if you're *not *an administrator. That doesn't even make sense; out of the box EVERYONE is granted both local and remote permissions in Edit Limits. Granting remote access to ANONYMOUS LOGON is what you have to do. Why, I have no idea, but it is totally repeatable across three computers here, including my otherwise unmodified laptop. There are  plenty of people in Google groups [complaining about this problem](http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&q=remote+debugging+on+the+web+server+%22Access+is+denied%22&ref=blog.codinghorror.com), so hopefully this will help someone.


Oh, and by the way, be careful: this is also a great way to trash your machine. I strongly suggest you only grant additional permissions in dcomcnfg; do not remove any permissions. In the process of testing this – ironically, after I finally got it working, and in order to ensure that I understood the failure conditions – **I inadvertently removed all permissions from the Edit Limits box. Friends, do not do this.** Two in-place reinstalls later (one reinstall to get COM permissions back, another one to re-install the COM stuff that failed to install with the borked permissions), I had a functioning OS again. Revenge of COM...

[debugging](https://blog.codinghorror.com/tag/debugging/)
[dcom](https://blog.codinghorror.com/tag/dcom/)
[remote debugging](https://blog.codinghorror.com/tag/remote-debugging/)
[xp sp2](https://blog.codinghorror.com/tag/xp-sp2/)
[iis](https://blog.codinghorror.com/tag/iis/)
