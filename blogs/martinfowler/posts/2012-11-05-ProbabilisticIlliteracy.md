---
title: "Probabilistic Illiteracy"
description: "As I write this towards the conclusion of the US presidential   election ,   there's a side debate that's appeared about the forecasts produced   byNate   Silver. Many Republicans claim he's a   shill"
date: 2012-11-05T00:00:00
tags: ["data analytics"]
url: https://martinfowler.com/bliki/ProbabilisticIlliteracy.html
slug: ProbabilisticIlliteracy
word_count: 1615
---


As I write this towards the conclusion of the US presidential
  election 1,
  there's a side debate that's appeared about the forecasts produced
  by [Nate
  Silver](http://fivethirtyeight.blogs.nytimes.com). Many Republicans claim he's a
  shill for the democrats and his forecast of an 85% chance of an
  Obama win is bogus 2. Part of me wishes I knew
  more innumerate Republicans that I could make side-bets
  with. Perhaps a better wish would be that the polls were the other
  way around as I have more Democratic-leaning friends. In reality
  either way I wouldn't gain too much as most people I know are
  numerate. Sadly this isn't true in general - this side-show is an
  illustration of the deep illiteracy most people have for
  probability, which has some important ramifications for society in
  general and software development in particular.


1: 
      I made a deliberate point of writing this before the election.
      My point being that the result doesn't affect the issues I'm
      talking about here.


2: 
      This is from the [538 blog](http://fivethirtyeight.blogs.nytimes.com) on
      Sunday November 4th. The forecast changes regularly as he
      re-runs his model with recent data. Other references to published
      forecasts also refer to that same day, when I first drafted this article.


As I've been reading around this, it's not hard to find evidence
  of probabilistic illiteracy:

- Many people claim that Silver is predicting an Obama victory.
    This isn't true, Silver is saying his model forecasts an 85%
    chance of an Obama victory, which is not at all the same thing.
    (It's roughly equivalent to saying that Romney will win if he
    takes a die and rolls a 6, which is really not that
    unlikely. 3)
- It's said that you shouldn't listen to Silver because polls
    are often wrong, but Silver states his model does attempt to take this into
    account. Silver says the polls confidently state an Obama victory,
    but his model gives Romney a 15% chance of a win because [that's
    the chance that the polls are wrong](http://fivethirtyeight.blogs.nytimes.com/2012/11/03/nov-2-for-romney-to-win-state-polls-must-be-statistically-biased/).
- People claim that Silver will be proven right or wrong on
    Tuesday when the election is held. But one event cannot say much
    about an underlying distribution. You'd have to hold many tens of
    elections to really test the model. 4


This side-debate has caught my interest because it taps many of what I
  see as fundamental problems people have with understanding
  probabilities and how to use them properly. To begin with there's
  the matter of certainty - people want to hear a binary answer rather
  than a probabilistic one. We see this, of course, in project
  planning where people want firm numbers rather than ranges and
  probability estimates for various outcomes. That difference between
  85% and 100% can lead to some serious errors. I've developed a
  strong distrust of certainty, to the point that the more certain
  someone seems to be, the less I'm inclined to believe them. 5


5: 
      And yes, that includes myself.


One aspect of this dispute is how you should use the poll
  information to make forecasts. If I head over to [RealClearPolitics](http://www.realclearpolitics.com/) today, I
  see the election as a âtoss-upâ, because a critical 11 states are
  marked as âtoss-upsâ in their analysis. Silver says that this
  conclusion is profoundly wrong. RCP's current poll average shows a
  3.9% average poll lead for Obama in Ohio. Silver argues that when you
  average these multiple polls, the margin of error due to statistical
  sampling [is
  about 1.5%](http://fivethirtyeight.blogs.nytimes.com/2012/11/03/nov-2-for-romney-to-win-state-polls-must-be-statistically-biased/) - so if the polls are accurate Obama will win in Ohio
  (and you certainly can't call Ohio a toss-up, which implies 50%
  odds).


There are many reasons why people are implying this race has
  tighter probabilities than Silver does. Some are reasonable, such as
  disagreements about the model Silver uses for his forecast. Some are
  less reasonable: people are afraid of being seen to be wrong, they
  are indulging in partisan cheerleading 6, or they
  want make the race seem more exciting in order to gain eyeballs.


6: 
      Many Republicans claim that Silver is only publishing the
      figures he gets because he is personally biased in favor of the
      Democrats. Personal bias always affects peoples' thinking, but
      there is an important difference between those who embrace their
      biases and those who strive to be objective. Silver has talked a
      lot about his model and how it works (although sadly it isn't
      open-source). There's no indication in his discussion of a
      conscious bias, indeed his odds give a [higher
      chance to Romney than similar analyses](http://www.washingtonpost.com/blogs/ezra-klein/wp/2012/10/31/nate-silver-and-the-forecasting-consensus-in-one-chart/) While absolute
      objectivity is impossible, if you make the effort it is possible 
      to get closer to objectivity than just wallowing in your
      prejudices.


One argument is that this inappropriate use of âtoss-upâ is a
  consequence of probabilistic illiteracy. Since people don't
  understand what 85% means, then we'll call it a toss-up. As there's
  plenty of empirical evidence for this confusion, I have some
  sympathy for this argument.


But the real issue here is the underlying probabilistic
  illiteracy. Increasingly we are faced with a world where
  understanding probabilities matters. Understanding how probability
  works is a vital underpinning to making sense of statistics - and
  statistics is a key tool to understanding how to make sense of much
  of the data that is now available to us. This can make global sense
  (much of the debate about climate change is based on statistics) and
  but also matters in more local circumstances.


I'm of the opinion that we are seeing [an important shift in the
  role that data can play in our lives](http://www.infoq.com/presentations/The-Evolving-Panorama-of-Data). For software developers, this
  means that more of our work is going to be about making sense of
  this deluge of data. An important part of this is helping people to see
  the difference between signal and noise - which is going to require
  a better understanding of the probability and statistics required to
  separate the two. As software professionals, we need to take a lead
  in this so we can fulfill our duty to avoid distorting information,
  we also need to educate consumers of our data so that they can better
  interpret it. 7


7: 
      This may be one benefit of this controversy - more attention
      paid to these techniques, so that more people learn how they
      work and how to interpret them.


## Further Reading

- Well not actually reading, but one of my favorite
      introductions to probabilistic illiteracy is [Stochasticity](http://www.radiolab.org/2009/jun/15/) - a
      wonderful episode of Radiolab.
- And this gives me another opportunity to recommend [Thinking Fast and
  Slow](https://www.amazon.com/gp/product/0374275637/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0374275637&linkCode=as2&tag=martinfowlerc-20)
- The thing I've most appreciated from the [538 blog](http://fivethirtyeight.blogs.nytimes.com) is how
      he discusses how his forecasting is done, including the various
      areas of uncertainty. Silver has written a [recent book on predication models](https://www.amazon.com/gp/product/159420411X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=159420411X&linkCode=as2&tag=martinfowlerc-20) - I
      haven't had chance to read it yet, but it's on my list.
- Although it's 538 that been getting a lot of the attention
      lately, a couple of similar approaches are [Princeton Election
      Consortium](http://election.princeton.edu) (led by Sam Wang), [DeSart and
      Holbrook](http://research.uvu.edu/DeSart/forecasting/), [Gott and
      Colley](http://www.colleyrankings.com/election2012/), and [Drew Linzer
      (Votamatic)](http://votamatic.org). Sam Wang has an excellent [comparison
      of these models](http://election.princeton.edu/2012/11/04/comparisons-among-aggregators-and-modelers/). 8


## Notes


1: 
      I made a deliberate point of writing this before the election.
      My point being that the result doesn't affect the issues I'm
      talking about here.


2: 
      This is from the [538 blog](http://fivethirtyeight.blogs.nytimes.com) on
      Sunday November 4th. The forecast changes regularly as he
      re-runs his model with recent data. Other references to published
      forecasts also refer to that same day, when I first drafted this article.


3: 
      That is, of course, a 6-sided die. I have to say this as I'm
      sure this article is read by many people who, like myself, are
      familiar with more esoteric dice. Silver also had another
      probabilist analogy, saying it was like an [NFL
      team being ahead by a field goal with three minutes left to
      play.](http://fivethirtyeight.blogs.nytimes.com/2012/11/01/oct-31-obamas-electoral-college-firewall-holding-in-polls/) (I'll leave that one in for the jocks in the
      audience.)


4: 
      I can't be bothered to figure out how many elections you'd need,
      but know enough to know that you can do this with the right
      statistical techniques - and that the answer only provides a
      probabilistic indication of confidence.


5: 
      And yes, that includes myself.


6: 
      Many Republicans claim that Silver is only publishing the
      figures he gets because he is personally biased in favor of the
      Democrats. Personal bias always affects peoples' thinking, but
      there is an important difference between those who embrace their
      biases and those who strive to be objective. Silver has talked a
      lot about his model and how it works (although sadly it isn't
      open-source). There's no indication in his discussion of a
      conscious bias, indeed his odds give a [higher
      chance to Romney than similar analyses](http://www.washingtonpost.com/blogs/ezra-klein/wp/2012/10/31/nate-silver-and-the-forecasting-consensus-in-one-chart/) While absolute
      objectivity is impossible, if you make the effort it is possible 
      to get closer to objectivity than just wallowing in your
      prejudices.


7: 
      This may be one benefit of this controversy - more attention
      paid to these techniques, so that more people learn how they
      work and how to interpret them.


8: 
      One counter that I've seen to all these poll-based models is
      that of [Bickers and Berry](http://www.colorado.edu/news/releases/2012/10/04/updated-election-forecasting-model-still-points-romney-win-university), which predicted a Romney
      victory. They don't use polls, but base their model on economic
      fundamentals. Their prediction jives well with my instinct - I
      confidently predicted that Obama would be a one-term president
      from the day he was elected. This prediction wasn't due to
      anything he might do, but just because he was elected too soon
      in the economic cycle for the economy to improve enough before
      2012 for him to have a chance of being re-elected. If he does
      get re-elected, contrary to Bickers and Berry, I would
      argue that this suggests the Republicans have badly misplayed a
      winning hand.
