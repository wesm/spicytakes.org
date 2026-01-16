---
title: "Does data quality matter?"
subtitle: "Garbage in; whatever, it’s fine."
date: 2024-11-22T16:59:10+00:00
url: https://benn.substack.com/p/does-data-quality-matter
slug: does-data-quality-matter
word_count: 2265
---


![The Weeknd Joins Travis Scott For Four Songs In Australia - SPIN](https://substackcdn.com/image/fetch/$s_!k1cO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff86c4a41-b8c6-43f7-a0c4-4843c0c641a5_1668x1112.jpeg)


An obvious thing that often happens is that, whenever the world changes in some significant way, companies will say that it is very good for them, actually. In 2020, when the Covid shut everything down, lots of software businesses said stuff like, “in these trying times, collaborative task management software is more critical than ever.” When the economy took off in 2021, and investors on Wall Street and Silicon Valley put a huge premium on growth, those same companies said that “collaborative task management software will make sure your team can ship their transformative new initiatives as fast as possible.” Then, after thegood times diedin 2023, they said “inyears of efficiency, collaborative task management software helps you do more with less.”


Of course, some of these might be true, but they can’tallbe true. If low interest rates and a booming stock market are the ideal circumstances for buying collaborative task management software, high interest rates and a stagnant stock market can’t also be the best time to buy collaborative task management software. But, collaborative task management software vendors will always want to sell you collaborative task management software, so they will always tell you that there’s never been a better time to buy it. And it’s usually not too hard to come up with a plausible reason why thing X is good for situation Y, for just about any X and Y you can think of.1


Sometimes these reasons sound more compelling than others. “Ah ha,” a company that sold a business intelligence application might’ve said in 2022, “analytics software is valuable when you need to find ways to grow quickly, but being data-driven is even more critical when you’re optimizing your margins to be more profitable.” Sounds right;was wrong.


Anyway, now, that new thing is AI. "In the age of AI," every CEO says on LinkedIn née content marketer says in a corporate blog née billboard says in an actual overt advertisement, "you’ll get left behind if you don’t buy our stuff.” Recruiting services, a new CRM, a data streaming platform, a vaguely scammy online writing class—all of it is more urgent than ever, according to the people who sell recruiting services, new CRMs, data streaming platforms, and vaguely scammy online writing classes.


Most of the time, we don’t think about this much, because the motivations are so transparent. Of courseMicrosoft would saythat Azure’s new unified application platform is exactly what businesses need to “harness the full potential of AI efficiently and effectively.”2It would be weird if they didn’t say that.


But sometimes, we don’t think about these sorts of pitches because they seem so transparentlytrue. One of those claims—made not just by vendors, but also often present in more ostensibly objective blog posts and presentation preambles, and treated as obvious and indisputable—is that data quality is becoming more important than ever. In the age of AI, the story goes, the companies with the best models will win; the best models will be built on the best data; the best data is, at least in part, the highest quality data. If you have “bad” data, your models will be bad, your chatbots will give bad answers, your employees will make bad decisions, and you will go out of business.3Garbage in, garbage out; sounds right. But is it?


# Math, ish


Loosely speaking, companies collect data for two reasons: To help them make strategic decisions, and to help them make operational decisions. Strategic decisions come from reporting—say, “we make 80 percent of our money selling shoes”—and analysis of that reporting—“people leave a lot of shoes in their online shopping carts, and maybe we should send them some emails to remind them about that.” Operational decisions are the often automated ones that carry out a strategic decision—“every morning, at 9:15 am in their local time zone, send people who have shoes in their shopping cart an email with a big picture of those shoes.”


Neither of these things work very well if the data they’re built on top of bad data. If you don’t track what people leave in their shopping carts, you’ll never know that they’re full of shoes. If you have missing data because your Android app doesn’t record what people put in their carts, you won’t email people shopping on their phones. If your data is messy and takes too long to clean up, you might email people after they’ve decided to buy shoes from some other store. If a bug mixes up which shoes a customer has in their cart, you’ll remind them to buy the wrong pair, and they will be confused or upset. This is all well understood, so much so that you can make jokes about it on billboards in San Francisco, andpeople will laugh about it.


Today, people collect data for a (still hypothetical but much hyped) third reason: To train, tune, or be available to some AI model. The shoe store needs product catalog data so that their customer support chatbot can be informed about all of the latest products that are in stock. It needs to know demographic information about its customers, so that it can write custom marketing copy for each user when they land on a product page.4It needs to ingest all of its customers’ reviews into a giant vector database so that procurement managers can “chat with virtual customers,” and figure out which styles of shoes to stock next season.


In some cases, these sorts of problems are no different than what we do with data today; they’re just operational decisions, where the decision is made by an LLM rather than a series of if-this-then-that heuristics. They need accurate data, sure, but no more or less than anyone already does today.


But for the other cases—for the “transformative” ones, in which data is used to train some model, or build some AI agent—data quality actually seems to matterless?


Very roughly, bad data can throw a wrench in today’s analytical gears because most analysis is done with math. Math is useful, but it has a problem: One wrong number can mess everything up. The sum of nine correct data points and one incorrect data point is wrong; the average of 999 accurate numbers and one inaccurate one is wrong. The revenue you report to the SEC can be undone by one bad number; the effect of an A/B test can get inverted if a few data points get dropped. That’s the blessing and curse of math, I suppose: Every aggregation is a precise summarization of every piece underneath it.


To me, the most useful way to think about an LLM is asaggregation functions for text(or images, or videos, or whatever). It is a way to combine a bunch of previously unsummable data into something that acts like an average: Average thenews; average myemail; averageevery Drake and The Weeknd song.


But they’re very loose averages. If you toldSuno, an AI music generator, to make a mashup of Drake and The Weeknd and left out a few of theirworst songs, or even mistakenly threw in a few of Travis Scott’s, you’d still probably get something pretty similar to “Heart on My Sleeve.”


More importantly though,you probably wouldn’t be able to tell the difference.Whereas an analyst can dutifully double and triple check their math to make sure that their figures are correct, or they can determine precisely how some missing numbers warped their final results, an AI DJ can’t. There are no “correct” averages of songs; there is no way to audit “Heart on My Sleeve” to know whether “Fein” was mistakenly included in its input data or not.5


In other words, the approximate qualitative averages that get built by these models bulldoze bad data in ways careful mathematical computations do not. Which isn’t to say that better data doesn’t make a better model—I’m sure it does—but it means the connection is at least somewhat indirect, and that a lot of generative AI models, including the best ones in the world, are pretty durable to bad data.6Copilot, a code writing model, is trained oncode in public Github repositories, some of which are meticulously maintained by professional developers and some of which are theconfused midnight wanderingsof a desperatepretenginner. ChatGPT istrained on Reddit, which is not a clean corpus of text, in any sense of the word. Midjourney is trained on100 million images, which likely includes both well-cataloged Ansel Adams photos and a bunch of badly labeled pictures dredged up from the depths of Instagram. And perhaps most tellingly, AI companies commonly use this point—that there is a fuzzy connection between what goes into a model and what comes out—as a legal defense against copyright claims. Another way to phraseOpenAI’s responsetoNew York Times’lawsuit against them—that “models learn from the enormous aggregate of human knowledge” so “any single data source - including The New York Times - is not significant for the model’s intended learning”—is to say that no individual data source really matters, including bad and messy ones.


All of which raises the question—if data teams’ bleating about the dangers of bad data haven’t been listened to before, why would they be listened to now? You can imagine the conversation: A CEO says they want to train some fancy model to create animmersive commerce experience, because “a standard search bar is no longer the fastest path to purchase, rather we must use technology to adapt to customers’ individual preferences and needs.” The data team says, “Ok, but it is critical that we invest in robust data quality solutions, so that we can build the best models.” The CEO then says, “We have aprofit margin of 2.7 percent. How will I know that this additional investment in data quality will make us more money?” And the data team says, “Ah, well, you see, no single source is significant for the model’s intended learning.”


Which is not a very good answer? And it’s certainly a much worse answer than saying “we need to invest in robust data quality solutions, so that you can correctly report how much money we make and don’tget sued by the SEC.” So why would data quality matter more now?


# Vibes


There may be one reason. Even if AI models aren’t fully undone by bad data—even if you can make a popular song on a messy catalog of songs, or build a good immersive shopping experience on an incomplete event stream of customer behaviors—something about thatfeelswrong. It’s one thing to intellectually understand that the best softwareshould have some bugs, and that you’rewasting timeif you never miss a flight. But it’s another thing to actually tolerate the bugs, and to miss the flights. If it ain’t broke, don’t fix it—but if it is broke, a lot of us get twitchy.


We haven’t gotten twitchy about broken dashboards because, frankly, people don’t get twitchy about broken things that they don’t care about.7And if nothing else, people seem to care about AI. CEOs are excited about it. Everyone isjealous of Nvidia. There is aparty full of rich people, and nobody wants to miss it.


If data quality matters more now than it did before, it seems like that will be the reason why: Not because AI models care more about higher quality data than traditional reporting, but because, at least during the current AI circus, businesses care more about AI models than they ever did about reporting. And that, I’m sure plenty of software companies will say, is a big change that is very good for data quality, actually.

[1](https://benn.substack.com/p/does-data-quality-matter#footnote-anchor-1-152026526)

But not all of them! In early 2020, a friend of mine was teaching bridge 1) to seniors 2) in giant enclosed conference rooms 3)on cruise ships. Quite hard to spin a global pandemic as being good for that business, I’m afraid.

[2](https://benn.substack.com/p/does-data-quality-matter#footnote-anchor-2-152026526)

It is, after all, theage of AI. Or theera of AI. I don’t know.

[3](https://benn.substack.com/p/does-data-quality-matter#footnote-anchor-3-152026526)

Take one sipof that poison, and everything will immediately spiral out of control, until you are dead in a ditch.

[4](https://benn.substack.com/p/does-data-quality-matter#footnote-anchor-4-152026526)

This will be a thing, right? Someone will go to look at a pair of shoes, and rather than thewebsite sayingthat they “call to simplicity through their archetypal shape, and their matte leather is contrasting with the shine of the lacquer, giving them a strong and timeless presence,” it’ll identify them as the type who’s insecure about their height and will instead say “these shoes have 4 inch heels and we promisenobody will be able to tell.”

[5](https://benn.substack.com/p/does-data-quality-matter#footnote-anchor-5-152026526)

Or intentionally included! The person who made it is alsomaking fake Travis Scott songs, so who knows how any of them are actually made. And that’s sort of the point. If you can’t tell what the inputs are, can we really say it’s important for all of those inputs to meet some high standard of quality?

[6](https://benn.substack.com/p/does-data-quality-matter#footnote-anchor-6-152026526)

You could probably even make the argument that some messy data isgood.As OpenAI’s Andrej Karpathy said, a bit of randomness is a feature of LLMs, not a bug. It is our disjointed and idiosyncratic experiences that make us creative; it is the imperfect training data in an LLM that makes it more than a mechanical search engine.

[7](https://benn.substack.com/p/does-data-quality-matter#footnote-anchor-7-152026526)

Consider, for example, the oddity of the entire data contract debate. If data teams need people tosign actual contractsso that they’ll be motivated to give us good data—good data that we are supposed to manufacture into something useful and give back to them—how valuable can that thing that we’re making really be? You only need hall monitors when nobody believes that the rules actually matter.
