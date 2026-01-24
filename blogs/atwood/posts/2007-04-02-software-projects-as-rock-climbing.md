---
title: "Software Projects as Rock Climbing"
date: 2007-04-02
url: https://blog.codinghorror.com/software-projects-as-rock-climbing/
slug: software-projects-as-rock-climbing
word_count: 1196
---

If you accept the premise that [software development is a cooperative game](https://blog.codinghorror.com/software-development-as-a-collaborative-game/), then you might wonder: **what kind of game is it?**


Alistair Cockburn believes the closest analog to a software project is the [cooperative game of rock climbing](https://web.archive.org/web/20070402084629/http://alistair.cockburn.us/index.php/Software_development_as_a_cooperative_game#---------------_4._Games):


![rock climbing](https://blog.codinghorror.com/content/images/uploads/2007/04/6a0120a85dcdae970b0128777009a2970c-pi.jpg)

- **Technical.** The novice can only approach simple climbs. With practice, the climber can attack more and more difficult climbs. The more technically proficient rock climber can do things that the others cannot. Similarly, software development is technical and requires technical proficiency, and there is a frank difference in what a more skilled person can do compared with a less skilled person.
- **Individual and Team.** Some people naturally climb better than others. Some people will never handle certain climbs. At each moment of the climb, each person is drawing on their own capabilities. They have to hold their own weight. And yet climbing is usually done in teams. There are solo climbers, but they are in the minority. Under normal circumstances, climbers form a team and the team has to work together to complete the climb. Similarly, software developers, while working on their individual assignments, must function as a team to get the software out.
- **Tools.** Tools are a requirement for serious rock-climbing: chalk, chucks, harness, rope, carabiner, and so on. It is important to be able to reach for the right tool for the right moment. It is possible to climb very small distances with no tools. The longer the climb, the more critical the tool selection is. Software developers will recognize this. When you need a performance profiler, you really need it. You can’t function without the compiler. The team gets stuck without the version control system. And so on.
- **Planning and Improvising.** Whether bouldering, doing a single-rope climb, or a multi-day climb, the climbers always make a plan. The longer the climb, the more extensive the plan must be, even though the team knows that the plan will be insufficient, and wrong in places. Unforeseen, unforeseeable and purely chance obstacles are certain to show up on even the most meticulously planned climbing expeditions, unless the climb is short and the climbers have completed it several times before. Therefore, the climbers must be prepared to change their plans, to improvise, at a moment’s notice. This dichotomy is part of what makes software development manages gnash their teeth. They want a plan, but have to deal with unforeseen difficulties. It is one of the reasons why incremental development is so critical to project success. It is why climbers climb in stages, and set various base camps.
- **Fun.** Climbers climb because it is fun. Climbers experience a sense of flow while climbing, and this total occupation is part of what makes it fun. Similarly, programmers typically enjoy their work, and part of that enjoyment is getting into the flow of designing or programming.
- **Challenging.** Climbers climb because there is a challenge. Can they really make it to the top? Most programmers crave this challenge, too. If programmers do not find their assignment challenging, they may quit, or start embellishing the system with design elements they find challenging.
- **Resource-limited.** Rock climbing works against a time and energy budget. The climb needs to be completed before the team is too tired, before the food runs out, by nightfall or before the snows come.
- **Dangerous.** If you fall wrong on a rock climb, you can be killed or maimed. This is probably the one aspect of rock climbing that does not transfer to software development. Rock climbers are fond of saying that climbing, done properly, is less dangerous than driving a car. However, I have never heard programmers compare the danger of programming with the danger of driving a car or even crossing the street.


I’ll admit I had never quite thought of software development in this way, but Alistair’s rock climbing metaphor holds. It’s certainly a far better metaphor than the [tired old bridge building chestnut](https://blog.codinghorror.com/bridges-software-engineering-and-god/). I see further analogs in the way the natural environment itself – and the difficult to predict, uncontrollable weather conditions – can make or break a project.


The one unsatisfying aspect of the rock climbing metaphor is that **software tends to build upon itself in a way that rock climbing doesn’t.** Each subsequent version of the software expands on the capabilities and the platform established in the previous version. So there are really *two* goals:

1. to reach the summit.
2. to make it easier for subsequent teams to reach the summit.


But these goals can be mutually exclusive. In a [followup article](https://web.archive.org/web/20070912091649/http://alistair.cockburn.us/index.php/The_end_of_software_engineering_and_the_start_of_economic-cooperative_gaming#Games.2C_Cooperative_Games.2C_Series.27_of_Games), Alistair illustrates with an example he calls “The Swamp Game.”


> Consider a race across an uncharted swampland in which some particular (unknown) artifact must be produced at some particular (unknown) place in the swamp. A team in this race would employ scouts and specialists of various sorts, and would create maps, route markings, bridges and so on. The racers would not, however, construct commercial quality maps, roads or bridges, since doing so would waste precious resources. Instead, they would estimate how much or little of a path must be cleared for themselves, how strong to build the bridge, how fancy of markings to make, how simple a map, in order to reach their goal in the shortest time.
> If the race is run as part of a series, there will be new teammates coming after them to pick up the artifact and move it to a new place. The first team will therefore be well served to make slightly better paths, maps and bridges, always keeping in mind that doing this work competes with completing the current stage of the race. They also will be well served if they leave some people who understand the territory to be part of the next team. **Thus, the optimal strategies for a series of races are different than for a single race.**
> There is no closed-form formula for winning the game. There are only strategies that are more useful in particular situations. That realization alone may be the strongest return for using the economic-cooperative game language: people on live projects see that they must constantly observe the characteristics of the changing situation, to collect known strategies, to invent new strategies on the fly; and that since a perfect outcome is not possible in an over constrained situation, they much choose which outcome to prioritize at the expense of which others.


I find Alistair’s game theories fascinating and illuminating. Based on the strength of these two essays, I just picked up a copy of Alistair’s book, [Crystal Clear: A Human-Powered Methodology for Small Teams](http://www.amazon.com/exec/obidos/ASIN/0201699478). It’s based on the same [cooperative game manifesto](https://web.archive.org/web/20071008180353/http://alistair.cockburn.us/index.php/Cooperative_game_manifesto_for_software_development) I’ve covered in my last two entries.


![Crystal Clear: A Human-Powered Methodology for Small Teams](https://blog.codinghorror.com/content/images/uploads/2007/04/6a0120a85dcdae970b0128777009a7970c-pi.jpg)


I’ve already run into one team using the Crystal method (no, not [that crystal method](http://en.wikipedia.org/wiki/The_Crystal_Method)) at a customer site. I’ll have to check in with them next week and see how close they are to the summit.


And the next time someone asks *you* why software projects are [so challenging](https://blog.codinghorror.com/the-long-dismal-history-of-software-project-failure/), **invite them to go rock climbing with you**.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
