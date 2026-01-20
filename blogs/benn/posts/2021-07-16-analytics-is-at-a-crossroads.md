---
title: "Analytics is at a crossroads"
subtitle: "The world is full of great analysts. Will we have the courage to go looking for them?"
date: 2021-07-16T17:11:53+00:00
url: https://benn.substack.com/p/analytics-is-at-a-crossroads
slug: analytics-is-at-a-crossroads
word_count: 2063
---


![](https://substackcdn.com/image/fetch/$s_!5tz1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F982c4291-6947-4b84-8af0-897428e4500d_1600x901.jpeg)

*It’s subtle, but see if you can spot the metaphor.*


If my brother Will were to apply for a job as a data analyst in Silicon Valley, he’d get rejected immediately. Nothing on his résumé would get him noticed by a recruiter or by one ofour screening AIs: He has degrees in law and history, not in STEM; he knows his way around Excel, not Python or SQL; he’s an analytical thinker, but not, as defined by the technical parameters of most tech company job listings, an analyst.


And yet, if he wanted such a career, he’d be as good at it as any of us. He’s one of the country’sleading experts on urban demography, a subject more textured and quantitatively complex than nearly any industry concern. He routinely works with government data sources that are messier and more cumbersome than even the most disorganized corporate databases. And despite working for a relatively obscure organization a thousand miles from Washington, DC, he’s earned a place in “the discourse” on politics in America by seeing things other people don’t see and, above all, by writing about those ideas better than just anyone else on the internet.1Given a nuanced problem in need of a discerning eye, an analytical mind, and a persuasive pen for recommending a concrete solution, Will is the perfect person to call. But if that problem is to develop a SaaS pricing strategy rather than measuring school integration—one of which is much easier than the other, by the way—we rarely give people like him that chance.


This is an inexcusable loss. It’s a loss for our industry, which has been complaining about atalent gapfornearly a decade, and has beenignoring gender and racial gapsfor even longer. And it’s a loss for younger versions of Will—early in fragile careers, looking for opportunities, and only finding doors wedged shut by unnecessary technical requirements.


I was reminded of all of this after reading Pedram Navid’sthoughtful responseto Jamie Brandon’sviral list of grievancesabout SQL. Jamie’s original post argued that SQL didn’t meet a number of standards that other modern languages do; consequently, according to Jamie, the entire analytics edifice built on top of SQL is irreparably flawed.


Pedram disagreed on the merits, saying that SQL’s shortcomings were in “parts of the language that almost no one interacts with.” I’m partial to this; nearly ten years into using SQL on a nearly daily basis, and I don’t even understand many of Jamie’s concerns, much less feel frustrated by them. (In Jamie’s defense, ignorance isn’t a sign that all is well. In my defense, ignorance is bliss.)


Pedram’s bigger gripe was with the post’s overall posture, which he saw as contributing to the general perception that analytics is the underdeveloped sidekick to software engineering. Diminishing SQL, particularly its obscure technical quirks, "perpetuates that myth that data analysis is a second-class skill.” To accuseTwilightof being a boorish beach read is to accuseTwihardsof being philistines; to accuse SQL of having foundational technical deficiencies is to accuse analysts of being juvenile engineers.


I see Pedram’s point here as well—but I don’t think he goes far enough. Though he nods at analysts’ curiosity and their ability to communicate, the thrust of his argument is that Jamie misjudges what it means to be technical. Analysts have to spin up databases, manage Docker, get Python environments running, develop testing frameworks, and maintain a fragile Rube Goldberg machine of mismatched internal tools and third-party applications. This may not look like traditional software engineering, he argues, but it’s engineering, it’s hard, and it’s not to be dismissed.


This is true enough, but it sidesteps the more fundamental point:Analytics isn’t primarily technical.While technical skills are useful, they’re not what separate average analysts from great ones. When someone questions if we’re real engineers, we shouldn’t feel the need to pull out our technical credentials. We should instead say, “So what? That’s not our job.”


# Analytics, engineering


Several years ago, as dbt and its philosophies were beginning to infiltrate a growing number of data teams, folks in the data community started describing analytics “as a subfield of software engineering.” I understand the temptation to push these disciplines together: Analytics tools have become more collaborative and code-oriented, and analysts—and especially capital-D “data scientists”—are adopting many of the same paradigms that software engineers pioneered years ago. You can no longer be effective on many data teams without knowing how to version control your code, how to write tests, or the basics of how a Python runtime works.


Positioning analytics inside engineering—or, more broadly, emphasizing the technical aspects of analysts’ work—has real effects. It suggests that great analysts need to be, first and foremost, great engineers. It also outlines a career path into analytics: Learn technical fundamentals, and then specialize. For an aspiring analyst, engineering bootcamps are your med school, and reasoning about data is yourmedical fellowship.


I hate this. In so many ways, I hate this.


First, it’s factually wrong. By and large, the hardest and most important problems analysts work on aren’t technical, or even mathematical. Spinning up a database is frustrating; inferring something about an ambiguous business problem using the data in that database ishard. Building a fancy model to predict churn is complex; reasoning about what makes that model useful and what makes it dangerous ishard. Solving these problems requires curiosity and inductive reasoning, not a CS textbook and a calculator. Given the choice, I’d hire Sherlock Holmes—the antiquated Sherlock Holmes, from the 19th century, a man for whom “technology” means the light bulb—over any present-day MIT engineering PhD.


This gap between theoretical technical problems and real ones was particularly stark last week. Two posts went viral on analytics Twitter:2Jamie’s piece about SQL, and Erik Bernhardsson’sarticle about the organizational and cultural obstaclesthat make building a data team difficult. Jamie’s post kicked off a bunch of grandstanding on Hacker News (and navel-gazing think pieces like this one). Erik’s, by contrast, was met with responses like “It’s so realistic” and “Very relatable” and “This is so spot on” and “OMG - its my life!” By describing analysts as engineers, we’re telling people we want them to solve Jamie’s problems, and then expect them to solve Erik’s—because Erik’s are the problems we really have.


Elevating technical skills also encourages us to not just develop those skills, but to see our value in how well we’re able to apply them. Go down this path far enough, and the issues in Erik’s post become distractions at best, and beneath us at worst.


In some cases, technical skills can even be counterproductive, for the same reason that upper-body strength can actually make inexperienced rock climbers worse. If beginners can muscle their way through simple climbing routes, they don’t develop the technique necessary to complete harder ones. Analysts who are technically and statistically proficient tend to do the same, defaulting to overpowered solutions over more elegant—and ultimately more useful—ones.3


Finally, as Pedram alluded to, framing analysts in technical terms shuts people out of a field they’re otherwise qualified to work in.


I was nearly one such casualty. In 2012, after a six-month job search, I landed my first offer on my fifty-ninth application: a data analyst atYammer. But it wasn’t my résumé that got me the job; it was nepotism. A coworkers’ sister worked at Yammer, and she’d made sure my application made got a careful look. I know that I wouldn’t have gotten the job without a referral because Ididn’tget the job without a referral: I’d actually applied for the same position a few months earlier, and been rejected immediately. Had it not been for one fortunate connection and a hiring manager willing to stake his social capital on an unconventional candidate, my career path would’ve been very different.4


More insidiously, emphasizing the technical elements of the role discourages people—andwomenandpeople of colorin particular—from considering careers in data at all. People who are analytically sharp and quantitatively comfortable are good enough for this job. It makes no difference if they use Vim or know what an incompressive language is. They can learn these things on the job, if they need to learn them at all. Follow our discourse, though, and you’d be forgiven for thinking otherwise.


![](https://substackcdn.com/image/fetch/$s_!KoIo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F63799a65-0f27-4639-a064-c5a7e50c5db8_1230x884.jpeg)

*For those who say it’s a “pipeline problem,” I found you a pipeline. National Center for Education Statistics, Tables322.40,322.50.*


# Analytics engineering


Over the last couple years, the analytics community—led again by dbt Labs—has largely stopped talking about analytics as a flavor of engineering. Instead, we’ve created a new role in the middle: theanalytics engineer. On the whole, this is a useful evolution, and dbt deserves a lot of credit for cultivating the ground from which it’s grown. But this nascent role puts us as a crossroads.


Down one path, analytics engineering becomes the barrier between engineering and analytics. Rather than needing to be animpossible combinationof statistician, developer, and business expert, analysts can simply be great critical thinkers. Rather than looking for people with an advanced degree in a quantitative field, 5 years of experience with Python, familiarity with AWS, and a passion for optimizing the conversion rates of white paper download forms, data teams can enthusiastically hire creative historians, sociologists, and political scientists5who are exceptional communicators rather than mathematicians who are passable coders. With the help and support of analytics engineers, analysts can learn the technical skills they need (just as I did at Yammer), and focus on being the curious puzzle solvers they are.


Down the other path, analytics engineering is the bleed. It’s the conjunction that puts analysts and engineers in the same sentence, creating a continuous spectrum from each role to the next. Analysts, once they become technical enough, “graduate” to becoming analytics engineers. Senior analysts aren’t analytical specialists, but data generalists who can be both analyst and engineer. Though analytics engineering widens what we consider to be technical, technical skills are still the ruler by which we measure ourselves.


I hope we choose the former path—for ourselves and, more importantly, for the versions of my brother who are looking for open doors, and more than capable of doing the work on the other side of ours.


---


As a postscript, I suspect some folks will bristle at the claim that analytics isn’t a technical role. We’ve collectively invested a lot of time into learning technical skills, and this post feels like it dismisses that.


That reaction is fair, but also my point: Why do we feel so insulted when people don’t give us credit for this particular dimension of our job? You can’t be an effective analyst without being able to clearly communicate in emails, written documents, and presentations, but most of us don’t feel a need to be called writers.


On one hand, it makes sense we’d be focused on this ancillary skill over others like writing. Silicon Valley is infatuated with engineers as “creators;” companies talk about searching for the 10x engineer but not the 10x analyst, sales rep, support agent, or even CEO; there’s a non-trivial salary gap between analyst and data scientist. On the other hand, we’ll always play second fiddle to software developers because, for most of us, our primary function isn’t to develop software. Rather than fighting this claim, we should demand that others judge us against a different yardstick. And that starts with judging ourselves in the same way.

[1](https://benn.substack.com/p/analytics-is-at-a-crossroads#footnote-anchor-1-38845231)

For measured, weighty examples, check out hispiecesinThe Atlantic. For unfiltered (and much more frequent) samples, followhim on Twitter.

[2](https://benn.substack.com/p/analytics-is-at-a-crossroads#footnote-anchor-2-38845231)

“Viral” on analytics Twitter is a few dozen likes, a retweet by a VC, and write-ups in two of the six data engineering newsletters.

[3](https://benn.substack.com/p/analytics-is-at-a-crossroads#footnote-anchor-3-38845231)

I’ve personally done this in several ways. After learning d3, I tried to tell every story withover-stylized interactive visualizations. In most cases, simple charts would’ve been better. After learning how to scrape websites, I started trying to collect my own data rather than looking for existing datasets. I wasn’t an analyst, but a man with a chainsaw, intoxicated by its power, hell-bent on cutting something, anything, everythingdown with it.

[4](https://benn.substack.com/p/analytics-is-at-a-crossroads#footnote-anchor-4-38845231)

It’s left to the reader to decide how they feel about this particular point.

[5](https://benn.substack.com/p/analytics-is-at-a-crossroads#footnote-anchor-5-38845231)

Plus, if we hire people with these backgrounds, maybe our leading “thinkers”would stop calling them the easy subjects. Also, Paul, we could do without the subtle suggestion that high-income students’ systemic advantages are just a statistical quirk that you were the first person clever enough to see.
