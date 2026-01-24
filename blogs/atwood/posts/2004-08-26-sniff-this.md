---
title: "Sniff this!"
date: 2004-08-26
url: https://blog.codinghorror.com/sniff-this/
slug: sniff-this
word_count: 153
---

I’ve occasionally used network sniffers in the past, but with the rise of REST, XML, SOAP and .NET Remoting in the last year, sniffing has become an essential part of my development toolkit. I’ve evaluated a bunch of network sniffers, including the excellent open-source Ethereal, but the one I keep coming back to is [Etherdetect](http://www.etherdetect.com/):


![](https://blog.codinghorror.com/content/images/2025/06/image-44.png)


Etherdetect isn’t free, and it isn’t perfect, but it offers the best blend of functionality and ease of use that I’ve found. Peeking behind the scenes at network traffic has solved some tough performance and debugging problems in our .NET apps. Highly r**ecommended.**


One tip: you typically can’t sniff traffic going to localhost, at least not without some special workarounds; the loopback TCP/IP stack behaves very differently than the “normal” network paths. Also, you’ll need the latest WinPcap libraries installed, particularly if you have a hyperthreading CPU.

[network sniffer](https://blog.codinghorror.com/tag/network-sniffer/)
[rest](https://blog.codinghorror.com/tag/rest/)
[xml](https://blog.codinghorror.com/tag/xml/)
[soap](https://blog.codinghorror.com/tag/soap/)
[.net remoting](https://blog.codinghorror.com/tag/net-remoting/)
[etherdetect](https://blog.codinghorror.com/tag/etherdetect/)
[ethereal](https://blog.codinghorror.com/tag/ethereal/)
[winpcap](https://blog.codinghorror.com/tag/winpcap/)
