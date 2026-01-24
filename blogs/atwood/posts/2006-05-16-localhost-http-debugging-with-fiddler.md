---
title: "Localhost HTTP Debugging with Fiddler"
date: 2006-05-16
url: https://blog.codinghorror.com/localhost-http-debugging-with-fiddler/
slug: localhost-http-debugging-with-fiddler
word_count: 227
---

I’ve had great success using ethernet sniffers (such as [Etherdetect](http://www.etherdetect.com/), or [Ethereal](https://web.archive.org/web/20060516094008/http://www.ethereal.com/)) to troubleshoot communication problems. Installing a sniffer, even after installing the [required WinPcap packet capture library](http://www.winpcap.org/install/default.htm), doesn’t require a reboot. I frequently use sniffers to troubleshoot servers and desktops alike. Ethernet sniffers should be a standard tool in your development troubleshooting toolkit, too.


However, Windows ethernet sniffers do have one significant limitation: **they can’t sniff localhost traffic**. Localhost packets don’t pass through the regular network stack, so they’re invisible to an ethernet sniffer.


What’s a poor developer to do? The only recourse is a **local HTTP proxy**, such as [Fiddler](https://web.archive.org/web/20060527004620/http://www.fiddlertool.com/fiddler/):


![](https://blog.codinghorror.com/content/images/2025/05/image-283.png)


Fiddler has some special integration with IE that makes it particularly easy to use, but it can be [used with Firefox as well](http://west-wind.com/weblog/posts/4085.aspx).


I had some erratic results under IE7, but Fiddler basically works as advertised. There’s tons of supporting documentation on how to use it, including two MSDN articles. I’m using Fiddler as a localhost sniffer that’s limited to the HTTP protocol, but it does have some capabilities beyond what you’d see in a sniffer. For example, with Fiddler **you can set breakpoints and tamper with the HTTP data before it is sent or received**.


On the whole, I’d prefer to stick with a sniffer for localhost debugging. But a HTTP proxy like Fiddler is a reasonable workaround.

[networking](https://blog.codinghorror.com/tag/networking/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
[localhost](https://blog.codinghorror.com/tag/localhost/)
[http](https://blog.codinghorror.com/tag/http/)
[fiddler](https://blog.codinghorror.com/tag/fiddler/)
