---
title: "Why I Don’t Host My Own Blog Anymore"
date: 2012-02-09
url: https://www.kalzumeus.com/2012/02/09/why-i-dont-host-my-own-blog-anymore/
slug: why-i-dont-host-my-own-blog-anymore
word_count: 1939
---


**I moved my blog over to [WPEngine](http://wpengine.com) recently. Why? Read on.**


I started blogging about 375,000 words ago (about three full-length novels… crikey). At first, I was on a subdomain of WordPress.com, mostly because a) it was free and b) I had no intention of ever writing anything more significant than a few observations I made while developing a summer project.  My posts about making and marketing software turned out to be rather more popular than I anticipated, and I eventually made them my main professional presence and moved them to their own domain name.


Eventually, I decided that I had to be in control of my site rather than being locked into only the themes and functionality that WordPress.com supported, so I started hosting the blog myself.  I installed WordPress on a modest 512 MB VPS from Slicehost, with the standard Apache 2 / PHP / MySQL stack, and thought that would be the end of my hosting decisions.  Sadly, it was only the beginning.


## WordPress, PHP, and Apache: The Trifecta Of Finnicky Software


I’m a web developer by trade, so I’m very skeptical of unevidenced comments like “lol, PHP can’t scale.”  It’s transparently obvious that PHP can scale — one look at who uses it (*Facebook* is really all you need to know) proves that.  Sadly, my system crashed frequently under load, even after upgrading the 512 MB slice to a 1,024 MB slice, and after tweaking Apache and PHP’s memory-usage settings for hours.  I read practically everything written about caching plugins for WordPress and it availed me not.  The loads at issue weren’t generally that impressive, either: 10,000 pageviews here,  100,000 pageviews there, either way a modern server in 2006 ~ 2012 should eat those numbers for breakfast.


In addition to tweaking the heck out of my settings, I was hacking WordPress to lessen the load on the server.  I went so far as to putting all the static resources for this blog (CSS, images, etc) on a server used for my software business, since no level of traffic has ever managed to give Nginx a problem in my experience.  This made the blog much more stable under load, but it still crashed occasionally.


I eventually found the culprit: a setting in Apache named, ironically, KeepAlive.  Since then I have been seized by missionary zeal in trying to [convince people](http://www.hnsearch.com/search#request/all&q=patio11+keepalive) that leaving KeepAlive on will [probably not be in your best interests](https://www.kalzumeus.com/2010/06/19/running-apache-on-a-memory-constrained-vps/).  I turned off KeepAlive and have had a much more stable time since then.


Even with all this work, my blog crashed four times in 2011.  Each time, my monitoring software woke me up, and I learned things like “Oh, Jimmy Wales tweeted about an article of mine” at 4 AM in the morning while trying to restart the server.  I’ve probably lost in excess of 100,000 readers over the years for the blog being down.


I eventually got so fed up with Apache that I spent a day to migrate this (and 15 other sites) from using Apache as a front-end webserver to using Nginx to serve all requests and proxy dynamic requests to a backend Apache instance.  (Why not use Nginx to execute the PHP directly?  Long story — I do that elsewhere, but it isn’t painless.)


## Routine Maintenance Sucked, Too


You’ve heard about WordPress’ somewhat spotty security record, right?  I’m aware of it as a practicing engineer and have even reported a few doozies in commonly deployed themes/plugins myself.  So I took some fairly extraordinary measures to secure the blog versus a stock WordPress installation:

- required all access of the admin to happen through a proxy that I control
- locking down all files on the WordPress installation such that the webserver could not write to them — this makes plugin installation/maintenance a manual chore and breaks some plugins, but makes it less likely that a [vulnerability in a plugin or theme](http://markmaunder.com/2011/08/01/zero-day-vulnerability-in-many-wordpress-themes/) will ruin your day
- performed some sporadic code audits on things I am inexpert on in a language I detest.  I eventually stopped doing this because reporting vulnerabilities to the WordPress ecosystem could easily be my full time job.


As a result of this, to my knowledge my blog never got compromised.  Whee, great.  It only took me a few billable *weeks*.  Plus I had all the usual fun of applying patches, making backups, restoring from backups when MySQL decided to eat the wp_posts table (still no clue why that happened), tweaking settings for rotating logs, migrating my hosting provider (Rackspace bought Slicehost so I had to move servers), yadda yadda yadda.


## “Do You Enjoy Hosting WordPress?”


Two years ago at a conference I ran into Jason Cohen, a [very smart guy](http://blog.asmartbear.com/) who had sold his previous software business.  He told me that his new venture was managed WordPress hosting.  I was outwardly interested and inwardly cringing, because I thought “There are already WordPress hosts available for $4 a month, they all suck, and the software is pretty much irredeemable.  If it weren’t the best blogging software available I’d take a hammer to my backups then burn the shards and bury them on sanctified ground so that they never troubled the world again.”


At some point Jason asked me if I liked hosting WordPress.  I told him “I love hosting WordPress!  I love all the power and tweakability!”  And while I do appreciate control, I still can’t imagine what possessed me to say that.  Hosting WordPress has been a black hole of my time.


Last year I ran into Jason Cohen at another conference. He told me that WPEngine, the [WordPress hosting](http://wpengine.com) company he’d told me about, was live and doing well.  In my haste to demonstrate that I had learned something from cutting myself on WordPress for the last five years, I mentioned “I guess you guys figured out to turn KeepAlive off, huh?”


Jason said “Actually, no.  I mean, sure, in the general case for a VPS, you want it off because otherwise your site gets non-responsive under load.  However, if you’ve got Apache talking to the outside world, something is wrong.  Apache only handles the request after it’s been through a load balancer, a Varnish caching proxy, and then Nginx, because Nginx does static content so well.  If the request gets that far *you want KeepAlive on* because your Apache will only be talking within your datacenter, only have a handful of connections, and you want those connections to be alive almost indefinitely because setup/teardown is always waste.”


You know how often I talk to software company CEOs and get not just corrected but *destroyed* and then re-educated about a point of technical fact?  Suffice it to say it made an impression.


So when Jason invited me over to WPEngine to do some marketing work, I leaped at the chance.  I went down to Texas for a week, met the team, and did my thing.  (Sidenote: Want to see a fairly typical week’s work for me?  Take a gander at their [speed test tool](http://speed.wpengine.com), which you can point at an arbitrary WordPress site and learn why your page load speed isn’t optimized enough yet.  The punchline is, of course, that if you were with WPEngine they would have already fixed that for you.  I assisted with a redesign of this, wrote the month-long WordPress optimization course that the tool will let you sign up for, and generally improved copy and the like on their marketing site.)


## So I Switched


In the course of hearing the sales pitch from them several times so I could write it accurately, I became convinced: WPEngine is absolutely superior in every way to me continuing to host the blog myself.  So I took out my credit card, signed up for their $200 a month plan (prices got reduced recently, [see here](http://wpengine.com/pricing)), and migrated my blog over.  It has been quietly hosting my blog for the last several weeks, including through two of my highest traffic days ever, without a hitch.  For the first time, I can watch a post go to the top of HN and not have to have “top” open to keep an eye on swap consumption.


A few things that particularly impressed me about WPEngine:

- A few hours after migrating my blog I got an automated email saying that they had found an outdated copy of TimThumb in my WordPress install and had upgraded it for me.  It wasn’t a vulnerability (permissions locked down saved the day for that one), but I’m very, very glad they keep an eye on things so that I don’t have to.
- Migration was almost painless.  I just dumped the WP database, grabbed my existing files, and copied them over as instructed.  I needed to speak to support to get a setting tweak done for me (the plan I bought has WordPress multi-site not single site like my old blog, and this resulted in a minor issue), but all told I was up and running in about two hours of elapsed time.
- Just like their speed tool promised, my site did get modestly faster.


I’m a bit of a YSlow fanboy and ever once in a while I go through my sites and make an optimization pass, so I usually have all the low-hanging fruit like gzipping, static content loaded from multiple domains, and the like taken care of.  I wasn’t expecting WPEngine to shave much time from my page loads, given the amount of optimization work I had already done, but I kept the old server around to do a fair test on AOL’s speed tool.  Take a look what happens: here’s a video showing (left) my old 1,024 MB VPS versus (right) WPEngine showing the same page from my blog.


If you didn’t watch the movie, I’ll spoil it: content pops in about half a second earlier (and finishes loading .8 seconds earlier) on WPEngine with no manual tweaking versus my tweaked-to-limit-of-my-ability VPS.


That test uses IE8 on a reasonable residential Internet connection coming from the US. For accessing from Japan or on a mobile device, it is *viscerally* faster for me, probably due to the CDN which WPEngine uses.


## Do You Have A Blog For Business? Use WPEngine


The VPS that I used to run my blog on cost a bit over $100 a month (1 GB Rackspace slice + 160 GB of bandwidth + backups = I am not actually sure). WPEngine runs me $200 a month because I have high anticipated traffic. They have a $29 option for folks who don’t.


$2,500 a year for blog hosting sounds a bit on the high side, but it is honestly nothing against the amount of time that I will no longer have to invest supporting this sucker. I love being out of the hosting business. I never intended on being in it in the first place — it was always just something I needed to do to write for people. Less time poured down that black hole means more time to work on my businesses and share what I learn doing so.


WPEngine has been a total, epic win for me. I suggest that you use them if you are using WordPress for a business: go ahead, [make with the clicky clicky](http://wpengine.com). Want to just geek out on how they have their infrastructure setup? See [here.](http://wpengine.com/our-infrastructure/)


P.S. Long-time readers are aware of this, but just to reiterate: I don’t take money for blog posts, was not asked to write this by WPEngine (who are, again, clients of mine), and would not have written it except that their service really rocks.
