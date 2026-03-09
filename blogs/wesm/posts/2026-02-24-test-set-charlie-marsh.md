---
title: "More productive but a lot less fun — with Charlie Marsh"
summary: "Podcast at The Test Set (Posit)"
date: 2026-02-24T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-charlie-marsh
word_count: 17417
source_file: transcripts/2026-02-24-test-set-charlie-marsh.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://www.youtube.com/watch?v=NoxoQHhrkoc"
---

{{< video https://www.youtube.com/watch?v=NoxoQHhrkoc >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, Michael Chow and I sit down with Charlie Marsh, the creator of Ruff, uv, and founder of Astral, the company building high-performance Python developer tools. We recorded this one in person in Times Square, New York. Charlie walks through how he taught himself Java in high school, studied CS at Princeton, worked at Khan Academy and a computational biology startup, and eventually started building Python tooling in Rust because he felt Python was "succeeding in spite of its tooling."

A good chunk of the conversation covers how Astral's tools gained adoption. Charlie explains that Ruff succeeded by being drop-in compatible with existing linters while being orders of magnitude faster, which inverted the adoption calculus from "why should I switch?" to "why wouldn't I?" For uv, the team was intentional about starting with a pip-compatible interface before rolling out the new uv run/uv lock/uv sync workflow. I share some history on the Python packaging mess, how Conda emerged to solve the polyglot dependency problem, and the ongoing challenges with things like CUDA runtime versions and statically linked libraries like gRPC and protobuf.

We spend a significant portion of the episode on AI and coding agents. Charlie describes his current workflow: four Claude Code terminals running in parallel, almost exclusively using agents for implementation, with his editor now mainly for reading code and touch-ups. He shares candid feedback from his team that they trust his PRs less now because agent-generated code introduces patterns and mistakes he wouldn't have made before. I relate to this, describing my own similar workflow and the code quality problems I've noticed, especially bloated and duplicated test suites. We both discuss "adversarial code review" as a strategy, since asking an agent to review its own code produces overly positive assessments.

The conversation turns to bigger questions: does code quality even matter if agents are writing and reading it? Charlie acknowledges he doesn't know, but thinks different projects will have different answers. He notes that in TY (Astral's type checker), merging every agent-generated PR would destroy the project, while in their Python frontend, it would probably be fine. I raise the idea that Python may lose ground to compiled languages like Go and Rust for agent-driven development because the agentic loop is faster with faster test suites and easier distribution. Charlie doesn't dismiss this but says Astral wants to figure out how to make Python a great choice for agents, potentially through faster test infrastructure or standalone binary support. We close by discussing the "Lisp Curse" parallel: just as Lisp's power disincentivized collaboration, coding agents may do the same to open source by making it easier to fork and move on than to engage with maintainers.

## Key Quotes

> "I feel like working with agents is a lot more productive but a lot less fun." -- Charlie Marsh

> "People on the team felt like they couldn't trust my PRs as much anymore, which is completely fair and very interesting. Previously when people were reviewing my changes, they didn't feel like they had to review them super closely. They trusted my work a lot. And now if I'm putting up a PR that's done by Cloud Code, empirically, I'm putting up code that has patterns or mistakes or issues in it that I just wouldn't have put up before." -- Charlie Marsh

> "I think it's a hard time to be a leader because there's so much uncertainty." -- Charlie Marsh

> "The whole model for how people discover and start using new open source technologies is going to have to change. Otherwise we're going to end up locked in the present moment -- nobody uses anything new because their LLMs don't know how to use it." -- Wes McKinney

> "Why bother doing open source when you can just fork the project and make it exactly the way that you want?" -- Wes McKinney

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field. In this episode, we sit down with Charlie Marsh, the creator of Ruff, a mind-blowingly fast Python linter. He's also the founder of Astral, where he and his team have built tools like uv for package management and Ty for type checking, and I have to say they've really taken the ecosystem by storm. Later in the conversation, Charlie talked about his heavy use of AI for development, including whether his AI use reduces his team's confidence in his PRs today. And regarding AI, he told us, "I think it's a hard time to be a leader," and I'm still chewing on that. All right, let's get to it.

**Michael Chow:** All right, Charlie, welcome to The Test Set. We're in Times Square, and joined by my co-host, Wes McKinney. So excited to have you on. I'm a giant fan of Ruff, and I know you started a company a few years ago, so you're the CEO of Astral, making blazing fast Python tools. Thanks so much for coming on.

**Charlie Marsh:** Yeah, absolutely. It's great to be here. I live here in New York. I don't come to Times Square every day, so it's also exciting to be here in Times Square and on the show. Yeah, I'm Charlie. I'm the founder and CEO of Astral. We build high-performance developer tools focused on the Python ecosystem, so we're very focused on our open-source tools. Ruff is one that you mentioned, it's a static analysis tool, and then we also build uv, which is our package management tool, and a couple others.

**Michael Chow:** Yeah, awesome. Yeah, and I'm so excited. You have Ty recently, too, which is doing a lot of the type checking.

**Charlie Marsh:** Yeah, exactly. Yep, yep. So we recently released Ty, it's our type checker and language server, and so that came out of beta just before Christmas in December. We kind of work across, we think of it as like two domains. We build a lot of static analysis tooling, so we have Ruff, which is our linter and formatter, Ty, which is our type checker and language server, and then we have uv, which is our package manager. And then we also do our own builds of CPython, so there's kind of two big areas that we play in in the open source.

**Michael Chow:** Yeah, I feel like it's wild. The past few years, I feel like Ruff, uv, and I'm sure Ty have just taken over kind of everywhere, and I'm so curious to talk a little bit more about those tools. And I do also want to flag, I've seen a lot of your recent tweets of using things like Claude Code and AI, so I'm so excited to get into both this really interesting set of blazing-fast tooling, but also this AI component that has sort of emerged, I feel like, over the last...

**Charlie Marsh:** Yeah, 100%. Yeah, I'd love to go deep on that. I mean, I feel like work is changing so fast, even month over month, the way that I work, the way that I see our users working, and even the way that we build our own tools, Ruff, uv, Ty, the way that we've tried to fold in Claude Code and Codex and all these other tools has really changed how we develop. I think it's also changing in ways that we, as an industry, haven't really figured out. It's also changing open source in a lot of ways, and what the engagement and the interactions look like between contributors, community, maintainers, so yeah, there's no shortage of things to talk about there.

**Michael Chow:** I think one thing I'm curious about, before we jump into... I'm curious to hear a little bit more about you and kind of how you got into software engineering and stuff. How'd you get into the field?

**Charlie Marsh:** Let's see. I mean, I taught myself to program the summer before I went to college, so that's what I did with my summer. I read a textbook on programming with Java. Java was my first programming language. And then, by the time I got to school, I think I really enjoyed it. I was pretty convicted that I wanted to study computer science, so I did. I went to Princeton, I studied computer science, and from there, I've worked as a software engineer ever since. My first job out of school was at Khan Academy, an education technology non-profit. I was there for a couple of years, and then I went and worked at a computational biology company. I had no bio background. I also had really no ML or computation background, so I was largely responsible for the software infrastructure and the data infrastructure and a lot of machine learning infrastructure that we built up over the course of a few years.

I guess the way I look at why I started to work on all this Python tooling was that, well, I think there were a few threads that came together. One was, everywhere I'd worked, we just had a lot of Python, especially when I was working at Spring, which was this AI-enabled biotech company. We were doing scientific computing, so we just had tons and tons of Python. I was always on small teams trying to do a lot, and so we were trying to take advantage of tools, and Python, to me, always felt like a language that was succeeding in spite of its tooling. It just kept growing and growing and growing, but the tooling... I mean, there were things happening, but it didn't quite feel like it was accelerating the language.

**Wes McKinney:** I remember the first time I met you, I was introduced to Charlie when he was just starting Astral, so we'd never met before that. I think I had just heard about Ruff, or it was just Ruff at that point, and so I remember meeting with you and thinking, I'm like, okay, he seems really smart. There's Ruff. Ruff's clearly very fast. It's a linter. I was like, okay, a company for a linter. How can a linter be a company? But I'm like, oh, he seems really motivated, so yeah, I'll let him run with that and see what happens.

But I think, to me, it's honestly amazing what you and the team have pulled off in a short amount of time, because, in a sense, I've been involved in Python for a long time. It's almost 20 years now. I started doing Python in 2007, and so things have obviously grown and changed a lot during that time. But there was always this feeling that, with each passing year, that Python is getting better and worse at the same time, if that makes sense. We have all these nice tools and libraries and things, and look at all these problems we can solve, and the community of Python developers is getting bigger, and more and more people are choosing Python. I remember just getting from the point where Python was a language that was a niche hacker language or something that was a little bit underground. You had to be an enthusiast, if you ever remember Paul Graham's Python Paradox essay. So a lot of people were choosing Python, but it was not a popular thing. The fact that companies such as Dropbox were using Python was considered avant-garde. Like, oh, Reddit uses Python. So people would talk about companies using Python, but it wasn't a mainstream language.

And so somewhere in the early 2010s, it crossed the chasm from being not a mainstream language to being a mainstream language. But then there was this explosion of tools and development and different things, and you had everyone grappling with, like, gosh, how do we manage our environments? How do we deploy our code? And basically, just things turned into this giant tangled mess where every project was doing things a little bit different way, and so companies would do things differently. They'd be like, oh, we're using this packaging and virtual management tool, and like, oh, we're using Conda over here, or like, there's many different ways you can install and deal with Conda, and there's different package channels. And it was just a giant mess that everyone would complain about, and it was making nobody happy.

And then there was also the friction between the scientific data machine learning ecosystem, now the AI ecosystem, and the traditional OG Python web developer community. And so you had folks who didn't have any compiled code at all, like no C extensions, no Rust extensions. Maybe this was even pre-Rust, like we weren't even thinking about Rust at that point.

And so we would have these conversations. I remember at one point we talked to Guido van Rossum, the creator of Python, about the whole packaging conundrum and how it's a giant mess. And his reaction was kind of like, oh, well, maybe you should build your own packaging and installation solution to solve this problem.

**Charlie Marsh:** And that became Conda, right?

**Wes McKinney:** And that became Conda, and what's now Conda-Forge, and all that. But yeah, I think the fact that you stormed onto the scene and made a difference in a short amount of time is -- considering how many failed attempts there were at doing that -- frankly kind of amazing.

And so I think one question I have is, what made you decide, I can fix this, I'm going to do this? Did you kind of visualize where things would be today and how rapidly the Python ecosystem could change? And then what are some of the things that you think, what were the catalysts, what was the tipping point, or how do you feel that rapid hockey stick-type growth for uv in particular happened?

**Charlie Marsh:** Yeah, definitely. So I think when I decided to work on this full-time and start a company and bring people on board, I certainly didn't have everything figured out. I mean, I probably still don't, although I hope I have better ideas now than I did then around how the company will grow. But I did have at least a clear set of things that I thought we could build.

And for me, it was really, Ruff was really starting to succeed. And I think it was also showing me evidence that people would change their tools. If you could do a few things, right? Like one, you had to build something that people really believed was significantly better than whatever they were using. It's very hard to get people to switch tools if it's going to require a bunch of changes in their workflow, and it's only a little bit better in these one or two ways. Why would anyone spend time on that?

And with Ruff, I think the way that I tried to view it was, okay, we want it to be very compatible with your existing tools today and orders of magnitude faster, hopefully. And so for a lot of teams, it was like, well, if it's drop-in compatible and it's orders of magnitude faster, you kind of try to invert the calculus around, well, why wouldn't I switch? We should do it.

I think the project was also bolstered a lot by early adopters who had important projects and big presences and were willing to give it a shot, like Sebastian Ramirez from FastAPI. He was pretty early in the issue tracker asking for things. Or like Samuel Colvin from Pydantic. I just thought, if we're just kind of ruthless about thinking about what those people need in order to migrate and really focus on trying to do those things, I think it gave the tool a lot more social credibility early on. So a couple of projects migrating over, and then we started to get projects that are much more established, like SciPy migrating over. And I was like, okay, if that's happening, if those projects that have been around for decades are willing to adopt this sort of radical Rust-based tool where I'm shipping a release every day and I have no versioning policy, then to me that was basically a sign that there was a lot of demand if we could build something that was really good.

I think I always assumed that the packaging adoption curve would be much more difficult because it's closer to production, there's a lot more ways that people work, people are very ingrained in their workflows. And I think we did a couple things right there. One is we started with this uv pip interface. Actually when we first shipped uv, that was all there was. And a lot of people were like, oh, that's weird, why is it like uv pip, it should just be uv install. But it was very intentional, it was like, that's kind of like our compatibility layer. It's kind of the old world.

**Wes McKinney:** Yeah, in some ways.

**Charlie Marsh:** And I think people didn't realize what we were even pitching with the new world at that point, which is fine, but that was the thing that we shipped to start.

**Michael Chow:** And just in case, I think uv's kind of like taken over the world, but just in case someone hasn't heard of uv, how would you explain it?

**Charlie Marsh:** Yeah, yeah, of course. I mean, I view uv as our sort of like all-in-one Python packaging binary or toolkit. So it's a single binary that you install that will install Python for you, manage your Python installations, and those are Pythons that we build. It'll automatically create virtual environments for you, it'll automatically lock and resolve your dependencies across platforms. So it's designed to be extremely fast, and like our other tools, we really thought about in building it, we wanted to build the entire stack in a very cohesive way.

I think one of the things that's been hard in Python tooling is you often have lots of different tools that are built separately or built on top of one another. And for us, it was like, okay, we're actually going to try and do basically everything ourselves from maybe except the runtime, like we do our own Python builds, so we don't have our own runtime. But then it's like the virtual environment layer, the lock file, the resolver, the package installer, it's all one system.

And when we launched, we were very focused on compatibility because we wanted to build something that was easy to adopt, that demonstrated the performance piece, and let us get something out and get it battle-tested. So we just had uv pip install, uv venv, these were meant to be very close to drop-in alternatives for pip and virtualenv. And that actually grew a lot, but after six months or so, we launched a whole new interface, which was uv run, uv lock, uv sync, and you should be able to clone a project, you just do uv run, and then we resolve the dependencies, install Python, create the virtual environment, wire the dependencies up to your runtime and run the command. And all of that should happen without you having to really think about it.

**Michael Chow:** I'm so curious, I know like Ruff, like between releasing Ruff and I think between releasing uv, you started a company and became CEO. And I noticed you're using "we" a lot with uv, I'm really curious the kind of design and the process that went into that from being, like I'd imagine when you were building Ruff, you were sort of like a solo creator, and kind of up to the point of uv, you might have had a crew. Could you tell us a little bit about that?

**Charlie Marsh:** Yeah, yeah. Of course. I mean, building Ruff was like, at least the version up until the first, we hired our first team member, it started like March 2023. So it was actually, between starting a company and hiring our first team member I also had a kid. So it was a really crazy period of my life.

So like Ruff, yeah, the initial Ruff codebase, it was me sort of figuring out how to do things. I think our code quality has gone up a lot over time, especially as we've hired people who are much better than me at Ruff or more experienced than me at Ruff. But yeah, we started working on Ruff and we grew the team, we've always grown the team. The word I often use is like, deliberately. We were usually hiring, but we're not usually like hiring a million people. So we grew the team from like one to two to three to four. I think when we launched uv, we might have been like six or seven total.

**Michael Chow:** Are you all remote?

**Charlie Marsh:** Yes, we're all remote. So I'm here in New York. We have two other people here in New York. I mean, they just sort of happened to be here in New York. And then we have team members, we're about 23 now, and we have team members from Pacific all the way through to CET, like Germany, Switzerland, and then we also have one team member in India. So we try to span a lot of time zones and learn to work together remotely in an effective way.

But I would say in terms of building out the team, it's been pretty amazing. I think I'm stunned at the quality of the team that we've been able to put together. And I think a lot of that is, we're kind of a unique and different company. If you want to work on programming language tooling written in Rust, and now we have massive distribution with the stuff we've built, so everything we ship has a really big impact. Open source, remote -- we've been able to bring in a really amazing team.

And there were sort of a couple philosophical points that I've thought about over time with building the team. One is, we've intentionally tried to hire people from outside the Python ecosystem. We've brought in, because I wanted to bring in a lot of different ideas from how other programming ecosystems work. So we've brought in a bunch of people from, I think that would be best known for their work in the Rust ecosystem, for example. Mika, who was like the third person to join the team, had basically never written any Python before, but he'd built very similar tooling for TypeScript. And so he brought a lot of knowledge about what it looks like to build these tools correctly, but in a different context. And I've learned so much from him.

At the same time, I think it's really important that everything we do, all of our success, basically comes from having a really good understanding of our users. It's not a unique observation. I think most companies would say that. But for us, a lot of the ideas for Ruff and uv came from our own time working in Python. So we've also brought in people who have been involved in the Python ecosystem for a very long time, like Carl Meyer on our team was one of the authors of the virtualenv PEP and he was very involved in Django early on.

So we try to make this mix of people with very different programming backgrounds and bring them together in a very collaborative and fun environment. And I think that's been really successful for trying to build tools that work for a lot of different people.

I mean, I think to your point, building in Python is very interesting and it's challenging because every company on earth is using Python for something within some margin of error. But the things they're doing can be super different. Some companies it's like they're building a huge web application and it's a giant monorepo that's all Python. Some companies it's like they're all Ruby, but they have an AI/ML or data science team and they're obviously all using Python. Some are research labs, even that's pretty different. Some are like it's all build scripting or networking or whatever else. And so you're building for a very diverse user base and we're trying to build things that work both for beginners but can scale to enormous projects. So we've put all these hard design constraints in place where we're trying to satisfy all these different people.

I think we do a good job managing it, but to me it feels quite different than, I mean the TypeScript ecosystem is absolutely enormous, but most people building in TypeScript are building web applications and the applications can be very complicated, but the user story I think is a little bit more straightforward. For us, we have our feet in all these different communities, just like Python is.

**Wes McKinney:** Yeah. I mean, I think from what I've seen, from the segment of the Python ecosystem that I come from, originally the SciPy, NumPy, scientific computing ecosystem, which turned into the PyData ecosystem, and now of course it's all AI and all the most popular Python repositories on GitHub are AI related. I actually looked at the top 100 Python repositories by GitHub stars and most of them I haven't even heard of. There's something related to AI or LLMs.

**Charlie Marsh:** Totally mind-blowing.

**Wes McKinney:** But it's interesting because I think in my world, I've had a lot of exposure to companies that have a lot of stuff that's written in Python, but then a lot of other software which is not written in Python and stuff that has to be built and deployed. So it's not just library software, but it's stuff that has to be built and deployed with the Python. And that's why, even still for many years and even still, I became a big proponent of the Conda, Conda-Forge way of doing things. Basically a cross-language binary package system where you can have all of your system libraries, all of your C, C++ libraries, Rust libraries.

**Michael Chow:** Can you give some context to Conda? Like what's Conda to kind of a general audience?

**Wes McKinney:** Yeah. So Conda is a packaging tool originally written in Python. Now there's a C++ package resolver installer, like parallel resolver installer backend called Mamba or LibMamba that powers Conda. But originally it was all written in Python. It was developed by Continuum Analytics, which is now Anaconda. And it was basically an evolved approach to Python packaging that would allow you to package Python libraries, but also non-Python application dependencies.

And so the idea is that you could have an application that has R in it or that has something written really in any programming language. You could imagine it as being like a non-OS specific version of a Linux distribution. So if you think about using apt or yum or a Linux package manager, you have access to this whole compendium of all these libraries and tools that have been packaged so that they can be installed in Linux. And so whenever you're doing apt install this tool, apt install that tool, you don't care what programming language that is as long as the libraries and the bin files end up in the right place. And so Conda is like that except that it works on every OS and it's not OS dependent. So you can have a single Conda environment definition that you can use on Windows, macOS, Linux, and they figured out how to make the binaries that ship in a Conda package channel portable across Linux distributions.

Python also had to solve the same problem of Linux distribution portability for binaries with the manylinux specifications. So Conda essentially was a whole parallel world that was created for solving packaging and distribution for polyglot stacks. Yes, Python, but also all the other things. A lot of the banks in New York City are Conda users because they have large complex C++ codebases that they need to package and version alongside their Python libraries. And so using pip to manage everything, or now uv to manage everything, actually wouldn't be practical because you would have to figure out how to take those non-Python things and turn them into things that uv and pip can install.

But this is interesting because this is actually the exact problem that all the AI libraries have had to solve to figure out how to get PyTorch and all the CUDA runtime libraries just magically pip installing. There was a period of time where you actually couldn't pip install and get everything you needed. Things went through a messy period where you could pip install PyTorch, but there were PyTorch versions for different versions of the CUDA runtime, and it was just a giant mess and very painful for everyone.

And so I can imagine with the rapid growth and everyone wanting to be able to uv pip install or uv add packages that depend on a complex... essentially it's like the Python part is the small part. It's actually these gigabytes of CUDA libraries and stuff, all the packages depend on that also now have to get installed. Otherwise people get into this morass of, oh, I have to go to the NVIDIA website and figure out, oh, this Python package depends on what version of the CUDA runtime? Make sure I install exactly that version and I don't have a version conflict where it doesn't link when I import the Python. I've of course suffered greatly from these problems over the years.

**Michael Chow:** So I feel like you've solved it. Like this problem has been solved at least for the AI stack, but still there's a lot of other underserved applications that if you want to have Python and other stuff, I think Conda is probably still the right solution, but maybe in the fullness of time the uv world can expand to maybe solve that problem and do it better. Just kind of recap, you're saying Conda, if I want to install GeoPandas as a classic thing, it's like GeoPandas has some Python, but also a bunch of other libraries.

**Wes McKinney:** Well, I'm sure that you can install GeoPandas with pip, but what happens with the Python package index... I understand you're also building an alternative to the Python package index or maybe something like that. We can talk more about that. But the idea is that whenever you deploy a library like PyArrow or GeoPandas to the Python package index, there is a requirement on the Python package index that all of those binary packages that you deploy are self-contained. And so any system libraries that they depend on, so if there's C or C++ libraries or Rust libraries that your package depends on, those have to all be fully self-contained. So they have to be either bundled and ship inside the wheel, inside the Python package, or they have to be statically linked inside your C extensions that are inside the library.

And so the outcome of that, for better or for worse, is that whenever you pip install stuff, you end up with a lot of libraries that have all these C and C++ libraries that have been statically linked. So just tying back to uv, you're saying Conda solves a really big problem. If I'm pip installing and it requires other things, I'm going to have a bad time. But uv has made a really good time in Python -- it's fast, it's good.

Just to give you an example, one library that often ends up statically linked into Python packages is gRPC. So that's Google's RPC messaging library. And so there's a lot of projects that need to use gRPC, but if you want to use gRPC, you have to statically link it. And so you might install two Python packages that have different versions of gRPC, which also depends on protobuf. And so there's situations that people get into where they import Python libraries in the wrong order, and they get some kind of weird linker error because there's some conflict whenever the two libraries load their incompatible statically linked versions of libprotobuf. And this is still a problem that plagues us greatly. And so the better scenario would be if the offending library dependency, libprotobuf or libgRPC, is actually something that can be managed by uv. And so it isn't having to be statically linked, and the static linking is something that's required by the Python package index.

And so I'm optimistic, because I think this is a problem that Charlie can solve. He's solved all these other problems. But I'm getting ahead of myself.

**Michael Chow:** Charlie, please. I believe in Charlie. We brought you on here. Commit to us.

**Charlie Marsh:** Well, I mean, I actually feel kind of lucky, because I think we started building uv at a moment in time where it became very practical, in some sense, to build, because there was a lot of work that happened in standards in the years that preceded working on uv. I think it would have been a lot harder to build uv a few years before.

**Wes McKinney:** You mean like pyproject.toml?

**Charlie Marsh:** Yeah, yeah. Just like there were a bunch of Python standards that happened that formalized various behaviors or made it so more things were available statically, and you didn't have to depend on Python to do a bunch of other things.

And I remember, I think there was, I'll probably misparaphrase this slightly, but after we released uv, one of the reactions that I saw from a pip maintainer was something along the lines of, "I actually think it's great that this is possible. It's very good for the ecosystem for there to be multiple installers that follow the same spec and the same standard."

And the fact that that's possible is actually very good for the ecosystem. You don't just have pip as a de facto standard of how things work. You have a set of standards that are written down and codified and evolved through a governance process, and then tools can actually implement those.

And so I think similar with bundling extension modules, like Python packages where you're including Rust or C or C++ code or Fortran or whatever else, that is now so normal, and there's been a lot of standards work to make that possible. I think at the period of time when Conda emerged, that was not seen as something that the Python ecosystem was treating as a priority. And now, that's the superpower of Python, at least from my perspective. The fact that you can do that, I think, is really amazing.

And we're continuing to try and push the standards there. We're working on a proposal with people from NVIDIA and PyTorch that we call Wheel Variants. It's now up for comments, so it'll be a big debate around whether that actually happens, but there's still a lot of evolution in terms of those problems.

**Wes McKinney:** This is for that CUDA runtime version problem?

**Charlie Marsh:** This is for being able to encode... Right now, when you build a Python file someone can install with Python, you encode certain things like the operating system -- Windows, Linux, macOS -- and maybe the CPU architecture like x86 or ARM. But there's a bunch of stuff that you can't really encode in any way. Does it depend on CUDA? If so, what driver version does it need? And so this is trying to generalize that problem. I think parts of it are definitely learning from the Conda ecosystem and looking at how Conda approached things.

That's what I always view as the most important part of standards and language and ecosystem design is you have to learn from what other people have done. You don't have to do exactly what they did, but you should be very curious about why they made certain choices and how those have played out.

So that's just to say I think Python packaging is still evolving a lot, and I'm optimistic that we can push it forward. There are also things that we've done in uv that have then, either there are ambiguities around how things should behave and then it leads to a lot of clarification of like, well, the spec isn't clear about this, what should we do? Or things we've done in uv that have then turned into standards proposals, which has been cool to see.

**Michael Chow:** I feel like that is an interesting kind of challenge or maybe design path too with Ruff and uv of ambiguities. I know a lot of these tools, you mentioned compatibility, so really being sure that it enhances people's experience but is often compatible with, say, pip or Ruff used a lot of existing linting rules, which is a great bootstrap into the tool because it's often things people already know. I'm curious, that philosophy, how that's worked out as you've kicked the tools off and as the tools mature?

**Charlie Marsh:** Yeah, I would say we try to be very intentional about where we knowingly are incompatible or make very different decisions. We try to document those. An example would be with pip and with uv, if you try to install packages across multiple different indexes, like maybe you have your own private index and PyPI and you want to configure the tool to look at both, how the tools make decisions about which one to look in and where to get packages from are different, and that was a very intentional choice that we made largely because we thought our design was more secure.

We got a lot of user complaints about it because people were like, this is different, and in some sense that's very justified, but we try to be very principled about where we break compatibility or where we do something different, and then we also try to listen. There are some areas where we really changed our mind about things. A week or two after we shipped uv, we made a pretty big breaking change because there was a very confusing behavior around what counts as a project and what doesn't, and we were constantly getting reports, we were getting tons of reports of people being just confused about this behavior, and we were like, okay, we took a very principled stance on that, but it's clearly not working out, and so we were willing to correct course.

So I think being open-minded about it and also being mindful of where the tool is at in its maturity cycle. I said this earlier, but when I was working on Ruff initially, I was shipping a new release literally every day, sometimes twice a day, and they would have all sorts of things. Sometimes they would have breaking changes, and it sort of got to the point where I would ship a release, and there would almost always, within five or 10 minutes, be an issue that was some kind of regression or something that broke people's workflows, and there was a moment where I kind of had to change my act.

That way of working makes sense for a project at a certain stage in its life, but as the project became more mature, we had to get way more serious about how often we ship, having a clear versioning policy.

**Michael Chow:** You're doing a lot of QA.

**Charlie Marsh:** Yeah, a lot of QA, all that kind of stuff. So we just evolved that a lot over time. In some ways, it's like a productivity tax, but it's a very important one to pay. Eventually, we put in a versioning policy, so now we do not ship breaking changes outside of -- we use patch and minor releases, but the point is we have a very clear versioning policy. We ship more like once a week, all that kind of stuff. We have a whole preview system, whereby whenever we add new features, by and large, we put them under preview flags, and then there's a period where we take commentary on it, and we sort of reserve the right to make breaking changes while the preview flags are up. It's just changing over the course of time how the project works and how it operates, I think is pretty important. It's fine to ship breaking changes if you're a very new thing, but eventually, the project's adopted, and you have to view how you release and how you ship very differently.

**Michael Chow:** Yeah, it's really interesting, because these are such big projects and communities. Maybe to shift a bit, I saw you've mentioned a lot about Claude Code and using AI in Claude Code quite a bit.

**Wes McKinney:** One thing I wanted to say on that is I think one of the reasons I've become such a big fan of uv is actually because of AI. One thing we didn't really talk about is that one of the problems that uv solves is this whole problem of, like, I made a thing, I want you to run my thing, because it used to be that you had to say, you've got to create a virtualenv, and then you've got to install stuff, and you've got to activate the virtualenv. It was this whole kind of nightmare. But now I can say, here's my Python script, just uv run this, and don't worry about it.

So I think that feature was developed pre-AI, but yet is also the killer app for making self-contained, runnable things that are outputted by coding agents. I do feel like step zero of Claude Code with Python is ensure that it's using uv.

**Charlie Marsh:** It's people's number one priority, just for sanity.

**Wes McKinney:** It's like, we're always using uv. Do not pip install. If I see it pip installing or using pip, I'm like, escape, no, do not. Only uv. It will still ignore me sometimes, but...

**Charlie Marsh:** Yeah, yeah, yeah. I think the models are getting better about it over time. I think there's more, hopefully, RLing in the labs of get it to use uv. I think there are also Python users, and so I think they're also on the bleeding edge. There are also uv users, yes.

**Wes McKinney:** Well, anyway, I guess to Michael's point, curious on your journey with AI. We were looking and you've been doing stuff with AI and large language models for a lot longer than many people, and so I'm interested just, how things have developed, what your current workflow looks like, and what's been your path to getting there?

**Wes McKinney:** So, just for context, I saw in like 2022, you had an experiment called Autobot. Like, you were kind of on the bleeding edge, tinkering with tooling.

**Charlie Marsh:** Yeah, Autobot was one of the projects I was working on when I also started working on Ruff. I had a couple different projects going, and that was AI-assisted code mods refactoring, so you would give it a few examples and then it would find others in your codebase to apply the same pattern. I mean, it's pretty straightforward, but it was very early for that, yeah.

**Michael Chow:** Yeah, it's actually mind-blowing for me to hear that you were working on Ruff and Autobot at the same time.

**Charlie Marsh:** Yeah, it was the same time, yeah. But yeah, I mean, I've gone through just so much change. Even comparing November to now, I think the way I work is really different.

For me, I think there was a long period of time where I was in IntelliJ IDEs, just using Copilot for tab completion, and that was a big step up from normal tab completion, and then I remember I'd go on an airplane and I'd find it very hard to write code because I couldn't tab complete.

And then I started using Cursor, and again, that was really about the really great tab completion that felt like it was predicting what I wanted to do next and jumping me around the file and across files, and the Command-K sort of more targeted editing, where I'd highlight a bunch of code and I'd say, rewrite this to do X, Y, and Z, or give me an implementation for A and B. But I wasn't really using agents very much, and I was pretty bearish on them, I guess, because I'm short-sighted, and they weren't feeling reliable. I just didn't feel like I could trust the code.

So there was a long period of time, I think a lot of last year, where I wasn't really using agents, but I was using Cursor really heavily for Python and Rust. And I felt like for a long time the models were way better at Python than they were at Rust, and I think that also impacted my own adoption or perspectives on things, because I mostly write Rust. But our hosted product, PYX, is written in Python, a lot of it's in Python, and that's actually a very intentional choice, because we want to be using our own tools to build a thing, which I think has been really good.

**Michael Chow:** I'm curious, did something tip the scales for you? Like you mentioned using AI for suggestions or the really beefed up autocomplete, and then now it seems like you are using agents a lot. I'm curious if something shifted.

**Charlie Marsh:** Yeah. I mean, now, for me, I still use my editor, but it's mostly for reading code, or maybe making touch-ups if I have a complicated change that I want to finish up on my own. I would say since at least the beginning of December, maybe earlier, I am exclusively using Claude Code and Codex, and I really just run those locally. I don't really use the web products too much, although some people on our team do.

So basically everything I'm doing now is going through Claude Code or Codex. I'll just say what I do locally. I'm typically working on a bunch of things at once. I think that's actually been the big unlock for me, is it's not always the case that it can do any one thing way faster or way better than I could, but I can parallelize or multitask a lot more. I'm using it for Rust too. I think the models have gotten significantly better at Rust, and so for Ty, for uv, for Ruff, any change I make there will start with a Claude Code session, and then same for PYX or for anything else that we do.

The way I work now is I have maybe four terminals open. I'm not doing like 20 different terminals all yolo-ing on something.

**Wes McKinney:** Just four.

**Charlie Marsh:** Yeah, it's more intentional than that. It's like, I'm working on four changes, and once it's done, I'm kind of reading the code, prompting more, maybe going in and making some edits myself. I would say increasingly, though, when there are small things I want it to change, I'm telling it the small things I want it to change rather than editing the code myself.

I mean, I think the main thing is agents are just becoming more and more capable. I do think using them well is a skill like anything else, and I think it's very easy to use them poorly and also to get burned on them and think they're not useful. Because they're billed as this magical thing, and then you try it, and if you just sort of walk in and try it for something and it doesn't do it right or it makes one of the mistakes that I would recognize as the unobvious thing that an LLM might get wrong, like, okay, it tells me something that's not true -- a lot of people will have that interaction and they're like, I can't trust it for anything. I actually think that's not right. I think it's a skill like anything else to figure out how to use them well, when to accept what they believe, how to get them to validate it.

Obviously it's bad if the thing is telling you something that's not true, but I think as you use it more and more, you start to identify why that would happen, how you can avoid it. So I view it as very much a skill that you can get better and stronger at.

And a big thing that I say a lot with the team is, so much of our success has come from having a deep understanding of our users and increasingly our users are building with agents. And so even if we don't want to build with agents for whatever reason, we sort of have a responsibility to, because at least I feel that way, because I need to have a really good understanding of how people are working and how programming is changing, how people are using our tools. That's why PYX being written in Python, we have a big Python project where we're using uv, Ruff, Ty, big monorepo.

**Wes McKinney:** So if you're not building large applications in Python, then you're not experiencing what it's like to...

**Charlie Marsh:** Yeah, exactly, and with agents, right? And so I think as a team, we're this mass of people all trying to figure out how to use these tools in different ways, and we're learning a lot from each other, but it's also changing super fast. And I think the best thing, at least from my perspective, the best thing we can be doing is just experimenting and trying things and viewing that as a core part of the job, to learn and understand how this stuff works.

**Michael Chow:** Do you have any advice for people maybe looking to contribute to Ruff or uv or things like that who are dipping their toes into agents?

**Charlie Marsh:** It's a challenging time, yeah. I would say, there are certainly a lot of projects that have publicly put out AI policies in different ways. Like, I think tldraw stopped accepting external PRs or something to that effect. And then I know Ghostty has a very specific AI policy. We're not there yet. I think it's almost guaranteed that we will be.

But I think the thing that's challenging is writing the code, a draft of the code is not expensive. That is the cheap and easy part. The hard thing is validating correctness, thinking hard about the architecture, all these things that come downstream of writing code.

And so increasingly what we see is, an interaction that I don't really know what we do about, but it just doesn't really make sense, is we have an issue, a contributor takes it, they just drop it into Claude Code and say, "fix" and link to the issue, and then they just put up the PR. And then it's like, what's the point of that? Because I could just do that, right? And the hard part is what happens after, which is we have to give a bunch of feedback, we have to think hard about the change, we have to think hard about how you validate it. And if the person who puts it up hasn't done that work or thought about doing that work, that is the hard part. It's like, I can prompt the agent.

So it's a lot of, I guess I call them slop PRs.

**Wes McKinney:** Well-intentioned.

**Charlie Marsh:** Yeah, well-intentioned, yeah. Often well-intentioned. But it does create a weird dynamic because for us it's, we get a huge PR, we kind of have to think through, well, how do we engage with this? Is the person going to engage if we ask them hard follow-up questions? Or maybe they're like, we have all these questions, well, what should I do next? And we're like, well, that's actually the hard part is we don't really know what you should do next. You have to kind of do the work of figuring out how do we develop confidence in the change.

And so I think we're trying to figure out how to navigate that. And it's not even exclusive to open-source contributors. There are elements of this, too, that happen within the team. I got some feedback, which I really appreciated, which was that people on the team felt like they couldn't trust my PRs as much anymore, which is completely fair and very interesting.

Because the point was, previously when people were reviewing my changes within the team, they didn't feel like they had to review them super closely. They trusted my work a lot. And now it's like, if I'm putting up a PR that's done by Claude Code, empirically, I'm putting up code that has patterns or mistakes or issues in it that I just wouldn't have put up before.

**Wes McKinney:** Do you feel like your trust or confidence in your PRs stayed the same?

**Charlie Marsh:** No, I mean, definitely gone down.

**Wes McKinney:** Fair.

**Charlie Marsh:** I think I'm still a lot more productive, but this is why it's a very challenging moment to figure out how to think about these things. And sometimes, too, a bunch of stuff gets pointed out on a PR. What it took for me to realize this was I put up a PR, and I will try to review my PRs myself first, but it's a little different when it's code that you've been close to and writing. But I put up a PR, and I thought it was fine. And then I got a lot of feedback from someone on our team who's great. And he looked at it really closely, and he gave me a lot of real feedback. He's like, this is unused. This is... why are we doing this here? Why aren't we using the implementation we have from over here? All these problems that I hadn't really noticed.

And so getting a review from someone who wasn't using an agent at all and was a domain expert and was thinking really carefully about it -- I've just had to, over time, build up the philosophy that I'm still responsible for my own code. Because it's very easy to forget that when the agents are just churning stuff out, and you're like, this looks good.

**Wes McKinney:** Yeah, I mean, lately I've been on this journey of essentially, I think I'm also in the same place that you are now, where I'm primarily using Claude Code to implement. My workflow is I have a bunch of stacked terminals, usually three or four or five Claude Code sessions. I work on different projects in parallel because while I'm busy working on one thing, I can work on something else. And so I've enjoyed the productivity benefit of being able to nudge along work on multiple things or multiple work trees within the same project.

But like you, I've run into the same problem of the code quality just being often poor, surprising. I mean, it has certainly gotten a lot better, but there's this code quality problem either of solving the problem in a much more verbose way or with a lot of code duplication, copy and pasting the same thing. Especially the test suites end up much bigger and much more bloated and duplicated. And I'm one of these, I'm obsessed with code cleanliness and not repeating yourself and not having code duplication.

**Wes McKinney:** And so whenever you open up these code bases and look at the PR, you're like, ooh, this is, as far as code smells, this is stinky, stinky cheese level of code smell. Yeah. You know a thing or two about this.

**Charlie Marsh:** Yeah, so I feel like there's certainly the human element of code review that is important. And I think for you, the agent user, part of it is your responsibility to do as much of that before putting up a PR so that you aren't essentially asking other people to do all of the review labor. And so I've been trying to figure out how to do that.

I've also been investing a lot in what I call adversarial code review tools. Because if you ask Claude Code to review its own code that it just generated, you just do slash review, it's going to be like, looks great, ready for production. And then if you're like, no, it's not, it's like, you're absolutely right. I need to write more test cases.

**Wes McKinney:** And so I think we've all been through that gaslighting of the agent's overconfidence and self-confidence in its work.

**Michael Chow:** So I think just to connect these two things, I think it's so interesting, this -- your people on your team who are like, I feel less confident in your PRs. And you're like, maybe me, too. It's just a lot of work. That's totally fair. And you and Wes saying, exploring this idea of adversarial reviews, is there a way to up the confidence and the quality?

**Wes McKinney:** Yeah, I'm really curious. I think it connects back to something you said on Twitter, that reviewing code is the hard part.

**Charlie Marsh:** Yeah. And that we're not very good at understanding code quality, I think, as humans.

**Charlie Marsh:** I think the mentality I try to take towards some of this stuff is, one, if we put something up and it's -- well, first of all, the thing where you have a Claude Code session that writes the code and then you create a separate session and ask it to review it and it comes up with a bunch of valid feedback. It's incredibly unintuitive if you don't know anything about how these work. Because you're like, wait a second, it's the same agent. It wrote the code. How does it not find these problems?

And for me, that's actually a good example of trying to develop intuition around the limitations that these things have. Because it does kind of make sense if you understand how they work. But if you don't, and you just view it as, I put things into the model and it should always do the perfect right thing, it's an oracle -- if you view it in a certain way, it's a very good example of how you have to learn to use the tools.

Yeah, I mean, that's not a hard thing to learn or to do. But it's very unintuitive that that would be the case, in my opinion, if you don't understand how they work.

I think one thing I've tried to internalize, and we're still -- I would say we as a team don't have answers to any of this stuff. We're still really trying to figure it out. For me, again, people need to be responsible for their own code. When you see the model do things wrong, try to find ways to prevent that in the future. Whether it's updating the CLAUDE.md or the agents' MD or adding static analysis tooling.

We're actually probably turning on more lint rules now than we used to. And we have, even in Rust, we've always used Clippy pedantic. It's the most pedantic. We have a couple of rules disabled. So try to enforce things programmatically because the model's good at following if you have something that's enforced programmatically and it's getting diagnostics about it, it will fix those things.

Or try to give feedback in the CLAUDE.md or similar. We had all these problems, like in Python, Claude kept adding dunder all to all these things. And it's like, we basically never want to use that. Or in Rust, it wasn't using let chains, which are a very new feature, and so probably not as much of it in the training data or doesn't realize it has access to them. So putting that in the CLAUDE.md.

And then over time, trying to bolster -- I mean, this was important even before AI, but trying to bolster, how can we get confidence in changes faster? In Ty, for example, we've invested a lot in this ecosystem report infrastructure. So every time we put up a change, we run over a bunch of projects. And we have a really nice report that diffs all the diagnostics and links to the lines of code and helps you understand what's going on. And that's really helpful for building confidence in changes because we can click through that report and see what changed and try to identify problems.

Ironically, also a thing that's incredibly useful is you give Claude that report and you ask it, are these false positives or false negatives? Go analyze the code. We've probably saved, we're saving hours and hours and hours on that. Try and understand whether these changes are false positives or false negatives. Or we get a user report, come up with a very minimal reproduction. Someone on our team yesterday was like, I think this would have taken me six hours before.

And so another lesson is trying to find things that are off the critical path, that aren't shipping production code that you can automate. And I've discovered just through trial and error that different agents are better at different things. For me, the stuff that I'm working on, it happens to be that Codex from OpenAI is a better code reviewer. It's a lot slower. I wouldn't use it for implementing, necessarily, because it feels slow. And I just prefer the ergonomics of Claude Code. But I'm happy to let Codex grind all day doing my code reviews.

**Wes McKinney:** One of the things that, maybe a segue into a slightly deeper topic -- I'm very curious on your take on some ideas that I've been having lately. We're talking about code quality. But the question I've been asking myself, and that's been keeping me up at night is, if humans aren't--

**Charlie Marsh:** Does it even matter?

**Wes McKinney:** If humans aren't -- it's like, maybe it's even this idea of code quality. This is something that only people care about. And so if people aren't reading the code anyway, what is the new code quality?

**Charlie Marsh:** I know. I'm thinking about this a lot, too.

**Wes McKinney:** What does it mean?

**Charlie Marsh:** Existential. Or maybe what is good code quality for agents is different than what it is for humans. Actually, maybe code duplication, which I detest, and whenever I see, like, no, no, this could be factored out into a helper function -- maybe the repetition is actually good for the agent. It helps establish what is the proper pattern for solving that problem.

And so I found myself being like, well, should I refactor this? Is this going to improve or hurt the agent's performance in the future? I don't rightly know the answer to that.

**Wes McKinney:** And that's kind of the segue into the big idea that's been keeping me up at night lately. The more -- I feel like there was a big sea change in September, October when Opus 4.5 came out. When it was evident that the quality -- as I dabbled, I started using Claude Code and became an adherent back in April. And I was using Claude Code to do fairly significant changes in Positron, which is Posit's data science IDE. And I work on, have worked on the Data Explorer, which is an advanced data viewer within Positron.

And I found myself often struggling because I'm bad at UI code, and it uses React, and there's a lot of nitty-gritty React details. And so whenever I had to touch the UI layer of the Data Explorer, I would find myself just slowing down because I'm like, not only do I not enjoy TypeScript at all, but there's all these foreign concepts, and I'm not a front-end developer. And so I found myself in the past being dependent on other developers to get help. Say, like, I can't do front-end, please help. And now I'm like, Claude, please help.

And so I found that actually was productive, and so I was getting a lot of stuff done, but obviously with a high error rate and a lot of just struggling with this massive -- because Positron is a fork of VS Code, so it's a massive TypeScript codebase. Even getting to the point where I could orient Claude in the codebase where it could run the build system, run the unit tests for that part of this million-line codebase was a lot of work.

But September, October, there was an evident sea change where, like, wow. Because I went from being a huge AI skeptic, was not even using Cursor or Windsurf prior to last March. I was still Emacs. I was writing code by hand like a caveman. And so there was an evident sea change. I'm like, okay, coding agents of the future. And then September, October, okay, this is the way I should be writing code from now on. I don't anticipate writing much code anymore.

But what happened as I moved on was, Python seems like the wrong language to be using. And the reason that I started feeling that way was because the codebases that I was creating -- and this was especially personal tools and projects.

**Michael Chow:** I just want to take a second to dwell on the big point you made, which was existential. Like, what's our job?

**Charlie Marsh:** I have a bodily response.

**Charlie Marsh:** Well, sorry. My response was to the question of, which I've also thought about before, which is -- if some of this stuff -- I mean, I tweeted about this the other day. I was kind of kidding because I occasionally -- I'm, for whatever reason, I really like my code comments to be complete sentences, right?

**Michael Chow:** Like a psychopath.

**Charlie Marsh:** And end in a period, stuff like that. And so I find myself at the end of a session often saying, make sure all the comments -- it's in my CLAUDE.md, but sometimes it doesn't do it. And I'm like, make sure the comments end in periods. Or I really don't like when you use em dashes in comments. Use a semicolon or a comma or a period or a parenthetical or whatever.

**Charlie Marsh:** And it's like, okay, that's actually a good example, maybe. Because does it matter? Like, sorry, that didn't even matter before. So maybe it's a bad example.

**Michael Chow:** You're like, am I holding Claude back?

**Charlie Marsh:** Well, no. But it's a question of, like, okay, I don't really like when the model uses dunder all. Or I don't really like in Python when the model does local imports. Sometimes it's just easier for it to import within a function.

**Wes McKinney:** Oh, I hate local imports, yeah.

**Charlie Marsh:** Yeah. And so, okay, and then we added a rule in our project where you can't do that except for certain modules where you have to do that because they're big SDKs or whatever. And so now it's enforced.

But the question for me is, does it matter? And I think -- well, first of all, I absolutely don't know the answer. And I think no one does. And I think anyone who claims that they are confident, basically, about anything that is going to happen in the next six months is mistaken.

But a couple things that have occurred to me. One, I do think the notions of code quality will be really different. I think what's good for agents and what's good for humans will be different. I don't think we really know what's good for agents yet. And I think that itself will also evolve a lot as the models get more capable. The things that are helpful maybe right now might get completely solved by the next generation of models.

I think we will need much better ways to understand code quality. And I would love to see actual quantitative metrics about this stuff, because every opinion that basically everyone has in the industry right now is just based on feeling, which is not nothing. But I'd love to understand, can we do long-scale longitudinal experiments where we measure how does an agent act more efficiently to get to the end result? What are actual metrics that we can think about?

I also think different software is built very differently. That's even true today. And I think that will continue to be true. Certain projects -- there are certain parts of my codebase where I'm way more hands-off with the agents, and certain parts where I'm way more hands-on. In Ty, if we just merged every PR that Claude wrote, it would completely destroy the project. We would get a bunch of things wrong. We would accumulate incredible debt, performance problems, correctness issues. Also, no one would understand it, which is a really big problem for that codebase. Because it's a compiler, right? I mean, it's a type checker, but it kind of looks like a compiler. It's a very sophisticated project.

In the PYX frontend, if we just merged every PR that Claude wrote, things would actually probably be totally fine. And those are very different. Or I have a bunch of experimental scripts that I use to pull data and stuff. And I don't really care what the code looks like. It's really about the output artifact.

And so my point is just, I think different projects will have very different needs. And the way they are built will probably be different.

**Michael Chow:** Just to put a cap on that, too. It's so interesting to hear you talk about -- start with should sentences and comments end with periods, all the way out to, like, does it matter in Ty if we just accept Claude's commits, or does it matter in the package manager?

**Charlie Marsh:** Yeah, it's -- I don't know. I mean, I think we're still just figuring all this out. And all my opinions on this stuff, by the way, are super different than they would have been four months ago.

**Wes McKinney:** I mean, for me, it just -- the prevailing feeling I've had lately is, I think that there's probably no more exciting time to be alive than right now. I think, honestly, I'm 40, so I was 10 years old in 1995 -- because 1995 was the big year of the internet becoming a thing, Netscape browser. So I was using computers, and there was an evident, palpable feeling of the world is about to change in a very significant way.

And for me, I started -- I had that same feeling when I started doing Python. I was like, this language is -- I think there's a world in which it gets big, and the world is profoundly different because people are programming in this language that is fun and accessible. Because it felt to me that programming was so kind of painful and not accessible. And so that was the big thing, why Python was so important, because of its -- and the reason it's so popular now is because it's so ergonomic and fun to work in. Writing Python is fun. The language is ergonomic. It's readable. It's concise.

And clearly, there were parts of Python that weren't very good. And Charlie and your team, you've fixed, largely fixed, some of the parts of Python that weren't working. The packaging and distribution and the fast installation.

And so now, the problem is Python has still got some issues. Python distribution is still, it's not a static binary, like you can make in Rust or you can make in Go. Python still, compared to compiled languages is relatively slow. And so that means running your unit tests, the same unit test suite written in Rust or Go might take three seconds to run, but it takes three minutes to run in Python.

And so now, viewed through the lens of the agent kind of grinding on the codebase and iterating and figuring out the right way to solve this problem -- what I've observed in using coding agents is that the agent is -- I've never, prior to this, felt my MacBook Air getting hot before because basically the agent is just pinning my CPUs all the time, running all the unit tests.

And what I found, and why I was saying a few minutes ago that I'm starting to question whether I should be using Python at all, is because that agentic loop is slower in Python. The agents are really good at writing Python because they have massive amounts of training data and reinforcement learning. And I do believe that Python's readability and conciseness is also a benefit for the LLMs generating that code. But ultimately, if you compare the agentic Claude Code, Codex loop, or agent of your choice loop, building a Go codebase that solves one problem, you compare that to the Python -- if you set two people to work building the same project in Go versus the same project in Python, what I'm seeing is that you can build the same project in Go faster because the agentic loop is faster. The tests run a lot faster, a hundred times faster. And then also the distribution problem. So if you build a Rust project, you end up with a static binary that you can just copy over. But with Python, still, it's like, oh, we got to put it on the package index. And you got to install uv. And even though uv's fast, you still got to install it. And so there's all these caveats.

And so I do think that I'm not of the opinion that AI is going to cause massive job loss and put software engineers out of work. I'm more of the optimist, like we're going to end up with 10 to 100 times as much software and all these personalized, customized tools and tools for small audiences. But I do believe that we're going to see on a proportional basis less software being written in Python because of that agentic loop.

**Charlie Marsh:** Yeah. I mean, I have a lot of thoughts on it. I think that's very plausible. I think it's definitely possible that areas where you would have reached for Python before, it's no longer the right fit. I think that evolution might happen or might be happening, like things like standalone CLIs or whatever else. Because I think different languages will have different strengths. And suddenly the calculus around how you choose what to build in is very different. And so it will just naturally be the case that some things will be better for certain things versus others.

I mean, I'm still sort of figuring all this out myself. I guess one thing I think about a lot is I actually haven't really been a huge Python defender as a language in general. I think the thing that is part of why Python is so powerful is just network effects and path dependence are very strong. And so Python has this huge scientific computing ecosystem. And it's very hard if you want to do anything that involves any form of scientific computing to use anything else. And a lot of that will continue to be true. Those things exist and they will continue to be critical.

I think the other thing is, we certainly as a team want to figure out how can we make Python a great choice for agents? And so how should the language and the tooling evolve? We've thought, for example, a lot about building our own test infrastructure or even, should we do our own runtime? Something that makes very different trade-offs. Those are obviously all very hard problems. But the question is, what if we wanted Python to be a great choice or remain a great choice for agents? I think we kind of have a responsibility to try to solve some of those problems and make it a better choice.

I'd love to do standalone binaries, just for example. Kind of like what you can do with bun and JavaScript. We should absolutely just make that possible. And there's no reason we can't. It's just a question of prioritization. And I'm sure there will be trade-offs and whatever else.

But I think what I would say is, we're trying to learn about how to build software with agents and what's required. I think it'll probably impact our roadmap a lot in terms of the problems we choose to take on. I think it will also be the case that the way people make decisions about what programming language to use will be super different. It might not be the case that most people are writing most of their code with agents this year. I'm not sure if the distribution will happen that fast. But I think it's important, when you think about building tools, that's what software is going to. Software is going to be really different. And so I want to fold that into our roadmap. I want to fold that into how we think about what we're building. Even if we choose, say, actually, we're going to build this other tool that has nothing to do with Python. I'm even open-minded to that because what's the thing that's going to make people more productive?

**Wes McKinney:** Yeah. I mean, but you're right. One of the -- I mean, Python has enormous inertia in the scientific world.

**Charlie Marsh:** Yeah, yeah, yeah. Most people listening know, but I think almost all of the LLMs and the AI labs themselves, modern LLMs are all built with Python.

**Wes McKinney:** Yeah, I mean, it's entirely Python. PyTorch and JAX, and even Google, which has its own silicon. So Python's clearly not going anywhere.

I think the shift in agent ergonomics may influence the builders of those AI frameworks. It may influence their future choices in terms of where they build. Even in the fullness of time, the architects of the LLMs, people building training, post-training, reinforcement learning the LLMs, the people writing that code, increasingly they are going to be using agents to write that code. And so at some point, maybe it's three years down the line, maybe it's 10 years down the line, I could imagine that we'll end up with a whole parallel ecosystem of non-Python AI training frameworks.

In a sense, maybe Google's already working on it. But for now, the foothold that the -- the anchor that we have through PyTorch and JAX and the whole ecosystem of AI frameworks for Python, that's a juggernaut, right? And there's already teams in place that are continuing to build and maintain those libraries.

And so I think some people might hear what I'm saying and say, oh my God, is Wes saying Python's going to die? I'm like, no, I'm not saying that at all. I think if we look at the Stack Overflow language rankings, Python just emerged out of the 2000s. And now it's just this hockey stick of, it's the most popular language by far. And I think it will still remain the number one or number two or three language. But I expect that we'll see significant growth in other languages. But the amount of Python that's generated will be 10x or 50x or 100x.

**Charlie Marsh:** Yeah, I mean, obviously I would say this because I'm working on a company that builds Python tooling. But I don't think Python's going anywhere. But I do think that the way that we choose what we build with, the things that make a language great, all that will change a lot.

And it even impacts how we think about things. Today, obviously, we're building Ty. It's a type checker and a language server. But there's a bunch of things we're building there where I'm like, wow, this is really specific to how humans work. Things like hover. You hover over a symbol. And what does it show you?

**Wes McKinney:** Machines don't hover.

**Charlie Marsh:** Yeah, well, I'm like, oh, we're spending a lot of time on really good hover. And it does matter. But an agent will never use it.

Or even auto-completion, right? That's actually a very hard problem. We're spending a lot of time on that. And I absolutely think it's merited. I think it's good, important work. We have to have those things. It's still table stakes to be a usable LSP. You have to have good auto-complete. But the way that agents would use that tool is going to be really different.

And so at least I'm thinking about it a lot. I've always tried to think, ever since AI became really usable, about how can we make sure what we're building is resilient? Because we really cannot predict the future. But we can think about what's going to be resilient and what's not.

And so static analysis, having really good verification, really fast verification -- that's, in my opinion, very resilient. As you write Python, I think typing, for example, will only become more important and more useful because it's a very fast way to validate correctness.

And then package management. I mean, maybe there's a world where you have no dependencies and you're building everything from scratch. But I think we're much further away from that. And so being able to install and manage your dependency tool chain, making it really easy to start and run your project, those are things that I feel like we're making very resilient bets.

But we also have to be thinking a lot about how it's changing.

**Michael Chow:** If I could just try to put a thread to it, because I feel like all these points are so interesting. And I hate to go back to it, but this point of starting at, should I put a period at the end of my comment? To Wes being like, should I just use Go for this? And this fact that there's an ergonomics to what agents care about, and what do you choose for humans versus machines is such an interesting topic. And to your point, what would be resilient? What's going to endure five, ten years?

**Charlie Marsh:** That's why it's an amazing time.

**Wes McKinney:** I don't know. We don't know the answers to any of these things. We're just sitting here talking. I frankly find the uncertainty -- I haven't felt this kind of state of just excited enthusiasm about what's happening.

**Charlie Marsh:** I find it terrifying.

**Wes McKinney:** Yeah, I mean, it's scary, but I think that's part of what makes it so exciting is because it is also scary. Just even taking in what's happening on a daily basis or a weekly basis. I open Hacker News, I'm like, oh, what fresh hell is being unleashed on us today?

But even having wild thoughts -- you're talking about IDEs, I haven't touched an IDE in like two months. The only reason I've opened an IDE is because there's still IDE tooling that is necessary for, if I'm working on Positron, you need to use the whole VS Code IDE tooling for debugging. And there's still the need to sometimes set breakpoints.

But even, maybe breakpoints are only for humans. Agents have got to figure out how to debug themselves.

**Charlie Marsh:** And I think it's a very -- at least I feel -- it's a hard time to be a leader because, in any capacity. Because I think there's just so much uncertainty. And I think my approach, which I guess is the same as it's always been, is just to be really honest and be like, this is what we think we understand. This is what we don't. Here's what I think we should be trying to answer.

**Michael Chow:** Do you think, is that hard because as a leader, uncertainty is hard? Or do you think that's hard because there's something about the uncertainty or this situation?

**Charlie Marsh:** Maybe it is a little bit of the latter because I think things are changing really fast. And so there are lots of products that you could build today. Even if you said, okay, we're going to really focus only on building around AI and agents. There are lots of products that you would think about building today that could be made completely redundant in three months or something.

And so I think that, again, that's where, for me, it comes down to trying to build around resilience. And I think the layer that we're at is a very good one for being robust to change. But yeah, there are lots of products that we might think about building today -- what if we were like, oh, we want to build a code review tool? Not to comment too much on that example. But how relevant is that going to be in three years?

So I think to some degree, uncertainty is hard. To some degree, I think it's just the change is so fast and the capabilities are changing so much that maybe it is a little bit unique.

But as a leader, at least in my opinion, you don't always have to have all the answers. But you have to have some opinions and a clear strategy to rally around, even if it's get more information or learn more.

**Wes McKinney:** I mean, how do you -- so there's Charlie Marsh, the person, but then there's also Astral, the company and the team. So I'm curious, how has the team and the company changed in the last six, nine months in reaction to everything that's been happening?

**Charlie Marsh:** I think thankfully, we haven't had to make too many major strategic shifts. I feel like the things that we were focused on have remained good bets, maybe just by chance. But I think a lot of it is actually cultural around trying to get people curious and interested in experimenting with a lot of these tools.

So I've tried to do that a lot. We've set up, because across the team, the adoption varies a ton. There are some people who don't use this stuff at all. And then there are people like me, I guess. And maybe a few others who are on the other end of the spectrum where everything we're doing is through agents.

And I think a lot of that has been -- we're small enough. We're small and we're flexible, which is a huge benefit. I'd much rather be a 20-person team than a 200-person team trying to figure out how to adapt. It's way harder.

But we do these AI knowledge-sharing sessions where we bring the whole team together and someone just screen shares. And they literally walk through how they do their work.

**Wes McKinney:** Oh, awesome.

**Charlie Marsh:** And so it's just, yeah, this is -- I'll have this open and then I'll do this and I'll do that. I mean, it's like pair programming. It's just sharing how you work. But everyone has a super different approach. And then a bunch of people have reactions and we just have an open conversation about it.

And so just trying to get people thinking about it in a very genuine way. The good thing about having a company culture like this is we can come in and I can be like, yeah, I do like this, but it kind of sucks. And this, I've tried this, it doesn't really work. We're not sitting there going, this is the most amazing thing ever. You have to use this right now or you're about to be made redundant. Your job is gone, or programming is over if you don't -- it's really not like that. It's, hey, we should all be pretty curious about what's happening here.

So that's sort of been my approach. And I think another thing that's been cool is we try to do a lot of just sharing in Discord around what's working and what's not. Like, hey, I built this thing. Especially for internal tooling, that's been a great test bed for us or tooling around PRs, like the ecosystem report stuff that I mentioned. I think Claude created this really nice report that, so it's not just a GitHub comment. It's actually an interactive report and you can click on it and that's super useful.

And so seeing wins like that come out in areas that are kind of low stakes, all that's been helpful for getting people interested.

There's another part, too, which is just access. How do you make it so the bar to trying this stuff is very low? There are a lot of different tools. And so we're basically, everyone at the company, everyone on the team has a corporate card. Anyone can just put a Claude Max subscription on it and no questions asked. That's an easy thing to do and that companies should be doing. But just making sure that there's a very low bar to trying things out and sharing what's working and what's not.

**Michael Chow:** Yeah, it's interesting to hear where you mentioned this feeling of uncertainty and the challenge as a leader in building AI products. But it's also interesting to hear inside the company, how do you encourage a culture of experimenting?

**Charlie Marsh:** Yeah. No, because there are definitely people on the team who are skeptical, for sure. Our team, I mean, it probably doesn't represent an average sampling of human beings across America or whatever, but we have programmers who come from all different sorts of backgrounds and ages or programming ecosystems or what they did before or whether they're self-trained or academic. People have very different opinions about a lot of this stuff.

And so I don't approach that, and I think people on our team don't approach that in a combative way, like you have to be using this stuff. I really want it to just be more like, okay, this is weird, we have to figure out what we're doing here.

So that's sort of been my approach. And I feel a lot more uncertainty, honestly, about things like the open source and the contributors and how we manage those interactions. It is increasingly the case that we get these PRs that are a lot of work to shepherd, and we don't quite know what to do with it yet.

**Michael Chow:** And I did hear you -- one thing that struck me before is you mentioned when someone opens a PR and you're thinking about a response, you don't want to discourage them, you don't want to give them a response that sends them away. So hearing you say that, thinking about contributors in the context of not sending them away being a really welcoming...

**Charlie Marsh:** Yeah, that's always been a big part of the project for me. We want to have a community where, even if we say no to whatever you're asking for, you should feel respected. You should feel like we listened to what you asked for, we thought about it, and we gave you a reasonable rationale for why we couldn't. And then obviously, if we say yes, that's always a better experience for people.

But that for me was also a big thing that created really positive feedback loops over the course of the projects. I think we just created a community where people felt like we took them seriously and were really responsive.

**Michael Chow:** And then I guess you were talking about today in open source with AI, these contributions now as part of a welcoming community.

**Charlie Marsh:** It's very hard. I don't really know how to navigate it. I mean, we also get things like issues that are clearly written by an LLM, and there are all these tells -- lots of headers, lots of bulleted lists with bulleted items, lots of parentheticals, maybe some emojis, things that are way too thorough. A human would never do it this way. It not only talks about the problem, but also the proposed solution and everything.

When we get issues like that, we don't have any policies on this yet, but sometimes we'll basically just be like, was this written by an LLM? If so, can you just talk us through how you verified correctness? I don't really know. It's just things that used to make sense don't quite make sense anymore.

Even sometimes now, in the context of open source and code review, sometimes I put up a PR that I wrote with Claude and then hopefully did a bunch of iteration. Hopefully it's not just a first pass slop thing that I put up. Someone puts comments and then a decent chunk of the time what I'm doing is I just copy and paste the comments into Claude Code and have Claude fix the thing. And I review -- I paste one comment.

**Wes McKinney:** You can have Claude Code read the comments using the GitHub CLI.

**Charlie Marsh:** I know, I know, I know. But I will basically sometimes just copy the comment. I'll put it in Claude Code and then I'll do it one at a time. Ideally I'll look at what changes and then I'll commit that and then I'll go to the next one. So I am being thoughtful about what it's doing. But that's pretty weird. Like, why are we working that way? There's a bunch of connectivity that's lost.

And I just think the way that that whole loop works will be really different. And the way that the open source contract works, it sort of has to change because it used to be that writing the code was the hard part and now putting up code that passes the tests, let's just put it that way, is not hard. But validating, especially in a project like uv, just for example, okay, I'm going to write some code and then that has to work on Windows, macOS, Linux. It has to work with maybe people having all sorts of different drive setups. Maybe it has to do with symlinks or hardlinks or there's all these things that are actually very hard to test and we have no way to really verify those.

**Wes McKinney:** It reminds me, maybe you've read this famous essay from years ago called, I believe it's called the Lisp Curse?

**Charlie Marsh:** I don't think I've heard of it.

**Wes McKinney:** So I'll summarize it for you. The idea of the Lisp Curse is that it's trying to reckon with why did Lisp, the Lisp ecosystem, that includes Scheme and there was a whole Lisp thing in the 80s -- why did Lisp not become more popular? And so the idea is that problems that are technical problems in other programming languages are social problems in Lisp.

And so the idea was that individuals could craft these solutions to problems in this elegant way all by themselves. And so the barrier for an individual to be able to create their own personalized solution to the problem was not as high as it would have been in C or in COBOL or other languages of the 1980s. And so the outcome of this, back in the 1980s when programming was a lot harder -- the outcome was that people were less incentivized to collaborate because they could just do their own thing.

And I feel like now we have that problem but worse. Because it's like, why bother collaborating? Why bother doing open source when you can just fork the project and make it exactly the way that you want?

**Charlie Marsh:** Yeah.

**Wes McKinney:** And so even the incentive to participate and to propose changes and to have to interact with humans to get changes into a project -- I'm seeing people just fork it, fix it, and move on. Maybe they'll throw up a PR.

**Charlie Marsh:** Maybe they won't.

**Wes McKinney:** Maybe they won't. But I think that Lisp Curse problem, now we have this problem of how do we continue to incentivize that collaboration, that healthy collaboration, which yields communities that work together to solve problems and collaborate over a long period of time when now the code is super cheap and the cost of saying, well, I'm not going to collaborate with you because it's easier to talk to my agent than it is to talk to a human on GitHub. And so I'm just going to go solve the problem and move on because I've got a job to do.

**Charlie Marsh:** Yeah. And so the whole cost-benefit of open source has completely changed. I don't mean to catastrophize, but people are talking about, oh, the end of open source and they may not be wrong. I don't know.

I think one challenge with that and with a lot of these things is there will be compounding effects over time that we won't see acutely. Okay, one person forking a project is one thing, but then over the course of a year or two or three years, everyone forking and no one building new foundational tools -- what are the effects of that? Everyone forking and introducing their own CVEs.

**Wes McKinney:** Yeah, there's the whole security thing.

**Charlie Marsh:** There's just, and so I don't know. I think it's important to be thinking about right now. I don't know what to do about it.

**Michael Chow:** Yeah, it is so interesting with you mentioning Lisp. And I think sometimes, too, it's called the Curse of Lisp where it's too much of a good thing.

**Wes McKinney:** I think the essay may actually be called the Lisp Curse or something. I'm thinking of Python Paradox as the Paul Graham essay.

**Michael Chow:** I think it's so spot-on, though, that it's a good thing to have a really powerful language and want to roll something, and it's a good thing to have a really powerful coding agent. But it is so interesting, your points about being social or needing to reach out as hints of the curse. You mentioned working on Positron, and when you need to work on React stuff. Before, I think you mentioned you'd have to grab someone on the team, and now you can kind of just fire it off on your own, which I feel like has that big curse energy. It's a good thing, but who knows?

**Wes McKinney:** Invariably, the thing that I do will be worse because I also don't know React, and so I don't have the ability to read the output and judge, is this the right way to solve the problem? And so essentially, you're pushing off that burden onto the code reviewer, which has more experience.

And so yeah, I don't have a good answer, but I view it as more of an opportunity than -- I'm certainly not catastrophizing, but it's good that we're aware of it and we're asking these questions. Because for us, as open source maintainers, I'm very passionate about open source, you're very passionate, we're all open source package maintainers, and I love open source, I love working with the community, I love working with other people. And so I'm optimistic that we'll be able to create new tools and solutions to incentivize human collaboration.

**Michael Chow:** Yeah. And I think it's been so helpful to hear, Charlie, what you're doing in the ecosystem and keeping it welcoming. And also just thinking in terms of what you build next and how you think about focusing on humans and agents.

**Michael Chow:** And I think there's so much to chew on just in this space of how will people interact with code. And I think you all have built such great tools for running really helpful things fast, whether it's linting or packaging and running scripts, which is -- uv I'm running all day every day. So I'm so excited and curious to see what you all do and embrace both the human and the machine part of the future.

I guess closing out, I'd be curious what you're maybe most excited about for the coming years.

**Charlie Marsh:** Well, I think, I guess as a broad theme, the way we build software will change a lot. And I'm hopeful that people keep quoting this back at me because I tweeted this thing that was, I feel like working with agents is a lot more productive but a lot less fun.

**Michael Chow:** And that's what you're excited about there?

**Charlie Marsh:** I think I'm hopeful that we will find, we will sort of solve some of the things that make it feel less fun. It's not about having fun. Okay, having fun is great. I love having fun. Everyone loves having fun. But I think for me, it's more that the way that we build right now is there's a lot of friction between this new world and the current world that we're in, this potential new world and the current world that we're in. And I think we'll just learn a lot more about what building software should look like, and I'm excited for that.

I think in the Python world, this is fairly niche, but we've been working a lot on these standards. They are largely born out of the question of how do we make it easier to install PyTorch? Because I spend a lot of time helping people install PyTorch and making that easy, and the PyTorch ecosystem is absolutely enormous. And so that for me, the standards we're pushing on around wheel variants, I think is kind of an exciting change that, should it be accepted, I think will change a lot of what it feels like to work in Python and kind of enable us to solve some of the pain points that we just have to live with today and can't solve in uv. So one sort of more near-term thing and one sort of very long-term, big picture thing.

**Michael Chow:** I love the two of, how can this be fun and this very specific detailed pain point. I think it is spot-on kind of Astral that a lot of these tools have made things way faster and more fun, and there's been so much thought into these tools.

**Charlie Marsh:** I appreciate that. Yeah, thank you.

**Michael Chow:** Well, thanks. Thanks for coming on. I know we went super long. Thanks for joining us.

**Wes McKinney:** A lot to think about. I got fired up.

**Charlie Marsh:** Felt short, yeah. That was fun. I've got a lot of AI thoughts.

**Michael Chow:** It was super fun, yeah.

**Charlie Marsh:** Thank you. Thanks so much for having me and just for the great questions, the great perspectives from both of you, and yeah, I'm excited to see what the next year brings.

*[Podcast outro]*

The Test Set is a production of Posit PBC, an open-source and enterprise tooling data science software company. Visit thetestset.co or find us on your favorite podcast platform.