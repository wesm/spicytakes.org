---
title: "Bringing A/B Testing To The Fortune 5 Million"
date: 2009-12-09
url: https://www.kalzumeus.com/2009/12/09/bringing-ab-testing-to-the-fortune-5-million/
slug: bringing-ab-testing-to-the-fortune-5-million
word_count: 1187
---


After writing an [A/B testing library](http://www.bingocardcreator.com/abingo/) and blogging about the subject for a [couple](https://www.kalzumeus.com/2007/09/29/bingo-cards-on-rails/) [of](https://www.kalzumeus.com/2009/02/22/ab-testing-lightbox-screenshot-vs-screenshot-download-link/) [years](https://www.kalzumeus.com/2009/08/19/minor-lessons-from-ab-testing/), I somehow unwittingly sleepwalked into being that most loathsome of creatures, a technology evangelist.  This means that periodically I get emails from folks with the Next Big Thing who want my opinion on it.  I rather enjoy this, as I’m passionate about the subject, can usually find ideas to steal become inspired by, and always enjoy a good tech demo.


One of the folks who asked my opinion was Paras Chopra over at [Wingify](http://www.wingify.com).  Wingify is an analytics startup which, from my brief impression of using it, was trying to be an awful lot of things to an awful lot of people.  That is sort of the nature of the beast with enterprise software.  I did the requisite “install the tracking code” thing, commented to Paras that I would have felt a little lost if I didn’t breathe analytics systems, and more or less forgot about it.


But Paras and his team kept iterating and they produced a real gem — probably the best single piece of software I’ve seen in this field.  As Paras explains:


> One of the biggest [lessons] I have had is that there is a huge gap in what we (split testing community) profess and what small businesses actually adopt. I have [learned] that many website owners are curious about split and multivariate testing but don’t have a clue where to start and what to use. Though [the] Google Website Optimizer guys are doing a great job to the community by evangelising split testing, … the difficulty in using the tool and fiddling with code leaves most people wondering how to really [use] testing.


I think this is an extraordinarily good job of learning from your customers, like that “customer development” that seems to be going the rounds these days.  Wingify initially set out to be an enterprise-class analytics system, but when trying to sell it Paras et al found out that the customers *don’t need* an enterprise-class analytics system.  They need the Microsoft Word of Internet marketing, a simple pick-up-and-go tool that you can install, employ, and benefit from without needing cooperation from the operations, marketing, and engineering teams which you either a) don’t have or b) can’t get to do your bidding.


This is sort of like the process I went through with making A/Bingo, except from another direction.  I couldn’t use the market-leader A/B testing tool ([Google Website Optimizer](http://www.google.com/websiteoptimizer)) because it was built for non-technical marketers and made [too many compromises](http://www.bingocardcreator.com/abingo/compare) to be useful for me.  Paras’ customers can’t use GWO because it **isn’t nearly non-technical enough** — it still requires inserting multiple chunks of Javascript code, knowing HTML to make alternatives, being comfortable with regular expressions and URLs, etc.  These aren’t core concerns if your market is Rails developers, but if your market is e.g. real estate agents with 5 page brochureware sites who want to split test the call to action to join their mailing list without having to engage a freelancer to do it, they’re *huge* stumbling blocks.


# Genius UI


[VWO](https://vwo.com) (originally known as Visual Website Optimizer), Wingify’s new product, has such a UI for creating A/B tests so simple it will crush the life out of all other solutions for non-technical users:

1. VWO opens your site in a browser.
2. You click the element on the page you want to A/B test.
3. You click “Add variation.”
4. You add a variation by typing into a WYSIWYG editor.  ([TinyMCE](http://tinymce.moxiecode.com/), if I don’t miss my guess.  Score one for OSS.)
5. Copy/paste the Javascript we give you into your page.  You don’t have to identify sections, massage your HTML, or create alternate URLs.  We do that %(#$ for you.


For example, here is me clicking on the headline for BCC:


And I think I’ll rewrite it to say “PC or Mac” instead of computer.


Dead easy.  The remainder of the process involves a bit of Javascript cut/pasting and some URL specifying.  (The interface for this could still be improved a little bit, to be sure.  I don’t think it is quite at the level where it needs to be for non-technical folks to intuitively grasp it.  But, hey, ship and iterate, right?)


## Why I’m Particularly Impressed With This


Aside from the work going on in the background to make this process so pain-free (that is live, unaltered HTML they’re working with, and I didn’t do anything when coding it to make it particularly easy for them to rewrite the DOM model on the fly with their injected Javascript), this software impresses me as a business.  It solves a clear need for a huge number of small businesses, and brings a powerful technique to people who would never have been able to use it before.  Moreover, it does it so disruptively, *embarrassingly* better than Google does that it puts a smile on my face.  I like Google, don’t get me wrong, they’ve made me a lot of money.  But all the kings horses and all the kings men apparently can’t deliver a UI as good as a small team.


A quick note: Paras et al are from India.  After a few years of doing outsourcing management I’m quite happy to see a young team producing something very worthwhile rather than doing the traditional thing and being a wee little cog in a giant corporation working on grinding out back-office software.  I have to say one thing, though, and it is straight out of the Economic History of Japan playbook: people don’t take copiers seriously, and it is a hard impression to shake once you’ve gotten it attached to you, fairly or otherwise.  The design “inspired by” Basecamp is… ahem…  well, suffice it to say that it does not demonstrate nearly as much originality as the software does.  I’d hate for folks to write this startup off just for that, but first impressions matter.


Rather than taking (deserved) lumps for flying the Jolly Roger, I’d suggest folks to either use an open source web design, one of the attractive reasonably priced templates the Internet is overflowing with, or hire somebody with design skills to bang out something decent for v1.0.  [StyleShout](http://www.styleshout.com/) (OSS) and [ThemeForest](http://themeforest.net/) (paid, but sinfully cheap) both have very attractive Web 2.0-y designs.  After you have revenue you can always improve it to your heart’s content, particularly if you’ve kept the design mostly separate from your program logic.  (A taller order than it needs to be in PHP, I know…)


## Want To Try It Out?


See [VWO](https://vwo.com); it’s easy to get up and running.


I’d expect pricing to be “reasonable”, although my advice (to Paras and anyone else) is to charge more than he thinks it is worth.  Trust me, it would be cheap at ten times the price if it worked for dentist offices, real estate agents, car mechanics, and the other constituents of the Fortune 5 Million.  One conversion at the margin is potentially worth hundreds or thousands of dollars, and even a single lead would pay for a month of most software-as-a-service products.
