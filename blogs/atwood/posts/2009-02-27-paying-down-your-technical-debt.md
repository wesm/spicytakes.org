---
title: "Paying Down Your Technical Debt"
date: 2009-02-27
url: https://blog.codinghorror.com/paying-down-your-technical-debt/
slug: paying-down-your-technical-debt
word_count: 805
---

Every software project I’ve ever worked on has [accrued technical debt](http://martinfowler.com/bliki/TechnicalDebt.html) over time:


> Technical Debt is a wonderful metaphor [developed by Ward Cunningham](http://www.c2.com/cgi/wiki?TechnicalDebt) to help us think about this problem. In this metaphor, doing things the quick and dirty way sets us up with a technical debt, which is similar to a financial debt. Like a financial debt, the technical debt incurs interest payments, which come in the form of the extra effort that we have to do in future development because of the quick and dirty design choice. We can choose to continue paying the interest, or we can pay down the principal by refactoring the quick and dirty design into the better design. Although it costs to pay down the principal, we gain by reduced interest payments in the future.
> The metaphor also explains why it may be sensible to do the quick and dirty approach. Just as a business incurs some debt to take advantage of a market opportunity developers may incur technical debt to hit an important deadline. The all too common problem is that development organizations let their debt get out of control and spend most of their future development effort paying crippling interest payments.


No matter how talented and smart the software developers, all these tiny deferments begin to add up and cumulatively weigh on the project, dragging it down. My latest project is no different. After six solid months working on the Stack Overflow codebase, this is *exactly* where we are. We’re digging in our heels and retrenching for a major refactoring of our database. We have to **stop working on new features for a while and pay down some of our technical debt**.


![](https://blog.codinghorror.com/content/images/2025/04/image-306.png)


I believe that accruing technical debt is unavoidable on any real software project. Sure, you [refactor as you go](http://c2.com/cgi/wiki?RefactorAsYouGo), and incorporate improvements when you can – but it’s impossible to predict exactly how those key decisions you made early on in the project are going to play out. All you can do is roll with the punches, and budget some time into the schedule to **periodically pay down your technical debt.**


The time you take out of the schedule to make technical debt payments typically doesn’t result in anything the customers or users will see. This can sometimes be hard to justify. In fact, I had to defend our decision with Joel, my business partner. He’d prefer we work on some crazy thing he calls *revenue generation*, whatever that is.


Steve McConnell has a lengthy [blog entry examining technical debt](https://web.archive.org/web/20080119115611/http://blogs.construx.com/blogs/stevemcc/archive/2007/11/01/technical-debt-2.aspx). The perils of not acknowledging your debt are clear:


> One of the important implications of technical debt is that it must be *serviced*, i.e., once you incur a debt there will be interest charges. **If the debt grows large enough, eventually the company will spend more on servicing its debt than it invests in increasing the value of its other assets.** A common example is a legacy code base in which so much work goes into keeping a production system running (i.e., “servicing the debt”) that there is little time left over to add new capabilities to the system. With financial debt, analysts talk about the “debt ratio,” which is equal to total debt divided by total assets. Higher debt ratios are seen as more risky, which seems true for technical debt, too.


Beyond what Steve describes here, I’d also argue that **accumulated technical debt becomes a major disincentive to work on a project.** It’s a collection of small but annoying things that you have to deal with every time you sit down to write code. But it’s exactly these small annoyances, this sand grinding away in the gears of your workday, that eventually causes you to stop enjoying the project. [These small things matter](https://blog.codinghorror.com/revisiting-the-xml-angle-bracket-tax/).


It can be scary to go in and **rebuild a lot of working code that has become crufty over time.** But [don’t succumb to fear](http://en.wikipedia.org/wiki/Bene_Gesserit#Litany_against_fear).


> *I must not fear.*
> Fear is the mind-killer.
> Fear is the little-death that brings total obliteration.
> I will face my fear.
> I will permit it to pass over me and through me.
> And when it has gone past I will turn the inner eye to see its path.
> Where the fear has gone there will be nothing.
> Only I will remain.


When it comes time to pay down your technical debt, [don’t be afraid to break stuff](https://blog.codinghorror.com/dont-be-afraid-to-break-stuff/). It’s liberating, even energizing to tear down code in order to build it up stronger and better than it was before. Be brave, and realize that paying your technical debt every so often is a normal, necessary part of the software development cycle to avert massive interest payments later. After all, [who wants to live forever?](https://blog.codinghorror.com/how-to-stop-sucking-and-be-awesome-instead/)

[software development](https://blog.codinghorror.com/tag/software-development/)
[technical debt](https://blog.codinghorror.com/tag/technical-debt/)
[refactoring](https://blog.codinghorror.com/tag/refactoring/)
[software design](https://blog.codinghorror.com/tag/software-design/)
[development practices](https://blog.codinghorror.com/tag/development-practices/)
