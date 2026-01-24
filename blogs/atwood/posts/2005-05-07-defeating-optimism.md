---
title: "Defeating Optimism"
date: 2005-05-07
url: https://blog.codinghorror.com/defeating-optimism/
slug: defeating-optimism
word_count: 932
---

In [Extreme Programming Explained](http://www.amazon.com/exec/obidos/ASIN/0321278658/), Kent Beck notes that optimism is an occupational hazard of programming. Excess optimism, in the guise of enthusiasm, is a serious [pitfall for game developers](https://web.archive.org/web/20050527122025/http://www.gamasutra.com/features/20031226/fristrom_pfv.htm) in particular:

kg-card-begin: html

> Rein in enthusiasm? Now why would we ever want to do that? Isn’t keeping the team motivated one of the most important factors of game development? Doesn’t every management book you’ve ever read stress how important it is to keep the team motivated? The thing is, almost by definition, videogame developers are motivated. I’ve never seen a videogame where the developers didn’t want to put more features and content into the game than they could possibly have time for. Motivation and enthusiasm, in this industry, is just about a given. Where this hurts us is when:
> We do a bunch of things halfway and don’t have time to take them all to completion: we might have been able to finish one whole level in the time it took to do those two levels halfway.
> We save bug-fixing for later, and the cost of fixing those bugs goes up.
> We cut corners and work inefficiently.
> We do the wrong things: our pet features, or the publisher’s pet features, instead of what’s important for the game.
> We need to rein ourselves in. We could tell everyone on the team that they suck and their ideas are valueless, but that may be going too far in the other direction.

kg-card-end: html

Most software developers are highly motivated by nature; the real art of managing programmers lies in **knowing when to **[**demotivate**](http://www.demotivation.com/)** them**.


![](https://blog.codinghorror.com/content/images/2025/07/image-3.png)


Two of Steve McConnell’s [classic software development mistakes](https://www.amazon.com/exec/obidos/ASIN/1556159005/) are related to optimism. First, the distinction between optimism and **wishful thinking**:


> I am amazed at how many problems in software development boil down to wishful thinking. How many times have you heard statements like these:
> *“None of the team members really believed that they could complete the project according to the schedule they were given, but they thought that maybe if everyone worked hard, and nothing went wrong, and they got a few lucky breaks, they just might be able to pull it off.”
> “Our team hasn’t done very much work to coordinate the interfaces among the different parts of the product, but we’ve all been in good communication about other things, and the interfaces are relatively simple, so it’ll probably take only a day or two to shake out the bugs.”
> “We know that we went with the low-ball contractor on the database subsystem and it was hard to see how they were going to complete the work with the staffing levels they specified in their proposal. They didn’t have as much experience as some of the other contractors, but maybe they can make up in energy what they lack in experience. They’ll probably deliver on time.”
> “We don’t need to show the final round of changes to the prototype to the customer. I’m sure we know what they want by now.”
> “The team is saying that it will take an extraordinary effort to meet the deadline, and they missed their first milestone by a few days, but I think they can bring this one in on time.”
> Wishful thinking isn’t just optimism. It’s closing your eyes and hoping something works when you have no reasonable basis for thinking it will. Wishful thinking at the beginning of a project leads to big blowups at the end of a project. **Wishful thinking undermines meaningful planning and may be at the root of more software problems than all other causes combined.***


Optimism is fine if it’s based on actual data; this is where [prototyping and tracer code](https://blog.codinghorror.com/the-prototype-pitfall/) comes in handy.


![](https://blog.codinghorror.com/content/images/2025/07/image-4.png)


The second optimism-related [classic development mistake](https://web.archive.org/web/20051025035617/http://www.stevemcconnell.com/rdenum.htm) is **heroics**. Nobody wants to be the “guy who said [it couldn’t be done](https://blog.codinghorror.com/just-say-no/)”, but I’ve personally seen the project destruction wrought by developer heroics – and frankly, I’d rather work with the cynics:


> Some software developers place a high emphasis on project heroics, thinking that the certain kinds of heroics can be beneficial. But I think that emphasizing heroics in any form usually does more harm than good. In the case study, mid-level **management placed a higher premium on can-do attitudes than on steady and consistent progress and meaningful progress reporting**. The result was a pattern of scheduling brinkmanship in which impending schedule slips weren*’*t detected, acknowledged, or reported up the management chain until the last minute. A small development team held an entire company hostage because they wouldn*’*t admit that they were having trouble meeting their schedule. An emphasis on heroics encourages extreme risk taking and discourages cooperation among the many stakeholders in the software-development process.
> Some managers encourage this behavior when they focus too strongly on can-do attitudes. By elevating can-do attitudes above accurate-and-sometimes-gloomy status reporting, such project managers undercut their ability to take corrective action. They don*’*t even know they need to take corrective action until the damage has been done. As Tom DeMarco says, **can-do attitudes escalate minor setback into true disasters.**


The opposite of can-do attitudes isn’t can’t-do but simple pragmatism. I’m a firm believer in the **it’s always better to under-promise and over-deliver** policy. Rather than saying “It can’t be done!”, promise only what is essential – but continue to develop alternatives and contingency plans as time permits. Being realistic doesn’t mean giving up; it takes a lot more bravery to acknowledge the unknown than it does to blindly promise the world.

[programming](https://blog.codinghorror.com/tag/programming/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
[game development](https://blog.codinghorror.com/tag/game-development/)
[extreme programming](https://blog.codinghorror.com/tag/extreme-programming/)
