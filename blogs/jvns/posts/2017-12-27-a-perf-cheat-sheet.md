---
title: "A perf cheat sheet"
date: 2017-12-27
url: https://jvns.ca/blog/2017/12/27/a-perf-cheat-sheet/
slug: a-perf-cheat-sheet
word_count: 184
---


Right now I’m working on finishing up a zine about perf that I started back in May, and I’ve been
struggling with how to explain all there is to say about perf in a concise way.


Yesterday I finally hit on the idea of making a 1-page cheat sheet reference which covers all of the
basic perf command line arguments. I’m going to make it the centerfold for the zine.


It has a lot of the basics, as well as some slightly more advanced stuff – for example `sudo perf top -e raw_syscalls:sys_enter -ns comm -d 1` counts system calls by process and shows you live updates, and `stdbuf -oL perf top -e net:net_dev_xmit -ns comm | strings` counts sent network packets by process and prints an update every second. I didn’t realize you could do either of those things!


All the examples in this cheat sheet are taken (with permission) from [http://brendangregg.com/perf.html](http://brendangregg.com/perf.html), which is a
fantastic perf reference and has many more great examples.


Here it is. You can click to make it bigger. There’s also a print version: [perf cheat sheet PDF](https://jvns.ca/perf-cheat-sheet.pdf).
