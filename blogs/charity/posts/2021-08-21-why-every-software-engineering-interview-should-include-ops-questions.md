---
title: "Why every software engineering interview should include ops questions"
date: 2021-08-21
url: https://charity.wtf/2021/08/21/why-every-software-engineering-interview-should-include-ops-questions/
word_count: 1155
---


I’ve fallen way behind on my blog posts — my goal was to write one per month, and I haven’t published anything since MAY. Egads. So here I am dipping into the drafts archives! This one was written in April of 2016, when I was noodling over my CraftConf 2016 talk on “[DevOps for Developers (see slides)](https://speakerdeck.com/charity/devops-for-developers-building-an-effective-ops-org-1).”


So I got to the part in my talk where I’m talking about how to interview and hire software engineers who aren’t going to burn the fucking house down, and realized I could spend a solid hour on that question alone. That’s why I decided to turn it into a blog post instead.


### Stop telling ops people to code better, start telling SWEs to ops better


Our industry has gotten very good at pressing operations engineers to get better at writing code, writing tests, and software engineering in general these past few years. Which is great! But we have not been *nearly* so good at pushing software engineers to level up their systems skills. Which is unfortunate, because it is just as important.


Most systems suffer from the syndrome of running too much software. Tossing more software into the heap is as likely to cause more problems as often as it solves them.


We see this play out at companies stacked with good software engineers who have built horrifying spaghetti messes of their infrastructure, and then commence paging themselves to death.


The only way to unwind this is to reset expectations, and make it clear that

1. you are still responsible for your code after it’s been deployed to production, and** **
2. operational excellence is everyone’s job**.**


Operations is the constellation of tools, practices, policies, habits, and docs around shipping value to users, and every single one of us needs to participate in order to do this swiftly and safely.


### Every software engineering interviewing loop should have an ops component.


Nobody interviews candidates for SRE or ops nowadays without asking some coding questions. You don’t have to be the greatest programmer in the world, but you can’t be functionally illiterate. The reverse is less common: asking software engineers basic, stupid questions about the lifecycle of their code, instrumentation best practices, etc.


It’s common practice at lots of companies now to have a software engineer in the loop for hiring SREs to evaluate their coding abilities. It should be just as common to have an ops engineer in the loop for a SWE hire, especially for any SWE who is being considered for a key senior position. Those are the people you most rely on to be mentors and role models for junior hires. All engineers should embrace the ethos of owning their code in production, and nobody should be promoted or hired into a senior role if they don’t.


And yes, that means *all engineers*!  Even your iOS/Android engineers and website developers should be interested in what happens to their code after they hit deploy.  They should care about things like instrumentation, and what kind of data they may need later to debug their problems, and how their features may impact other infrastructure components.


You need to balance out your software engineers with engineers who don’t react to every problem by writing more code. You need engineers who write code begrudgingly, as a last resort. You’ll find these priceless gems in ops and SRE.


### ops questions for software engineers


The best questions are broad and start off easy, with plenty of reasonable answers and pathways to explore. Even beginners can give a reasonable answer, while experts can go on talking for hours.


For example: give them the specs for a new feature, and ask them to talk through the infrastructure choices and dependencies to support that feature. Do they ask about things like which languages, databases, and frameworks are already supported by the team? Do they understand what kind of monitoring and observability tools to use, do they ask about local instrumentation best practices?


Or design a full deployment pipeline together. Probe what they know about generating artifacts, versioning, rollbacks, branching vs master, canarying, rolling restarts, green/blue deploys, etc. How might they design a deploy tool? Talk through the tradeoffs.


Some other good starting points:

- “Tell me about the last time you caused a production outage. What happened, how did you find out, how was it resolved, and what did you learn?”
- “What are some of your favorite tools for visibility, instrumentation, and debugging?
- “Latency seems to have doubled over the last 6 hours. Where do you start looking, how do you start debugging?”
- And this chestnut: “What happens when you type ‘google.com’ into a web browser?” You would be fucking *astonished* how many senior software engineers don’t know a thing about DNS, HTTP, SSL/TLS, cookies, TCP/IP, routing, load balancers, web servers, proxies, and on and on.


Another question I really like is: “what’s your favorite API (or database, or language) and why?” followed up by “… and what are the worst things about it?” (True love doesn’t mean blind worship.)


Remember, you’re exploring someone’s experience and depth here, not giving them a pass-fail quiz. It’s *okay* if they don’t know it all. You’re also evaluating them on communication skills, which is severely underrated by most people but is actually as a key technical skill.


### Signals to look for


You’re not looking for perfection. You are teasing out signals for things like, how will this person perform on a team where software engineers are expected to own their code? How much do they know about the world outside the code they write themselves? Are they curious, eager, and willing to learn, or fearful, incurious and begrudging?


Do they expect networks to be reliable? Do they expect databases to respond, retries to succeed? Are they offended by the idea of being on call? Are they overly clever or do they look to simplify? (God, I hate clever software engineers 🙃.)


It’s valuable to get a feel for an engineer’s operational chops, but let’s be clear, you’re doing this for one big reason: to set expectations. By making ops questions part of the interview, you’re establishing from the start that you run an org where **operations is valued**, where ownership is non-optional. This is not an ivory tower where software engineers can merrily git push and go home for the day and let other people handle the fallout


It can be toxic when you have an engineer who thinks all ops work is toil and operations engineering is lesser-than. It tends to result in operations work being done very poorly. This is your best chance to let those people self-select out.


You know what, I’m actually feeling uncharacteristically optimistic right now. I’m remembering how controversial some of this stuff was when I first wrote it, five years ago in 2016. Nowadays it just sounds obvious. Like table stakes.


Hell yeah. 🤘
