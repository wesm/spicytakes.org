---
title: "Followup Questions for 'Strategic SEO for Startups'"
date: 2010-01-25
url: https://www.kalzumeus.com/2010/01/25/followup-questions-for-strategic-seo-for-startups/
slug: followup-questions-for-strategic-seo-for-startups
word_count: 1340
---


Peter Christensen had a few [questions for me](http://www.pchristensen.com/blog/articles/followup-questions-to-strategic-seo-for-startups/) regarding my last blog post about [SEO for startups](https://www.kalzumeus.com/2010/01/24/startup-seo/).  I thought the questions were interesting enough to require a bit more than a comment on his post, so I’m going to answer them in detail here.  The details are very, very specific to my particular business — if you want a high-level strategic overview, I suggest reading that post instead.


In the past you’ve talked about outsourcing your content creation to your “army of freelancers”.  What did that consist of on your end?  My guess is you looked at terms and topics people were searching for (you mentioned “[baby shower bingo](http://www.bingocardcreator.com/bingo-cards/parties-and-events/baby-shower)” once) and then sent a job to your freelancers to come up with 80 or so baby shower words that you feed into your card generator and sample bingo card landing pages.


Periodically, when I have an idea for a new project, I put out a call for freelancers on my blog [similar to this](https://www.kalzumeus.com/2009/08/29/seeking-a-freelance-writerblogger/) (for blog writing on my “sprawling bingo empire”) or [this](https://www.kalzumeus.com/2007/10/03/before-i-try-rentacoder/) (for creating bingo cards).  (Incidentally, “army” is an overstatement: I think in my business career I’ve used a bit less than a dozen, but don’t have my expenses report in front of me.  One woman  in particular is easily 80%+ of that.  Why mess with something that works?)


The work-flow for those two projects is a bit different, but in general I write up the general outline of what I expect (you can see the most important bits in those posts) and then let my freelancers run with them.  For bingo cards I typically give them discretion to choose their own topics (although I let them see my stats for what previous cards were popular — for example, [sorted by genre](http://www.bingocardcreator.com/stats/download-charts) or [popular this week](http://www.bingocardcreator.com/popular)).  For the blog creation project I came up with a list of 14 mini-sites via a one-off SQL query.


The deliverable for bingo cards has changed over the years as I’ve upgraded my CMS.  Currently, there is a back-end one page web form on my site which asks for a title for the card, a subtitle, a brief sentence of description, and then a word list.  Anything submitted there goes into my database and awaits my review, which given that my freelancer is very good at what she does is typically “Oh, good, here’s 30 lists for this month.  Approve All.  *Goes off to bank site to mail check*.”  Within a few seconds of me hitting approve, the CMS backing my site turns the word list into a PDF file, grabs a screenshot of it, and does a bit of content page generation.


The deliverable for the mini-sites is just pages made in WordPress, extolling the virtues of [Valentine’s Day bingo](http://www.valentinebingocards.com) or what have you.


How do you analyze and rank your SEO strategies?  I see your sample card landing pages have an id that they pass to the registration page so you know how the different landing pages are converting.  What other methods do you use to determine which SEO methods are most valuable to you?


The flippant answer is that if I make more money than I expect to then I guess everything is working.  Seriously speaking, though, I do very little backwards facing analysis (“Did that work?”) and concentrate mostly on forward facing analysis (“What opportunities can I exploit now?”), with the exception of when I’m writing a blog post to comment on how something worked.


One of the reasons I’ve cooled on Google Analytics over the years is it doesn’t really lend itself to providing data which lets you make actionable decisions in a reasonable amount of time.  For example, if I look at my stats, I can tell you with arbitrary precision how much more popular baby shower bingo cards are than football bingo cards.  Whee.  That doesn’t tell me anything I can do to improve my business today.  Most of the things which can tell me stuff that will improve my business are the domain-specific analytics functions I’ve created (like the above) or fun little one-off explorations of my database that I do from the Rails console.


For example, I might play around one day and see what the most common 25 words are for customers making bingo cards.  (That was what clued me into baby shower bingo.)  That usually identifies a weak spot in my pre-made card lineup, which I can either tell a freelancer about or just fill myself.


Incidentally, you mention that you think the ID I pass to the registration page is for tracking conversions.  Actually, not so much.  I [track conversions](http://www.bingocardcreator.com/articles/tracking-with-mixpanel.htm) with [Mixpanel](http://www.mixpanel.com).  The reason that ID gets passed is to provide continuity of experience for new trial users.  I’m actually really proud of this hack: if you show up on my landing page for, I don’t know, tea bingo, and you click “Create Your Own Bingo Cards” and sign up for the free trial, your free trial account gets pre-initialized with my set of tea bingo cards already in it and “personalized” instructions on the dashboard about how you can print bingo cards like the tea bingo cards you were just interested in.


This **greatly** increases funnel success in A/B tests.  (You are roughly 20% more likely to successfully download a set of customized bingo cards if I give you the “personalized” treatment than you are if I drop you at a blank dashboard and expect you to fight your way through.)


I also do this for my PPC (AdWords) campaigns: if you respond to an ad for Halloween Bingo Cards, then by jove I’m going to everything short of dropping a pumpkin on your desktop.


**Best idea here**: I don’t think enough software companies unify the marketing and product sides, incidentally.  We tend to treat everybody coming in to the top of the funnel as absolutely the same.  Then we treat everybody who makes it through funnel step N exactly the same.  But we’ve got data that says they are different — why not use the data to enhance their experience and, not incidentally, improve their propensity to buy the product?


For example, if I were in charge of World of Epic Dragonslaying, and I had a PPC


Your Bingo Card landing pages allow you to programatically generate tons of pages from content in your product.  What other tips do you have for getting lots of good SEO content for a low investment of time/money?


I suggest reading the parts of the article about scalable content generation.  I don’t have another magic secret that I use for my own business.  OK, maybe half a secret: data begets data.  For example, I’ve got my 800 or whatever the number is bingo card activities that my freelancers and I cooked up.  I use that in several places: each bingo activity becomes

- a content page
- a PPC landing page
- an activity in the downloadable version of the software
- an activity in the online version of the software


This gives me usage/popularity data about the same subjects.  I use that for:

- automated interlinking of content pages  (see left hand sidebar, “Related Activities”)
- automated decisions of promoted content on the front page
- my popular activities list
- widgets across my “sprawling bingo empire” which list popular activities
- semi-automated decisions on which content to promote to mini-sites


Anyhow, if I should come up with a good second idea to generate content for the website, you’ll likely hear about it here roughly contemporaneously with me implementing it.  Many of my friends have suggested I might be at the point of diminishing returns for BCC.  I think that is likely accurate, and so my very best ideas this year are probably going to be in service of my next software project.  However, given that BCC has always been nights and weekends for me, that doesn’t necessarily mean “maintenance mode” for it will be totally bereft of new ideas.


I hope that answers your questions, Peter.  Thanks for asking.
