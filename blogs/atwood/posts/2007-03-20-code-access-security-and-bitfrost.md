---
title: "Code Access Security and Bitfrost"
date: 2007-03-20
url: https://blog.codinghorror.com/code-access-security-and-bitfrost/
slug: code-access-security-and-bitfrost
word_count: 735
---

The [One Laptop Per Child](http://www.laptop.org/) operating system features a new security model – [Bitfrost](http://wiki.laptop.org/go/OLPC_Bitfrost). It’s an interesting departure from the traditional UNIX and LINUX security model.

kg-card-begin: html

> The 1971 version of UNIX supported the following security permissions on user files:
> non-owner can change file (write)
> non-owner can read file
> owner can change file (write)
> owner can read file
> file can be executed
> file is set-uid
> These permissions should look familiar, because they are very close to the same security permissions a user can set for her files today, in her operating system of choice. What’s deeply troubling – almost unbelievable – about these permissions is that they’ve remained virtually the only real control mechanism that a user has over her personal documents today: a user can choose to protect her files from other people on the system, but has no control whatsoever over what her own programs are able to do with her files.
> In 1971, this might have been acceptable: it was 20 years before the advent of the Web, and the threat model for most computer users was entirely different than the one that applies today. But how, then, is it a surprise that we can’t stop viruses and malware now, when our defenses have remained largely unchanged from thirty-five years ago?

kg-card-end: html

BitFrost intends to address this problem by **adding a new level of permissions that applies to code**, not users: code access security.

kg-card-begin: html

> Consider the Solitaire game shipped with most versions of Microsoft Windows. This program needs:
> no network access whatsoever
> no ability to read the user’s documents
> no ability to utilize the built-in camera or microphone
> no ability to look at, or modify, other programs
> Yet if somehow compromised by an attacker, Solitaire is free to do whatever the attacker wishes, including:
> read, corrupt or delete the user’s documents, spreadsheets, music, photos and any other files
> eavesdrop on the user via the camera or microphone
> replace the user’s wallpaper
> access the user’s website passwords
> infect other programs on the hard drive with a virus
> download files to the user’s machine
> receive or send e-mail on behalf of the user
> play loud or embarassing sounds on the speakers
> The critical observation here is not that Solitaire should never have the ability to do any of the above (which it clearly shouldn’t), but that its creators know it should never do any of the above. If the system implemented a facility for Solitaire to indicate this at installation time, Solitaire could irreversibly shed various privileges the moment it’s installed. This severely limits or destroys its usefulness to an attacker were it taken over.

kg-card-end: html

If I sound skeptical, that’s because BitFrost sounds suspiciously similar to .NET framework code access security, as outlined in the  [`System.Security.Permissions`](http://msdn2.microsoft.com/en-us/library/system.security.permissions.aspx) namespace. It’s an enormous, complex list of explicit permissions you can grant or deny in your application’s install manifest, exactly as described in the Solitaire example above. It sounds great in theory: establish a limited set of permissions your application needs up front, and let the .NET runtime worry about enforcing those permissions while your application is running.


But in practice, very few .NET developers make use of code access security. It appears Microsoft noticed that, too:


> It seems Microsoft does not understand why nobody uses Code Access Security. In fact, Microsoft has [a survey on the Internet](https://web.archive.org/web/20091219204923/http://blogs.msdn.com/brada/archive/2005/03/06/386172.aspx). You can go ahead and answer the survey but if you have followed this entry, you should know what I am getting at: **Code Access Security is too hard**. Don’t get me wrong, I think Code Access Security is great. In particular, the stack walk mechanism is terrific. But the policy side is way too hard for most people.


The CAS model was so profoundly unsuccessful in .NET 1.0 and 1.1 that ClickOnce in .NET 2.0 effectively does away with CAS. You’re now exactly one click away from running a full trust application that can do whatever it wants to on your machine, with no restrictions of any kind.


Perhaps the OLPC’s BitFrost model will fare better than .NET Code Access Security did. But somehow I doubt it. **What good is a security model that’s so cumbersome to use, nobody ever adopts it?**

[security](https://blog.codinghorror.com/tag/security/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
