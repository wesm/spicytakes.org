---
title: "Questionable Advice: “My boss says we don’t need any engineering managers. Is he right?”"
date: 2024-01-05
url: https://charity.wtf/2024/01/05/questionable-advice-my-boss-says-we-dont-need-any-engineering-managers-is-he-right/
word_count: 2959
---


> I recently joined a startup to run an engineering org of about 40 engineers. My title is VP Engineering. However, I have been having lots of ongoing conflict with the CEO (a former engineer) around whether or not I am allowed to have or hire any dedicated engineering managers. Right now, the engineers are clustered into small teams of 3-4, each of which has a lead engineer — someone who leads the group, but whose primary responsibility is still writing code and shipping product.
> I have headcount to hire more engineers in the coming year, but no managers. My boss says we are a startup and can’t afford such luxuries. It seems *obvious* to me that we need engineering managers, but to him, it seems just as obvious that managers are unnecessary overhead and that all hands should be on deck writing code at our stage.
> I don’t know how to make that argument. It seems so obvious to me that I actually struggle to put it into words or make the case for why we should hire EMs. Help?
> — Unnecessary Overhead(?!?)


Oh boy, there’s a lot to unpack here.


It is unsurprising to me that your CEO does not understand why managers exist, given that he does not seem to understand why organizational structures exist. 🙈 Why is he micromanaging how you are structuring your org or what roles you are allowed to fill? He hired you to do a job, and he’s not letting you do it. He can’t even explain *why* he isn’t letting you do it. This does not bode well.


But I do think it’s an interesting question. So let’s pretend he isn’t holding your ability to do your damn job hostage until you defend yourself to his satisfaction. 😒


I can think of two ways to make the case for engineering managers: one is rather complicated, from first principles, and the other very simple, but perhaps unsatisfying.


I personally have a … vigorous … [knee-jerk response to authority](https://charity.wtf/2022/09/23/the-hierarchy-is-bullshit-and-bad-for-business/); I *hate* being told what to do. It’s only recently that I’ve found my way to an understanding of hierarchy that feels healthy and practical, and that was by looking at it through the lens of systems theory.


### Why does hierarchy exist in organizations?


It makes sense that hierarchy comes with a lot of baggage. Many of us have had bad experience with managers — indeed, entire organizations — where hierarchy was used as a tool of oppression, where people rose up the leadership ranks by hoarding information and playing dominance games, and decisions got made by pulling rank.


Working at a place like that *fucking sucks*. Who wants to invest their creativity and life force into a place that feels like a Dilbert cartoon, knowing how little it will be valued or reciprocated, and that it will slowly but surely get crushed out of you?


But hierarchy is not intrinsically authoritarian. Hierarchy did not originate as a political structure that humans invented for controlling and dominating one another, it is in fact a *property of self-organizing systems*, and it emerges for the benefit of the subsystems. In fact, hierarchy is absolutely critical to the adaptability, resiliency, and scalability of complex systems.


Let’s start with few basic facts about [systems](https://www.amazon.com/Thinking-Systems-Donella-H-Meadows/dp/1603580557), for anyone that may be unfamiliar.


### Hierarchy is a property of self-organizing systems


A **system** is “a network of interdependent components that work together to try to accomplish a common aim” (W. Edward Deming). A pile of sand is not a system, but a car is a system; if you take out its gas tank, the car cannot achieve its aim.


A **subsystem** is a collection of elements with a smaller aim inside a larger system. There can be many levels of subsystems that operate interdependently. The subsystems *always* work to support the needs of the larger system; if the subsystem instead optimizes for its own best interests, the whole system can fail (this is where the term “suboptimize” comes from 😄).


A system is **self-organizing** if it has the ability to make itself more complex, by diversifying, adapting, and improving itself. As systems self-organize and their complexity increases, they tend to generate **hierarchy** — an arrangement of systems and subsystems. In a stable, resilient and efficient system, subsystems can largely take care of themselves, regulate themselves, and serve the needs of the larger system, while the larger system coordinates between subsystems and helps them perform better.


Hierarchy minimizes the costs of coordination and reduces the amount of information that any given part of the system has to keep track of, preventing information overload. Information transfer and relationships within a subsystem are much more dense and have fewer delays than information transfer or relationships between subsystems.


(This should all sound pretty familiar to any software engineer. Modularization, amirite?? 😍)


Applying this definition, we can say that a manager’s job is to coordinate between teams and help their team perform better.


### The false binary of sociotechnical systems


You’ve probably heard this canard: “Engineers do the technical work, managers do the people work.” I hate it. ☺️ I think it misconstrues the fundamental nature of sociotechnical systems. **The “socio” and “technical” of sociotechnical systems are not neatly separable, they are interwoven and interdependent. **There is actually precious little that is *purely* technical work or *purely* people work; there is a metric shitload of [glue work](https://noidea.dog/glue) that draws upon both skill sets.


Consider a very partial list of tasks done by any functional engineering org, besides writing code:

- Recruiting, networking, interviewing, training interviewers, synthesizing feedback, writing job descriptions and career ladders
- Project management for each project or commitment, prioritizing backlog, managing stakeholders and resolving conflicts, estimating size and scope, running retrospectives
- Running team meetings, having 1x1s, giving continuous growth feedback, writing reviews, representing the team’s needs
- Architecture, code review, refactoring; capturing DORA and productivity metrics, managing alert volume to prevent burnout


A lot of this work can be done by engineers, *and often is.* Every company distributes the load somewhat differently. This is a good thing! You don’t WANT an org where this work is only done by managers. You want individual contributors to help co-create the org and have a stake in how it gets run. Almost all of this work would be done more effectively by someone with an engineering background.


So you can understand why someone might hesitate to spend valuable headcount on engineering managers. Why *wouldn’t* you want everyone in engineering to be writing and shipping code as their primary job? Isn’t that by definition the best way to maximize productivity?


Ehhh… 😉


### Engineering managers are a useful abstraction


In theory, you *could* make a list of all the tasks that need to be done to coordinate with other teams and have each item be picked up by a different person. In practice, this is impractical because then everybody would need to know about everything. One of the primary benefits of hierarchy, remember, is to *reduce information overload*. Intra-team communication should be high-bandwidth and fast, inter-team communication should be more sparse.


As the company scales, you can’t expect everybody to know everyone else; we need abstractions in order to function. A manager is the point of contact and representative for their team, and they serve as routers for important information.


> Graph theory: for each of n engineers to be connected ("aligned") w each other you need n(n-1)/2 links, i.e. you need 780 interactions just to keep consistency. Without a few engineering managers (and arks) he is allowing velocity to build up tech debt at blazing speed.— HurtingBrain (@HurtingBrain) [January 5, 2024](https://twitter.com/HurtingBrain/status/1743159594606542963?ref_src=twsrc%5Etfw)


I sometimes imagine managers as the nervous system of the company body, carrying around messages from one limb to another to coordinate actions. Centralizing many or most of these functions into one person lets you take advantage of specialization, as a manager builds relationships and context and improves at their role, and this **massively reduces context switching** for everyone else.


### Manager calendars vs maker calendars


Engineering labor takes concentration and focus. Context switching is expensive, and too many interrupts can be fatal. Management labor consists of context switching every hour or so, and being available for interruptions throughout the day. These are two *very* different modes of being, headspaces, and calendar schedules, and do not coexist well.


In general, you want people to be able to spend most of their time working on things that contribute to the success of the outcomes [they are directly responsible for](https://charity.wtf/2021/03/07/know-your-one-job-and-do-it-first/). Engineers can only do so much glue work before their calendar turns into Swiss cheese and they can no longer deliver on their commitments. Since managers’ calendars are already Swiss cheese, it’s typically less disruptive for them to take on a larger share of glue labor.


It isn’t up to managers to do all the glue work, but it *is* a manager’s job to make sure that **everything that needs to get done, does gets done**. It is a manager’s job to try to line up every engineer with work that is interesting and challenging, but not overwhelming, and to ensure that unpleasant labor gets equitably distributed. It’s also a manager’s job to make sure that if we are asking someone to do a job, they are equipped with the resources they need to succeed at that job. Including time to focus.


### Management is a tool for accountability


When you’re an engineer, you are responsible for the software you develop, deploy, and maintain. When you’re a manager, you are responsible for your team and the organization as a whole.


Management is one way of holding people accountable for specific outcomes (building teams with the right skills, relationships, and processes to make good decisions and build value for the company), and equipping them with the resources (budget, tools, headcount) to achieve those outcomes. If you aren’t making building the organization *someone’s* number one job, it won’t be *anyone’s* number one job, which means it probably won’t get done very well. And whose responsibility will that be, Mr. CEO?


There’s a real upper limit to what you can reasonably expect tech leads, or engineers, or anyone whose **actual job is shipping software** to do in their “spare time”. If you’re trying to hold your *tech leads* responsible for building healthy engineering teams, tools, and processes, you are asking them to do two calendarily incompatible jobs with only one calendar. The likeliest scenario is that they will focus on the outcomes they feel comfortable owning (the technical ones), while you pile up organizational debt in the background.


**In natural hierarchies, we look up for purpose and down for function**. That, in a nutshell, is the more complicated argument for why we need engineering managers.


### Choose Boring technology Culture


The simpler argument is this: *most engineering orgs have engineering managers*. That’s the default. Lots of people much smarter than you or me have spent lots of time thinking and tinkering with org structures over the years, and this is what we’ve got.


As Dan McKinley famously said, we should “[choose boring technology](https://mcfunley.com/choose-boring-technology)“. Boring doesn’t mean bad, it means **the capabilities and failure conditions are well understood**. You only ever get a few innovation tokens, so you should spend those wisely on core differentiators that could make or break your business. [The same goes for culture](https://charity.wtf/2023/05/01/choose-boring-technology-culture/). Do you *really* want to spend one of your tokens on org structure? Why??


For better or for worse, the hierarchical org structure is well understood. There are plenty of people on the job market who are proficient at managing or working with managers, and you can hire them. You can get training, coaching, or read a lot of self-help books. There are various management philosophies you can coalesce around or use to rule people out. On the other hand, the manager-free experiments I’m aware of (e.g. [holacracy](https://en.wikipedia.org/wiki/Holacracy) at Medium and GitHub, or “Choose Your Own Work” at Linden Lab) have all been quietly abandoned or outgrown. Not, in my experience, because leaders went mad for power, but due to chaos, lack of focus, and poor execution.


When there is no explicit structure or hierarchy, the result is not freedom and egalitarianism, it’s “informal, unacknowledged, and unaccountable leadership”, as famously detailed in “[The Tyranny of Structureless](https://en.wikipedia.org/wiki/The_Tyranny_of_Structurelessness)“. In reality, sadly, these teams tend to be chaotic, fragile, and frustrating. I know! I’m pissed too! 😭


This argument doesn’t necessarily prove your CEO is wrong, but I should think his bar for proof is much higher than yours. “I don’t want any of my engineers to stop writing code” is not an argument. But I’m also feeling like I haven’t quite addressed the core question of productivity, so let’s pick that up again once more.


### More lines of code != more productivity


To briefly recap: we were talking about an org with ~40 engineers, broken up into 10 small clusters of 3-4 engineers, each with a tech lead. Your CEO is arguing that you can’t afford to lose any velocity, which he thinks is what would happen if anyone stops writing code full time.


Maybe. But everything I have ever experienced leads me to believe that a fewer number of larger teams, each helmed by an experienced engineering manager, should *way* outperform this gaggle of tiny groups. It’s not even close. And they can do so in a way that’s more efficient, sustainable, and humane than this scrappy death march.


And systems thinking shows us why! With fewer groups, but larger ones, you have less overall management overhead, and *much* less of the slow and costly intra-group coordination. You unlock rich, dense knowledge transfer within groups, which gives you more shared coverage of the surface area. With 7-9 engineers per group you can build a real on call rotation, which means fewer heroics and less burnout. The coordination that you *do* need to do can be more strategic, less tactical, and much more forward-looking.


Would five big teams ship as many lines of code as 10 small teams, even if five engineers become managers and stop writing code? Probably, but who cares? **Your customers give zero fucks** how many lines of code you write. They care about whether you are building the right things and solving problems that matter to them. What matters is moving the business forward, not churning out code. Don’t forget, the act of churning out code creates costs and externalities in and of itself.


What defines your velocity is that you **spend your time on the right things**. Learning to make good decisions about what to build is something every organization has to work out for itself, and it is *always* an ongoing work in progress. Engineering managers don’t do all the work or make all the decisions, but they are *absolutely fucking vital*, in my experience, to ensuring that work happens and is done well. As I wrote in my last piece, [engineering managers are the embodiment of the feedback loops](https://charity.wtf/2023/12/15/why-should-you-or-anyone-become-an-engineering-manager/) that systems use to learn and improve.


### Are managers *ever* unnecessary overhead?


Sure, absolutely. Management is about coordinating between teams and helping teams run more optimally, so anything that decreases your need for coordination also decreases your need for management. If you are a small company, or if you have really senior folks who are used to working together, you need a lot less coordination. The next most relevant factor is probably the rate of change; if you’re growing fast or have a lot of turnover, or if there’s a lot of time pressure or frequent shifts in strategy, your need for managers goes up. But there are plenty of smaller orgs out there that are doing just fine without a lot of formal management.


Look, I’m not a fan of the word “overhead”, because a) it’s kind of rude and b) people who call managers “overhead” are typically people who disrespect or do not value the craft of management.


But management is, in fact, overhead. 😅 So is a lot of other glue work! By which I mean the work is important, but does not itself move the business forward; we should do as much of it as absolutely necessary and* no more*. **The nature of glue work is such that it too-easily expands to consume all available time and space** (and then some). Constraints are good. Feeling a bit underresourced is good, and should be the norm. It is incredibly easy for management to get a bit bloated, and managers can be very loath to acknowledge this, because it’s not like they ever feel any less stressed or stretched.[*]


Management is also very much like operations work in that when it’s being done well, it’s invisible. Evaluating managers can be very hard, especially in the near term, and making decisions about when it’s time to create or pay down organizational debt is a whole nother ball of wax, and way outside the scope of this post.


But yes, managers can *absolutely* be unnecessary overhead.


However, if you have 40 engineers all reporting to one VP, and *nobody else* whose number one job is the outcomes related to people, teams and org, I feel pretty safe in saying this is not a risk for you at this time.


<3 charity


[*] In fact, the reverse can be true; bloated management can create MORE work for managers, and they may counterintuitively feel LESS stretched or stressed with a leaner org chart. Bureaucracies do tend to pick up a momentum all their own. Especially when management gets all wrapped up in promotions and egos. Which is yet another good reason to ensure that [management is not a promotion](https://charity.wtf/2020/09/06/if-management-isnt-a-promotion-then-engineering-isnt-a-demotion/) or a form of domination.
