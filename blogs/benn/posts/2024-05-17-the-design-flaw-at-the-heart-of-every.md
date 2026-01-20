---
title: "The design flaw at the heart of every data product"
subtitle: "I'll save you a click: It's because they weren't designed for real data."
date: 2024-05-17T16:41:02+00:00
url: https://benn.substack.com/p/the-design-flaw-at-the-heart-of-every
slug: the-design-flaw-at-the-heart-of-every
word_count: 1999
---


![](https://substackcdn.com/image/fetch/$s_!B59Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedd20d67-4fae-49f4-a461-e98445f88706_1161x738.png)

*If you know, you know. If you don’t know, no spoilers, go watchThe Good Place.*


If you’ve ever seen a demo of a data product, you know the script:


Ava, the CEO of Playful Pines,1opens Slack. A message is waiting for her. It’s fromJanet, the AI-enabled chatbot from PowerStrategy BI.2“Here is your Daily Insights report,” Janet says. There are a few tidy charts: A forecast shows revenue on aclear upward trajectory; an uncannily legible area chart showssales by marketing channel;a colorful map shows nothing at all. But look, Janet say,sales jumped last night! Oh my! Ava asks Janet to explain what caused the sudden spike. “Sales of Bumble Blocks are up 600 percent,” Janet says, and shows Ava a chart of sales by product line. There are five lines on the chart. Four of them roll gently up and down, while the line for Bumble Blocks rises distinctly above the rest. The chart is clean; the lines are smooth; the axis is unbroken; the comparisons are easy; the conclusion is obvious.


Ava is delighted, but worried.Can we fill all those orders?Bumble Blocks are made with real wood; real,reclaimedwood. If this trend continues, Playful Pines will need to ramp up production!


Ava sends a message to Simon, the production manager. Simon is already on it! Janet alerted him about the incoming orders, and his real-time PowerStrategy dashboard says that they have enough inventory for three more days of above-average sales. He’s already preparing to shift production from other toys to Bumble Blocks. But how many new sets do they need? How long will the new orders keep coming in? Ava posts a message to her chief marketing officer: “@meredith, Bumble Blocks is selling out! Do you know where yesterday’s new customers came from?”


Olivia, Playful Pines’ social media manager, quickly chimes in. “ToysWithTaylor posted about Bumble Blocks on TikTok last night! She has 4 million followers!” Olivia shares a PowerStrategy report of Bumble Block orders by referrer; another pristine chart shows that most of last night’s orders came from TikTok. She sends a second graph: “When playtimeOFFICIAL posted about Tilted Towers, the increase in sales lasted about a little over a day, but they only had 600,000 followers. Janet is predicting this could last for as long as a week.”


Great work everyone, says Ava. She asks Simon to prepare for up to ten days of new orders. She congratulates Olivia on her successful influencer campaigns. Everyone is happy. Playful Pines is up and to the right. Some B-roll shows a smiling kid playing with blocks. Olivia updates her Slack profile from social media manager to marketing director. With PowerStrategy, you can understand your business as well as Ava. You can be as prepared as Simon. You can get promoted like Olivia. You can love your job as much as everyone at Playful Pines. The video closes with an animated PowerStrategy logoandaquirkysound. Delightful.


# The bad place


Unfortunately, in real life, here's what happens instead:


Ava is the CEO of Red Eye Entertainment, LLC, the obscure parent company of several dozen online gaming brands. They make clones of popular apps likeCandy Crush, and try to game social media algorithms into making them go viral. They run a secondary business reselling user data to advertisers.


Ava opens her PowerStrategy dashboard. There are 44 charts. The big one, monthly revenue, is mostly flat. Maybe it’s down? Ava squints. It’s hard to say because May is only half over. Eyeballing it, May looks to be on track to be about the same as April? She scrolls down. Total daily signups are all over the place: 95 yesterday, 455 two days ago, 501 three days ago, 220 the day before. There is a bar chart that shows signups by game; there are 45 series on the chart; it is completely illegible.Spades with Friendslooks steady.Smuggler's Runis doing well?Operation: AnnihilationandHedge Mazeare having down months?


The marketing funnel is even more incomprehensible. A line chart of signups by source looks like a Jackson Pollock painting. The biggest source is “Unknown.” The second biggest is “Social.” The third biggest is “Twitch - display.” There is also a series called “utm_source=twitter&camp_name=MM-en_ABO_WW_keywords-bitcoin-new-10.05&utm_campaign=46829847&utm_term=gg_v1-cAF_dDT_pic_MM-tm1%28gaming%29_len_p%28fb%29_gM_.”


Weekly active users are up; promising. In-app purchases are down; alarming. The percentage of users playing multiple games is twice as high this month as last month—from 1 percent to 2 percent. One-day retention rates are all over the place; one-month retention rates haven't moved in over a year. Average daily playing time is falling, though recent iOS changes have made tracking it less reliable. Game ratings are rising, though recent Android changes made it harder to collect feedback from users.


What should Ava do? Which of the four dozen noisy graphs should she drill into? Who knows. Nobody knows. Some charts are up. Some charts are down. Some charts are flat. Most charts look likeSolo Jazz. There is no orderly spike of Builder Block sales. There is only noise, and auseless chatbotthatnobody wants. The dashboard is a horoscope, capable of telling whatever story its reader is looking for. The business is turning around. The business is flat. The business is in its death throes, moments from bankruptcy. Well, Ava thinks, it was like this yesterday, and we're still here. Ava moves on.


# Fake data, fake designs


We all design demos around the first story because a demo about the second story would be terrible. Which, sure, fine; demos are supposed to be tight sizzle reelsthat skip the boring parts. The problem, however, is that we also designproductsaround the first story.


This happens in two ways. The first is aesthetic—products are literally designed for the first story.Figma mocks for data productsalmost always show charts with a few well-labeled series. They show tables where every field is nicely formatted and every value fits comfortably in its cell. They show database schema browsers with a reasonable number of tables that are named reasonable things. No designer has ever walked into a product review meeting with mocks ofborked areas charts, tablesmangled by multi-line HTML, or schema browsers with100,000 tables.


Instead, products are designed tohandlethese experiences. They’re designed to encounter one of these issues—a chart full of nulls, a column full of JSON, a schema browser full of tables named nicolle_alexander-walker.dbt_dev.salesforce_opportunity_fields and nicolle_alexander-walker.dbt_dev.salesforce_opportunity_field_history—andnot break. In a sense, every product is built for the happy path of Playful Pines, full of clean data that makes beautiful charts. But Playful Pines isn’t the default experience; it’s the edge case. Most of us are Red Eye Entertainment, plagued by messy data, erratic metrics, and graphs with too many series. This is why most data products never look as good as the mocks:3It’s not the products that are the problem; it’s the data we put underneath.


But of course, that data isn’t going to change—especially whendata quality toolsare designed for the samefantasies.4So itisthe products’ problem.


Though I’m not sure how to best solve this, there’s at least one way to start: Make mocks on real data. Find a real dashboard, a real schema, a real dbt project, and a realmarketo_leadstable, and use those things as design templates. If it makes the UI ugly or the experience confusing,make the UI and the experience better. Until the nerf data in our designs magically show up in our databases, that reality—not the Playful Pines pipe dream—is the world we need products for.


# Everything wiggles


But there’s a bigger issue: A product built for Playful Pines solves the wrong problem.


In that world, Ava needs help finding needles in haystacks. Her business is full of metrics, and she needs to be told of the one that’s moving in a meaningful way. Fundamentally, it’s a problem about search and discovery—it’s about making sure the right people know the right things at the right time.


That, I think, is a gross misunderstanding of what most businesses need. Their problems are more like Red Eye’s: There are needles everywhere, and they all halfheartedly point in different directions. Not only doesthe chart wiggle, 44 of them wiggle. Some wiggle up. Some down. Some wiggle across 20 product SKUs. Some have too many null values to wiggle. Some just say, “Error while reading data, error message: Failed to parse JSON: Unexpected end of string; Unexpected end of string; Expected key.”


In other words, we aren’t detectives looking for thesingle strand of hairthat explains the entire case.We’re Benoit Blanc, investigating a murder full of contradictory clues where everyone has a motive.Interpreting data is hardbecause everything is inconclusive—MQLs are up, ACVs are down, NRR had its worst quarter ever and DAUs have never been higher—and we don’t know how to add it all up.5


So much of what we build is for the former problem.Askanyquestion;drillintoanything; have an AI agent spelunk through every metric and dashboard, and create a daily digest of the important changes.6Find that one missing clue—that spike in new orders of Bumble Blocks from TikTok—that cracks the case.


All of this, however, is often counterproductive. More clues don’t help us know what to do; they just create more confusion. Instead, we need help making sense of what we already know. We need help with deduction, not discovery.


# The elephant in the room


From Julie Zhao:


> A famous Indian parable describes five blind men encountering an elephant for the first time. They each decide to touch the elephant to understand what the animal is like.“An elephant is smooth and hard, like bone,” says the man who grasped its tusk“Nonsense, an elephant is soft like leather,” says the man who felt its ear.“You’re both wrong; an elephant is rough like a tree,” says the man who touched its leg.The five men begin arguing vehemently, each convinced that he is right. None of them manages to convince the other of anything, except that everyone else is untrustworthy.


Every day, companies are handed a new animal, and have to decide what it is. How would we solve that problem? Probably,with a process: A standard way to poke at the animal and a standard way to evaluate what we learned.


But most data products are designed with the implicit assumption that we can figure out what the animal is if only we touch just the right corner of if. They’re designed for the paradise of Playful Pines, in which we’re one clever query or one AI-surfaced insight away from discovering that the elephant is an elephant.


Unfortunately, that’s not where we are, no matter how much we pretend to be living in thatperfect afterlife. And the only way to get to the good place is by designing things for bad place that we’re living in.

[1](https://benn.substack.com/p/the-design-flaw-at-the-heart-of-every#footnote-anchor-1-144726809)

We’re never quite told what Playful Pines does. It seems like they make analog games for kids? Whatever, it doesn’t matter, as long as the products are whimsical, the brand is wholesome, the team is diverse, and the office is colorful. (There’s apparently a realPlayful Pines, but man,it does not look playful.)

[2](https://benn.substack.com/p/the-design-flaw-at-the-heart-of-every#footnote-anchor-2-144726809)

Weknow exactlywhat PowerStrategy BI does. It brings life to data. It masters your data to accelerate business outcomes. It sets your data free. It unlocks enterprise data for modern analytics. It fuels innovation. It’s data-obsessed. It’s setting the stage for the AI-powered enterprise. It uses analytics for rapid insights to drive informed actions. Data is its rich history. Data is the opportunity. It’s reimagined the future.

[3](https://benn.substack.com/p/the-design-flaw-at-the-heart-of-every#footnote-anchor-3-144726809)

For example, Sisense’sillustrationsof their dashboards, fromhere, are beautiful. Their demo dashboards, fromhere, area mess. Thestylized screenshotsof Tableau tell a satisfying story; theirexample dashboards, fromhere, are full of noise. And shortly before thatflashy Looker demo, weseeanactual Looker report.

[4](https://benn.substack.com/p/the-design-flaw-at-the-heart-of-every#footnote-anchor-4-144726809)

Fromhere.

[5](https://benn.substack.com/p/the-design-flaw-at-the-heart-of-every#footnote-anchor-5-144726809)

If you’ve ever run an A/B test, you probably know what this is like. The main metric you’re tracking is up, a little? But some secondary metric is way down, another one is way up, and everything else is flat.

[6](https://benn.substack.com/p/the-design-flaw-at-the-heart-of-every#footnote-anchor-6-144726809)

If 2023 was the year that every data new startup was a SQL chatbot, 2024 is the year that every startup is a news feed of AI-powered insights.
