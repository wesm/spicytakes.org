---
title: "Microsoft Doesn’t Trust .NET"
date: 2006-03-17
url: https://blog.codinghorror.com/microsoft-doesnt-trust-net/
slug: microsoft-doesnt-trust-net
word_count: 363
---

Richard Grimes recently posted an Analysis of .NET Use in Longhorn and Vista, wherein he draws two conclusions:

1. Between PDC 2003 and the release of Vista Beta 1, Microsoft has decided that it is better to use native code for the operating system
2. **Microsoft has shown no intention so far to use .NET on a large scale on XP** or the server versions of Windows, neither in the operating system, nor in their major revenue generating applications.


I agree with the first point. If you’re writing an OS, you need to get down to the metal. Managed code trades off CPU cycles for protection from buffer overruns and other C++ nastiness, but I’d rather spend those CPU cycles on [virtualization to protect myself](https://blog.codinghorror.com/our-virtual-machine-future/). That said, there is [Microsoft’s Singularity project](http://research.microsoft.com/os/singularity/), which is an OS written entirely in managed code.


But the second point is *just plain wrong*. The **Windows XP Media Center Edition functionality was, and is, written in .NET!** Just ask [Joel Belfiore](https://web.archive.org/web/20060408213759/http://www.winsupersite.com/showcase/freestyle_joeb.asp):


> *From a technical standpoint, Media Center user interface functionality is almost entirely written in C# managed code, on top of native Win32 and DirectX Windows XP components. These operating system components render video and draw fluid animations smoothly on the screen at 60 frames per second, with hardware acceleration and MPEG decoding provided by 3rd parties. Getting all these technology components to work together well was our biggest challenge.*


Windows XP Media Center Edition happens to be one of the fastest selling versions of Windows at the moment:


> *Sales of Media Center have reached the 6.5 million mark in just three years.*


MCE is a superset of Pro, in that it is based on Pro (it has IIS, etc.) but with added MCE functionality. Now check out the newegg.com Windows pricing:


XP Pro : $139.95
XP MCE : $114.95


So you’re getting *more* functionality for *less* money. Hmm. I wonder which version of Windows is going to sell faster?


I would say the 6.5 million sales of XP MCE to date clearly indicates “[Microsoft’s] intention to use .NET on a large scale on XP,” wouldn't you?

[.net](https://blog.codinghorror.com/tag/net/)
[microsoft](https://blog.codinghorror.com/tag/microsoft/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
