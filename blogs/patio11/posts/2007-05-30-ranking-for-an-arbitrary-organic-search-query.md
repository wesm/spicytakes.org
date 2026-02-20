---
title: "Ranking For An Arbitrary Organic Search Query"
date: 2007-05-30
url: https://www.kalzumeus.com/2007/05/30/ranking-for-an-arbitrary-organic-search-query/
slug: ranking-for-an-arbitrary-organic-search-query
word_count: 1116
---


This was posted on May 30th, 2007, Japan time. If it is after June 5th where you are, I predict that I’m pretty high on Google for the search [arbitrary organic search query](http://www.google.com/search?hl=en&c2coff=1&q=arbitrary+organic+search+query&btnG=Search). I know this mostly by construction — I looked at the results before writing this post, observed that the competition is very weak for that query, used those words in my title, and will easily leapfrog over the weak competition.


What does that have to do with microISVs? Well, indulge me in a little meandering around the world of SEO for a moment. Roughly a fifth of my traffic at Bingo Card Creator comes from obvious and highly competitive search terms like “bingo cards” or “bingo card maker”. You know how many people have a substantial monetary interest at being #1 for bingo cards? Plenty of them, and most aren’t selling to elementary school English teachers, if you catch my drift. (Ironically, most of us who actually rank highly *are*. Go figure.)


Then I get another chunk of traffic from less obvious search terms, which I know because I know my niche well. [Dolch Sight Word Bingo](http://www.bingocardcreator.com/dolch-sight-words-bingo.htm), for example. The amount of people searching for that won’t make me rich but they easily justify writing a page about it, which pays off month after month.


Then I get a huge percentage of my organic search traffic, about 60-70%, from arbitrary organic search queries. The majority of them are never repeated by another person, which gells with Google’s observation that 50% of search queries are unique (that is a “remembered factoid”, treat it with a grain of salt). Some are simple typos, many of them are natural language searches (“how can i make a bingo card for a third grader”), and then the rest are just unique because they’re… *unique* (“kasmir pulaski day spanish bingo” — yes, by the way, Bingo Card Creator will meet your needs). I like to mentally think of these as snowflake queries — every one is unique but if you look at a lot of them at once they certainly look a good deal similar.


I have actually been looking at snowflake queries and doing some work based on them. I’ve been doing some minor optimizations to my website for months, gradually including more content (which has a tendency to grab snowflake queries just because educated writers use synonyms and from Google’s perspective third grader != third grader != grade three != beginning English student) and adding in specific vocabulary which I wouldn’t use naturally but which my searchers do for whatever reason. For instance, some people call bingo cards “bingo boards”. Who knew? Certainly not me, as I went through my entire life without hearing that usage, but my search logs do not lie. This is the reason “bingo boards” is now bolded on the front page of my website and sprinkled on a few of the sub pages.


However, I had a bit of a brainstorm recently: this sort of optimization is nice and demonstrably effective, but what would happen if you took it to the next level. The trigger for this was when I wrote the blog post [Increase Your Software Sales](http://microisvjournal.wordpress.com/2007/05/14/increase-your-software-sales/), I mentioned that it would rank pretty highly for “increase software sales”, which would be a nice thing if I cared about that keyword. When I said that, it was mostly a minor boast which I thought of little importance in the scheme of things. But it sent me to thinking:


1) Hey, wait a second, I can rank for a snowflake query with a really trivial amount of work. Put query in title, use in body text, don’t spam, done.


2) I have pages and pages of snowflake queries. Many of them have strong commonality in either words or theme.


3) These queries make me money. Snowflakes account for more than half of my organic search conversions.


And this got the wheels of my head turning. What if, instead of doing the haphazard optimization to grab some of the words in these queries that I wasn’t targetting already (like “bingo boards”), I just data-mined the bejeesus out of the suckers. Say I found 100 strings from there that were reasonably close to each other, distilled that down into 5 main words and 5 supporting words or variations, and then wrote my next resource page or blog post about them. Why, that page or post would probably rocket to near the top of 100 queries. That is worth pure gold, since people will write dozens of minor variations of each of those minor little snowflake queries. And my page or post would suck them all up in one big snowball of goodness.


I was briefly very, very excited about the idea, and started working on a gawk script to start clustering my snowflakes. (Incidentally: by training, I’m a natural language researcher. I know this to be a hard problem and yet hacky solutions to hard problems are fun for me — thats why I got into natural language research in the first place.) Then I slapped myself silly, figuring that somewhere on the Internet somebody smarter than me has already had this brainstorm and developed the same tool. I should really pay them the money for the tool and spend my time actually writing the text which will clump up the snowflakes (which only I can do, since I’m the guy who presumably has the domain knowledge) rather than reinventing a solution to a Certified Hard Problem and then using it to squeeze out an extra sale or two of a $24.95 app a month.


Anyhow, after a bit of searching, it turns out that the guy who already solved this problem made a webapp called [HitTail](http://www.hittail.com/). It has the broad thrust of the features I wanted: tracks what queries get people to find you (unnecessary, I can do that already), and then selectively picks queries out which (the site claims) hit a cluster of snowflakes and are not currently very competitive. I’ll be taking it for a test drive this week.


This is of particular interest for me for my next project ([Kalzumeus](http://microisvjournal.wordpress.com/tags/kalzumeus), for regular readers of this blog). It is adjacent to a market space which is extraordinarily competitive and has many established firms with Big Budget$ To $quash uISVs. I don’t see them as particularly competitive for my niche but I do see them camping on some major keywords (both for organic search and AdWords). Time to go around the obstruction rather than running straight into it. I think I’ll see how far I can get with optimizing for snowflakes, well, once I have something to optimize for at any rate.
