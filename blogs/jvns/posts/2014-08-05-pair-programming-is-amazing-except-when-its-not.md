---
title: "Pair programming is amazing! Except... when it's not."
date: 2014-08-05
url: https://jvns.ca/blog/2014/08/05/pair-programming-is-amazing-except-when-its-not/
slug: pair-programming-is-amazing-except-when-its-not
word_count: 1284
---


I wrote a blog post in March about
[why I find pair programming useful](https://jvns.ca/blog/2014/03/01/pair-programming/)
as a tool and why I enjoy it. There are entire companies like Pivotal
that do pair programming 100% of the time, and they find it useful.


To get our terms straight, by “pair programming”, I mean “two people
are trying to accomplish a task by sitting at a single computer
together”.


Some people mentioned after I wrote that blog post that they disliked
pair programming, sometimes strongly! Obviously these people aren’t
wrong to not like it. So I asked people about their experiences:


> I'm pretty
> interested in why people find pair programming hard or scary or not
> useful. (I find it not-always-appropriate but a good tool.)—
> Julia Evans (@b0rk) [March 2,
> 2014](https://twitter.com/b0rk/statuses/440023032178814976)


People responded *wonderfully*. You can see about 160 thoughtful
tweets about what people find hard or difficult in this Storify
[What do you find hard about pair programming?](http://storify.com/jvns/what-do-you-find-hard-about-pair-programming/).
I learned a ton, and my view that “pair programming is great and you
totally should try it!!!” got tempered a little bit :)


If you’re not up to reading all that, here are the broad categories
that the difficulties fell into. Thanks very much to everyone who
responded for giving permission for me to post their comments!


### “I’m completely drained after an hour or two”


Pair programming is really intense. You concentrate really hard, don’t
take a lot of breaks, and it’s very mentally taxing. *Tons* of people
brought this up. And this seems to be true for everyone, even people
who find it a useful tool.

- “it can be very stressful and draining for an introvert, both
productivity killers in the long run.” -
[@hoxworth](http://twitter.com/hoxworth)
- “I used to work at Pivotal (100% pairing). IME pairing makes
everything go faster. Also exhausting.” -
[@shifrapr](http://twitter.com/shifrapr)
- “definitely would not like my entire project to be pair programmed
though; even 2-3 days would be exhausting.” -
[@lojikil](http://twitter.com/lojikil)
- “Downsides I hear a lot when teaching workshops on pairing:
exhausting” - [@moss](http://twitter.com/moss)
- “I find it sometimes awesome & sometimes really frustrating,
honestly. It can be exhausting,but also a way to discover unknown
unknowns” - [@DanielleSucher](http://twitter.com/DanielleSucher)
- “that being sad: pairing is great. All the time though would be
exhausting (for me)” - [@qrush](http://twitter.com/qrush)
- “It is hard sometimes because you need to be on the same wavelength
as another person which can be tiring.” -
[@zmanji](http://twitter.com/zmanji)


### “I can’t type when there’s somebody looking. I hate pairing.”


Anxiety around pairing is *really* common. Some people say that they
found it easier as time went on. Some people also didn’t! It can be
good to encourage someone to try something, but if someone’s tried and
it just makes them super-anxious, respect that!

- “I hate pairing because I can’t type when there’s somebody looking
and I get anxious when I watch somebody else typing for long D:” -
[@seaandsailor](https://twitter.com/seaandsailor)
- “I type somewhat slow and I always feel pressure (real or imagined)
from the other person.” - [@Torwegia](https://twitter.com/Torwegia)
- “I have seen seasoned vim users writhe in pain upon having to watch
a normal user type at a typically glacial human speed :)” -
[@brandon_rhodes](http://twitter.com/brandon_rhodes)
- “I suffer keyboard anxiety when I haven’t paired in a while.” -
[@meangrape](http://twitter.com/meangrape)
- “anxiety, fear of being judged” - [@qrush](http://twitter.com/qrush)
- “i get self-conscious, make dumb mistakes, confuse myself.. :(
pairing is the worst” -
[@wirehead2501](http://twitter.com/wirehead2501)
- “it’s something about having someone see my process, like when
you’re writing an email with someone reading over your shoulder.” -
[@wirehead2501](http://twitter.com/wirehead2501)


### “I only like pairing when my partner is a pleasure to work with”


This is pretty key. Pairing is a pretty intimate thing to do – you’re
letting people see exactly how you work. If you don’t trust and
respect the person that you’re pairing with, it doesn’t work. There
also seems to be some mystical magical pairing juice where with some
people it just doesn’t work, and with some people it’s amazing.

- " once you’re pairing with an asshole, you might as well stop.
There’s no point." - [@hsjuju2](http://twitter.com/hsjuju2)
- “I only like pairing when my partner is a pleasure to work with. So
I try to be too.” - [@rkulla](http://twitter.com/rkulla)
- “if you feel like someone will see you as less competent for voicing
your thoughts, I’d rather code by myself” -
[@hsjuju2](http://twitter.com/hsjuju2)
- “I think the social rules of [Hacker School] make pairing a lot more
helpful and fun.” - [@hsjuju2](http://twitter.com/hsjuju2)
- “yeah it really has to be a safe space. Done among people who trust
and respect one another. It also builds trust and respect.” -
[@gigachurch](http://twitter.com/gigachurch)


### “Talking through something doesn’t help me think”


A lot of the reason that I like pairing is that talking helps me work
through problems. People are different! Some people *hate* talking
about things to think. Something to be aware of.

- “personally I only make progress on problems when talking to
someone.” - [@cartazio](http://twitter.com/cartazio)
- “I am *not* someone who thinks out loud, and i feel like that’s one
reason pairing is hard for me.” -
[@wirehead2501](http://twitter.com/wirehead2501)
- “like, not only do i not understand by talking, but trying to talk
through something before i think = more confused” -
[@wirehead2501](http://twitter.com/wirehead2501)
- “I’m someone who thinks out loud, and understands by talking,
whereas some people take that as bad” -
[@hsjuju2](http://twitter.com/hsjuju2)


This is also relevant to interviewing: advice like “try to talk
through your issue!” works really well for some people, and badly
for others.


### “It’s bad when one person dominates”


My first pairing experience (years ago) was with someone who was a
much better programmer than me, and basically bulldozed through the
problem and left me no room to contribute. This really undermined my
confidence and was awful.


When pairing with people with significantly less experience than me, I
try to be really careful about this. One good trick that I learned
from Zach Allaun at Hacker School is to always pair on the less
experienced person’s project and/or let the newer person drive. If
you’re working on their project then they’re at least the expert on
how their project works, which helps a lot.


### “I love pair *debugging*, not pair programming”


Variations on this were pretty common. A few people said that they
like working together, but not for producing code. It’s totally okay
to use pairing in specific ways (for teaching or for debugging or for
debugging), and not for other things.

- “+1 for loving code reviews, pair programming, not do much. Pair
*debugging* on the other hand can be excellent.” -
[@pphaneuf](http://twitter.com/pphaneuf)
- “i actually find it really useful as a “let’s get to know how each
other’s brain works” & a shortcut for coming up to speed on a
codebase or a new language. otherwise–i haven’t had really awesome
experiences with it.” - [@zmagg](http://twitter.com/zmagg)
- “I’m not sold on *always* pairing, but being able to debug or design
w/ a second pair of eyes is often useful, & it helps share
skills.” - [@silentbicycle](http://twitter.com/silentbicycle)
- “Can be a good way to learn. I was pretty much taught perl via pair
programming years ago by a very patient coworker.” -
[@wendyck](http://twitter.com/wendyck)
- “I spend half my day staring into space letting solutions pop into
my head. Hard to do that with a partner there.” -
[@aconbere](https://twitter.com/aconbere)


## Pair programming is amazing… sometimes


Pair programming can be a super useful tool. If you understand why
people (such as yourself, maybe!) might find it hard or stressful, you
can have more productive pairing sessions, and decide when pair
programming is a good way to get a task done!
