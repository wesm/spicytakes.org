---
title: "Systems We Love 2016"
date: 2016-12-23
url: https://jvns.ca/blog/2016/12/23/systems-we-love/
slug: systems-we-love
word_count: 252
---


A couple weeks ago I went to Systems we Love!
There’s a list of [all the talks here](https://blog.bradfieldcs.com/all-the-talks-from-systems-we-love-debcd9cffca#.o499a5isd). A few of my favorites: (they’re all 20 minutes)


[A Race Detector Unfurled](https://youtu.be/TPe6UXMDMGM?t=5h55m17s) by
Kavya Joshi was definitely my favorite talk of the conference. She
explains how the Go race detector works super super clearly. I didn’t
know anything about the topic, and now I do!


7074 says Hello World by Marianne Bellotti was another of my favorites.
I think sadly it wasn’t recorded, but it talked about where mainframes
fit in in the US government’s technology, and about what it’s like to
have to integrate with them.


I liked [Less Ado about NTP](https://www.youtube.com/watch?v=TPe6UXMDMGM&feature=youtu.be&t=2h25m9s), mostly because it laid out really
clearly the **assumptions** about the NTP system, specifically that the
latency from computer A to computer B is the same as the latency from
computer B to computer A. It made me want to learn more about NTP!


[DNS and the Art of Making Systems “Just Complex Enough”](https://youtu.be/TPe6UXMDMGM?t=7h4m4s) by Alex Wilson is an
interesting discussion about the design of DNS. It talks about how the DNS
spec goes out of its way to say “hey, if you don’t understand a record,
you have to pass it on verbatim”. This is a great example of a design
decision that helps you upgrade a protocol gradually over time!


[An AWK Love Story](https://youtu.be/TPe6UXMDMGM?t=7h51m20s) is also
super good. I’ve been confused by awk for a long time and this helped me
understand a little better how it’s used.
