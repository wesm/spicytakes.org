---
title: "Behold WordPress, Destroyer of CPUs"
date: 2008-04-22
url: https://blog.codinghorror.com/behold-wordpress-destroyer-of-cpus/
slug: behold-wordpress-destroyer-of-cpus
word_count: 733
---

Lately I’ve been delving into the [WordPress](http://wordpress.org/) ecosystem, as it seems to be the most popular blogging platform around at the moment. I’ve set up two blogs with it so far. In the process, I’ve gotten quite comfortable with the setup, interface, and overall operation of WordPress.

1. [blog.stackoverflow.com](http://blog.stackoverflow.com/)
2. [www.fakeplasticrock.com](https://web.archive.org/web/20080429210309/http://www.fakeplasticrock.com/)


I’ve been thoroughly impressed with the community around WordPress, and the software itself is remarkably polished. That’s not to say that I haven’t run into a few egregious bugs in the 2.5 release, but on the whole, the experience has been good bordering on pleasant.


Or at least it *was*, until I noticed how much CPU time the PHP FastCGI process was using for modest little old blog.stackoverflow.com.


![](https://blog.codinghorror.com/content/images/2025/04/image-88.png)


For context, this is running on a Windows Web Server 2008 virtual machine with a single core of a 2.13 GHz Xeon 3210 entirely dedicated to it.


This is an *incredibly* scary result; blog.stackoverflow.com is getting, at best, a **moderate trickle of incoming traffic**. It’s barely linked anywhere! With that kind of CPU load level, this site would fall over instantaneously if it got remotely popular, or God forbid, anywhere *near* the front page of a social bookmarking website.


For a bare-bones blog which is doing approximately nothing, this is a completely unacceptable result. It’s appalling.


As evidence of what a systemic problem this is, there’s an entire cottage industry built around shoehorning better caching behavior into WordPress. Take your pick: [WP-Cache](https://web.archive.org/web/20080422091045/http://mnm.uib.es/gallir/wp-cache-2/), [WP-Super-Cache](https://web.archive.org/web/20080424124200/http://ocaoimh.ie/wp-super-cache/), or [Bad Behavior](http://error.wordpress.com/2006/07/04/bad-behavior-2/). The caching add-ins don’t work very well [under IIS](http://www.allaboutduncan.com/index.php/2008/wp-cache-on-iis-finally/) because they assume they’re running on a *NIX platform, but they can be coerced into working.


Does it work? Does it ever. Here’s what CPU usage looks like with basic WP-Cache type functionality enabled:


![](https://blog.codinghorror.com/content/images/2025/04/image-87.png)


I’m not alone; just do a web search on [WordPress CPU usage](http://www.google.com/search?q=wordpress+%27cpu+usage%27) or [WordPress Digg Effect](http://www.google.com/search?q=wordpress+%27digg+effect%27) and you’ll find page after page of horror stories, most (all?) of which are solved by the swift and judicious application of the WP-Cache plugins.


It’s not like this a new issue. Personally, I think it’s absolutely irresponsible that **WP-Cache like functionality isn’t already built into WordPress.** I would not even consider deploying WordPress anywhere without it. And yet, according to a [recent podcast](https://web.archive.org/web/20080430064145/http://wp-community.org/2008/04/06/episode-39/), Matt Mullenweg dismisses it out of hand and hand-wavingly alludes to vague TechCrunch server reconfigurations.


A default WordPress install will query the database twenty times every time you refresh the page, even if not *one single element* on that page has changed. Doesn’t that strike you as a bad idea? Maybe even, dare I say it, *sloppy programming?*


I understand that users may have umpteen thousand [WordPress plugins](http://wordpress.org/extend/plugins/) installed, all of which demand to change on every page load. Yes, the easiest path, the path of least resistance, is to mindlessly query the database every time you’re building a page. But I *cannot* accept that a default, bare-bones WordPress install hasn’t the first clue how to cache and avoid expensive, redundant trips to the database.


It’s frustrating, because caching is a completely solved problem in other programming communities. For example, the .NET framework has had [page output caching](http://msdn2.microsoft.com/en-us/library/aa478965.aspx) and [page fragment output caching](http://msdn2.microsoft.com/en-us/library/h30h475z(VS.71).aspx) baked into ASP.NET for years.


I sure am glad I started this blog in [Movable Type](http://www.movabletype.org/) way back in 2004. Their classic static rendering blog engine approach may be derided today, but I shudder to think of the number of times the Coding Horror webserver would have been completely incapacitated over the years by the naïve – no, that’s too tame – brainlessly stupid dynamic rendering approach WordPress uses.


What I just don’t understand is why, after all these years, and all these documented problems, WordPress hasn’t **folded WP-Cache into the core**. If you’re ever planning to have traffic of any size on a WordPress blog, consider yourselves warned.


Update: Matt Mullenweg kindly responded to this post and offered his recommended MySQL [configuration optimizations](https://web.archive.org/web/20080501180002/http://www.codinghorror.com/blog/files/matt-mullenweg-wordpress-mysql-recommendations.txt). I definitely agree that the Query Cache is extremely important to performance, and for some reason it defaulted to off (zero size) on my installation. You may also want to look into [innotop](https://web.archive.org/web/20080915190650/http://www.xaprb.com/blog/2006/07/02/innotop-mysql-innodb-monitor/) and [mysqlreport](http://hackmysql.com/mysqlreport) to ensure that all your MySQL caches are functioning at appropriate levels. Also, thanks to a few commenters for letting me know that one of this year’s Google Summer of Code projects is integrating caching into the core WordPress code. It is badly needed.

[php](https://blog.codinghorror.com/tag/php/)
[wordpress](https://blog.codinghorror.com/tag/wordpress/)
[cpu usage](https://blog.codinghorror.com/tag/cpu-usage/)
[web server](https://blog.codinghorror.com/tag/web-server/)
[bug](https://blog.codinghorror.com/tag/bug/)
