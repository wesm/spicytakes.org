---
title: "Human Task Switches Considered Harmful"
date: 2001-02-12
url: https://www.joelonsoftware.com/2001/02/12/human-task-switches-considered-harmful/
word_count: 1222
---


When you’re managing a team of programmers, one of the first things you have to learn to get right is task allocation. That’s just a five-dollar word for *giving people things to do*. It’s known colloquially as “file dumping” in Hebrew (because you dump files in peoples’ laps). And how you decide which files to dump in which laps is one of the areas where you can get incredible productivity benefits if you do it right. Do it wrong, and you can create one of those gnarly situations where nobody gets anything accomplished and everybody complains that “nothing ever gets done around here.”


Since this site is for programmers, I’m going to warm up your brains a little bit with a programming problem.


Suppose you have two separate computations to perform, A and B. Each computation requires 10 seconds of CPU time. You have one CPU which, for the sake of this problem, doesn’t have anything else in the queue.


On our CPU, multitasking is optional. So you can either do these computations one after the other…


Sequential Processing



| Computation A | Computation B |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |



… or, you can multitask. If you multitask, on this particular CPU, tasks run for 1 second at a time, and a task switch takes no time at all.


Multitasking



| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |



Which would you rather do?  Most people’s gut reaction is that multitasking is better. In both cases, you have to wait 20 seconds to get both of your answers. But think about how long it takes to get the results to *each *computation.


In both cases, the results of Computation B (shown in blue) take 20 seconds to arrive. But look at Computation A. With multitasking, its results take 19 seconds to arrive… yet with sequential processing they are ready in only 10 seconds.


In other words, in this nice contrived example, the *average time per computation* is lower (15 seconds rather than 19.5 seconds) when you do sequential processing rather than multitasking. (Actually, it’s not such a contrived example — it’s based on a real problem Jared had to solve at work).



| **Method** | **Computation A takes** | **Computation B takes** | **Average** |
| Sequential | 10 seconds | 20 seconds | 15 |
| Multitasking | 19 seconds | 20 seconds | 19.5 |



Earlier I said that “a task switch takes no time at all.” Actually, on real CPUs, a task switch takes a little bit of time… basically enough time to save out the state of the CPU registers and load the CPU registers for the other task. Realistically, this is as close to negligible as possible. But to make life interesting, let’s imagine that task switches take half a second. Now things look even worse:



| **Method** | **Computation A takes** | **Computation B takes** | **Average** |
| Sequential | 10 seconds | 20 + 1 task switch = 
20.5 seconds | 15.25 |
| Multitasking | 19 + 18 task switches =
28 seconds | 20 + 19 task switches = 29.5 seconds | 28.75 |



Now … just humor me, I know this is silly … what if task switches take a whole minute?



| **Method** | **Computation A takes** | **Computation B takes** | **Average** |
| Sequential | 10 seconds | 20 + 1 task switch = 
80 seconds | 45 seconds |
| Multitasking | 19 + 18 task switches =
1099 seconds | 20 + 19 task switches = 1160 seconds | almost 19 minutes! |



The longer a task switch takes, the worse the multitasking penalty.


That, in and of itself, is not so earth shaking, is it? Pretty soon I’m going to be getting irate email from morons accusing me of being “against” multitasking. “Do you want to go back to the days of DOS when you had to exit WordPerfect to run 1-2-3?” they will ask me.


But that’s not my point. I just want you to agree with me that in this kind of example:


> a) sequential processing gets you results faster *on average*, and
> b) the longer it takes to task switch, the bigger the penalty you pay for multitasking.


OK, back to the more interesting topic of managing humans, not CPUs. The trick here is that when you manage *programmers*, specifically, task switches take a really, really, really long time. That’s because programming is the kind of task where you have to keep a lot of things in your head at once. The more things you remember at once, the more productive you are at programming. A programmer coding at full throttle is keeping zillions of things in their head at once: everything from names of variables, data structures, important APIs, the names of utility functions that they wrote and call a lot, even the name of the subdirectory where they store their source code. If you send that programmer to Crete for a three week vacation, they will forget it *all*. The human brain seems to move it out of short-term RAM and swaps it out onto a backup tape where it takes forever to retrieve.


How long? Well, [my software company](http://www.fogcreek.com/) recently dropped what we were doing (developing a software product codenamed CityDesk) to help a client with a bit of an emergency situation for three weeks. When we got back to the office, it seemed to take *another* three weeks to get back to full speed on CityDesk.


On the individual level — have you ever noticed that you can assign one job to one person, and they’ll do a great job, but if you assign *two* jobs to that person, they won’t really get anything done? They’ll either do one job well and neglect the other, or they’ll do both jobs so slowly you feel like *slugs* have more zip. That’s because programming tasks take so long to task switch. I feel like when I have two programming projects on my plate at once, the task switch time is something like 6 hours. In an 8-hour day, that means multitasking reduces my productivity to 2 hours per day. Pretty dismal.


As it turns out, if you give somebody two things to work on, you should be grateful if they “starve” one task and only work on one, because they’re going to get more stuff done and finish the average task sooner. In fact, the real lesson from all this is that you should **never let people work on more than one thing at once.** Make sure they know what it is. Good managers see their responsibility as *removing obstacles* so that people can focus on *one thing* and really get it done. When emergencies come up, think about whether you can handle it yourself before you delegate it to a programmer who is deeply submersed in a project.
