---
title: "homu + highfive: awesome bots that make open source projects easier"
date: 2016-05-13
url: https://jvns.ca/blog/2016/05/13/homu-plus-highfive-making-less-work-for-open-source-maintainers/
slug: homu-plus-highfive-making-less-work-for-open-source-maintainers
word_count: 288
---


Someone described my approach to blogging as “fanfiction” recently, a description that I kind of loved. A lot of the time I write about things that I find in the world that love and my take on them. So here is a small thing I saw that I liked!


The other day I submitted a pull request to an open source project ([rust-lang/libc](https://github.com/rust-lang/libc)) for the first time in a while and it was a really delightful experience! There were two bots involved and they were both great.


The first thing that happened is `rust-highfive-bot` commented. It said:


> Thanks for the pull request, and welcome! The Rust team is excited to review
> your changes, and you should hear from @alexcrichton (or someone else) soon.


I was like YAY! The aforementioned @alexcrichton responded almost immediately, saying


```
@bors: r+ 1931ee4

Thanks!

```


Cool! What is this mysterious `r+ 1931ee4` incantation? What is he saying? Basically he’s saying “this looks reasonable; fine with me as long as the tests pass!” Who is @bors?


bors is the Github account of a [homu](https://github.com/barosl/homu), [homu.io](http://homu.io/) bot. Homu’s job is to make it so that you don’t have to keep checking to see if the tests pass! This is a huge blessing on this particular repository because the tests take like an hour. Also, the tests seem to be flaky or something, so they failed a few times and bors took care of rerunning them. [here is the pull request, and you can see it getting merged!](https://github.com/rust-lang/libc/pull/283).


I’m really into homu. It’s the second iteration of a piece of software called [bors by Graydon Hoare](http://graydon.livejournal.com/186550.html), and there’s a great blog post talking about it and highfivebot called [Rust infrastructure can be your infrastructure](http://huonw.github.io/blog/2015/03/rust-infrastructure-can-be-your-infrastructure/).
