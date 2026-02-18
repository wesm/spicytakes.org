---
title: "On the profitability of image hosting websites"
date: 2014-10-10
url: https://drewdevault.com/2014/10/10/The-profitability-of-online-services.html
slug: The-profitability-of-online-services
word_count: 1004
---

I’ve been doing a lot of thought about whether or not it’s even possible to both
run a simple website  *and*  turn a profit from it  *and*  maintain a high quality
of service. In particular, I’m thinking about image hosts, considering that I
run one (a rather unprofitable one, too), but I would
think that my thoughts on this matter apply to more kinds of websites. That
being said, I’ll just talk about media hosting because that’s where I have
tangible expertise.

I think that all image hosts suffer from the same sad pattern of eventual
failure. That pattern is:

1. Create a great image hosting website (you should stop here)
2. Decide to monetize it
3. Add advertising
4. Stop allowing hotlinking
5. Add more advertising
6. Add social tools like comments, voting - attempt build a community to look at
your ads

Monetization is a poison. You start realizing that you wrote a shitty website in
PHP on shared hosting and it can’t handle the traffic. You spend more money on
it and realize you don’t like spending your money on it, so you decide to
monetize, and now the poison has got you. There’s an extremely fine line to walk
with monetization. You start wanting to make enough money to support your
servers, but then you think to yourself “well, I worked hard for this, maybe I
should make a living from it!” This introduces several problems.

First of all, you made an image hosting website. It’s already perfect. Almost
anything you can think of adding will only make it worse. If you suddenly decide
that you need to spend more time on it to justify taking money from it, then you
have a lot of time to get things wrong. You eventually run out of the good
features and start implementing the bad ones.

More importantly, though, you realize that you should be making  *more*  money.
Maybe you can turn this into a nice job working on your own website! And that
means you should start a business and assign yourself a salary and start making
a profit and hire new people. The money has to come from somewhere. So you make
even more compromises. Eventually, people stop using your service. People start
to  *detest*  your service. It can get so bad that people will refuse to click on
any link that leads to your website. Your users will be harassed for continuing
to use your site.  **You fail, and everyone hates you.**

This trend is observable with PhotoBucket, ImageShack, TinyPic, the list goes
on. The conclusion I’ve drawn from this is that  **it is impossible to run a
profitable image hosting service without sacrificing what makes your service
worthwhile** . We have arrived at a troubling place with the case of Imgur,
however.  MrGrim (the creator of Imgur) also identified this trend and decided
to put a stop to it by building a simple image hosting service for Reddit. It
had great intentions, check out the old archive.org mirror of it 1 .  With
these great intentions and a great service, Imgur rose to become the 46th most
popular website globally 2 , and 18th in the United States alone, on the
shoulders of Reddit, which now ranks 47th. I’m going to expand upon this here,
particularly with respect to Reddit, but I included the ranks here to dissuade
anyone who says “there’s more than Reddit out there” in response to this post.
Reddit is a  *huge*  deal.

Other image hosts died down when people recognized their problems. Imgur has
reached a critical mass where that will not happen. 20% of all new Reddit posts
are Imgur, and most users just don’t know better than to use anything else. That
being said, Imgur shows the signs of the image hosting poison. They stopped
being an image hosting website and became their own community. They added
advertising, which is fine on its own, but then they started redirecting direct
links 3  to pages with ads. And still, their userbase is just as strong,
despite better alternatives appearing.

I’m not sure what to do about Imgur. I don’t like that they’ve won the mindshare
with a staggering margin. I do know that I’ve tried to make my own service
immune to the image hosting poison. We run it incredibly lean - we handle over
10 million HTTP requests per day on a single server that also does transcoding
and storage for $200 per month. We get about $20-$30 in monthly revenue from our
Project Wonderful 4  ads, and a handful of donations that usually amount to
less than $20. Fortunately, $150ish isn’t a hard number to pay out of our own
pockets every month, and we’ve made a damn good website that’s extremely
scalable to keep our costs low. We haven’t taken seed money, and we’re not
really the sort to fix problems by throwing more money at it. We also won’t be
hiring any paid staff any time soon, so our costs are pretty much constant. On
top of that, if we do fall victim to the image hosting poison, 100% of our code
is open source, so the next service can skip R&D and start being awesome
immediately. Even with all of that, though, all I can think of doing is sticking
around until people realize that Imgur really does suck.

*2017-03-07 update*

* mediacru.sh shut down (out of money)
* pomf.se shut down (out of money)
* minus.com shut down after going down the decline described in this post

I have started a private service called  [sr.ht](https://sr.ht) , which I aim to
use to fix the problem by only letting my friends and I use it. It has
controlled growth and won’t get too big and too expensive. It’s on Github if you
want to  [use it](https://github.com/SirCmpwn/sr.ht) .

1. [Original Imgur home page](https://web.archive.org/web/20090225014924/http://imgur.com/) ↩︎
2. [Imgur on Alexa](http://www.alexa.com/siteinfo/imgur.com) ↩︎
3. [Imgur redirects “direct” links based on referrals](https://dillpickle.github.io/imgur-please-dont-be-the-next-tinypic-or-imageshack.html) ↩︎
4. [Project Wonderful, an advertising service that doesn’t suck](https://www.projectwonderful.com/) ↩︎
