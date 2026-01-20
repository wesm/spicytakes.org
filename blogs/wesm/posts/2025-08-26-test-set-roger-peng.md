---
title: "Roger Peng: Impact takes time, and it's totally worth it"
summary: "Podcast at The Test Set (Posit)"
date: 2025-08-26T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-roger-peng
word_count: 9641
source_file: transcripts/2025-08-26-test-set-roger-peng.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://www.youtube.com/watch?v=WhpHBDiR10Q"
---

{{< video https://www.youtube.com/watch?v=WhpHBDiR10Q >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, Michael Chow, Hadley Wickham, and I talk with Roger Peng, a professor of statistics and data sciences at UT Austin who has been podcasting for about 10 years with Not So Standard Deviations. Roger shares how he got into R back in 1997 using version 0.65, finding it through the Yahoo directory as a free alternative to S-Plus while working on author identification using discriminant analysis.

We discuss how data science as a field essentially happened to people like Roger and me who happened to combine statistics and programming before the term existed. Roger offers advice to students: try analyzing data before investing in expensive degrees to see if you actually enjoy it. The conversation touches on how academia is set up to discover things rather than develop and maintain them, which creates challenges for software development in that environment.

Roger explains his philosophy on podcasting, emphasizing sustainability over burning bright for a short time. He and his co-host Hillary Parker keep prep minimal and focus on having authentic conversations about what data scientists are actually doing. We also discuss the R versus Python debate, with consensus that we're now "post-language" given tools like Arrow and DuckDB that enable sharing technology between ecosystems. The episode closes with reflections on impact and timescales in open source work. Roger notes that impact often takes years to unfold, but when you see environmental policies change because of your research or meet people whose careers were shaped by your courses, it's deeply rewarding.

## Key Quotes

> "Impact often takes a lot of time to kind of unfold, but it does happen... Things like environmental policies change because of the research that we've done and things like that. And also, you know, some of the online courses that we've built, you know, you have like millions of people who have taken these courses. I've met them in person." — Roger Peng

> "Data science happened to me. I don't feel like I got into data science... I double majored in computer science and statistics, which is a weird combination at the time. Like alchemy." — Roger Peng

> "Academia to this day, I think it's set up to discover things. It's not set up to develop things or maintain them for that matter. And I think, you know, if you think about what a paper is, it's like, you know, you discover a fact, you write a paper about it. You don't have to maintain that fact." — Roger Peng

> "If someone's been doing it for 10 years, they have—it's got to be like a sustainable kind of like manageable approach." — Roger Peng, on longevity in content creation

> "We're post-language." — Roger Peng, quoting Hillary Parker on the R versus Python debate

> "I talked to Hillary last week and she's like, we're post-language. I completely agree with that." — Roger Peng

> "One optimistic view is that it will allow students to focus more on the scientific reasoning and knowing like, you know, what are the right tools to use and like how can I give the best quality feedback to the AI code generator." — Wes McKinney, on AI and the future of data science education

> "The most satisfying thing has been hearing from people all around the world about how their path to discovering Python, learning language, learning how to use pandas and the impact that it's had in their lives." — Wes McKinney

> "Don't get too locked into one path or one vision for your future, but make sure you're taking, you know, there's weird and wacky courses that, you know, maybe sound like something you're not interested in, but might turn out to be that's actually the thing that drives the rest of your career." — Hadley Wickham

> "I very deliberately try to be kind and patient to people regardless of how much they know about the field. And that just feels like over time that's increasingly valuable." — Hadley Wickham

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field.

On this episode, we chat with Roger Peng, author and professor of statistics and data science at the University of Texas at Austin.

**Michael Chow:** I'm Michael Chow. Thanks for joining us. Welcome everyone in the world. This is The Test Set, a podcast where I'm joined by my fabulous co-hosts, Hadley Wickham and Wes McKinney. And today we're here with Roger Peng, a professor at the University of Texas at Austin and prolific course creator, podcaster, and researcher. Roger, do you mind telling us a little bit about yourself?

**Roger Peng:** Sure, yeah. So I'm a professor of statistics and data sciences at UT Austin. I've been there only about three years, actually. I used to be at Johns Hopkins University in the Department of Biostatistics. And like you said, I do a number of things. I do a little bit of research, primarily kind of developing statistical methods for environmental health problems. But then I've also developed a number of online classes, developed two podcasts, and written a couple of books. So yeah, general content creator.

**Michael Chow:** Yeah, awesome. Yeah, and we're so glad you came. We hit Roger up kind of last minute and Roger was like, I'm there, you know, hop in the car, get in the band together. And I think it's super relevant because The Test Set is just, it's a little baby podcast right now. And we're feeling out sort of baby's first steps into podcasting. We've got some really great people and we feel like there's a lot of chance to kind of look at the people behind the data and the landscape. But with you as a kind of like grizzled podcaster, I think you've been doing a podcast for like 10 years?

**Roger Peng:** Something like 10 years. Yeah.

**Michael Chow:** Nice. Not So Standard Deviations. How many episodes?

**Roger Peng:** 186, I think it was.

**Michael Chow:** Wow.

**Roger Peng:** Yeah, I think we're really excited to hear your take on like why podcasts exist and how to make them nice and what to do. But I think maybe to start out, it'd be really interesting to hear maybe some of your background in data too. Like, what was your very first data analysis?

**Roger Peng:** Oh, wow. That's a good question. I have to go back pretty far now. Every year it just gets harder and harder. One of the first data analyses I did, which actually is the reason I started using R actually, was looking at—I was doing like a project in school and looking at different like texts and trying to be able to develop a way to kind of identify who wrote which text, like author identification, using just discriminant analysis, very basic tools. And so there was like some text processing, a little statistical modeling, and yeah, and it was all done in R.

**Michael Chow:** Oh, nice. Yeah. And when was this?

**Roger Peng:** Oh, wow.

**Michael Chow:** Or what stage of life?

**Roger Peng:** Well, I can tell you. It was R version 0.65, something like that.

**Michael Chow:** Okay. Wow.

**Roger Peng:** Yeah. It was like '97.

**Michael Chow:** Two people speak in R stages.

**Roger Peng:** Did you use anything before R?

**Roger Peng:** Well, yeah. So I was like an S-Plus user for sure, yeah. But like S-Plus—I don't know, it was like hundreds of dollars. And I was looking around for a free alternative and in the Yahoo search directory, R came up.

**Michael Chow:** Incredible. Yeah.

**Roger Peng:** Do you mean you're like free alternative to S-Plus?

**Michael Chow:** No. Well, you didn't really search in Yahoo because it was like you click on a link and then you click on another link. It was like a directory kind of thing. You click on it and it was like free software, statistics, something. And then eventually there was like a couple of options.

**Roger Peng:** Yeah. You like went down a series of pipes.

**Michael Chow:** Exactly. Yeah. There was no like searching.

**Hadley Wickham:** Yeah. Wait, that's incredible.

**Roger Peng:** Yeah. Wow.

**Michael Chow:** And do you have any advice you'd give students today trying to get into data science?

**Roger Peng:** Yeah. So I also find that I get that question a lot, as you might imagine. I teach a lot of undergraduate students and they're interested in data science. And it's always a little weird for me because I kind of feel like for me and maybe for you, like data science happened to me. I don't feel like I got into data science.

**Michael Chow:** You mean like it tackled you like on the street?

**Roger Peng:** Yeah. More or less. Yeah. Like I double majored in computer science and statistics, which is a weird combination at the time.

**Michael Chow:** Like alchemy.

**Roger Peng:** Yeah. Yeah. And so I did statistics. I got my PhD in statistics. But I just happened to really enjoy programming. I took a lot of CS courses in college and I just really enjoyed programming. And I think it wasn't immediately clear that that would be useful in getting a PhD in statistics.

So I think, but yeah, so now that data science has happened, people kind of assume, especially the students that I have, they kind of assume it's been around forever. And so it's a little tricky. But I think, I mean, one of the things I generally try to tell them, especially at an early stage, is kind of like make sure that you can have some way to show people what you've done. Like you've analyzed data, that you've been able to ask a question, draw some sort of even basic conclusion from the data you've looked at or from the work you've done. And then kind of go from there. And see if it interests you. If doing that doesn't interest you, then that's a good sign. Then you'll know early.

**Michael Chow:** Yeah. It's really interesting to hear about students, yeah, the value of producing a report to see how it feels for you. And like having something, kind of the whole process to put out for other people.

**Roger Peng:** Yeah. And one of the things that I think is a little different now is that there are like a lot of programs that you can go into and maybe get a certificate or get a degree or something like that. And I'm always a little hesitant, even though I teach in a program, obviously, I'm always a little hesitant to say like, oh yeah, go get a master's or go, you know, because that costs a lot of money. And you don't want to find out you hate doing this, you know.

**Michael Chow:** Right.

**Roger Peng:** So at least, but now, you know, it's pretty easy to get data. You know, there's a lot of data around. There's a lot of things that you could try. And I think if you could try it and find out that you enjoy doing it, then it's maybe worth investing a little bit more.

**Michael Chow:** Yeah. That's fair. It's interesting to hear, too, like where you two mentioned like getting basically like data science. I think you said that came to you like where you did like stats and computer science and that kind of like added up to or somewhere in that space. You hit data science that like you—there was less, I guess, like sampling, like trying out a report and where students today kind of have this actual program and can kind of quickly figure out like, is it for me?

**Wes McKinney:** I mean, even the—I mean, even the term like the field of data sciences, I think as recently as 15 years ago, that term didn't really exist. It was almost like a marketing term to describe doing statistical computing or data analysis in a business setting. So like some combination of like programming and data and data analysis combined with reporting and communication and then combining that with combining that with domain knowledge about some business domain, you know, the famous Drew Conway Venn diagram.

And then suddenly, you know, it became so popular. And also there was this big shift toward open source. And then every university needs to have a data science program because students are arriving and they're like, well, I want to learn how to do data science because that's where the job opportunity is. Like there's a great need for more data scientists in this industry.

And so it seems like universities had to respond by, you know, reorganizing themselves to create these cross-disciplinary data science programs to pull together statistics, computer science and maybe political science and economics and other fields that crossover into where—because you have statisticians that live in all these different departments, but they do statistics within these domain-specific settings. But there's a lot to be gained from making all of those different research specialties accessible to undergrads and master's students and PhD students who are building skills in that area.

**Roger Peng:** Yeah, I think it's been interesting to see just kind of how that has evolved at various universities. Because there are like, like I said, there's lots of people analyzing data all across different areas. And they're in different departments usually because they're looking at different kinds of data like psychology or, you know, economics or whatever.

And so it's a little bit of a challenge because then you've got to put everyone together. You have to think about like, well, what is the unifying principle? What is the generalizing kind of thing? And I think a lot of times it's software, you know, so it's like, you know, there's lots of different places that you can analyze different kinds of data. But like, you know, in other areas might be like theorems or whatever laws, you know. But I think in data science, a lot of the unifying thing is software. You know, we can use a piece of software for so many different things. You know, that's the generalizing kind of element.

**Michael Chow:** Yeah, that's an interesting...

**Wes McKinney:** So do you think there's like more respect in academia for like developing software now compared to like 10 years ago or 12 years ago when I left?

**Roger Peng:** Yes, I think, yes, compared to 10 years ago, there definitely... Whether that's enough, I don't know. But there's definitely more, I would say, than, you know, back compared to back when you were there.

One of the challenges, I think, with academia and software is that, you know, academia to this day, I think it's set up to discover things. It's not set up to develop things or maintain them for that matter. And I think, you know, if you think about what a paper is, it's like, you know, you discover a fact, you write a paper about it. You don't have to maintain that fact, right? I mean, for the most part. And so you can just let it go and then move on to the next one. And it's not how software works, obviously. And so it is a challenge in that environment, I think.

**Michael Chow:** It's kind of interesting to think, though, that like maybe more papers, like if you had more of a maintenance approach to papers, like maybe there'd be like less of a reproducibility crisis. You can like update.

**Roger Peng:** Yeah. Or if you were like allowed to go back to it.

**Michael Chow:** Yeah. And check it out. Like, oh, actually, we're kind of like not so sure about this.

**Roger Peng:** Yeah. Yeah. Yeah.

**Michael Chow:** I'm super curious—we're kind of kicking off a podcast now about data and data science. And you have like 10 years of doing kind of podcasts. And then earlier than that, like Coursera courses. I'd be really curious to hear from you, like what do you think is like the secret of a great podcast?

**Roger Peng:** If I knew that, I'd have one. I think it's pretty baller, you know? I don't know for sure. I don't know. And I think that question can be asked from two perspectives. One's from the audience and one is from the actual like podcaster, right?

**Michael Chow:** Yeah. Like who's it for, I guess.

**Roger Peng:** Yeah. And also like, you know, what are your goals at developing the podcast? Do you want it to be something, you know, from my perspective, I want it to be something that, you know, I have a job, I have all these things that I'm working on, had to be kind of easy to do, fun to do, but still kind of have some sort of useful product at the end of the day.

And so it's, you know, it's very minimal setup, you know, just recording over the internet. And so, and, you know, not too much prep. You know, the other end of the spectrum, you got like these narrative podcasts where everything's scripted and everything, you know, and that's a super expensive way to do things, but you get a really amazing product at the end of the day.

And so, and so then everything else is kind of in between, I think. My personal, like personally, I like listening to conversations between people that are like kind of deep and kind of involved and where there's like a relationship there and kind of people can just take time to move into like more than just scratch the surface. But that's just my personal thing. And that's kind of how I modeled the two podcasts that I, you know, that I built.

**Michael Chow:** Yeah. That's really interesting. I mean, for some context. So yeah, I think we mentioned like Not So Standard Deviations. So you've gone 10 years and you have over 180 episodes. How did that kick off? Like what led to Not So Standard Deviations?

**Roger Peng:** Yeah. So, I mean, I think I had listened to—I've been listening to podcasts, I mean, probably since the early 2000, you know? Yeah. So like when they first came out and I've always enjoyed—most of those podcasts were like tech podcasts for the most part, you know?

And I think I always felt like there—at the time, which is like 2015, I didn't feel like there were too many podcasts where you just—a couple of data scientists just talking about stuff they're doing. Just very informal, very just kind of casual. And there were a couple of things where like, you know, a lot of podcasts were like, you know, this tonight—or today we're going to talk about linear regression and tomorrow we're going to talk about random forests or different techniques and different software packages. Yeah. There were more like, for lack of a better word, instructional.

And I think I wanted to just have like, imagine just like a hallway conversation between two data scientists. Some place, you know? And that's kind of like how I wanted to feel, whether I achieved it, I don't know.

**Michael Chow:** Yeah. I think it really shines through like the responses to things and like what people are up to and getting takes. It's like your co-host, Hillary Parker. Like I do feel like my take, and this might be wrong, it's like 70% Hillary's going, you know?

**Roger Peng:** Yeah. What's latest views.

**Michael Chow:** Yeah. Hot takes.

**Roger Peng:** Yeah. And then you're like, yeah, yeah.

**Michael Chow:** You're like, maybe.

**Roger Peng:** Yeah. Complicated. Yeah. It's been a little work for me, I would say.

**Michael Chow:** Yeah. One of the things that's actually been quite interesting, I think, is that she's changed jobs a couple of times, you know, which I think is the norm in the data science industry. And so we've been able to like kind of take a little tour of like what the different kinds of things that can happen in different companies and—

**Michael Chow:** Oh, cool. Yeah. In the data science world.

**Roger Peng:** Oh, nice.

**Michael Chow:** Yeah. And did you approach her? Did she approach you about the podcast? How did you—

**Roger Peng:** I approached her.

**Michael Chow:** Okay. Yeah.

**Roger Peng:** So our connection, she graduated from the PhD program at Johns Hopkins. And then we kind of lost touch for a number of years. And then I think we reconnected at like one of these rOpenSci kind of unconference.

**Michael Chow:** Yeah, yeah, yeah.

**Roger Peng:** I think it was in the GitHub headquarters.

**Michael Chow:** Yeah. Yeah. And so I just kind of—we were chatting at that time and I kind of just proposed the idea.

**Roger Peng:** Oh, cool.

**Michael Chow:** And is it—

**Roger Peng:** Two years later.

**Michael Chow:** Yeah, exactly. Just cooking.

**Roger Peng:** Yeah. Do you, are you like keeping a log of topics? Like how are you hitting stuff? Or are you texting latest news?

**Roger Peng:** There's a little bit of that, a little bit of the latest news. There's a little bit of like, let's maybe take a topic and just kind of go deep that we choose on our own. We've had a couple episodes where we read certain books or something like that.

And so, but it's a, yeah, I mean, I try to keep it—for better for worse—I keep the prep to a minimum just because I've got—I don't want it to take over my life. But usually, especially nowadays, there's always stuff happening in the news and, you know, whatever.

**Wes McKinney:** I mean, there is an interesting tension between like, you know, kind of burning brightly for a short amount of time versus like that sustained, like if you want to do something for like decades, then you can't like kill yourself putting together every episode. Like it's got to be sustainable.

**Roger Peng:** Yeah. Yeah. So, and I think that's true for so many things. Like you look at blogging, you look at YouTube, you know, YouTubing or whatever, anything like if someone's been doing it for 10 years, they have—it's got to be like a sustainable kind of like manageable approach.

**Michael Chow:** Yeah. That's a good point. I mean, it's interesting parallel too between the like papers versus software. It's like big that you kind of like go and publish and then like drop the mic.

**Roger Peng:** Right.

**Michael Chow:** Versus software where you're like chipping away for—

**Roger Peng:** Only if people are using it. Yeah.

**Michael Chow:** Yeah. Chipping away where you like quietly disappear and kind of like close the door.

**Roger Peng:** Yeah.

**Wes McKinney:** Yeah. I mean, how do you—how do you think your listener community has shaped the podcast? Like, you know, positive feedback, negative feedback. And like, I find that, you know, from having, you know, worked in data science tools for the better part of two decades, like fads come and go. There's like always like the things that are in, you know, really hyped and everyone talks about and wants to hear your opinions on. So there must be a little bit of like, you know, talking about the things you want to talk about, the stuff that's interesting, but then also maybe hitting on some of the, you know, flavors of the week or flavors of the month that are—

**Roger Peng:** Right.

**Wes McKinney:** Like on everybody's mind.

**Roger Peng:** Yeah. Yeah. I think you have to—there's got to be some blend of that. We don't have really any data on our audience. We don't really collect any data, which I think is good for the most part.

And I think, but my suspicion is just from the feedback that we get is that it has kind of like turned over a little bit, you know, over the last 10 years. And so it's not like there are maybe some people who are still listening from 10 years ago, but probably not that many. And I think, because I think we try to—it's pretty, maybe a little bit more attractive to somebody who's like starting out just to kind of hear this kind of stuff.

But yeah, so we do have—there is an element of like keeping up with the latest things, even if I don't use them and just kind of understanding how they work and what they do.

**Michael Chow:** Yeah. Do you feel like it's more—yeah, is the podcast more for you or more for the audience?

**Roger Peng:** That's a good question. Yeah. A little of both. I mean, I would—I mean, I like, I think doing it for us has been really helpful just to think through ideas and, yeah, actually some of the stuff that we've talked about have, you know, over time turned into papers, for example.

**Michael Chow:** Yeah. Yeah. It's almost like—I mean, it almost strikes me as like pair programming, like you spent 180 hours, like, or episodes, which are like almost an hour just like working through something with a person. It's like, yeah. Kind of interesting. You're like pairing on the topics of the day.

**Roger Peng:** Yeah. Yeah.

**Michael Chow:** Did you say you—your, how you got started with the podcast with Hillary is you kind of ran into her at a conference?

**Roger Peng:** Yeah. Yeah. Yeah.

**Michael Chow:** Nice. I think it might be good to loop back to how y'all know each other and like the places y'all know each other from. Is it conferences? Is it like cryptic R mailing lists?

**Hadley Wickham:** Yeah. Where did we?

**Wes McKinney:** I think it might be something along those lines. Yeah. Yeah. Yeah. I think there—I think I might've responded to one of your early R like mailing lists posts. And then—

**Hadley Wickham:** Yeah.

**Wes McKinney:** And then also in academia there's kind of like a network of, you know, it's a pretty small world in statistics. You kind of see—

**Hadley Wickham:** You hear about people.

**Wes McKinney:** Yeah. Yeah.

**Michael Chow:** Nice. I'd actually never met Roger before today.

**Roger Peng:** Yeah. Yeah.

**Wes McKinney:** I mean I was in statistics. Like I was a PhD student at Duke before I dropped out to, you know, work on, work more on pandas and do entrepreneurial things. But I had met—I had met Hadley in early pandas days. And he invited me to give a talk at Rice statistics, which I think was maybe 13 or 14 years ago. Something like that.

**Hadley Wickham:** Yeah. That's wild. That's way, way back.

**Roger Peng:** Yeah. I mean, I've known about Wes forever, you know, but I just, yeah, it's nice to be able to finally meet up.

**Michael Chow:** Yeah. Yeah. Where are like the places that a lot of the kind of like development and the conversations happen? Like how much of it's happening at like conferences or other places?

**Wes McKinney:** I mean, there's a surprising amount of things that come out of conferences and like the hallway, you know, the hallway track. And you know, you maybe there's something you're thinking about and just when you're together with like birds of a feather, they have these, you know, birds of a feather want to talk about, I don't know, data visualization or data frames or, you know, data access and different things.

And, you know, you'd be surprised how many times that just like a casual conversation turns into like, hey, we should do something together. We should start something. And so like, I know like, you know, Hadley—you know, Hadley and I created a file format called Feather based on just like Hadley was visiting. And I said, hey, I'm thinking about this new thing called Arrow. It's like, why not? How hard could it be?

**Hadley Wickham:** Yeah. Yeah.

**Wes McKinney:** But that was also like, I think, especially during COVID, like we really—I think we all realized like how difficult it was to be deprived of having those serendipitous in-person reactions with people at conferences and meetups and things, because all of a sudden, you know, you have to go out of your way to like, you know, that bumping into somebody at a statistics conference or at a data science conference, like suddenly those interactions are not happening.

And so, but yeah, so for me, at least like that's been a rich source of like inspiration and new ideas and new collaborations.

**Michael Chow:** How often is it like a friendly collab conversation? Like, oh, I love your work versus like strong opinion. Hey, I got a bone to pick, you know, like, ooh, we got to get this package sorted out.

**Hadley Wickham:** People are almost always pretty friendly in person. Like I've got a bone to pick things. It's like email. We're all hiding behind masks.

**Roger Peng:** Yeah. I mean, or at least in my experience, if it does, if it is like that, it's for like five seconds and then it's like, okay, let's just have a conversation about whatever, you know? And then you can often sort it out, I think.

**Michael Chow:** I do feel like that's going to remind me that in-person conferences are kind of like a nice balm sometimes where like, yeah, you might interact with someone online and they seem like kind of intense or mad, but like getting in person does feel like it kind of like—

**Roger Peng:** Yeah. But I guess there's still like the—especially like academic conferences, like the questions at the end of your talk. It can be like, sometimes they're like pointed or they're like, this isn't actually a question. I'm just going to talk about what I'm working on.

**Hadley Wickham:** Right. Exactly.

**Roger Peng:** Yeah. Like a one-upmanship and yeah.

**Michael Chow:** Yeah. That is an important point that I guess I wasn't thinking of academic conferences at all where I do think the intensity lingers on even after the talk sometimes.

**Roger Peng:** Yeah. But there is still that hallway element, you know, like I think conferences are useful if you've got like ideas kind of cooking in your head for a while and then you see someone who like, oh, you know, mentions the same idea. Then you see a little validation, like, oh, maybe there's something to this, you know?

**Hadley Wickham:** Yeah. I do think there's like something about travel as well that just kind of knocks you out of your day-to-day routine and makes you think about—and then like a bunch of new ideas and even if you're not really necessarily paying attention to like all the talks you're in, but there's just like something about like jolting you out of your local minima of thinking.

**Roger Peng:** Yeah. Or like plane coding. Do you like coding on the plane speed run? Like I have X hours. Will I complete this package in time?

**Hadley Wickham:** I don't know. It's like so dependent. Like, I don't know. It's very difficult for me to program without good internet now.

**Roger Peng:** Yeah.

**Hadley Wickham:** And I feel like planes, it's often like the maximally worst internet where if it's like any worse, you'll just give up. But you're just on that cusp of like, oh, I'm like—for like four hours you're like struggling.

**Wes McKinney:** Yeah. We've got to put you on a train, like an Amtrak. So you have like 30 hours with internet, but you're still trapped.

**Hadley Wickham:** Yeah.

**Wes McKinney:** I've definitely had my fair share of productive plane hacking sessions, but you know, it's funny now, like so much of development is, as Hadley said, has become internet dependent. And of course, like none of your nice AI auto-completion and tools and whatnot, you know, work well. You know, if there's certainly—if there's no internet or if there's bad internet, then it just ends up being a bit frustrating.

Like I, you know, make sure, like make sure that I've pulled from—like, I'd git pulled before getting on the plane. I've definitely forgotten to do that.

**Hadley Wickham:** Like, make sure I build and like download all the dependencies.

**Roger Peng:** And like load up like seven tabs of the issues you want to work on.

**Hadley Wickham:** Yeah. I do that. I do like that. Like stashing away, getting ready for the plane.

**Michael Chow:** Since we have you all here, I thought this was the perfect time to broach the podcast question. R versus Python.

**Hadley Wickham:** Is this the only time we should ask this question?

**Michael Chow:** Yeah. I don't know if it's fair, but we'll see.

**Roger Peng:** I don't know. Like I was talking to Hillary last week and she's like, we're post-language.

**Hadley Wickham:** We're post-language. I completely agree with that.

**Wes McKinney:** Yeah. And I think Hadley and I have like kind of been on the same page about that for a long time. Just like that the language wars are not productive or at least like, I think we've reached a point where, you know, we've established a basis of like, there are certain things that we figured out how to share technology between the Python and R world.

Like we built Arrow and like that was like a many year endeavor. And now there's DuckDB and you can use that. And you know, of course now like so many—we're using all these services that live in the cloud. And so, you know, we can use those portably.

But it's also interesting because I think like Python and R, like at one point it seemed like they were in direct competition with each other. Maybe like, you know, the early 2010s, like Python started to become popular in a business setting for doing data analysis and some data science type work. There were some new open source projects for doing statistics and some of the work that you would do in R. You had some data visualization—still not as good as R, even today still not as good as R, I would argue.

But I feel like at some point, maybe in the mid-2010s and like certainly, you know, more recent times, like Python world has diverged a lot more into like analytics engineering, data engineering, AI engineering, you know, machine learning engineering.

And so in a sense, like it feels like where Python was in terms of like statistical computing and data analysis hasn't evolved that much. Where like I still wouldn't—if you're doing, you know, coming from SAS or SPSS or like a commercial statistics language, like R is the—if you want to be open source, like R is the thing to use. I think R is the thing to use regardless for that, you know, for that type of work. But certainly in open source.

Whereas the Python ecosystem has, you know, gone in kind of a different direction. And it certainly has become like, you know, the scripting and automation language of AI.

**Hadley Wickham:** Yeah. For like the conference that Wes and I were at last week, the language that everyone was talking about was SQL.

**Roger Peng:** Oh, interesting. Okay.

**Hadley Wickham:** Like that was like by far and away, more people talking about SQL.

**Wes McKinney:** Yeah. Like SQL seems to be having like a resurgence right now over the last few years.

**Michael Chow:** Like we're asking R versus Python and SQL is laughing.

**Hadley Wickham:** Yeah, like 40 years later. It's like, it's my time.

**Michael Chow:** Do you feel like it's—do you think that SQL is seeing a surge of popularity or it was like already there and we're just sort of like—

**Hadley Wickham:** Noticing it now.

**Michael Chow:** Noticing it.

**Hadley Wickham:** Yeah. I mean, I think it's just been like steadily—

**Wes McKinney:** Yeah. It's just like this layer that underpins all data activities is like SQL is there.

**Hadley Wickham:** Yeah. And my feeling is like, it always will be there. Like a hundred years' time, people will still be running SQL.

**Wes McKinney:** Right. We're stuck with it like forever.

**Hadley Wickham:** Yeah. Yeah.

**Michael Chow:** That's fair. Any advice? I know we asked Roger advice to students. Maybe it's a good time to also turn it to you too.

**Hadley Wickham:** I don't know how. I'd like to hear it to be honest. All right.

**Michael Chow:** Any advice to students learning data science today?

**Hadley Wickham:** I have to say it was really interesting. Like I think Roger's advice was mostly like learn if you actually want to do data science, which like thinking about like, yeah, like when you're a student, like you've got no idea about what is actually appealing to you.

So I think there's like two—like part of it is like finding out like what really resonates with you. And part of it is the sort of like optionality, like making sure you're trying to keep your options open so that you can, you know, get a job and decent money and still consider, you know, still be able to find out like, what is it that you really care about?

So I don't know, to me it's about like, don't get too locked into one path or one vision for your future, but make sure you're taking, you know, there's weird and wacky courses that, you know, maybe sound like something you're not interested in, but might turn out to be—that's actually the thing that drives the rest of your career.

**Roger Peng:** Yeah. That's a good point about kind of discovery and feeling it out.

**Wes McKinney:** I mean, I have to—I mean, I have to think that now that if you were, you know, 17, 18 years old and undergrad entering and wanting to become a data scientist, that the path now is probably, you know, radically different, not just like what it's like to, you know, go from not knowing R, not knowing Python to—you know, it's like, what does it mean to now master a programming language in the age of LLMs where in a sense, like you want the AI tools to help you automate away a lot of the boring stuff.

Like you would have to learn all of this boilerplate and, you know, stuff that frankly was getting in the way and the higher level thinking, like actually thinking about the data, actually asking questions and engaging in more of the scientific reasoning process. And so you would have to learn how to program and learn the mechanics of writing code and all of the package management and environment management and the nuts and bolts of doing that.

And so now we can rely on AI autocomplete and LLMs and agents and all those things to write a lot of that boilerplate for us. So one optimistic view is that it will allow students to focus more on the scientific reasoning and knowing like, you know, what are the right tools to use and how can I give the best quality feedback to the AI code generator.

If you don't know which models to use and like I guess you can—there will be certainly a lot of data scientists who are just letting, going full vibe coding, letting the LLM, you know, do all the work. And they look at it, they get a nice PDF document or a markdown document at the end and they're like, it looks good. It looks good, send to boss.

But I think that it's still going to be important for data science. Like there needs to be a human in the loop to be able to judge the output to say like, is the LLM doing the right thing? Does this analysis make sense? Is it asking the right questions? Do we need to ask more questions?

And so I think, I have a more optimistic view that, you know, it's not like AI is going to eliminate the need for data scientists, but it is going to—I think it's going to require people to get better at the actual data science and maybe developing advanced programming skills I think is going to become less, you know, maybe on a relative basis less important.

**Roger Peng:** Yeah. That's actually my hope. I don't think we're quite there yet. We're kind of in a weird in-between stage I think right now, but I think what you said highlights—I think there's aspects about doing data analysis and looking at data that are difficult to really kind of quantify or really understand. So it's like, it will really highlight that we don't—there's a lot of things that we don't know yet.

Because the easy stuff, which is really—or so to speak, the programming, you know, if that's all taken away and we don't have to do that anymore, then we have to actually think about data and that can be hard.

**Hadley Wickham:** Yeah. I have to say I'm sort of—I don't know, I'm optimistic about this idea that human plus AI can do better than either alone. But I would still say if I was a student today, I'd also be making sure there's something I can do that AI cannot. Something with my hands, like just have a backup plan.

**Roger Peng:** Something like manual dexterity as job insurance.

**Hadley Wickham:** Yeah. Or like human to human interaction. It just feels like I'd be like, just to make sure you've got a backup plan.

**Wes McKinney:** Yeah. That's a good point. Make sure you can shoot a gun.

**Hadley Wickham:** Drill game. Yeah.

**Wes McKinney:** Stock up on tacit knowledge. That's what they say.

**Hadley Wickham:** Yeah. Grow vegetables.

**Michael Chow:** Yeah. There's somewhere 10 years down the road, someone's going to say, when did you become such a good hunter farmer in this barren strip of some state? And they'll be like, oh, I watched this podcast.

**Wes McKinney:** Well, you know, like the Jedi meme, it's like, you know, a person of your skills, you know, why be a farmer? It's a simple life.

**Hadley Wickham:** Yeah. Geez.

**Michael Chow:** Are there any communities like in data science or kind of around the ecosystem that you're most curious about?

**Wes McKinney:** Just to inject one, I'd say like DBT, I think is a really interesting, like wherever SQL people live, I find is a really interesting—

**Hadley Wickham:** Yeah. We were just talking about SQL.

**Wes McKinney:** Well, I think it's interesting that, you know, I guess the emergence of like Python is the mainstream business computing and data orchestration and automation language has brought a lot of work that was taking place in proprietary tools and by like, you know, stodgy database administration tools has brought all of that into the land of open source.

And so DBT is taking on the role of like, you know, enterprise ETL, which used to be done with like, you know, all these products that people bought that were really expensive. And people still had to build—30 years ago, people were still building data warehouses and they had much smaller data sets. There wasn't, you know, what we now think of as big data, but they still had to design schemas and architect the data warehouse. And people would spend their whole careers just like architecting Oracle databases, like designing things for performance.

So like that work has always existed, but now there's like, you know, hype—you know, sort of really hyped up open source projects that everybody's scrambling to learn because new companies are being founded all the time and they need to say, okay, what's my analytics stack? Like what's my—how do I go from collecting data out of my mobile application or my website to like, I have a data warehouse where I can run a SQL query and build a dashboard.

And DBT has become like one of the sort of mainstream technologies to make all that work. You need a lot of other pieces, of course, in the pipeline, but as far as like the semantic layer of like, how do you describe what's going on? Like what queries are being run to generate the final product?

I've never actually used DBT directly, so I will admit that, but I've been following its trajectory and I think it's definitely very interesting. It's not data science. It's like analytics engineering or data engineering, but because it's adjacent to our space, like it creeps up and it's not uncommon for people doing data science to incidentally say, oh gosh, like I have to learn how to do DBT because like I don't have the data that I need. And in order to have the data that I need reliably for my data science application, I need to set up some DBT workflows or pipelines so that I can deliver this data science application.

**Michael Chow:** Yeah, that's a good point. It is an interesting case too, like the R versus Python situation and the like, what is data science and the kind of role that DBT has carved out with analytics engineers. Like I know they, one infamous talk, which I think is pretty tongue in cheek, like down with data science. It's an interesting kind of comparison there too, like analytics engineering versus data science is kind of like roles in the ecosystem.

**Hadley Wickham:** I think that—I feel like that's really changed a lot over the course—like when I started doing data science, like you were the data engineer. Like the data would be in like, oh, here's like 100 CSV files in this directory and here's a random API, here's a SQL database. Like your first job as a data scientist is just to get the data into a usable form for you.

And I think that's no longer so much the case. There's still challenges, but that's much less of a challenge now than it was 10 years ago, which I feel like a little sad about because that's like part of the job that I love doing, like collecting data sets and organizing them.

**Michael Chow:** Yeah.

**Roger Peng:** Yeah. So Roger, do you see much interest in like analytics engineering or do you see it show up much with students?

**Roger Peng:** I'm not 100% clear that they necessarily are exposed to that kind of work or that they necessarily would be aware that it exists. I think, but I think, so but I think as we talk and we teach them data science and they get to understand like what are the different components that are involved and how do you get data from A to B so that you can analyze it. Eventually, I think they get an understanding of why you need something like that.

**Michael Chow:** Yeah. Yeah, that's fair. I mean, there's probably like a fair amount of—I hesitate to call it bait and switch, but like students are getting recruited into these data science type roles and then finding that the actual work that they're doing is a lot of—they're maybe doing a lot more ETL and SQL and data engineering than they expected.

**Wes McKinney:** I know that that certainly happened to me. Like I got a degree in pure math, like this is before I did statistics, but I was working for a quantitative hedge fund and I got so excited. Like, gosh, I'm going to be doing modeling and like working out equations and like applying math in the real world.

And, you know, I sit down the first day, it's like, okay, here you go. Here's SQL Server Management Studio. Microsoft SQL Server's over here. A lot of the work was like data quality, like data cleaning, data—like really, but it's, you know, quality, like having good quality data as inputs to your data analysis process is essential.

So I think there was an initial shock of like, gosh, like I'm spending all my time like, you know, monkeying with stored procedures and looking at Excel data quality reports. But then, you know, if you don't have that, it's like a little bit like if you haven't got your health, you haven't got anything.

**Roger Peng:** There's a little bit of that, I think, everywhere. Like in academia, I think it's just kind of the same thing. They think they're going to be doing all these great scientific theories and then at the end of the day, it's like you're merging CSV files and you're going through Excel spreadsheets or something like that.

**Hadley Wickham:** I think a lot of that too is like, you know, to be useful, like you have to not be too constrained by what you already know how to do. You have to look, you know, when you're faced with a new problem, be like, well, what's—where's the value? Like what do I need to learn in order to be good at this? Rather than thinking like these are the six things I know, like how do I apply them to this situation?

**Michael Chow:** Yeah. Yeah. I think one more question for you all. What do you think has been most impactful from your work? And yeah, what excites you most about data science?

**Roger Peng:** Now that it's actually in many ways a lot easier now that I've been doing this for quite a long time, like 20, 25 years-ish. And I can see—like one thing I can see is that impact often takes a lot of time to kind of unfold, but it does happen.

And so I think it's easier for me to justify to myself, like why am I doing this? Because I have seen some impact. Things like environmental policies change because of the research that we've done and things like that. And also, you know, some of the online courses that we've built, you know, you have like millions of people who have taken these courses. I've met them in person.

**Michael Chow:** Oh, cool.

**Roger Peng:** And they've gone into data science or whatever. So that—but that takes a huge amount of time. That doesn't happen tomorrow or overnight. It takes a long time for it to unfold, but then it does happen and it's really rewarding.

**Michael Chow:** Yeah. It seems incredible having a long kind of time horizon to really let that stuff grow and appreciate.

**Roger Peng:** Yeah. I think it's hard to do when you're starting out. You kind of have to just believe that's going to work.

**Michael Chow:** Yeah. That's really neat.

**Michael Chow:** Wes, any thoughts?

**Wes McKinney:** I mean, I've really enjoyed just expanding access to technology, like to open source technology. So building open source projects and then creating technical communication. Whether, you know, like I wrote a Python book. I haven't written as many books as Hadley has, but Hadley enjoys writing more books more than I do, it seems.

But, you know, so having—you know, now it's been, I think Python for Data Analysis came out 13 years ago and pandas has been around for a few more years than that. And so, you know, I think for me the most satisfying thing has been hearing from people all around the world about how their path to discovering Python, learning language, learning how to use pandas and the impact that it's had in their lives.

And so, you know, hearing from people in like really humble circumstances about how they were able to learn these tools and it got them their first job or it was really essential to the way that they work.

In the past, a lot of computing technology was hidden behind a paywall, essentially. So you had to buy a license to a piece of software. And for many people that was a practical barrier to learning and to being able to use those tools.

And so I think having free software available, anybody with an internet connection and now computers have gotten a lot more capable. And so people all around the world can use these tools to empower themselves and change their lives.

And I also find that building these open source communities around them and building communities that eventually run themselves so that you can step away and think about what's next, I think has been really satisfying too. And I like seeing people more productive. And so seeing that has been pretty exciting.

**Michael Chow:** Yeah. It's really incredible. I mean, I think you mentioned too before, I think pandas, you said is 17 years old?

**Wes McKinney:** 2008. Yeah. Yeah.

**Michael Chow:** Wow. Okay. So yeah, it's powerful to hear both of you talk about sort of this timescale, you know, where I'd imagine a lot of people cobbling a tool today are not thinking about like 17 years from now. It's really—

**Wes McKinney:** I mean, I think I always was just thinking about tomorrow, like I want it to be better tomorrow. And so, you know, thinking about years from now, I mean, of course, people find it useful and they use it and that's great.

But yeah, often the motivation is the problems that are right in front of you and the things that you see are not good now. And that like if you perceive that you have the ability to—whether it's writing something that helps people learn or making the software better and solving a problem that's annoying you, then it's really satisfying to see that through and to put it and get it in people's hands.

**Michael Chow:** Yeah. Yeah. Thanks.

**Hadley Wickham:** Yeah. I mean, I do think that is like one of the positive things about academia. It's like that more of that long-term timescale. Like things don't have to—you know, like you don't have a deadline on next Friday to get this done. That things can take like months or years to do.

It does feel like that. Like, yeah, like the impact you have, it just takes like a long time to build up and to really know what the things you do—like what were the things, what were the actually impactful things that you did?

And I had a few conversations again at this conference we went to last week. Like I kind of like to think it's my code that's most impactful. But, you know, like I talked to a lot of people that, you know, that maybe they used R and then enjoyed using ggplot2 or the tidyverse. But like what stuck with them was the underlying ideas or some of them—like I was just kind to people when they talked to me like 10 years ago. And like, oh, you know, I still remember that.

And that just feels like—it just kind of reaffirmed to me like, you know, that I had made this deliberate choice. Like I had had some negative role models of like, you know, people higher up in their fields who were like did not—I did not have a good experience with. And I very deliberately try to be kind and patient to people regardless of how much they know about the field. And that just feels like over time that's increasingly valuable.

**Michael Chow:** Yeah. Yeah. It's really impactful. It's really amazing to hear it circle back like 10 years later that somebody might still be kind of carrying that and thinking about that.

**Hadley Wickham:** Yeah. And it's also like scary when you think like, oh, you know, I've had a bad day and I get a bad interaction with someone and I don't even remember that like 10 years later, like when Hadley said something really mean to me. Like you don't—you don't hear the people who are like, I'm leaving data science because of Hadley. Like I never hear from those people.

**Michael Chow:** Yeah.

**Michael Chow:** Well, thanks. Yeah. Thanks everybody so much for coming on. I mean, you two are part of the podcast. So thanks me. I don't know. Definitely. Thanks, Roger. A hundred percent.

**Wes McKinney:** Thank you, Roger.

**Roger Peng:** But no, it's been—it's been so helpful, I think, and incredible just hearing about the field of data science and, you know, your interactions with open source over the years and how that timescale can be really long. And I do think that's one really neat thing about this podcast is the opportunity to hear kind of some of these long term projects or like the histories that brought people to where they are. And so just really appreciate you being here and taking the time to come down.

*[Podcast outro]*

The Test Set is a production of Posit PBC, an open-source and enterprise tooling data science software company. This episode was produced in collaboration with Agi. For more episodes, visit thetestset.co or find us on your favorite podcast platform.