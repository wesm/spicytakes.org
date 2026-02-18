---
title: "Day 22: Got some TCP packets back!"
date: 2013-11-06
url: https://jvns.ca/blog/2013/11/06/day-22-got-some-tcp-packets-back/
slug: day-22-got-some-tcp-packets-back
word_count: 190
---


I spent a bunch of time with [Jessica](http://web.mit.edu/jesstess/www/)
trying to send TCP packets to get the
[http://example.com](http://example.com) homepage.


It turned out that the problem we were having was not at the TCP level,
but actually at HTTP level: we needed to send something like


```
example.com\r\nAccept: */*\r\n\r\n"

```


to make the server actually reply. I then successfully reassembled a
bunch of TCP packets into a webpage! I still need to

- reply saying I got the packets (to the FIN-ACK, I think)
- Make sure I don’t use duplicate packets when I reassemble
- probably lots of things.


Today wasn’t super productive, I think because I gave a talk at NYC
Python and I was a bit worried about it. The talk went well, though! So
tomorrow I will hopefully get more done. We will see!


I really want to start writing “real” code again soon. Maybe tomorrow.
This exploratory networking stuff is super fun and I’m learning a lot,
but I feel like I haven’t written much code in a while and it is
bothering me. Maybe a bittorrent client will come soon =)


BUT WHICH LANGUAGE. Clojure? Hmm.
