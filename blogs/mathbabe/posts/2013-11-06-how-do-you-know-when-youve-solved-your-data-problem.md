---
title: "How do you know when you’ve solved your data problem?"
date: 2013-11-06
url: https://mathbabe.org/2013/11/06/how-do-you-know-when-youve-solved-your-data-problem/
word_count: 941
---


I’ve been really impressed by how consistently people have gone to read my post “[K-Nearest Neighbors: dangerously simple](https://mathbabe.org/2013/04/04/k-nearest-neighbors-dangerously-simple/),” which I back in April. Here’s a timeline of hits on that post:


Stats for “K-Nearest Neighbors: dangerously simple.” I’ve actually gotten more hits recently.


I think the interest in this post is that people like having myths debunked, and are particularly interested in hearing how even the simple things that they thought they understand are possibly wrong, or at least more complicated than they’d been assuming. Either that or it’s just got a real catchy name.


Anyway, since I’m still getting hits on that post, I’m also still getting comments, and just this morning I came across [a new comment](https://mathbabe.org/2013/04/04/k-nearest-neighbors-dangerously-simple/#comment-40304) by someone who calls herself “travelingactuary”. Here it is:


> My understanding is that CEOs hate technical details, but do like results. So, they wouldn’t care if you used K-Nearest Neighbors, neural nets, or one that you invented yourself, so long as it actually solved a business problem for them. I guess the problem everyone faces is, if the business problem remains, is it because the analysis was lacking or some other reason? If the business is ‘solved’ is it actually solved or did someone just get lucky? That being so, if the business actually needs the classifier to classify correctly, you better hire someone who knows what they’re doing, rather than hoping the software will do it for you.
> Presumably you want to sell something to Monica, and the next n Monicas who show up. If your model finds a whole lot of big spenders who then don’t, your technophobe CEO is still liable to think there’s something wrong.


I think this comment brings up the right question, namely* knowing when you’ve solved your data problem, *with K-Nearest Neighbors or whichever algorithms you’ve chosen to use. Unfortunately, it’s not that easy.


Here’s the thing, it’s almost never possible to tell if a data problem is truly solved. I mean, it might be a business problem where you go from losing money to making money, and in that sense you could say it’s been “solved.” But in terms of modeling, it’s very rarely a binary thing.


Why do I say that? Because, at least in my experience, it’s rare that you could possibly hope for high accuracy when you model stuff, even if it’s a classification problem. Most of the time you’re trying to achieve something better than random, some kind of edge. Often an edge is enough, but it’s nearly impossible to know if you’ve gotten the biggest edge possible.


For example, say you’re binning people you who come to your site in three equally sized groups, as “high spenders,” “medium spenders,” and “low spenders.” So if the model were random, you’d expect a third to be put into each group, and that someone who ends up as a big spender is equally likely to be in any of the three bins.


Next, say you make a model that’s better than random. How would you know that? You can measure that, for example, by comparing it to the random model, or in other words by seeing how much better you do than random. So if someone who ends up being a big spender is three times more likely to have been labeled a big spender than a low spender and twice as likely than a medium spender, you know your model is “working.”


You’d use those numbers, 3x and 2x, as a way of *measuring the edge your model is giving you*. You might care about other related numbers more, like whether pegged low spenders are actually low spenders. It’s up to you to decide what it means that the model is working. But even when you’ve done that carefully, and set up a daily updated monitor, the model itself still might not be optimal, and you might still be losing money.


In other words, you can be a bad modeler or a good modeler, and either way when you try to solve a specific problem you won’t really know if you did the best possible job you could have, or someone else could have with their different tools and talents.


Even so, there are standards that good modelers should follow. First and most importantly, you should always set up a model monitor to keep track of the quality of the model and see how it fares over time.  Because why? Because second, you should always assume that, over time, your model will degrade, even if you are updating it regularly or even automatically. It’s of course good to know how crappy things are getting so you don’t have a false sense of accomplishment.


Keep in mind that just because it’s getting worse doesn’t mean you can easily start over again and do better. But a least you can try, and you will know when it’s worth a try. So, that’s one thing that’s good about admitting your inability to finish anything.


On to the political aspect of this issue. If you work for a CEO who absolutely hates ambiguity – and CEO’s are trained to hate ambiguity, as well as trained to never hesitate – and if that CEO wants more than anything to think their data problem has been “solved,” then you might be tempted to argue that you’ve done a phenomenal job just to make her happy. But if you’re honest, you won’t say that, because it ‘aint true.


Ironically and for these reasons, some of the most honest data people end up looking like crappy scientists because they never claim to be finished doing their job.
