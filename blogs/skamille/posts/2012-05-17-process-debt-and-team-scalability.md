---
title: "Process Debt and Team Scalability"
date: 2012-05-17
url: https://www.elidedbranches.com/2012/05/process-debt-and-team-scalability.html
word_count: 555
---

Most of us in tech spend time thinking about
[technical debt](http://martinfowler.com/bliki/TechnicalDebt.html)
. Whether it's a
[short-term loan or a massive mortgage](http://blog.ircmaxell.com/2012/03/power-of-technical-debt.html)
, we've all seen the benefits and costs of managing and planning a code base with technical debt, and we are generally familiar with ways to identify, measure and eliminate this debt.
What about process debt? Process debt is a lot like technical debt, in that it can be a hack or a lack. The lack of process as debt is pretty easy to see. For example, never bothering to create an automated continuous build for your project. That's a fine piece of process to avoid when you have only one or two developers working on a code base, but as your team grows, your lack of process will start to take its toll in broken code and wasted developer time.
There are also plenty of ugly process hacks. Take for example the problem of a team of varying skill levels, and a code base that is increasingly polluted by poorly formatted, totally unreadable code. When faced with this problem you may be tempted to institute a rule where every line of code must be reviewed by a teammate. Later you discover that the two people with the worst style are reviewing each other, and things still aren't improving enough. So you declare that everyone must have their code reviewed by one of the senior developers that you have appointed. Now you have better style, but at the cost of everyone's productivity, especially your senior developers.
Adding code reviews was the easiest path to take. You just hacked in some process instead of paying up front to think about what the best process would be. But process, once added, is hard to remove. This is especially true for process intended to alleviate risk. Maybe you realize after a few months that the folks with questionable style have learned the ropes, and you remove the rule. But what if you added code reviews not to fix a style problem, but to act as a risk mitigant? I've done this myself in the case of a code base with very little automated testing and a string of bad releases. I'm now paying for my technical debt (a lack of automated testing) by taking out a loan on process.
An easy way to identify process debt is to ask yourself the following question: Will this solution still work when I have twice as many developers? What about ten times as many? A hundred? Process debt, like technical debt, makes scaling very difficult. If every decision requires several meetings and a sign-off, if every git pull is a roll of the dice for your continued productivity, or if you have to hire three project managers for every five developers just to keep track of the task list, you're drowning yourself in process debt.
Developers are
[wary of process](http://teddziuba.com/2011/12/process.html)
because we too often experience process debt of the hack sort. I believe that both a lack of process and an excess of process can cause problems, but if we begin to look at process debt with the same awareness and calculations that we apply to technical debt, we can refactor our playbook the way we refactor our code and end up with something functional, simple, and maybe even elegant.