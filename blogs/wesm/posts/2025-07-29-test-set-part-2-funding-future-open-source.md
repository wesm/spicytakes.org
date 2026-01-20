---
title: "Funding the Future of Open Source"
summary: "Podcast at The Test Set (Posit)"
date: 2025-07-29T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-part-2-funding-future-open-source
word_count: 4604
source_file: transcripts/2025-07-29-test-set-part-2-funding-future-open-source.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://posit.co/thetestset/episode/wes-mckinney-part-2-open-source-sustainability/"
---

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In part two of this conversation on The Test Set, Michael Chow and Wes McKinney dive into the complex world of funding open source, the role of the Apache Software Foundation, working on Positron's data viewer, and even some metal music recommendations.

### Funding Open Source

Wes reflects on the challenges of funding open source development. Coming from finance, he knew that firms historically weren't keen to fund work that might benefit competitors. Beyond making the business case for adopting software, the next level—direct funding—involves "boring problems around budgeting and accounting." With Apache Arrow being more resource-intensive than pandas, Wes embraced the role of "developer evangelist" to convince companies both technically and financially.

### Finding Maverick Investors

Early Arrow development was funded by companies like Two Sigma, who were willing to take risks on experimental technology. "People have this idea that a lot of open source projects succeed on single passionate developer working nights and weekends, squirreled away in the attic, but the reality is that it takes corporate resources—it takes a village."

### The Apache Software Foundation

The ASF provides a neutral home for corporate contributors, offering legal protections, trademark management, and a governance model based on openness. The key rule: you can't make decisions in private. "All communications have to be public," creating a level playing field where competitors can collaborate. The ASF motto is "community over code"—emphasizing how you communicate and treat each other over pure technical output.

### Positron and the Data Viewer

At Posit, Wes has been working on Positron, a new polyglot data science IDE built on VS Code. A major focus has been the data explorer component—enabling users to peek at data frames with smooth infinite scroll (horizontally and vertically), live updates while coding, sparklines, and summary statistics. "What do I want if I have data frames in memory? What do I want a data explorer to do?" The viewer also provides instant preview of data files like Parquet, powered by DuckDB.

### Metal Music Corner

Wes shares his appreciation for symphonic and power metal—Dream Theater, Nightwish, Sabaton, and Dragon Force. He enjoys the technical execution and crowd energy at live shows. But for coding music, he needs something more chill: "music without lyrics"—movie soundtracks and video game soundtracks work well as coding background music.

---

## Key Quotes

> "The whole funding open source is a really complex question... the person who wants to fund the project, they want to fund the project, but they have to convince the powers that be to allocate budget to do the work." — Wes McKinney

> "You're asking people to take a leap of faith, and so you have to identify people who have that maverick type innovator personality that are willing to take a risk, that they're willing to try something new, and they hope that it succeeds, but they're willing to fail." — Wes McKinney

> "People have this idea that a lot of open source projects succeed on single passionate developer working nights and weekends, squirreled away in the attic, but the reality is that it takes corporate resources—it takes a village." — Wes McKinney

> "In the ASF, the rule is that you can't have—you can't make decisions in private, or in backroom discussions. If you want to make a decision, you have to have the discussion openly and in public in a way where everybody can participate." — Wes McKinney

> "'Community over code' is the motto of the ASF—this sort of community first mindset of how you communicate, how you make decisions, how you treat each other." — Wes McKinney

> "There's no project dictator, benevolent dictator for life—there's no explicit hierarchy within a project. If you have commit access to a project, your commit access cannot be taken away." — Wes McKinney

> "How can we build tools that could help maybe tear down the language walls and some of the language wars?" — Wes McKinney

> "I imagined myself like, what do I want if I have data frames in memory? What do I want a data viewer, a data explorer component to do? So we set about to try to build that thing." — Wes McKinney

> "Now we have LLMs and LLMs also need to be able to look at data. They need to be able to look at a lot of data and context windows are only so big." — Wes McKinney

---

## Transcript

**Michael Chow:** Welcome to the test set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field. This episode is part two of a conversation with Wes McKinney, open source software developer, author, metalhead, and principal architect at Posit. I'm Michael Chow, thanks for joining us.

I do feel like that's a theme that comes up too in a lot of your work and what you talk about—the funding side, like how do we get people into this position? And I think a lot of really interesting things you've said have also highlighted what gets attention and what doesn't.

**Wes McKinney:** Well, the whole funding open source is a really complex question. I came initially from the finance world, and historically folks from financial firms were not so keen to release open source software, and maybe even less keen to fund work that might benefit their competitors.

So I recognize that a big part of being a successful open source developer is building a business case—why people should adopt the software, and why people should contribute to it. But then the next level beyond that is direct funding, and that often is even more complicated in part because of boring problems around budgeting and accounting and things like that. Because the person who wants to fund the project, they want to fund the project, but they have to convince the powers that be to allocate budget to do the work.

I recognize that particularly with Arrow, because Arrow was a project that was much more resource intensive than pandas, and it also needed to have broad buy-in from a lot of sectors of business. I had to essentially embrace this role of being like developer evangelist or chief marketing officer for the project to convince—

**Michael Chow:** You mean like, why should you fund Arrow, and how to?

**Wes McKinney:** Yeah, well there's the technical persuasion of convincing people that this is—you have an approach to solving a problem that is the right one, and that they, that it is also solving a problem that they have, and that they should consider adopting your experimental brand new technology, which not that many other people use.

You're asking people to take a leap of faith, and so you have to identify people who have that maverick type innovator personality that are willing to take a risk, that they're willing to try something new, and they hope that it succeeds, but they're willing to fail.

As an example, early on in Arrow, I connected with folks at Two Sigma, and they were like, we're really excited about this, and so we spent a bunch of time together, and they were willing to put their money where their mouth is, and put significant resources behind me to work on the project.

People have this idea that a lot of open source projects succeed on single passionate developer working nights and weekends, squirreled away in the attic, but the reality is that it takes—you know, corporate resources—it takes a village essentially. I couldn't have done most of what I've achieved without the support of people believing in the different visions and experiments that I've run, some of which have succeeded, and not everything has been successful.

**Michael Chow:** How did—I'm so curious how Apache factored in, too. I never—so I know the name Apache, and obviously a lot of the Apache projects, but I'm curious what were the benefits you saw in the strategy?

**Wes McKinney:** The Apache Software Foundation, or the ASF—it's one of the best known open source foundations. They provide a home for open source projects, they provide developer infrastructure, legal protections, they manage trademark and copyright and that sort of thing, code licensing.

They were started in the 1990s, when the world of open source was very different. Linux was only a few years old at that time, and everyone was freaked out about getting sued by Oracle, or Sun, or whoever were the major players in that day, because open source was just—as a thing, the free software movement, it was still very new.

**Michael Chow:** Yeah.

**Wes McKinney:** And as the ASF evolved, it has become essentially a neutral home for open source projects that have corporate contributors, that are looking to establish a neutral, Switzerland-like neutral ground for governance, so that contributors can develop the project in a way that is open and transparent, and to try to, at least as much as possible, mitigate some of their conflicts of interest.

When a company is looking to develop a project, but to give up enough control where maybe even their direct competitors can join as contributors—you don't want to be looking around and say, what's your motivation, or what are you hiding, what's going on in these backroom discussions?

So in the ASF, the rule is that you can't have—you can't make decisions in private, or in backroom discussions. If you want to make a decision, you have to have the discussion openly and in public in a way where everybody can participate. This helps level the playing field.

But it also helps people who maybe don't work at your company—it gives them visibility into how you're thinking, what you're doing, why you're doing it, and gives them a way to also get involved. As a way to build community, I think the ASF has played a pretty important role.

**Michael Chow:** It sounds like Apache really establishes a place for companies or competitors to kind of trust open source in an interesting way. Whereas I guess I've often as an open source developer thought mostly about the licensing. It's interesting to hear all the other factors.

**Wes McKinney:** Yeah, so ASF is a combination of a permissive license that's corporate friendly. The Apache 2.0 license includes do whatever you like with the software, but also don't sue us and don't get software patents and then sue us over the software patents. So it has protections for all of those things to make the corporate pointy haired lawyers happy that their bases are covered with respect to IP.

But yeah, beyond the licensing, there's just this community—"community over code" is the motto of the ASF—this sort of community first mindset of how you communicate, how you make decisions, how you treat each other, having a code of conduct, being respectful.

But how you treat each other is also—you treat people with respect in terms of you don't just show up and try to steamroll a pull request or say, I'm the authority on this matter and this is the way that I think it should be done. You actually have to argue from first principles why your approach to the problem is the right one. There's no project dictator, benevolent dictator for life—there's no explicit hierarchy within a project. If you have commit access to a project, your commit access cannot be taken away.

So it's a very egalitarian and I think pretty successful model that other projects that aren't necessarily in the ASF for whatever reason have strived to emulate. But I had almost no exposure to this way of working in open source until circa 2015 when I ended up at Cloudera.

That was interesting because it was a combination of seeing how ASF projects work, but then also exposure to big enterprise software because I had lots of colleagues at Cloudera who had worked for VMware or for Google or Meta, Microsoft—worked for all these big tech companies. Having come from the finance world, which software engineering wise is a little bit more of the wild west, coming to more of this highly enterprise corporate software engineering culture—it was very eye opening. That definitely helped me become a better software engineer, or at least thinking about how to build larger software projects and enable them to scale in a way that's more healthy.

**Michael Chow:** What kind of stuff are you up to now? I know a little bit about your stuff on the Positron team that I'm curious to hear about.

**Wes McKinney:** Yeah. I know you're up to a lot more. Well, it was just around the time that I was learning about the ASF and we decided to start the Arrow project—that's when I first got involved with Posit.

I'd known Hadley Wickham for several years and Hadley just happened to be in town the month that we were launching Arrow. And I was really excited about it. Oh, we're starting this new thing. And the idea is to have portable interoperable data frames.

So we spent a day together and brainstormed—what could we do with this that could be useful for the data science community? We decided to create a small file format called Feather. So that was my first concrete collaboration with Hadley.

I think that was pretty successful, but it also helped demonstrate the potential of sharing—the potential of sharing technology between, across the language fences. We're like, how can we build tools that could help maybe tear down the language walls and some of the language wars?

That kind of sent me down this path of just thinking a lot about how to build tools and systems that empower polyglot teams and polyglot development. I've spent the better part of a decade working on the Arrow project, which has been all about building composable, modular, interoperable technologies that can be used interchangeably across programming languages, and that can be mixed and matched to build different types of data processing systems.

I was catching up with JJ Allaire, founder of Posit, and the Posit team. I was like, what's new at Posit? And they said, oh, we're building a new polyglot data science IDE called Positron. This was in 2023. It was all under NDA—you can't talk about this.

I found the idea of taking everything that Posit (formerly RStudio) had learned about building an amazing data science user experience in an IDE form factor—code first, code editor, console, variables pane, plots pane—and re-imagining that within the context of the modern programming landscape, which is very dominated by VS Code and the VS Code extension ecosystem.

At that point, Positron had been developed privately for a year and a half or so. The prospect of getting involved in that and also getting involved in Posit's Python strategy more broadly really appealed to me.

Posit had been RStudio and had been focused on R programming, had rebranded to Posit, added Python support to all of its products, started making significant contributions in the Python landscape—

**Michael Chow:** And hired you.

**Wes McKinney:** Sure. Yeah. Starting new projects as well as bringing some of the goodness from the R world into the Python world—Shiny, Great Tables, lots of good stuff.

I never imagined myself working on an IDE, but I found some things in Positron—for example, building a modern data viewer, a data explorer component. I imagined myself like, what do I want if I have data frames in memory? What do I want a data viewer, a data explorer component to do?

So we set about to try to build that thing and it's still early, but it's already a very useful thing that I enjoy using on a nearly daily basis. Just as a decision on data viewer—

**Michael Chow:** If I'm understanding, it's basically like if I'm doing data analysis, I have a data frame, a really common activity I want to do is just peek at it and interact and kind of see what I've got. Is that right? So a data viewer is a really fast glimpse into your data that you can filter and—

**Wes McKinney:** So as we initially brainstormed on it—because RStudio has a data viewer component. When you have a data frame loaded up in RStudio, you can click on the data frame in the variables pane and it will pop open this data viewer window. It has some basic filtering capabilities, some search capabilities.

We started from that place where like, well, we'd like to essentially have table stakes, deliver what exists in RStudio, but also the sky's the limit. What else can we build? What have we always dreamed of having?

For me, so often I found myself looking at the data while I'm writing code to clean it and manipulate it. I wanted to have the thing that I could apply selective filters or I could sort or I could search, but that would live update while I'm writing code and modifying the data set. I wanted that live update experience.

I want something that has really smooth, infinite scroll, both horizontally and vertically. I've often found myself with these massive 10,000 column or 100,000 column data sets. I'm like, why can't we have a data explorer that is infinitely scrollable horizontally and vertically?

**Michael Chow:** I like that you just get to—

**Wes McKinney:** Yeah, so we built that thing. And of course, seeing some of the innovations that have come out of the business intelligence world, having things like sparklines, summary statistics, being able to have the statistical visualizations just immediately available.

I think we were really influenced by—I'm a big fan of this tool called Rill Data. So it's Mike Driscoll's latest company, powered by DuckDB.

But I also want really basic stuff like, when you're in data, if you're in VS Code and you have a data file, shouldn't you be able to just open the data file and look at it? I wanted that instant preview experience. So we use DuckDB to build that. Now you can just click on a Parquet file and it opens and everything works. If it's a really big Parquet file, it may not be instantaneous, but it's really snappy.

I'm proud of what we built and it's a nice feeling to cross over, to build something that's at the intersection of backend engineering—because there's clearly a lot of, you need to have knowledge of the internals of how pandas works and how Polars works and R data frames and how DuckDB works—to create this thing that you can deliver that snappy kind of intuitive thing, something that's easy to use, but also is fast.

**Michael Chow:** Yeah, that's cool.

**Wes McKinney:** But now having something that I just know is there and I can pick up and use whenever I have data files is really nice.

**Michael Chow:** Yeah, that's cool. It is funny. I do feel like data viewers—in the abstract, it's such a funny concept where you're like, it's a grid, I can scroll it a lot. It's got my data. I feel like it's one of those things where—well, like working on tables, how to display tables—I feel like tables seem like a really bizarre thing to focus on, but when it hits, it really hits. As it turns out, it's a real load bearing thing.

**Wes McKinney:** We spend a lot of time looking at data. And now I think what's interesting is that now we have LLMs and LLMs also need to be able to look at data. They need to be able to look at a lot of data and context windows are only so big. It may not be practical to take the whole data frame and stuff it in a context window.

Clearly, the focus of Positron and this data explorer is empowering humans to be able to get the information that you need quickly and intuitively and for it to be fast and not get in your way. But then also as time goes on, we have to think about the role of how we expose information about data sets to the LLMs so that they also can—if they're empowering you to ask more questions, that they can get the information they need to give you high quality suggestions.

That's something I've been thinking about, and I'm sure any data tool, any data analysis environment is going to be asking themselves similar questions.

**Michael Chow:** I'm also so curious with the data viewer and stuff, what your day looks like. What's the breakdown of how often are you hands on keyboard coding versus emailing people or nudging communities? What's your day breakdown?

**Wes McKinney:** Yeah, so basically I've been working on Positron lately and since I work closely with folks who specialize in front end development—sometimes I find myself bottlenecked on, I need help from somebody who knows front end better than I do. Or if I try to do the front end portion I'll make a mess.

So it's a good ebb and flow in that I might have a week where I work mostly on Positron and have ten pull requests or something, and then a week where maybe I'm at a conference or joining customer calls or doing presentations.

Actually, I think one of the great things about being back at Posit is having more input from real data science users—learning from people who are using open source data science in a business setting. Because I've been so heads down just working on open source projects—I was full time at a startup up until a year and a half ago, so I didn't have a lot of time to interview people working on enterprise data science teams to learn about what their big problems are. So that's been really interesting.

I do spend a portion of my time investing—I have a small venture fund which basically started out as an extension of the angel investing that I was already doing. But it also helps me be Posit's eyes and ears in the broader market and understand where technology trends are going, what new companies are doing, what can we learn from, what should we do differently, are there opportunities, things that we should be doing that we're not doing. So that's been interesting as well.

I do not aspire to be a full time venture investor. People are asking me that all the time—I was just at a conference last week, they're like Wes, you're a VC now. I'm like no, no, I'm at best a super angel. My hope is—especially I've really focused on working with companies that are directly involved in areas that I care about, like data infrastructure, developer tools, open source, things relating to open source data science and now some of the crossover into the AI landscape.

I'm hoping and helping—picking companies to work with that they're building stuff or they're engaging with communities that I care about and that helps enrich the whole, make the whole pie bigger for everyone.

**Michael Chow:** I like that—not looking to do it full time. In a way I feel like you're like, I simply like code and organize and do this, it's like maybe the more intense version.

**Wes McKinney:** Right, yeah, it's essentially another lever in the community development sort of toolbox in a sense. If you work with a company—I've been an advisor, I'm an advisor for Lance DB for example, which is Chang's new company. He co-founded Lance DB with Lei from Cloudera. They're building vector database and a file format for multimodal machine learning AI workloads.

That's like the perfect example of—they're using Arrow, they're using Data Fusion, which came out of the Arrow ecosystem. So their success is the success of the Arrow ecosystem, and that benefits the data science world more broadly.

**Michael Chow:** I'm so curious to ask you, because I know last year we were both in Charleston and we went to a metal bar. And in fact someone in a review called it a relatively new metal bar that hadn't gotten its patina, its metal bar patina.

I remember asking who listened to metal and we had one very obviously metal co-worker, and I feel like you really surprised us by coming out of the woodwork. I figured this is our chance for you to maybe tell the people about your—what do you love, what's hot, what's not in metal for you?

**Wes McKinney:** Well, I definitely have wide ranging and at times eclectic music tastes, but I do enjoy—when I was in college, I had a number of friends who were big metal heads and they introduced me to symphonic and power metal.

Recently, the last metal show I saw was Dream Theater. They played Nashville—it was awesome—the second time that I've seen them. I wouldn't say I listen to too much metal these days. Maybe when I ran the half marathon in San Francisco several years ago, my playlist was mostly metal and I think it really helped.

**Michael Chow:** I could see it really pushing you out.

**Wes McKinney:** I really enjoy the concerts, especially the live concerts, because I think the crowd energy is amazing. But also I appreciate the technical execution—the playing is just incredible. Everything—the singers, the drummers, all of the guitar and bass—they put on really technically impressive shows.

**Michael Chow:** And power metal's pretty epic and fancy. Dragon Force is the one a lot of people—is that the?

**Wes McKinney:** Yeah, they're kind of the most over the top, but I do like Dragon Force. I saw them once in concert, it was pretty insane.

A band that I really liked was Sabaton. They're Swedish, they do a lot of war themed music, but it's all just a crowd energy thing. I didn't even know them—I went to see them in San Francisco with a former colleague from Cloudera and I was there to see Nightwish, which is a famous symphonic metal band from Finland. It's been around since the late 90s.

Sabaton was the opener and I realized pretty quickly, oh, everyone's here to see Sabaton, they're not here to see the main show. And we were also blown away by the opener that by the time Nightwish was still great—they're always great—but it was almost a little bit of a letdown.

Anyway, so my fellow metal heads, yeah, keep it real.

**Michael Chow:** And I guess my last question is, are you ever like, Positron Data Viewer, Sabaton, let's go?

**Wes McKinney:** I find that for coding music, it needs to be a little more chill. I do like having something on in the background, but I got to listen to music without lyrics, I found. But music like movie soundtracks and soundtracks to video games have been pretty successful coding background music. But that's just—it varies by the day and my mood and whatnot.

**Michael Chow:** Oh yeah, I love it. Well Wes, thanks so much for chatting. I mean, we're co-hosts, so.

The Test Set is a production of Posit PBC, an open source and enterprise tooling data science software company. This episode was produced in collaboration with branding and design agency, Agi. For more episodes, visit thetestset.co, or find us on your favorite podcast platform.