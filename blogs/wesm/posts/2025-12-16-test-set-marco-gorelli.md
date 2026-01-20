---
title: "Marco Gorelli: Narwhals, ecosystem glue, and the value of boring work"
summary: "Podcast at The Test Set (Posit)"
date: 2025-12-16T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-marco-gorelli
word_count: 9124
source_file: transcripts/2025-12-16-test-set-marco-gorelli.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://www.youtube.com/watch?v=dotdfMcfw20"
---

{{< video https://www.youtube.com/watch?v=dotdfMcfw20 >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, Michael Chow and I sit down with Marco Gorelli, a software engineer at Quansight Labs and creator of Narwhals, a compatibility layer between DataFrame libraries. Marco explains how Narwhals allows library authors to write DataFrame operations against an abstract interface while supporting multiple backends (pandas, Polars, PyArrow, and others) without forcing users to convert between formats.

The conversation covers how Marco got motivated to build Narwhals after becoming frustrated that Polars users had to convert to pandas when using most data science tools. He chose to use a strict subset of the Polars API because it transpiles more cleanly to pandas than the reverse. We discuss how the concept of lazy expressions has become central to modern DataFrame APIs, and how projects like Ibis, Polars, and Narwhals have influenced each other.

Marco shares his approach to building community around Narwhals, including proactively searching GitHub for mentions of the project and reaching out to help with integration. The Narwhals Discord has become an active community with regular study groups where contributors help each other understand topics like Python's type system.

I share some thoughts on using AI coding tools for personal projects, noting that while they're not suitable for building something like Apache Arrow, they're effective for building personal tools quickly. We also discuss the chicken-and-egg problem of LLMs needing training data from projects that users won't adopt until LLMs know how to use them.

## Key Quotes

> "If there's something you find interesting that other people find boring, then you've just found your competitive advantage." — Marco Gorelli

> "The dog fooding process is just so valuable. For anyone wanting to start a tool, that's probably the best thing you can do to make it usable. Just try using it yourself for an extended period of time." — Marco Gorelli

> "Most people if they try a tool and find a bug, they uninstall it and move on to something else without even reporting the bug." — Marco Gorelli

> "People sometimes underestimate how important the social part of open source is as opposed to purely the technical part." — Marco Gorelli

> "I think the best way to look at some of these AI tools is as a way to delegate work that is suitable for AI and work that you don't want to do, that you would benefit from but you don't want to do it yourself because it will drain too much of your energy." — Wes McKinney

> "You can build a totally custom tool for yourself in a short amount of time in a way that would never have made sense in the past... while sitting on the couch watching Netflix, sipping tea, and occasionally interacting with the agent." — Wes McKinney

> "For the development of Narwhals, AI tools have been incredibly frustrating because they just always spit out things that look plausible but that actually are missing some very key details." — Marco Gorelli

> "If you ask an AI what's the SQL equivalent of the Polars n_unique function, it'll tell you count distinct. Except it's not actually equivalent because Polars counts null values in n_unique, but count distinct doesn't." — Marco Gorelli

> "The most satisfying parts of doing open source for me have been the people that I've met along the way, the collaborations that I've been able to have." — Wes McKinney

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field.

On this episode, we sit down with Marco Gorelli, Celtic folk shredder, Narwhals mastermind, and software engineer at Quansight Labs.

**Michael Chow:** Welcome to The Test Set where we explore the people behind the data. I'm Michael Chow, a principal software engineer at Posit. And I'm joined here with my co-host Wes McKinney, creator of pandas, co-creator of Arrow, and principal architect at Posit. And I think we're super pumped to have Marco with us, who is a software engineer at Quansight and creator of Narwhals and also a maintainer or former maintainer of pandas. So doing a lot of DataFrame stuff. Marco, thanks so much for coming on to The Test Set. I'm a giant fan of your work and just the rowdy party that is the Narwhals Discord. So happy to have you on.

**Marco Gorelli:** Yeah, thank you so much for having me. It's a pleasure to be here. In fact, Michael, I think you might have been the first person—you and Rich—I think you might have been the first people who I ever demoed Narwhals to.

**Michael Chow:** Oh, wow. Yeah, that's actually—I remember a lot of this is almost like an open-source thing. Like I remember having like an early chat. But that's actually crazy. I didn't know that it was that early in the Narwhals process.

**Marco Gorelli:** We met up to talk about something else which was about Great Tables and then I think I just ended the call by saying, "Hey, check this thing that I just started over the weekend." And sometimes your little weekend projects end up running away from you a bit and spiraling out of control. And that's what's happened here.

**Michael Chow:** Yeah, I love that. I mean, it's been really cool to see. And maybe for some background context, I guess you're also a contributor to Polars. So you've kind of spanned a lot of these DataFrame libraries. Polars, pandas, Narwhals. I mean, I'm embarrassed to say that I've actually never used Narwhals myself. I know what it is, but probably there's plenty of people listening who haven't heard of Narwhals. They're like, Narwhals, what is that? So maybe you can explain the project and how it came about.

**Marco Gorelli:** Yeah. Sure. I mean I think it's very likely that you have used it but accidentally in the sense that it's intended as a compatibility layer between DataFrame libraries and it's not something that end users tend to use directly. Rather it's something that people tend to use as a transitive dependency. So they tend to use it because some library that they're using is actually using Narwhals under the hood in order to be able to handle multiple kinds of DataFrame inputs.

As an example, if you've been using Plotly since version six, then Narwhals is a required dependency and it's used to do all of the DataFrame operations. This allows it to accept let's say a Polars DataFrame and keep all the computation native to Polars until it has to serialize it, without having to convert to pandas or to depend on pandas. And conversely, pandas users can keep passing in pandas DataFrames to Plotly without needing to take on Polars as a dependency. Like you can meet users where they are and both the pandas and Polars and PyArrow user bases can just enjoy using their native tools with Plotly and other data science tools without having to even necessarily know that Narwhals exists.

**Wes McKinney:** Yeah, I was just looking and I saw that it has 43 million monthly downloads. So it's definitely gotten some uptake, but to your point, I guess it's being picked up as a transitive dependency in a number of projects.

But I'm familiar with the problem because in the early days of pandas, people would want to accept pandas DataFrames in different libraries. I know that scikit-learn was one of those projects where people were like, I really just want to pass a pandas DataFrame into this project. But there was this challenge of like well we can't require pandas as a hard dependency of scikit-learn, and but then like what if people want to pass other types of tabular data structures? And so yeah it seems like it's solving that problem and the evidence is in the uptake of the project which is great.

**Marco Gorelli:** Cheers. Thank you. It's interesting that you mentioned scikit-learn actually. I just got pinged today on an issue in their repository where they're talking about using Narwhals because they do currently accept both pandas and Polars but they've got their own hand-rolled compatibility code which I think they're getting a little bit tired of maintaining. There's been some issues reported and it's the kind of situation where if they can outsource the work to a project where the only thing that we're concerned about is handling compatibility between different DataFrame libraries, then that can leave them to focus on their own competitive advantage.

**Michael Chow:** And if I'm understanding—is it you're saying a lot of libraries they need to do like a little bit of DataFrame stuff, like they want to take kind of like a tabular structure, they might want to choose some columns or filter a little bit of data. So before Narwhals or a lot of these kind of compatibility tools, they were sort of stuck with being like, oh well, I want to do a little bit of DataFrame stuff, so I sort of need to choose a DataFrame to make a dependency and kind of build on top of. Is that right?

**Marco Gorelli:** Yes, that's exactly right. Whereas Narwhals allows you to write your DataFrame operations against the abstract idea of a DataFrame and then whatever the user passes in will use the user's library.

Now my expectation when starting it was that the pain points we'd be addressing would be things like—I don't know—does group by maintain order? Or in the unique function if you've got a null value does that count as one unique value or do you have one unique per None or do you not count null values at all? And in the early days I realized that actually the biggest pain points had to do with data types. In pandas if you want an int64, there's currently three different ways of expressing an int64 column. If you want a string column, there's even more. And unless you're actively very closely following developments in the pandas GitHub repository, it's very difficult to stay on top of it all.

**Michael Chow:** Yeah. I could see that some of the details of some of these DataFrame libraries can be a bit tricky for developers.

**Marco Gorelli:** Yes, exactly. I think I might—we might have had a discussion in Great Tables about this as well where there was one of pandas' string data types which was displayed in one way but then if you used the PyArrow-backed string type it was displayed in a different way, but arguably from an end user perspective it's just a string column.

**Michael Chow:** Yeah, totally. In this—I should say so Great Tables is a tool I maintain that helps display tables and we don't use Narwhals yet because I think we released before Narwhals did. But we're ready—just to maybe hype you up—we're ready to switch to Narwhals for a lot of the things you said, to kind of take some of that burden off of wrangling different types of DataFrame inputs. So people can just bring whatever DataFrame they want and kind of get really consistent stuff.

But yeah, I wouldn't be surprised if some of this happens—like as things go in and come out, if they come out really different than maintainers expect, because it's just so many details to kind of keep track of. Like it's a big job that Narwhals does.

**Marco Gorelli:** Exactly. Yeah. I mean in the Narwhals documentation there's a "why" section where I try to answer why would we need something like this anyway and I give some examples of simple DataFrame operations which look like they should be superficially the same between libraries but actually behave wildly differently.

Now, I don't know if we'll get to it later on the topic of using AI tools for development, and I don't for a second want to discount the value that AI tools can bring in certain contexts, but for the development of Narwhals, they've been incredibly frustrating because they just always spit out things that look plausible, but that actually are missing some very key details.

For example, if you ask an AI, what's the SQL equivalent of the Polars n_unique function, it'll tell you count distinct. Except it's not actually equivalent because Polars counts null values in n_unique, but count distinct doesn't. So you'll need to do count distinct and then compensate for whether there were null values present or not.

**Wes McKinney:** I mean, the irony is that LLMs are notoriously bad at counting.

**Marco Gorelli:** Yeah, I thought too.

**Michael Chow:** Yeah. Wes, I know you've—I feel like you've talked a bit about this, like the challenge of even indexibility, like what have LLMs trained on and absorbed from open source tools?

**Wes McKinney:** Yeah. Well, there was a period of time—I think it's gotten better now—but there was a moment in time where there was a gap between the present reality and when the training cutoff date was for some of especially the earlier versions of ChatGPT or Claude.

I think it's gotten a lot better because firstly I think the AI labs have done a better job of getting their models closer to present day in terms of slurping up all of the data on GitHub and all over the internet to keep the training data closer to the present day whenever they release the models. That plus libraries like Polars have stabilized a little more—like they aren't changing and refining nearly as quickly. And so just as a combination of the models getting better, the training data getting better, and Polars stabilizing—so now using the coding agents to use Polars, like I've been using Polars to build a personal finance side project. And yeah it stubs its toes and it does things wrong maybe 10% of the time or 20% of the time but it's a lot more—I feel comfortable, a lot more comfortable using Polars with Claude than I did a year ago.

**Michael Chow:** Yeah, sure. So, this was MoneyFlow, was it something like that? Yeah, just saw some announcement about that. Looks good.

**Marco Gorelli:** Funnily enough, the first time I met Ritchie who is the creator of Polars was at EuroPython, I think in 2023. And I remember at the time we had a little discussion and we were saying, "Should group_by actually be group_by because that's generally the philosophy that Polars follows in its API." But groupby was just a single word, I think, just for compatibility—just because he'd taken it from what pandas was doing.

So we said, "Yeah, sure. Let's change it. Seems like a minor thing. What's the worst that can happen?" And then GPT got super popular and the cutoff date was just before that deprecation was introduced. It was phenomenally bad timing. I'm relieved that this didn't kill the project. But I think it was a good idea to change it anyway. Like it is kind of nice that now Polars has got to the point where the API is really consistent in its naming. You always know that if you've got a method with multiple names, it's always snake case.

**Wes McKinney:** We did the same thing with group by in Ibis, which is like maybe has a slightly similar type of vibe to Narwhals but different goals.

But you know partially—when designing the API of Ibis, there was a goal of deliberately placing distance between the perceived sins of the pandas API, like making things a little more normalized and consistent.

But it's interesting because it's nice that now we have this whole idea of having an expression system and being able to express complex aggregations or complex DataFrame operations with a lazy expression system. Going back in time, we really didn't have that. But now it's nice that we have the type system of Arrow and modern databases with nested types to provide some structure for—okay, these are all the things that expression systems need to support. And then Polars designed its expression system to be able to do all of the fancy things you can do inside Polars aggregations and Narwhals has adopted that.

It seems like there was an effort to maybe push some of that upstream into pandas. Like I heard rumblings of pd.call and—you know, I always wanted to have an expression system within pandas but it was one of those things that even today it's still like my eyes bleed when I look at people trying to do complex aggregations in pandas and they're passing lambda functions and I'm like no, that destroys the performance. And yeah so it's the nature of open source—we're never quite where we want to be but we're always working and trying to make progress.

**Michael Chow:** Yeah. And I think pd.call is out. I think they released pd.call. Was that Marco? Were you responsible for that?

**Marco Gorelli:** I opened the pull request. Yeah. Maybe just to clarify, it's not as nice as I would like it to be. So currently it can only be used in places where pandas already accepts callables. So for example the .loc and get_item and assign—those are the big ones. In group by it would require some other upstream changes in pandas which I didn't yet have the capacity to do.

But it's interesting that you bring up how central the concept of expressions became and I totally agree. I think it's just so important to be able to express the abstract idea of an operation that you want to do without any of the objects in the expression having to be tied to any particular DataFrame.

When Narwhals started, it was somewhat in response to a previous effort at trying to standardize DataFrame APIs where one of the major points of contention that I had with the other participants was on the concept of expressions. Other people wanted to keep the API much more tied to Series and DataFrames. Those were the two main objects they wanted. Whereas I wanted expressions. That was one of the major points that we just were not able to get agreement on unfortunately.

But I'm glad that in the years that have since passed the concept of expressions has become really popular and users certainly seem to enjoy it. You mentioned Ibis having expressions and in fact I think Ibis took expressions from Siuba which was a product started by Michael. So, we've really come full circle here in this chat.

**Michael Chow:** This is really—there are a lot of arrows pointing to a lot of different places so far in this chat. But it is funny because I do think that Ibis adopting lazy expressions is actually what really made me feel good about Ibis.

Like Ibis is so powerful. So, it's a—I'll just summarize again, I know it's come up. It's a tool to basically be a DataFrame API that could fire on say a SQL backend or like a pandas DataFrame. I think they have support for Polars and things like DuckDB. So it's a nice way to kind of use a single API to fire a lot of places. And these types of tools are so critical I think as a human being—to just be able to think in one DataFrame and fire a lot of places is such a relief.

But it is funny when I was thinking about building Siuba I did try Ibis and I do think that there were a lot of—for me coming from R—it did involve a lot of lambdas that was a bit cumbersome. But I think to that team's credit once they rolled out lazy expressions and they really got cooking on a lot of different stuff, I feel like they really created such a powerful tool.

**Wes McKinney:** Yeah, at that time Ibis didn't have the underscore—the generic expression. So you would have to start from a referenceable expression object in order to build subsequent expressions. Whereas the underscore allows you to build an expression and then it late-binds and resolves the expression kind of within the expression tree when it's compiling.

But it's a good example of—because I started on Ibis in 2015 and initially around that time there was another project that was being developed at Anaconda, formerly Continuum Analytics, called Blaze. And it was a similar expression system trying to tie together NumPy and pandas-like operations as well as potentially—this is the same era where Dask was created by Matthew Rocklin. And I was working with a lot of SQL engines and so Ibis was essentially an effort to try to reconcile the relational algebra of SQL databases with DataFrame operations.

So it started from the standpoint—not necessarily of being—and so this is where I say the vibe is similar to Narwhals but the objective, the end goal, is different. Whereas rather than being a portability layer to enable libraries to write code once and target different DataFrame libraries, Ibis' goal actually was to have a DataFrame-like API that could express all of the concepts that are found in modern SQL.

So if you're using Postgres, Postgres has these fairly normal concepts in relational algebra and in databases that don't really exist in pandas. For example, ideas like correlated and uncorrelated subqueries, and anti-joins and semi-joins—you know, different things that are very normal in the database world but there hadn't been that much database technology that had trickled through to the Python ecosystem.

So it's interesting, but it's nice that these projects have influenced each other and—again, that's the magic of open source that people have good ideas and every project should curate everybody's best ideas and use them to be better and to make improvements. And not be stuck in the way that things are and be willing to give credit where credit's due.

And so I'm very excited about where things are and the general trajectory of things. Compared with 10 years ago it feels like a world of difference. So I have to give credit to everyone and all the work that they've done to get to where we are today.

**Marco Gorelli:** Absolutely. And it's impressive just how many projects you've been involved in that have then played such a central role in this.

**Wes McKinney:** I like to tinker but I also like to collaborate. I like to work with people. And so sometimes people are often saying hey you worked on this or you built that or you built that. But honestly, the most satisfying parts of doing open source for me have been the people that I've met along the way, the collaborations that I've been able to have. Like finding smart people who are really motivated about working on a certain problem and trying to figure out—okay how do we work together, how do we find the best path forward? Build things that people like, get them out there, get them released, help them get adopted and all that.

So yeah, I mean I'm curious. I mean Marco, how you got involved in the space and what's driven you to work on these problems? Because working on expression systems and abstract DataFrame APIs and those sorts of things—it's not... they're problems that appeal to certain people but not all people. Love using the libraries, but actually building them is another thing entirely.

And so we have—we're here on a podcast with all three of us who have worked on different lazy expression systems for DataFrames. And so I think that's kind of maybe the first time I've been—maybe it would be nice if Philip Cloud was here and maybe Matthew Rocklin, you know, we would have a whole group full of intermediate representation expression system fanatics.

**Michael Chow:** Yeah, totally.

**Marco Gorelli:** Yeah, sure. So how did I get interested in this space? What made me want to spend a big chunk of my time and now fortunately some part of my job tackling this problem?

Perhaps just quickly before I answer this—since Ibis has come up a few times—just to clarify, it's not in competition with Narwhals at all. In fact, Narwhals now supports Ibis as an input. So you can choose to use Ibis with a Narwhals front end if you wish to.

**Wes McKinney:** Yeah, I don't regard the projects as competitors and but I agree that to an onlooker who isn't familiar with this ecosystem—superficially when you squint at these projects from afar they do look very similar. But when you actually get involved in the details—there's what it feels like to actually use the library day-to-day.

So when I was saying that the vibe is similar, I feel like the vibe is—like the feeling of using the software is a little bit similar but the goals and the objectives of the project and what it's trying to do—that's where there's the divergence.

So but I can admit that trying to explain that to people on LinkedIn or on X or Blue Sky or something could be a little bit tricky.

**Marco Gorelli:** So yeah, to get back to the question, what got me interested in the space?

Originally, I was really just frustrated with the fact that I was a huge fan of Polars. I really liked using Polars. I really liked contributing to Polars. But then one of the most frequent complaints I heard from prospective users was that when they went to use their favorite data science tools, they either had to convert everything to pandas or the tool would claim to support Polars, but under the hood it was just converting to pandas.

There are some cases when that's okay. You really don't see the effect of it. But there are cases when the performance penalty can be quite large—like converting a string to object in pandas can be quite expensive. There are some data types that don't exactly match. And perhaps one that I really felt strongly about in terms of missed opportunities was that Polars has both a lazy and an eager API whereas pandas is purely eager. So having to convert everything to pandas when there were some operations which could in principle have been done lazily—it really felt like a missed opportunity. It felt like it should have been possible to do much better.

And I could see that some libraries were doing—like what you were doing in Great Tables, Michael, where you had your own hand-rolled compatibility layer. Scikit-learn was doing something similar. HPPlot had their compatibility layers for cuDF and Dask and others. There were some other libraries that were doing similar things.

So I just figured well let's try to make something reusable. And we need to choose a common API. Originally I thought about using the pandas API but I found that it was a bit frustrating to try to transpile Polars to pandas whereas doing it the other way round it just worked beautifully. The Polars API is stricter than pandas and arguably when it comes to doing transpilation, it's easier to start from users writing something in a stricter API and then transpiling that to the less strict one.

Also, pandas has the concept of an index that Polars doesn't have. So if the user does not have to write index code directly then that's one less thing to worry about.

So I just tried this and you can see in the early commit messages in Narwhals before I released it—when I was just writing it by myself as a little one-person experiment—the commit messages start saying things like "ooh it works," "getting there," three exclamation marks. Like I was really excited at first.

At some point, I published it online and started enforcing pull requests and reviews and all of that. But for better or for worse, those early commit messages that I was just writing to myself are still there in the project history. But it's actually not too bad to see the excitement that I was feeling at the beginning when I realized that actually transpiling Polars—yeah, translating Polars syntax to pandas was fairly satisfying.

So really that was the original motivation—just trying to solve this ecosystem problem where we had all of these really nice DataFrames out there but frustratingly the data science ecosystem was locked in to pandas.

The first time I presented Narwhals after having showed it on a call to Michael was at PyCon Lithuania in 2023. And I ended the presentation by saying that my hope for the next year was that we would see the data science ecosystem become less locked into pandas and that maybe we would also see Duolingo add a Lithuanian course. And only one of these things happened. I think there's still no way to learn Lithuanian on Duolingo, but hopefully they'll address that as well.

**Michael Chow:** Wait, I'm super curious to hear about—to go back to Wes's question—how you got into some of this. And also I know Narwhals has this really active Discord community. I'd be really curious to hear some of the outreach you did, like how did you get involved and what did you do early on to kind of build out the Narwhals community? Because it's a happening place. It's like a pretty sweet crew you've got.

**Marco Gorelli:** Sure. Yeah. So, you're asking how did I get started with the project? Yeah. So, I've covered the motivation—about not having data science tools all locked into pandas.

And about physically how it started, I just put it out there. I remember sending it to some newsletters and to my surprise people started checking out the repository, giving it stars. And I kind of got a bit of a signal that okay maybe it can be useful, maybe people kind of like the idea.

And the original name for the project was "polars-api-compat"—the idea was that it would just make other APIs compatible with the Polars API. And then I figured, wait a second, I really want this to become popular. That's not going to work in the present day and age, is it? We need an entertaining name. People want to be entertained. And all popular data science projects seem to be named after animals.

So I looked on the Wikipedia page on the list of animals that had not yet been taken and I found puffin. Seemed like the perfect name. But unfortunately, there was already a Python package called Puffin.

And then I found Narwhals which immediately reminded me of that viral Mr. Weeble song about narwhals. And I thought ah I can't call it this, people will just think of the meme. But actually that ended up being the biggest strength—like you see the project, you already feel entertained and you already get a bit of a sense of fun. And that's something we've tried to keep throughout the contributing process.

When people submit pull requests, I don't just approve it. I give them a little narwhal gift. And I love how other people who I then added as maintainers also took on the practice and give each other celebratory narwhals gifs on their successful pull request reviews. It's honestly really sweet.

**Michael Chow:** Yeah. Super sweet to see gif slinging I feel like in a repo.

**Marco Gorelli:** Yeah. We were thinking about making an official list of Narwhals-approved gifs to use in pull request reviews.

On the rest of the community—I feel like I need to give a shout out to Inessa Pawson who is from Open Teams, which is a sister company of Quansight Labs. And she was one of the first people to really believe in the Narwhals project. And she encouraged me to start a community call and a Discord and a way for contributors to interact in a low pressure environment.

Because if you've got a GitHub page, in theory anyone can communicate with the project. In practice, a lot of people don't really feel comfortable just asking a casual question by opening an issue. They feel like it's a very serious place and that GitHub issues aren't really an appropriate place to banter or to just have a casual chat about what you're doing with the project. Nor is it an appropriate place to showcase things that you might have built using the project.

But if you've got a Discord with several channels, then people are more than welcome to do that. And I really need to give her credit for having encouraged me to do this early on. I did not think that there would be any interest. I thought it would just be like a dead Discord server. But no, contributors started hanging out there, helping each other out, sharing things.

The best thing that's happened, as far as I'm concerned, is the study group. So I think weekly or bi-weekly some regular contributors meet for what they call the Narwhals study group in which they just share learnings that they've made while contributing to Narwhals and they help each other out with making sense of lots of topics. They've had a lot of discussions around the type system in Narwhals. In Narwhals we take typing very seriously. There's a lot of typing shenanigans going on. But if you want compatibility between APIs, then I think that's a fairly important thing to do.

**Michael Chow:** It's cool to think about that—like doing a contribution where you wire some stuff up is maybe a good step into a study group. That kind of pipeline from contribution to study group in Narwhals. It's interesting to hear that kind of dynamic brought to the front of a Discord.

**Marco Gorelli:** Nice. Yeah. And the group really has gone beyond Narwhals in the sense that it usually starts off with some topic that they might have encountered while contributing to Narwhals. For example, like what's a protocol? What does it mean for a type to be covariant? And then they explore this deeply, try to understand it, try to make analogies. And yeah, it's really been very rewarding to see that happen.

**Michael Chow:** And you were—I feel like there's a period of time where you were almost showing up in any place that made any mention of Narwhals. It was like a way to summon you. Is that true?

**Marco Gorelli:** Yeah, there is some truth to this. So I realized when I published my first open source project back during the initial COVID outbreak—it was called nbqa. It was a little quality assurance tool for Jupyter notebooks. And at the time my assumption was that if you published a tool and it had a bug, somebody would open an issue and tell you about it and then you fixed the bug and then it would be better for everyone else.

And that's when I realized no. Most people if they try a tool and find a bug, they uninstall it and they move on to something else without even reporting the bug.

But GitHub makes it easy to just do a sitewide search for mentions of keywords. So just searching around for mentions of the word—I started seeing issues that people were running into that they weren't even reporting. And I just figured, ah, this is so valuable, this is so useful, I can address these things.

And so when I started Narwhals, I was just already used to having to proactively look for issues that people might be encountering rather than relying on them to report things. So yes, I would just do GitHub searches for mentions of Narwhals. Fortunately, Narwhals is a fairly unique name. So most mentions that came up were exactly of this project.

And if I saw projects saying, "Oh yeah, we should maybe consider looking into this Narwhals project," I was just so keen on getting it, getting the ball rolling, that I would show them how it could be done or in some cases even open a pull request to them showing, hey, here's a proof of concept of how you can Narwhal-ify your codebase.

And that was so valuable. Like you just realize so many things about your tool once you actually start trying to use it to solve a problem. The dog fooding process is just so valuable. For anyone wanting to start a tool, that's probably the best thing you can do to make it usable. Just try using it yourself for an extended period of time.

**Michael Chow:** Yeah. Yeah. I love that. And I will say I know we got some experience of that too on the Shiny team at Posit for Py Shiny. Some engineers from the Py Shiny team and you got to pair and I got to ride along. And just as you were like, "I'll jump on a call, you know, if you want to roll Narwhals in." And I do feel like it really gassed them up—to just have you there, break things down and even explain how Narwhals could do the things that they asked. To have that answered so fast was I feel like really impressive—to just have the person on a call kind of clearing the path.

**Marco Gorelli:** Oh, thank you. I think people sometimes underestimate how important the social part of open source is as opposed to purely the technical part.

Maybe a nice example of why this is so important. The first major library to start using Narwhals was the Altair visualization library. And originally I would have thought there's no way that they would trust a small project like Narwhals or consider taking it on as a required dependency.

But I remember in the GitHub discussion about it that one of the Altair maintainers had said that he'd seen a talk that I'd done in person at PyCon Germany. He liked the talk I'd given. He liked how I'd come across to the audience and all of that. And so because he already knew me, because I'd already earned a bit of social capital in their world, they felt that they could trust this project that I'd put out.

So talking at conferences, putting yourself out there, generally trying to be a good member of the community—it can really pay off later if you want people to trust something that you've built.

**Michael Chow:** Yeah. Super cool to see. Wes, are you doing—I know you're—you've mentioned MoneyFlow a little bit, the open source tool you've been tinkering on. Are you rolling into any places or getting the word out, surfing GitHub?

**Wes McKinney:** I mean, it's really just a that's just a nights and weekends thing that was also an experiment to see—to learn more about building a new open source project from scratch being using Claude Code as the main driver. So, you know, it's done all the CI/CD. It built the docs, the website—like everything is pretty much AI generated.

But it's really a side project and if nobody uses it, it's actually fine because I use it to do my personal accounting and keep track of my expenses.

And I think what's interesting about this new era of AI assisted coding is that you can build a totally custom tool for yourself in a short amount of time and in a way that would never have made sense in the past. Like this is a tool that—maybe if it was my own time coding from scratch, maybe I could have built it in like three or four weekends, working eight hours per weekend. And I could have built it all myself. Like I didn't need a coding agent to build it.

But I could build it basically while sitting on the couch watching Netflix, sipping tea, and occasionally interacting with the agent. And I could build a totally custom tool for myself that's customized to my particular needs and not feel bad about it or feel like I'm overengineering, yak-shaving something just to save myself 5 minutes now and then—which is kind of the reality.

You know, there's that XKCD comic—like how do you justify building something to save yourself time? And I think now if it's building some custom widget that saves you a little bit of time here and there, you can justify doing that with coding agents. Especially stuff that involves a lot of just interacting with web APIs. So simple stuff like that—it's not suited—I don't—it's not suited for—you aren't going to build a new Apache Arrow with Claude Code, at least not yet. But you can build a CRUD app for working on your personal finances.

**Marco Gorelli:** In terms of social capital, it sounds like this MoneyFlow is like a personal tool that you're happy to share with people but it's not your primary goal that this gets a lot of adoption. Like the impression I get is that what drives—what's maybe been the greatest driver or source of satisfaction for you has been enabling what I've heard you refer to as the composable data system where you think about how different tools are working together.

**Wes McKinney:** Yeah. I mean that's been—you know in terms of professionally the last 10 years like building the composable data stack. Like creating Apache Arrow and now the greater Arrow ecosystem of like Arrow Database Connectivity (ADBC), DataFusion, DuckDB—kind of two of the embeddable execution engines that are designed for use with Arrow.

There's now a bunch of new file formats—like I got very involved in Parquet development in the mid-2010s because you couldn't read Parquet files in Python and that was just completely unacceptable.

But it's nice that AI has come around and enabled me to scratch itches—things that I've thought about for several years, but I could just never justify taking time away from my main work projects to work on. I couldn't spare energy on nights and weekends because I needed to save that energy for maintaining open source projects or working on a new edition of my book or things like that.

But I think the best way to look at some of these AI tools is as a way to delegate work that is suitable for AI and work that you don't want to do—that you would benefit from but you don't want to do it yourself because it will drain too much of your energy. Or it's just would take time away from stuff that actually is the more valuable work that you could be doing—like enable you to focus on the things that really matter.

**Michael Chow:** It is really interesting too. I feel like these types of tools—whether it's like a composable data stack ecosystem or Narwhals kind of undergirding and connecting a lot of pieces versus a sort of more tightly scoped thing like MoneyFlow where you're like, oh I have this personal problem and actually I could tell you right away if it feels good to use this tool on it.

I feel like it's such an interesting dynamic—those tools that are more kind of ecosystem, social, infrastructural versus one where you have a quick feedback loop with yourself where you're like I'm feeling good. And it is interesting that I do feel like for AI projects, I've also—it's been interesting to spin up personal libraries and just kind of see like am I having a good time so fast? Like that feedback loop.

**Wes McKinney:** Well, one question I have for Marco. I'd be interested in what it's been like because Narwhals is a newer project and so people are—many people are hearing about it for the first time in the last year or two.

And so I feel like AI is definitely shaping the way that people learn about new open source projects and how they interact with them. And so we spoke earlier in the podcast about the challenges of LLMs being able to keep up with the latest API changes in projects.

But how people will discover and start using a totally new piece of software is a little bit an open question. Like I'm concerned that maybe people won't be motivated to use anything new that their LLM assistants don't already know about. And so you're kind of hopeful that eventually the AI labs will index your project's documentation and figure out how to use the project on their own and then start offering suggestions to the users.

But essentially it creates this chicken and egg problem where the models are dependent on training data to understand how to best use these projects. But if people won't use the projects and create the training data, then how will the LLM ever bootstrap and get to a point where they become experts in how to use your new open source project?

So I wonder—do you feel like you see the effects of that in Narwhals and how responsive—I mean it sounds like you've got a community of people that are contributing to the project and really active in development and you get feedback from them. But often I find in open source that the feedback from the user base can often be delayed by 3 to 6 months because it might take six months before somebody picks up the last release that you made or the release that you made six months ago and starts to wrap their mind around new things that you added or changes that you've made.

**Marco Gorelli:** Yeah, that's absolutely been at the top of my mind. So when I started the project, I thought it was fairly important to make something that felt familiar to people. So that's why I chose the top level API. I decided it would just be a strict subset of the Polars API.

So whatever work in indexing LLMs have to do to familiarize themselves with the Polars API—it should all automatically transfer to Narwhals. They only need to learn some extra things like from_native and to_native for how to get in and out of the library.

Seeing as composability has been brought up as well as DataFusion—something that we've just released this week has been narwhals-daft. So this is a plug-in for Narwhals and this is the first plug-in that we release. And it's intended to be a reference for how to write Narwhals plugins.

And what I'm envisioning here is really something like a composable ecosystem where in Narwhals we have some protocols which just define what methods some expression classes, some DataFrame classes, and some namespaces need to implement. And as long as libraries implement those and they hook things up correctly using the plug-in architecture, then they can become Narwhals-compatible for free.

So this means that any codebase written using Narwhals—like Plotly, Altair, scikit-learn, etc.—it means you can pass in a Daft DataFrame as long as you've got your plug-in installed. And it also means that people can make plugins for their own systems.

Like I'm hoping that either we or somebody can make a DataFusion plugin, somebody can make a pure Python dictionary plugin, somebody can make a plug-in for Bodo—like lots of other tools are coming out. It's not really feasible for us to maintain all of them in a library that is meant to stay lightweight.

But what we can do is we can define a plug-in mechanism, we can define some protocols that people can follow, and then hopefully the ecosystem can just become composable from people following it.

**Michael Chow:** Just for people listening, what would you—how would you define a plugin? Like what is a plugin?

**Marco Gorelli:** By this I mean an extra library that you can install which is an optional add-on. So by default if you install Narwhals it'll support pandas, Polars, PyArrow, Modin, cuDF, Dask, Ibis, SQLFrame, PySpark, DuckDB—hope I've not forgotten anyone. It'll support these inputs.

And if you install a plugin like the narwhals-daft plugin it'll also accept Daft. When we have the narwhals-datafusion plugin, if you install that it'll also support DataFusion, and so on.

So I think like this we should be able to really empower the community to make their own little plugins that can compose with everything else.

**Michael Chow:** Yeah, that's really exciting. So people can make some of these that don't have to live inside the Narwhals community. They can kind of build them out on their own but still work and integrate with Narwhals.

**Marco Gorelli:** Yeah, that's exactly what we're aiming to enable. Yes.

**Michael Chow:** Just looking more broadly, anything you're really excited about in the Python ecosystem more generally?

**Marco Gorelli:** Overall, I'm really excited about people solving quote unquote "boring problems." Be it enabling tools to compose better with each other, be it the typing—like just the static typing in Python that just keeps getting better with each new Python release.

I think when it started to come out, people were often very skeptical about it. Feelings were mixed. But recent Python releases—it's getting really solid. It's getting much better. So I'm fairly excited about that.

I like the advent of tools like DuckDB which even the creators describe as a quote unquote "boring project." And yeah, hope that we can have more of this.

And even what Wes was talking about—you know, file formats. I think there's just so much that we can solve to make the experience of working with technology more efficient and more pleasurable.

**Michael Chow:** Yeah. Yeah. That's so powerful to hear and I definitely—I don't doubt that a lot of boring problems deep in the ecosystem will make lives way better for users kind of across the board.

**Marco Gorelli:** Totally. So, there's one piece of advice somebody once gave me. Unfortunately, I can't remember who. But it was that if there's something you find interesting that other people find boring, then you've just found your competitive advantage.

So to anyone listening, if you happen to stumble on a problem that you find interesting and other people just don't seem very excited about it, well, maybe don't give up on it. Maybe try to go really deep on it, and you might just discover something that you can make an impact on, and that can be very rewarding.

**Michael Chow:** Yeah, that's incredible. I feel like that's such helpful advice. I guess maybe one thing I do want to close out on that I feel like we can't leave out is—as a personal tidbit, I think you mentioned for fun, just Marco fact, you like to jam out for little Celtic folk sessions. Is that—could you take us on a tour of that, Marco? You know, Celtic folk Marco.

**Marco Gorelli:** Sure. Well, in fact, just after this call, I'm going to head to the Irish pub in Cardiff. There's an Irish themed session this evening. So, we're going to play some mix of tunes, some Irish traditional music, some crowd pub pleasers. And yeah, that's my favorite thing to do outside of work—just learning songs, mostly on guitar, which I've played for the last 20 years or so.

And yeah, I think it's a good way to disconnect from work and kind of escape into a different world. And it's a very fun way to meet people who you otherwise wouldn't get the chance to meet as part of your work.

**Michael Chow:** Do you ever—have you ever jammed out on Celtic folk at like a PyData or have you taken it on the road?

**Marco Gorelli:** Oh yeah. Yeah. So in Quansight, the company I work for, there's quite a few people who play instruments. The company founder Travis Oliphant is an incredible singer. So when we have our meetups, we always make sure to reserve some time in the agenda for jam sessions. And for me, those are the highlights of the trips. And I know that other people feel similarly. Music really has this power to bring people together and connect them.

**Michael Chow:** Yeah, that's so cool. Wait, I love that y'all are getting together and are able to do that. Also doesn't—so I do a little bit of contra dance down the street every week and I know that—are there people boogieing? Is there—do you have people dancing or is it just you're just jamming out?

**Marco Gorelli:** So sometimes people dance. Yeah.

**Michael Chow:** Is that person ever you? Are you strictly—

**Marco Gorelli:** Usually I'm just so focused and excited by the music that I'm too busy playing it. I'm also not particularly good at dancing. So I wouldn't be the person to lead that.

**Michael Chow:** Well, Marco, I feel so honored to have us all—to have you and Wes in a podcast. I feel like life with DataFrames and analyzing data has been made so much better in Python today by you focusing on this problem of just how to connect things and how to interchange.

And I do think that your emphasis on boring problems—like I feel like we're all so much better today because you're thinking about how every DataFrame thing can talk to every other DataFrame thing. And so I'm so excited to have you on today and to hear a bit about your process and the things you're working on.

**Marco Gorelli:** It's been an absolute pleasure. Thanks for having been encouraging about the project when I first showed it to you. I think it makes such a difference when the first person you show something to is encouraging. And for anyone listening, if people show you something, maybe it doesn't hurt to say something positive and encourage people to take it further.

**Michael Chow:** Yeah. Yeah, that's huge. Well, thanks. Yeah, thanks so much for coming on and really excited to see what you do with Narwhals over the next year.

**Marco Gorelli:** Thanks. It's been an absolute blast. And now, if you'll excuse me, I need to go and tune up.

**Michael Chow:** This is it. Celtic folk. Let's go.

**Marco Gorelli:** Thank you.

**Wes McKinney:** Thank you, Marco.

*[Podcast outro]*

The Test Set is a production of Posit PBC, an open-source and enterprise tooling data science software company. This episode was produced in collaboration with Creative Studio AI. For more episodes, visit thetestset.co or find us on your favorite podcast platform.