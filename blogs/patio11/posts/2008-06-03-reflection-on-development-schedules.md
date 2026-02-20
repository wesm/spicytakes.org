---
title: "Reflection on Development Schedules"
date: 2008-06-03
url: https://www.kalzumeus.com/2008/06/03/reflection-on-development-schedules/
slug: reflection-on-development-schedules
word_count: 340
---


This was much easier last time, when I was at the job which got out at 4:30 and has a 20 minute commute, rather than the one that got out at 9:00 with the 2 hour commute…


While I didn’t get anything done for myself today, I did manage to put some of the finishing touches on the best 800 lines of code I’ve ever written.  Sadly the day job owns it so I can’t go around showing it off, but darn, when all six hundred automated tests worked it was a beautiful, beautiful thing.  Its probably one of the few times where I actually got to put my CS degree qua CS degree to use, rather than just using programming skills.


Let’s see, what would have the same complexity.  OK, imagine you own a zoo.  The zoo has many families of animals.  Each family is composed of several individual types of animals.  The zoo has to fill certain exhibits, given constraints like “This exhibit needs at least one animal from the family of cats, one animal from the family of turtles, and two animals from the family of rodents of which at least one is not a rabbit”.  Each exhibit is in an enclosure, of which the number is strictly limited.


Certain animals eat each other, and as a result can’t be placed in the same enclosure.


Your tasks:


#1 — I give you an exhibit and a list of animals the zoo has on hand.  You tell me what animals I can put in the exhibit to satisfy it.


#2 — As #1, except there are 2 exhibits with 1 enclosure and a limit on space, and your solution must be correct for any possible exhibit (and correctly report “impossible” as well).


#3 — Here’s the freaking zoo.  Enumerate all possible states of it.


I’ll admit — I stayed a little later than I was planning not so much because this was urgent to get done today but because I was so close to beating the stupid thing.
