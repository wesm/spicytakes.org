---
title: "Gerrymandering algorithms"
date: 2016-06-22
url: https://mathbabe.org/2016/06/22/gerrymandering-algorithms/
word_count: 846
---


I’ve been thinking about gerrymandering recently, specifically how to design algorithms to gerrymander and to detect gerrymandering.


**Whence “Gerrymander”?**


First thing’s first. According to [wikipedia](https://en.wikipedia.org/wiki/Gerrymandering) (and my friend Michael Thaddeus), the term “Gerrymander” is a mash-up of a dude named Elbridge Gerry and the word “salamander.” It was concocted when Gerry got made fun of for his crazy districting of Massachusetts back in 1812 to push out the power of the Federalists:


![800px-The_Gerry-Mander_Edit](https://mathbabe.org/wp-content/uploads/2016/06/800px-the_gerry-mander_edit.png?w=595)


It’s true, this is depicted as a dragon. But believe me, someone thought it looked like a salamander.


**How To Gerrymander**


Think about it. In this crazy pseudo-democratic world of ours, we’re still voting locally and asking delegates to ride their horses to a centralized location to cast a vote for the group. The system was invented well before the internet, and it is a ridiculous and unnecessary artifact from the days when information didn’t travel well. In particular, it means you can manipulate voting at the local level, by gaming the definition of the district boundaries.


So, let’s imagine you’re in charge of drawing up districts, and you want to rig it for your party. That means you’d like your party to win as often as possible and lose as seldom as possible per district. If you think about it for a while, you’ll come up with the following observation: you should win by a thin margin but lose huge.


Theoretically that would mean building districts – a lot of them – that are 51% in your favor, and then other districts that are 100% against you.


In reality, you can’t count on anything these days, so you might want to create slightly wider margins, of maybe 55% your party, and there might be rules about how connected districts must be, so you’ll never achieve 100% loss districts.


![disconnected_voter_district](https://mathbabe.org/wp-content/uploads/2016/06/disconnected_voter_district.jpg?w=595)


Although clearly [not very hard and fast rules](https://pjmedia.com/zombie/2010/11/11/the-top-ten-most-gerrymandered-congressional-districts-in-the-united-states/).


**How Not To Gerrymander**


On the other side of the same question, we might ask ourselves, is there a better way? And the answer is, absolutely yes. Besides just counting all votes equally, we could draw up districts to contain similar numbers of voters and to be more or less “compact.”


If you don’t know what that really means, you can go [look at the work of a computer nerd named Brian Olsen](https://www.washingtonpost.com/news/wonk/wp/2014/06/03/this-computer-programmer-solved-gerrymandering-in-his-spare-time/), who built a program to do just this.


![Screen Shot 2016-06-22 at 7.43.40 AM](https://mathbabe.org/wp-content/uploads/2016/06/screen-shot-2016-06-22-at-7-43-40-am.png?w=595)


Before and after Brian Olsen gets his hands on Pennsylvania


**Detecting Gerrymandering**


The concept of compactness is pretty convincing, and has led some to define gerrymandering to be, in effect, a measurement of the compactness of districts. More formally, [there’s a so-called “Gerrymander Score”](http://www.motherjones.com/politics/2010/09/gerrymandering-math) that is defined as the ratio of the perimeter to the area of districts, with some fudge factor which allows for things like rivers and coastlines.


Another approach is a “Gerrymander statistical bias” test, namely the difference between the mean and the median. Here you take the results of an election by district, and you rank them from lowest to highest for your party. So there might be a district that only voted 4% for your party, and it might go on the left end, and on the other end the district that voted 95% for your party would be on the other end. Now look at the “middle” district, and see how much that district voted for your party. Say it’s 47%. Then, if your party won 55% of the vote overall in the state – the mean in this case is 55% – there’s a big difference between 55 and 47, and you can perhaps cry foul.


I mean, this seems like a pretty good test, since if you think back to what we would do to gerrymander, in the ideal world (for us) we’d get a bunch of districts with 45% for the other side and then a few with 99% for the other side, and the median would be 45% even if the other side had way more voters overall.


**Problems With Gerrymandering Detection **


There’s a problem, though, [which was detected by, among other people, political scientists Jowei Chen and Jonathan Rodden](http://web.stanford.edu/~jrodden/wp/florida.pdf). Namely, if you run scenarios on non-gerrymandered, compact districts, you don’t get very “fair” results as defined by the above statistical bias test.


This is because, in reality, Democrats are *more clustered* than Republicans. Democrats are quite concentrated in cities and college towns, and then they are more sparse elsewhere. They, in essence, gerrymander themselves.


Said another way, if you build naive districts that are compact (so their Gerrymander Scores are good) then there will be automatic “Gerrymander statistical bias” problems. Oy vey.


Which is not to say that there isn’t actual effective and nasty Gerrymandering going on. There is, in [North Carolina, Florida, Pennsylvania, Texas and Michigan for the Republicans and in California, Maryland and Illinois for the Democrats](http://www.nytimes.com/2014/01/26/opinion/sunday/its-the-geography-stupid.html?_r=0).


But what it means overall is that there’s no reason to believe we’ll ever get out of this stupid districting system, because it gives an inherent advantage to Republicans. So why would they agree to tossing it?
