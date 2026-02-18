---
title: "A few notes on my CUSEC talk"
date: 2016-01-14
url: https://jvns.ca/blog/2016/01/14/a-few-notes-on-my-cusec-talk/
slug: a-few-notes-on-my-cusec-talk
word_count: 225
---


I gave a talk today! If you came, thanks for coming! Here are some notes and links if you’d like to learn more!


### on debugging

- on Linux, learn strace. It’s the best. I wrote [a zine about it](http://jvns.ca/blog/2015/04/14/strace-zine/) that you can download and print. I also wrote a [a million blog posts about it](http://jvns.ca/categories/strace/).
- on OS X, learn dtrace. It’s even better than strace. [This post](https://blog.8thlight.com/colin-jones/2015/11/06/dtrace-even-better-than-strace-for-osx.html) has a great introduction
- [the 40ms networking bug I talked about fixing](http://jvns.ca/blog/2015/11/21/why-you-should-understand-a-little-about-tcp/)
- ngrep is a fun tool for network analysis
- If you need to analyze encrypted traffic, use [mitmproxy](https://mitmproxy.org/)
- [wireshark](https://www.wireshark.org/) gives you a really nice graphical interface for network spying. It’s fun.
- [How I got better at debugging](http://jvns.ca/blog/2015/11/22/how-i-got-better-at-debugging/)
- for more tools: [a few spy tools for your operating system (other than strace)](http://jvns.ca/blog/2015/04/06/a-few-spy-tools-for-your-operating-system-other-than-strace/)


### on computers being fast

- play the game: [computers-are-fast.github.io](http://computers-are-fast.github.io)
- visualvm comes with Java, and it’s a good first step ([a screenshot of it](http://jvns.ca/blog/2016/01/03/java-isnt-slow/))
- [A millisecond isn’t fast](http://jvns.ca/blog/2015/09/10/a-millisecond-isnt-fast-and-how-we-fixed-it/)
- YourKit is a great profiler for Java, but not free
- for stories of performance debugging, see [Nancy Drew and the case of the Slow Program](http://jvns.ca/blog/2015/03/15/nancy-drew-and-the-case-of-the-slow-program/)
- perf is cool for C++, and I wrote [a blog post about it](http://jvns.ca/blog/2014/05/13/profiling-with-perf/)
- [the video of Brendan Gregg yelling at a hard drive](https://www.youtube.com/watch?v=tDacjrSCeq4). his website is also fantastic: [brendangregg.com/](http://www.brendangregg.com/)
