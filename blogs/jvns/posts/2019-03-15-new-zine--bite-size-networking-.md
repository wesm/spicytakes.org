---
title: "New zine: Bite Size Networking!"
date: 2019-03-15
url: https://jvns.ca/blog/2019/03/15/new-zine--bite-size-networking-/
slug: new-zine--bite-size-networking-
word_count: 729
---


Last week I released a new zine: Bite Size Networking! It’s the third zine in the “bite size”
series:

1. [Bite Size Linux](https://wizardzines.com/zines/bite-size-linux/)
2. [Bite Size Command Line](https://wizardzines.com/zines/bite-size-command-line/)
3. [Bite Size Networking](https://wizardzines.com/zines/bite-size-networking/)


You can get it for $10 at [https://wizardzines.com/zines/bite-size-networking/](https://wizardzines.com/zines/bite-size-networking/)! (or $150/$250/$600 for
the corporate rate).


Here’s the cover and table of contents!


A few people have asked for a 3-pack with all 3 “bite size” zines which is coming soon!


### why this zine?


In last few years I’ve been doing a lot of networking at work, and along the way I’ve gone from “uh,
what even is tcpdump” to “yes I can just type in `sudo tcpdump -c 200 -n port 443 -i lo`” without
even thinking twice about it. As usual this zine is the resource I wish I had 4 years ago. There are
so many things it took me a long time to figure out how to do like:

- inspect SSL certificates
- make DNS queries
- figure out what server is using that port
- find out whether the firewall is causing you problems or not
- capture / search network traffic on a machine


and as often happens with computers none of them are really that hard!! But the man pages for the
tools you need to do these things are Very Long and as usual don’t differentiate between “everybody
always uses this option and you 10000% need to know it” and “you will never use this option it does
not matter”. So I spent a long time staring sadly at the tcpdump man page.


the pitch for this zine is:


> It’s Thursday afternoon and your users are reporting SSL errors in production and you don’t know
> why. Or a HTTP header isn’t being set correctly and it’s breaking the site. Or you just got a
> notification that your site’s SSL certificate is expiring in 2 days. Or you need to update DNS to
> point to a new server. Or a server suddenly isn’t able to connect to a service. And networking
> maybe isn’t your full time job, but you still need to get the problem fixed.


Kamal (my partner) proofreads all my zines and we hit an exciting milestone with this one: this is
the first zine where he was like “wow, I really did not know a lot of the stuff in this zine”. This
is of course because I’ve spent a lot more time than him debugging weird networking things,
and when you practice something you get better at it :)


### a couple of example pages


Here are a couple of example pages, to give you an idea of what’s in the zine:


![](https://jvns.ca/images/ngrep.png)


![](https://jvns.ca/images/ping.png)


### next thing to get better at: getting feedback!


One thing I’ve realized that while I get a ton of help from people while writing these zines (I
read probably a thousand tweets from people suggesting ideas for things to include in the zine), I
don’t get as much feedback from people about the final product as I’d like!


I often hear positive things (“I love them!”, “thank you so much!”, “this helped me in my job!”) but
I’d really love to hear more about which bits specifically helped the most and what didn’t make as
much sense or what you would have liked to see more of. So I’ll probably be asking a few questions
about that to people who buy this zine!


### selling zines is going well


When I made the switch about a year ago from “every zine I release is free” to “the old zines are
free but all the new ones are not free” it felt scary! It’s been startlingly totally fine and a very
positive thing. Sales have been really good, people take the work more seriously, I can spend more
time on them, and I think the quality has gone up.


And I’ve been doing occasional [giveaways](https://tweets.jvns.ca/b0rk/status/1104368319816220674) for
people who can’t afford a $10 zine, which feels like a nice way to handle “some people legitimately
can’t afford $10 and I would like to get them information too”.


### what’s next?


I’m not sure yet! A few options:

- kubernetes
- more about linux concepts (bite size linux part II)
- how to do statistics using simulations
- something else!


We’ll see what I feel most inspired by :)
