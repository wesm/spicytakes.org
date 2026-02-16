---
title: "Rebecca Barter: Persistent learning, tool building, and 'Will code even exist?'"
summary: "Podcast at The Test Set (Posit)"
date: 2026-01-13T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-rebecca-barter
word_count: 9780
source_file: transcripts/2026-01-13-test-set-rebecca-barter.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://www.youtube.com/watch?v=qpaw2sHaR7Y"
---

{{< video https://www.youtube.com/watch?v=qpaw2sHaR7Y >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, Michael Chow, Hadley Wickham, and I talk with Rebecca Barter, a senior data scientist at Arene and adjunct assistant professor at the University of Utah. Rebecca describes her work in healthcare-focused data science, where she splits her time between building internal tools and pipelines and doing exploratory data analysis to improve patient outcomes.

A large portion of the conversation centers on AI coding tools. Rebecca shares her experience preparing her PositConf talk "AI: Hype, Helper, Hindrance," noting that the tooling landscape changed so fast between proposal and delivery that she had to rework her material. Her conclusion was that AI tools are mostly helpful, though they can be a hindrance when they give confident but wrong advice, especially for newer or less-documented tools. I share my view that "vibe coding" is overhyped and that having an experienced person in the loop remains essential for quality output.

We discuss how AI changes the learning process. Rebecca describes using AI as a tutor when picking up Streamlit, getting it to generate example code and then interrogating it line by line rather than blindly accepting output. Hadley raises the question of whether programming skills will remain important as tools improve, and Rebecca speculates about whether code itself might eventually become obsolete for certain tasks if AI can reason directly from questions to answers.

Rebecca also talks about her path from teaching R workshops to faculty and postdocs at the University of Utah to working in industry. She finds the most transferable skill from teaching is the ability to explain technical results clearly to non-technical stakeholders. We close with some lighthearted discussion about accents, the word "data," and the differences between jumpers and sweaters.

## Key Quotes

> "Sure, I'm really good at R and I'm decent at Python now. But those are not the things that are going to propel me in the future. The thing that's really going to propel me is, you show me a new tool, I'll play with it and learn how to use it really quickly." -- Rebecca Barter

> "It gives you a lot of very confident advice. It doesn't tell you, 'Hey, I don't actually know much about this because it's kind of new.' It very much gives you confident advice and you end up trying to spend a lot of time debugging the terrible code that it gives you because it's just made it up." -- Rebecca Barter

> "Coding agents have revealed something that we already knew deep down, which is that probably 80% of the work that we do as programmers is not that special. But where the actual value is in that 20% that requires judgment or requires synthesizing your experience or your background in a certain domain." -- Wes McKinney

> "I love taking someone who doesn't know anything about a topic from that point to being like, 'Oh, it's not actually that complicated.' Making them realize that it's not that complicated is the thing that I find the most energizing." -- Rebecca Barter

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field. On this episode, we sit down with Rebecca Barter, senior data scientist at Arene and adjunct assistant professor at University of Utah, who has really interesting perspectives on learning, teaching, and demystifying AI.

**Michael Chow:** Hey, everyone. Welcome to The Test Set where we dig into the people behind the data. I'm joined here with Rebecca Barter, who's a senior data scientist at Arene and an adjunct professor at University of Utah. I'm joined by my co-hosts, Wes McKinney, who's a principal architect at Posit, and Hadley Wickham, who's chief scientist at Posit. Rebecca, we're so happy to have you. I thought as maybe a quick icebreaker, I could just start off with something you said. There's so much I want to get into, but just really quick. You mentioned a lot in prepping about AI, and teaching, and kind of your path. But one thing that stood out to me was, you said you're not the kind of person who can work on something you don't care about. And I feel like that is so relatable. I thought maybe you could just kick us off with a little bit of that.

**Rebecca Barter:** Absolutely. Yeah, no, I get bored easily, I think is really what happens. So if I'm given a bunch of tasks, or working on a kind of field that I'm like, there's no point to doing any of this, it's just mindless tasks, I start just staring out the window thinking about what I'm doing with my life. So I'm very much like, if I wake up in the morning and I have tasks where I'm like, yeah, I actually care about completing these. I feel like there's some kind of impact, whether it's to other people, to the company that I work for, or to a field as a whole. I'm going to be so much more engaged. I'm going to actively have fun. Whereas if I wake up and I'm like, all right, let's just kind of get butt in seat and do the thing I got to do, and it doesn't really matter if I do it or not, but I have to do it -- I'm going to probably stop trying at some point. That's just, it's not me. Some people can.

**Michael Chow:** No, that's so real. And as I understand it, you're in Tahoe, so you live in the mountains. So if you're not motivated, also you have all these beautiful mountains outside.

**Rebecca Barter:** Exactly. And I've definitely done that. Before I was living in Tahoe, I was living in Salt Lake City. It was the same thing. So there's like mountains right there. You know, anytime I start feeling that feeling of like, I don't want to be doing this, I find some kind of excuse to just go run away in the mountains and stop doing the task.

**Michael Chow:** No, I feel that so hard. How do you, Wes, how do you feel about -- can you grind through things you don't want to do?

**Wes McKinney:** So sometimes you have to do work that you'd rather not, but it's for the greater good or like the project just is not going to be able to move forward without it. So I've definitely found myself thinking back on the early days of pandas -- everything having to do with Windows was the thing that I didn't want to do. And so there was a dark period where I had my Windows virtual machine, which was the blessed place where I would create the installer packages for pandas. This was before we had wheels. This was before Conda and UV -- it was dark times creating these .exe files to install pandas. And at no point did that ever spark joy. This was purely work that needed to get done for the greater good of the project.

**Michael Chow:** Yeah, I can see Windows -- no shade on Windows, but yeah, sometimes Windows is being the demotivator. JJ used to say that, I think it was some company, he was like, if you want people to work on Windows, particularly Windows installers, those people just need an automatic bonus because it's such important work, but no one wants to do it and it's painful.

**Rebecca Barter:** I think that that comes around in a lot of aspects as well. I feel like whenever I'm teaching a workshop, it's always the people on Windows who have installation issues. And I'm like, I have no idea how to help you because I don't even know how to use a Windows machine normally.

**Michael Chow:** Yeah, that's real. Well, I hope that you're working on a lot of things you do want to do right now. And I think, yeah, I'm so curious to dig into a bit about your AI work and what you're doing as a data scientist now. I figured one approach that might be nice is maybe you could tell us a little bit about your work at Arene now, and then I'd love to circle back and maybe talk about kind of your path to getting there a little bit.

**Rebecca Barter:** Absolutely. Yeah. So, I mean, I think related to your previous question as well of like, I like to do things that I'm passionate about, really is kind of what it's about. The thing that's really got me going in terms of data science has been applications in healthcare and the kind of patient-focused approach to analysis, trying to help improve patient experiences. And so that's a really big part of what's driven me to my current position, which is at Arene, which is a medication management startup where we're really trying to make sure people are taking correct medications, they're adhering to their medications, all of that stuff, really focusing on the patient experience and trying to make sure we're improving health outcomes. So that for me is something that I can wake up in the morning and be like, yeah, stoked to do that.

I'm also lucky that I get to work with a lot of really wonderful, intelligent people who are kind and just a joy to work with, which makes a big difference.

**Michael Chow:** Yeah, that's awesome. What's the team you're on like? How many people do you work with and what's the setup?

**Rebecca Barter:** Yeah, we're a team of like maybe 10 to 12 people. We're kind of split between health outcomes and data science. And I kind of do both. I do a lot of tool building. So if there's a lot of tech debt and things that have been built that are really ad hoc and inefficient, I do a lot of working with whoever wrote that original code to be like, let's create this, just turn this into a pipeline where you just run a script, it maybe does something with Quarto even down the end and creates this nice report. And you don't have to run this and then run this and then change this config and then change that config and then run that and then run that. And then, oh, you want something else? Okay, let's do it all again.

The people that I work with are a big combination of engineers, people with stats backgrounds, people who are more data science background. It's a pretty diverse team and it's really cool. Everyone's really easy to work with and really friendly.

**Michael Chow:** Oh, cool. Yeah. I love the role where you get to kind of roll in and help spruce things up and put some glitter on it. How do you find, how do you choose what to beef up or which tools need a little bit of tool love?

**Rebecca Barter:** Yeah. Usually it's pretty clear when we've got inefficient pipelines. I think it's also a nature of being a startup where a lot of things are built kind of ad hoc and for individual customers, and then it's like, oh, we need to scale this up to be more general and more applicable. So a lot of the time there's things that we do repeatedly for customers that are very clear -- this could be improved. It's pretty easy to point towards, okay, that particular pipeline is really inefficient and could very much benefit from having someone create an overall compute pipeline that makes it a lot easier to go from point A to point B, rather than going point A, point one, point two, point three, and then eventually you get to point B and you realize a lot of things that you could have done differently along the way.

**Michael Chow:** Yeah, for sure. And I think you mentioned before this that you've done a lot of R work, but that you might be doing a little more Python and stuff now. I'm curious about the kind of mix of tools you're using in your work now.

**Rebecca Barter:** Yeah. So for a very long time, I learned R when I was like 18. I'm not going to tell you how old I am now, but I'm older than 18. I learned R before the tidyverse existed, before Hadley had created ggplot, all the good stuff. And that was very much what I was comfortable with. I was like, yeah, I get it. I'm R queen, you know, I know how to do R things. And then Hadley came along and ruined everything. Because now he's created all these new tools that are way better that I have to go and learn.

I remember someone being like -- I was fortunately in grad school by this point -- "Okay, we're going to use this new thing called ggplot and dplyr in this project." And I was like, can't I just do what I've always done? And it was like, no.

So that forced me to learn. And in that experience, I also very much realized, oh, things do kind of keep changing. You can't just learn the one thing and say, oh, I've mastered it. You never really master it because what you've mastered today is going to be really irrelevant -- these days, really irrelevant in like three weeks. But back then it was like a couple of years.

Through grad school, I did a lot of R. I feel like I got pretty good at R, mostly a lot of the stuff that Hadley and co have built. In academia, I was in a statistics department and people are using R -- that's the normal thing.

Then gradually, as I started trying to intentionally expose myself to projects where I would be forced to learn new tools, someone was like, oh, hey, I've got this project -- and I realized it would mean I'd have to learn some NLP, I'd have to use Python. The stakes were low. So I was like, this is perfect, because this will be a really good opportunity for me to learn new tools where there's no particular deadlines, they don't have any expectations. This is when I was at the University of Utah full time. I found some collaborators in health informatics and health communications that really wanted help with a lot of text data. I specifically took that on because it meant I was going to learn something new.

Now I've transitioned to industry. Especially with the advent of AI, I feel like I've gotten really good at picking up new tools. And I think that's one of my main skills. Sure, I'm really good at R and I'm decent at Python now. But those are not the things that are going to propel me in the future. The thing that's really going to propel me is, you show me a new tool, I'll play with it and learn how to use it really quickly. Mostly because, as long as you can get to a basic level of competence, AI can kind of help you get the rest of the way these days pretty quickly.

In terms of the specific tools that I'm using -- yesterday I used Python, I used R, I used Quarto, I used Streamlit, which is like Python -- it's kind of like Shiny but not really, like Shiny Python kind of. I stared and got very confused by an AWS step function. I use SQL. Every day I'm just exposed to such a broad array of tools, some of which I'd never even heard of six months ago.

**Michael Chow:** Yeah. That's cool, you're able to just pick up new tools and kind of move into them faster. And I almost wonder, it's interesting you brought up ggplot2 also as being the one someone might dread learning, because I think ggplot kind of warns people -- it doesn't say you're going to have a bad time, but I think it's like, you're going to need to put some work in before you have a good time.

**Hadley Wickham:** One of those branding startup messages used to recommend reading a whole book.

**Rebecca Barter:** I distinctly remember when I first started using ggplot, I was trying to make just a simple scatterplot and I just kept getting an error and I could not figure out what I was doing wrong. I'm sure now thinking back, I was just missing the aes function. But I was getting so frustrated. Now I look at it and I'm like, well, it's so obvious and it's so clear. I think it's just when you aren't used to learning new things, especially when it's a big change in syntax, you kind of look at the code and you can't see what's wrong with it.

**Hadley Wickham:** It's also a different era of getting help. There wasn't obviously chatbots. There wasn't even Stack Overflow. There was the R help mailing list, which was pretty unfriendly.

**Wes McKinney:** Yes. I mean, a thing that's been keeping me up at night lately thinking about is -- I feel like the whole model for how people discover and start using new open source technologies, new R libraries, new Python libraries, is going to have to change. Because our LLM coding agents and assistants are all really good at all of the projects that exist now, which have rich bodies of training data available on GitHub and Stack Overflow and all over the internet. But if you build something new, almost by definition, there's not going to be any training data available. And so essentially we're going to have to build things in such a way that we can point the agents at the project's documentation or create projects in such a way such that this new thing can be presented to our AI co-pilots so that they can figure out how to take advantage of something new. Because otherwise we're going to end up locked in the present moment -- nobody uses anything new because their LLMs don't know how to use it. And the snake has no tail left to eat at a certain point.

**Rebecca Barter:** No, I think about that a lot actually. And I encountered that. Because I mentioned I've been using Quarto -- specifically what I've been doing with Quarto is building a quite sophisticated Quarto dashboard report with all the tabs and cards and all this kind of stuff. And I'm using Gemini because that's what we use at our company. And it does not know anything about Quarto dashboards.

My default now, when I'm looking something up, is I type it into Gemini or GPT or whatever I'm using, or I use the inbuilt thing in my IDE. That's my go-to now. And it's very clear to me when I encounter something that's new -- it gives you a lot of very confident advice. It doesn't tell you, "Hey, I don't actually know much about this because it's kind of new or there's not a lot of documentation." It very much gives you confident advice and you end up trying to spend a lot of time debugging the terrible code that it gives you because it's just made it up. It doesn't tell you that it made it up.

At the same time, I used to write a lot of blogs, tutorials and stuff on a lot of R stuff and coding stuff. And there's not nearly as much incentive to do that anymore, because people aren't Googling "how do I use the purrr package?" They're going to AI and they're being like, "How do I use the purrr package?" And it's going to do a much better job than I ever did.

So things are shifting a lot in terms of how we learn things and how we troubleshoot. And I don't know how that's going to look in terms of new stuff coming out that really doesn't have a whole lot of documentation and people asking good questions and giving good answers on Stack Overflow. Who knows?

**Michael Chow:** Yeah, I do. It's tough too. I love blogs so much, just somehow also encountering a new person with a blog when they have a post that really resonates with you. So that is a tough one, thinking about motivation for certain types of blog posts being lower.

I guess maybe one thing that would be cool to talk about is, on the topic of AI, I know you gave the talk, "AI: Hype, Helper, Hindrance." Maybe you could explain a little bit of that.

**Rebecca Barter:** So that was at PositConf. Yeah, that was a really fun talk to give and to prepare actually. It was kind of funny. When I started preparing it, or when I proposed the talk, I was very much like, yeah, I know how to use all these AI agents and whatever IDE I was using. I was using VS Code a lot because I wanted to use Copilot -- that was kind of the main option when I started using it. And then I came around to the point where I had to actually write this talk and everything had changed. Literally there was no resemblance between how I was using it when I started to how I was using it or could have been using it.

Because it's another one of those things where it's really easy -- you start using it and then you're like, okay, I get it. And then you stop paying attention. But basically so many things have been added. There was now an agent, and I kind of focused that particular talk a lot on the Positron Assistant, but it's the same -- I'm using Claude in PyCharm a lot in my current job, and VS Code has equivalent stuff as well. There's an agent, there's an editor, there's a chat, there's code completion -- all this stuff that is now a part of these AI tools for coding that I really wasn't keeping up with.

I feel like I do this kind of wave where I'll learn something and then I'll be like, yeah, I get it. And then I'll suddenly realize, oh wait, it's moved on. And then I'll have another rapid period of learning and then stagnate again. And then I'll be like, oh wait, what? It can do what now? It's hard keeping up. I struggle with that for sure.

But I think my conclusion from this talk is -- I've been using these tools for quite a while now. I probably started when Copilot was pretty new. And hype, help, or hindrance: well, it's kind of hype -- it's not really going to do everything for you. You have to really be able to tell it what you want it to do. It can't really read between the lines if you give it a very vague prompt. So I don't think it's going to take our jobs. Is it a hindrance? A little bit -- it gives you wrong code, there's security issues, sometimes it just sends you in circles. But mostly it's just really helpful. Honestly, all of these tools -- Positron Assistant, GitHub Copilot, Claude Code -- that are embedded inside of your IDE, whether it's Positron or VS Code or PyCharm, I think I said in my talk, for some projects they don't really help me much at all. If it's a pure R project, I'm so good at R that I don't need help, I don't have to think that hard. Whereas if it's another project where I'm using Python or writing a bunch of really complex CTEs in SQL that I'm not that good at, it means that instead of spending all my time Googling how to fix the thing that I did or figure out what function I need, it helps me -- I know exactly what I want to do because I have that base competence, and it just really helps me go from that level of "I am kind of competent in this but I'm not an expert" to "I can just produce the thing as if I was an expert." It really covers that gap really well.

So I think my conclusion was hype, help, hindrance, all three, but mostly help.

**Michael Chow:** Yeah. Did you get any feedback or response? Did you have a sense for the audience, how people felt overall?

**Rebecca Barter:** Yeah. I had a lot of people talk to me after this talk. And for the most part, it was actually a lot of people who felt like they didn't know how to get started with these things. So they weren't even at the point of saying whether it was hype, help, or hindrance -- they were aware of these things existing, but just literally didn't know how to use them or what they are.

Preparing for that talk, I was talking to several people during the speaker coaching where they're like, "I think you can assume everyone in the room is going to be familiar with these things." And I was pushing back a lot, being like, I don't think so. I think there's a lot of people -- even me, someone who's very enthusiastic about learning new things, it's hard to keep up. And I think it was a very biased room, that preparation session, where everyone was excited about learning new things and engaged enough to put time into learning how to use these new tools. But honestly, I think the vast majority of people aren't like that. And that's fine. It's not a big deal. It's hard. I distinctly remember this feeling of, I'd learned base R, I'm good. This was the skill that I needed. Why should I learn something new when I can already do everything I need to do just fine?

Yeah, the vast majority of people who came up and chatted with me afterwards were people just being like, "Thank you for just showing me how I can use these things." And like, "I kind of want to give it a go now."

Definitely there's a lot of people who -- the more experienced you are, the more likely you're going to lean on the hindrance side. And sometimes the newer you are as well, because if you lean on it too heavily but you don't actually know anything about the language, it's also kind of a hindrance because you can't debug, you don't know how to prompt it well enough. So it's kind of a spectrum. It's not great for everyone at every stage.

**Wes McKinney:** Yeah. I mean, I was going to say, my hot take on the matter: I've been using Claude Code-like coding agents pretty extensively this year. But I think so-called vibe coding is way, way overhyped, in the sense that there's a lot of people -- AI boosters -- going around saying that soon (trademark), the coding agents are going to allow somebody without coding skills or data science skills to replace a senior or expert person in those fields. But as a user of these tools every day, I simply don't see it.

I feel like being in the loop and reviewing the work that's being produced -- it's helping me go faster, it's doing the typing for me, as one person put it. But I feel like if I weren't in the loop, reviewing the work and giving feedback and catching the mistakes, which it sounds like exactly what you're saying -- without having somebody with the experience in the loop to judge the output, you could end up creating a morass that's very difficult to escape, quite quickly.

And so I can imagine sometime in the next year, we're going to enter some kind of trough of disillusionment where a big wave of business users try vibe coding and end up disappointed and conclude that AI sucks and was overhyped and oversold. And even though they feel like they have a gun at their head saying "use AI or else," a lot of the initial attempts to eliminate data scientists or eliminate coders are going to fail as a result.

**Rebecca Barter:** Oh, yeah. There's definitely a lot of people who are not good at using the AI who think it's just a waste of time and way overhyped. I don't know. I watched Hadley's keynote at PositConf though, so I'm convinced.

**Hadley Wickham:** I was interested -- I read a good criticism of AI by Cory Doctorow, and I think the thing that he kind of pointed out, the real risk right now is not that AI will replace software engineers, which I don't know, the more I use it and even as the better it gets, I'm less convinced of that. The real risk though is that CEOs believe that it's going to replace software engineers and hence start firing them.

**Rebecca Barter:** It's just, yeah, there's clearly like -- I love the tool and how empowering it is, even for me as someone who's a pretty good programmer, but all of the stuff around concentration of wealth and the people involved and the people who stand to make the most money from this, it's pretty icky.

**Michael Chow:** It is so interesting. I find it really hard sometimes with a very AI-assistant-heavy project. In the early stages too, I find it really hard to evaluate, is this even going to pay off? I just feel like sometimes it gets into states where I'm like, I don't know if I'm just generating a lot of garbage. How can I kind of rate, will I be able to reign this thing in? And I also don't know what the moves are either. It feels very managerial almost, but also embracing so much production that it's like trying to control a fire hose sometimes.

But I do think, to that point of "will software engineers be replaced, do CEOs think software engineers will be replaced" -- it is such a funny time. What are the hard challenges that will kind of linger?

**Wes McKinney:** Well, I think what's interesting is that coding agents have revealed something that we already knew deep down, which is that probably 80% of the work that we do as programmers is not that special. It's a lot of configuring YAML files and things that are essential, but not special. But where the actual value is in that 20% that requires judgment or requires synthesizing your experience or your background in a certain domain.

I feel like there is a meaningful difference between the applicability of these coding agents to software engineering versus data science. Software engineering is often implementing something based on a specification and then showing compliance with a specification. Whereas data science can often be as much art as science -- knowing what are the right tools to employ, and then even interpreting the results may be subjective.

**Michael Chow:** Rebecca, I'm curious -- at your work, what do you see with AI? It sounds like you've done a lot of really great work talking about it and helping people ease into it. What have you seen in terms of people picking it up and trying it out?

**Rebecca Barter:** Yeah, I think there's a big spectrum. I know people who have no interest in trying it out and using it and incorporating it into their day to day. And maybe they don't need it. If they're only ever doing stuff that's the same as what they've already done and they're really good at that, maybe it doesn't help them that much.

But then I also see a lot of people who are diving really deep into it. There's a lot of people at my company and outside who are building all these agents to do all this stuff, just to take as much away from the human as they possibly can -- but in a good way for them. They're very excited about it.

I think other people look at that and they get that fear. I mean, the first time I ever used it, I definitely had that fear. I remember I just asked it -- I said, write some code to do -- I don't remember what I asked. It was some kind of R code. I asked it to write for me and it just did it really well. It was early days of ChatGPT and I had this sinking feeling of, "Oh no. Thank you. And how dare you? Everything I've gotten so good at, I really didn't need to get that good at anymore. I just needed to get okay."

I feel like people -- there's so many dimensions. Some people are really excited about it. Some people really hate it. Some people think it's stupid and useless. Some people are very anti, some people are very pro. It's the entire spectrum. And I don't even know what the distribution is because I'm probably biased. I was never anti AI. There's a lot of ethical questions and concerns that I have for sure. But in terms of a tool, once I started getting better at using it, it just increased my efficiency so much that, when I'm talking to people about it, I'm usually trying to convince them how useful it is because a lot of people are skeptical. And I understand, because initially I was kind of like, okay cool, it can write that code, but I could also write that code. But it can do so much more.

**Michael Chow:** I know preparing for this, you mentioned critical thinking skills being a really big piece for a data scientist. I'm curious how that plays into the infusion of AI into your work.

**Rebecca Barter:** Yeah, definitely. It's kind of interesting because I think I use AI a lot more for tool building than I do for actual analysis. When I'm doing actual data analysis where I have to do some exploration -- maybe I'll be like, "How do I write this complicated SQL thing that I need to write?" and AI will do a better job than me, so I might use it to help me come up with my SQL query. But overall, other than sometimes outsourcing code that I can't immediately think of how to write, I don't use AI that much for exploratory stuff.

That is still very much just me thinking and me being like, okay, I see that there's this many claims. Is that normal? How many are there supposed to be? And then I'll go look at another data set and compare. And I'll be like, oh, that seems low. And then I'll have to think about, how do I need to communicate this to the right people? Based on who it is I'm trying to communicate it to, I need to think about, do I just need to write a sentence? Do I need to create a table? Do I need to give them the code? None of that -- AI can't do any of that.

My job, I do a lot of tool building, but I also do a lot of analytics. So it's kind of split 50-50. Tool building stuff, AI all day. The analytics stuff, a little bit of AI -- to kind of help speed up the code writing when it doesn't really matter, I just need the query to be written. How many CTEs do I need? How do I lateral flatten? I can't remember any of that stuff. For that kind of stuff, it is helpful. But for things where you do need to do a lot more critical thinking and thinking about how to communicate things, that's all still me as a human needing to do that.

**Michael Chow:** It's interesting to hear about data analysis -- that when you're in tool-building mode versus data analysis mode, you're using AI a lot more heavily for the tools.

**Hadley Wickham:** Yeah, I'm curious if you have had similar experiences with working on tools versus analyzing data. Do you use AI to analyze data ever?

**Rebecca Barter:** I don't do that much data analysis, but it does seem kind of fundamentally less useful, at least right now, just because there is that loop. You don't know what you're doing -- sometimes you don't know what you're doing in software engineering, but most of the time you've got some task, you kind of know what you need to do. Whereas a lot of the time in data science, you're just like, well, what's going on here? And there's much more of a loop of do something, look at the results, do something else, look at the results. And bringing in all of your other context about what does this variable mean, and remembering, oh, actually there was this problem back in 2020 and you can't trust the data before that.

**Hadley Wickham:** Bringing all of that context -- yes, it would be awesome if that was all written down somewhere. And probably we should be striving towards that just so people in our org know, but also so agents in our org can know. But it feels like we're a long way away from that. It's just the kind of tacit knowledge, and this EDA loop of try something, ask a question with a plot, look at the answer, generate another plot and do that as rapidly and as many times as you can.

**Wes McKinney:** I mean, I've definitely used it for a lot of mundane data wrangling and one-off simple queries. As an example, in my home here, I have some little apps that I've built with Claude Code that I run on machines on my home network that I can access over Tailscale, which is super convenient. But then they have SQLite databases, some of them. And every now and then I'll have a question about what's going on with this -- something looks wrong in this app. And yes, I could SSH into the machine and start SQLite3 and write the SQL query. But using an agent, I don't have to. And everything is very simple. But rather than something taking me 20 minutes of fiddling, it's something that can be done in 60 seconds or two minutes.

So that seems like a good application. But if I were doing something more advanced or requiring discretion or judgment, I would be less comfortable.

**Rebecca Barter:** I think what you said earlier about even as software engineers, 80% of what we do is not that magical -- it's the same for data scientists. A lot of it is just doing pretty routine stuff and having something to help you do that faster is super empowering. But that last 20%, if you completely take the human out of the loop, that starts to get pretty scary and pretty dangerous.

**Hadley Wickham:** Yeah, the AI can definitely help take away a lot of those mundane tasks from us, but then hopefully give us more time to do a lot more of the stuff that is less mundane -- the thinking, you know, whether it's critical or not.

**Michael Chow:** Yeah, that's fair. I find for data analysis, even in the early stages, if the data is messy or there's a lot of uncertainty -- I think Hadley mentioned this a bit about discovering sometimes the really bizarre, complex things that generated specific kinds of messy data. I find I have a lot of trouble with the chunk size of the work that an assistant might do with an analysis -- getting spit out a big blurb or giant piece of work. Analyzing is pretty overwhelming, where in software engineering I feel like I'm much more accepting of a lot of work being spit out.

**Hadley Wickham:** I do feel like it's a bit easier in software engineering too, because you've kind of got this double-entry bookkeeping with code on the one hand and tests on the other. But it doesn't feel like there's an equivalent of that for data science. You're not writing reusable functions most of the time. This is a pure one-off, doesn't make sense for this particular data set. And getting this big chunk of code, which you're either trusting or not as a whole, seems more risky. Like a single big pass to a bar chart when you don't know what's real yet, without the kind of...

**Michael Chow:** Yeah, a bunch of data cleaning and you're like, I'm sure the data needed cleaning, but did it make good decisions along the way?

**Hadley Wickham:** And then the statistical challenges -- you can't look at the data again and again and again in a million different ways. And then after 17 hours of torturing the data and it finally confesses to something, that's no longer -- you can't trust your p-values if you're in some kind of scientific context where that matters. If you're spending your degrees of freedom, you're spending your ability to -- and if the model is doing a bad job, you're just kind of biasing the rest of your work.

**Michael Chow:** Yeah, it's a tough one. Maybe to switch topics a bit. Rebecca, I know you're an adjunct professor at University of Utah and you spent a pretty good chunk of time teaching. You have a PhD in statistics?

**Rebecca Barter:** It's the best PhD to have, in statistics.

**Michael Chow:** Wait, no, I was going to say a blurb about how psychology is the best, but I take it back.

**Rebecca Barter:** No, I think you're probably right. I do feel like you probably actually learn more useful things in psychology classes than you do in statistics PhD classes.

**Michael Chow:** I love -- I don't, maybe it's a grass is always greener. Maybe it's not too late to bring in a third degree and argue that's the best.

**Wes McKinney:** Well, I have a math degree and I dropped out from a statistics PhD. So, yeah, I've got nothing to add.

**Rebecca Barter:** Honestly, I think there's some real power in dropping out. Actually, I would put that as number one.

**Michael Chow:** I'm glad I got a PhD, but I do think strategic dropout is another top contender.

**Rebecca Barter:** Yeah, I kind of weirdly think it's more brave to drop out than to just finish.

**Wes McKinney:** Well, the running joke at the Duke statistics department, whenever I would see my advisor there -- Mike West, who is a Bayesian time series specialist -- he always joked that I was the best student who never graduated.

**Michael Chow:** Yeah, it's high praise. I'm just curious about the teaching aspect. Maybe tell us a little bit about your teaching. And I'm so curious to hear what you learn moving from teaching into data science and industry.

**Rebecca Barter:** Yeah, I mean, definitely the most transferable skill is being able to explain things clearly. I can't even say the word "clearly" when I'm talking about explaining clearly.

I always really loved teaching. When I was in grad school doing my PhD in statistics, it was very clear to me -- I am not a statistical researcher. That is not a path that is ever going to bring me joy or success, however you want to define that. I'm just bad at it. That was very obvious to me fairly early on. But I really loved teaching. I did think for a while, maybe I would go down the lecturer path, be an instructor, until I learned about how that is not a particularly viable path to take most of the time. It's getting better.

But I also kind of realized, one of the main things -- I love teaching. The thing that I love about teaching is explaining things. I love taking someone who doesn't know anything about a topic from that point to being like, "Oh, it's not actually that complicated." Making them realize that it's not that complicated is the thing that I find the most energizing.

And then when I was actually teaching semester-long courses, teaching a lot of undergrads, I found that I still loved when I was actually in front of people explaining things. But then the part where I've got students saying, "Oh my God, if you don't give me an A, you're ruining my life." Students saying, "I don't want to be here, I have to be here." Having to be like, did you learn this well enough to get this grade? When you teach in statistics, if you start teaching upper level classes, you start having to teach a lot of theory that I just didn't care about. Kind of back to -- I can't do things I don't care about. Little things, sure. But the big picture, me teaching a theory class, sure maybe I'd do a decent job at it, but I'm not going to have a good time.

I love teaching really intro-level things. I loved teaching R workshops specifically to faculty, which is a lot of what I was doing at the University of Utah. I was teaching Python, machine learning workshops to faculty and postdocs and people in other departments who wanted these skills because they have data and they didn't know how to do anything with it. They weren't taking it because they wanted a grade or needed it on their transcript, or were just doing it to get a degree. They were taking it because they had a specific reason that they wanted to learn.

I love teaching in those kinds of environments where it's very much taking absolute beginners -- I love teaching absolute beginners for whatever reason -- and helping them realize that doing data analysis with R in particular (my favorite to teach, because I think all the tools that Hadley and everyone for the tidyverse has created are so good for data analysis, so much better than anything else that I've used, and maybe I'm biased just because that's how I learned it) -- taking people from the level of they can't do anything, they think it's so difficult, to, oh, I can actually do some simple analyses. I would teach a two-day workshop -- I don't necessarily think that's the best format, but that was what I was doing. A lot of people after that were able to incorporate it into what they were doing.

I think really that explanation part of it, that way of communicating, is the thing that I took the most from my teaching experience into my job as a data scientist. So much of what I do is, I find something in the data or I have a result and I need to explain to people who are not technical. I need to explain to them, what does this mean in the context of decisions we have to make or things we have to communicate to clients? How do you translate this data thing to an actual practical real-world thing?

**Hadley Wickham:** Yeah, I had a similar experience. Teaching that kind of intro to programming and data science just felt so empowering to people. I feel wistful that the next generation is not going to have that experience, just because it seems like so much of what they're going to do is mediated through AI. That kind of pure experience of turning your ideas into code that the computer then does something with -- it's empowering, and something that I love doing. It feels like the relationship between you and the computer is fundamentally changing. Who knows where we're going to end up, but it certainly seems like your ability to write code is less important now than it was five years ago. I do feel wistful for those simpler times.

I admire a lot of the educators right now who are trying to figure out how to adapt the way that you teach in the wake of, we do things differently now. Not everyone does, but I do. I do things very differently now. And I think people learning are going to be doing things very differently. The way that you teach has to change as well. And that's not always something people are prepared for.

**Rebecca Barter:** But I guess, I mean, people must have had some wistfulness about like, oh, it's so good on the slide rule. And now that skill is just --

**Wes McKinney:** I felt so empowered when I learned how to use the punch cards.

**Rebecca Barter:** The punch cards! Yeah.

**Michael Chow:** It is an interesting trade-off. Do you have a sense, if you had to teach someone how to get started with AI and data analysis today, how would you approach it?

**Rebecca Barter:** Man, that's -- I think about that sometimes. When I was wrapping up at the University of Utah, they were starting up AI initiatives and doing all of this kind of stuff. And I don't 100% know -- I have things that I would try.

Because the way that I learn now is different. I've always taught people in the way that I try to remember, how was it when I learned something, and use my own experiences from learning to teach. So I think now, the way I learn something, and I probably would try and teach in a similar way, is: I try to get the basics down. Sometimes I use AI to do that, but I'm not trying to use AI to do it for me until I feel like I at least understand the general syntax of the language or whatever I'm trying to do.

Streamlit was the example. I had literally never heard of Streamlit and I had to use Streamlit, which is essentially a reactive dashboard that uses Python code. It's a Python library. I went to Gemini and I was like, "I need to create a Streamlit app to create this plot." And I just looked at the code that it gave me. I at least have -- I know how to code. So I can kind of look at that and understand at least somewhat what it's doing. And then I'll go through and be like, what does this line do? What does this line do? Why is it structured like this? I'll try to create something and copy it and run it. Then I'll see what errors I get. And maybe I'll do some regular Googling or AI Googling.

It is very much an interactive thing with AI. I don't start out being like, "Do it for me" and not expecting to learn. I start out maybe being like, "Do it for me" as a learning experience -- do it for me, but I want to understand what you're doing. I do use the AI kind of as a tutor, and very quickly I felt like I understood how the syntax worked and could probably modify it. I couldn't necessarily write it from scratch myself, but I don't know that I need to be able to anymore now that I have AI.

Learning for me -- I want to get to a basic level of understanding so that when I do encounter errors and want to do some more sophisticated things, I know how to guide the AI. But I do actually use AI these days to get me to that point. I don't vibe code and say I don't care how this works, just do it. It's a trade-off, it's a balance.

So I think if I were to teach it, it would be: how do we interact with the AI in a way that we can effectively understand what the code is doing and be able to at least conceptually create it ourselves, even if we can't necessarily write it start to finish, because I don't think we need to be able to anymore, necessarily.

**Michael Chow:** Yeah. It's really interesting to hear. It's like generating a case study for you that you're able to take the example and have it break it down and then try to transfer it to what you want to do as a learning aid. So you pick up a little bit, but you're also not needing to start from zero.

**Hadley Wickham:** The question I kind of wonder about is, do you need to be able to do maths in your head when calculators exist? How important is it that you still have some programming abilities?

**Rebecca Barter:** Yeah, I kind of think at the moment it's still a little bit important, but down the line as these tools get better and better, maybe less and less important. I think we do still need to be able to code, but I don't know how long that'll be true for.

**Hadley Wickham:** There is still the imprecision of English. There's always going to be cases where you could look at the code and make a change -- if you understand it, you can just be like, oh, I need to change this and it's really easy. And if you've got to express that in English, it's either ambiguous and you're going to go through multiple loops, or sometimes you just get stuck doing weird things in an endless loop and it's easier for you to do it yourself.

**Rebecca Barter:** Although I do kind of wonder, I mean, right now it's like we use the AI to write code, or the AI is writing code under the hood. At some point, is the AI going to get so good that it doesn't really need code? The code is just a tool we use to get from question to answer. Is it going to develop something where it's not really code as we know it? Like it can do the reasoning and figure out stuff, but it's not necessarily writing Python code or R code to answer the question. I don't know. It's this kind of formless thing in my head sometimes. The code is the tool that we created for us, but maybe at some point, for certain types of tasks, the code itself is kind of going to become obsolete. I don't know.

**Hadley Wickham:** Yeah, it's a tricky one. I feel like with arithmetic -- the operation of adding numbers is one a calculator can do, but I almost feel like the code is the representation of the problem. If you're accounting and you're adding up numbers, having those numbers there is to me the code, where the adding is the execution. Still having that representation seems useful, but I guess it's also fair that at a point where you're confident enough, you could just use English and not even have to think about it.

**Wes McKinney:** I mean, the point is the AI is never going to be as reliable as a calculator in the sense that we can prove that a calculator can do addition 100% correctly. AI can never get to that point. It still isn't very good at adding. I think I just wrote a blog post about LLMs struggling to add numbers. They've gotten better, but it's not 100% of the time.

**Rebecca Barter:** Oh yeah. I still feel like when I Google something and it comes up with that AI thing at the top, I just usually scroll straight past it. Because it's just wrong 70% of the time. Or it'll be like, "According to one Reddit user" -- that's your source?

**Michael Chow:** Yeah, it's pretty freaky. I think we're getting pretty long in the tooth, kind of running up at time. But yeah, I really appreciate all of this thought on AI and teaching. And I'll say, I am impressed that you have held onto your accent for pronouncing "data."

**Rebecca Barter:** My accent -- I think at this point it's increasingly American though. Like there's -- I think you still sound like a solid Kiwi, Hadley.

**Hadley Wickham:** I don't say "data." I say -- I don't say "data" anymore. I say "data."

**Michael Chow:** Yeah. But it's "data."

**Rebecca Barter:** I mean, when I was teaching R a lot, and maybe you get the same thing, where I'll just be like "ah" and people are like...

**Hadley Wickham:** Yeah. That's why I say "R" now. It's because Australians and New Zealanders have a non-rhotic "ah" which is the vowel sound.

**Michael Chow:** I like to think that whenever you chat with an Australian or New Zealander, you're clocking their use of "data." You're like, Hadley clearly is on it.

**Hadley Wickham:** Yeah. Just when I'm in America and someone says "data," I'm like, oh, that's not an American.

**Rebecca Barter:** There's some words -- I do put Rs in places now where I don't think they belong, the letter R and the sound "are." But there's certain words that I hold onto with dear life. So for example, I'm not wearing a sweater right now, I'm wearing a jumper. And I will hold onto that for the rest of my life. Even though every time someone's like, "A jumper, isn't that like a jumpsuit?" And I'm like, no.

**Michael Chow:** I love that. I think it's good to keep people on their toes, you know, you gotta have a couple of things.

Rebecca, thanks so much for coming on. I really appreciate all your thoughts on AI and also your role building out tooling. I feel like it's such an interesting role for data scientists to take in orgs. So thank you so much for coming on.

**Rebecca Barter:** Thank you so much for having me. It was good to chat with you all.

**Hadley Wickham:** Yeah. Thanks Rebecca.

**Wes McKinney:** Thank you. Thanks for coming.

*[Podcast outro]*

The Test Set is a production of Posit PBC, an open-source and enterprise tooling data science software company. This episode was produced in collaboration with Creative Studio Adji. For more episodes, visit thetestset.co or find us on your favorite podcast platform.