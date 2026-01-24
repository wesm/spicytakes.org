---
title: "Why Can’t Microsoft Ship Open Source Software?"
date: 2008-07-02
url: https://blog.codinghorror.com/why-cant-microsoft-ship-open-source-software/
slug: why-cant-microsoft-ship-open-source-software
word_count: 1143
---

In [Codeplex wastes six months reinventing wheels](http://ryepup.unwashedmeme.com/blog/2007/03/27/codeplex-wastes-six-months-reinventing-wheels/), Ryan Davis has a bone to pick with Microsoft:


> I saw an announcement [in March, 2007] that CodePlex, Microsoft’s version of Sourceforge, has [released a source control client](https://web.archive.org/web/20080604022450/http://blogs.msdn.com/codeplex/archive/2007/03/26/announcing-the-codeplex-source-control-client.aspx).
> This *infuriates* me. This cool thing they spent six months (six!) writing is called Subversion, and it had a 1.0.0 release [in early 2004]. Subversion had its first beta in late 2003, so the Codeplex folks are waaay behind the state of the art on this one.
> As a whole, I think the state of software is abysmal. The only way to make it better is to **stop writing new code**. New code is always full of bugs, and its an expensive path to get from blank screen to stable program. We need to treat programming more like math, we need to build on our results. Development tools is a special market, as our needs are all very similar, and when we need a tool, we have the skills to make it.


It’s a great rant – you should read the whole thing – but I’m not sure I entirely agree.


While I do empathize with the overall sentiment that Ryan is expressing here, I also found myself nodding along with Addy Santo, who left this comment:


> Author seems to think that all software development is done in basements and dorms. The reality is that software is an industry like any other - and follows the same simple rules of economics. How many brands of sports shoes are there? How many different MP3 players? Flavors of toothpaste ? If you can walk down the soft drink isle and not be “infuriated” by Vanilla Cherry Diet Doctor Pepper then you might just be a hypocrite.


So if you think Microsoft’s particular flavor of source control is redundant, **you’ll *really* hate Diet Cherry Chocolate Dr. Pepper**.


![](https://blog.codinghorror.com/content/images/2025/04/image-165.png)


(I am now required by law to link Tay Zonday’s [Cherry Chocolate Rain](http://www.youtube.com/watch?v=2x2W12A8Qow) video. My apologies in advance. And if that makes no sense to you, [see here](http://en.wikipedia.org/wiki/Chocolate_Rain).)


Are there meaningful differences between Microsoft’s Team Foundation flavor of version control and Subversion? The short answer is that there aren’t – **if all you’re looking for is a carbonated beverage**. If all you require is run of the mill, basic centralized source control duties, they’re basically the same product. So why not go with the free one?


But Team Foundation is much more than just source control. Of course there are open source equivalents to much of the functionality offered in Team System, as Ryan is quick to point out.


> The Codeplex staff stated they needed to write their own client in order to integrate with the TFS server infrastructure. According to an MSDN article ([Get All Your Devs In A Row With Visual Studio 2005 Team System](https://web.archive.org/web/20090218033824/http://msdn.microsoft.com/en-us/magazine/cc163686.aspx)), TFS seems to be a complicated tool to help manage your developers. Reading the description, TFS is an issue tracker, unit tester, continuous integration, source control system, and Visual Studio plugin. So, basically a combination of [Trac](http://trac.edgewall.org/), [NUnit](http://www.nunit.org/), [CruiseControl.NET](http://cruisecontrol.sourceforge.net./), Subversion, and a Visual Studio plugin. Why not just write the Visual Studio plugin, and hook into the tools people are already using? All those tools have rich plugin-architectures that would probably support any sensible addition you’d want to make.


The answer, of course, is that Microsoft does all that painful integration work for you – at a price.


If you have the time to look closer, you’ll find more flavorful differences between Subversion and TFS source control. Differences more akin to, say, Dr. Pepper and Mr. Pibb.


![](https://blog.codinghorror.com/content/images/2025/04/image-164.png)


I’m not going to enumerate all the subtle and not-so-subtle differences between the two here; picking a fight between two modern centralized version control systems is not my goal. They’re both great. Choose whatever modern source control system you prefer, and take the time to [learn it in depth](http://www.ericsink.com/scm/source_control.html). Source control is the [bedrock of modern software engineering](https://blog.codinghorror.com/source-control-anything-but-sourcesafe/), and I’ve found precious few developers that truly understand how it works. All that time we were going to spend arguing whether your source control system can beat up my source control system? I’ve got a radical idea: let’s spend it on *learning the damn stuff* instead.


Still, there is a much deeper, more endemic problem here that Ryan alludes to, and it deserves to be addressed.


One of Microsoft’s biggest challenges in the last few years has been that **its competitors are free to ship what are, by now, fairly mature open source components as parts of their operating systems.** When was the last time you ever saw any open source *anything* shipping in a Microsoft product? On some deep, dark corporate level, Microsoft must feel compelled to rewrite everything to completely own the source code. Sometimes – a more cynical person might say “often” – this results in poor quality copies instead of actual innovation, such as Microsoft’s much-maligned MSTest unit test framework. It’s a clone of [NUnit](http://www.nunit.org) with all new bugs and no new features, but it *can* be included in the box with Visual Studio and integrated into the product. It’s a one step forward, two steps back sort of affair.


Everybody I know – including our own Stack Overflow team – who has tried to use the MSTest flavor of unit tests has **eventually thrown up their arms and gone back to NUnit**. It’s just too painful; the commercial clone lacks the simplicity, power, and community support of the original open source version. There’s simply no *reason* for MSTest to exist except to satisfy some bizarre corporate directive that Microsoft never ship open source code in their products. Furthermore, this blind spot hampers obvious integration points. Microsoft could build first-class integration points for NUnit into Visual Studio. But they haven’t, and probably never will, because so much effort is poured into maintaining the second-rate MSTest clone.


In fact, the more I think about this, the more I think Microsoft’s utter inability to integrate open source software *of any kind whatsoever* into their products **might just end up killing them**. It’s a huge problem, and it’s only going to get worse over time. Open source seems to evolve according to a different power law than commercial software. If I worked in the upper echelons of Microsoft, I’d be looking at the graph of open source software growth from the years of 1999 to 2008 and crapping my pants right about now.


It’s a shame, because the best way to “beat” open source is to join ’em – to integrate with and ship open source components as a part of your product. Unfortunately, that’s the one route that Microsoft seems hell bent on never following.

kg-card-begin: html

Update: For background, do read Jon Galloway’s explanation: [Why Microsoft Can’t Ship Open Source Code](http://weblogs.asp.net/jgalloway/archive/2007/05/02/why-microsoft-can-t-ship-open-source-code.aspx).

kg-card-end: html
[open source](https://blog.codinghorror.com/tag/open-source/)
[microsoft](https://blog.codinghorror.com/tag/microsoft/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[source control](https://blog.codinghorror.com/tag/source-control/)
[codeplex](https://blog.codinghorror.com/tag/codeplex/)
