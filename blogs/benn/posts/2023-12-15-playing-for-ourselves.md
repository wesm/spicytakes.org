---
title: "Playing for ourselves"
subtitle: "A review, of sorts, of 'Who Makes the NBA?,' and what it means for the rest of us."
date: 2023-12-15T18:12:58+00:00
url: https://benn.substack.com/p/playing-for-ourselves
slug: playing-for-ourselves
word_count: 3386
---


![Jusuf Nurkic: Draymond Green needs help, glad he didn't 'choke me'](https://substackcdn.com/image/fetch/$s_!H1pn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06566c12-8cfa-46e1-9fda-23576ad058bc_1024x682.jpeg)

*Draymond Green,team player.*


Google came out when I was in middle school. We were taught how to use it in “Computer Lab,” a once-a-week class in which we mostly learned about Microsoft Office, struggled withTouch Typing for BeginnersandWhere in the World Is Carmen Sandiego?, and tried not to get caught playingJippii mini golf.


The world wide web was coming, our teachers said, and search engines were going to be an important tool for navigating the information superhighway. To make the most of Google and Yahoo, we needed to learn about“advanced” search techniques, using logical operators, range searches, and prefixes like “site:” that would refine our results. These were going to be the critical skills for the information age; learn them, or get left behind.


Thefear mongeringturned out to be half right. Being proficient with Google is clearly an important skill—far more important than my teachers probably anticipated. It’s difficult to imagine being able to function in today’s world, much less in its job market, without having a fair bit of intuition about how to use Google. “Let me Google that for you” wasfunny in 2008; now, it’d be genuinely alarming.


But that expected proficiency has nothing to do with the cheat sheets of boolean operators we were given in 2000. People who aregoodatGoogling1aren’t good because they know that you search for keywords in URLs by using the “allinurl:” prefix; they’re good because they have an instinct for how Google works. They know its quirks, and how to take advantage of them. They are like F1 drivers—their ability doesn’t come from reading the manual, but from having a feel for the machine.


We are having the same moment with AI. Twitter narcissists,2LinkedIn influencers,3and VCs4are warning us that we need toevolve or die. Hundreds of vendors are predicting futures in which everyone needs to buy what they’re selling. And out-of-touch bloggers are soapboxing aboutwhat it all means, andhow our jobs and lives will changebecause of it.


Among this sea of Nineties’ middle school teachers, Seth Stephens-Davidowitz is from the future.


Earlier this week, Stephens-Davidowitz published histhird book,Who Makes the NBA?: Data-Driven Answers to Basketball's Biggest Questions.Like his prior two books,Who Makes the NBA?attempts to put numbers to a bunch of interesting questions about how the world actually works. In hisfirst book, he analyzed Google search data5to figure out what people are really thinking, and if it matches what they say; in his new book, he tried to find patterns that explain who plays in the NBA, and who excels there.


But unlike his prior two books, each of which took about three years to write,Who Makes the NBA?was written in thirty days. After playing around with OpenAI’s ChatGPT andData Analysis(which wasformerlyknown asCode Interpreter),6Stephens-Davidowitz didn’t writearamblingblogpostaboutwhatitallmeant, ortalkaboutthetools; he stepped into the arena. Given how quickly he found he could clean, munge, and analyze data with ChatGPT, he gave himself a challenge: Use it towrite a book in thirty days.


He did, kinda. The book is brief—it’s a breezy two-hour read, about a third of which is an appendix about his AI-powered research process.7ReadingWho Makes the NBA?felt less like reading a book, and more like reading a loose collection of FiveThirtyEight (RIP) and Deadspin (RIP) blog posts.8


But for those of us who work in data, that’s exactly what makes the book worth paying close attention to (and paying for; it’s ten dollars;go buy it). Instead of working like a novelist or an academic to writeWho Makes the NBA?, Stephens-Davidowitz worked like one of us: Against a tight deadline, worried more about directional correctness than scientific rigor, and responsible for not just producing his analysis but also presenting it. Every chapter ofWho Makes the NBA?is roughly the same as a report we might deliver on some strategic corporate question. If we want to understand what our jobs might look like in several years,Who Makes the NBA?is the best answer we have yet.


# The practical section on what we all need to learn


The biggest conclusion—for better or for worse, I suppose—is that AI is a long way from replacing us. When instructing ChatGPT to do its works, Stephens-Davidowitz found that “clarity and precision are paramount” and “any ambiguity can lead to unintended consequences.” This suggests that, at least when doing open-ended analysis on new datasets,9it’s important to be analytically fluent. ChatGPT can port theTidyversefrom R toEnglish—but it still needs to be talked to using the vocabulary of the Tidyverse.


Furthermore, Stephens-Davidowitz said that ChatGPT struggled with mildly complex analyses, and was loose in its statistical computations: “Handling more complex aspects of regressions, such as dealing with standard errors, may not be as robust.”


None of this is terribly surprising; these sorts of shortcomings are well-documented at this point. As Iwrote earlier this year—and as Andrej Karpahty, one of OpenAI’s leading researchers, saidin a recent tweet—the randomness inherent in LLMs make them undisciplined order-takers. Instead, I though, we should treat them like creative but unruly prima donnas:


> One of the most striking things about LLMs is that they’re much better at the creative parts of analysis than they are at the mechanical parts. Ask ChatGPT to write a SQL query against an artificially simple schema; it’s a junior analyst, at best. But ask it to come up with possible hypotheses to explain why there’s some anomaly in a metric, and it does better than I would. …I’m not sure that I want to say that all the query-writing chatbots should pivot into analytical reasoning bots.That’s the job I want, to be at the top of the creative food chain with an army of machines doing the mundane tedium below me. But the army we’re building—creative, unpredictable, and equally prone to both novel ideas and lies—is becomingmore man than machine. If we’re looking for chatbots that make us all better at working with data, without having to rebuild an entire BI tool in the process, our best option may be to let them do the jobwewanted to do all along.


Not yet, apparently. In an interview, Stephens-Davidowitzwas askedabout exactly this. Did he ever use ChatGPT “as a collaborator to help drive his own hypothesis formation?” He said he tried, but it never worked.


For example, he gave ChatGPT a list of countries and the number of NBA players they produced per capita, and asked it to tell him what the countries at the top of the list have in common. It said nothing useful. ChatGPT’s “current capabilities in correlating [its] extensive knowledge to generate new theories or uncover complex patterns were limited.” Moreover, one of the book’s most interesting findings—that most seven-footers in the NBA aren’t particularly gifted athletes—was recommended by one of Stephens-Davidowitz’s Twitter followers, not ChatGPT.


In the end, most of the value that Stephens-Davidowitz got from ChatGPT was in accelerating the mundane and tedious tasks of cleaning and blending data, and in quickly cycling through dozens of regressions and pivots of those datasets. It wasn’t a second brain; it was several dozen extra pairs of hands.From another interview:


> AI, for me, just eliminates all the parts of my job or work process that I hate. I hate cleaning datasets, merging datasets. … It does all of that for you and frees you to be creative and ask the questions.


Stephens-Davidowitz did find at least one novel application though. In trying to determine the relationship between the difficulty of a player’s upbringing and their performance in the NBA, he asked ChatGPT to “objectively rate the childhood difficulty of each NBA player on a scale from 1 to 10.” Notably, he didn’t provide any biographical data to ChatGPT to do this; he just asked it to use what it already knew about the players. Though that feels like a particularly fraught issue to score in this way—players’ biographies come from sources like Wikipedia, and those pages are surely biased in all sorts of ways—it partially confirms that LLMs can almost be treated like adatabase of unstructured textthat can be summarized, queried, and manipulated directly.


So what do all of us need to learn? The answer, it seems, is nothing in particular. We just need to start using tools like ChatGPT, and, as we all did with Google, develop an intuition for how they work. Though Stephens-Davidowitz lists a number of specific tips and tricks in the book’s appendix, he ultimately concluded that the best way to make the most of ChatGPT is just to “practice with it.”


# The blustery section on What It All Means


Practice enough, and you can write a book in thirty days. But can you write agoodbook? This is where things get weird.


My initial answer is, not really? The analytical substance ofWho Makes the NBA?felt rushed and incomplete. Stephens-Davidowitz posed a number of questions, offered some circumstantial answers, and quickly moved on to the next topic. Its conclusions feel more like curious gimmicks than actual results, and I came away sometimes skeptical and rarely satisfied.10None of this was true forEverybody Lies; after reading that book, I felt convinced of most of what Stephens-Davidowitz had said.


But if I’m honest with myself, that certainty didn’t come from his analytical arguments; it came from the context around them. I readEverybody Liesin a hardcover, with an imprint from HarperCollins and a foreword by aprominent academic.11The book’s arguments were neatly tied together in a crisp narrative. It had impressive testimonials, had been featuredon various morning shows, and was aNew York Timesbestseller.


Who Makes the NBA?, by contrast, was self-published hours after its completion. The book was short; its narrative was clunky; its charts were visually mismatched. When I bought it, the only customer review wasfrom Stephens-Davidowitz’s mom.12


Obviously, these differences are to be expected, when one book was written over three years and one was an experiment written in thirty days. My point here is not to criticizeWho Makes the NBA?; my point is that analytical workis very hard to judge on its merits alone.


Give us a chart with a startling conclusion, and we don’t judge it based on the math that’s underneath it; we judge it based onhow compelling the story is around it. We judge it based on how others seem to be judging it. We judge it based on the anecdotes and personal experiences that confirm it.


More subtlety, we also judge it based on effort that went into creating it, and what I’ve previously called “foundational legitimacy.” Stephens-Davidowitz spent three years writingEverybody Lies; I assumed its conclusions must’ve been rigorously tested. And Stephens-Davidowitz, as a human being and not an all-powerful supercomputer that can find correlations on command, had to develop his theories and find evidence to support them on his own. As I said a year ago, “yes, we cantorture data to make it say anything—but making it confess a lie takes a lot more effort than getting it to tell the truth.”


That’s what’s most jarring about readingWho Makes the NBA?—it break both of these assumptions too. People have spent lifetimes looking for better ways to measure the talent of NBA players, and for hidden signals that predict which draft prospects will become All-Stars. After thirty days of work, in a book that was set to be published before any of its discoveries had been made, Stephens-Davidowitz proposed new and novel answers.


Are they right? It would be kind of wild if they were! But they might be! I don’t know! And without looking for external signals, I don’t knowhowto know!


Of course, it doesn’t matter if I ever know; no NBA team is asking me to rank their draft boards. But as I mentioned before, the work inWho Makes the NBA?is pretty similar to the sort of work that analysts create inside of companies, and people do ask me to create or assess that work. Though I like to think that I judge it based on its merits, I probably judge it the same way I judge books likeWho Makes the NBA?—on how good its narrative is, on how roughly reasonable its math looks, on how much effort I think someone put into hardening it, and on the foundational legitimacy that comes from the fact that the report only exists because someone had to figure out how to put it together.


IfWho Makes the NBA?is a glimpse into the future, all of this may be going away. Analyses that used to take days and weeks will take minutes and hours. Even if LLMs can’t manufacture our results for us, as they couldn’t for Stephens-Davidowitz, they’ll let us ask far more questions, and help us find more potentially interesting—and potentially spurious—conclusions. And bots will wrap our work withwhatever narrative we tell them too. How will we judgethatwork?


It won’t be easy. Case in point: Even Stephens-Davidowitz needed external signals when judging his own work. At one point when he was writingWho Makes the NBA?, he created a new metric for measuring coaches, andfound that Warriors’ coach Steve Kerr was more valuable than LeBron James. The claim went viral on Twitter, people found the unconventional argument unconvincing, and Stephens-Davidowitz changed the metric for the book’s final version.


Every analyst who’s ever had to work quickly should sympathize with this. If not for other people’s reactions, how do you know if your result is crazy? The numbers add up; the reasoning makes sense. Analysis isn’t an irrefutable science, but a kind ofquantitative logical argument. Some ideas make more sense than others, but until we test them—assuming we even can—we won’t know ifthe rock actually floats or not.


---


InWho Makes the NBA?,Stephens-Davidowitz says that NBA players are trapped by bad incentives. On one hand, their pay and popularity is mostly based on how many points they score. On the other hand, their teams’ benefit the most from players who areefficientscorers. Taking lots of bad shots is good for players, but bad for teams.


AI may create the same sort of problem for analysts. As both an analyst and a hack on the internet, I want to find results with clever punchlines. I likely benefit more by saying something startling than I do by saying something that is right. The brilliant analyses that perfectly predict when the sun will rise tomorrow get no press, because it’s expected. The bold and exciting claims get the clicks.


Today, we can only make those claims when we piece them together ourselves. But just as Google made it possible tofindan argument for anything, I suspect AI will eventually make it possible tocreatean argument for anything. And if people struggle to judge them on their own merits, it will take a lot of discipline for us to promote what we think is right—to play the team sport—rather than what gets attention.


---


# The fun section about the NBA


Of course, you don’t have to readWho Makes the NBA?so that you can write some tiresome meta-commentary about it; you can also read it because it’s a fun book about the NBA. Despite me sticking these questions in a lazy list at the bottom of this post, these are the topicsthat I’m really here to talk about:

1. The single-most surprising point in the book was footnote 26: “The average player increases his free throw percentage by about 0.1 percentage points each year of his career.” Anecdotally, it seems like most players are much better shooters, from the field and the free-throw line, in the NBA than they were in college. (E.g.,StephCurryandChrisPaulboth shoot three percentage points higher;AnthonyDavisandJoelEmbiidboth improved by about ten percentage points.) Are those anecdotes abnormal? Do most players have a kind of natural ceiling to their free-throw shooting abilities, and they can hit it pretty quickly on an NBA training schedule? What is going on?
2. In the chapter on identifying good draft prospects, Stephens-Davidowitz says that a few teams regularly overperform. He then proposes a few unconventional predictors of how successful a college player will be in the NBA, including a player’s hand size, how high they can jump from a standing start, and if they were a highly recruited coming out of high school. Do successful teams use or overweight these metrics in their evaluations? Do the players they draft perform highly on these scales? I doubt that Popwill say muchabout his proprietary trading algorithms, but can they be reverse engineered?
3. He argues that one of the strongest predictors of how many NBA players a country produces is population height. That makes sense—but it seems like thepercentageof people who are tall matters less than thetotal numberof people who are tall. Though China may not produce as many seven-footers per capita as Latvia, its population is almost 1000 times bigger. Given howpopular the NBA is in China, why hasn’t there been an explosion of Chinese big men?
4. One of the most unsettling points in the book is about talent discovery. In the chapter about players’ national origins, he points out that nearly all of the NBA’s guards come from countries in which basketball is very popular. If you’re from a country in which basketball isn’t popular, you’ll probably never discover your basketball talent unless you’re so tall that everyone tells you to play it. AsStephens-Davidowitz said in an interview, this could be extended well beyond basketball. There are a million things we could all be doing, and we could be world-class at a few of them. But most of us will never find them. Sleep well with that thought.
5. Stephens-Davidowitz proposes a new metric for measuring the height-adjusted talent of an NBA player. The idea is to remove their “unearned” ability, and rank them by what’s left. Could you not do the same thing for cognitive ability? It’s long struck me as somewhat odd that people who are tall (or good-looking, or whatever) have their success discounted because of their genetic luck, but people who are smart are seen as fully earning theirs. I guess that would be uncomfortable for the IQ absolutists, who prefer to live in their contradictory world in which intelligence is as genetic (which is often a euphemism for racial) as height and looks, but it’s only the tall and athleticChadswho have an unfair advantage.

[1](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-1-139817807)

For millennials, Googling is the ultimate Dunning-Kruger bait. I’m convinced that if you asked a hundred 33-year olds if they were better than the average person their age at Googling,ninetyof them would say yes.

[2](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-2-139817807)

“If you found this thread helpful, join 30,000+ other learners by subscribing to my newsletter for more insights like these!”

[3](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-3-139817807)

“I’m offering a one-time discount on my new two-week course on how to boost your personal productivity with AI to anyone who shares this post!”

[4](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-4-139817807)

[ Post disclosing their investment in the company they’re promoting not found. ]

[5](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-5-139817807)

Stephens-Davidowitz is probably very good at Googling. Not only did he literally write a book about it, but he was also a data scientist at Google.

[6](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-6-139817807)

Because using Data Analysis as a noun makes me flinch, I’m going to refer to all of these tools—ChatGPT, Data Analysis, and its former versions of Code Interpreter—as ChatGPT.

[7](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-7-139817807)

One very important note: He used ChatGPT for research and analysis, not to write the book’s text. As he said, its writing was too stale and formulaic, on par with agood eighth grade essay. He did say that ChatGPT proved to be a very capable copy editor, though.

[8](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-8-139817807)

To be clear, this isn’t a criticism; this was the point. He was racing to see how far he could go in a set amount of time.

[9](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-9-139817807)

As opposed to, say, exploring the pre-defined paths created by a semantic model and a BI tool.

[10](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-10-139817807)

To reiterate, this isn’t a criticism of the book, or of Stephens-Davidowitz. The whole point of the experiment was to see what was possible in thirty days, not to see how long it took to write a book as good asEverybody Lies.

[11](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-11-139817807)

A prominent academic who, notably, isn’t afraid to shoot down pop science heroes. Pinkeronce saidthat Malcom Gladwell is “a minor genius who unwittingly demonstrates the hazards of statistical reasoning and who occasionally blunders into spectacular failures.”

[12](https://benn.substack.com/p/playing-for-ourselves#footnote-anchor-12-139817807)

Tyler Cowen also reviewed it in avery short blog post. Cowen said it was “quite good,” though he also had several follow-up questions.
