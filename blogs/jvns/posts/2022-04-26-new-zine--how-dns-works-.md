---
title: "New zine: How DNS Works!"
date: 2022-04-26
url: https://jvns.ca/blog/2022/04/26/new-zine--how-dns-works-/
slug: new-zine--how-dns-works-
word_count: 880
---


Hello! On Thursday we released a new zine about one of my favourite computer systems: DNS!


You can get it for $12 here:
[https://wizardzines.com/zines/dns](https://wizardzines.com/zines/dns), or get
an [11-pack of all my zines here](https://wizardzines.com/zines/all-the-zines/).


Here’s the cover and table of contents:


### why DNS?


I wanted to write about DNS for three reasons:

1. **DNS is everywhere!** You basically can’t use the internet without using
DNS — nobody is going to memorize all the IP addresses for every domain they
use. You need to look them up with DNS!
2. **DNS has a really cool decentralized design!** I love that it gives you
control of your own little corner of the internet (it just costs ~$12/year to
own a domain!), I love that the basic design is relatively straightforward,
and I love that it’s worked basically the same way for 40 years and scaled
relatively well over time
3. **DNS is very frustrating!** I’ve run into some VERY weird DNS problems over
the years, and it can feel magical and incomprehensible if you don’t know
how it works. But once you learn how DNS works, these problems all become
totally possible to understand.


And I’ve never seen a clear explanation of DNS that included all of the
technical details I wanted to know, so I decided to write one.


### a DNS playground!


I find the most fun way to learn is by experimenting and breaking things! So back in December,
[Marie](https://marieflanagan.com/) and I built a playground where you can do
weird DNS experiments with no consequences if you mess something up.


It’s called [Mess With DNS](https://messwithdns.net). It has examples of
experiments you can try, and you’ve very encouraged to come up with your own
experiments.


There’s also [a blog post](https://jvns.ca/blog/2021/12/15/mess-with-dns/) from when we released it in December.


### a simple DNS lookup tool


I also built a little DNS lookup tool at [https://dns-lookup.jvns.ca](https://dns-lookup.jvns.ca) to provide
an easy way to do DNS queries without using the command line. Even though I
love the command line I actually find myself using it all the time.


### what we left out: DNS security


The main thing that *isn’t* in the zine is DNS security (DNS over HTTPS, DNS
over TLS, DNSSEC).  This is because the DNS security landscape still seems to
be evolving, and I didn’t feel confident that we could write something that
would still be true in 5-10 years.


I think I’ll try to write a blog post about DNS security at some point though.


### identifying common points of confusion is amazing


I mentioned earlier that my friend [Marie Claire LeBlanc Flanagan](https://marieflanagan.com/) and I built
Mess With DNS together in December. That was really fun, so Marie and I decided
to work together on this zine too – we paired on it for about an hour every
weekday for almost 4 months. I’m pretty sure I wouldn’t have finished the zine
without her.


She was incredibly helpful with everything to do with the zine (editing!
character design! marketing! rewriting the NS records page 5 times!), but one
of the biggest things she improved for this zine was *feedback*.


Usually I only get feedback from maybe 10 beta readers, but this time we wanted
to hear from more people and get better at identifying common points of confusion.


We did this by building a small custom feedback website where people could
click on a page and leave feedback (“I have a question! This is confusing! I
learned something! I have a suggestion! I love this!”).


Building a custom website let us organize the feedback way more easily and hear
from more people – in the end we got ~1200 feedback items from ~60 people and
all of the feedback made the zine a LOT better.


I might write a longer meta post about all of this later.


### some blog posts leading up to this zine


I wrote a bunch of blog posts about DNS over the last year or so while thinking
about this zine. Here they all are:

- [What happens when you update your DNS?](https://jvns.ca/blog/how-updating-dns-works/)
- [A little tool to make DNS queries](https://jvns.ca/blog/2021/02/24/a-little-tool-to-make-dns-queries/)
- [A tool to spy on your DNS queries: dnspeep](https://jvns.ca/blog/2021/03/31/dnspeep-tool/)
- [How do you tell if a problem is caused by DNS?](https://jvns.ca/blog/2021/11/04/how-do-you-tell-if-a-problem-is-caused-by-dns/)
- [DNS “propagation” is actually caches expiring](https://jvns.ca/blog/2021/12/06/dns-doesn-t-propagate/)
- [Why might you run your own DNS server?](https://jvns.ca/blog/2022/01/05/why-might-you-run-your-own-dns-server-/)
- [Some ways DNS can break](https://jvns.ca/blog/2022/01/15/some-ways-dns-can-break/)
- [A toy DNS resolver](https://jvns.ca/blog/2022/02/01/a-dns-resolver-in-80-lines-of-go/)
- [The multiple meanings of “nameserver” and “DNS resolver”](https://jvns.ca/blog/2022/02/14/some-dns-terminology/)


### you can get a print copy shipped to you!


There’s always been the option to print the zines yourself on your home printer.


But this time there’s a new option too: you can get a print copy shipped to
you! (just click on the “print version” link on [this
page](https://wizardzines.com/zines/dns/))


The only caveat is that the international shipping costs are unreasonably high,
so if you’re outside the US it probably doesn’t make sense to get just 1 zine
shipped to you. I’m still trying to find a workaround for that. Orders of $60+
do include free international shipping though.


Here’s the link to get the zine again:
[https://wizardzines.com/zines/dns/](https://wizardzines.com/zines/dns/)


### thank you


If you’ve bought zines in the past, thanks so much for all your support over
the years. None of this would be possible without you.
