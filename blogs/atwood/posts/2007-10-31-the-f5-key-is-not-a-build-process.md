---
title: "The F5 Key Is Not a Build Process"
date: 2007-10-31
url: https://blog.codinghorror.com/the-f5-key-is-not-a-build-process/
slug: the-f5-key-is-not-a-build-process
word_count: 701
---

Hacknot’s [If They Come, How Will They Build It?](http://web.archive.org/web/20071013071537/http:/www.hacknot.info/hacknot/action/showEntry?eid=97) is a harrowing series of 29 emails sent over a two week period.


> **To: Mike Cooper
> From: Ed Johnson**
> Mike,
> I finally got CVS access today from Arnold. So I’ve checked out the AccountView module OK, but it won’t compile. The Eclipse project has dependencies on about five other projects. I tried checking those dependent projects out as well, but a few of them won’t build at all? How are you managing to develop this thing when the dependent projects don’t build?
> Ed
> **From: Mike Cooper** **To: Ed Johnson**
> Oh yeah - I forgot to tell you about the dependent projects. I always forget about them. I’m not so surprised some of them don’t build for you. I’ve got versions on my machine that build OK but I haven’t checked them in for a while. Gimme about 15 minutes and I’ll check them in, then you should be right to go.
> M.


It’s a cautionary tale about a serious software project pathology: the pain of getting a new developer up and running on an existing software project. It’s startlingly common.


This points us to one of the most important health metrics on a software development project. **How long does it take for you to get a new team member working productively on your project?** If the answer is more than one day, *you have a problem*. Specifically, you don’t have a proper build process in place.


I’ve talked before about [the importance of a build server](https://blog.codinghorror.com/the-build-server-your-projects-heart-monitor/) as the heartbeat for your project. A sane software development project has automatic daily builds, performed on a neutral build server. If your team is in the habit of producing those kind of daily builds, it’s difficult to accumulate the [deep technical debt](https://web.archive.org/web/20071102163417/http://blogs.construx.com/blogs/stevemcc/archive/2007/11/01/technical-debt-2.aspx) enumerated in all those emails. If the build server can do it, so can your newly hired coworkers.


But based on the development practices I’ve often seen on site with customers, I think setting up a build server might be an unrealistic goal, at least initially. It might not get done. We should shoot for a more modest goal to start with.


![visual-studio-debug-menu](https://blog.codinghorror.com/content/images/uploads/2007/10/6a0120a85dcdae970b0120a86da094970b-pi.png)


Here’s how most clients I work with build a project:

1. Open the IDE
2. Load the solution
3. Get latest
4. Press F5 (or CTRL+SHIFT+B)


**If your “build process” is the F5 key, *you have a problem*.** If you think this sounds ridiculous – *who would possibly use their IDE as a substitute for a proper build process?* – then I humbly suggest that you haven’t worked much in the mainstream corporate development world. The very idea of a build script outside the IDE is alien to most of these teams.


**Get your build process out of the IDE and into a build script**. That’s the first step on the road to build enlightenment.


The value of a build script is manifold. Once you have a build script together, you’ve **created a form of living documentation**: here’s how you build this crazy thing. And naturally this artifact is checked into source control, right alongside the files necessary to build it (and even the [database necessary to run it](https://blog.codinghorror.com/is-your-database-under-version-control/), too). From there, you can begin to think about having that script run on a neutral build server to avoid the [“Works On My Machine” syndrome](https://blog.codinghorror.com/the-works-on-my-machine-certification-program/). You can also consider all the nifty ways you could enhance the script with stuff like [BATs, BVTs, and Functional Tests](https://web.archive.org/web/20071126110522/http://blogs.msdn.com/steverowe/archive/2007/10/25/testing-a-daily-build.aspx). Your build server can become [the heartbeat of your project](https://blog.codinghorror.com/the-build-server-your-projects-heart-monitor/). There’s no upper limit on how clever you can be, and how many different build scripts you can come up with. Build scripts can be incredibly powerful – but you'll never know until you start using them.


**The F5 key is not a build process**. It’s a quick and dirty substitute. If that’s how you build your software, I regret that I have to be the one to tell you this, but *your project is not based on solid software engineering practices*.


So, if you don’t have a build script on your project, what are you waiting for?

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[software dependencies](https://blog.codinghorror.com/tag/software-dependencies/)
[software project management](https://blog.codinghorror.com/tag/software-project-management/)
