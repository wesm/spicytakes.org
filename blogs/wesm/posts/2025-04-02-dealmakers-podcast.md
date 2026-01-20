---
title: "Raising $110 Million for Open-Source Data Analytics"
summary: "Video at DealMakers Podcast"
date: 2025-04-02T00:00:00
tags: ["video", "transcript"]
slug: dealmakers-podcast
word_count: 5203
source_file: transcripts/2025-04-02-dealmakers-podcast.md
content_type: transcript
event: "DealMakers Podcast"
video_url: "https://www.youtube.com/watch?v=6Ji4wyBhlRM"
---

{{< video https://www.youtube.com/watch?v=6Ji4wyBhlRM >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this interview with Alejandro Cremades on the DealMakers podcast, I discuss my journey from math competitions to creating pandas, founding multiple companies, and now investing in data infrastructure startups through Composed Ventures.

### Background

My dad was in the newspaper business, so we moved around—Knoxville, Tennessee and Northeast Ohio. I graduated from a suburb of Akron called Cuyahoga Falls, then went to MIT to study math. I enjoyed math competitions in high school and did well at state and national levels, though I never reached the USA Math Olympiad. In college, I realized I wasn't going to become the greatest mathematician and should find something more applied.

### Creating pandas at AQR

I started building Python code in 2008 at AQR—"a little miniature research framework for myself so I could do my work faster." It was a skunkworks project, not sanctioned by management. I showed up one day having rebuilt pieces of fund infrastructure in Python. Leadership gave me people to work with, and they ultimately decided to use Python to rebuild future models. Now AQR—and much of finance—runs on Python.

In 2009, I pitched open-sourcing the core IP, now known as pandas. It took about six months to convince everyone and get lawyers on board. I argued it would serve as advertisement—smart programmers could come to AQR to work on tools like pandas. External contributors would make it better. "It required a leap of faith on everyone's part, but in the fullness of time, it's been a good decision."

### Datapad and the First Exit

I started a PhD in statistics at Duke but kept getting contacted by people who'd seen pandas. I dropped out to work full-time on open source with small contracts to pay rent. With colleagues from AQR, we explored a financial analytics framework but found it difficult to sell to hedge funds at startup-viable prices.

Chang She and I founded Datapad, a Python-powered business analytics company. We raised a seed round from Accel in early 2013 and moved from New York to San Francisco. After two years, facing an ultra-crowded BI market with companies like Looker taking attention, we decided to find the right home for the team. We ran a tight M&A process with four offers and chose Cloudera because we wanted to continue making impact in open-source data science.

### Apache Arrow and Two Sigma

At Cloudera, we created Apache Arrow, a data connectivity and acceleration framework. After about six months, I realized Cloudera wasn't the best place for this work. Two Sigma hired me to work on Arrow full-time. Other companies—NVIDIA, Bloomberg—wanted to commit capital to Arrow development. Rather than join another company, I created a nonprofit industry consortium to combine those commitments.

### Founding Voltron Data

By 2020, Neil Richardson and I had built conviction it was time to found a company. We'd built Ursa Labs inside RStudio (now Posit), which served as our startup incubator. In August 2020, during COVID, we raised our initial round led by Google Ventures and Walden.

At the end of 2020, I started talking with Josh Patterson from NVIDIA's RAPIDS team. We created a "super company" bringing together Ursa Computing, BlazingSQL, and RAPIDS concepts. By end of 2021, we'd raised $110 million in a Series A.

### Stepping Back

We went from 35 to 130 people in about a year. But the economic environment shifted—interest rates rose, capital became harder to raise. The company focused on GPU-accelerated data workloads. I felt my impact had been in building the underlying core technology and getting the company started. I wanted to spend time on a broader portfolio of projects and investing, without feeling guilty about taking energy from the startup.

### Investing Philosophy

I've done over 40 angel investments focused on data infrastructure, data science, accelerated computing, and developer tools. I prefer working with technical founders, especially technical CEOs. My thesis centers on the "composable data stack"—enabling data systems to become more modular and interoperable.

When meeting founders, I look for the right way of thinking—being able to visualize what the future might look like—combined with ability to execute. "The joke among venture investors is always to try to skate where the puck is going."

### Advice for Founders

"Know yourself—your strengths—and be really mindful in choosing who to work with." Choose people you're in sync with on values and communication, and who can fill gaps in your skill set. Working relationships are long-term things. "Being a reliable person of integrity—someone who's helpful and upstanding, consistently—that bears dividends."

---

## Key Quotes

> "It was totally a skunkworks project. It wasn't really sanctioned, authorized, or planned by company management." — Wes McKinney, on creating pandas at AQR

> "It required a leap of faith on everyone's part, but I think in the fullness of time, it's been a good decision." — Wes McKinney, on open-sourcing pandas

> "Without pandas and the other projects that happened at the same time, it's unclear that Python would be where it is today as the number-one language of AI and data science." — Wes McKinney

> "The big lesson was that, first, I needed to collect evidence that there was a need in the market—that there was a product to be created and that a startup was actually needed. Not just to found a startup for the sake of it, but because there was a real opportunity." — Wes McKinney, on founding Voltron Data

> "Having been through that the first time at a small scale with Datapad, I was familiar with the emotional burden you carry as a founder, and the toll that process takes on you." — Wes McKinney

> "I think it's important to know yourself—your strengths—and to be really mindful in choosing who to work with." — Wes McKinney

> "Working relationships are long-term things. You might work with someone for a period of time, and they might pop up again. You might be able to help them, or they might be helpful to you in some way." — Wes McKinney

> "Being a reliable person of integrity—someone who's helpful and upstanding, consistently—that bears dividends." — Wes McKinney

> "The joke—or the saying—among venture investors is always to try to skate where the puck is going." — Wes McKinney

> "Sometimes we stumble into things and we find our passion. I'm okay with how things ended up." — Wes McKinney

---

## Transcript

**Alejandro Cremades:** All right, everyone, thank you so much for tuning into The Dealmaker Show. Today we have an amazing guest. He's a founder—a repeat founder—a founder that has had exits. His last company also raised quite a bit of money. We're going to be talking about open sourcing, knowing when it's the right time to turn the page and move on to the next chapter, as well as managing relationships, building, scaling, and financing—all the things we like to hear. So without further ado, let's welcome our guest today, Wes McKinney. Welcome to the show.

**Wes McKinney:** Thanks for having me.

**Alejandro Cremades:** So Wes, originally born near Philadelphia, but you did travel quite a bit. Give us a walk down memory lane. How was life growing up for you?

**Wes McKinney:** Yeah, well, my dad was in the newspaper business. He was managing newspapers, so we moved around a fair bit growing up. I have no memory of the Philadelphia area, but I was born there. When I was a year old, we moved to Knoxville, Tennessee. I spent about half my childhood in Knoxville and the other half in Northeast Ohio. I graduated from high school in Akron, Ohio—a little suburb of Akron called Cuyahoga Falls. Then I left the Midwest, went to MIT, and studied math. Initially, I was interested in becoming a mathematician or doing something more academic. I had a passing interest in computers and computer programming, but I didn't realize that my future career would lie in computer programming, data science, and entrepreneurship. But sometimes we stumble into things and we find our passion. I'm okay with how things ended up.

**Alejandro Cremades:** How did you develop that love for math? How did you get into math?

**Wes McKinney:** It was pretty self-driven. I think I enjoyed the structured aspect of problem-solving and abstract thinking. Being able to solve more and more difficult problems, building up a stack of tools that fit together and enable you to think through these really complex or abstract problems.

When I was in high school, I started doing math competitions. I went to a high school that did have a math team, but it was a little bit self-organized by the students. There was a teacher who helped facilitate, but we didn't have a lot of formal instruction or former mathletes to help teach us.

So I went down the rabbit hole of doing math competitions. I did pretty well at the state and national level in high school, but I never reached the USA Math Olympiad or the International Math Olympiad or anything like that. But that was kind of my interest in math at the time.

I'd done a little bit with computers, but high school for me was basically math, a little bit of computers, and foreign languages. When I got to college, I pretty quickly realized that I wasn't going to become the greatest mathematician. I figured I should find something more practical to apply myself to—something that could have more impact in the world, something less abstract, more applied and tangible in terms of having a real effect outside of the esoteric world of theoretical mathematics.

**Alejandro Cremades:** Let's talk about how you got into finance after college and joined AQR. One thing you did there that may be quite interesting to our listeners is open sourcing IP from a financial firm. That sounds like quite the challenge.

**Wes McKinney:** Yeah, it wasn't easy. I started building a body of Python code in 2008, basically building a little miniature research framework for myself at AQR so I could do my work faster, be more productive, and be better at my job. It was also an experiment to learn Python programming and try to use Python for data analysis. I found that I really enjoyed building tools for working with data and also for other people. But it was totally a skunkworks project.

It wasn't really sanctioned, authorized, or planned by company management.

I think I showed up one day and had rebuilt a number of pieces of fund infrastructure in Python just so I could do research. I found a couple of champions in leadership who said, "This seems really interesting. We should give him a couple of people to work with—a little more room to focus on this and see if it could be a viable path for the future of the company." They ultimately decided to use Python to rebuild and build the future models that run the business. Now, I believe AQR—along with a lot of the financial industry—runs on Python based on those core principles from 15, 17, 18 years ago.

In 2009, after working on this for about a year, I started making the pitch about open sourcing some of the core IP, which was the data analysis framework that's now known as the pandas project. It's now a very popular Python data science library for working with data.

I'd say it took probably six months to convince everyone and get all the lawyers on board, figure out the licensing, and make sure it wasn't going to create liability for the company or give away our secret sauce or competitive edge.

But I think I made the argument convincingly that it would mostly serve as an advertisement for the fund—that smart programmers could come to AQR and work on tools like pandas and use Python.

Also, people outside the company would contribute to the project and make it better, and we would reap the benefits of the external open-source community.

It required a leap of faith on everyone's part, but I think in the fullness of time, it's been a good decision. It helped catalyze the growth of the Python data science ecosystem. pandas, along with a number of other projects that came about during that era, all fit together to create a really productive environment for doing data analysis and data science work.

Without pandas and the other projects that happened at the same time, it's unclear that Python would be where it is today as the number-one language of AI and data science.

At a certain point, Google, Meta (formerly Facebook), and other companies piled on and chose Python as the language for building their AI frameworks. Now all of the LLMs and AI frameworks are built in Python. It's definitely a big change from 20 years ago, when people were questioning whether Python was a safe language for building real software.

**Alejandro Cremades:** Now in your case, you go from there into thinking that maybe a PhD is your next chapter, but then you drop out and really enter the world of entrepreneurship. How did that happen?

**Wes McKinney:** I started a PhD in statistics at Duke because I wanted to develop a better academic and applied foundation for doing data science work.

But while I was in grad school, I started getting pinged by folks who had seen pandas and one of my first conference talks, which was about using Python for quantitative finance.

I saw there was a lot of interest in using Python for real industry work. I said to myself, "I can't stay in grad school and not have this be my primary focus." So I took a leave from grad school, ultimately dropped out, and went back to New York to work full-time on open source. I had a couple of small contracts to help pay my rent, but it was really an exploration—just to see how far down the well goes, so to speak.

I got a couple of my colleagues from AQR to join me and start exploring entrepreneurial ideas. Initially, we were interested in building a financial analytics framework based in Python, but we found it was going to be pretty difficult to get hedge funds and other financial institutions to buy it—at least at a price that would make sense for a startup. So we ultimately decided not to pursue that route.

Adam Klein and Chang She—Chang and I ultimately decided to found a different company called Datapad, which was more of a business analytics, business intelligence company, all Python-powered.

We raised a seed round from Accel in early 2013. We decided that building the company in San Francisco was the best move, so we relocated from New York to SF at the beginning of 2013 and built the company in the heart of SOMA.

**Alejandro Cremades:** That's amazing. Now with Datapad being a venture-backed business, what I want to ask—and I think this will be really impactful for founders listening—is: how do you think about exiting well? In the case of Datapad, how did you guys think about it? When did you realize it was the right time? Walk us through that process.

**Wes McKinney:** We worked on the company for about two years before we exited in an acqui-hire type deal to Cloudera at the end of 2014.

After we raised our seed round, we hired a small team and were really heads down building the product and working with some initial design partners to get feedback.

But in the broader context of the time, we were in a really crowded space. Even though we were building a business analytics product that featured Python and Python extensibility at its core, we were classified in the business intelligence space—which was super crowded. There were some really successful companies founded around that time, like Looker, that were taking up all the attention of the venture community.

When we went to raise our Series A round in 2014, we saw pretty quickly that we were facing an uphill battle in terms of differentiating ourselves and succeeding in this ultra-crowded market.

At a certain point, we were contemplating a bridge round of financing, and we decided it would be better to find the right home for the team—a place where we could exit well. As co-founders, we wanted to end up in a place where we could get good jobs for as many people on the team as we could. We entertained a number of offers—I think we ultimately had four different offers to exit. So we ran a pretty tight M&A process, and it came together really quickly.

But we ended up choosing Cloudera because we knew we were passionate about data infrastructure and open-source software. We decided we wanted to be in a place that valued those things, where we could continue to make an impact in the space of open-source data science and data infrastructure.

**Alejandro Cremades:** Talking about open source and ecosystems—I know after Cloudera, you spent a bit of time there. But after the integration, you went on to work at Two Sigma, and from there it all matured into what became Voltron Data, your next company. What events needed to happen for you to feel really good and comfortable with the thought of doing it again?

**Wes McKinney:** Yeah, it was a bit of a winding journey from the exit to Cloudera in 2014 to founding Voltron Data in 2020.

Initially, while I was at Cloudera, a group of other open-source developers and I created a new open-source project called Apache Arrow, which was a new data connectivity and data acceleration framework. So we focused on building that project. After about six months or so, I realized that Cloudera was not going to be the best place to continue that work.

Two Sigma got in touch with me because they had seen the early Arrow work. They offered to hire me to work on Arrow, and I thought, "This sounds great." After a very productive couple of years being full-time at Two Sigma, there were a bunch of other companies interested in committing capital to fund Arrow development. That included NVIDIA and some other financial firms like Bloomberg.

I thought, "Well, I'm not going to leave Two Sigma and go join NVIDIA or some other company"—although it probably would have been a good short-term financial decision to join NVIDIA in 2016 or 2018. So instead, I created a kind of nonprofit industry consortium to combine all those capital commitments into one place so we could continue working on the project without necessarily founding a for-profit company.

It took a long time for me to convince myself there was even a business to be created around Arrow. The big lesson was that, first, I needed to collect evidence that there was a need in the market—that there was a product to be created and that a startup was actually needed. Not just to found a startup for the sake of it, but because there was a real opportunity.

I also needed to feel conviction about going down the startup path, because startups are really difficult. It's a lot of work. It involves managing a lot of relationships—with investors, with your team—you're carrying a lot of weight on your shoulders. Having been through that the first time at a small scale with Datapad, I was familiar with the emotional burden you carry as a founder, and the toll that process takes on you.

But by 2020, just as the impact of Arrow was snowballing, Neil Richardson and I—who were leading Ursa Labs—had built up the conviction that it was time to found a company.

We had built Ursa Labs inside RStudio (now called Posit), the data science platform company. In effect, they were our startup incubator. We set up a separate entity for all the committed funds to support the development work. The operational side—healthcare, benefits, all that—was managed by RStudio (Posit).

In 2020, in the middle of COVID while we were all quarantining at home, we decided to spin out of Posit to create a startup. We raised our initial round of venture capital, led by Google Ventures (GV) and Walden, in August 2020.

So we were off to the races.

**Alejandro Cremades:** So obviously that became Voltron Data. For the people listening, to really get it—what ended up being the business model of Voltron Data?

**Wes McKinney:** Yeah, so just to briefly explain how we went from Ursa Labs to Ursa Computing to Voltron Data: We raised the seed round for Ursa Computing, which was the startup spun out of Ursa Labs.

At the end of the year, I started talking with Josh Patterson, who led the RAPIDS team at NVIDIA. RAPIDS was a GPU acceleration framework for analytics at NVIDIA. They were interested in founding a company. Another startup called BlazingSQL had been working closely with the RAPIDS team to build a GPU-accelerated data engine.

We had business ideas we were pursuing at Ursa Computing around enterprise support for Apache Arrow and improving and accelerating enterprise data connectivity.

Pretty quickly, ideas started to percolate to create a "super company" that could bring all these concepts together. During that time, we also spent more time talking with Lip-Bu Tan and his fund, Walden. Lip-Bu is now the CEO of Intel.

They were really keen—if we could bring all these folks together—there was a lot of appetite to bring significant capital to the table to build an accelerated computing company around all of our ideas.

We were able to do that at the beginning of 2021. There was a bit of "sausage making" involved in reorganizing the company to make sure everybody had equity stakes they were happy with and to get the rounds of funding done.

By the end of 2021, we had a Series A in the works to bring our total capital raised to $110 million.

So we were suddenly operating on a scale of business that was an order—or probably two orders—of magnitude greater than what I had been involved with before at Datapad, which was a small seed round a decade earlier.

**Alejandro Cremades:** So you said a Series A of $110 million? That's quite a lot of money for a Series A.

**Wes McKinney:** It is, yeah. I mean, it was the first—well, it's funny these days. What you call a Series Seed versus a Series A—those lines are blurry. But we called it a Series A because it reflected, first, the stage of the business. We were definitely a Series A company in terms of where we were at in the development timeline.

But also, the level of ambition of the business—to build an accelerator-native, multi-hardware, distributed execution engine. To support the development and growth of the Arrow ecosystem. To do enterprise support. And to partner with other vendors to become more Arrow-native.

We were tackling a very ambitious space. So I think the $110 million Series A also reflected the scale, scope, and ambition of the business.

**Alejandro Cremades:** I guess for you guys, that was quite the ride, quite the journey. At what point do you realize it might be time to turn the page? How do you go about that as a founder—especially as the founder of such a fantastic and meaningful operation?

**Wes McKinney:** Yeah. Well, in 2021, when we initially put the company together, we were around 30–35 people.

We went from 35 people to 130 in about a year—definitely some pretty intense blitzscaling. We also had a large founding team, and fairly diverse in terms of the different product directions we were pursuing.

The big thing that changed between when we founded the company and when I decided to step out of my full-time operational role—well, there were a number of things.

First, the economic environment in 2021 was very different from the environment at the end of 2022. Interest rates went up a lot. Capital became a lot harder to raise.

We had to make a conscious decision as a company to really focus on narrower verticals in our product strategy. We had to place fewer bets but focus on areas where we could be really successful.

The area the company chose to focus on was large-scale, GPU-accelerated data workloads.

For me, there were a number of directions I was interested in pursuing within the company that we just couldn't fit into our short-term product strategy.

We had built an amazing team to work on the GPU-accelerated side of the business. And increasingly, I felt that the impact I had brought to the business was in building the underlying core technology—Apache Arrow—and helping catalyze the creation of these frameworks we were using to build the company's products.

Getting the company started, raising money, building the leadership team, building the engineering team.

But I felt the desire to spend my time on a broader portfolio of projects. I had started investing more actively and wanted to be able to spend more time doing that—without feeling guilty about taking energy away from my startup.

So there were a bunch of factors that led me to feel that it was best for me to not be in a full-time operational role so I could spend more time investing, spend more time working with other founders on projects that are based on the Arrow ecosystem. As I saw that there were lots of new companies being founded in and around Arrow.

**Alejandro Cremades:** Well, let's talk about that. Why don't we double-click on that, Wes? Because on the investment side, you've done 40 investments. I mean, you've done 40 angel investments. Now you've got the venture fund going too. I guess as part of these investments and working with founders—when you've done over 40—you develop pattern recognition to see what works and what doesn't, right? When it comes to investing in founders.

What would you say are the three key ingredients that you see repeating from those founders that tend to be the ones with more chances of succeeding?

**Wes McKinney:** Yeah. I mean, the investments I've made have been focused on data infrastructure, data science, accelerated computing, and developer tools more generally. I've tended to prefer working with deep tech companies or founding teams that are technical. Since I'm a technical founder, I enjoy working with other technical founders—especially technical CEOs.

Especially as we created the Arrow project in 2015–2016, a few years later, more and more companies started using Arrow and related technologies as part of their core technology platform.

So I said to myself, "Well, if companies are going to use this technology, I'd like to be involved and be as helpful as I can to these companies." I initially started angel investing as a way to be involved and participate in the success of entrepreneur friends of mine. They would start companies, and I'd say, "Hey, could I invest in your company?" And they would let me.

But now it's become a little more structured. I'm thinking about broader technology trends and theses. One of the core ideas is this notion of the composable data stack—enabling data systems and data infrastructure to become more modular, composable, and interoperable. That's one of the central ideas of Arrow.

I think about older legacy systems and how we could rebuild those systems in a way that incorporates principles of modularity, composability, and interoperability.

So in terms of investments, if I meet founders who have the right stuff—the technical background, the ability to execute—but who are also operating on a similar intellectual wavelength, where they perceive what's wrong with the prior generations of technologies and have an idea of what they can make better…

I think it's about the right way of thinking—being able to visualize what the future might look like with their contributions through their companies—and combining that with the ability to execute.

When I meet with founders, I'm really trying to recognize those attributes. I'm looking at people's track records, what they've done in the past.

The joke—or the saying—among venture investors is always to try to skate where the puck is going.

**Alejandro Cremades:** Yeah, no kidding. Now, imagine if I could bring you back in time. Let's say I bring you back to that moment when you were working at AQR and thinking about maybe starting something of your own.

And you had the opportunity to have a chat with that younger Wes and give him one piece of advice before launching a company. What would that be, and why, given what you know now?

**Wes McKinney:** I think it's important to know yourself—your strengths—and to be really mindful in choosing who to work with.

Firstly, choose to work with people you're in sync with in terms of values and how you think about operating day to day, how you communicate. Also look for people who can fill in the gaps in your skill set. Because realistically, you can't be great at everything.

And so being honest with yourself about what you're good at, what you're not good at—you can grow and improve, of course—but you need to seek out people who are really good in those areas, who can bring the whole picture into balance.

Something I've learned—and I think I've always felt this way, but more so as time has gone on—is that working relationships are long-term things. You might work with someone for a period of time, and they might pop up again. You might be able to help them, or they might be helpful to you in some way.

So I think being a reliable person of integrity—someone who's helpful and upstanding, consistently—a useful person over time… I think that bears dividends.

Investing in relationships, being a reliable person that people value—that's worth a lot. And you never know when the time and effort you've spent helping someone, or being useful in your role in the past, is going to show up later and pay dividends.

**Alejandro Cremades:** That's so profound. I love it. For the people who are listening and would love to reach out and say hi, what's the best way for them to do so?

**Wes McKinney:** You can reach out on LinkedIn. I'm here and there—I try not to spend a lot of time on social media. I guess these days, LinkedIn is basically social media.

I do have a Twitter/X account—less and less active there. I'm also on Blue Sky. I think on Twitter/X, I'm Wes McKinney.

On Blue Sky, I think I'm my domain name—wesmckinney.com. I've blogged, and I have a blog and a Python book, Python for Data Analysis. You can read that on my blog. I haven't been writing as much lately, but whenever inspiration strikes and I have something to say, I do enjoy writing here and there.

**Alejandro Cremades:** Amazing. Well, Wes, thank you so much for being on The Dealmaker Show today. It has been an absolute honor to have you with us.

**Wes McKinney:** Thanks again for having me. It's great.