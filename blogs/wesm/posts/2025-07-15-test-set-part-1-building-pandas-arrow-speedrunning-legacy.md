---
title: "Building pandas, Arrow, and a Speedrunning Legacy"
summary: "Podcast at The Test Set (Posit)"
date: 2025-07-15T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-part-1-building-pandas-arrow-speedrunning-legacy
word_count: 4400
source_file: transcripts/2025-07-15-test-set-part-1-building-pandas-arrow-speedrunning-legacy.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://posit.co/thetestset/episode/wes-mckinney-part-1-building-pandas-arrow-and-a-speedrunning-legacy/"
---

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, host Michael Chow interviews Wes McKinney about his journey from GoldenEye 007 speedrunning to creating pandas and Apache Arrow.

### Early Community Building: Speedrunning

Before open source, Wes cut his teeth on community development through an unlikely venue: the GoldenEye 007 speedrunning community in the late 1990s. He took over stewardship of the community, learning about governance, decision-making processes, and building systems for verifying records. "That was my first exposure to community development," he notes, and those behaviors proved familiar when he later entered open source.

### Creating pandas

Wes started building pandas in 2008 at AQR, a quant hedge fund, initially as a tool to make himself more productive. Influenced by R circa 2008 (before the tidyverse existed), he found working with data in Python frustrating and set out to fix it. After getting permission to open source the project in 2009, pandas grew slowly until 2011-2012 when Wes dropped out of his statistics PhD to work on it full-time. He wrote "Python for Data Analysis" in 2012 and recruited colleagues from AQR to join him.

### Handing Off pandas

By early 2013, Jeff Reback and Philip Cloud had stepped up as major contributors. Wes felt comfortable handing the project to them, crediting the community for growing pandas from 10-20 contributors to thousands. "I helped seed the project... but going from 10 or 20 contributors to 2,000, I really have to give them the credit."

### Apache Arrow and Ibis

At Cloudera, Wes and colleagues started Apache Arrow, now entering its 10th year. Arrow focused on building a better computational foundation for data science—portable, interoperable data frames and file formats. Around the same time, Ibis emerged as a Python project bridging pandas-style data frame concepts with SQL databases. Ibis acts as a query transpiler: you express data frame operations in Python and it generates SQL for BigQuery, PostgreSQL, DuckDB, or other backends.

### Philip Cloud and Long-term Collaboration

Philip Cloud, one of the first major pandas contributors, later joined Ibis development. When Wes founded Voltron Data, Philip was "basically the first person I called" to lead the Ibis team. Their collaboration spans nearly 14 years—a testament to the value of finding the right people to work with in open source.

### Speedrunning Meets Data Science

Wes reflects that his speedrunning mindset—optimizing efficiency and thinking about how to do things better—translated directly to building data tools. "It frustrates me that doing this task related to data processing is tedious or inefficient. And so I want to find a way to make it more efficient."

---

## Key Quotes

> "That was my first exposure to community development and building that speedrunning community. In a sense, when I later got involved in open source development, some of those behaviors were familiar to me." — Wes McKinney

> "It frustrates me that doing this task related to data processing or related to data science is tedious or inefficient. And so I want to find a way to make it fit my brain better or make it more efficient." — Wes McKinney

> "In a sense, you're like speedrunning—I guess it's just a personality trait of trying to speedrun the data science workflow a little bit." — Wes McKinney

> "I think I helped seed the project with developing it the first five years and getting that first critical mass of contributors. But going from 10 or 20 contributors to pandas to 2,000, I really have to give them the credit." — Wes McKinney

> "By really casting a wide net and making the tent bigger to invite as many people from all around the world to make contributions to the project, both big and small... all are welcome, come here, work on this project and make it better." — Wes McKinney

> "Philip was basically the first person I called because he's the perfect person who knows a lot about this... I've looked for ways to continue working with him in any capacity over the last 10 years." — Wes McKinney

> "If you can take something that takes three seconds and take that down to 300 milliseconds, that's a big difference. That's a big deal in terms of you press return and how long do you have to wait to rerun your whole analysis." — Wes McKinney

> "I remember the first time I got a contribution from Jeff Reback—he sent me an email and he had edited a bunch of files in pandas and was like, look, I edited these files in pandas and made them better, accept my changes." — Wes McKinney

---

## Transcript

**Michael Chow:** Welcome to the test set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field. This episode is part one of a conversation with Wes McKinney, open source software developer, author, metalhead, and principal architect at Posit. I'm Michael Chow. Thanks for joining us.

All right, Wes, thanks for coming on the test set. I'm so privileged and honored to be able to interview you about your contributions to the Python open source ecosystem. And just to be doing this podcast with you, I feel like is a really incredible opportunity. Maybe to start out, do you mind just catching everybody in the world up on sort of what you've worked on?

**Wes McKinney:** Happy to be here. Yeah, well, it's been a lot of projects over time, but I definitely get asked about this a lot. It's like, how did you start building pandas? And it was, we were just talking earlier today, I think it was 17 years ago this month that I started working on the code base that became pandas.

But I got interested in Python as a programming language in my first job out of school. I was a math major and didn't have much programming experience. I didn't do computer science—I took a couple of theoretical computer science classes in college—but then I got a job in quant finance and thought that I would be doing financial modeling and stuff like that. It turns out I was doing a lot of data processing and data analysis, data cleaning, that kind of thing. And I found that working with data was fairly frustrating.

So I initially became really interested in how I could build tools for myself to make myself more productive and make it easier to work with data. I was very influenced by the R ecosystem, R circa 2008. This was a really long time ago—the tidyverse didn't exist yet. There was ggplot2, but there was no dplyr. A lot of the things that we now take for granted didn't really exist. And the development environment—there was no RStudio either. R was very much more primordial in those days. And I was doing a lot of SQL.

So I started building pandas, which initially was an internal project at AQR where I worked. I eventually got permission to release that as an open source project. I spent a couple years working on pandas a little bit on the side. It didn't get really popular until maybe 2011, 2012 when I had switched to being a grad student in statistics. I was interested in becoming a statistician because I wanted to get better at data science by learning about statistics. But I saw that Python was getting more popular, and I just felt like I need to figure out how to work full time on pandas and help grow this ecosystem.

So it was around that time that I started writing Python for Data Analysis. I ended up dropping out of my PhD and working on pandas full time. I recruited a couple of my colleagues from AQR to come and work with me on that. So that was 2011. I released my book, Python for Data Analysis in 2012.

Then I started doing a hybrid of open source development and entrepreneurship because I was trying to figure out how can I build businesses or create some kind of business model to support the open source development that I was doing. I ended up founding a company in 2013 with Chang She, who was one of the first contributors to pandas that wasn't me, who was also at AQR. We did that startup and ended up getting acqui-hired by Cloudera. So I was at Cloudera, and a group of us started the Apache Arrow project, which is entering its 10th year of development now. That was a big focus for many years.

Right around the time that we started the Arrow project, you mentioned Ibis. Arrow was more about building a better computational foundation for data science, for data frame libraries, but also for interacting with databases in the outside world, file formats, all that fun stuff. And Ibis was a Python project that was about building a richer user interface for translating between the composable data frame concepts that people were familiar with with pandas, but bridging that into the SQL database and data warehouse world, which I was seeing a lot of in the big data ecosystem. Ibis is still an active and in-development project. I'm not working on it so much lately, but yeah.

**Michael Chow:** I feel like there's so much—it's just a tremendous amount of work. And I feel like it's so neat. One thing that really stuck out to me is a lot of the history, and not just the creation, which I think you hit on a bit, but all the organizing and getting people together. The first most impressive—maybe not the most impressive example of organizing, but the first case that really stuck out to me—was your time speed running. And I don't want to take away from the other things, but I almost feel like I'd love to explore just all the organizing you've done, and almost maybe starting there and working forward. This is going back in another decade. Just dial it back one more.

**Wes McKinney:** So in the late 90s, there was a video game that came out in 1997 called GoldenEye 007, and it was one of the most popular console first-person shooters—I think it was the first really popular console first-person shooter that came out. And it developed this cult following, which included me.

For some weird reason, the developers had included this feature in the game where it would show you the fastest time where you beat each level. And I discovered the speed running community when it already existed. There was a website run by this fellow, Glenn McDiarmid in Australia, where it assembled people's fastest times playing the game.

For whatever reason, I was really attracted to helping that community thrive and grow. There was an opportunity for me to take over stewardship of the community and run it for a couple of years. I didn't really know that much about web development, but I really did enjoy, as you said, the community development aspect of building processes and thinking about the governance and how we make decisions. Like if you suspect that somebody is cheating at the game, we had to create processes—submit videotapes and digitize the videotapes and put them online. So that was my first exposure to community development and building that speed running community.

In a sense, when I later got involved in open source development, some of those behaviors were familiar to me from having been active for a few years in that.

**Michael Chow:** And when you were getting involved, how did you find this community and what stood out to you the most? Being part of the speed running community, what really drew you to it?

**Wes McKinney:** I think the people in it were mostly interacting through both email and eventually message boards. This was pre-Slack and pre-Discord, way ancient history. But I found that the people in the community were—I felt that they were a lot like me, that they liked video games and they were interested in technology and the internet.

And the fact that we were like, we don't know how to create the right tools and systems to create this speed running ecosystem and to make it function. But we'll figure it out together. Eventually the community grew and I also got—I went to college and I got busy. I didn't have time to speed run because when you're 13, 14 years old, you have infinite time and schoolwork doesn't take that much time. So I stopped having that much time to play games.

But yeah, eventually I was all surpassed and I'm just a drop in the ocean at this point. If you look at the latest GoldenEye world records—which they still exist and there's still records being set all the time—it's pretty wild.

**Michael Chow:** Yeah. I'd imagine as time goes on, they're like really cooking on it and figuring it out.

**Wes McKinney:** Yeah. You know, maybe you could psychoanalyze it, just like that fixation on efficiency and thinking about how to do things optimally translated in some way to building tools. And it's like, oh, it frustrates me that doing this task related to data processing or related to data science is tedious or inefficient. And so I want to find a way to make it fit my brain better or make it more efficient.

So in a sense, you're like speed running—I guess it's just a personality trait of trying to speed run the data science workflow a little bit.

**Michael Chow:** Yeah. That's fair. And I guess you see that with pandas too, like some of the optimizing and speeding up that there's a lot—I feel like through your work, there's a lot of optimizing.

**Wes McKinney:** Yeah. Early on in pandas, because it was the only tool around for a lot of the things that it was doing—just reading a CSV file and doing some basic data preparation, data manipulation. It was the best, but also effectively the only tool available in Python for doing that. And so if you could make something twice as fast or three times as fast, that would have a meaningful improvement in people's lives.

I remember there were some things that were out of my control, for example, getting data out of databases. In my first job, there was a lot of frustration around doing SELECT * FROM this database table. And that whole pipeline of how do I get this data into pandas so that I can do my data analysis—that was just completely inaccessible to me. I couldn't interact with the database driver, there's just a lot of the machinery there was just out of my reach to really make better. I think that definitely motivated the Arrow work later on.

**Michael Chow:** I do remember, I think you've maybe talked about or written about too, the read CSV is a big one where reading a CSV in pandas, as it turned out was a big kind of—getting that fast was its own thing.

**Wes McKinney:** It's a huge bottleneck. This is going back to 2011—I think we had built a fairly primitive CSV parser reader for pandas that was written in pure Python. There really was no other tool that did the equivalent of read.csv in R. And now there's—I think there was also an early version of fread with data.table at the time. So there was a faster version of read.csv in R.

But it's this kind of small, self-contained problem and very—even though it's a little bit boring, it's weirdly appealing to work on because everybody's got CSV files as much as we talk about how much we hate them. And so if you can improve that fundamental workflow, whether it's making the CSV reader automatically recognize more weird scenarios, like weird delimiters or other things that often foul up CSV readers.

But if you make it twice as fast—a lot of data analysis work, even still, people are working on a laptop, they've got 100 megabyte or could be a small CSV file. But if you're reading it a lot of times doing the same analysis over and over, if you can take something that takes three seconds and take that down to 300 milliseconds, that's a big difference. That's a big deal in terms of you press return and how long do you have to wait to rerun your whole analysis. It might be that 50% of the time is just reading the CSV file, which is pretty annoying.

**Michael Chow:** Yeah, I'm also curious. I know you've mentioned before that for pandas, you spent—your first year, you convinced some friends to go at it with you. What did that look like in the early days of pandas—to convince your buds?

**Wes McKinney:** Well, yeah, abandon their jobs and it was a little more complicated than that. I worked with Adam Klein and Chang She at AQR and we had been internally call it partners in crime in evangelizing Python and building early tooling around Python there. They saw the potential of Python as a language that could straddle the interactive computing and data analysis world and the production software world.

In particular, we saw a lot of potential in finance. And as we explored the ecosystem and talked to a lot of banks and hedge funds and stuff, we just found that it was going to be difficult to build a toolkit that we could license because a lot of financial firms, they want to build all of their own tools top to bottom. To get to the point where—even though we were former quants ourselves—to get to the point where they could license our toolkit and depend on us as a company, that was, in addition to adopting Python at that time, which was 2011, that was a bridge too far.

So ultimately Adam ended up going back into finance. And then Chang and I decided to do a different startup—something still using Python and the Python data stack, but we decided to build more of a visual analytics, data exploration tool company. And that's what brought us from New York to the West Coast, because that's where the center of gravity for those types of tools was in those days.

**Michael Chow:** And then I guess at that point, the community had also started to pick up a lot of the maintenance of pandas?

**Wes McKinney:** Yeah. It was very fortunate that right around that time that we were figuring out what kind of startup to do, the pandas community started getting new core team members. Two of the first major contributors to pandas were Jeff Reback and Philip Cloud.

I remember the first time I got a contribution from Jeff Reback—he sent me an email and he had edited a bunch of files in pandas and was like, look, I edited these files in pandas and made them better, accept my changes. This was pre-GitHub pull requests, I guess. GitHub existed at the time, but pandas was on Google Code and hadn't yet adopted GitHub.

But they were essential to the project becoming more than just my passion project. Eventually it got to a point in early 2013 where I felt comfortable handing off the project to them and say, I trust you, we've been working together for more than a year on this and I'm doing the startup. And they really took it and ran with it.

I frankly credit them and other people that showed up, came out of the woodwork and became really active in the project as being—I think I helped seed the project with developing it the first five years and getting that first critical mass of contributors. But going from 10 or 20 contributors to pandas to 2,000, I really have to give them the credit for essentially building out the project and nurturing it over these last 11, 12 years.

**Michael Chow:** Yeah. It's a really wild move. Just the scale of some of these Python projects like pandas, just the sheer number of contributors and scope they have to wrangle. It seems like a really heroic effort.

**Wes McKinney:** I mean, pandas became this gravity well for anything having to do with data manipulation or data wrangling. But the community has done an amazing job. They've also done a lot in terms of community outreach and saying, we want all kinds of contributions to this project. We want help with documentation, we want help improving even small things in an open source project that make a difference.

By really casting a wide net and making the tent bigger to invite as many people from all around the world to make contributions to the project, both big and small—because you do see some open source projects where the contributors maybe don't communicate so openly, or there's a small group of developers that are insular and they don't try to recruit and bring people into the project and be inclusive.

So having international documentation sprints and community events to get people involved in pandas development has gone a long way towards saying, all are welcome, come here, work on this project and make it better. I think that's clearly been a success. And I don't know the exact number of unique contributors to pandas, but I think it's several thousand at least at this point.

**Michael Chow:** I'm curious too about Philip Cloud, because I know Philip, and I actually love interacting with Philip. I find he's—I mean, I don't know a better way to say this—super funny as a person. He's just a funny guy. He's just got a lot of zingers, I feel like.

**Wes McKinney:** Well, Philip's main thing is that he loves puns.

**Michael Chow:** Yeah, yeah. Okay. You get it. He's a person that you can always count on to not miss a pun.

**Michael Chow:** Yeah. I do feel like we all need a pun person in our lives. All lives are made better with a pun person. And yeah, so I'm glad that pandas got its resident punner.

**Wes McKinney:** What's interesting about Philip is he came from a more science and research background, and that's how he initially got involved in pandas. Then he worked at both Anaconda (formerly Continuum Analytics) and Facebook. So he got a lot of exposure to the development of the Python data science world in the early 2010s, as well as at Facebook (now Meta)—what enterprise ETL, SQL, data warehousing and data management looks like at large scale.

I think it was when he was working for Facebook that he saw that I was working on Ibis. And so the appeal of working on a framework that can translate between the SQL data warehouse world and the data frame world of pandas was really appealing.

Ibis is essentially a query transpiler. It gives you an API for expressing data frame operations. It gives you the benefits of code reuse and programming in Python, tab completion, all the things that SQL doesn't give you—functions, reusable functions.

**Michael Chow:** Mind blowing. Yeah.

**Wes McKinney:** And so you build these big expressions and then you say, oh, I want to run this on the SQL engine and it will give you a SQL query that runs on—I don't know—runs on BigQuery or that runs on PostgreSQL or SQLite or what have you. Now the default backend for Ibis is DuckDB. But when Ibis started, DuckDB didn't exist at all.

Anyway, having him involved in the project and also having the practical experience of coming from that large data warehousing environment at Facebook was really critical for the development of the Ibis project. And I've looked for ways to continue working with him in any capacity over the last 10 years. It's certainly been 13 or 14 years since we started working on pandas together.

**Michael Chow:** And do y'all—like, how does it work? Do y'all have some kind of chat? Is Philip like, yo, I'm looking to get into Ibis, or do you just start—he's working on pandas, y'all are collaborating on pandas, and then he slides over to Ibis. What did he do?

**Wes McKinney:** He just started sending pull requests initially and—I'd have to look back, but I'm sure I sent him an email, say, hey, you're interested in this, tell me more, why are you interested in contributing to this?

So we developed a collaboration on that and then fast forward several years after that—this was like around 2015 that he got involved in Ibis development—and then six years later, Ibis was six years old and Arrow had been in development for six years. I founded a company called Voltron Data with a group of people and we decided that we were going to make a big investment in Ibis as a user interface to a lot of the tools for accelerated computing that we were building.

So Philip was basically the first person I called because he's the perfect person who knows a lot about this and has done a lot more development on Ibis than I have at this point. But by that time, there were also another collection of people who had gotten involved in Ibis development.

So even though it's not as popular or well-known a project as pandas, it still developed a healthy and reasonably thriving community around it—people who are passionate about Python but also have the need to interact with all these different SQL systems and want to write more Python and less SQL.

**Michael Chow:** It seems nice too—I feel like working on open source, it's kind of the dream too, to get a call and be asked, would you want to work on this full-time as a job? It's a real dream scenario.

**Wes McKinney:** Absolutely.

The Test Set is a production of Posit PBC, an open source and enterprise tooling data science software company. This episode was produced in collaboration with branding and design agency, Agi. For more episodes, visit thetestset.co or find us on your favorite podcast platform.