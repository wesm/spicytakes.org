---
title: "Coding Horror: Movable Type Since 2004"
date: 2009-07-29
url: https://blog.codinghorror.com/coding-horror-movable-type-since-2004/
slug: coding-horror-movable-type-since-2004
word_count: 748
---

When I [started this blog](https://blog.codinghorror.com/in-the-beginning-there-was-movable-type/), way back in the dark ages of 2004, the best of the options I had was [Movable Type](http://www.movabletype.org/).


![](https://blog.codinghorror.com/content/images/2025/06/image-111.png)


A Perl and MySQL based blogging platform may seem like an odd choice for a Windows-centric developer like me, but I felt it was the best of the available blog solutions at the time, and *clearly* ahead of the .NET blogging solutions.


Sure, I have areas of expertise that I like to stick to, but my attitude has always been to **put religion aside and use what works**, regardless of language or platform. That’s much more of a reality today than it was five years ago. Today, we have embarrassing amounts of CPU power and memory in our servers, and a plethora of good virtualization solutions. Spinning up a Linux virtual machine to solve some problem is no big deal, and we do it every day on Stack Overflow.


In retrospect, my choice of Movable Type was a fortunate one. Although I also use and appreciate [WordPress](http://wordpress.org/), it’s a [bit of a CPU hog](https://blog.codinghorror.com/behold-wordpress-destroyer-of-cpus/). Given the viral highs and lows of my blogging career, there’s no way this modest little server could have survived the onslaught of growth with WordPress. It would have been inexorably crushed under the weight of all those pageviews.


What’s Movable Type’s performance secret? For the longest time – almost 5 years – I used the version I started with, 2.66. That version of Movable Type writes each new blog entry out to disk as a single, static HTML file. In fact, every blog entry you see here is a physical HTML file, served up by IIS just like it would serve up any other HTML file sitting in a folder. It’s lightning fast, and serving up hundreds of thousands of pageviews is no sweat. The one dynamic feature of the page, comments, are handled via a postback CGI which writes the page back to disk as each new comment is added. (This is also the source of the occasional comment disk write collision, when two commenters happen to leave a comment at the same time.) Yes, it’s a little primitive, but it’s also very much in the spirit of KISS: why not do the simplest possible thing that could work?


This static publishing mode precludes glitzy dynamic per-page widgets, but I am a minimalist who [likes his pages austere](https://blog.codinghorror.com/thirteen-blog-cliches/). That restriction suits me fine. The other downside is that a site-wide change requires republishing hundreds or thousands of blog entries. Over time, that can get painful. Modern versions of Movable Type offer both [static and dynamic publishing modes](http://www.movabletype.org/documentation/administrator/publishing/static-and-dynamic-publishing.html), which can give you the best of both worlds.


Movable Type was created by Six Apart. Over the last few years, I’ve had the opportunity to meet [Anil Dash](http://www.dashes.com), who is not only the chief evangelist for and first employee of Six Apart, but also an old-school blogger from way back in 1999. This is a guy who has been through the intertubes a time or two. That’s why I sought out Anil’s advice when we were struggling to come up with a decent name for this crazy website concept Joel Spolsky and I were working on – and it was his excellent advice on naming that eventually guided us to [the name Stack Overflow](https://blog.codinghorror.com/help-name-our-website/).


Anil isn’t just a brilliant blogger and community evangelist, he’s quite influential in his own humble way. And despite his well earned status as a lion of the Web 1.0 blogging era, he’s also willing to go far, *far* out of his way to help a fellow blogger. Anil *personally* helped me drag Coding Horror from the dark ages of 2004-era Movable Type 2.66 to today’s modern Movable Type 4.2x. And by that I mean he logged in himself and did the grunt work to make it happen, including following up with me personally and going through at least two rounds of my crazy demands to make everything as primitive and featureless as I need it to be.


In short, Anil’s a mensch.


So, if you’re considering a blogging platform, I can vouch for not only the Movable Type software, but the Six Apart team, and the community around it.


![](https://blog.codinghorror.com/content/images/2025/06/image-113.png)


In all honesty, [blogging changed my life](https://blog.codinghorror.com/how-to-achieve-ultimate-blog-success-in-one-easy-step/). I’m not sure that’s directly attributable to me choosing Movable Type, exactly, but I *can* give it the highest praise I give any software I’ve used:


**It Just Works.**

[perl](https://blog.codinghorror.com/tag/perl/)
[mysql](https://blog.codinghorror.com/tag/mysql/)
[movable type](https://blog.codinghorror.com/tag/movable-type/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
