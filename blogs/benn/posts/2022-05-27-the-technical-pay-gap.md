---
title: "The technical pay gap"
subtitle: "The culture we build is the culture we buy."
date: 2022-05-27T16:26:54+00:00
url: https://benn.substack.com/p/the-technical-pay-gap
slug: the-technical-pay-gap
word_count: 1721
---


![The 'real' Rosie the Riveter dies at 96 | CNN](https://substackcdn.com/image/fetch/$s_!Fe7K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F73e3a09d-0e1f-4567-98ee-11438c36556c_1200x675.jpeg)


If you ask ten data organizations what titles they use on their teams, you’ll get eleven different answers. Some teams call everyone data analysts; some teams call them all data scientists. Some teams have data analysts, data scientists, and data engineers. Some now have analytics engineers andmachine learning engineers. Some preferBI developers.Some calldata analysts data scientists, and data scientists research scientists. Some havebusiness analysts, orbusiness data analysts, ordata business analysts. Some putdata scientists on analytics teams, and some putanalysts on data science teams. And some just give, mash it all together into a Russian nesting doll, and call it adata science analyst/engineer.1


Thismangled Venn diagramof disputed boundaries and overlapping responsibilities makes it very hard to figure out what people’s jobs are. It makes it even harder to figure out what they should get paid.


Though job titles can sometimes seem like little more than an aesthetic (in)convenience, they serve an important financial function. When companies create pay scales and salary bands for different roles, those bands are typically benchmarked against industry standards for that title. For example, when a company wants to figure out what it should pay a senior data analyst, it often starts by asking what the market pays senior data analysts, and adjusts from there.


Without a clear consensus on titles—if there’s no commonly accepted definition for what a data analyst is—this entire exercise happens on very unstable ground. This is bad for teams, who want to match roles with the right candidates. It’s bad for companies, who want to fairly compensate their employees. And it’s bad for job seekers, especially those new to the industry, who are trying to figure out which skills to acquire and how much they should be paid for doing so.


No blog post is going to fix this. Even in the simplest of cases, compensation is a frighteningly complicated subject; a few hundred words on the subject is a pathetically shallow attempt to swim in very deep water.2


However, we can’t stay out of that water entirely—especially not right now. The last few years have been a whirlwind for the data industry, with the introduction of hundreds of new tools, dozens of new responsibilities, and several new roles. If we don’t talk about pay—because it’s complicated, because it’s taboo, or because we assume it’ll just sort itself out—pay bands and industry habits will settle along the samebiasedlinesthat they always have. We shouldn’t waste this opportunity to outline something better.


# Unequal pay for unequal work


To followErica LouieandMichael Kaminsky, both of whom rightly led us into this water last week, I have one principal hope for how these salary norms develop: Analysts and analytics engineers shouldnotbe paid the same.


Generally speaking, the two roles do different things, and one tends to be more complex than the other. Analytics engineers are responsible for maintaining ELT pipelines, writing a lot of SQL in dbt, architecting a DAG and authoring tests, and keeping a close eye on Snowflake bills. They also have to work with non-data folks to translate their semantic understanding of the business into tables and metrics that accurately reflect that definition.


Analysts, by contrast, often embed themselves alongside non-technical teams, turn ambiguous, qualitative problems into quantitative ones, build dashboards (reluctantly), do in-depth analyses (excitedly, supposedly), and try to influence decision makers with their work. They work in tools like dbt as well, though they’re typically more concerned about the logical details in individual models than the overall cleanliness of the DAG.


These sets of responsibilities require different skills, some of which are much harder to acquire and hone than others. We should pay people accordingly—and, therefore, analysts should make more than analytics engineers.


Wait, what?


It’s telling, I think, that this feels like a radical proposal. Even suggesting it feels like a troll, a hot take, a cheap controversy for some clicks. Whenever we talk about the relative pay of analysts and analytics engineers, there seem to be two options: They get paid the same, or analytics engineers get paid more. I’ve never actually heard anyone suggest that it’s analysts, in fact, who do the more valuable, harder, higher-skilled work.


But you could easily make the case that they do! People in both roles need to know SQL, probably to an equal degree. Python is helpful, though not entirely necessary. The two roles live in similar tools, and both have to work closely with other people at the company to understand their business needs.


There are a couple places where the roles diverge. Analytics engineers, who need to be comfortable with git and know their way around the command line, are marginally more technical than analysts. This isn’t a huge technical leap though, and many analysts have a passing familiarity with these tools.


For their part, analysts are often engaged in more “soft” issues. They have to identify which business challenges are most pressing, figure out how to solve squishy, shape-shifting problems, and package their conclusions into persuasive narratives, all while navigating their stakeholders’ organizational politics. It’smessy,uncomfortable, and—at least in my experience—far harder than git.


Case in point: The Analytics Engineering Club offersa thirty- to forty-hour courseto help analysts learn the skills necessary to become an analytics engineer. It would take far more than a week’s worth of work to train a data engineer to become an even passing analyst.3


If analytics engineering skills aren’t harder to acquire, why do we generally assume that, if anyone’s to be paid more, it’s the analytics engineer? Why, until writing an entire (now ripped up) draft of this post, did I not even consider the possibility of the reverse?


# New rules


One explanation is that analytics engineering is a new role, so it’s a supply problem; salaries will come down, at least relative to analysts, as the field cools.4That seems possible, especially given thecurrent hypearound the role.


Another explanation is that the job is viewed as tedious or dull, and higher pay is necessary to attract people into it. Unlikely; if anything, analytics engineering has areputation for the opposite.


A third possibility is that analytics engineers are a subset of analysts. They have to have the same skills, and then some. While that may be true in some companies, it’s atypical. Thetweet that promptedErica’s original thread suggests the roles are overlapping, but not concentric.


Do analytics engineers produce more valuable work than analysts? Maybe, though this is immensely difficult to measure. Moreover, most people’s assumption that analytics engineers should get paid as much as analysts seems to be rooted in their gut reaction to the comparison, not in a careful study of which role’s nebulous output creates more shareholder value.5


To me, the most plausible explanation is a simpler one: Silicon Valley overvalues technical skills. For several reasons—some with understandable origins, some withdeeply sexist ones—the industry puts inherent and unquestioning value on being able to write code. If you can do it, you get paid more, full stop. Engineers are unimpeachable; those who architect HR policies or write effective marketing copy are replaceable.6


Within the data industry, we’re affected by the same gravity. Analytics engineering, through its name and its gesturing in the direction of data engineering, paints itself with a thin technical veneer. In Silicon Valley, that type of touch up—the sort that lets you rebrand yourself as a “systems thinker,”7as a shape rotator and not a wordcel—comes with a raise.


I don’t think this is a good thing. The work analysts do, especially the non-technical, interpersonal parts, is valuable and exhausting. If the natural tilt of Silicon Valley encourages us to pay analytics engineers more, we’ll pull analysts, including those who are uniquely talented inthatrole, to move into a different one for higher pay and more prestige.


Given the choice, I’d rather the hill slope the other way. I’d rather overvalue analysts. People who are great at working on uncertain questions, digging for tough answers, and fighting to make sure others hear them are fewer and farther between than people who’d rather cancel their Zoom meetings to write code. If a wide net is needed to find the best“above replacement”talent, it’s needed for analysts.


By paying analysts more, we can also break down some of the historic rot that has denigrated “feminine” soft skills. The data industry can signal that, no, we don’t blindly pay for technical ability, nor do we use gendered credentials as proxies to figure out if you’re smart. Instead, we pay you to work with people; to communicate; to influence; to understand and listen and support.


The data community has made commendable (though imperfect) progress in welcoming more diverse members into its ranks. That’s a form of winning, but, if we build a cultural hierarchy that’s organized by technical talent, we won’t rewrite the sexist rules that govern the game. So here’s tocounting off some new rules, and paying analysts more.

[1](https://benn.substack.com/p/the-technical-pay-gap#footnote-anchor-1-56820702)

I would’ve preferred they go with the turducken approach, and called this datalsciengineer.

[2](https://benn.substack.com/p/the-technical-pay-gap#footnote-anchor-2-56820702)

So deep thatpeople can win Nobel prizesfor devoting their lives to studying one aspect of it.

[3](https://benn.substack.com/p/the-technical-pay-gap#footnote-anchor-3-56820702)

To be clear, this isn’t an indictment of the Analytics Engineering Club, which appears to cover the major topics it needs to cover. It’s a measure of the relatively short distance from analyst to analytics engineer.

[4](https://benn.substack.com/p/the-technical-pay-gap#footnote-anchor-4-56820702)

For context, according toGlassdoorandComparably, data analysts in the Bay Area make an average of about $100,000 a year, compared to $110,000 for analytics engineers.

[5](https://benn.substack.com/p/the-technical-pay-gap#footnote-anchor-5-56820702)

Put another way, if we want to claim that analytics engineers produce more valuable work than analysts, we have to actually make that claim. What work do the two produce, and why is the former’s more valuable?

[6](https://benn.substack.com/p/the-technical-pay-gap#footnote-anchor-6-56820702)

Spend an afternoon on Hacker News, and you can’t help but wonder how many engineers assume nobody can do their jobs, but they can do everyone else’s.

[7](https://benn.substack.com/p/the-technical-pay-gap#footnote-anchor-7-56820702)

When recruiters design hiring programs, they think about how outreach sequences, interview panels, and closing processes all interact. When marketers run campaigns, they think about the relationship between branding, segmentation, product offerings, and marketing content. When sales reps work accounts, they balance complex political dynamics across champions, decision makers, budget holders, and deal approvers. Self-proclaimed systems thinkers aren’t unique because they think in systems; they’re unique because they think they’re smarter than everyone else for doing so.
