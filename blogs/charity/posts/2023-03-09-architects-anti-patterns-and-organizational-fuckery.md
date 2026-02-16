---
title: "Architects, Anti-Patterns, and Organizational Fuckery"
date: 2023-03-09
url: https://charity.wtf/2023/03/09/architects-anti-patterns-and-organizational-fuckery/
word_count: 3557
---


I recently wrote a twitter thread on the proper role of architects, or as I put it, tongue-in-cheek-ily, whether or not architect is a “bullshit role”.


> I don't know if this is a troll or not, but with all apologies to my many wonderful, highly skilled "Architect" friends, I tend to think it's a bullshit role. 🙃
> I believe that only the people building software systems get to have opinions on how those systems get built. [https://t.co/aUShYfyIKY](https://t.co/aUShYfyIKY)— Charity Majors (@mipsytipsy) [February 22, 2023](https://twitter.com/mipsytipsy/status/1628295050215182336?ref_src=twsrc%5Etfw)


It got a LOT of reactions (2.5 weeks later, the thread is still going!!), which I would sort into roughly three camps:

1. “OMG this resonates; this matches my experiences working with architects SO MUCH”,
2. “I’m an architect, and you’re not wrong”, and
3. “I’m an architect and I hate you.”


Some of your responses (in all three categories!) were truly excellent and thought-provoking. THANK YOU — I learned a *ton.* I figured I should write up a longer, more readable, somewhat less bombastic version of my original thread, featuring some of my favorite responses.


### Where I’m Coming From


Just to be clear, I don’t hate architects! Many of the most brilliant engineers I have ever met are architects.


Nor do I categorically believe that architects should not exist, *especially* after reading all of your replies. I received some interesting and compelling arguments for the architect role at larger enterprises, and I have no reason to believe they are not true.


Also, please note that I personally have never worked at a company with “architect” as a role. I have also never worked anywhere but Silicon Valley, or at any company larger than Facebook. My experiences are far from universal. I know this.


> Feel like architecture is a leaky abstraction for organizational disfunction.— rocpatel (@rocpatel) [February 22, 2023](https://twitter.com/rocpatel/status/1628430386454839297?ref_src=twsrc%5Etfw)


Let me get suuuuuper specific here about what I’m reacting to:

- When I meet a new “architect”, they tend toward the extremes: either world class and *amazing* or useless and out of touch, with precious little middle ground.
- When I am interviewing someone whose last job title was “architect”, they often come from long tenured positions, and their engineering skills are usually very, very rusty. They often have a lot of detailed expertise about how their last company worked, but not a lot of relevant, up-to-date experience.
- Because of 👆, when I see “architect” on a job ladder, I tend to feel dubious about that org in a way I do not when I see “staff engineer” or “principal engineer” on the ladder.


What I have observed is that **the architect role tends to be the locus of a whole mess of antipatterns and organizational fuckery**. The role itself can also be one that does not set up the people who hold it for a successful career in the long run, if they are not careful. It can be a one-way street to being obsolete.


I think that *a lot* of companies are using some of their best, most brilliant senior engineers as glorified project manager/politicians to paper over a huge amount of organizational dysfunction, while bribing them with money and prestige, and that honestly makes me pretty angry. 😡


But title is not destiny. And if you are feeling mad because none of what I’ve written applies to you, then *I’m not writing about you*! Live long and prosper. 🖖


## Architect Anti-patterns and fuckery


> people sometimes talk about "flattening" an org structure, but they may really just lack efficient/durable cross-tree links (which doesn't require a reorg)! easier said than done of course— d@nny "disc@" mcClanahan (@hipsterelectron) [March 7, 2023](https://twitter.com/hipsterelectron/status/1633011382340943872?ref_src=twsrc%5Etfw)


There is no one right way to structure your org and configure your titles, any more than there is any one right way to architect your systems and deploy your services. And there is an eternal tension between centralization and specialization, in roles as well as in systems.


Most of the pathologies associated with architects seem to flow from one of two originating causes:

1. unbundling decision-making authority from responsibility for results, and
2. design becoming too untethered from execution (the “Frank Gehry” syndrome)


But it’s only when being an architect brings more money and prestige than engineering that these problems really tend to solidify and become entrenched.


### Skin In The Game


> I do agree alot here. You should never stop coding, never stop reviewing, never stop implementing what you design, do not fall in the trap of "just thinking alot", you have to do alot, be there, solve the messy problems, dont expect others will do it, pair with them. [https://t.co/frpn0gMCsX](https://t.co/frpn0gMCsX)— Lucas Coppio (@lscoppio) [February 23, 2023](https://twitter.com/lscoppio/status/1628589524858142720?ref_src=twsrc%5Etfw)


When that happens, you often run into the same fucking problem with architects and devs as we have traditionally seen with devs and ops. Only instead of “No, I can’t be on call or get woken up, my time is far too valuable, too busy writing important software”, the refrain is, “No, I can’t write software or review code, my time is far too valuable, I’m much too busy telling other people how to do their jobs.”


This is also why I think calling the role “architect” instead of “staff engineer” or “principal engineer” may itself be kind of an anti-pattern. A *completely different* title implies that it’s a *completely different job*, when what you really want, at least most of the time, is an engineer performing a slightly different (but substantially overlapping) set of functions as a senior engineer.


> Taleb agrees[https://t.co/oUoeGL9ytO](https://t.co/oUoeGL9ytO)— Mathias Lafeldt (@mlafeldt) [March 6, 2023](https://twitter.com/mlafeldt/status/1632707146314924034?ref_src=twsrc%5Etfw)


My core principle here is simple:** only the people responsible for building software systems get to make decisions about how those systems get built**. I can opine all I want on your architecture or ours, but if I’m not carrying a pager for you, you should probably just smile politely and move along.


Technical decisions should be ultimately be made by the people who have to live with the consequences. But good architects will *listen* to those people, and help co-create architectural decisions that take into account local, domain, and enterprise perspectives (a [Katy Allred](http://twitter.com/themindfulmommy) quote).


### Architecture is a core engineering skill


When you make architecture “someone else’s problem” and scrap the expectation that it is a core skill, you get weaker engineers and worse systems.


Learning to see the forest as well as the trees, and factor in security, maintainability, data integrity and scale, performance, etc is a *critical* part of growing up as an engineer into senior roles.


> "When you make architecture someone else's job and scrap the expectation that it's a core skill, you get weaker engineers & worse systems." - this part resonated with me very much.
> You can also replace "architecture" with "security", "testing" or various others.— C (@_cd83) [March 6, 2023](https://twitter.com/_cd83/status/1632761368997765122?ref_src=twsrc%5Etfw)


The story of QA is relevant here. Once upon a time, every technical company had a QA department to test their code and ensure quality. Software engineers weren’t expected to write tests for their code — that was QA’s job. Eventually we realized that we **wrote better software** when engineers were held responsible for writing their own tests and testing their own code.


Developers howled and complained: they didn’t have time! they would never get anything built! But it gradually became clear that while it may take more time *up front* to write and test code, it saved immensely more time and pain in the longer run because the code got so much better and problems got found so much earlier.


It’s not like we got rid of QA  — QA departments still exist, especially in some industries, but they are more like consulting experts. They write test suites and test software, but more importantly they are a resource to make sure that *everybody* is writing good tests and shipping quality software.


> I think the root problem is too many devs don't THINK in terms of systems architecture.  So many orgs try to "centralize" that function vs. fix the problem of helping devs to think differently & how they integrate.— Jason McIntosh (@mc717990) [February 22, 2023](https://twitter.com/mc717990/status/1628482204027297797?ref_src=twsrc%5Etfw)


This was long enough ago that most people writing code today probably don’t remember this. (It was mostly before my own time as well.) But you hear echoes of the same arguments today when engineers are complaining about having to be on call for their code, or write instrumentation and operate their code in production.


The point is not that every engineer has to *do everything*. It’s that there are elements of testing, operations, and architecture that every software engineer needs to know in order to write quality code — in order to *not* make mistakes that will cost you dearly down the line.


Specialists are not here to do the job for you, they’re to help you **do the job better**.


> When embedded in a team, the architects would write an awful lot of code. But when on the arch team, the role was more about talking to other engineers, reading a lot of code, and generating a lot of diagrams and documentation about the current/future systems as your output.— Pay Tree Arch, Context Dependent (@paytreearch) [March 5, 2023](https://twitter.com/paytreearch/status/1632259051613569025?ref_src=twsrc%5Etfw)


## “Architect” Done Right


> I’ve had various Enterprise Architect roles over the past 15 years. It’s a common role to dunk on, because we’ve historically done a terrible job with enablement. When done well, the role requires constant movement to stay relevant with teams. You can’t only be high level. [https://t.co/LxPTJAU3l5](https://t.co/LxPTJAU3l5)— Kevin Swiber (@kevinswiber) [March 5, 2023](https://twitter.com/kevinswiber/status/1632211716804321283?ref_src=twsrc%5Etfw)


If you must have architects at all, I suggest:

1. Grow your architects from within. The best high-level thinkers are the ones with a thorough grounding in the context and the particulars.
2. Be clear about who gets to have opinions vs who gets to make decisions. Having architects who consult, educate, and support is terrific. Having “pigeon architects” who “swoop and poop” — er, make technical decisions for engineers to implement — is a recipe for resentment and weak architectures.
3. Pay them the same as your staff or principal engineers, not dramatically more. Create an org structure that encourages pendulum swings between (eng, mgr, arch) roles, not one with major barriers in form of pay or level disparities.
4. Consider adopting one of the following patterns, which do a decent job of evading the two main traps we described above.


If your architects don’t have the technical skills, street cred, or time to spend growing baby engineers into great engineers, or mentoring senior engineers in architecture, they are probably also crappy architects. (another [Katy Allred](http://twitter.com/themindfulmommy) quote)


### The “Embedded Architect” (aka Staff+ Engineer)


> "Architecture Astronaut" -- n. Someone with 'architect' in their job title, but who doesn't code.— ./adhddd  # 🍁 (@douglasdd) [February 22, 2023](https://twitter.com/douglasdd/status/1628311019121410051?ref_src=twsrc%5Etfw)


The most reliable way I know to align architecture and engineering goals is for them to be done by the same team. When one team is responsible for designing, developing, maintaining, and operating a service, you tend to have short, tight, feedback loops that let you ship products and iterate swiftly.


Here is one useful measure of your system’s complexity and the overhead involved in making changes:


> “How long does it take you to ship a one-character fix?”


There are many other measures, of course, but this is one of the most important. It gets to the heart of why so many engineers get fed up with working at big companies, where the overhead for change is SO high, and the threshold for having an impact is SO long and laborious.

[https://twitter.com/jetpack/status/1633005928399384576](https://twitter.com/jetpack/status/1633005928399384576)

The more teams have to be involved in designing, reviewing, and making changes, the slower you will grind. People seem to accept this as an inevitability of working in large and complex systems far more than I think they should.


Embedding architecture and operations expertise in every engineering team is a good way to show that these are skills and responsibilities we expect every engineer to develop.


This is the model that Facebook had. It is often paired with,


### The “Architecture Group” of Practicing Engineers


> twitter had a Twitter Architecture Group (TAG) composed of practicing engineers across the co (two of them were on my team). they met once or twice a month and collabed on docs and i thought it was a great way to ensure that people doing the work are the ones making decisions— d@nny "disc@" mcClanahan (@hipsterelectron) [March 5, 2023](https://twitter.com/hipsterelectron/status/1632242505768136705?ref_src=twsrc%5Etfw)


Every company eventually needs a certain amount of standardization and coordination work. Sometimes this means building out a “[Golden Path”](https://charity.wtf/2018/12/02/software-sprawl-the-golden-path-and-scaling-teams-with-agency/) of supported software for the organization. Sometimes this looks like a platform engineering team. Sometimes it looks like capacity planning years worth of hardware requirements across hundreds of teams.


I’ve seen this function fulfilled by super-senior engineers who come together informally to discuss upcoming projects at a very high level. I’ve seen it fulfilled by teams that are spun up by leadership to address a specific problem, then spun down again. I’ve seen it fulfilled by guilds and other formal meetings.


> Although systems design (and thus architecture) are real, I tend to agree with Charity that you shouldn’t be doing it unless you’re also very close to the implementation details. It’s way too easy to miss a critical detail that derails your entire plan otherwise. And not notice.— apenwarr (@apenwarr) [March 5, 2023](https://twitter.com/apenwarr/status/1632462705612271617?ref_src=twsrc%5Etfw)


These conversations *need* to happen, absolutely no question about it. The question is whether it’s some people’s full time job, or one of many part-time roles played by your most senior engineers.


I’m more accustomed to the latter. Pro: it keeps the conversations grounded in reality. Con: engineers don’t have a lot of time to spend interfacing with other groups and doing “project management” or “stakeholder management”, which may be a sizable amount of work at some companies.


### The “architect-engineer” pendulum


> Great topic. Yes and no for me. I definitely grew from within… but I feel like “waves” are needed… You come from deep in the systems/code. You surface use exp to influence and set direction. Then at some point you have to dive deep again.. repeat repeat.— Brian Chambers (@BriChamb) [March 5, 2023](https://twitter.com/BriChamb/status/1632224964278460417?ref_src=twsrc%5Etfw)


The architect-to-engineer pendulum seems like the only strategy short of embedded architects / shared ownership that seems likely to yield consistently good results, in my opinion.


The reasoning behind this is similar to the reasons for saying that [engineering managers](https://charity.wtf/2022/06/13/advice-for-engineering-managers-who-want-to-climb-the-ladder/) should probably spend some time doing hands-on work every few years. You need to be a pretty good engineer before you can be a good engineering manager or a good architect, and 5+ years after doing any hands-on work, you probably aren’t one anymore.


> I’ve done the architect to engineer pendulum as many times as the IC to manager pendulum. There are contexts in which architects are useful (eg integrating 3rd party systems like platforms) - requiring them to code (Musk-style) doesn’t mean they take better design decisions.— Jan Peuker (@janpeuker) [March 5, 2023](https://twitter.com/janpeuker/status/1632194401731739649?ref_src=twsrc%5Etfw)


If you’re the type of architect that is part of an engineering team, partly responsible for a product, shipping code for that product, or on call for that product, this may not apply to you. But if you’re the type of architect that spends little if any time debugging/understanding or building the systems you architect, you should probably make a point of swinging back and forth every few years.


### The “Time-Share Architect”


> Is there precedent in large organizations for Architects with a capital "A" being more of a "Tour of Duty" type role for senior-most engineers, something akin to a really extended "pager rotation"?
> It seems better suited for that vs. a permanent role.— Eric Nograles (@grales) [March 1, 2023](https://twitter.com/grales/status/1630919342303977472?ref_src=twsrc%5Etfw)


This one has aspects of both the “Architecture Working Group” and the “Architect-Engineer Pendulum”. It treats architecture is a job to be done, not a role to be occupied. Thinking of it like a “really extended pager rotation” is an interesting idea.


Somewhat relatedly — at Honeycomb, “lead engineer” is a title attached to a particular project, and refers to a set of actions and responsibilities for that project. It isn’t a title that’s attached to a particular person. Every engineer gets the opportunity to lead projects (if they want to), and everybody gets a break from doing the project management stuff from time to time. The beautiful thing about this is that *everybody* develops key leadership skills, instead of embodying them in a single person.


The important thing is that someone is performing the coordination activities, but the people building the system have final say on architecture decisions.


### The “Advisor Architect”


> I agree with this! I do _some_ coding but mostly I'm product, so I may have suggestions or ask questions about broad architecture/eng choices, but every one comes with a reminder that they can disregard my suggestions entirely. They don't even have to say why.— Michael Snook (@michaelsnook) [March 5, 2023](https://twitter.com/michaelsnook/status/1632264419974713344?ref_src=twsrc%5Etfw)


I honestly have no problem with architects who are not seen as senior to, and do not have opinions overriding those of, the senior engineers who are building and maintaining the system.


Engineers who are making architectural decisions should consult lots of sources and get lots of opinions. If architects provide educated opinions and a high level view of the systems, and the engineers make use of their expertise, well  that’s fan fucking tastic.


If architects are handing them assignments, or overriding their technical decisions and walking off, leaving a mess behind … fuck that shit. That’s the opposite of empowerment and ownership.


> The most effective architecture organization I've ever seen effectively operated as an internal analyst organization.  Think captive Gartner (or Redmonk, ideally), working with senior engineering resources to identify and document internally.— Jonathan Altman (@async_io) [February 22, 2023](https://twitter.com/async_io/status/1628448367872286720?ref_src=twsrc%5Etfw)


The “skin in the game” rule of thumb still holds, though. The less an architect is exposed to the maintenance and operational consequences of decisions, the less sway their opinion should hold with the group. It doesn’t mean it doesn’t bring value. But the limitations of opinions at a distance should be made clear.


## The Threat to Architects’ Careers


It’s super flattering to be told you are just too important, your time is too valuable for you to fritter it away on the mundane acts of debugging and reviewing PRs. (I know! It feels great!!!) But I don’t think it serves you well. Not you, or your team, your company, customers, or the tech itself.


And not *every* architect role falls into this trap. But there’s a definite correlation between orgs that stop calling you “engineers” and orgs that encourage (or outright expect) you to stop engineering at that level. In my experience.


> Am an architect. 100% agree. Your engineering skills begin to degrade and your project management skills grow slowly but weakly.— crozierm (@crozierm) [February 22, 2023](https://twitter.com/crozierm/status/1628394726360743938?ref_src=twsrc%5Etfw)


But your credibility, your expertise, your moral authority to impose costs on the team are all grounded in your fluency and expertise with this codebase and this production system — and your willingness to shoulder those costs alongside them. (All the baby engineers want to grow up to be a principal engineer like this.)


But if you aren’t grounded in the tech, if you don’t share the burden, your direction is going to be received with some (or a LOT of) cynicism and resentment. Your technical work will also be lower quality.


Furthermore, you’re only hurting yourself in the long run. Some of the most useless people I’ve ever met were engineers who were “promoted” to architect many, many years ago, and have barely touched an editor or production shell since. They can’t get a job anywhere else, certainly not with comparable status or pay, and they know it. 🤒


> I get paid to be an architect, and at least half of the architects I work with live in fear that someone will discover they've forgotten how to code, the rest of us are devs that get paid a bit more to sometimes draw a picture.— canihavebiscuit (@canihavebiscuit) [February 23, 2023](https://twitter.com/canihavebiscuit/status/1628738467160285185?ref_src=twsrc%5Etfw)


They may know EVERYTHING about the company where they work, but those aren’t transferable skills. They have become a super highly paid project manager.


And as a result … they often become the** single biggest obstacle to progress**. They are just plain terrified of being automated out of a job. It is frustrating to work with, and heartbreaking to watch. 💔


Don’t become that sad architect. Be an engineer. Own your own code in production. **This is the way**.


### Coda: On “Solutions Architects”


You might note that I didn’t include solutions architects in this thread. There is absolutely a real and vibrant use for architects who advise. The distinction in my mind is: who has the last word, the engineers or the architect? Good engineering teams will seek advice from all kinds of expert sources, be they managers or architects or vendors.


My complaint is only with “architects” who are perceived to be superior to, and are capable of overruling the judgments of, the engineering team.


Exceptions abound; the title is not the person. My observations do not obviate your existence as a skilled technologist.  You obviously know your own role better than I do. 🙃


charity
