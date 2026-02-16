---
title: "Questionable Advice: War Rooms? Really?!?"
date: 2020-09-02
url: https://charity.wtf/2020/09/02/questionable-advice-war-rooms-really/
word_count: 421
---


> My company has recently begun pushing for us to build and staff out what I can only describe as “command centers”. They’re picturing graphs, dashboards…people sitting around watching their monitors all day just to find out which apps or teams are having issues. With your experience in monitoring and observability, and your opinions on teams supporting their own applications…do you think this sounds like a bad idea? What are things to watch out for, or some ways this might all go sideways?
> — Anonymous


Jesus motherfucking Christ on a stick. Is it 1995 where you work? That’s the only way I can try and read this plan like it makes sense.


It’s a giant waste of money and no, it won’t work. This path leads into a death spiral where alarms are going off constantly (yet somehow never actually catching the real problems), people getting burned out, and anyone competent will either a) leave or b) refuse to be on call. Sideways enough for you yet?


Snark aside, there are two foundational flaws with this plan.


1) watching graphs is pointless. *You can automate that shit, remember?*  ✨Computers!✨ Furthermore, this whole monitoring-based approach will only ever help you find the known unknowns, the problems you already know to look for. But most of your actual problems will be [unknown unknowns](https://www.honeycomb.io/blog/observability-whats-in-a-name/), the ones you don’t know about yet.


2) those people watching the graphs… When something goes wrong, what exactly can they do about it? The answer, unfortunately, is “not much”. The only people who can swiftly diagnose and fix complex systems issues are the people who build and maintain those systems, and those people are busy building and maintaining, not watching graphs.


That extra human layer is worse than useless; **it is actively harmful**. By insulating developers from the consequences of their actions, you are concealing from them the information they need to understand the consequences of their actions. You are interfering with the most basic of feedback loops and causing it to malfunction.


The best time to find a bug is as soon as possible after writing it, while it’s all fresh in your head. If you let it fester for days, weeks, or months, it will be exponentially more challenging to find and solve. And the best people to find those bugs are the people who wrote them


Helpful? Hope so. Good luck. And if they implement this anyway — *leave*. You deserve to work for a company that won’t waste your fucking time.


with love, charity.
