---
title: "How Do We Trust Our Science Code?"
date: 2017-08-14
url: https://www.hillelwayne.com/post/how-do-we-trust-science-code/
slug: how-do-we-trust-science-code
word_count: 486
---

In 2010 Carmen Reinhart and Kenneth Rogoff published [Growth in a Time of Debt](http://scholar.harvard.edu/files/rogoff/files/growth_in_time_debt_aer.pdf). It’s arguably one of the most influential economics papers of the decade, convincing the IMF to push austerity measures in the European debt crisis. It was a very, very big deal.


In 2013 they shared their code with another team, [who quickly found a bug](http://www.nytimes.com/2013/04/19/opinion/krugman-the-excel-depression.html). Once corrected, the results disappeared.


Greece took on austerity because of a software bug. That’s pretty fucked up.


Programming is now essential to scientific research. Pretty much every policy, econ, and sociology grad student I know has used Python or Excel at least once, to say nothing of the hard scientists out there. For most them coding is not interesting. Their job is research, not fighting weird computer bullshit. Knowing shell arcana is as little a part of their world as grantwriting is to me. They want to hammer out some code, get some results, and get back to their work.


In 2015 a well-known fintech company accidentally introduced hundreds of mock applicants into their production database. For months their credit models were completely wrong and nobody noticed. This was a disciplined engineering team who documented carefully, practiced TDD, and ran rigorous code reviews. Even with all of that, serious bugs can slip through. Software engineers know this.


How many bugs happen when you don’t use any of that? Hell, how many bugs happen when you don’t use functions, descriptive variables, or comments?


So how do we fix this? No clue. Obviously we have the technical tools: tests, code reviews, etc. But how do you convince everyone to make a boring, frustrating part of their work more boring and frustrating for such a nebulous benefit? Most researchers don’t worry about this. Neither did Reinhart.


This is a social problem, not a technical one. Which is why I don’t have a good answer. Watching engineers try to solve social problems is either tragic or hilarious, depending on how far you are from the explosion.


The only thing I can think of is to have all papers include their source code. That way other people can help you find any bugs. Not a great solution, but at least it’s something. This is something a lot of researchers want and many are quite happy to share their code. There’s no way to do it simply and at scale, though. Every journal has different means of distributing code, if they require open code at all. I don’t think this would be an easy fix, or even a painless one.1


If you have any ideas, feel free tell me about them. Being paranoid about science isn’t fun.


*Thanks to [Daiyi](http://www.daiyi.co/), Elliot Abrams, and Sasha Ayvazov for their feedback.*


---

1. “What about Github?” Two problems: first, git is notoriously difficult to learn; second, a *lot* of people are going to accidentally upload private info. Remember, we’re working with scientists, not programmers.
 [return]
