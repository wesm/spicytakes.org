---
title: "Day 7: An echo server in Clojure"
date: 2013-10-09
url: https://jvns.ca/blog/2013/10/09/day-7-an-echo-server-in-clojure/
slug: day-7-an-echo-server-in-clojure
word_count: 172
---


Today I spent some time on a fun kernel module, but it is not working
yet!  So here is what I also did.


It did not take very long and I didn’t really learn too much Clojure
doing this – this is really just procedural code written in Clojure. I
can’t tell yet if this is an appropriate way to write a small Clojure
program. Need to get some code review on this.


But it works! You can see the code here: [https://gist.github.com/jvns/6910896](https://gist.github.com/jvns/6910896)


You can interact with the server using `netcat`
(see also: [Day 2: netcat fun!](http://jvns.ca/blog/2013/10/01/day-2-netcat-fun/)).
The `-u` option here tells netcat to use UDP instead of TCP.


```
bork@kiwi ~/w/h/clorrent> nc -u localhost 12345
Hi, Clojure!
Hi, Clojure!

```


If you don’t want to set up a whole
[Leinengen](https://github.com/technomancy/leiningen) project to run
this, you can use
[lein-exec](https://github.com/kumarshantanu/lein-exec).


This is the first step towards maybe writing a BitTorrent client in
Clojure – many other people are writing BitTorrent client and really
enjoying it, and I’m jealous. We’ll see if it happens!
