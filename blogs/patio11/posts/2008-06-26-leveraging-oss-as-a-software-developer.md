---
title: "Leveraging OSS As A Software Developer"
date: 2008-06-26
url: https://www.kalzumeus.com/2008/06/26/leveraging-oss-as-a-software-developer/
slug: leveraging-oss-as-a-software-developer
word_count: 1518
---


Cards on the table: I sell [proprietary software](http://www.bingocardcreator.com), do occasional [OSS](http://kalzumeus.com/2007/04/17/simple-enhancement-to-lightbox/) [work](http://sourceforge.net/projects/megamek) on both a volunteer and paid basis. and have been known to post to Slashdot on occasion about my love of Windows Vista.  This either means I’m sort of an agnostic in the wars of religion over software business models, or that I really love making enemies.  But I’m more of a fan of making friends, so I’m perpetually trying to convince members of both warring camps that they can get a lot of what they want out of the others.


One perpetual worry on the [Business of Software forums](http://discuss.joelonsoftware.com/?biz) is that some OSS developer (invariably a grungy, marginally employed coder with Jolt stains on his T-shirt) is going to come along, clone your application, and eat your lunch.  As a result there is a certain amount of hostility among small software developers towards OSS, which is a shame.  I spent some time earlier trying to address [myths about it](https://www.kalzumeus.com/2006/08/23/open-source-vs-uisvs-some-myths-that-need-to-die/), but I thought I’d go one better and focus on ways OSS can make you money.


**Concentrate On What You Do Best.  Let Other People Do Everything Else**


Currently I’m finally getting restarted on my latest project, which is a web service that helps small businesses do content syndication across the Internet.  There are a number of interesting technical challenges here, including both server-side (“How do I let a person who is potentially only paying me $9 a month generate tens of thousands of pageviews without the server bills putting me in the poorhouse?”) and client side (“How do I use Javascript to make the whole process pain-free for non-technical end users?”).


As it turns out, I’m a fair hand at some portions of the puzzle, but portions of it are complex.  Very complex.  You have no idea how far down the rabbit hole goes in web development, Alice.  I honestly think that it is impossible, flat out *impossible*, for any one person to be expert at all the technologies which are implicated by a trivial web application running on a modern web stack.  This includes everything from HTTP to the DOM model to Javascript to the database to relative velocities of the little spinning bits of metal that make everything work.


Thankfully, programmers get this lovely tool called *abstraction*, which means we can concentrate on one bit of the problem at a time and treat the rest of the world as a Solved Problem.  For example, when I’m working on Rails, I am not thinking about the L1 cache policy on the server.  In fact, although I really appreciate my $150,000 CS degree, it is entirely possible that I will grow old and die without ever once worrying about L1 cache.  Smarter people take care of that stuff for me.


**OSS Is About Smarter People Taking Care Of That Stuff For You**


One key feature of my content syndication widgets is that they be able to spread without requiring user action away from the host site, to avoid antagonizing hosting site owners.  This was going to require some serious work on my part to achieve — probably several days worth, as Javascript is not my bag.  As it turns out, [Lightbox Gone Wild](http://particletree.com/features/lightbox-gone-wild/) (a variant of the Lightbox project which I’ve [previously used](http://kalzumeus.com/2007/04/14/lightbox-quick-pretty-screenshot-previews/) to business-enhancing effect) took this from several days of work to about five minutes of integration.


Lightbox Gone Wild is made by [Wufoo](http://wufoo.com/), a company which doesn’t specialize in wild-and-crazy Javascript, but rather in selling a service which makes data collection easy for people.  Note that key word *selling* – OSS developers are typically not poor aesthetics who need to beg for their next cup of coffee.  Since wild-and-crazy Javascript doesn’t make Wufoo money directly, they release it back into the ecosystem for someone to extend (much as how they themselves extended the previous Lightbox project), with the added benefit that they may get to incorporate the extensions later and in the meantime people who have no interest in HTML forms nonetheless say good things about them.  (If you need form input and HTML scares you, go to Wufoo.  There, did my good deed for the day.)


In turn, I’m going to tweak *their* script a few times to add usability enhancing features (like backporting my “escape button closes the layer” tweak to the original Lightbox, which is a big win for non-technical customers), which increases the aggregate value of free OSS available but still gets me incrementally closer to making money from my paying customers.


In fact, taking stock over what I’ve accomplished so far, I realize I’m doing a *whole lot* of this borrowing from OSS.  From classic infrastructure components ([database](http://www.mysql.com), [web server](http://nginx.net), [application stack](http://www.rubyonrails.org)) to user interface elements ([editing controls](http://tinymce.moxiecode.com/), [charts](http://code.google.com/p/google-charts-on-rails/)) to a zillion pieces of behind the scenes wizardry, I’m probably literally using several thousand man months worth of software, adding two man months worth of glue and secret sauce, and then if all goes according to plan making a bit of money off of it.


**That’s the OSS Business Model**


I often hear folks wondering whether they’ll make more money if they stop charging for their main application and OSS it.  Survey says *no* in most cases.  Rather than being engaged 100% in the production of OSS, you can OSS contributions you make which are boring, routine, and only tangentially connected to the main business of solving specific problems for your customers.  This allows you to lower development costs very modestly, but the social benefits are very nice for a bootstrapped software company.


Giving away [free](http://www.bingocardcreator.com/free-trial.htm) [stuff](http://www.bingocardcreator.com/printable-bingo-cards.htm) directly to your customers is a time-worn capitalist tradition, but giving away free stuff to other people works pretty decently too.  We live in an era where, for better or worse, GoogleBot is a judge of character and strongly prefers people who share.  (OSS users/developers have, on average, extraordinarily high levels of technical expertise and are solidly members of the [linkerati](http://www.seomoz.org/blog/identifying-the-linkerati).  They make good folks to influence from an SEO perspective.  You also get direct benefits from having vocal, technically capable, engaged people interested in you personally — although those direct benefits may not extend into them actually buying your software, but then again they weren’t in your niche to begin with so no harm done.)


**OSS as a Barrier To Entry**


But wait, there’s more.  It seems funny to say, since OSS is making it vastly *easier* for *me* to build my website, but I think that it functions as a barrier to entry for competitors.  You can’t just whistle your fingers and snap together 15 diverse and unconnected OSS projects into a usable application — the design and integration of complex systems is still a skill, and it is one that is in many ways more difficult than straight-up application development in some domains.  This turns skill with particular OSS projects, or generalized methods and patterns of integration, into one more competitive wedge you’ve got in your arsenal.


Additionally, OSS raises something of a **quality cliff** in front of prospective competitors who are not using as much as you.  Consider the typical graph of development effort expended versus value to the customer.  Typically, this gently slopes upwards for the first portion of the graph (“20% of the effort secures 80% of the value”), and then it plateus for a very long time as the easy wins are exhausted and the long, arduous process of software development begins.


The curve for a developer using lots of OSS doesn’t look different in asymptotic behavior, but it contains numerous discontinuities along the way.  Every time you spend a small quantum of effort to integrate a new feature (that you didn’t have to write), your user-perceived quality gaps up.  Someone running along on your old curve, trying to keep up, runs straight into the quality cliff-face.


Example: assume you and hypothetical competitor Bob include analytics in your application.  Both of you decide, sensibly, that the screens require a visual component.  Bob starts coding his.  You quickly integrate [Google Charts](http://code.google.com/apis/chart/), which while not strictly speaking OSS is the same general principle.  Now Bob isn’t just running the race against you — he’s running against the team at Google doing the Charts development and you’re already done and busy working on your next feature.  It makes OSS a great force multiplier.


**Sidenote**


Speaking of Google Charts: wonderful output, neatly solves the problem of graphing without requiring massive server-side resources or Flash-capable browsers.  Terrible, terrible API from a programming standpoint — you write uber-ugly incomprehensible URLs and their servers return the appropriate charts.  Luckily, folks have already extended it by offering wrappers in many popular programming languages (I mentioned the Ruby one already), which is another example of collaboration making a good thing better.


I’m planning on eventually releasing a bit of magic myself, which will let you treat the charts as if they were being produced locally.  (There are decent reasons for this, from branding issues to future-proofing your site in case Google decides to cancel the charts project and you don’t want holes developing in all your old content all of a sudden.)
