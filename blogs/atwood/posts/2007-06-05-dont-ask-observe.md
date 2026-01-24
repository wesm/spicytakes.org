---
title: "Don’t Ask – Observe"
date: 2007-06-05
url: https://blog.codinghorror.com/dont-ask-observe/
slug: dont-ask-observe
word_count: 1301
---

James Surowiecki, author of [The Wisdom of Crowds](http://www.amazon.com/exec/obidos/ASIN/0385721706), writes about the paradox of [complexity and consumer choice](http://www.newyorker.com/talk/financial/2007/05/28/070528ta_talk_surowiecki) in a recent New Yorker column:


> A recent study by a trio of marketing academics found that when consumers were given a choice of three models, of varying complexity, of a digital device, more than sixty per cent chose the one with the most features. Then, when the subjects were given the chance to customize their product, choosing from twenty-five features, they behaved like kids in a candy store. (Twenty features was the average.) **But, when they were asked to use the digital device, so-called “feature fatigue” set in. They became frustrated with the plethora of options they had created, and ended up happier with a simpler product.**


It’s impossible to see that you’re creating a Frankenstein’s monster of a product – until you attempt to use it. It’s what I call **the all-you-can-eat buffet problem**. There’s so much delicious food to choose from at the buffet, and you’re so very hungry. Naturally you load up your plate with wild abandon. But after sitting down at the table, you belatedly realize *there’s no way you could possibly eat all that food*.


In all fairness, sometimes people do, in fact, want complexity. The [newly redesigned Google Korea homepage](http://blog.outer-court.com/archive/2007-06-04.html#n60) is intentionally complex. Google’s Marissa Mayer noted “*It was important where our classic minimalism wasn’t working that we adapt.”*


![](https://blog.codinghorror.com/content/images/2025/05/image-491.png)


This echoes an earlier [blog post by Donald Norman](https://web.archive.org/web/20070611190005/http://www.jnd.org/dn.mss/simplicity_is_highly.html) describing the way South Koreans seek out complexity in luxury goods:


> I recently toured a department store in South Korea. Visiting department stores and the local markets is one of my favorite pastimes whenever I visit a country new to me, the better to get to know the local culture. Foods differ, clothes differ, and in the past, appliances differed: appliances, kitchen utensils, gardening tools, and shop tools.
> I found the traditional “white goods” most interesting: Refrigerators and washing machines. The store obviously had the Korean companies LG and Samsung, but also GE, Braun, and Philips. The Korean products seemed more complex than the non-Korean ones, even though the specifications and prices were essentially identical. “Why?” I asked my two guides, both of whom were usability professionals. “Because Koreans like things to look complex,” they responded. It is a symbol: it shows their status.


What’s particularly telling in the study Surowiecki cites is the disconnect between what people *say* they want and what they *actually* want. You’ll find this theme echoed over and over again in usability circles: **what users say they will do, and what they actually do, are often two very different things.** That’s why asking users what they want is nearly useless from a usability perspective; **you have to *observe what users actually do***. That’s what [usability testing](https://blog.codinghorror.com/low-fi-usability-testing/) is. Instead of asking consumers what features they wanted in a digital camera, the study should have presented them with a few digital camera prototypes and then observed how they were used. Consumers’ success or failure interacting with the prototypes tells us more than a thousand surveys, questionnaires, or focus groups ever could. Unfortunately, creating physical prototypes of digital cameras is prohibitively expensive, so it doesn’t happen.


Prototyping software, which is built out of [pure thought-stuff](https://blog.codinghorror.com/uml-circuit-diagrams-and-gods-rules/), is a much easier proposition. [Dare Obasanjo](http://www.25hoursaday.com/weblog/) recently pointed out a great paper, [Practical Guide to Controlled Experiments on the Web](http://exp-platform.com/Documents/GuideControlledExperiments.pdf) (pdf), which makes a strong case for frequent observational A/B usability tests:


> Greg Linden at Amazon created a prototype to show personalized recommendations based on items in a shopping cart. You add an item, recommendations show up; add another item, different recommendations show up. Linden notes that while the prototype looked promising, a marketing senior vice-president was dead set against it, claiming it would distract people from checking out. Greg was forbidden to work on this any further. Nonetheless, Greg ran a controlled experiment, and the feature won by such a wide margin that not having it live was costing Amazon a noticeable chunk of change. With new urgency, shopping cart recommendations launched. Since then, multiple sites have copied cart recommendations.
> The culture of experimentation at Amazon, where data trumps intuition, and a system that made running experiments easy, allowed Amazon to innovate quickly and effectively.


Why *ask* users if they’d like recommendations in their shopping carts when you can simply deploy the feature to half your users, then *observe* what happens? Web sites are particularly amenable to this kind of observational testing, because it’s easy to collect the user action data on the server as a series of HTTP requests. You don’t even have to be physically present to “observe” users this way. However, you can perform the same kind of data analysis, with a little care, even if you’re deploying a traditional desktop application. Jensen Harris describes how [Microsoft collects user action data](https://web.archive.org/web/20070608140350/http://blogs.msdn.com/jensenh/archive/2005/10/31/487247.aspx) in Office 2003:


> Suppose you wanted to know what [Office 2000] features people use the most. Well, you start by asking a “guru” who has worked in the product for a long time. “Everyone uses AutoText a lot,” the guru says. The louder the “experts” are, the more their opinions count. Then you move on to the anecdotal evidence: “I was home over Christmas, and I saw my mom using Normal View... that’s probably what most beginners use.” And mix in advice from the helpful expert: “most people run multi-monitor, I heard that from the guy at Best Buy.”
> SQM, which stands for “Service Quality Monitoring” is our internal name for what became known externally as the [Customer Experience Improvement Program](https://web.archive.org/web/20070613194217/http://www.microsoft.com/products/ceip/en-us/default.mspx). It works like this: Office 2003 users have the opportunity to opt-in to the program. From these people, we collect anonymous, non-traceable data points detailing how the software is used and and on what kind of hardware. (Of course, no personally identifiable data is collected whatsoever.)
> As designers, we define data points we’re interested in learning about and the software is instrumented to collect that data. All of the incoming data is then aggregated together on a huge server where people like me use it to help drive decisions.
> What kind of data do we collect? We know everything from the frequency of which commands are used to the number of Outlook mail folders you have. We know which keyboard shortcuts you use. We know how much time you spend in the Calendar, and we know if you customize your toolbars. In short, we collect anything we think might be interesting and useful as long as it doesn’t compromise a user’s privacy.


This may sound eerily like Big Brother, but the SQM merely extends the same level of reporting enjoyed in every single web application ever created to desktop applications.


The true power of this data is that you can remotely, silently, automatically “observe” what users actually do in your software. Now you can answer questions like what are the [top 5 most used commands](https://web.archive.org/web/20070704145556/http://blogs.msdn.com/jensenh/archive/2005/11/07/489864.aspx) in Microsoft Word 2003? The answer may surprise you. Do you know what the top 5 most frequently used functions in *your* application are?


Don’t get me wrong. I love users. Some of my best friends are users. But like all of us humans, they’re unreliable at best. **In order to move beyond usability guesswork, there’s no substitute for observing customers using your product.** Wouldn’t it be liberating to be able to make design decisions based on the way your customers actually use your software, rather than the way they tell you they use it? Or the way you *think* they use it? Whether you’re observing users in low-fi usability tests, or collecting user action data so you can observe users virtually, the goal is the same: **don’t ask – observe**.

[consumer behavior](https://blog.codinghorror.com/tag/consumer-behavior/)
[product design](https://blog.codinghorror.com/tag/product-design/)
[feature fatigue](https://blog.codinghorror.com/tag/feature-fatigue/)
[complexity](https://blog.codinghorror.com/tag/complexity/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
