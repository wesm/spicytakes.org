---
title: "Why do people want to be analytics engineers?"
subtitle: "The job nobody wanted is now the job we can’t get enough of."
date: 2022-07-01T16:20:15+00:00
url: https://benn.substack.com/p/why-do-people-want-to-be-analytics
slug: why-do-people-want-to-be-analytics
word_count: 2181
---


![Marin Headlands — Park Review | Condé Nast Traveler](https://substackcdn.com/image/fetch/$s_!drZo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F90fb384d-f294-407f-83ec-e3d16a98a161_2560x1440.jpeg)

*We live in SF for the nature, right?*


When I started working in data ten years ago, I knew four and only four things.


First, data was everywhere. Publications like theEconomist—required reading for conceited twenty-four year old econ majors, insofar as subscribing to it and piling unread issues on your coffee table counts as reading—routinely published breathlesschartsandarticlesabout how the amount of data in the worlddoubles every two years. Second, all this data could predict the future. Specifically, it could predictwhen your teenage daughter was pregnantbefore you, her parent, knew about it—and this was just the beginning.1Third, theoracles behind these predictionsheld the “sexiest job of the twenty-first century.” In the wake of the Great Recession, banking, consulting, and going to law school were out; learning Chinese and becoming a data scientist was in. Fourth, the reality of being a data scientist didn’t match the image. They spentup to eighty percent of their timecleaning data. The job, it turns out, wasn’t sexy; it was mostly “headaches” and “mundane labor.”


This final number—eighty percent!—was burned in Silicon Valley’s collective brain. Though it mayhave been exaggerated, it captured a deep frustration in the industry: Cleaning data is atedious chorethat prevents data scientists from working on exploration and analysis, the “parts of the job that they enjoy most.” Asone data scientist told theNew York Times, this drudgery got in the way of the “cool, sexy things that got you into the field in the first place.” Internet famous peoplewrote blog postslamenting it. Other internet famous peoplestarted companiesto fix it. And some peoplequit their jobs because of it.


So naturally, ten years later, the newsexiest job of the twenty-first century, the job thatanalysts want to graduate into, is…theanalytics engineer, whose primary responsibilityis cleaning and modeling messy data.


Huh?


Though you could certainly quibble with elements of this narrative—“sexy” could be an cringey label for jobs that are in demand, rather than jobs that are desirable to hold; people might be migrating into analytics engineeringto get paid; analytics engineers do a lot more than just clean data—the broader trend is hard to deny. For years, analysts and data scientists came into the data industry hoping to work on big, strategic problems. This was the game people wanted to play, and cleaning and preparing data was its expensive ante. As Jeff Magnussonwrote in a postthat (somewhat ironically) catalyzed the rise of analytics engineering, “nobody enjoys writing and maintaining data pipelines or ETL. It’s the industry’s ultimate hot potato.”


Today, several dominos down from Jeff’s post,analytics engineering is everywhere. We cut the analyst role down the middle, stuffed all of the historically repellent work into one half—and immediately watched everyone rush towards it. How in the world didthathappen?


# All hype, all substance


One theory is that it’s pure hype. Analytics engineering became a buzzword, and people are chasing the shiny new thing. This seems mostly wrong though; a lot of people are now well educated on what analytics engineers do, and, as best I can tell, that’s led tomoreinterest in the role, not less.


Another theory is that people are drawn to it because it solves a real and meaningful problem. Jason Ganz indirectlymade this argumentlast year. Commenting on the role’s explosive rise, he said that “analytics engineering is agoddamn superpower.” Though I don’t disagree with Jason’s point, I’m skeptical that that’s why people want to become analytics engineers. Not only can analystsbe justas impactful, most people don’t blindly hunt the highest leverage jobs they can find. And even if we did, wouldn’t we have enthusiastically embraced data cleaning and preparation years ago?


In fairness, there’s a potential answer to that last question: We didn’t have the tooling to make data cleaning and modeling scalable. Years ago, we equated these tasks with writing one-off scripts and plodding throughheinous Excel files. Today, modern data tooling—and dbt in particular—makes this work both repeatable and ergonomic. This suggests a third theory as to why analytics engineering is popular: With better tools, we can, following Randy Au’s lead, rebrand data cleaning asbuilding reusable transformations. The problem, in other words, was never the task; it was how we did it.


All together, these theories tell a potentially compelling story. The industry was initially drawn to analytics engineering because it is valuable work; better tools made it less frustrating; as it built momentum, more people were drawn to the hype that surrounded it.


Sounds reasonable—but I think it’s somewhere between incomplete and wrong. To me, the rise of analytics engineering says less about the job, and more about ourselves.


# Color by numbers


This is my wildly speculative and loosely supported theory about what’s happening: A lot of us got into data because we were problem solvers who liked puzzles and weren’t afraid of numbers. We liked thinking creatively, but not like a capital-C Creative; instead, we liked finding interesting paths through structured problems. Don’t give us blank canvas or Word doc; give us a board game, a Lego, a brain teaser, orWordle.


At first glance, these interests seem like the perfect match for a data analyst. Analysis is a kind of numerical puzzle, defined well enough to put us at ease, and open-ended enough to let us be creative in how we approach it. So many of us, especially those of us who weren’t exposed to computer science or software development, decided that analysis was our thing.


But, it turns out, this is only part of the job. We also have to work through a lot of hardsocial and organizational challenges. We get thrown into business domains we don’t understand, and have to work with people who don’t understand our domain. The problems that were supposed to be reasonably structured are actuallyunmitigated messes. And our job isn’t to find the solution to a puzzle, but to make a persuasive argument ontop of shifting definitions of the truth. It’s hard, humbling, chaotic, and bureaucratic. And it’s not, I think, what many of us wanted when we became analysts.


Analytics engineering emerged as our escape.


Though analytics engineers aren’t fully removed from business problems and organizational politics, they’re often protected from its messiest edges. Building crisp models and designing efficient DAGs are tasks with well-defined starting and ending points, and lots of space for creativity in between. For an analyst, a job well done is a more convinced executive, an adjusted decision, and lingering doubt about what stones were left unturned. For an analytics engineer, success is a humming system, a clean codebase, and the satisfying tick of dbt jobs completing in your terminal. Despite telling ourselves that exploration and analysis are the reasons we’re here, I think a lot of us, like more traditional engineers, find a lot of satisfaction in the latter.


# Voting with our feet


Ask people what they like about San Francisco, and many will say, almost automatically, that you can’t beat the nature that surrounds it. Beaches, mountains, state and national parks—it’s all a short drive away.


Does everyone in SF hike through Point Reyes on the weekends? Do they stand-up paddle board to Angel Island? Do they bike on the trails in the Marin Headlands before work? A few do, but most people—including a lot of people who say they love SF “for the nature”—don’t. So why do we say it?


My guess is that it’s a mix of aspiration andmimetic desire.2We often struggle to identify what we want, especiallyin the heady excess and expansive possibility of Silicon Valley. So we end up settling on wanting what everyone else seems to want, without realizing we’re all just chasing each others’ tails.


A lot of analysts do the same. It’s expected of us to say that thefun part of our jobis a hard problem, a clear calendar, and a dataset full of insights waiting to be tapped. When people ask me why I got into analytics, it’s the answer I give.3And when I ask senior data leaders what work they enjoy the most, nearly all of them say that, though they spend most of their time on other jobs responsibilities now, “of course, there’s nothing like getting their hands dirty on some real analysis.”


But if you look at how many of usact, you have to wonder if we mean what we say—or if our supposed affection for analysis is a romanticized, reflexive belief about ourselves that we stopped thinking about critically years ago.


Consider, for example, how long data analysts have been doing data analysis.4Despite the role being formalized decades ago, we still haven’t figured out how to publicly share most of the work that we do. There are no communities where people get together to discuss the “real analysis” that supposedly motivates them.5There aren’t conferences with this as their mandate. For as much as we say we like this part of our job, we don’t talk about it very much.


Contrast this with our response to analytics engineering. The field was practically created by the community, and people’s interest in talking about data tools, data modeling techniques, and the various details of how they do their jobs. These topics dominate Twitter, public Slack conversations, and the emerging constellation of data Substacks6so much that, a few months ago, people had to start tellingustochill.


Yes, there are obstacles to sharing analysis publicly that don’t exist when talking about ETL tools. But if we really wanted to talk with one another about that part of our job—if we were truly motivated to do it—wouldn’t we find a way? There are a handful of folks likeCassie KozyrkovandDavid Robinsonwho built large audiences by figuring this out; yet, much of the data community is reluctant to do the same.


To me, that reveals the real reason behind the industry’s hard tilt towards analytics engineering: Many of us have had a latent interest in engineering, and, more cynically, a lurking dissatisfaction with the messier side of analytical roles. Tools like dbt captured this demand by providing an off-ramp for analysts who were in the wrong role, while injecting just enough engineering flavor into data cleaning and modeling to convert it from an ugly task done in Excel to one that’sattractive to “systems builders”.


On one hand, this is an undeniably positive development. We can’t do much with data without preparing it first. Elevating that task, rather than complaining about it, will surely make us better at doing it. It’s an even better trend for the analysts who’ve become analytics engineers, as many of them were probably chasing a career that they never really wanted.


On the other hand, it suggests we might need to rethink what it means to be an analyst. Though data cleaning may not be eighty percent of our job anymore,7we might not be as enamored with the remaining twenty percent as we thought—particularly the portion that asks us to be more of a politician, lawyer, and therapist than a detective or consultant.


I’m not sure what we should do about that. But I think it starts with all of us pausing next time someone asks us what we like to do, discarding the scripted answer about “finding insights in data,” and thinking about which moments of our jobsmake us genuinely happy. More often than not, I suspect, we’ll find out we know fewer things thanwe thought we did.

[1](https://benn.substack.com/p/why-do-people-want-to-be-analytics#footnote-anchor-1-62062026)

Every movement and ideology has its founding myth. I’m convinced that this article is data science’s: It was powerful, visceral, scary, repeated everywhere—andprobably not true.

[2](https://benn.substack.com/p/why-do-people-want-to-be-analytics#footnote-anchor-2-62062026)

And the tech industry (and itsfaux-intellectual con men)loves it some mimetic desire.

[3](https://benn.substack.com/p/why-do-people-want-to-be-analytics#footnote-anchor-3-62062026)

More specifically, I say that I enjoyed solving analytical problems when I was working at a think tank in DC, but I wanted to beMaKe A rEaL iMpAcT(by, you know, helping rich people better hawk software to other rich people).

[4](https://benn.substack.com/p/why-do-people-want-to-be-analytics#footnote-anchor-4-62062026)

For20,000 years, apparently. Shoutout to the data teams living in Uganda in 18,000 BCE, who were evidently doing morepredictive analyticswith a bone than nine out of ten teams can do in 2022 with pandas, Databricks, and a monthly subscription to theHarvard Business Review.

[5](https://benn.substack.com/p/why-do-people-want-to-be-analytics#footnote-anchor-5-62062026)

People have tried, and nothing stuck. We took a swing at Mode a while back; someone made aHacker News clonefor data (population: crickets);r/DataIsBeautifulhas a lot of members, though I’d argue it’s more of a subreddit for visual fun facts than analytical discussion. Tableau might also claim that they’ve built one, but theircommunity pagesays otherwise: Even under the most generous assumptions, only nine out of eighty topics listed on the page primarily focus on analysis.

[6](https://benn.substack.com/p/why-do-people-want-to-be-analytics#footnote-anchor-6-62062026)

For what it’s worth, this Substack succumbed to the same pull. When I first started it, Iplanned on writing“on data, with data, plus some essays on technology, culture, sports, or politics.” Though some of those topics have made a few cameos, they play bit parts relative rants about data companies and the tools they make.

[7](https://benn.substack.com/p/why-do-people-want-to-be-analytics#footnote-anchor-7-62062026)

It’s funny—ten years ago, we said we’d reduce this percentage by using AI to automatically clean up data. But then we solved the problem by saying, in effect, eh, nvm, what if we just make it someone’s job?
