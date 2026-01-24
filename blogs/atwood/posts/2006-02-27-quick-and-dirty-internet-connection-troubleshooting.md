---
title: "Quick and Dirty Internet Connection Troubleshooting"
date: 2006-02-27
url: https://blog.codinghorror.com/quick-and-dirty-internet-connection-troubleshooting/
slug: quick-and-dirty-internet-connection-troubleshooting
word_count: 401
---

So I had a few [bandwidth issues](https://web.archive.org/web/20060322070625/http://scobleizer.wordpress.com/2006/02/16/im-getting-into-coding-horror/) recently, which you can see in the six-month Alexa traffic graph for this domain.


There wasn’t much I could do about the traffic spike. But I did make good use of **two of my favorite tools for quick and dirty internet connection troubleshooting**. The two most important questions to ask are:


**How wide is your internet connection?**


In other words, **bandwidth**. How many kilobytes per second does your ISP allow you to transmit and receive? Most consumer internet connections are highly asymmetric – they offer extremely fast downloads but only a tiny fraction of that for uploads. Your typical cable modem is around 300 kilobytes per second when downloading (sometimes even faster), but only 30 kilobytes per second when uploading.


For quick bandwidth measurements, I like [NetMeter](https://web.archive.org/web/20060405034446/http://readerror.gmxhome.de/). It only shows traffic on a single computer, but when run on a server it can give you a nice idea of how much bandwidth you’re using at any given time. For such a lightweight little applet, it also has some surprisingly sophisticated long-term logging and reporting abilities – you can see how much bandwidth you’ve used over weeks and even months.


![](https://blog.codinghorror.com/content/images/2025/05/image-219.png)


**How fast is your internet connection?**


In other words, **latency**. How quickly does your ISP get your packets from point A to point B? Do they arrive in a timely fashion? Do they arrive at all? Unless your connection suffers from severe packet loss, this is a bit less of a priority than raw bandwidth. But it can be frustrating if your connection isn’t responsive or is unreliable.


For latency measurements, I like [PingPlotter](http://www.pingplotter.com/). It comes in a few editions, including free. To test for latency or connectivity problems you’ll want to run a few instances of PingPlotter over a series of days, all pinging large websites.


![](https://blog.codinghorror.com/content/images/2025/05/image-220.png)


Set the graph interval to something wide like 24 or 48 hours, and once you collect enough samples, you’ll have a nice idea of when your ISP’s network is busy or unavailable:


![](https://blog.codinghorror.com/content/images/2025/05/image-221.png)


Now, these are intentionally lightweight tools. They’re no match for fancy, dedicated networking diagnostic apps. But they’re simple to use and easy to gather data with. When you’re calling your ISP’s tech support, having these kinds of graphs to email them carries a heck of a lot more weight than generic complaints about “slowness.”

[network troubleshooting](https://blog.codinghorror.com/tag/network-troubleshooting/)
[internet bandwidth](https://blog.codinghorror.com/tag/internet-bandwidth/)
[netmeter](https://blog.codinghorror.com/tag/netmeter/)
[bandwidth measurement](https://blog.codinghorror.com/tag/bandwidth-measurement/)
[internet connection](https://blog.codinghorror.com/tag/internet-connection/)
