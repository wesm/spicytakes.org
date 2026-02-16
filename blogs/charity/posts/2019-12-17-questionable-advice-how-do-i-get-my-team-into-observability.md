---
title: "Questionable Advice #2: How Do I Get My Team Into Observability?"
date: 2019-12-17
url: https://charity.wtf/2019/12/17/questionable-advice-how-do-i-get-my-team-into-observability/
word_count: 2611
---


*Welcome to the second installment of my advice column! Last time we talked about [the emotional impact](https://charity.wtf/2019/11/23/questionable-advice-after-being-a-manager-can-i-be-happy-as-a-cog/) of going back to engineering after a stint in management. If you have a question you’d like to ask, please email me or DM it to me on twitter.*


> Hi Charity! I hope it’s ok to just ask you this… 
> I’m trying to get our company more aware of observability and I’m finding it difficult to convince people to look more into it. We currently don’t have the kind of systems that would require it much – but we will in future and I want us to be ahead of the game. 
> If you have any tips about how to explain this to developers (who are aware that quality is important but don’t always advocate for it / do it as much as I’d prefer), or have concrete examples of “here’s a situation that we needed observability to solve – and here’s how we solved it”, I’d be super grateful. 
> If this is too much to ask, let me know too 🙂 
> I’ve been talking to [Abby Bangser](http://twitter.com/a_bangser) a lot recently – and I’m “classifying” observability as “exploring in production” in my mental map – if you have philosophical thoughts on that, I’d also love to hear them 🙂
> [alex_schl](http://twitter.com/alex_schl)


Dear [Alex](http://twitter.com/alex_schl),


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2019/11/systembroeknsun.png?resize=224%2C130&ssl=1)

*Everyone’s systems are broken. Not just yours!*


Yay, what a GREAT note!  I feel like I get asked some subset or variation of these questions several times a week, and I am delighted for the opportunity to both write up a response for you and post it for others to read.  I bet there are orders of magnitude more people out there with the same questions who *don’t* ask, so I really appreciate those who do. <3


I want to talk about the nuts and bolts of pitching to engineering teams and shepherding technical decisions like this, and I promise I will offer you some links to examples and other materials. But first I want to examine some of the assumptions in your note, because they elegantly illuminate a couple of common myths and misconceptions.


#### **Myth #1: you don’t need observability til you have problems of scale**


First of all, there’s this misconception that observability is something you only need when you have really super duper hard problems, or that it’s only justified when you have microservices and large distributed systems or crazy scaling problems.  No, no no nononono.


There may come a point where you are ABSOLUTELY FUCKED if you don’t have observability, but it is ALWAYS better to develop with it.  *It is never not better to be able to see what the fuck you are doing!*  The image in my head is of a hiker with one of those little headlamps on that lets them see where they’re putting their feet down.  Most teams are out there shipping opaque, poorly understood code blindly — shipping it out to systems which are themselves crap snowballs of opaque, poorly understood code. This is costly, dangerous, and **extremely wasteful of engineering time**.


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2019/01/Sea-of-Metrics-Alien.png?resize=160%2C160&ssl=1)


Ever seen an engineering team of 200, and struggled to understand how the product could possibly need more than one or two teams of engineers? They’re all fighting with the crap snowball.


Developing software with observability is better at ANY scale.  It’s better for monoliths, it’s better for tiny one-person teams, it’s better for pre-production services, it’s better for literally everyone always.  The sooner and earlier you adopt it, the more compounding value you will reap over time, and the more of your engineers’ time will be devoted to forward progress and creating value.


#### **Myth #2: observability is harder and more technically advanced** **than monitoring**


Actually, it’s the opposite — it’s *much* easier.  If you sat a new grad down and asked them to instrument their code and debug a small problem, it would be fairly straightforward with observability. Observability speaks the native language of variables, functions and API endpoints, the mental model maps cleanly to the request path, and you can straightforwardly ask any question you can come up with. (A key tenet of observability is that it gives an engineer the ability to *ask any question*, without having had to anticipate it in advance.)


With metrics and logging libraries, on the other hand, it’s far more complicated.you have to make a bunch of awkward decisions about where to emit various types of statistics, and it is terrifyingly easy to make poor choices (with terminal performance implications for your code and/or the remote data source).  When asking questions, you are locked in to asking only the questions that you chose to ask a long time ago. You spend a lot of time translating the relationships between code and lowlevel systems resources, and since you can’t break down by users/apps you are blocked from asking the most straightforward and useful questions entirely!


Doing it the old way Is. Fucking. Hard.  Doing it the newer way is actually much easier, save for the fact that it is, well, newer — and thus harder to google examples for copy-pasta. But if you’re saturated in decades of old school ops tooling, you may have some unlearning to do before observability seems obvious to you.


#### **Myth #3: observability is a purely technical solution**


To be clear, you *can* just add an observability tool to your stack and go on about your business — same old things, same old way, but now with high cardinality!


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2019/11/survive.png?resize=174%2C144&ssl=1)


You *can, *but you *shouldn’t*.


These are sociotechnical systems and they are best improved with sociotechnical solutions.  Tools are an absolutely necessary and inextricable part of it.  But so are on call rotations and the fundamental virtuous feedback loop of *you build it, you run it.  *So are code reviews, monitoring checks, alerts, escalations, and a blameless culture.  So are managers who allocate enough time away from the product roadmap to truly fix deep technical rifts and explosions, even when it’s inconvenient, so the engineers aren’t in constant monkeypatch mode.


I believe that observability is a prerequisite for any major effort to have saner systems, simply because it’s *so powerful* being able to see the impact of what you’ve done.  In the hands of a creative, dedicated team, simply wearing a headlamp can be transformational.


#### **Observability is your five senses for production.**


You’re right on the money when you ask if it’s about exploring production, but you could also use words that are even more basic, like “understanding” or “inspecting”.  Observability is to software systems as a debugger is to software code.  It shines a light on the black box.  It allows you to move much faster, with more confidence, and catch bugs much sooner in the lifecycle — before users have even noticed.  It rewards you for writing code that is easy to illuminate and understand in production.


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2019/09/panda_nines.png?resize=212%2C178&ssl=1)


So why isn’t everyone already doing it?  Well, making the leap isn’t frictionless.  There’s a minimal amount of instrumentation to learn (easier than people expect, but it’s nonzero) and then you need to learn to see your code through the lens of your own instrumentation.  You might need to refactor your use of older tools, such as metrics libraries, monitoring checks and log lines.  You’ll need to learn another query interface and how it behaves on your systems.  You might find yourself amending your code review and deploy processes a bit.


Nothing too terrible, but it’s all *new*.  We hate changing our tool kits until absolutely fucking necessary.  Back at Parse/Facebook, I actually clung to my sed/awk/shell wizardry until I was professionally shamed into learning new ways when others began debugging shit faster than I could.  (I was used to being the debugger of last resort, so this really pissed me off.)  So I super get it!  So let’s talk about how to get your team aligned and hungry for change.


#### **Okay okay okay already, how do I get my team on board?**


If we were on the phone right now, I would be peppering you with a bunch of questions about your organization.  Who owns production?  Who is on call?  Who runs the software that devs write?  What is your deploy process, and how often does it get updated, and by who?  Does it have an owner?  What are the personalities of your senior folks, who made the decisions to invest in the current tools (and what are they), what motivates them, who are your most persuasive internal voices?  Etc.  Every team is different.  <3


There’s a virtuous feedback loop you need to hook up and kickstart and tweak here, where the people with the original intent in their heads (software engineers) are also informed and motivated, i.e. empowered to make the changes and personally impacted when things are broken. I recommend starting by **putting your software engineers on call for production** (if you haven’t).  This has a way of convincing even the toughest cases that they have a strong personal interest in quality and understandability.


Pay attention to your feedback loop and the alignment of incentives, and make sure your teams are given enough time to actually fix the broken things, and motivation usually isn’t a problem.  (If it is, then perhaps another feedback loop is lacking: your engineers feeling sufficiently aligned with your users and their pain.  But that’s another post.)


#### **Technical ownership over technical outcomes**


I appreciate that you want your team to own the technical decisions.  I believe very strongly that this is the right way to go.  But it doesn’t mean you can’t have influence or impact, and *particularly* in times like this.


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2019/11/delusion.png?resize=215%2C192&ssl=1)


It is literally your job to have your head up, scanning the horizon for opportunities and relevant threats.  It’s their job to be heads down, focusing on creating and delivering excellent work.  So it is absolutely appropriate for you to flag something like observability as both an opportunity and a potential threat, if ignored.


If I were in your situation and wanted my team to check out some technical concept, I might send around a great talk or two and ask folks to watch it, and then maybe schedule a lunchtime discussion.  Or I might invite a tech luminary in to talk with the team, give a presentation and answer their questions.  Or schedule a hack week to apply the concept to a current top problem, or something else of that nature.


But if I really wanted them to *take it fucking seriously*, I would put my thumb on the scale.  I would find myself a champion, load them up with context, and give them ample time and space to skill up, prototype, and eventually present to the team a set of recommendations.  (And I would stay in close contact with them throughout that period, to make sure they didn’t veer too far off course or lose sight of my goals.)

1. **Get a champion.**

Ideally you want to turn the person who is most invested in the old way of doing things — the person who owns the ELK cluster, say, or who was responsible for selecting the previous monitoring toolkit, or the goto person for ops questions — from your greatest obstacle into your proxy warrior.  This only works if you know that person is open-minded and secure enough to give it a fair shot & publicly change course, has sufficiently good technical judgment to evaluate and project into the future, and has the necessary clout with their peers.  If they don’t, or if they’re too afraid to buck consensus: pick someone else.
2. **Give them context.  **

Take them for a long walk.  Pour your heart and soul out to them.  Tell them what you’ve learned, what you’ve heard, what you hope it can do for you, what you fear will happen if you don’t.  It’s okay to get personal and to admit your uncertainties.  The more context they have, the better the chance they will come out with an outcome you are happy with.  Get them worried about the same things that worry you, get them excited about the same possibilities that excite you.  Give them a sense of the stakes.  

And don’t forget to tell them why you are picking them — because they are listened to by their peers, because they are already expert in the problem area, because you trust their technical judgment and their ability to evaluate new things — all the reasons for picking them will translate well into the best kind of flattery — the true kind.
3. **Give them a deadline.**

A week or two should be plenty.  Most likely, the decision is not going to be unilaterally theirs (this also gives you a bit of wiggle room should they come back going “ah no ELK is great forever and ever”), but their recommendations should carry serious weight with the team and technical leadership.  Make it clear what sort of outcome you would be very pleased with (e.g. a trial period for a new service) and what reasons you would find compelling for declining to pursue the project (i.e. your tech is unsupported, cost prohibitive, etc).  Ideally they should use this time to get real production data into the services they are testing out, so they can actually experience and weigh the benefits, not just read the marketing copy.


As a rule of thumb, I always assume that managers can’t convince engineers to do things: only other engineers can.  But what you can do instead is set up an engineer to be your champion.  And then just sit quietly in the corner, nodding, with an interested look on your face.


#### **The nuclear option**


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2019/11/meplusprod.png?resize=164%2C248&ssl=1)

*if you <3 prod,prod will <3 you back*


You have one final option.  If there is no appropriate champion to be found, or insufficient time, or if you have sufficient trust with the team that you judge it the right thing to do: you *can* simply order them to do something your way.  This can feel squicky. It’s not a good habit to get into.  It usually results in things being done a bit slower, more reluctantly, more half-assedly. And you sacrifice some of your power every time you lean on your authority to get your team to do something.


But it’s just as bad for a leader to take it off the table entirely.


Sometimes you will see things they can’t.  If you cannot wield your power when circumstances call for it, then you don’t fucking have real power — you have unilaterally disarmed yourself, to the detriment of your org.  You can get away with this maybe twice a year, tops.


But here’s the thing: if you order something to be done, and it turns out in the end that you were right?  You earn back all the power you expended on it *plus interest.  *If you were right, unquestionably right in the eyes of the team, they will respect you more for having laid down the law and made sure they did the right thing.


xo


charity


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2019/10/img_6377.png?resize=199%2C265&ssl=1)


Some useful resources:

- [https://thenewstack.io/observability-a-3-year-retrospective/](https://thenewstack.io/observability-a-3-year-retrospective/) a super meaty technical retrospective
- [https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool/](https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool/) the technical underpinnings of observability, and why they are different from monitoring (and why they matter)
- [https://www.heavybit.com/library/podcasts/o11ycast/ep-1-monitoring-vs-observability/](https://www.heavybit.com/library/podcasts/o11ycast/ep-1-monitoring-vs-observability/) (a podcast, lots of folks have cited this as a great intro)
- [https://www.honeycomb.io/blog/incident-report-running-dry-on-memory-without-noticing/](https://www.honeycomb.io/blog/incident-report-running-dry-on-memory-without-noticing/) one of our recent incident reports, with screenshots
- [https://charity.wtf/2019/10/28/deploys-its-not-actually-about-fridays/](https://charity.wtf/2019/10/28/deploys-its-not-actually-about-fridays/) includes some observations on what it’s liek to be working on a stack where we actually understand what the fuck we are shipping, we aren’t just accumulating blacker and blacker boxes with every depoy.
