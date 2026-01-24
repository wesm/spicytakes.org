---
title: "VNC vs. Remote Desktop"
date: 2005-07-11
url: https://blog.codinghorror.com/vnc-vs-remote-desktop/
slug: vnc-vs-remote-desktop
word_count: 607
---

Microsoft’s [Remote Desktop](http://en.wikipedia.org/wiki/Remote_Desktop_Protocol) is incredibly convenient. It’s the next best thing to physically being in front of the target computer – and it’s by far the fastest remoting protocol I’ve ever used. Over a fast network, you can *almost* convince yourself that you’re using the local machine. Remote desktop is great stuff, and it’s basically free. It does have a few annoying limitations, though:

1. it insists on treating every remote login as a **separate user session**. Except in the special case where you log into your own session.
2. it **can’t handle multiple monitors** in any way; you’ll only see the primary monitor. Fortunately, [UltraMon](http://www.realtimesoft.com/ultramon/) has a convenient one-click taskbar enable/disable function for the alternate monitors. It even remembers the position of windows when moving them back.
3. in fine Microsoft tradition, **it’s intentionally crippled**. You can only have one active Remote Desktop session under XP, and two sessions under Windows 2003/2000 server. I suppose this is to keep us from setting up our own OS/360 timeshare boxes.


Point #1 is in stark contrast to “old school” remoting programs such as pcAnywhere and Carbon Copy, which simply **displayed whatever happened to be on the client’s screen –** sort of like virtual video adapters. Sometimes, this is what you want. And in those situations, [you want TightVNC](http://www.tightvnc.com/). VNC follows the older model of simply showing whatever is on the screen with no forced logins required. Of course, this has security implications; if you remote into a machine that an Administrator is logged into, you’ll effectively be an Administrator. And if you’re both trying to use the computer at the same time, it’s even more fun!


VNC has been around for years in various incarnations; what makes TightVNC so useful is that it’s free, natch, but more importantly, **it implements a video hook driver**. One of the long-running historical weaknesses of the VNC protocol was that it didn’t interface at the video driver level with Windows; it had to poll for screen changes. This works, and it’s a very cross-platform approach, but it’s also hellaciously inefficient and highly CPU intensive. Why poll for changes when the video driver can tell you what the changes were? When you [download TightVNC](http://www.tightvnc.com/download.html), be sure to download the “developmental” version (at the time of writing, 1.3d7) and the dfrimage.zip video hook driver.


Even with this hook driver, it isn’t as fast as Remote Desktop, but it’s at least in the ballpark. If you ever used VNC in the past and were disappointed with how slow and CPU intensive it was, you should try again with TightVNC and the video hook driver. There’s a world of difference.


If you’re feeling really adventurous, there’s even an [open-source C# VNC client](http://dnvnccl.sourceforge.net/). TightVNC implements a few specially optimized protocols of its own, but it does support the “classic” VNC protocols as well. I was able to remote into a TightVNC server using this C# client.


Unfortunately, neither Remote Desktop nor VNC does a good job of handling multiple monitors on the target machine, so that’s a wash. You’ll get the primary monitor, and you’ll like it. There is some support for multimon in the latest versions of pcAnywhere, as [this review at RealTimeSoft](https://web.archive.org/web/20051026151608/http://www.realtimesoft.com/multimon/reviews/pcanywhere/) points out.


Note that a few key sequences, such as CTRL+ALT+DEL, can’t be intercepted by any remote desktop client, even in full screen mode. There’s a handy list of keyboard shortcuts for the Remote Desktop key equivalents in [the online XP resource kit.](https://web.archive.org/web/20060615143017/http://www.microsoft.com/technet/prodtechnol/winxppro/reskit/default.mspx)


Incidentally, there are [hardware-level remote desktop solutions](https://web.archive.org/web/20050724001023/http://www.kvmpartnership.co.uk/eric.htm) which are capable of remotely displaying BIOS setup screens – even the Blue Screen o’ Death! Pretty gnarly stuff.

[remote desktop](https://blog.codinghorror.com/tag/remote-desktop/)
[vnc](https://blog.codinghorror.com/tag/vnc/)
[networking](https://blog.codinghorror.com/tag/networking/)
