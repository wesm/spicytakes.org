---
title: "A/B testing in politics"
date: 2015-03-24
url: https://mathbabe.org/2015/03/24/ab-testing-in-politics/
word_count: 751
---


As research for my book I’m studying the way people use big data techniques, mostly from the marketing world, in politics. So naturally I was intrigued by [Kyle Rush’s blogpost about A/B testing on the Obama campaign](http://kylerush.net/blog/optimization-at-the-obama-campaign-ab-testing/). Kyle was the Deputy Director of Frontend Web Development at Obama for America.


In case you don’t know the lingo, A/B testing is a test done by marketers to decide which of two ad designs is more effective – the ad with the dark blue background or the ad with the dark red background, for example. But in this case it was more like, the ad with Obama’s family or the ad with Obama’s family and the American flag in the background.


The idea is, as a marketer, you offer your target audience both ads – actually, any individual in the target audience either sees ad A or ad B, randomly – and then, after enough people have seen the ads, you see which population responds more, and you go with that version. Then you move on to the next test, where you keep the characteristic that just won and you test some other aspect of the ad, like the font.


As a mathematical testing framework, A/B testing is interesting and has structural complications – how do you know you’re getting a global maximum instead of a local maximum? In other words, if you’d first tested the font, and then the background color, would you have ended up with a “better ad”? What if there are 50 things you’d like to test, how do you decide which order to test them in?


But that’s not what interests me about Kyle’s Obama A/B testing blogpost. Rather, I’m fascinated by the *definition of success* that was chosen.


After all, an A/B test is all about which ad “works better,” so there has to be some way to measure success, and it has to be measured in real time if you want to go through many iterations of your ad.


In the case of the Obama campaign, there were two definitions of success, or maybe three: how often people signed up to be on Obama’s newsletter, how often they gave money, and how much money they gave. I infer this from Kyle’s braggy second sentence, “Overall we executed about 500 a/b tests on our web pages in a 20 month period which increased donation conversions by 49% and sign up conversions by 161%.” Those were the measures Kyle and his team was optimizing on.


Most of the blog post focused on getting people to donate more, and specifically on getting them to fill out the credit card donation page form. Here’s what they A/B tested:


> Our plan was to separate the field groups into four smaller steps so that users did not feel overwhelmed by the length of the form. Essentially the idea was to get users to the top of the mountain by showing them a small incline rather than a steep slope.


What I find super interesting about this stuff (and of course this not the only “data science” that was used in Obama’s campaign, there was a separate team focused on getting Facebook users to share their friends’ lists and such) is that nowhere is there even a slight nod to the question of whether this stuff will improve or even maintain democracy. They don’t even discuss how maintainable this is.


I mean, we gave the Obama analytics team lots of credit for stuff, but in the end what they did was optimize a bunch of people’s donation money. Is that something we should cheer? It seems more like an arms race with the Republican party, in which the Democrats pulled ahead temporarily. And all it means is that the fight for donations will be even more manipulative, by both sides, by the next presidential election cycle.


As Felix Salmon pointed out to me over [beer and sausages last week](http://www.lederhosennyc.com/), the problem with big data in politics is that the easiest thing you can measure in politics is money, which means everything is optimized to that metric of success, leaving all other considerations ignored and probably stifled. And yes, “sign ups” are also measurable, but they more or less correspond to people who will receive weekly or daily requests for money from the candidate.


Readers, please tell me I’m wrong. Or suggest a way we can measure something and optimize to something that is less cynical than the size of a war chest.
