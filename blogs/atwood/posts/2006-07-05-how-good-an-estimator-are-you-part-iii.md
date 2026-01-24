---
title: "How Good an Estimator are You? Part III"
date: 2006-07-05
url: https://blog.codinghorror.com/how-good-an-estimator-are-you-part-iii/
slug: how-good-an-estimator-are-you-part-iii
word_count: 1219
---

For the final installment in the [How Good an Estimator Are You](https://blog.codinghorror.com/how-good-an-estimator-are-you/) series, I’d like to start with an anecdote from chapter 7 of [Software Estimation](http://www.amazon.com/exec/obidos/ASIN/0735605351): Demystifying the Black Art:


> Suppose you’re at a reception for the world’s best software estimators. The room is packed, and you’re seated in the middle of the room at a table with three other estimators. All you can see as you scan the room are wall-to-wall estimators. Suddenly, the emcee steps up to the microphone and say “We need to know exactly how many people are in the room so we can order dessert. Who can give the most accurate estimate for the number of people in the room?”
> Bill, the estimator to your right, says “I make a hobby of estimating crowds. Based on my experience, it looks to me like we’ve got about 335 people in the room.”
> The estimator sitting across the table from you, Karl, says, “This room has 11 tables across and 7 tables deep. One of my friends is a banquet planner, and she told me that they plan for 5 people per table. It looks to me like most of the tables do actually have about 5 people at them. If we multiply 11 times 7 times 5, we get 385 people. I think we should use that as our estimate.”
> The estimator on your left, Lucy, says, “I noticed on the way into the room that there was an occupancy limit sign that says this room can hold 485 people. This room is pretty full. I’d say 70 to 80 percent full. If we multiply those percentages by the room limit, we get 340 to 388 people. How about if we use the average of 364 people, or maybe just simplify it to 365?”
> Bill says, “We have estimates of 335, 365, and 385. It seems like the right answer must be in there somewhere. I’m comfortable with 365.”
> Everyone looks at you. You say, “I need to check something. Would you excuse me for a minute?”
> You return a few minutes later. “Remember how we had to have our tickets scanned before we entered the room? I noticed on my way into the room that the handheld ticket scanner had a counter. So I went back and talked to the ticket taker at the front door. She said that, according to her scanner, she has scanned 407 tickets. She also said no one has left the room so far. I think we should use 407 as our estimate. What do you say?”


The moral of this story, of course, is that **you should avoid estimating what you can count.** And if you can’t get a count, you should at least try to **compute the estimate from a related count**, like Karl did in the anecdote above. The absolute worst estimates you can produce are judgmental – estimates that are not derived from an actual count of any kind.


The real art of software estimation, then, is the frantic search for data points to hang your estimates on. Hopefully you’re fortunate enough to work for an organization that captures historical data for your projects.


What kind of stuff can you count on a software project? Lots of stuff, actually:

- Marketing requirements
- Features
- Use cases
- Stories
- Engineering requirements
- Function points
- Change requests
- Web pages
- Reports
- Dialog boxes
- Database tables (or procs, views, etc.)
- Classes
- Defects found
- Configuration settings
- Lines of code
- Test cases
- Code churn


One reason I’m working so closely with Team System these days is that it makes capturing some of these metrics (almost) effortless.


The art of building an estimate from known reference points isn’t a new topic in computer science. One of my favorite chapters in [Programming Pearls](http://www.amazon.com/exec/obidos/ASIN/0201657880) is about how essential back of the envelope calculations are to software development:


> It was in the middle of a fascinating conversation on software engineering that Bob Martin asked me, “How much water flows out of the Mississippi River in a day?” Because I had found his comments up to that point deeply insightful, I politely stifled my true response and said, “Pardon me?” When he asked again I realized that I had no choice but to humor the poor fellow, who had obviously cracked under the pressures of running a large software shop.
> My response went something like this. I figured that near its mouth the river was about a mile wide and maybe twenty feet deep (or about one two-hundred-and-fiftieth of a mile). I guessed that the rate of flow was five miles an hour, or a hundred and twenty miles per day. Multiplying
> 1 mile x 1/250 mile x 120 miles/day ~ 1/2 mile3/day
> showed that the river discharged about half a cubic mile of water per day, to within an order of magnitude. But so what?
> At that point Martin picked up from his desk a proposal for the communication system that his organization was building for the Summer Olympic games, and went through a similar sequence of calculations. He estimated one key parameter as we spoke by measuring the time required to send himself a one-character piece of mail. The rest of his numbers were straight from the proposal and therefore quite precise. His calculations were just as simple as those about the Mississippi River and much more revealing. They showed that, under generous assumptions, the proposed system could work only if there were at least a hundred and twenty seconds in each minute. He had sent the design back to the drawing board the previous day. (The conversation took place about a year before the event, and the final system was used during the Olympics without a hitch.)
> That was Bob Martin’s wonderful (if eccentric) way of introducing the engineering technique of “back-of-the-envelope” calculations. The idea is standard fare in engineering schools and is bread and butter for most practicing engineers. Unfortunately, it is too often neglected in computing.


Steve Bush, in a recent comment, pointed out that physicist [Enrico Fermi](http://en.wikipedia.org/wiki/Enrico_Fermi) was famed for these kinds of calculations, and apparently Fermi coined the phrase “[back-of-the-envelope calculation](http://en.wikipedia.org/wiki/Back-of-the-envelope_calculation).”


These calculations are typically represented in the form of Fermi Questions; the canonical Fermi Question is [How many piano tuners are there in Chicago?](http://www.grc.nasa.gov/WWW/K-12/Numbers/Math/Mathematical_Thinking/fermis_piano_tuner.htm)

- From the almanac, we know that Chicago has a population of about 3 million people.
- Assume that an average family contains four members. The number of families in Chicago is about 750,000.
- If one in five families owns a piano, there will be 150,000 pianos in Chicago.
- If the average piano tuner serviced four pianos every day of the week for five days, rested on weekends, and had a two week vacation during the summer, then in one year (52 weeks) he would service 1,000 pianos.
- 150,000 / (4 x 5 x 50) = 150
- there are ~150 piano tuners in Chicago


Fermi questions are interesting, because the actual answer to the question is secondary to the process of how you arrived at the answer. **Did you guess? Or did you *estimate?***

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[estimation](https://blog.codinghorror.com/tag/estimation/)
[software estimation](https://blog.codinghorror.com/tag/software-estimation/)
[black art](https://blog.codinghorror.com/tag/black-art/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
