---
title: "My Scaling Hero"
date: 2008-12-10
url: https://blog.codinghorror.com/my-scaling-hero/
slug: my-scaling-hero
word_count: 880
---

Inspiration for [Stack Overflow](http://stackoverflow.com/) occasionally comes from the unlikeliest places. Have you ever heard of the [dating website, Plenty of Fish?](http://www.nytimes.com/2008/01/13/business/13digi.html?ex=1357966800&en=bfde0f1a6ec77632&ei=5090&partner=rssuserland&emc=rss&pagewanted=all)


> **Markus Frind built the Plenty of Fish Web site in 2003 as nothing more than an exercise to help teach himself a new programming language, ASP.NET.** The site first became popular among English-speaking Canadians. Popularity among online daters in many United States cities followed more recently, and with minimal spending on advertising the site. According to data from comScore Media Metrix for November 2007, Plenty of Fish had 1.4 million unique visitors in the United States. In December, Mr. Frind said, the site served up 1.2 billion page views, and page views have soared 20 percent since Dec. 26.


The actual [plentyoffish.com](http://www.plentyoffish.com/) site design, although it has improved (believe it or not) since the last time I looked, is almost horrifyingly bad; it literally looks like a high school student’s first website programming attempt. But *it doesn’t matter*. The site is a resounding success with users, to the point that it is almost completely user-run:


> No one heads to Plenty of Fish for the customer service, which is all but nonexistent. The company does not need a support structure to handle members’ subscription and billing issues because the service is entirely advertising-based. Its tagline is: “100 percent free. Put away your credit card.” For hand-holding, users must rely on fellow members, whose advice is found in online forums. The Dating & Love Advice category lists more than 320,000 posts, making up in sheer quantity what it lacks in a soothing live presence available by phone.


Granted, comparing a dating site to other online properties is kind of unfair. As I mentioned in [an earlier post](https://blog.codinghorror.com/design-matters-but-content-is-king/), the most sustainable and enduring business models either get you laid, or get you paid – and the more directly the better. Jamie Zawinski’s classic [Groupware Bad](http://www.jwz.org/doc/groupware.html) article covers the same ground:


> So I said, narrow the focus. Your “use case” should be, there’s a 22 year old college student living in the dorms. How will this software get him laid?


It’s pretty clear which axis of human needs Plenty of Fish tends to. It’s already working with [way more cheese](https://blog.codinghorror.com/youll-never-have-enough-cheese/) than most software developers will ever have.


OK, so Markus Frind singlehandedly built a massively popular free dating site that is almost entirely community run. Big deal. But what makes it *especially* incredible is that he does it all on [a handful of servers](http://highscalability.com/plentyoffish-architecture):

kg-card-begin: html

> 1.2 billion page views per month, 500,000 average unique logins per day
> 30+ million hits per day, 500-600 per second
> 45 million visitors per month
> top 30 site in the US, top 10 in Canada, top 30 in the UK
> 2 load balanced Windows Server 2003 x64 web servers with 2 Quad Core 2.66Ghz CPUs, 8 GB RAM, 2 hard drives
> 3 database servers. No data on their configuration
> Approaching 64,000 simultaneous connections and 2 million page views per hour
> Internet connection is a 1 Gbps line, 200 Mbps is used
> 1 TB per day serving 171 million images through Akamai
> 6 TB storage array to handle millions of full sized images uploaded every month to the site

kg-card-end: html

These traffic and size numbers are nothing short of astonishing. **He’s accomplished all this on his own, using only five servers with the same Microsoft and ASP.NET stack we use**. This gives me great hope for scaling Stack Overflow without needing a lot of employees or server hardware. I’m not sure we’ll ever reach those kinds of traffic levels.


That said, there are some dark clouds on the horizon; in a recent blog post, Markus noted that [their free business model](https://web.archive.org/web/20081210033047/http://plentyoffish.wordpress.com/2008/11/13/monetization-free-verse-paid/) doesn’t always scale as well as the hardware:


> The problem with free is that every time you double the size of your database the cost of maintaining the site grows 6 fold. I really underestimated how much resources it would take, I have one database table now that exceeds 3 billion records. The bigger you get as a free site the less money you make per visit and the more it costs to service a visit.


Of course, any resemblance between a free dating site and a question-and-answer site for programmers is [purely coincidental](https://blog.codinghorror.com/egoless-programming-you-are-not-your-job/), I’m sure.


> In the early years of programming, a program was regarded as the private property of the programmer. One would no more think of reading a colleague’s program unbidden than of picking up a love letter and reading it. **This is essentially what a program was, a love letter from the programmer to the hardware, full of the intimate details known only to partners in an affair.** Consequently, programs became larded with the pet names and verbal shorthand so popular with lovers who live in the blissful abstraction that assumes that theirs is the only existence in the universe. Such programs are unintelligible to those outside the partnership.


Maybe Stack Overflow is also built on [love, internet style](http://www.youtube.com/watch?v=Xe1TZaElTAs). Here’s hoping that scales as well as Plenty of Fish has.

kg-card-begin: html

Update: Markus notes that according to hitwise, as of 2008, he runs the [#13 website](https://web.archive.org/web/20081222013953/http://plentyoffish.wordpress.com/2008/12/20/2008-was-a-good-year-now-13-in-the-us/) in the United States.

kg-card-end: html
[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[scalability](https://blog.codinghorror.com/tag/scalability/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
