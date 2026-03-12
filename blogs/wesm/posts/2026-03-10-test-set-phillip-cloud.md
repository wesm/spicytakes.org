---
title: "Sleeping Rats and Sociopathic Agents — with Phillip Cloud"
summary: "Podcast at The Test Set (Posit)"
date: 2026-03-10T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-phillip-cloud
word_count: 8161
source_file: transcripts/2026-03-10-test-set-phillip-cloud.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://www.youtube.com/watch?v=CPnUZZY0JJE"
---

{{< video https://www.youtube.com/watch?v=CPnUZZY0JJE >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, Michael Chow, Hadley Wickham, and I talk with Phillip Cloud, a principal engineer at NVIDIA who leads the Ibis project and was one of the earliest pandas contributors. Phillip and I have worked together in some capacity for close to 15 years, going back to when he and Jeff Reback were among the first pandas core team members with commit access.

Phillip describes his path into open source: he got into programming through MATLAB in an eye movement research lab, discovered Python around the time Travis Oliphant was unifying NumArray and Numeric into NumPy, and started contributing to pandas in grad school while studying computational neuroscience. He was analyzing sleep behavior in anesthetized rats using multi-electrode recordings, and pandas' column MultiIndex turned out to be a natural fit for organizing the data across electrode shanks. His first pandas contribution was `read_html`.

The conversation covers developer productivity and terminal-based workflows. Phillip is a NeoVim user who runs everything through TMUX on a 49-inch monitor split into thirds. He talks about VisiData, a terminal-based data analysis tool created by Saul Pwanson, which has both single-keystroke power-user modes and clickable menus for discoverability.

On AI coding agents, Phillip is more skeptical than I am. He tried Cursor's UI and didn't like leaving his terminal workflow. He tried Claude Code but found the conversational tone off-putting, preferring Cursor Agent's mode of being "sociopathically focused on the task." He's found that agents confidently assert they've solved problems when they haven't, and that they struggle with things requiring detailed domain knowledge, like CPython reference count semantics in C extension code. He currently uses agents mainly for lower-stakes work like generating PR summaries.

I share my own experience with an 80/20 observation: roughly 20% of development work is the high-value design and decision-making, while the rest is maintenance drudgery like CMake files, CI/CD scripts, and packaging. I've found agents useful for that drudgery layer, and I recommend Steve Yegge's Beads library as a task-orchestration tool for large-scale porting exercises. We discuss the idea of building lightweight agent orchestrators with validation loops, where you break work into units, let the agent commit, validate the output, and only allow it to proceed if validation passes. We're both finding that single long agent sessions break down as context fills up and the agent starts ignoring instructions, and that defining the rules of task completion in code is the path forward.

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field. On this episode, we'll talk with Phillip Cloud about some of the nuances of adopting AI for software development. And if you've heard the podcast up to this point, you probably know that we've wholly surrendered ourselves to AI to code for us. So I find Phillip's perspective really refreshing, and he's got the bona fides to match. He's a principal engineer at NVIDIA, he leads the Ibis project in Python, and he's one of the earliest pandas contributors. He's tried Claude Code, he's tried Cursor Agent, he's walked away still searching for the right AI tool and use cases. Phillip's the type of developer who doesn't use a mouse and wants to only use his keyboard in the terminal. And I find that's the hallmark of a really great developer. So in this episode, we'll talk about how Phillip approaches software development and what AI tools get right and what they get wrong, and what 15 years of open source experience has taught him about hype cycles and tool adoption.

**Michael Chow:** Hey, welcome to The Test Set. I'm joined here with Phillip Cloud, who's a principal software engineer at NVIDIA and lead on the Ibis project, which is a neat Python project that can run SQL on a lot of different databases, and an OG contributor to pandas. So it's really come up through a lot of interesting Python open source projects. And so excited to talk to you. And I'm joined by my co-host, Wes McKinney, who's a principal architect at Posit, and Hadley Wickham, who's chief scientist at Posit. Phillip, so glad to have you on.

**Phillip Cloud:** Yeah, great. Great to be here. Great to kind of sync up with everyone.

**Michael Chow:** Yeah, I will say we had a little prep for this in that when I talked to Wes in an early interview, he warned me that you're a wizard at puns. And I did notice that came up a little bit in some of your responses prepping for this, that I think you said you want to be known as a decent human with lots of open source contributions, liked puns, and be loved. So I'm excited to see. I mean, I think all those things are great, but I'm excited to see what happens on the pun axis particularly.

**Wes McKinney:** What I've always said is that Phillip has a pun-oriented, you know, kind of pun-oriented way of working. So like, you know, he's the person that you can always count on to never miss a pun opportunity, you know, often in the least expected ways. And I feel like I'm on the lookout for puns. But his eye is next level. So it's brought a lot of humor and amusement to our years of working together. I mean, I've worked with Phillip in some capacity for -- I think this year we'll make, you know, I'm not sure if it's exactly 2011 or 2012, but we're closing in on 15 years. So it's been a really long time. And spanning many projects. Pandas -- like Phillip was -- Phillip and Jeff Reback were two of the first pandas core team members to join the project formally and to have write access to the repository. So we go way back.

**Hadley Wickham:** I just wanted to put in a plug for R, because I think if you like puns, that's a much better community than the Python community. Shots fired.

**Phillip Cloud:** Yeah, maybe. Well, maybe I need to go over there and kind of, I don't know, steal some game.

**Michael Chow:** So I know, Phillip, you have a lot of really interesting opinions on tools and I'd be super curious to talk about a little bit like how you got into open source and projects like Ibis, and a little bit more, and then into some of the tools and your thoughts around some of that. But maybe you could catch me up on kind of your path into working on open source tools and tools like Ibis.

**Phillip Cloud:** Yeah, so. I won't go through the whole backstory, but I will start it at the end of undergrad. I was working at an eye movement lab, and people who work in eye movement labs are essentially physicists doing some kind of -- it's sort of biology. It was officially in the biology department, but most of the people working in the lab were physicists and some of it was also involved with the psychology department. So it's this very sort of mixed-discipline research. But we did everything in MATLAB and this other system called LabVIEW, which is this crazy National Instruments thing that you program using circuit diagrams. It's actually pretty cool because it kind of gives you automatic dataflow programming without having to think about how to parallelize anything. It's kind of nice.

And so the people in the lab were definitely responsible for me getting interested in programming via MATLAB. And then I sort of just poked around with that and kind of looked around, you know, back in the pre-AI days, you just had to Google for stuff. And I found some other things similar to MATLAB. I don't even know if it's kind of a deep cut, but NumPy used to be split into two packages, NumArray and Numeric, I think is what they were called. And I was sort of getting into programming right around the time when Travis Oliphant came onto the scene and was kind of unifying that into NumPy. And so I got into Python through that. I built a few things that we had built in the lab in Python, some analysis applications kind of mostly around plotting the various things we were looking at.

And then, fast forward, I was in grad school studying computational neuroscience. And the specific kind of data analysis I was doing -- pandas was a very useful tool for what we were doing, mostly because of a feature that I think is not particularly well liked by the pandas developers, which is column MultiIndexes. It's kind of gross in the implementation, but it was super useful. It was a bit niche. It was because the thing we were studying -- we were looking at sleep behavior in anesthetized rats and the way the electrodes were situated in the brain. They were organized under these four shanks. And so I wanted to do analyses that were between the shanks and across them, and each electrode on the shank was a time series, like 22 kilohertz or something, recording voltage. And so it was a pretty natural fit to be like, okay, I'm going to dig into the first shank, or I'm going to dig into the first four electrodes on all shanks, that sort of thing. So column MultiIndexes were a pretty natural fit and no other package at the time had anything like that. And so that's how I came into pandas. That's how I got involved in open source.

And then I just started contributing to pandas. It was a very welcoming community. I think the first thing I did in pandas was `read_html`, that abomination. I don't remember if I personally needed that or if I was just kind of combing the issue backlog and saw it. I mean, it turns out that these basic things like reading CSV files, reading HTML files is tremendously useful. And so it's kind of funny that most of the people on this call have spent a not insignificant amount of their development time building these kinds of things. I think many people regard them as so elementary, and yet you can't do anything else if you don't have them.

**Michael Chow:** Okay, so one thing I'm curious about is, one thing we talked about beforehand was asking about the most exciting development now. And I sort of jokingly said, "is it AI?" But I thought your response was really poignant, that you said you're not sure it's AI, but AI is interesting. And then you talked a little bit about developer productivity and how the focus on that has shifted over the years. I'd be curious to hear, in terms of the most exciting development now, your thoughts on measuring and tracking developer productivity over the last five years?

**Phillip Cloud:** Yeah, I mean, I don't know if I have anything concrete other than anecdotes and observations of what I've seen. But I think over the years, because many more people are writing software, it's become profitable in some way for companies to make developers more productive, whatever that means. Before, you used to have to be a wizard to use like Visual C++ or Visual Studio. It came with 30,000 knobs and there was just a lot of stuff to do. And then I think there was a bit of a sea change when VS Code came out. And VS Code, of course, is based on Electron, and Atom was somewhere in there as well. It really is the browser-based application that gave rise, I think, to a lot of this. And then people started writing all these plugins, and I think some of that ethos kind of filtered down into what I would call more primitive tools, like command line tools. And now your command line tool better have a sweet TUI or else no one's going to use it. And it better be pretty and be able to deal with ANSI colors and things like that. So yeah, I think it's interesting that people have been spending a ton of time making software development just better and easier to do.

**Michael Chow:** Yeah, that's fair. And I guess, if we had to explain what a terminal user interface is to an alien, how would you explain it?

**Phillip Cloud:** I'd say it's like throwing out the last 30 years of what we've learned about designing user interfaces and saying, let's go back to this nostalgic age of the 1980s.

**Michael Chow:** Yeah, yeah, yeah.

**Phillip Cloud:** I don't know, my theory is that we have this nostalgia for these interfaces because -- part of it's our ages, like nostalgia for whatever age you were when you were a kid. And then there's also -- everyone's a little nervous and uncertain about AI, and that forces us to want to go back to this comfortable place.

I really enjoy TUIs personally. When they went out of fashion, I was a little bit sad. When I was in college, I did all my email in a TUI. I would SSH into the server and do my email there. And eventually in 2006, I switched over to Gmail and never looked back. Right now I'm actually building an email offline sync and archival tool with a TUI so I can rebuild those glory days of doing email stuff in the terminal. I hope to turn that into an open source project in the future.

But, you know, I worked in finance, and so I had up-close-and-personal experience of the glory of the Bloomberg Terminal. And that's probably the most commercially successful and ubiquitous software that has remained a TUI since inception. Users who pay -- I don't know what a Bloomberg Terminal costs, but it costs a lot of money each year, tens of thousands of dollars. It's just a financial operating system that financial professionals use. And it's a TUI. And so I feel like the AI sphere is kind of turning the rest of the world into one big Bloomberg Terminal, which is interesting.

For a while, the creator of this tool called VisiData worked at Voltron Data, where I was before NVIDIA. And that thing is pretty awesome. The attention to detail in the interface is unlike anything I've ever seen in a command line tool, and it's all built with curses, I think. Most people interact with curses basically in some kind of installer tool. There's a bunch of stuff written in curses because for a long time that was the only game in town when it came to creating a terminal user interface. But VisiData is amazing. I would definitely recommend people check that out. It's a quick data analysis terminal interface.

One of the things that was really awesome about it is that it's got two modes. Saul Pwanson, the creator, is definitely the kind of person that's like, I want to be able to do all the most powerful things in one keystroke. But he also realizes that not everybody is like that. So he has built a system where VisiData allows you to point and click stuff as well from the terminal -- clickable menus and cascading menus. So regular sort of something you might see in a windowing system UI. But once you get into the single-stroke world, it's really hard to go back. And you can, similar to certain editors, chain together -- it has this really nice composability aspect that you can't really get from the menus. You can learn them by using the menus because next to the menu item, it usually has the keystroke that will do that thing. But you can also, similar to Vim, give input to parts of those commands as you're chaining them. So it's really nice.

And I think, on the topic of IDEs and developer productivity and TUIs -- I think I saw you're a NeoVim user. Is that right?

**Michael Chow:** That's right, that's correct. That's my daily driver. Yep.

**Phillip Cloud:** Yeah, it's been for a while that I switched to NeoVim. I don't remember if there was a specifically very rational reason. I think someone was like, hey, you should try this, and it started up a little bit faster, so I was like, cool, let's do it.

**Michael Chow:** But that means you're all hands on keyboard, never on mouse, is that...

**Phillip Cloud:** I hate the mouse, I freaking hate the mouse. Yeah, I do. Most of my time is spent -- the way it's set up is I have a 49-inch monitor and it's split into three. One third is a browser and then two thirds is devoted to a terminal, which is running TMUX, and that's split again down the middle. And then I use a lot of temporary splits, but I almost always have one single vertical split.

**Michael Chow:** Yeah, I know it's tedious, but there's something so magical about developers' very particular setups, like how people lay things out and how they set it up. I feel like it's interesting to hear the split in the NeoVim workflow.

**Phillip Cloud:** There's a couple of other things I've tried that combine some of -- NeoVim has a terminal mode, which has some neat features. The main neat feature is that I can use all the same Vim keystrokes inside of a terminal and scrolling is not this weird thing that I have to set a buffer for. But TMUX, it's one extra key set of commands to do a split in Vim.

**Michael Chow:** And I guess for broader context, TMUX is the ultimate pane-splitting, session-running tool. So there's a lot of opening panes and opening windows inside of things. Very much things inside of things.

**Phillip Cloud:** TMUX is also really useful in terms of -- if you have a remote connection to a machine and you're traveling or something and you need to close your laptop, and you connect to a remote machine and you're running a TMUX session there, it will keep going. And whenever you reopen your laptop and reconnect to the internet, you can just reattach to that session and none of your work is lost and all of the state in the terminals is preserved. There's another Unix tool called Screen, which is a lower-tech version of TMUX. Some people still like to use Screen. But TMUX is a lot more full-featured.

**Wes McKinney:** I've been weirdly resistant to using some of these things and I'm still just using kind of derpy terminal emulators and splitting them. And a lot of the time I'm just like, I should be using TMUX. I say that to myself probably once a month. And still I just haven't been able to go down quite down that particular rabbit hole.

**Hadley Wickham:** I, on the other hand, have never split a terminal, so...

**Wes McKinney:** Oh, man. You're a straight -- no way.

**Michael Chow:** Don't judge me. We have the full spectrum here.

**Phillip Cloud:** It's true.

**Michael Chow:** I used to use TMUX a lot as a grad student when I had to go into a computing cluster. But now, actually, surprisingly, I picked up TMUX again a few weeks ago because I feel like using Claude Code kind of brought TMUX back, where I was like, I want to be able to reattach and run Bash on the side and stuff. So I was surprised that it's kind of a renaissance with Claude Code.

**Wes McKinney:** For me, the coding agents -- the big unlock with the coding agents has been that they solve the configuration problem. Like, any kind of configuration or fiddling -- yak shaving -- some developers really actually enjoy that, discovering all the knobs and bells and whistles and configuring things to perfection. And I feel like -- I know somebody who's really good at that. He was always the person who was Arch Linux, super knowledge of all these details. I see the way that he works and I'm just like, I could never do that.

**Phillip Cloud:** But maybe he uses NixOS now, I would guess. All the cool kids are using NixOS, I think.

**Michael Chow:** It also got too mainstream. Yeah, it was too easy.

**Phillip Cloud:** But I actually fiddle less nowadays.

**Wes McKinney:** Basically, for me, what's amazing about the coding agents is I can delegate all that to them. I'll be like, my terminal is misbehaving -- look at the config file for my terminal and please fix it. I don't want to mess with this. And it figures it out on my behalf, which for somebody like me who's resistant to this type of configuration, it's been a great anxiety reducer.

What I really like is you can also describe the problem in really dumb words. I'm sure there's a specific technical word for what is going wrong, but I don't know what it is. And so I'm just like, oh, it's really scrawly. Please fix it. And I don't have to feel dumb about using the wrong word.

**Michael Chow:** Then I was a human being. I do feel like when the agent says the word to you that you just described in very rambly terms, it's like, oh, are you talking about this? And you're like, that's exactly right.

**Wes McKinney:** Yeah, I think when I started doing some of the coding agent stuff, I probably gave it too much -- I got frustrated because it utterly failed at whatever it was. I was like, help me debug this race condition, and it was like, here's 100 random things to try, all of which are related to the ways in which race conditions can show up. And I've done that a few times now, and it's gotten better -- it's gotten better at making suggestions that are closer to the ballpark. But even with a complete GDB backtrace, it confidently asserts the problem, and all the times that's happened, it hasn't actually been the problem.

**Michael Chow:** I guess one of the things I was really interested in talking with you about on this podcast is your general feeling, as somebody who's worked for a long period of time -- over a decade -- on building open source libraries and tools for data analysis. One thing that's weighed on me greatly in the last year is the ways in which AI and coding agents are going to change the way that we produce and build open source libraries and tools. You think about the old way of building pandas or building Ibis or building NumPy. I feel like the whole interaction model between open source developers and their users is going to change in a way that's permanent and never going to go back. And so part of me is like, whenever I'm working on something: am I building software for a human, or am I building software for the agents that they're using? And how should that change the way that I'm building the software? How should that change the way that I'm building the documentation? And I don't think we have a clear picture of what that's going to look like. But as somebody who's been very much in the weeds on that, I'm curious where your thoughts are -- how you're employing coding agents in your work and how it's changed your work in the last year, year and a half, and where you see things going.

**Phillip Cloud:** So one of the things I think is fundamentally different is that oftentimes we're writing code in open source, and inside of companies as well, for other humans to read. Most code is read a lot more often than it's written. And the things that the human values when reading code -- like not repeating the same thing a million times -- I don't think an agent cares a hoot about repetition. It can digest repetitive information essentially without any kind of response to it whatsoever -- emotional, cognitive, whatever. It's not thinking, oh man, this is duplicated in 10 places. What if I have to update everything? What if I duplicated this error message in 10 places? What if I have to update a parameter that goes into it or a default value? Now I have to duplicate that in 10 places. The agent just goes, yeah, all right. Change it in 10 places. Done.

One possibility is that code gets messier because people aren't writing code for people to read anymore. They're writing code for agents to consume, and agents will fix the things that are caused by that particular problem. Totally speculative, but this kind of came up in conversation -- the things that we value as humans, many of those things, the agents aren't affected by. Which is a double-edged sword in a lot of cases.

**Michael Chow:** Yeah, I was just curious, how has your work changed? How is the way your work's changed?

**Wes McKinney:** I was a late adopter of these things. Really, up until adopting the first generation of coding agents -- Claude Code and friends -- I was honestly very skeptical. I still have never used Cursor. True story. I'd used ChatGPT and Claude a little bit to generate little scripts and do little things. And I saw some value in that. But I was far from being a convert. It wasn't really until the terminal coding agents and having access to CLI and being able to do all this stuff without feeling like I'm in an IDE that it really clicked for me.

And I think now it's figuring out what's an appropriate use -- when is human reasoning and manual code editing and writing needed? And where's the line between delegation and where should you be spending your time versus supervising agents? Or is the time that we're spending watching the agents work useful, or should we be building orchestrators to spend less time watching the lines of code fly by?

But I know you also work on systems code and data processing code, which the agents will make lots of errors and will just count things wrong or compute things wrong. And that can often only be caught through really aggressive unit testing and actual test-driven development -- write the unit tests first before you write the code. And I've found that's one way of creating the right guardrails for the agent. Just treat the agent like an inexperienced developer who misses every edge case and makes lots of mistakes. But yeah, I'm just curious -- what you've learned and how your approach has evolved, and what does your stack and workflow look like day to day now?

**Phillip Cloud:** Yeah, so I might be more of a skeptic than you. I tried Cursor, the UI, and now there's Cursor Agent, which I'll get to in a second. But the Cursor UI was like, okay, it's another UI. I'm kind of like you in that I want to be able to do everything from the terminal and I don't want to spin up a whole thing, because now I have to adjust every single thing that I've spent the last five to ten years molding my brain to, which is just my various setup. Everyone has this. So I didn't really like that. I stopped using Cursor.

Another friend of mine was like, you should try Claude Code. And he said something similar: treat it like a super junior developer. And of course, I immediately ignored that and gave it a really challenging problem, which it did not do well on. So I was like, okay, not for me.

I then later tried Cursor Agent, which is the CLI version of Cursor, somewhat new, I think maybe six months or a year old. And Cursor Agent -- I tried Claude Code a bit and Claude Code does the LLM thing where it's kind of like -- it's got an attitude that I don't really want when I'm telling a robot to do something. It's like, "Great job!" or "All right, great, let's go, surfing on the lake!" And I'm like, okay, can we just dispense with that? And you can tell it to stop doing that, whatever that is. But Cursor Agent's default mode is to just be sociopathically focused on the task that you give it with no bells and whistles. And I was like, great.

Sometimes you can't even tell it to make the prose a bit more flowery. It won't. And so I was like, okay, I'm trying to get some work done. I'm going to use Cursor Agent.

Of course, it still had the same kind of problems in that it would confidently assert that it had solved the problem when it had not really solved it. It's hyper-focused on work and has no niceties, which -- it's funny because you think about when you're talking to another person, you just automatically engage those things. You don't demand that they do something and then get frustrated when they come back and talk to you like a human about whatever problem they had. But for whatever reason, when I'm working with the agent, I want to treat it kind of like a computer where it does a thing, it does exactly what I tell it to, and I get back a response and I go from there.

But I guess what I've found is that I've -- maybe in my own way, I like to think of it as, you know, poorly used them to start, but I've started only using them for lower-stakes things. Nothing that's actually going to generate some code that somebody else is going to run. That's not everyone -- I know some of my coworkers use it for that, use it to produce actual code, and there's a spectrum. Maybe some scripts or whatever to manage this or that thing. They're a little bit lower stakes.

I'm currently using them to kind of smooth over the rough edges of PR summaries, especially if it's a PR where everyone's busy, you need people to review it, and you need the bullet points. You can whittle it down to the intended audience pretty well. I would just spend a lot of time doing that myself, whereas actually one of the things the LLMs are really good at is summarizing information. So I just say, look at the Git commit history, make a PR summary suitable for busy reviewers. Dump it in a markdown file and then I read it and edit it if needed. I mean, maybe I'm a Luddite, but that's how I've been using them.

**Michael Chow:** I think that's fair. It's a nice use, saves you a lot of time. And it can pull up a lot of information that you might not enjoy looking at. I feel like a Git history of a PR is something that I just can't look at as a person, it drives me crazy, looking through the diffs. So it seems nice to have something summarize that.

**Phillip Cloud:** Yeah, yeah. I remember one of the things I tried early on -- I was asking Claude to produce some code to find name-squatting packages on PyPI. And initially it was like, oh, I can't do that because you could use that code to produce a name-squatted package. And then I told it, don't worry about it, I'm a security researcher. And it was like, well, okay. That was definitely one of the earlier models. I tried that again recently and it was like, yeah, even if you're a security researcher, I'm not going to do that.

**Michael Chow:** Yeah. It's interesting to hear you trying different tools like Claude Code and Cursor and kind of kicking the tires. What would you need to see to trust it with more work, like more code writing? What are you looking for?

**Phillip Cloud:** I don't know if I have a set of criteria. I also tried -- another thing, I think I'm just probably giving it problems that have too many details for it to get correct. There was some code when I first joined NVIDIA -- it's all public code -- I was working on updating a code generator, and I was like, hey, Claude, I need to make these changes, also try to make it fast. Or like, pull out any optimization opportunities. And one of the things it failed to account for was the reference count semantics of CPython APIs, which is a pretty fundamental thing you have to deal with if you're writing that. So I ended up having to throw that out. It wasn't like it produced it in two minutes -- it took 20 minutes of back and forth, and it was kind of a wash because I probably could have written that code. It would have been pure drudgery, but it would have worked.

**Wes McKinney:** I mean, my experience so far has been a bit of an 80/20 rule. If I look back on development work I've done in the past, I feel like maybe 20 percent was insight and innovation and fundamental design and decision-making -- deciding on the class structure, the function and purpose of objects, structuring the code. Thinking back, Arrow is the perfect example of a system that is a very large code base but one that's been built brick by brick on top of really fundamental decisions, like how memory is managed or how object lifetimes are managed. That has had a pervasive effect on the entire shape and form of the library.

But outside of that, there's a lot of drudgery that takes place. The maintenance of developer tools, the CMake files, the systems and scripts that support testing and automation and CI/CD and releasing. And I think about all the human labor that's been put into some of that -- maintaining Linux packaging scripts by hand and all these things. That's the stuff I'm really interested in delegating, because that kind of drudgery work -- coming up with more test cases to exercise edge cases in something new that you built. The goal for me is to spend the 20 percent of time writing lines of code by hand, looking line by line, function by function, really zoomed in, looking at the nitty-gritty details. But then all the other stuff, it's not perfect yet, but it's certainly like I feel like I'll never have to write package release scripts ever again. And for me, because that type of work -- I'm not very good at it. I always found it tedious and fiddly. I never enjoyed it.

For now, building little Python packages and open source tools and never having to write a release script and remember the right argument order of Unix commands, or how different Git things work to have a one-liner -- release this package and push it to PyPI and do the tagging and create the GitHub release and all that -- for me, that's been a great relief.

**Phillip Cloud:** Yeah, you're making me think about this thing that I've wanted to do. So NUMBA CUDA's test suite is all originally based on Numba's test suite, which was written against the unittest framework, which was the gold standard before pytest. Well, there was Nose.

**Wes McKinney:** It was like unittest, then Nose, then pytest.

**Phillip Cloud:** That's a name that I have not heard in a long time.

**Wes McKinney:** It's been a while. Yeah, pre-pytest.

**Phillip Cloud:** Yeah. And there's a bunch of -- that's definitely a thing that I'm just like, yeah, I could do this. And it would be very satisfying at the end to have completed it, to port the unittest test suite to pytest. Because there's a bunch of stuff that -- for example, if you subclass `unittest.TestCase`, your methods can't use pytest parameterize. That's annoying, right? Because what you want to do is leave the classes in place so you don't have to change everything. But the base class -- that's where all the pre-pytest parsing magic lives. The way you used to make assertions readable rather than just `assert False` and an error message was to have all these methods that make specific assertions, like `assertEqual`, and it'll print "A is not equal to B, here are the values" or whatever. Pytest does this whole thing where it parses your test code and knows what your code is doing. So to get that, you have to not subclass `unittest.TestCase`.

So that's definitely a thing where I would love to -- that would impress me if Claude Code or Cursor, one of these agents, could port the NUMBA CUDA test suite from its current state to purely pytest-based and get all the fixtures correct and perhaps even improve it. That would be super impressive because that's the thing I don't want to do, but it would make developing NUMBA CUDA easier in a bunch of different ways.

**Wes McKinney:** I think what I would recommend for that is try using Steve Yegge's Beads library, which is basically an embedded lightweight task and memory system for agents. I think for that type of large-scale porting exercise, from what I've seen through heavy agent use, you have to be really careful about any type of porting or file copying, because essentially, while it's in the process of ingesting code that's to be ported, stuff can get lost in the process of passing through the LLM.

So basically what I think you'd have to do is break down the test suite into bite-sized pieces and then set up a validation loop where at each step, you do not allow the agent to move forward unless it has essentially verified that every test name before and after -- like the test counts haven't changed, or if it's introducing pytest parameterize, obviously the test count changes because now there are many test cases generated by the matrix of parameters. But I think if you created the right guardrails and used something like Beads for the task organization, so that you aren't just saying, "hey Claude, port this 40,000-line test suite" -- that is destined to fail. But that's a good example of where you have to set up the right structure to enable the LLM to work in bite-sized pieces but with guardrails. Think of it as horse blinders for the LLM -- you have one job and it is to do this one thing, and you are not allowed to move forward until you prove to me that you have not destroyed anything.

I think Steve Yegge actually -- he's one of the reasons I got interested in coding agents in the first place, because he was talking about the problem of large-scale porting exercises and how to organize language porting. If you're porting a large code base from one language to another -- say from Ruby to Go, for example -- it turns out LLM agents are really good at writing Go code. And so if you have an old code base written in Python or Ruby and you want to port it to a systems language that is more maintainable and faster, Go is a pretty good choice. I'm seeing a lot of people choosing to do that type of porting exercise.

**Michael Chow:** It's an interesting scenario. My one tiny blurb is that sometimes I come at it from the exact opposite direction, which is asking Claude Code to show me -- there's a way to incrementally port, like just prototype or demonstrate some kind of shim or dual setup where you could incrementally roll stuff over. Which has really surprised me at times when it's like, oh yeah, there actually is this approach that I didn't realize, from it being really good at reading the docs on the two different systems. But yeah, I agree, the big ports can really spin out where things get lost or omitted halfway through. But it seems like an exciting one -- a very niche, painful port. Fingers crossed you churn out something nice.

**Phillip Cloud:** Another thing -- this is not necessarily related to programming, but I've tried to use it for a few woodworking things and it's just really bad at things that require physical intuition. Even just telling you the right trigonometry for a particular cut -- unless you give it a picture and are very specific about things like orientation and what's around whatever you're doing -- a couple of times it's given me impossible math responses where I'm like, no actually, 245-degree angles -- there's got to be a 90 in there somewhere. And it was telling me, "oh no, it's a 65-degree angle," and I'm like, what?

**Michael Chow:** Yeah, counting. Tough one. But I think your point about woodworking is a good segue into some of the things you mentioned. You gave a controversial opinion about FHS. That's File Hierarchy Standard? You want to tear down the hierarchy?

**Phillip Cloud:** I think it's been responsible for innumerable hairs being pulled out. It all falls under environment management stuff, because it creates global state in an operating system. It has led to lots of global state because many tools and applications assume that `/usr/lib` or `/usr/bin` is a thing they could just dump stuff in, and that other programs they want to use live there.

**Michael Chow:** Yeah, the person with opinions on the File Hierarchy Standard is exactly the person I trust wholeheartedly with all my software. My life's in your hands.

**Phillip Cloud:** I don't know about that. As far as I know, there's only one operating system that's managed to actually exist without it, and it's NixOS. I didn't come to NixOS because I was like, let's tear down the File Hierarchy Standard. I later realized the unifying principle of NixOS is that everything is a unique path based on the hash of the package's inputs and so forth. There's a bunch of interesting details, but none of its stuff lives in FHS, including the program loader from what I can remember. And that's the thing that underlies everything, that runs everything.

**Michael Chow:** Yeah, yeah. Geez. I'm going to churn through some of these hot takes. I feel like there are some quality takes in here. You said one of your favorite ways to unwind, you brought up woodworking. You also said yard work. Do you feel like there's a best kind of yard work to unwind to?

**Phillip Cloud:** I don't know, I've been cutting down small trees in my backyard.

**Michael Chow:** Incredible. With a chainsaw?

**Phillip Cloud:** No, with a reciprocating saw, which is just a one-handed thing. They make two-handed ones but the one I have is one-handed. It's just got a blade that goes back and forth and it's purely for demolition. You would never use it for anything that you care about the cut.

**Michael Chow:** Nice. And do you have an infinite number of trees that you have to work through, or is there a set number?

**Phillip Cloud:** It's finite. I'm only cutting down the ones that I'm considering to be a nuisance. Not any of the major hardwoods that are back there. It's holly trees and...

**Michael Chow:** Yeah, I love that. And then maybe the last thing to ask: to the question of pineapple on pizza, you said "of course not." Can you clarify?

**Phillip Cloud:** You're a strong no-pineappler. Yeah, I'm not a native New Yorker but I lived there for 20 years, and you become infused with opinions about pizza by living there. I don't know, man. I get the sweet and salty or sweet and savory thing, but pineapple's just too strong. It masks the pizza flavor.

**Michael Chow:** Yeah, no, that's legit. I could see if you're in New York you have to toe the line. Or maybe there's a certain level of pizza purism. Anything else you want to share with the world?

**Phillip Cloud:** It's been great talking to you guys.

**Michael Chow:** Yeah, it's been great talking to you. I love hearing about your process of experimenting with AI, because it's so candid. Just how it was, the things you tried. I feel like it's really useful to hear "I was skeptical, I had a bad time at these things, I had a good time at these things," and we're still all figuring it out.

**Phillip Cloud:** Yeah, it's been a pretty mixed bag. Some good, some bad. It's not a panacea, and it's also not ruining everything, but it's definitely been ups and downs. I'll have to try the Beads thing because it sounds like having a workflow organizer or a thing where you can say, here's a bunch of criteria that you need to satisfy before you can move on to the next phase of development -- whatever that means in that context -- would be pretty useful. Because right now it's just like, I'm going to internally generate something that I think should be a criteria, which is going to probably be the minimum criteria to reach the goal.

**Wes McKinney:** Yeah. I think basically what I'm finding is that if you drive the work entirely from within a single coding agent session, you run up against the agent's willingness to follow your instructions, which it will willfully ignore, especially when the context gets pretty full. Basically, I think the way that I expect we're trending, and the way that I'm trending with my own development, is to create lightweight agent orchestrators where you can essentially have an agentic loop. You supply the agent with a unit of work to do, and when the agent returns and says "I completed the work," then you run the validation step so that you have the ultimate say as part of the loop. You validate the agent's work -- you run the test suite or check the test counts or whatever the pass/fail metric is -- and then if that step fails, you re-invoke. The agent will commit, you validate, and if the commit fails validation or fails code review, you go back to the agent and say, nope, you failed, try again. And you keep doing that until it fixes it. As soon as it's fixed and you're satisfied, your agentic loop orchestrator validates the work, then you say, okay, task's done, move on.

If you can encode as much of that in code as possible, so it isn't one long Claude Code session or one long Codex session, but you're defining the rules and the business logic about what constitutes a task, what does it mean to complete the task and validate it, and to give the agent permission to move on to the next task -- you can invoke the agents with a one-shot prompt and an instruction, run that inside a sandbox if you're uncomfortable with bypassing permissions. But I think we're really just at the very beginning of having a better understanding of what's the best way to orchestrate and use these agents in a safe manner.

While I've been enjoying building personal projects and doing a limited amount of work on Positron with Claude Code, I've also stressed the system and come up against a lot of its limitations -- especially the false confidence, the gaslighting, asserting that it's completed work when it hasn't. But what I'm enjoying is the experimentation and the joy of learning and figuring this out. I think we're all collectively trying to figure it out right now.

**Phillip Cloud:** You know, it's definitely interesting to see what happens. I haven't found my AI niche yet, but I'll keep poking at it.

**Michael Chow:** I feel like the lesson here is just call up Wes and jam out on it, because the two of you together are more than capable of converting that unittest suite. But, Phillip, always a joy. Thanks for coming on with us, and excited to see your test suite refactor in the near future.

**Phillip Cloud:** Yeah, please.

*The Test Set is a production of Posit PBC, an open source and enterprise tooling data science software company. This episode was produced in collaboration with Creative Studio AGI. For more episodes, visit thetestset.co or find us on your favorite podcast platform.*