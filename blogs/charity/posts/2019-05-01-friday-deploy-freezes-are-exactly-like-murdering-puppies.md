---
title: "Friday Deploy Freezes Are Exactly Like Murdering Puppies"
date: 2019-05-01
url: https://charity.wtf/2019/05/01/friday-deploy-freezes-are-exactly-like-murdering-puppies/
word_count: 2382
---


**VOICEOVER**: “Previously, on twitter …”


> Happy Friday
> |￣￣￣￣￣￣￣￣￣￣￣|
>               Don't push 
>             to production       
> |＿＿＿＿＿＿＿＿＿＿＿| 
>              (___/)  ||
>             (⌾ㅅ⌾)  ||
>            / 　    づ
> — Kelly Vaughn (@kvlly) [April 12, 2019](https://twitter.com/kvlly/status/1116672656781266944?ref_src=twsrc%5Etfw)


So, that happened.


I hadn’t seen anyone say something like this in quite a while.  I remember saying things like this myself as recently as, oh, 2016, but I thought the zeitgeist had moved on to continuous delivery.


Which is not to say that Friday freezes don’t happen anymore, or even that they shouldn’t; I just thought that this was no longer seen as a badge of responsibility and honor, rather a source of mild embarrassment.  (Much like the fact that you still don’t automatedly restore your db backups and verify them every night.  *Do you.*)


So I responded with an equally hyperbolic and indefensible claim:


> If you're scared of pushing to production on Fridays, I recommend reassigning all your developer cycles off of feature development and onto your CI/CD process and observability tooling for as long as it takes to ✨fix that✨.
> — Charity Majors (@mipsytipsy) [April 15, 2019](https://twitter.com/mipsytipsy/status/1117858830136664067?ref_src=twsrc%5Etfw)


Now obviously, OBVIOUSLY, reassigning all your developer cycles is probably a terrible idea.  You don’t get 100x parallel efficiency if you put 100 developers on a single problem.  So I thought it was clear that this said somewhat tongue in cheek, serious-but-not-really.  I was wrong there too.


So let me explain.


There’s nothing morally “wrong” with Friday freezes.  But it is a costly and cumbersome bandage for a problem that you would be better served to address directly.  And if your stated goal is to protect people’s off hours, this strategy is likely to sabotage that goal and cause them to waste far more time and get woken up much more often, and it stunts your engineers’ technical development on top of that.


## Fear is the mind-killer.


Fear of deploys is the ultimate technical debt.  How much time does your company waste, between engineers:

- waiting until it is “safe” to deploy,
- batching up changes into bigger changes that are decidedly unsafe to deploy,
- debugging broken deploys that had many changes batched into them,
- waiting nervously to get paged after a deploy goes out,
- figuring out if now is a good time to deploy or not,
- cleaning up terrible deploy-related catastrophuckes


**Anxiety related to deploys is the single largest source of technical debt** in many, many orgs.  Technical debt, lest we forget, is not the same as “bad code”.  Tech debt *hurts your people.*


Saying “don’t push to production” is a code smell.  Hearing it once a month at unpredictable intervals is concerning.  Hearing it EVERY WEEK for an ENTIRE DAY OF THE WEEK should be a heartstopper alarm.  If you’ve been living under this policy you may be numb to its horror, but just because you’re used to hearing it doesn’t make it any less noxious.


If you’re used to hearing it and saying it on a weekly basis, *you are afraid of your deploys and you should fix that.*


> It’s a smell. If you can’t deploy at 6pm on a Friday it means you don’t understand or don’t trust your systems or process. That might be ok if you openly acknowledge it, but if your not talking about it, that’s dangerous
> — Erik Peterson (@silvexis) [April 16, 2019](https://twitter.com/silvexis/status/1118200830853824512?ref_src=twsrc%5Etfw)


If you are a software company, shipping code is your heartbeat.  Shipping code should be as reliable and sturdy and fast and unremarkable as possible, because this is the drumbeat by which value gets delivered to your org.


## Deploys are the heartbeat of your company.


Every time your production pipeline stops, it is a heart attack.  It should not be ok to go around nonchalantly telling people to halt the lifeblood of their systems based on something as pedestrian as the day of the week.


Why are you afraid to push to prod?  Usually it boils down to one or more factors:

- your deploys frequently break, and require manual intervention just to get to a good state
- your test coverage is not good, your monitoring checks are not good, so you rely on users to report problems back to you and this trickles in over days
- recovering from deploys gone bad can regularly cause everything to grind to a halt for hours or days while you recover, so you don’t want to even embark on a deploy without 24 hours of work day ahead of you
- your deploys are painfully slow, and take hours to run tests and go live.


These are pretty darn good reasons.  If this is the state you are in, I totally get why you don’t want to deploy on Fridays.  So what are you doing to actively fix those states?  How long do you think these emergency controls will be in effect?


The answers of “nothing” and “forever” are unacceptable.  These are eminently fixable problems, and the amount of drag they create on your engineering team and ability to execute are the equivalent of five-alarm fires.


Fix. That.  Take some cycles off product and fix your fucking deploy pipeline.


> It is difficult to combine "you shouldn't do this because it is a symptom of a systemic problem, you should instead address the systemic problem" with "yes actually you should do it for as long as the systemic problem exists, because it is adaptive".
> — Senior Oops Engineer (@ReinH) [April 16, 2019](https://twitter.com/ReinH/status/1118249822220251136?ref_src=twsrc%5Etfw)


If you’ve been paying attention to the [DORA](http://devops-research.com) report or [Accelerate](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339), you know that the way you address the problem of flaky deploys is NOT by slowing down or adding roadblocks and friction, but by shipping more QUICKLY.


## Science says: ship fast, ship often.


Deploy on every commit.  Smaller, coherent changesets transform into debuggable, understandable deploys.  If we’ve learned anything from recent research, it’s that velocity of deploys and lowered error rates are not in tension with each other, they actually reinforce each other.  When one gets better, the other does too.


So by slowing down or batching up or pausing your deploys, you are **materially contributing to the worsening of your own overall state.**


If you block devs from merging on Fridays, then you are sacrificing a fifth of your velocity and overall output.  That’s a lot of fucking output.


If you do not block merges on Fridays, and only block deploys, you are queueing up a bunch of changes to all get shipped days later, long after the engineers wrote the code and have forgotten half of the context.  Any problems you encounter will be MUCH harder to debug on Monday in a muddled blob of changes than they would have been just shipping crisply, one at a time on Friday.  Is it worth sacrificing your entire Monday?  Monday-Tuesday?  Monday-Tuesday-Wednesday?


> The worst, most PTSD-inducing outages of my life have all happened after holiday code freezes.  Every. Single. One.
> Don't use rules.  Practice good judgment, build tools to align incentives and deploy often; practice tolerating and recovering from pedestrian failures often too. [https://t.co/GH7lef274z](https://t.co/GH7lef274z)
> — Charity Majors (@mipsytipsy) [April 17, 2019](https://twitter.com/mipsytipsy/status/1118455862912098304?ref_src=twsrc%5Etfw)


## Good judgment matters more than rules.


I am not saying that you should make a habit of shipping a large feature at 4:55 pm on Friday and then sauntering out the door at 5.  For fucks sake.  Every engineer needs to learn and practice good technical judgment around deploy hygiene.  LIke,

- Don’t ship before you walk out the door on *any* day.

- Don’t ship big, gnarly features right before the weekend, if you aren’t going to be around to watch them.
- Instrument your code, and go and LOOK at the damn thing once it’s live.
- Use feature flags and other tools that separate turning on code paths from deploys.


But you don’t need rules for this; in fact, rules actually inhibit the development of good judgment!


> Policies (and enumerated exceptions to policies, and exceptions to exceptions) are a piss-poor substitute for judgment.  Rules are blunt instruments that stunt your engineers' development and critical thinking skills.
> Allow me to illustrate. [https://t.co/H8KgT7bRfU](https://t.co/H8KgT7bRfU)
> — Charity Majors (@mipsytipsy) [April 17, 2019](https://twitter.com/mipsytipsy/status/1118372788451053568?ref_src=twsrc%5Etfw)


Most deploy-related problems are readily obvious, if the person who has the context for the change in their heads goes and looks at it.


But if you aren’t looking for them, then sure — you probably won’t find out until user reports start to trickle in over the next few days.


So go and LOOK.


## Stop shipping blind.  Actually LOOK at what you ship.


I mean, if it takes 48 hours for a bug to show up, then maybe you better freeze deploys on Thursdays too, just to be safe!  🙄


I get why this seems obvious and tempting.  The “safety” of nodeploy Friday is realized immediately, while the costs are felt later later.  They’re felt when you lose Monday (and Tuesday) to debugging the big blob deplly.  Or they get amortized out over time.  Or you experience them as sluggish ship rates and a general culture of fear and avoidance, or learned helplessness, and the broad acceptance of fucked up situations as “normal”.


> If pushing to production is a painful event, make it a *non-event* (same philosophy as chaos engineering)
> — Paul Sec.jpeg                                 .exe (@PaulWebSec) [April 16, 2019](https://twitter.com/PaulWebSec/status/1118011657966489600?ref_src=twsrc%5Etfw)


But if recovering from deploys is long and painful and hard, then you should ***fix that***.  If you don’t tend to detect reliability events until long after the event, you should ***fix that***.  If people are regularly getting paged on Saturdays and Sundays, they are probably getting paged throughout the night, too.  You should ***fix that***.


On call paging events should be extremely rare.  There’s no excuse for on call being something that significantly impacts a person’s life on the regular.  None.


I’m not saying that every place is perfect, or that every company can run like a tech startup.  I am saying that deploy tooling is systematically underinvested in, and we abuse people far too much by paging them incessantly and running them ragged, because we don’t actually believe it can be any better.


It can.  If you work towards it.


Devote some real engineering hours to your deploy pipeline, and some real creativity to your processes, and someday you too can lift the Friday ban on deploys and relieve your oncall from burnout and increase your overall velocity and productivity.


## On virtue signaling


Finally, I heard from a alarming number of people who admitted that Friday deploy bans were useless or counterproductive, but they supported them anyway as a purely symbolic gesture to show that they supported work/life balance.


This makes me really sad.  I’m … glad they want to support work/life balance, but surely we can come up with some other gestures that don’t work directly counter to their goals of  life/work balance.


> That's it.  Because if you make it a virtue signal, it will NEVER GET FIXED.  Blocking Friday deploy is not a mark of moral virtue; it is a physical bash script patching over technical rot.
> And technical rot is bad because it HURTS PEOPLE.  It is in your interest to fix it.
> — Charity Majors (@mipsytipsy) [April 16, 2019](https://twitter.com/mipsytipsy/status/1118197531387633664?ref_src=twsrc%5Etfw)


## Recovery: building a healthy deploy culture


Ways to begin recovering from a toxic deploy culture:

- Have a deploy philosophy, make sure everybody knows what it is.  Be consistent.
- Build and deploy on every set of committed changes.  Do not batch up multiple people’s commits into a deploy.
- Train every engineer so they can run their own deploys, if they aren’t fully automated.  Make every engineer responsible for their own deploys.
- (Work towards fully automated deploys.)
- Every deploy should be owned by the developer who made the changes that are rolling out.  Page the person who committed the change that triggered the deploy, not whoever is oncall.
- Set expectations around what “ownership” means.  Provide [observability tooling](http://honeycomb.io/signup) so they can break down by build id and compare the last known stable deploy with the one rolling out.
- Never accept a diff if there’s no explanation for the question, “how will you know when this code breaks?  how will you know if the deploy is not behaving as planned?”  Instrument every commit so you can answer this question in production.
- Shipping software and running tests should be fast.  Super fast.  Minutes, tops.
- It should be muscle memory for every developer to check up on their deploy and see if it is behaving as expected, and if anything else looks “weird”.
- Practice good deploy hygiene using feature flags.  Decouple deploys from feature releases.  Empower support and other teams to flip flags without involving engineers.


Each deploy should be owned by the developer who made the code changes.  But your deploy pipeline needs to have a team that owns it too.  I recommend putting your most experienced, senior developers on this problem to signal its high value.


You can find more tips for boring deploys in my piece on why [shipping software should not be scary.](https://charity.wtf/2018/08/19/shipping-software-should-not-be-scary/)


## Good teams ship often.


Ultimately, I am not dogmatic about Friday deploys.  Truly, I’m not.  If that’s the only lever you have to protect your time, use it.  **But call it and treat it like the hack it is.**  It’s a gross workaround, not an ideal state.


Don’t let your people settle into the idea that it’s some kind of moral stance instead of a butt-ugly hack.  Because if you do you will never, ever get rid of it.


> There are plenty of good reasons to block deploys on Fridays, but it's not a good policy to cargo cult blindly.  It imposes real costs and ultimately hinders you from achieving safe, boring deploys.
> Good night.
> — Charity Majors (@mipsytipsy) [April 17, 2019](https://twitter.com/mipsytipsy/status/1118455871112015872?ref_src=twsrc%5Etfw)


Remember: a team’s maturity and efficiency can be represented by how long it takes to get their shit into users’ hands after they write it.  Ship it fast, while it’s still fresh in your developers’ heads.  Ship one change set at a time, so you can swiftly debug and revert them.  I promise your lives will be so much better.  Every step helps.  <3


charity.
