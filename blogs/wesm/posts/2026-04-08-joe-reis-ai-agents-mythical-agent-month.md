---
title: "AI Agents, The Mythical Agent Month, and My Wild AI Coding Setup"
summary: "Podcast at Joe Reis Podcast"
date: 2026-04-08T00:00:00
tags: ["podcast", "transcript"]
slug: joe-reis-ai-agents-mythical-agent-month
word_count: 6629
source_file: transcripts/2026-04-08-joe-reis-ai-agents-mythical-agent-month.md
content_type: transcript
event: "Joe Reis Podcast"
video_url: "https://www.youtube.com/watch?v=uC6g8L8zquE"
---

{{< video https://www.youtube.com/watch?v=uC6g8L8zquE >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this conversation with Joe Reis, I talk about my transition from existential dread about AI in early 2025 to being fully locked in on agentic software engineering by the end of the year.

I describe how I went from muting LLMs on Twitter to becoming a heavy Claude Code user after Steve Yegge's posts about it last April. The jump from Sonnet 4 to Opus 4.5 was a chasm crossing -- the models became good enough to build real software, not just toy features. I started building a personal productivity stack: Message Vault for email archiving and search (because Gmail search is terrible), AgentsView for session analytics, RoboRev for continuous code review, and Money Flow for personal finance. All built with coding agents.

I explain my development setup: three columns of Kitty terminal windows, six to eight concurrent Claude or Codex sessions, with a RoboRev review queue per project as an accountability system. Every agent turn generates a commit via post-commit hook, which triggers a background code review. I process reviews in batches and feed findings back into the originating session for best context. I recently switched to Superset (superset.sh) for managing git worktrees across projects.

A central point: the code coming out of coding agents is very buggy. Even Opus 4.6 output needs rigorous review. I run 150+ reviews per day across Codex, Gemini, and Claude, plus dedicated security reviews. Codex is my best code reviewer -- it deliberates 60-90 seconds on average versus Claude's 15 seconds. My theory is that Claude has been reinforcement-learned for faster cycle times to create engagement, at the cost of review depth.

I discuss why Go has become my language of choice for agentic development: fast builds (single-digit seconds), fast execution, and I never have to write a line of it. Python is too slow at runtime when you're not reading or writing the code. Rust compiles too slowly for tight agent feedback loops.

On the Mythical Agent Month: people underestimate the gap between working software and a viable product -- Fred Brooks estimated 9x. Coding agents are great at building Potemkin software, the facade, but struggle with the thorny details of robustness, scalability, and maintainability. The "brownfield barrier" hits around 100K lines of code, and working on million-line codebases like VS Code/Positron requires giving agents treasure maps and hard sandboxing. I'm not an AGI bull.

I describe turning scattered attention time -- Peloton rides, yoga, TV watching, Zoom calls -- into productive agent supervision time. The agents filled in my skill gaps in DevOps, CI/CD, and sysadmin, which I always hated. Building a Tauri desktop wrapper for AgentsView with Apple notarization is something I never would have done pre-AI.

## Key Quotes

> "If you're just committing and shipping the code that's coming out of Opus 4.6, that code is a bunch of hot garbage. It has to be really rigorously reviewed by other agents and different agent sessions to have any semblance of confidence that you're shipping something that isn't totally slop." -- Wes McKinney

> "Coding agents are very good at building the facade, the Potemkin's facade of the software. But when you actually go into the thorny issues associated with making it robust, making it scalable, making it maintainable by somebody other than its author -- all these things can go wrong." -- Wes McKinney

> "I put off learning Rust just long enough that I never have to learn it." -- Wes McKinney

> "The whole reason to use Python is that it's easy to read and write. So if I'm not reading or writing the code, what's the point?" -- Wes McKinney

> "I went from existential dread a year ago to being very stimulated and very locked in. I kind of prefer the being locked in because being in a state of existential dread and feeling like my career is over was not very fun." -- Wes McKinney

> "Coding agents don't care whether it's fun or not. They'll just do it for you. And if it doesn't work the first time, they'll keep trying until it's done." -- Wes McKinney

## Transcript

**Joe Reis:** We meet again. How you doing?

**Wes McKinney:** Doing good. Doing good. Yeah. Happy to be here.

**Joe:** I'm glad you're here. I think last time we saw each other was in freezing Nashville of all places.

**Wes:** Yeah. Was it cold? Or maybe it was about to be the ice storm.

**Joe:** Yes. Yeah. Storm of the century-ism.

**Wes:** Yeah. We ate Spanish food and then I flew out of town the next day to get to New York to record some other podcasts because I was worried -- justifiably -- about my flight being canceled. My original flight did get canceled. So it was a good thing I got to New York ahead of time.

**Joe:** Yeah. I just got like two feet of snow in New York. So for them it was no big deal. But for here it was like half inch of ice or an inch of ice on all the trees. And so all the dead branches and trees fell down and caused havoc all over town.

**Wes:** That was the storm for sure.

**Joe:** Well, I'm glad you made it out of it. What have you got to? It seems like you've hit a new stride. It's like Wes Renaissance man all of a sudden.

**Wes:** Yeah, I've been grinding. To be honest with you, I spent a lot of -- I was pretty tuned out of AI throughout 2023 and 2024. I remember when ChatGPT launched, I actually muted LLMs in my Twitter timeline. I was like, I'm just not interested in this. So I was just not tuned in at all.

And then in the beginning of last year, I spent the first couple months of the year in a state of existential dread about like, what is my purpose? What do I even do here anymore? Basically contemplating the future of software engineering and development as a journeyman programmer, somebody who's been working for 20 years, who's built a lot of projects and founded a bunch of companies and has been just building software.

I didn't really use the AI IDEs very much. I never paid for Cursor. I tried out Windsurf for a couple of months. I was like, ah, it's a little bit better than Copilot in VS Code. But then I saw Steve Yegge posting about Claude Code, I think last April. And I started going down the coding agent rabbit hole.

Obviously last April with Sonnet 4 at the time, it just wasn't that good. And I started using Claude Code in a limited way to do Positron development. Positron is a data science IDE, a multi-language data science IDE that Posit develops, where I work. And I started having some success using Claude Code with Positron. And that was pretty exciting. I was like, wow, okay, I could see a future where I just do development with this thing and I don't write any code anymore.

And so I started really leaning into that. I started leaning into the not writing code thing. I was like, let's just see how this works. So obviously that went on for four or five months and it was clear, especially with Opus 4.5, that the models had crossed a chasm and gotten significantly better where you could trust them -- not to do everything, they still needed a lot of supervision and guardrails -- but they could tackle much more difficult tasks. The difference between Sonnet 4 and Opus 4.5 was so significant where it was like, okay, I can use this to build real software that I use, as opposed to working on little toy features that require some amount of agentic development and then a bunch of manual fixes and tweaks and stuff.

And then I also got busy -- I remained pretty involved with Voltron Data up until the end. The company went through some restructuring and was working through its next steps. And ultimately they decided to wind the company down at the end of the year and the rest of the team was laid off. But I was pretty involved there at the end, helping find a path forward for the company and for the team.

Back in August, September, I just didn't really have that much bandwidth for development. But by the end of October, it was clear that the work I was doing with Voltron was winding down and I was obviously still at a full-time job at Posit. And so I started contemplating like, okay, it seems like this AI development thing is real, coding agents are real -- what do I want to build with this?

So I started basically reevaluating my whole personal productivity stack, how I do life basically. That started with personal finance and then started dipping into how I do software development, how I manage my personal information, my email, all my documents. And I've just started building a whole bunch of different tools.

For managing my development process -- because I want to be able to build software with agents faster and more confidently. And it turns out that just doing raw Claude Code is not very good. The code that it generates is still kind of hot garbage. Even Opus 4.6 -- if you're just committing and shipping the code that's coming out of Opus 4.6, that code is a bunch of hot garbage. It has to be really rigorously reviewed by other agents and different agent sessions to have any semblance of confidence that you're shipping something that isn't totally slop.

So I could see like, okay, what happens if I start having three or four agents look at every line of code that Claude is generating and then find all the bugs and find all the testing gaps. So I've been building a system for that called RoboRev.

And then I needed a system to understand all of my agentic development. So I built this system called AgentsView, which is kind of an omnibus session explorer plus session analyzer and insights. It's analytics -- I'm applying my data analytics hat to my agentic development.

And then I built an email system called Message Vault, which is archiving and getting all my data off of Gmail so that I can control my own data destiny and analyze my personal information with local inference or whatever I want to do. I don't want to have to log into Google and use their AI to analyze my email. I think that's BS.

So I've just been chipping away at one problem after another. I've got at least two other projects that I haven't released that I'm working on that I think are interesting. I won't talk about those today, but everything is in the personal productivity space because I feel like things have gotten kind of -- as Cory Doctorow puts it -- enshittified.

I've been very tuned into the platform decay, especially how bad Gmail has gotten. I've been using Gmail for 20 years and it frustrates me. Every time I have to search for something in Gmail, I'm like, what the hell is this? What product manager, what engineers worked on this search feature? Have you ever actually tried to find anything in your email and you thought that this search experience was acceptable?

**Joe:** It does suck.

**Wes:** It frustrated me on a daily basis. And so I started -- yeah, the way I described it on another podcast was like the He-Man grabbing the sword -- by the power of Grayskull. I will solve this personal productivity nightmare. I will not have to suffer this platform decay of Gmail, not being able to find things in my 20 years worth of email. Don't show me emails that are unrelated from six months ago. I'm looking for something that I know exists seven years ago with these exact words in it.

**Joe:** How are you actually getting your data off of Gmail?

**Wes:** You can set up an OAuth app, which allows you -- subject to some quotas -- to download your entire Gmail archive. You can also use Google Takeout, but that gives you a full data export as a tarball or a zip file. I've never actually used it.

**Joe:** I have before. It takes multiple days to get all your email.

**Wes:** Turns out via using OAuth, you can get all your email out of Gmail depending on the amount of email you have. Turns out I had around 50 gigabytes worth of email and about 2 million individual emails. And so it takes -- with Message Vault, for me it takes about 12 hours to exfiltrate everything because there's rate limits. Even on my eight gigabit Google Fiber here in Nashville, I can only get like 100 emails per second out. You do the math and it takes about half a day to get 2 million emails out of there.

But what's been fun is that now that I have this local email archive -- there's a SQLite system of record, I use DuckDB for all the queries and analytics -- I've been going through and purging email out of my Gmail en masse. Eventually I intend to have literal inbox zero, no emails in Gmail. Message Vault will be the system of record for my email and there will be nothing to search in Gmail, and that will fill me with joy.

**Joe:** You're still going to keep your Gmail though, right?

**Wes:** Yeah. I'll still receive email there, but periodically, maybe once a month, I'll do a sync to Message Vault and then do a purge, maybe once every 90 days or something like that.

But yeah, it's kind of not an every-person problem, but as somebody who really cares about personal data sovereignty and not having all my personal information and data locked up in these cloud silos -- I think right now what's interesting is that everyone's reevaluating their relationships with software-as-a-service providers and trying to see, do we really need all these features or can we vibe code a replacement?

I think there's some wrongheadedness here and that people are vibe coding replacements for things they really shouldn't. Either it's not a good use of their time or they're getting themselves in for a maintenance and support headache. People are joking on LinkedIn like, I replaced this $20 a month SaaS service and now I have an engineer that spends 20% of their time maintaining the vibe coded replacement. It's just easier to pay.

I remember when there was big news about Anthropic signing a big contract with Datadog and everyone was razzing them, like what, you didn't just vibe code a replacement for Datadog? But it turns out monitoring applications at scale and just having software that works...

It ties into an essay that I wrote recently called "The Mythical Agent Month."

**Joe:** That was a great essay.

**Wes:** Basically about how people underestimate how difficult it is to build software products. Fred Brooks, the author of The Mythical Man Month -- back in 1975, mind you -- estimated that the difference in the amount of work between working software and a viable software product is around nine times. People are standing up new applications with Claude Code all the time. They see the working application, they're like, my gosh, I have this new web application, this new iPhone app or whatever. And if you've never actually gone and built a full software product and supported it through its whole life cycle, there's all this invisible labor associated with making the software work over a long period of time.

Claude Code and Codex and the coding agents are really good at building the porcelain, the shell. It's kind of this Potemkin software.

**Joe:** That's a good way of putting it.

**Wes:** Coding agents are very good at building the facade, the Potemkin's facade of the software. But when you actually go into the thorny issues associated with making it robust, making it scalable, making it maintainable by somebody other than its author -- all these things that can go wrong when you're running a software product at scale.

Anyway, yeah, lots of -- I went from existential dread a year ago to being very stimulated and very locked in. I kind of prefer the being locked in because being in a state of existential dread and feeling like my career is over was not very fun. And so now I'm just super locked in. I wake up at 5:30, six in the morning and I'm just locked in until I go to bed. I don't know how healthy that is, but I'm not burned out. It's the opposite of burnout. So it's fun. I'm having fun.

**Joe:** I remember you, me, and Nick Schrock and Matt Housley, we did a podcast a while ago, I think before all of us got hooked on Claude Code. And I think one of you described themselves as the "AI boomer." Because Nick went through the same thing where he's kind of like, yeah, this stuff's okay, but whatever. And then fast forward to this time last year, Claude Code, all of a sudden you're like, huh, this stuff's actually pretty interesting.

Because I felt the same way with GitHub Copilot. It was like, I just turned it off, I hate it. I'd rather use IntelliSense. But those days feel like 1890 right now. We've come quite a ways in just a two year period.

**Wes:** Yeah.

**Joe:** I remember we were hanging out and you'd show me your phone and your dashboard of all your cool stuff. And I was like, Wes is a mad man. Everything -- your imagination is the only thing that limits you at this point.

**Wes:** I've got, yeah. I think I showed you my private personal command center. It's my personal to-do list system, personalized agenda. Why use Google Calendar when you can have your own personalized agenda that's exactly the way you want.

**Joe:** Yeah, it was cool.

**Wes:** I'm somebody that hates sysadmin and hates DevOps. And I think partly what has created a creative burst for me is that I can build full-stack applications now without having to get anybody's help. It used to be that whenever I'd have to touch DevOps or CI/CD or sysadmin, there's some people that love their home lab and fiddling with all the machines and doing the sysadmin and networking. But that for me was always my kryptonite.

Whenever I would go to work on something where I would touch the infrastructure of the project, I would kind of shrivel up and be like, oh, this is not enjoyable. Whenever I'd be Googling on Stack Overflow and looking up weird Linux stuff and be like, how do I do passwordless SSH? And there's this voice of the gray beard in my head being like, you didn't learn how to do sysadmin in college? What's wrong with you? But I'm 40 years old and I never learned how to do sysadmin.

Now the coding agents do all my sysadmin and they do all my DevOps and they do all my CI/CD. Suddenly the agents have filled in all these skill gaps that I had underdeveloped, things that didn't spark joy for me. Now I feel this empowerment where I can focus on solving the problems that I think are interesting and lean on the agents to take care of the stuff that I don't find interesting or enjoyable.

I'll give you an example. AgentsView started out as a Go binary which does syncing of agent sessions from JSONL files. And it has a web application for browsing files, full-text search, an analytics dashboard, and other features. But the issue is that people are building all these web applications where you run some program and it runs a web server on localhost. You connect to that application in Chrome or Safari. And it's just not a great experience because you end up having random applications running in Chrome tabs.

It was obvious I should set up either an Electron or Tauri, which is a much more resource-efficient Electron alternative. I should create a desktop application wrapper for AgentsView. This is the kind of thing I would have never done myself before AI. But I could sit on the couch in the evening watching a TV show and work with Claude and Codex to build the Tauri application, run the Go binary as a sidecar in the Tauri application, set up all of the CI/CD and the Apple notarization stuff to create the .app and the .dmg installer and make sure it's notarized because macOS makes you notarize your applications to protect users from malware.

There's all these little tedious details where in the past it would have filled me with such loathing and not-fun vibes that I would have just avoided it. But now coding agents don't care whether it's fun or not. They'll just do it for you. And if it doesn't work the first time, they'll keep trying until it's done.

**Joe:** In Go, by the way, which is a language I think you wrote that you're probably not as proficient in as Python.

**Wes:** No, I've never written a line of Go in my life and I don't see any reason to, honestly. There's a company that I work with, I'm an investor in -- it's a kind of neo data engineering company called Bruin. They're based in Berlin, really smart folks. They built this full-stack data engineering platform, kind of an alternative to using Airflow, dbt, Airbyte, that kind of thing. A little bit of an all-in-one, but it's written in Go. So they were using Go before it was cool.

Now that Go has become essentially the best language for agents -- they actually wrote a blog post, "Go is the ultimate language for agents." I feel like I sort of stumbled on that. I hesitate to call it a fact -- I think it's more of an opinion, but there's good evidence to suggest that Go is one of the very best languages for agents.

I stumbled on it after doing a bunch of agentic engineering with Python and also using Rust. Both of these languages -- I was like, neither of these feels quite right. Something about this is wrong.

In Python, the problem was that running the test suite and running the code was too slow. I'm like, okay, Python slowness is a problem because I'm not writing the code. The whole reason to use Python is that it's easy to read and write. So if I'm not reading or writing the code, what's the point? I should just choose a language that compiles fast and runs fast and that the agents are good at writing.

I tried doing some stuff in Rust -- I've never written Rust either. I put off learning Rust just long enough that I never have to learn it. I was getting shamed by people like, dude, you haven't learned Rust yet? What's wrong with you? And then suddenly I'm like, I never have to learn Rust.

But the problem with Rust is that it compiles pretty slowly. You can build debug binaries fairly quickly, but they don't run as fast. That's the trade-off. Optimized Rust binary builds, especially with a dependency stack, could take many minutes. That's a problem when your agents may take two or three minutes to do something and then have to spend three minutes waiting for the project to build before they can run the tests.

The reason I stumbled on Go is because people told me how fast Go's execution was, but also how fast the builds are -- legendarily fast builds. Go projects build in under 10 seconds, could be a big project. Having build cycles that are single-digit seconds is definitely a game changer when agents need to tweak something, build and test. Tweak, build and test. You can compress that cycle down so the agents' cycle times get shorter and shorter.

Of course, Go is not a perfect language for everything, but for terminal utilities, system utilities, web application backends, things like that, it's a good fit. If I were doing AI or data science, I wouldn't use Go, I'd use Python. But for most other general-purpose systems work, it's a pretty good language.

**Joe:** Pretty cool. What is your whole dev setup like?

**Wes:** Mostly, up until about a week ago, it was mostly just terminals. I use Kitty Terminal. I'm not yet on Ghostty, I'm working on it. But there was a minute where I knew I wanted a GPU-accelerated terminal because the lagginess of slower terminals -- the terminal embedded in VS Code is a little bit laggy, it's XtermJS. Once you've used a GPU-accelerated terminal like Ghostty or Kitty, it's kind of hard to go back.

**Joe:** Yeah, I use Ghostty.

**Wes:** I used Ghostty back in October, November, and it was crashing on me. I had a bunch of random crashes and I was like, that's not super cool. Then I used Kitty and Kitty has never crashed once on me. I've had multiple hard crashes -- lose my entire workspace -- with Ghostty, and I've never had that happen with Kitty.

I generally have three columns of terminals on my monitor. Three Kitty windows and every Kitty window has a stack of terminals with horizontal splits. I'll typically have one or two Claude Code sessions per window and then a terminal for random terminal commands. And then I'll have a RoboRev queue filtered down to the project I'm working on.

The RoboRev queue is where all my code reviews are running. The idea is that my agents do stuff, they execute on plans, they generate commits. The commits get picked up by RoboRev and reviewed in the background. The RoboRev queue is my accountability system for making sure all the code gets looked at. And then I have to take the review and feed the review back into the appropriate agent session to make sure the review feedback gets addressed. Because typically it's finding bugs -- sometimes it'll find stuff like, this isn't going to work on Windows, or this has an edge case that's going to break.

When the agents are implementing, they're just focused on code generation. They don't self-review and scrutinize the code they're generating for bugs. The default is that the code that comes out is very buggy. And the agents tend to believe that the code is good. They attest like, oh, this is ready for production. And it would be full of bugs. You'd launch the application and it'd be a blank screen. They've largely stopped doing that, but still the code is very buggy. Every line should get read three or four times by agents to make sure it's good.

Given the non-determinism of these agents, you could run the exact same prompt, the same review five times and get five different findings. Maybe four of them are valid and one is a false positive. But those four valid findings -- to fix those issues before you ship is worth a lot.

I'll work on two or three projects simultaneously, multiple sessions per project. Sometimes in the same branch or worktree, sometimes different worktrees in the same project. The review queue for each project is what keeps me accountable.

I have all my agents set up to beep when they stop doing things. So I get a little ping -- it's time to check on the cake in the oven. I see what the agent has done, where it stopped, what it says it's done. Sometimes Claude's like, I left some stuff undone, would you like me to do it? And I'm like, yes.

I have all my agents configured to commit every turn. This is essential because you want every agent turn to generate a checkpoint. This is how the RoboRev code review system works -- every time the agents commit, it fires a post-commit hook that triggers a code review. That code review goes into the review queue, which is an inbox for code reviews. I process the reviews in batches -- the last three turns generated these three reviews, I copy and paste all the findings into the agent session where those commits came from.

Feeding the reviews into the same session where the code was generated yields more productive feedback. Because if you start a fresh agent session and address the code review, there's this "Memento" feeling -- where was I? What's this about? Oh, I see, let me investigate the codebase before I address the feedback.

The code review is getting done by a different agent -- an adversarial agent, not the same one that did the implementation. Typically not even the same model. I use Codex to review Claude's work. That's my standard workflow.

About a week ago, I started using a new system called Superset -- not Apache Superset, it's superset.sh. The way I'd describe it is: if anyone's heard of Conductor, it's like a Claude Code and Codex application that manages git worktrees for you. Superset is like Conductor except unlike Conductor, it doesn't have an alternate UI for the Claude Code session itself. It's just terminals.

It's an Electron application where on the sidebar, just like Conductor, it has a list of your projects. For every project, the git worktrees that are active. If some of those worktrees have an upstream pull request, it'll show the PR number and whether CI is passing. You can switch between git worktrees really easily.

**Joe:** Looking at it right now, it looks pretty cool.

**Wes:** It's already the way I was working with Kitty manually, except it makes the git worktree aspect a lot easier. If I receive a new pull request for a project, I can create a new worktree that imports that PR from GitHub. Immediately I'll have it reviewed with RoboRev, address the review feedback. If it seems fine, I'll push the review changes up to the PR. If CI passes, I'll merge it. I don't even have to interrupt what I was doing.

I haven't done metrics, but I think pull requests I'm doing now are getting reviewed somewhere between 10 and 20 times on average. It's really heavy-duty code review. I'm burning a lot of tokens, but it gives me much more confidence that I'm not shipping slop.

I've been building mission-critical production software that can't break for a lot of years. I treat bugs very seriously. I don't want people to start thinking, oh, Wes is vibe coding, using agents, and went from being a legit programmer that makes high-quality software to shipping a bunch of slop. If I'm not reading the code, at least every line should get read three or four times by agents.

Every time I push to GitHub, there are three code reviews that happen. Both Codex and Gemini take a hard look at the branch holistically for bugs and regressions. And I also run a dedicated security review with Codex, just looking for security problems -- prompt injections, sly contributions.

**Joe:** How many tokens does a review take with RoboRev?

**Wes:** I'm not measuring exactly, but I'm running about four to five thousand reviews a month at my current rate. I have a Codex subscription, a Claude Max subscription, and a Gemini subscription. Three $200 a month coding subs is enough to keep up with not only the development but also the code reviews.

There's definitely times when I limit out. Codex is my code review workhorse, and it is definitely the best code reviewer of the three. Codex and Gemini are both better than Claude. Claude is the worst code reviewer, which is funny because sometimes I'll see people singing Claude Code's praises as a code reviewer. And I'm like, have you used Codex to code review? Because it's a lot better.

**Joe:** Why do you think it's better?

**Wes:** It deliberates. It reasons a lot longer. I'm working on a blog post about this because now that I've run on the order of 10,000 code reviews through the system, I have data showing how long each agent on average takes to code review. Claude kind of gives up around 15 seconds of reasoning and then renders a judgment. Codex and Gemini, their average review time is between 60 and 90 seconds. They're reasoning four to six times longer, so they're going to find more.

Maybe there's prompt engineering I could do to coax Claude into deliberating longer. But my sense is that Opus has been reinforcement-learned to have faster cycle times to give developers the feeling of forward momentum. If you've ever talked to somebody that goes from using Claude Code to Codex, Codex feels palpably slower, especially on high or extra-high reasoning.

I think Claude has been calibrated to do work faster, which means faster means worse because it's doing less reasoning. But it creates more engagement with the users. They're kind of engagement hacking. That's partly why people love Claude Code so much -- people feel like they're getting a lot done. But the reality is that the code coming out of Claude Code is very buggy.

**Joe:** Have you tried using Codex for code generation as well?

**Wes:** I do. But because I'm running so many reviews and the quality of reviews from Codex is so good, I try to save my tokens for code review. If I use it for a bunch of implementation, I just fully gas out my plan.

One week I gassed out my Codex plan in two days.

**Joe:** Nice.

**Wes:** And I had to go buy another plan because I was like a drug addict. I need the tokens. It's 5:30 in the morning. Let's go. Sam, it's 5:30 in the morning. I need the tokens. Where are the tokens?

I have used Claude as a surgical agent. Sometimes Claude gets stumped on something hard, and I'll have Codex take a look and Codex will figure it out. Yesterday I was working on something really thorny where I had all three agents investigating a tricky bug and eventually figured it out. I had three agents working on trying to figure something out for two hours. I had to burn a ton of tokens to debug what ended up being a one-line change. One of those classic things where, back in the caveman days, we used to beat our head against the wall for three days until we found the one-line change that fixed the memory leak.

**Joe:** Like a missing comma.

**Wes:** Yeah.

**Joe:** So you, 5:30 in the morning -- how long are you running these workflows for?

**Wes:** I'm still a human, I need some sleep. My friend from college on Twitter was joking about people using coding agents doing polyphasic sleep, waking up in the middle of the night to check on their agents. I have gotten up in the middle of the night to check on agents because sometimes I'll set them to work doing autonomous refactoring that might take four or six hours. That's all with RoboRev -- there's an autonomous fix mode. You can queue up a bunch of analysis and fix tasks one by one.

But mostly I'm sleeping during the night. I'll sleep from like 11 to 5:30 or six in the morning, which is probably not enough sleep. Typically I'll start working in the morning, make coffee. At some point I'll work out -- I have a Peloton. Maybe too much information, but I bought one of these plastic tablet holders. It turns out I can sit my MacBook Air on the Peloton. So I can work out for an hour on the exercise bike and keep an eye on my sessions and press okay and do stuff like that.

I do yoga. I'll set down the laptop while I'm doing yoga. I'm not making this up -- these are actual facts. I'll watch the screen while this is going.

I typically take a break to eat and I lift at the gym. I don't take my laptop to the gym, but the workflow is: get the agents busy with something while I go to the gym so they can do something productive when I'm away.

**Joe:** You could probably set up an OpenClaw setup for that. Just run everything at your house.

**Wes:** Yeah, OpenClaw. I haven't set up yet. I have a Mac Mini but I'm kind of like, okay, this is great, except I'm not going to give it any personal information. Passwords, credit cards -- I don't think I'm there yet.

I'm not coding with voice. I did buy a little C-shaped sofa table so I can put the laptop next to me if I'm watching TV at night. I play video games. The one thing that made me put down my laptop and focus on a video game was the new Resident Evil. That was where I was like, this only took 10 hours to get through, this deserves my full undivided attention.

But what I think is cool about coding agents now is that you can transform periods of divided or scattered attention into productive time. If you're on a Zoom call where you're not actively talking, you're listening, you can keep an eye on an agent session. It doesn't take that much energy to babysit an agent session.

**Joe:** I didn't think they'd keep you going. It's awesome to see. You're on a rampage, dude. Keep it up.

**Wes:** Yeah, try to get some sleep.

**Joe:** Overrated.

**Wes:** It's been inspiring seeing what you're doing too. I was on like, not exactly a hiatus, but I was working on a startup for five years, COVID happened, I wasn't super active developing since 2020. To get back into my stride, back into project creation motion, definitely feels really good. But to be able to do it with agents and without nearly so much of the drudgery is a breath of fresh air. Software engineering could become a little bit tedious and not fun. All of a sudden it feels fun again.

Part of the reason I really liked Python in the early days was that it gave you this feeling of being able to just sit down and write some code and get things done.

**Joe:** And build a spreadsheet called Pandas.

**Wes:** Yeah. And as time went on, Python became a little bit Java-ified, if that makes sense. It developed a lot of development process and types and development infrastructure, which is all there for good reason. But I feel like it made Python a better language for large teams and for software engineering at scale. It also took away some of the pure joy of being able to sit down and just write some Python code and make it go.

People are building stuff in Python now that they would have built in Java 20 years ago. Obviously we can't build the software of today the way we built small projects in Python 20 years ago. But the feeling I get now is that same joy of productivity I felt in the early days of Python, circa 2008, 2009.

**Joe:** Well, till next time, man. So good to see you.

**Wes:** Later. Thanks Joe.