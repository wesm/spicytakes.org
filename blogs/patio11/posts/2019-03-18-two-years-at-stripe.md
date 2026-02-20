---
title: "What Working At Stripe Has Been Like"
date: 2019-03-18
url: https://www.kalzumeus.com/2019/3/18/two-years-at-stripe/
slug: two-years-at-stripe
word_count: 5114
---


I joined [Stripe](https://stripe.com) two years ago to make starting an Internet business easier, mostly by work on [Stripe Atlas](https://stripe.com/atlas). After founding four small software companies I wanted peers to deal with less nonsense, either by productizing a solution to it or by writing up the things I wish I had known back in 2006 when I started. In the same spirit, here’s what I didn’t know prior to joining Stripe.


## What is it you do, anyway?


Stripe’s mission is increasing the GDP of the Internet. Mine is increasing the number of successful software companies on it. That is basically the entirety of the job description. On a day-to-day basis, it’s very Choose Your Own Adventure; I’ve written code, requirements documents, strategy memos, the [Stripe Atlas guides](https://stripe.com/atlas/guides) and advised Stripe employees, partners, and users.


This is… not a straightforward thing to write on a business card.


On the one hand, it gives me huge amounts of latitude to determine my day-to-day direction, and makes use of having a wide skillset. Relatively few people can solo ship an initiative which requires copywriting, React, an ETL pipeline, and a business negotiation; it turns out that is pretty valuable and decreasing the time-to-market of it (versus having to spin up a team of five people to do the same work) is useful.


At the same time, there are reasons why job descriptions exist; they help communicate one’s position to others at the company, clarify discussions about dependency graphs, give decisionmakers a handle when plans are made, etc etc. Being the singleton instance of `Stripe::Atlas::Patio11` is occasionally a mixed blessing.


## What else do you do?


Aside from “continuing to be my usual (hopefully) helpful self on the Internet,” I also try to contribute outside my formal role. One of the things I enjoy most about Stripe’s work culture is the notion that “nothing is Not My Job.” My first real pull request at Stripe was fixing a security bug; I was quite happy to learn that they meant what they had said in spinup about that, and that the Security team spent time getting my code up to scratch even though I looked like “random business (?) guy at the Japan office” in the company directory.


Stripe touches a *massively* large subset of human endeavor (basically, “just the things that involve money”). We operate at a scale which is both tiny relative to commerce on the Internet (which is, itself, nowhere near its asymptote yet) and yet already very material.


Some of my favorite projects have been ruining bad guys’ days. Our users have a lot of money flowing through us daily; every bad guy on the Internet wants it; we are in a constant footrace with all of them. There are a lot of smart people who work all day every day to frustrate them; I have been able to help a time or ten.


One example: we had an internal red-team exercise run as a contest: figure out how to steal All The Money, bonus points if one would probably get away with it. Folks across the company did security research and wrote up their findings; responsible teams then got oodles of high-quality fodder for remediation without us having actually lost a dollar. I won the contest with a few dozen submissions. We closed classes of vulnerabilities as a consequence of this effort.


The various efforts here (security, risk management, etc) benefit quite a bit from understanding what is technically possible, being able to implement it quickly, and having a good mental model for business in the small (“What’s normal behavior for an Internet-based software business?”) and the large (“Where are the weak points in global financial infrastructure, and how do we manage our exposure to them?”).


I also pitch in on (depending on the day) product strategy, writing, company culture building, organizational issues, supporting the Japan team, engineering recruiting, advising Stripe customers (often, very literally, to charge more), etc.


## Why work at Stripe when you could run your own business?


Leverage. [0]


Leverage means things which increase your capability to provide impact. For example, writing code is an extremely leveraged use of your time; you go off to continue living your life but your code keeps running. Some leveraged things I've done are writing, writing software, making businesses which employed people other than me, and joining forces with smart people to work on the problems I seek to solve.


I ran my own businesses for a number of years, including a startup with co-founders, and greatly enjoyed the experience, but I felt like I was maxing out on the challenges available in running small software companies.


It also felt like it was constraining the absolute amount of impact I had for the world. The parts of the job which I enjoyed the most were not my actual job (writing and selling software, filing taxes in a timely fashion, etc) but helping other software entrepreneurs optimize their businesses or engineers navigate career challenges.


[Kevin Kwok](https://twitter.com/kevinakwok) asked “Leverage on what?”. Fifteen years into this career thing I definitely know what my success function for the next thirty is: the product of the number of people I’ve helped in the community I serve (software people, broadly writ) times the delta in the average life that my efforts uniquely caused. If one uses e.g. income as a metric because it’s crunchy enough to keep one honest, then the most effective thing I’ve ever done (by *far* on an ROI-on-time basis) was writing about [salary negotiation for engineers](https://www.kalzumeus.com/2012/01/23/salary-negotiation/). A few hundred folks have emailed me the outcomes they attribute to that essay; this lower-bounds the impact to score of that essay at about 7,000,000 (a year).


Stripe offers a much larger platform to scalably educate and advise entrepreneurs from, and unlike my own companies, it structurally benefits directly from doing that. (There were some indirect benefits to e.g. Bingo Card Creator from me writing a few million words, but Stripe benefits *directly* from every artifact we produce which makes N businesses more successful at the margin. The company-level mission is “Increase the GDP of the Internet”; every time we increase the pace of business formation, the likelihood of business survival, or the rate of business growth, we win.)


A lot of my professional output over the past 12 years has been making businesses ~1% better and repeating that. This was an interesting game to play for Bingo Card Creator, but it was a lot more lucrative when doing it for consulting clients. Stripe’s scale allows some decisions to be *quite leveraged indeed*, both directly and at our customers’ businesses.


(An example which is just a *boggling* fact about the world: what’s your finger-to-a-wind guesstimate about what percentage of credit card payments fail with error code I Don’t Know Sometimes Things Fail In Credit Card Land? Hint: it’s higher than you think. Those failed payments cost conversions at the margin. When Stripe fights that number down by *a basis point*, that creates value across our entire portfolio, forever.)


Stripe’s network is far wider than mine, and where appropriate, I can trade on our organizational karma. This lets me do things which require collaboration from folks who I probably couldn’t just call in my personal capacity. An example: I can probably speculate my fingers off in HN comments about how to pitch an investor, but as a Stripe, I can collaborate directly with YC on optimizing [the advice](https://stripe.com/atlas/guides/pitching) to their partners’ true desiderata in looking at companies.


The amount of time I’ve spent on low-value business administration has declined from about 10~20% of my week (really!) to functionally zero. A surprising portion of running my own businesses was contract negotiation, making sure vendors got paid, and wiring profits in time to make rent. We have people who specialize in all those things so I no longer have to. (I miss getting woken up because a server had… just kidding, I do not miss that at all.)


Leverage has a cost.


One cost is that organizations eventually reach a point where “Just get a bunch of smart people in the room and let them do whatever” ceases to cause spontaneous order and begins to cause chaos. We’re well past that point. This means that we need some sort of planning and managerial processes, and while I interact quirkily with them I do interact materially with them. That interaction is an overhead on personal productivity. It isn’t a small overhead.


The search for leverage also means occasionally having to pick projects other than the ones I’d want to do ceteris paribus. Stripe would probably *let* me just lock myself in a room and write for N years, but that would likely greatly underperform the theoretical limit on impact, so I sometimes end up doing work which is more pressing for the company but less personally fulfilling.


Do I occasionally miss doing my own thing? Yep, on at least a monthly basis, most particularly when working with entrepreneurs directly. I don’t have nearly the bandwidth to prototype anything material but I feel the siren call of it; I’m pretty sure my next adventure will be running a software business again.


I *definitely* feel as if being at Stripe has increased my aspirations with regards to that next business. Partly this is via exposure to a wide variety of companies in the ecosystem; entrepreneurs’ creativity never ceases to amaze me. (All else being equal, *definitely* choose a customer base whose creative use of what you build will surprise and delight you.) I’ve also had some time to crawl around the ducts of Internet commerce, which is a beautiful fractal described by an equation capable of summoning horrors from beyond spacetime.


Probably the single biggest change in belief I’ve had since joining is that ambition properly harnessed can be an enormously productive force in the world. This is largely informed by working with people who are extremely ambitious and yet well-grounded, both at Stripe and at our customers. There is a great, great difference between “Build a credit card processor? That’s *impossible*.” and “Build a credit card processor? That probably involves compliance with an enumerable set of regulations and writing a finite number of lines of code.” You want more people in your life who say the second version, probably at most margins.


Relatedly, I think I agree with Tyler Cowen that [raising others’ aspirations](https://marginalrevolution.com/marginalrevolution/2018/10/high-return-activity-raising-others-aspirations.html) is an effective way to increase productivity.


One way that Silicon Valley does this at scale is creating a space in the culture for being just a little bit wild-eyed when envisioning potential impact and then, this is important, actually shipping tractable engineering artifacts against the vision.


This is often poked fun of when it is deployed in the service of ends people view as unserious or when done by folks who confabulate. I have probably made jokes like that before. I think I have come to regret them, because they’re *also* heard by people with serious goals who are scrupulous. The jokes, and the broader culture, discourage those people from trying extraordinarily ambitious things.


If I got a do-over on e.g. running my own businesses for a decade, I’d probably skip the relatively unambitious first two (which I did just because I knew I could probably do them) and proceed directly to trying things outside of my comfort zone. (I still have an enormous love in my heart for the aesthetics of small software businesses, but given a do-over, could have done much more interesting and impactful small software businesses earlier than I actually did.)


One can simultaneously hold two thoughts at once: that unserious ends and lies are not positive, but that we probably underestimate the number of teams doing very important work in a startup-y fashion. They’re on-paper unqualified, they are often running on a shoestring, they don’t look like who Hollywood would cast as Obviously Important Person, and yet they *often outperform anyway*. One of the best parts of my job is getting to help folks like this build their businesses.


That’s probably the single biggest revelation to me 15 years into my career, so, throwing it back in a bottle for any of y’all who are getting started. We might not have time travel yet, but the Internet is the next best thing.


## Being a senior individual contributor


Somewhat surprisingly to some folks who know me externally, I am not a manager (of Stripe Atlas or anything else). I’m an IC (“individual contributor”, a bit of widely-used jargon at companies large enough to have career tracks).


Early in their careers, ICs mostly create value by doing “the work.” In one’s first year of e.g. being an IC engineer, you write code backing projects of varying complexity.


As one increases up the skill curve, ICs continue doing “the work” while also spending an increasing amount of time on non-managerial metawork, like contributing in a directed fashion to the organizational culture, setting strategic directions, mentoring others (including managers), setting up systems and processes by which the work will be done in the future, etc.


Stripe has an explicit career path available to ICs in engineering and elsewhere. It is designed to avoid the relatively industry common failure mode that, as one advances in one’s career, one either has to start doing management or compromise quite a bit on career impact and outcomes. Management is a useful professional specialization but you probably shouldn’t do it if other specializations are more highly leveraged uses of your time.


One of the great sources of leverage is other people. You can get leverage via directing folks to do things (a superpower whose impact I probably underappreciated when running my business solo). You can also get it by making them more effective at doing things.


When I work with folks at Stripe, I try to make them more instrumentally effective at working the organization, at understanding the broader business context for individual units of work, at understanding the startup ecosystem and the mindset and challenges of our users, etc. For folks in particularly focused roles, I try to put in place efforts to make them better at the core content of their jobs.


For example, I write a lot at Stripe, but Stripe now has a number of people for whom that statement is true. I could plausibly ship X00,000 words in a year, but one eventually hits a plateau there; there is no plateau if the shippable thing is making other writers more instrumentally effective. This sometimes come from directly editing work but more often from teaching, sometimes about the craft of writing specifically and sometimes more Stripe-specific nuances like how to reproduce the company voice. (I also wrote a non-trivial amount of code because, fun fact, stripe.com spells CMS e-r-b, which didn’t optimize for writers’ ability to ship new words.)


My colleague Julia Evans has an essay on [being a senior engineer](https://jvns.ca/blog/senior-engineer/) which discusses being a senior IC in a lot of detail specific to engineers.


(Sidenote: One way to substantial impact as a senior IC is providing an example of what senior IC-ship looks like for folks growing in their careers to aspire to; another is working with people explicitly to accelerate their growth towards it and beyond.)


## Writing, writing, writing


Stripe is a celebration of the written word which happens to be incorporated in the state of Delaware.


We produce prodigious amounts of it internally, most of it widely visible within the company. My favorite job perk might be that library; it includes everything from a crackling memo about current state of book publishing (relevant to [our interests](https://press.stripe.com)) to experiment writeups about using machine learning to counter credit card fraud (relevant to [our interests](https://stripe.com/radar)) to market analyses of SaaS adoption in Japanese businesses (relevant to [our interests](https://stripe.com/billing)).


I expected to write a shedload at Stripe, and I do. I didn’t expect most of it to be internally facing. Example: we have a lot more people at Stripe who need to know how to reason about a SaaS business than who have run SaaS businesses, so I locked myself in a room and data dumped about what I had learned in ten years. (We eventually published a [publicly available version](https://stripe.com/atlas/guides/business-of-saas).)


I think I once had the typical engineer’s disdain for Strategy Memos (TM), but if you think of it as less a Strategy Memo (TM) and more a pull request for a very complicated program which directs the activities of dozens or hundreds of people, it gets a lot easier to stomach.


I recently wrote about where Stripe is in Japan right now, what it would take for Stripe to be as impactful to the Japanese Internet as it has been to the US Internet, and what concrete steps we should take in 2019 to get us closer to that goal. It’s low-degree wild to me that I have something useful to contribute there, but one of the things the company does rather well is being a distributed responsibility machine. Working at BigCo counsels you that there is some expert in another castle who has already written the marching orders and all you have to do is execute your tiny assigned portion of them. At Stripe, you can order the metaphorical [pizza](https://www.google.com/search?q=google+bezos+two+pizza+rule) and say “Good news: Stripe does have smart people working on the go-to-market plan for the world’s third largest economy. We just bought them a single large pizza.”


One could certainly write the Strategy Memo equivalent of bikeshedding on indentation rules. Try not to do that or to work with people who enjoy doing that.


An aside about indentation rules: the right way to do all stylistic arguments is to enforce them with code, and make the *sole* supported interface for stylistic arguments pull requests against the linter/compiler rather than comments on individual engineers’ work. `go fmt` might be the single best feature of Golang for this reason.


At Stripe, there are a lot of things which are valid Ruby which are nonetheless illegal. A trivial example would be a `@improper_casing_for_ruby`. A more meaningful example would be calling into another team’s code from outside a defined boundary. Since a linter catches essentially all of those, if one finds oneself nitpicking a pull request, one should generally either a) fix the linter or b) find something productive to do with one’s time.


This is one of many, many ways that considered use of technology helps to ameliorate human problems. One of the joys of working in a tech company is that they seem to have a comparative advantage on grokking this, and on self-modifying tools to more closely fit the desired way they want to work. This is one reason I expect 2019’s employment of engineers to be the lowest number for the rest of time: every organization which cares about the social reality of work would benefit from being able to compose their own tools. (That feels like a contentious claim, but it isn’t socially contentious to say that basically every organization considers leadership to be too critical to outsource, and leadership is just programming for organizations.)


## Being (very) remote


Stripe is expanding [internationally](https://stripe.com/global) rapidly, but most folks who I interact with on a day-to-day basis are in San Francisco. This is occasionally challenging.


In my eagerness to please, for my first year, I did not establish great boundaries around e.g. acceptable meeting times, and ended up taking a lot at, say, [11 AM PST](https://everytimezone.com/zones/009e62fa). After pulling out quite a bit of hair around my sleep schedule, I eventually blocked off my sleeping hours on my calendar; this was a major improvement in quality of life. These days I get up early (7 AM, generally) to have meetings, take a hard break to spend time with my kids before school, and then head into the office.


Folks ask me about work/life balance a lot. I (candidly) worry that I don’t always set a great example for my team or the office on this; I have periods which are quite crunchy interspersed by lulls, and even at a shop which doesn’t count hours or reward facetime-for-the-sake-of-facetime I find myself falling back into salaryman mode too frequently. I’m happy to report that folks who are better about self-discipline and maintaining boundaries do successfully do so at Stripe, and generally without sacrificing actual or perceived effectiveness.


I also think, particularly as companies mature, that they should generally evolve organizational alchemy to get greater-than-sum-of-the-parts effectiveness out of people with disparate working styles, in the same way that [businesses unite investors with differing tolerances for risk](https://www.bloomberg.com/opinion/articles/2019-02-13/santander-didn-t-pay-its-non-debt) to bankroll common enterprise that no tolerance level could fully fund by itself.


Here’s a question reasonable people can disagree on: is it OK to routinely have meetings at e.g. 7 PM? (I’m sympathetic to “Oh heck no” on this question, but note that if you want to support traditionally managed Japanese businesses that that won’t be a maximally effective response, and there are many other plausible reasons for someone to say, given their goals, values, and personal situation, “Actually, 7 PM meetings sound pretty reasonable to me. It’s not a crazy ask like e.g. showing up in an office at 9 AM, who does that.”)


If you have four people at your company, you probably need *almost total agreement* on whether 7 PM meetings are a routine expectation. If you have 400, you can probably tolerate groups/roles/individuals/etc ending up at different equilibria on this question. Save your limited Total Agreement Mandatory points for the key differentiating values of your culture. (Stripe describes its organizational culture to candidates with [this document](https://stripe.com/us/jobs/candidate-info).)


I fly to HQ about once a quarter, mostly to “meet old friends and make new ones.” It’s simultaneously incredibly useful and a bit jarring to, every single time, be in a lunchroom which has hundreds of people who were not there the last time I was in the lunchroom. Hypergrowth is a through-the-looking-glass sort of experience, particularly when you perceive it in slices.


Shoutout to my team, which is the most supportive one I’ve ever been on. We added a number of new remote engineers recently, and the entire team worked from home for a week to understand the experience better and capture requirements for improving our communication norms.


For a company which seems tied to email and Slack at all working hours, it’s useful to understand that a lot of information is distributed around the lunch table and decisions get made in hallway conversations, neither of which is great for folks who can only perceive HQ through the Internet. A tiny thing someone built recently which I really love for helping on this: if you schedule a meeting between Stripes, a video conference link gets automatically added to the meeting, so that any remote employee who might need it doesn’t need to feel like they’re constantly having to interrupt meetings to remind someone to turn on the camera and distribute the link to the remotes.


We are rather aggressively expanding the cohort of remote Stripes, driven partly by improved technologies for collaboration (Zoom, Google Docs, etc), partly by happy experiences on many teams which experimented with adding remotes, partly by desire to attract and retain talented folks wherever they may be, and partly by desire to be more local to our customers, who are very widely distributed.


## Fast and slow


For obvious reasons, I can’t tell you Stripe’s growth rate for anything, but let’s talk about a stylized company called 2X, Inc., where every graph is growing at 2X per year.


Working at 2X breaks so many intuitive understandings of how the world should work.


The day you start at 2X, half of your coworkers have less than 1 year of experience. A year later, when you’re starting to get your sea legs, half of your coworkers have less than 1 year of experience. A year later, when senior colleagues start forgetting that you were not actually there during the flood, half of your coworkers have less than 1 year of experience.


You get numb to graphs after a while. Numbers flit in one ear and out the other; retaining any is almost pointless, because by the time one sinks into your consciousness it will not merely be wrong but glaringly wrong. 2X doubles every year and everyone laughs about how the planning department got it right again; it’s eerie.


It’s exhilarating and terrifying all at once, because almost nothing in nature grows at 2X a year over sustained periods. 2X is constantly on the lookout for new opportunities to sustain the growth, but simultaneous with the hunt is the challenge of doing anything meaningful with *that graph* as a backdrop.


Stripe isn’t 2X, Inc., but occasionally has some challenges that this stylized company has.


You have to write dashboards and memos for people who *aren’t at the company yet*; most users of the artifact aren’t. You’ve got to stick up your hand in meetings and say “Hey, you just said ‘sales funnel’: can you give me the maximally pedantic explanation of what that means.” (This is a good thing for senior folks to ask, because forcing folks who joined last week to interrupt to ask a basic question doesn’t set them up for comfort or success.) You have to employ professional educators (and eventually historians and anthropologists, for real), because you effectively run a postgraduate study program on the scale of a small university.


You have to constantly course correct your understanding of what is material impact, because hopefully you’re searching for making material impact, and things that were material three years ago might not move the needle anymore. And things that were *outlandishly* impossible three years ago might now be quite possible, and worth doing, but only if you can get to them in the next six months.


You have to keep the culture to fight like hell for the expansive set of things which are very worth doing but which don’t obviously move needles. One reason I fly to [MicroConf](https://www.microconf.com) every year is to make sure we meet people who are hitting their first month of $1, $1k, or $10k worth of revenue and *thoroughly* understand what they need from us. We should not just prevent degradation of the experience for them but make it transformatively better than 5 years ago.


## Creating things which matter


As a long-time user of Stripe, as soon as I got git access, I went spelunking for where the magic behind the product pages lived. (If you’re not familiar at this: Stripe has a mostly deserved reputation for giving new product pages very well-designed treatments. Here’s [one](https://stripe.com/us/billing) for general reference.)


Spoiler alert: There is shockingly little magic, on that topic or anywhere else. The landing pages are an ERB file which starts out blank. It spits out HTML (and some CSS and Javascript), the same as every other page on the Internet. The reason those pages are phenomenal is that a very small group of very talented people care an almost unreasonable amount that they are phenomenal.


The route to great work is mostly a) hire small teams of very talented people who very intently care about something and b) incentivize great work amongst numerous other competing worthy priorities.


People often phrase that as “Protect teams doing great work”, but I don’t think that is entirely correct. Mediocrity doesn’t happen because a villain kills good work then cackles maniacally. BigCo doesn’t set out to be mediocre… BigCo just has an awful lot of people with an awful lot on their plate, and many of them are incentivized to make locally-optimal decisions at the expense of competing global goals.


Doing organizational design and incentive structuring to solve the principal/agent problem internally and cause people to optimize for the global outcome at scale may be the hardest unsolved problem. (In management? In capitalism? In anything? Take your pick.) We’re working on it; concretely, it often involves making space for folks to say “What does the *best possible* version of this project look like?” and being OK with e.g. delaying things until they are ready. (Note the implicit tension with doing that while one’s business and the environment are moving at Warp 7. None of the problems are easy, or there wouldn’t be any need to have smart people work on them.)


The founder in me thinks that a bit of experience in a large (or growing) organization is very useful for correcting one’s worldview and ability to anticipate the actions of future customers, counterparties, partners, etc at large organizations. That is a useful ability to have as a founder, and (somewhat surprisingly) we spend very little time at school teaching how large organizations actually make decisions.


There are e.g. civics classes which can teach you the orthodox understanding of the [legislative process](https://www.youtube.com/watch?v=tyeJ55o3El0), but it glosses over really important details to the real world, like e.g. how the regulated directly engage with their regulators to shape future legislation. I similarly think that no class about management or capitalism I’ve ever been in said “Sometimes the reason for an outrageous result isn’t a principal/agent problem or ‘Maximize the evil’ or incompetence, it is that writing a dashboard which would have surfaced the problem in time to fix it was beyond the SQL capabilities of the most directly responsible individual.”


Speaking of SQL, I love our internal tooling. We have a number of engineers specifically dedicated to it; I think we could probably tolerate having five times as many as we do. Some of the things they’ve built that clearly would have helped every software company I’ve ever worked at: an easy way to automate (and thereby secure) somebody-needed-to-pop-open-a-console style tasks, [instant code search over the entire codebase](https://github.com/livegrep/livegrep), and a way to subscribe oneself for daily emails about state changes to a certain set of objects (e.g. “For all the accounts I manage, email me the list of any who hit $MILESTONE every morning, so I can reach out to congratulate them.”) One of the reasons I love our tooling is that there is an engineering-driven emphasis on composability, such that each additional tool we add makes wide swathes of our tooling (and operations) more valuable, often in unanticipated ways. I cannot bang the drum enough for investing in internal tooling.


## I’d love to chat more about this


If you’re interested in hearing more about how the sausage gets made at scale, we’d love to chat. We’re in the usual places on the Internet.


[Stripe is hiring](https://stripe.com/jobs). I like it here. If you think you would too, or are curious about figuring out whether that would be true, please find us on the Internet.
