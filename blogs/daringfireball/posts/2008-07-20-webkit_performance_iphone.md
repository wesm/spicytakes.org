---
title: "WebKit Performance on iPhone OS 2.0"
date: 2008-07-20
url: https://daringfireball.net/2008/07/webkit_performance_iphone
slug: webkit_performance_iphone
word_count: 588
---


As part of the iPhone SDK developer program, I’ve been running a seed of the GM build of the new OS on my original iPhone for a few weeks now. Overall, there are surprisingly few visible changes to the system. Many of the built-in apps are, at least visibly, identical to the versions in iPhone OS 1.1.4. This includes Safari — if anything has changed in Safari’s user interface, I haven’t noticed it.1


But under the hood, MobileSafari 2.0’s performance is hugely improved over 1.1.4. Everything related to web surfing feels faster, and in side-by-side comparisons using my wife’s iPhone running 1.1.4, web pages consistently load faster on 2.0, both via Wi-Fi and EDGE. This has nothing to do with the new iPhone 3G hardware — this is about dramatic performance improvements on original iPhones upgraded to the 2.0 OS.


Using MobileSafari simply feels faster, especially with web applications. *Feel* is by nature subjective, but JavaScript benchmarks back this up.


In August last year, [Craig Hockenberry posted a few simple benchmarks](http://furbo.org/2007/08/15/benchmarking-in-your-pants/) to compare the iPhone’s processing power and JavaScript interpreter against Safari 3 running on a Mac with a 1.83 GHz Core Duo. At that time, the current version of the iPhone OS was 1.0.1. Here are the results of those same benchmarks on original iPhones running the 1.1.4 and new 2.0 OS versions, with Hockenberry’s 1.0.1 results included for comparison:



| Test | 1.0.1 | 1.1.4 | 2.0 | Vs. 1.0.1 / 1.1.4 |
| 100,000 iterations | 3.209 | 1.096 | 0.145 | 22× / 8× |
| 10,000 divisions | 0.413 | 0.181 | 0.029 | 14× / 6× |
| 10,000 sin(x) calls | 0.709 | 0.373 | 0.140 | 5× / 3× |
| 10,000 string allocations | 0.777 | 0.434 | 0.133 | 6× / 3× |
| 10,000 function calls | 0.904 | 0.595 | 0.115 | 8× / 5× |



The last column shows how many times faster the 2.0 version of MobileSafari was versus 1.0.1 and 1.1.4. The same results, charted (smaller bars are faster):


The results are obvious. WebKit JavaScript performance has improved steadily and significantly in just one year, with a huge jump between 1.1.4 and the new 2.0.0.


I also tested both iPhone 1.1.4 and 2.0.0 against [Celtic Kane’s JavaScript benchmarks](http://celtickane.com/webdesign/jsspeed.php). The average time over three runs for iPhone 1.1.4 was 8,945 ms; for iPhone 2.0 it was 5,307 — just under 1.7 times faster. (For comparison, Safari 3.1.2 on my 2.5 GHz MacBook Pro took just 133 ms — 40 times faster than the iPhone.)


The tests I ran here were specific to JavaScript, but I strongly suspect WebKit performance has improved across the board. In side-by-side page loading tests between two original iPhones running 1.1.4 and 2.0.0, the new version consistently finished at least a few seconds faster.


For all the hubbub regarding the new App Store, most “iPhone software” runs in the web browser. But improvements in WebKit performance often help native iPhone app performance, too — a slew of my favorite native iPhone apps have built-in WebKit browsers (e.g., NetNewsWire, Twitterrific, Instapaper, and Cocktails). When WebKit performance improves, any app that uses WebKit improves, and WebKit improved *a lot* between iPhone 1.1.4 and 2.0.0.


---

1. Except for the very cool new feature where you can tap-and-hold on an image to bring up a dialog that lets you save the image to your iPhone camera roll. ↩︎



| **Previous:** | [Distant and Remote](https://daringfireball.net/2008/07/remote_keyboard) |
| **Next:** | [Not Yet Squirrelly](https://daringfireball.net/2008/07/not_yet_squirrelly) |


PreviousNext