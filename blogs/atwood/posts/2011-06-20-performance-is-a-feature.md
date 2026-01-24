---
title: "Performance is a Feature"
date: 2011-06-20
url: https://blog.codinghorror.com/performance-is-a-feature/
slug: performance-is-a-feature
word_count: 1873
---

We’ve always put a heavy emphasis on performance at Stack Overflow and [Stack Exchange](http://stackexchange.com/). Not just because we’re performance wonks (guilty!), but because we think speed is a competitive advantage. There’s [plenty of experimental data](https://blog.codinghorror.com/speed-still-matters/) proving that **the slower your website loads and displays, the less people will use it.**


> [Google found that] the page with 10 results took 0.4 seconds to generate. The page with 30 results took 0.9 seconds. Half a second delay caused a 20% drop in traffic. Half a second delay killed user satisfaction.
> In A/B tests, [Amazon] tried delaying the page in increments of 100 milliseconds and found that even very small delays would result in substantial and costly drops in revenue.


I believe the converse of this is also true. That is, the faster your website is, the *more* people will use it. This follows logically if you think like [an information omnivore](https://blog.codinghorror.com/designing-for-informavores-or-why-users-behave-like-animals-online/): the faster you can load the page, the faster you can tell whether that page contains what you want. Therefore, you should always favor fast websites. The opportunity cost for switching on the public internet is effectively nil, and whatever it is that you’re looking for, there are multiple websites that offer a similar experience. So how do you distinguish yourself? **You start by being, above all else, *fast*.**


Do you, too, feel the need – [the need for speed?](http://www.youtube.com/watch?v=OlkInNZ7xis) If so, I have three pieces of advice that I’d like to share with you.


### 1. Follow the Yahoo Guidelines. Religiously.


The golden reference standard for building a fast website remains Yahoo’s 13 Simple Rules for [Speeding Up Your Web Site](https://blog.codinghorror.com/yslow-yahoos-problems-are-not-your-problems/) from 2007. There is one caveat, however:


> There’s some good advice here, but there’s also a lot of advice that only makes sense if you run a website that gets millions of unique users per day. Do you run a website like that? If so, what are you doing reading this instead of flying your private jet to a Bermuda vacation with your trophy wife?


So … a funny thing happened to me since I wrote that four years ago. I now run a network of public, [community driven Q&A web sites](http://stackexchange.com/sites) that *do* get millions of daily unique users. (I’m still waiting on the jet and trophy wife.) It does depend a little on the size of your site, but if you run a public website, **you really should **[**pore over Yahoo’s checklist**](http://developer.yahoo.com/performance/rules.html)** and take every line of it to heart**. Or use the tools that do this for you:

- [Yahoo YSlow](http://developer.yahoo.com/yslow/)
- [Google Page Speed](http://code.google.com/speed/page-speed/)
- [Pingdom Tools](http://tools.pingdom.com/)


We’ve long since implemented most of the 13 items on Yahoo’s list, except for one. But it’s a big one: [Using a Content Delivery Network](http://developer.yahoo.com/performance/rules.html#cdn).


> The user’s proximity to your web server has an impact on response times. Deploying your content across multiple, geographically dispersed servers will make your pages load faster from the user’s perspective. But where should you start?
> As a first step to implementing geographically dispersed content, don’t attempt to redesign your web application to work in a distributed architecture. Depending on the application, changing the architecture could include daunting tasks such as synchronizing session state and replicating database transactions across server locations. Attempts to reduce the distance between users and your content could be delayed by, or never pass, this application architecture step.
> Remember that 80-90% of the end-user response time is spent downloading all the components in the page: images, stylesheets, scripts, Flash, etc. This is the *Performance Golden Rule*. Rather than starting with the difficult task of redesigning your application architecture, it’s better to first disperse your static content. This not only achieves a bigger reduction in response times, but it’s easier thanks to content delivery networks.


As a final optimization step, we just [rolled out a CDN](http://blog.stackoverflow.com/2011/05/the-speed-of-light-sucks/) for all our static content. The results are promising; the baseline here is our datacenter in NYC, so the below should be read as *“how much faster did our website get for users in this area of the world?”*


![](https://blog.codinghorror.com/content/images/2025/04/image-536.png)


In the interests of technical accuracy, static content isn’t the complete performance picture; you still have to talk to our servers in NYC to get the dynamic content which is the meat of the page. But 90% of our visitors are anonymous, only 36% of our traffic is from the USA, and Yahoo’s research shows that 40 to 60 percent of daily vistors come in [with an empty browser cache](https://web.archive.org/web/20110718150652/http://yuiblog.com/blog/2007/01/04/performance-research-part-2/). Optimizing this cold cache performance worldwide is a *huge* win.


Now, I would not recommend going *directly* for a CDN. I’d leave that until later, as there are a bunch of performance tweaks on Yahoo’s list which are free and trivial to implement. But using a CDN has gotten a heck of a lot less expensive and much simpler since 2007, with lots more competition in the space from companies like [Amazon’s](http://aws.amazon.com/cloudfront/), [NetDNA](https://www.netdna.io/), and [CacheFly](http://www.cachefly.com/). So when the time comes, and you’ve worked through the Yahoo list as religiously as I recommend, you’ll be ready.


### 2. Love (and Optimize for) Your Anonymous *and* Registered Users


Our Q&A sites are all about making the internet better. That’s why all the contributed content is [licensed back to the community](http://blog.stackoverflow.com/category/cc-wiki-dump/) under Creative Commons and *always* visible regardless of whether you are logged in or not. I [despise walled gardens](https://blog.codinghorror.com/avoiding-walled-gardens-on-the-internet/). In fact, you don’t actually have to log in *at all* to participate in Q&A with us. Not even a little!


The primary source of our traffic is anonymous [users arriving from search engines](https://blog.codinghorror.com/trouble-in-the-house-of-google/) and elsewhere. It’s classic “write once, read – and [hopefully edit](http://blog.stackoverflow.com/2011/02/suggested-edits-and-edit-review/) – millions of times.” But we are also making the site richer and more dynamic for our avid community members, who definitely *are* logged in. We add features all the time, which means we’re serving up more JavaScript and HTML. There’s an unavoidable tension here between the download footprint for users who are on the site every day, and users who may visit once a month or once a year.


Both classes are important, but have fundamentally different needs. Anonymous users are voracious consumers optimizing for rapid browsing, while our avid community members are the source of all the great content that drives the network. These guys (and gals) need each other, and they both deserve special treatment. **We design and optimize for two classes of users: anonymous, and logged in.** Consider the following Google Chrome network panel trace on a random Super User question I picked:

kg-card-begin: html


|  | requests | data transferred | DOMContentLoaded | onload |
| Logged in (as me) | 29 | 233.31 KB | 1.17 s | 1.31 s |
| Anonymous | 22 | 111.40 KB | 768 ms | 1.28 s |


kg-card-end: html

We minimize the footprint of HTML, CSS and Javascript for anonymous users so they get their pages *even faster*. We load a stub of very basic functionality and dynamically “rez in” things like editing when the user focuses the answer input area. For logged in users, the footprint is necessarily larger, but we can also add features for our most avid community members at will without fear of harming the experience of the vast, silent majority of anonymous users.


### 3. Make Performance a Point of (Public) Pride


Now that we’ve exhausted the Yahoo performance guidance, and made sure we’re serving the absolute minimum necessary to our anonymous users – where else can we go for performance? Back to our code, of course.


When it comes to website performance, there is no getting around one fundamental law of the universe: **you can never serve a webpage faster than it you can render it on the server.** I know, duh. But I’m telling you, it’s very easy to fall into the trap of not noticing a few hundred milliseconds here and there over the course of a year or so of development, and then one day you turn around and your pages are taking almost a full freaking second to render on the server. It’s a heck of a liability to start *1 full second in the hole* before you’ve even transmitted your first byte over the wire!


That’s why, as a developer, you need to put performance right in front of your face on every single page, all the time. That’s exactly what we did with our [MVC Mini Profiler](http://code.google.com/p/mvc-mini-profiler/), which we are contributing back to the world as open source. The simple act of **putting a render time in the upper right hand corner of every page we serve** forced us to fix all our performance regressions and omissions.


![](https://blog.codinghorror.com/content/images/2025/04/image-535.png)


(Note that you can click on the SQL linked above to see what’s actually being run and how long it took in each step. *And* you can use the share link to share the profiler data for this run with your fellow developers to shame them diagnose a particular problem. *And* it works for multiple AJAX requests. Have I mentioned that our open source MVC Mini Profiler is totally freaking awesome? If you’re on a .NET stack, you should really check it out.)


In fact, with the render time appearing on every page for everyone on the dev team, **performance became a point of pride**. We had so many places where we had just gotten a *little* sloppy or missed some *tiny* thing that slowed a page down inordinately. Most of the performance fixes were trivial, and even the ones that were not turned into fantastic opportunities to rearchitect and make things simpler and faster for all of our users.


Did it work? You bet your sweet [ILAsm](http://msdn.microsoft.com/en-us/library/496e4ekx.aspx) it worked:


![](https://blog.codinghorror.com/content/images/2025/04/image-534.png)


That’s the Google crawler page download time; the experimental Google Site Performance page, which ostensibly reflects complete full-page browser load time, confirms the improvements:


![](https://blog.codinghorror.com/content/images/2025/04/image-533.png)


While server page render time is only part of the performance story, it is the baseline from which you start. I cannot emphasize enough how much the simple act of putting the page render time on the page helped us, as a development team, build a dramatically faster site. Our site was always relatively fast, but even for a historically “fast” site like ours, we realized huge gains in performance from this one simple change.


I won’t lie to you. Performance isn’t easy. It’s been a long, hard road getting to where we are now – and we’ve thrown a lot of unicorn dollars toward really nice hardware to run everything on, though I wouldn’t call any of our hardware choices particularly extravagant. And I did [follow my own advice](https://blog.codinghorror.com/hardware-is-cheap-programmers-are-expensive/), for the record.


I distinctly remember switching from AltaVista to Google back in 2000 in no small part because it was blazing fast. To me, **performance is a feature**, and I simply like using fast websites more than slow websites, so naturally I’m going to build a site that I would want to use. But I think there’s also a lesson to be learned here about the competitive landscape of the public internet, where there are two kinds of websites: **the quick and the dead**.


Which one will you be?

[performance](https://blog.codinghorror.com/tag/performance/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[speed optimization](https://blog.codinghorror.com/tag/speed-optimization/)
[website responsiveness](https://blog.codinghorror.com/tag/website-responsiveness/)
