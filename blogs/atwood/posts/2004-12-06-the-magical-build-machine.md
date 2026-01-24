---
title: "The Magical Build Machine"
date: 2004-12-06
url: https://blog.codinghorror.com/the-magical-build-machine/
slug: the-magical-build-machine
word_count: 612
---

Evidently, Jerry Dennany is a member of [the build machine cult](http://weblogs.asp.net/jdennany/archive/2003/11/26/39938.aspx):

kg-card-begin: html

> *One of the golden rules of modern software development is that one should build all software on a dedicated build machine.*
> A build machine should:
> Be well documented. This includes Version of the Operating System, Service Pack level, HotFixes installed, Tools installed, along with any special installation instructions.
> Be easily reproducible. Anyone on your development team should be able to take the documentation, the build machine, and any required installation media, and recreate that build machine on demand. If you can’t, then you don’t know what exactly is in your product.
> Not contain a single piece of software not related to the build. For example, just because your project uses crystal reports does not mean that you need crystal reports on the build machine.
> Be in an area that is controlled in its access, if at all possible. If this is not possible, then you should control who may log onto the computer.
> Be under change control. No change to the build machine should take place unless that change is documented and approved.
> A few things not to do:
> Never make the build computer a developer’s workstation!
> Never do anything with the build computer except build that version of software. I strongly suggest using a disk image tool such as Ghost to re-image after every build. You don’t get much more of a ‘known state’ than this. This was actually very important in the VB6 / COM world.

kg-card-end: html

While I am all for daily and even [hourly builds](https://blog.codinghorror.com/how-about-an-hourly-build/), I strongly disagree with the perpetuation of the **Magical Build Machine **concept. It’s a bad idea.

- **The magical build machine reinforces the disconnect between developers and users – “us” and “them.”** It runs on my box! Every developer on the team should understand how to produce a reliable build from their own machine. A build that runs on the webserver. A build that runs on the end users’ PC. And if it doesn’t run, they should know how to troubleshoot it. It is every developer’s responsibility to write responsible code, code that doesn’t cause a lot of deployment problems. If you isolate developers from this process, you do so at your own risk.
- **If you use a magical build machine, you’re implying that your project is so complicated to build that it takes special voodoo to get it to run.** Sacrifice a chicken, sprinkle salt over your shoulder, then re-image the build machine when the stars are perfectly aligned. That’s the only way to get a “clean” build! A project that is this difficult to build does not inspire confidence. It also smacks of voodoo programming or programming by coincidence.
- **Using a magical build machine perpetuates the idea that building and deployment is risky and incredibly sensitive to the exact client configuration.** Jerry correctly points out that deployment *was* a big deal in the bad old days of VB6 and COM – aka “dll hell.” On a correctly architected .NET project, this absolutely should not be true! One of the major selling points for .NET is ease of deployment:

1. Is the .NET runtime installed?
2. Xcopy files to a folder.
3. Run your app!


There are absolutely valid reasons to have a **controlled build process**. I’m not proposing that every developer build the project and deploy it at will. Use a build machine if it makes sense for your project, but be careful that you aren’t injecting any accidental “magic” into your development process along the way.

[software development](https://blog.codinghorror.com/tag/software-development/)
[build machine](https://blog.codinghorror.com/tag/build-machine/)
[documentation](https://blog.codinghorror.com/tag/documentation/)
[reproducibility](https://blog.codinghorror.com/tag/reproducibility/)
[software installation](https://blog.codinghorror.com/tag/software-installation/)
