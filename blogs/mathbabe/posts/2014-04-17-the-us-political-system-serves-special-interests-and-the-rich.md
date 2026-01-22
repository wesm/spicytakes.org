---
title: "The US political system serves special interests and the rich"
date: 2014-04-17
url: https://mathbabe.org/2014/04/17/the-us-political-system-serves-special-interests-and-the-rich/
word_count: 706
---


A paper written by [Martin Gilens](http://scholar.princeton.edu/mgilens) and [Benjamin Page](http://www.polisci.northwestern.edu/people/page.html) and entitled *[Testing Theories of American Politics:](http://www.princeton.edu/~mgilens/Gilens%20homepage%20materials/Gilens%20and%20Page/Gilens%20and%20Page%202014-Testing%20Theories%203-7-14.pdf) *[*Elites, Interest Groups, and Average Citizens*](http://www.princeton.edu/~mgilens/Gilens%20homepage%20materials/Gilens%20and%20Page/Gilens%20and%20Page%202014-Testing%20Theories%203-7-14.pdf) has been recently released [and reported on](http://www.telegraph.co.uk/news/worldnews/northamerica/usa/10769041/The-US-is-an-oligarchy-study-concludes.html) (h/t Michael Crimmins) that studies who has influence on policy in the United States.


Here’s an excerpt from the abstract of the paper:


> Multivariate analysis indicates that economic elites and organized groups representing business interests have substantial independent impacts on U.S. government policy, while average citizens and mass-based interest groups have little or no independent influence.


A word about “little or no independent influence”: the above should be interpreted to mean that average citizens and mass-based groups only win when their interests align with economic elites, which happens sometimes, or business interests, which rarely happens. It doesn’t mean that average citizens and mass-based interest groups never ever get what they want.


There’s actually a lot more to the abstract, about abstract concepts of political influence, but I’m ignoring that to get to the data and the model.


**The data**


The found lots of polls on specific issues that were yes/no and included information about income to determine what poor people (10th percentile) thought about a specific issue, what an average (median income) person thought, and what a wealthy (90th percentile) person thought. They independently corroborated that their definition of wealthy was highly correlated, in terms of opinion, to other stronger (98th percentile) definitions. In fact they make the case that using 90th percentile instead of 98th actually underestimates the influence of wealthy people.


For the sake of interest groups and their opinions on public policy, they had a list of 43 interest groups (consisting of 29 business groups, 11 mass-based groups, and 3 others) that they considered “powerful” and they used domain expertise to estimate how many would oppose or be in favor of a given issue, and more or less took the difference, although they actually did something a bit fancier to reduce the influence of outliers:


Net Interest Group Alignment = ln(# Strongly Favor + [0.5 * # Somewhat Favor] + 1) – ln(#

Strongly Oppose + [0.5 * # Somewhat Oppose] + 1).


Finally, they pored over records to see what policy changes were actually made in the 4 year period after the polls.


**Statistics**


The different groups had opinions that were sometimes highly correlated:


Note the low correlation between mass public interest groups (like unions, pro-life, NRA, etc) and average citizens’ preferences and the negative correlation between business interests and elites’ preferences.


Next they did three bivariate regressions, measuring the influence of each of the groups separately, as well as one including all three, and got the following:


This is where we get our conclusion that average citizens don’t have independent influence, because of this near-zero coefficient in Model 4. But note that if we ignore elites and interest groups, we do have 0.64 in Model 1, which indicates that preferences of the average citizens are correlated with outcomes.


The overall conclusion is that policy changes are determined by the elites and the interest groups.


We can divide the interest groups into business versus mass-based and check out how the influence is divided between the four defined groups:


**Caveats**


This stuff might depend a lot on various choices the modelers made as well as their proxies. It doesn’t pick up on smaller special interest groups. It doesn’t account for all possible sources of influence and so on. I’d love to see it redone with other choices. But I’m impressed anyway with all the work they put into this.


I’ll let the authors have the last word:


> What do our findings say about democracy in America? They certainly constitute troubling news for advocates of “populistic” democracy, who want governments to respond primarily or exclusively to the policy preferences of their citizens. In the United States, our findings indicate, the majority does not rule — at least not in the causal sense of actually determining policy outcomes. When a majority of citizens disagrees with economic elites and/or with organized interests, they generally lose. Moreover, because of the strong status quo bias built into the U.S. political system, even when fairly large majorities of Americans favor policy change, they generally do not get it.
