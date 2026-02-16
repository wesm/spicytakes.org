---
title: "On Call Shouldn’t Suck: A Guide For Managers"
date: 2020-10-03
url: https://charity.wtf/2020/10/03/on-call-shouldnt-suck-a-guide-for-managers/
word_count: 1203
---


> Maybe I need to write a blog post called "On Call For Managers". If you're asking engineers to be on call for their code — and you should — you owe in return:
> – enough time to fix what's broken
> – hands to do the work
> – closely track how often they are interrupted/woken
> – ..etc
> — Charity Majors (@mipsytipsy) [September 25, 2020](https://twitter.com/mipsytipsy/status/1309604622554640384?ref_src=twsrc%5Etfw)


There are few engineering topics that provoke as much heated commentary as oncall. Everybody has a strong opinion. So let me say straight up that there are few if any absolutes when it comes to doing this well; context is everything. What’s appropriate for a startup may not suit a larger team. Rules are made to be broken.


That said, I do have some feelings on the matter. Especially when it comes to the compact between engineering and management. Which is simply this:


> It is engineering’s responsibility to be on call and own their code. It is management’s responsibility to make sure that** on call *does not suck*.** This is a handshake, it goes both ways, and if you do not hold up your end they should quit and leave you.


As for engineers who write code for 24×7 highly available services, it is a core part of their job is to support those services in production. (There are plenty of software jobs that do not involve building highly available services, for those who are offended by this.) Tossing it off to ops after tests pass is nothing but a thinly veiled form of engineering classism, and you can’t build high-performing systems by breaking up your feedback loops this way.


Someone needs to be responsible for your services in the off-hours. This cannot be an afterthought; it should play a prominent role in your hiring, team structure, and compensation decisions from the very start. These are decisions that define who you are and what you value as a team.


Some advice on how to organize your on call efforts, in no particular order.

- It is easier to keep yourself from falling into an operational pit of doom than it is to claw your way out of one. Make good operational hygiene a priority from the start. Value good, clean, high-level abstractions that allow you to delegate large swaths of your infrastructure and operational burden to third parties who can do it better than you — serverless, AWS, *aaS, etc. Don’t fall into the trap of disrespecting operations engineering labor, it’s the only thing that can save you.
- Invest in good release and deploy tooling. Make this part of your engineering roadmap, not something you find in the couch cushions. Get code into production within minutes after merging, and watch how many of your nightmares melt away or never happen.
- Invest in good instrumentation and observability. Impress upon your engineers that their job is not done when tests pass; it is not done until they have watched users using their code in production. Promote an ownership mentality over the full software life cycle. This is [how dev.to did it.](https://dev.to/molly_struve/making-on-call-not-suck-490)
- Construct your feedback loops thoughtfully. Try to alert the person who made the broken change directly. Never send an alert to someone who isn’t fully equipped and empowered to fix it.
- When an engineer is on call, they are not responsible for normal project work — period. That time is sacred and devoted to fixing things, building tooling, and creating guard-rails to protect people from themselves. If nothing is on fire, the engineer can take the opportunity to fix whatever has been annoying them. Allow for plenty of agency and following one’s curiosity, wherever it may lead, and it will be a special treat.
- Closely track how often your team gets alerted. Take ANY out-of-hours-alert seriously, and prioritize the work to fix it. Night time pages are heart attacks, not diabetes.
- Consider joining the on call rotation yourself! If nothing else, generously pinch hit and be an eager and enthusiastic backup on the regular.
- Reliability work and technical debt are not secondary to product work. Budget them into your roadmap, right alongside your features and fixes. Don’t plan so tightly that you have no flex for the unexpected. Don’t be afraid to push back on product and don’t neglect to sell it to your own bosses. People’s lives are in your hands; this is what you get paid to do.
- Consider making after-hours on call fully-elective. Why not? What is keeping you from it? Fix those things. This is [how Intercom did it](https://www.intercom.com/blog/rapid-response-how-we-developed-an-on-call-team-at-intercom/).
- Depending on your stage and available resources, consider compensating for it.This doesn’t have to be cash, it could be a Friday off the week after every on call rotation. The more established and funded a company you are, the more likely you should do this in order to surface the right incentives up the org chart.
- Once you’ve dug yourself out of firefighting mode, invest in [SLOs](https://www.honeycomb.io/slo/) (Service Level Objectives). SLOs and observability are the mature way to get out of reactive mode and plan your engineering work based on tradeoffs and user impact.


I believe it is thoroughly possible to construct an on call rotation that is 100% opt-in, a badge of pride and accomplishment, something that brings meaning and mastery to people’s engineering roles and ties them emotionally to their users. I believe that being on call is something that you can genuinely look forward to.


But every single company is a unique complex sociotechnical snowflake. Flipping the script on whether on call is a burden or a blessing will require a unique solution, crafted to meet your specific needs and drawing on your specific history. It will require tinkering. It will take maintenance.


Above all: ✨RAISE YOUR STANDARDS✨ for what you expect from yourselves. Your greatest enemy is how easily you accept the status quo, and then make up excuses for why it is necessarily this way. You can do better. I know you can.


> treat every alarm like a heart attack.  _fix_ the motherfucker.
> i do not care if this causes product development to screech to a halt.  amortize it over a slightly longer period of time and it will more than pay for itself. [https://t.co/JSck2u86ff](https://t.co/JSck2u86ff)
> — Charity Majors (@mipsytipsy) [October 14, 2019](https://twitter.com/mipsytipsy/status/1183716460142575616?ref_src=twsrc%5Etfw)


There is lots and lots of prior art out there when it comes to making on call work for you, and you should research it deeply. Watch some talks, read some pieces, talk to some people. But then you’ll have to strike out on your own and *try something*. Cargo-culting someone else’s solution is always the wrong answer.


Any asshole can write some code; owning and tending complex systems for the long run is the hard part. How you choose to shoulder this burden will be a deep reflection of your values and who you are as a team.


And if your on call experience is mandatory and severely life-impacting, and if you don’t take this dead seriously and *fix it* ASAP? I hope your team will leave you, and go find a place that truly values their time and sleep.
