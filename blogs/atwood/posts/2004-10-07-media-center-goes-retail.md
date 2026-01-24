---
title: "Media Center goes retail"
date: 2004-10-07
url: https://blog.codinghorror.com/media-center-goes-retail/
slug: media-center-goes-retail
word_count: 788
---

I had no idea this was happening, but it is fantastic news: according to this GamePC article, the latest 2005 version of Windows XP Media Center Edition will be released as a **retail product** within a few weeks:


> *Windows XP Media Center Edition was originally launched roughly two years ago, and was the first variant of XP designed to be run on home theater systems and to be controlled via remote. The OS itself was based upon Windows XP core, but ran Microsoft’s Media Center application on top of the operating system, which was custom built to playback and record TV, movies, music, and videos. Since Microsoft was in complete control of the OS, the application, and the remote control hardware which was used, XP Media Center Edition had a higher level of integration and smoothness compared to other media center type applications.
> Unfortunately, Microsoft’s demanding control is what has held back this operating system for so long. XP Media Center Edition was never available as a retail product, nor was it available for end users to purchase directly from OEM’s. The only way you could get XP Media Center Edition was to purchase a full PC with the operating system pre-loaded. Given the enthusiast-nature of the HTPC community, many balked at the thought of having to purchase an entire new PC just to get a copy of this operating system. Thus, an entire crop of home-brewed media center applications has sprung up with excellent products such as SageTV and Meedio, which can perform many of Media Center Edition’s core functions on any PC. Even more threatening to Microsoft is that many HTPC users are switching over to Linux to meet their needs, as superb free software products like Freevo and MythTV have gained quite a following.
> While these applications have worked quite well thus far, if given the choice, many would simply go with an easier to use Microsoft solution. Fortunately, Microsoft finally listened, and are opening up Windows XP Media Center Edition for everyone. Their latest version, Media Center Edition 2005, is now selling on the open markets, and is available to all. While the OS itself is not officially launching for another week, we were able to get our hands on this final product to give everyone a first hand glimpse of how Media Center Edition 2005 (Codenamed Symphony) works in an uncontrolled environment.*


This rectifies a great wrong; the prior two editions of MCE were excellent mainstream products stymied into a tiny niche because *nobody could get a copy!* That is, unless you had a MSDN sub, or you were an OEM.


I’m something of an expert on HTPC related topics; I’m a long time Tivo user with modded Series 1 and Series 2 boxes, and I built up a specialized home theater PC box for MCE soon after that was released... with 480gb of storage. In short, I’m a giant dork – but you knew that already. The best source of information on MCE topics is [The Green Button](https://web.archive.org/web/20041014083337/http://www.thegreenbutton.com/), so check there if you want to go in depth.


Even if you have no interest in, uh, media, MCE is still interesting from a programming perspective. **Did you know that MCE was one of the first commercial products from MS developed entirely in .NET?** It’s a fanatastic proof of concept, and certainly does tons of hard-core interop for the DirectX Avalon style interfaces, hardware MPEG2 encoders, and media playback. And it works! Well, the initial version was a little rough around the corners, but the 2004 version works pretty darn well.


MCE also offers insight into another type of UI design. Putting together a usable **“10 foot interface”** is radically different from all my other GUI design experience. It’s not easy to do, and although MCE is by far one of the best HTPC apps you’ll find, Tivo still has a clearly superior UI. If you dig around on the Green Button programming forums ([thread with screenshot](https://web.archive.org/web/20041010041108/http://www.thegreenbutton.com/community/shwmessage.aspx?ForumID=30&MessageID=31768&TopicPage=3)), you’ll find links to a sample VS.NET 2003 project I created containing WinForms user controls in the style of MCE. This was dishearteningly difficult to do. I spent about two weeks hacking alphablended user controls into WinForms and I made some decent progress, but I reached one inevitable conclusion: **you really have to bite the bullet and develop against DirectX if you want something that looks like MCE and performs at a decent speed.**


MCE’s interface is very cool, though. If this is anything like what we’ll get with Avalon, it will be impressive indeed. And, really, what other logical use is there for 300gb+ hard drives, other than to fill them with video?

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
