---
title: "The SHSAT matching algorithm isn’t that hard"
date: 2016-01-15
url: https://mathbabe.org/2016/01/15/the-shsat-matching-algorithm-isnt-that-hard/
word_count: 595
---


My 13-year-old took the SHSAT in November, but we haven’t heard the results yet. In fact we’re expecting to wait two more months before we do.


What gives? Is it really that complicated to match kids to test schools?


A bit of background. In New York City, kids write down a list of their preferred public high schools that are not “SHSAT” schools. Separately, if they decide to take the SHSAT, they rank their preferences for those, which fall into a separate category and which include Stuyvesant and Bronx Science. They are promised that they will get into the first school on the list that their SHSAT score allows them to.


I often hear people say that the algorithm to figure out what SHSAT school a given kid gets into is super complicated and that’s why it takes 4 months to find out the results. But yesterday at lunch, my husband and I proved that theory incorrect by coming up with a really dumb way of doing it.

1. First, score all the tests. This is the time-consuming part of the process, but I assume it’s automatically done by a machine somewhere in a huge DOE building in Brooklyn that I’ve heard about.
2. Next, rank the kids according to score, highest first. Think of it as kids waiting in line at a supermarket check-out line, but in this scenario they just get their school assignment.
3. Next, repeat the following step until all the schools are filled: take the first kid in line and give them their highest pick. Before moving on to the next kid, check to see if you just gave away the last possible slot to that particular school. If so, label that school with the score of that kid (it will be the cutoff score) and make everyone still in line erase that school from their list because it’s full and no longer available.
4. By construction, every kid gets the top school that their score warranted, so you’re done.


A few notes and one caveat to this:

1. Any kid with no schools in their list, either because they didn’t score high enough for the cutoffs or because the schools all filled up before they got to the head of the line, won’t get into an SHSAT school.
2. The above algorithm would take very little time to actually run. As in, 5 minutes of computer time once the tests are scored.
3. One caveat: I’m pretty sure they need to make sure that two kids with the same exact score and the same preference would both either get in or get out (because think of the lawsuit if not). So the actual way you’d implement the algorithm is when you ask for the next kid in line, you’d also ask for any other kid with the same score and the same top choice to step forward. Then you’d decide whether there’s room for the whole group or not.


So, why the long wait? I’m pretty sure it’s because the other public schools, the ones where there’s no SHSAT exam to get in (but there are myriad other requirements and processes involved, see e.g. page 4 of [this document](https://steinhardt.nyu.edu/scmsAdmin/media/users/ggg5/HSChoiceReport-April2013.pdf)) don’t want people to be notified of their SHSAT placement 4 months before they get their say. It would foster too much unfair competition between the systems.


Finally, I’m guessing the algorithm for matching non-SHSAT schools is actually pretty complicated, which is I think why people keep talking about a “super complex algorithm.” It’s just not associated to the SHSAT.
