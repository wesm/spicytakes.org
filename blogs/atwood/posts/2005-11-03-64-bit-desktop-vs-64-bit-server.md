---
title: "64-bit Desktop vs. 64-bit Server"
date: 2005-11-03
url: https://blog.codinghorror.com/64-bit-desktop-vs-64-bit-server/
slug: 64-bit-desktop-vs-64-bit-server
word_count: 437
---

When people find out I’m a big fan of AMD’s Athlon 64 – specifically [the dual core X2 chips](https://blog.codinghorror.com/multiple-core-cpu-futures/) – they often ask how I’m enjoying 64-bit Windows. They’re always surprised to hear that **I have no interest in a 64-bit OS on the desktop**. I’m glad someone is laying the foundation for the next 10 years of computing. But as Tom’s hardware points out, there’s little to gain from running a 64-bit version of Windows XP [on the desktop today](https://web.archive.org/web/20051028091413/http://www.tomshardware.com/howto/20050823/winxp_x64-08.html):

kg-card-begin: html

> After collecting all the benchmark results in both the 32 bit and 64 bit Windows environments, here is what we found:
> The 64 bit version of Windows looks and feels pretty much like the popular 32 bit versions.
> Windows XP Professional x64 Edition provides performance comparable to Windows XP 32 bit when running 32 bit applications.
> Some programs run slightly faster, others slightly slower. At the end of the day, the difference is not noticeable.
> The perceived differences between the 32 bit and 64 bit versions are the same whether you run a single or a dual core processor.

kg-card-end: html

In the absence of any measurable performance improvement for typical desktop apps, why in the world would you want to be a guinea pig for 64-bit driver and OS teething problems? Answer: you wouldn’t.


**On the server, however, a 64-bit OS is a completely different story. **The [Microsoft.com operations blog](https://web.archive.org/web/20051122204202/http://blogs.technet.com/mscom/default.aspx) documents the massive performance improvement they realized when they switched to the 64-bit edition of Windows Server 2003:

kg-card-begin: html

```

req/sec  response time
X86 ASP               7.85  244 ms
X86 ISAPI           110.85  248 ms
X86 Static           41.90  135 ms
X86 Static (cached)  47.11    1 ms
X64 ASP               7.41   53 ms
X64 ISAPI           125.43   18 ms
X64 Static           31.01    3 ms
X64 Static (cached)  54.51    1 ms

```

kg-card-end: html

That’s just a small part of the performance story documented in [the full blog entry](https://web.archive.org/web/20051106014717/http://blogs.technet.com/mscom/archive/2005/09/26/411568.aspx). And these numbers alone are incredible, particularly considering this is a drop-in replacement with existing, unchanged 32-bit code. **It’s literally free performance!** If you’re running a web server of any significant load on a 32-bit server OS, I would run, not walk, to the nearest software store to grab a Windows Server 2003 x64 license.


The MS ops blog doesn’t get enough juice. And that’s too bad, because it’s full of practical, holistic tips based on running the fourth largest website in the world and thousands of servers. For example, their [logparser](https://web.archive.org/web/20051105084927/http://blogs.technet.com/mscom/archive/2005/10/19/412745.aspx) post is about ten times more useful than [mine](https://blog.codinghorror.com/microsoft-logparser/) ever was.

[operating system](https://blog.codinghorror.com/tag/operating-system/)
[windows xp](https://blog.codinghorror.com/tag/windows-xp/)
[64-bit](https://blog.codinghorror.com/tag/64-bit/)
[desktop vs. server](https://blog.codinghorror.com/tag/desktop-vs-server/)
[amd athlon 64](https://blog.codinghorror.com/tag/amd-athlon-64/)
