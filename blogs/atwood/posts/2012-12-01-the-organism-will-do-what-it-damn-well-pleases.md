---
title: "The Organism Will Do Whatever It Damn Well Pleases"
date: 2012-12-01
url: https://blog.codinghorror.com/the-organism-will-do-what-it-damn-well-pleases/
slug: the-organism-will-do-what-it-damn-well-pleases
word_count: 1372
---

In the go-go world of software development, we’re so consumed with [learning new things](https://blog.codinghorror.com/learning-or-learning-how-to-learn/), so fascinated with the [procession of shiny new objects](https://blog.codinghorror.com/the-magpie-developer/) that I think we sometimes lose sight of our history. I don’t mean the big era-defining successes. Everyone knows those stories. I’m talking about the things we’ve tried before that… didn’t quite work out. The failures. The also-rans. The noble experiments. The crazy plans.


I’m all for [reinventing the wheel](https://blog.codinghorror.com/dont-reinvent-the-wheel-unless-you-plan-on-learning-more-about-wheels/), because it’s one of the best ways to learn. But you shouldn’t even *think* about reinventing a damn thing **until you’ve exhaustively researched every single last wheel, old or new, working or broken, that you can lay your hands on. **Do your homework.


That’s why I love unearthing stories like [The Lessons of Lucasfilm’s Habitat](http://www.fudco.com/chip/lessons.html). It’s basically World of Warcraft… in 1985.


![Habitat](https://blog.codinghorror.com/content/images/uploads/2012/12/6a0120a85dcdae970b017c3424c4d8970b-800wi.png)


> [Habitat](https://en.wikipedia.org/wiki/Habitat_(video_game)) is “a multi-participant online virtual environment,” a cyberspace.
> Each participant (“player”) uses a home computer (Commodore 64) as an intelligent, interactive client, communicating via modem and telephone over a commercial packet-switching network to a centralized, mainframe host system. The client software provides the user interface, generating a real-time animated display of what is going on and translating input from the player into messages to the host. The host maintains the system’s world model enforcing the rules and keeping each player’s client informed about the constantly changing state of the universe.


This was the dark ages of home computing. In 1985, that 64k of memory in a Commodore 64 was a *lot*. The entirety of Turbo Pascal 3.02 for DOS, released a year later in 1986, [was barely 40k](https://prog21.dadgum.com/116.html).


The very concept of a multiplayer virtual world of any kind – something we take for granted today, since every modern website is essentially a multiplayer game now – was incredibly exotic. Look at the painstaking [explanation Lucasfilm had to produce](https://www.youtube.com/watch?v=VVpulhO3jyc) to even get folks to understand what the heck Habitat was, and how it worked.


The technical information in The Lessons of Lucasfilm’s Habitat is incredibly dated, as you’d expect, and barely useful even as trivia. But the sociological lessons of Habitat cut to the bone. They’re as fresh today as they were in 1985. Computers have radically changed in the intervening 27 years, whereas people’s behavior hasn’t. At all. This particular passage hit home:


> Again and again we found that activities based on often unconscious assumptions about player behavior had completely unexpected outcomes (when they were not simply outright failures). It was clear that we were not in control. The more people we involved in something, the less in control we were. **We could influence things, we could set up interesting situations, we could provide opportunities for things to happen, but we could not predict nor dictate the outcome. **Social engineering is, at best, an inexact science, even in proto-cyberspaces. Or, as some wag once said, “in the most carefully constructed experiment under the most carefully controlled conditions, the organism will do whatever it damn well pleases.”


Even more specifically:


> Propelled by these experiences, we shifted into a style of operations in which we let the players themselves drive the direction of the design. This proved far more effective. **Instead of trying to push the community in the direction we thought it should go, an exercise rather like herding mice, we tried to observe what people were doing and aid them in it.** We became facilitators as much as designers and implementors. This often meant adding new features and new regions to the system at a frantic pace, but almost all of what we added was used and appreciated, since it was well matched to people’s needs and desires. As the experts on how the system worked, we could often suggest new activities for people to try or ways of doing things that people might not have thought of. In this way we were able to have considerable influence on the system’s development in spite of the fact that we didn’t really hold the steering wheel – more influence, in fact, than we had had when we were operating under the delusion that we controlled everything.


That’s exactly what I was trying to say in [Listen to Your Community, But Don’t Let Them Tell You What to Do](https://blog.codinghorror.com/listen-to-your-community-but-dont-let-them-tell-you-what-to-do/). Unfortunately, because I hadn’t read this essay until a few months ago, I figured this important lesson out *25 years later* than Randy Farmer and Chip Morningstar. So many Stack Overflow features were the direct result of observing what the community was doing, then attempting to aid them in it:

- We noticed early in the Stack Overflow beta that users desperately wanted to reply to each other, and were cluttering up the system with “answers” that were, well, not answers to the question. Rather than chastize them for doing it wrong – *stupid users!* – we added the commenting system to give them a method of annotating answers and questions for clarifications, updates, and improvements.
- I didn’t think it was necessary to have a place to discuss Stack Overflow. And I was… kind of a jerk about it. The community was on the verge of creating a phpBB forum instance to discuss Stack Overflow. Faced with a nuclear ultimatum, I relented, and you know what? [They were right](https://blog.codinghorror.com/meta-is-murder/). And I was wrong.
- The community came up with an interesting convention for [handling duplicate questions](http://blog.stackoverflow.com/2009/04/handling-duplicate-questions/), by manually editing a blockquote into the top of the question with a link to the authoritative question that it was a duplicate of. This little user editing convention eventually became the template for the official implementation.


I could go on and on, but I won’t bore you. I’d say for every 3 features we introduced on Stack Overflow, at least two of them came more or less directly from observing the community, then trying to run alongside them, building tools that **helped them do what they wanted to do with less fuss and effort**. That was my job for the last four years. And I loved it, until I had to [stop loving it](https://blog.codinghorror.com/farewell-stack-exchange/).


[Randy Farmer](https://en.wikipedia.org/wiki/Randy_Farmer), one of the primary designers of Habitat at Lucasfilm, went on to work on a bunch of things that you may recognize: with [Douglas Crockford](https://en.wikipedia.org/wiki/Douglas_Crockford#Career) on JSON, The Sims Online, Second Life, Yahoo 360°, Yahoo Answers, Answers.com, and so forth. He eventually condensed some of his experience into a book, [Building Web Reputation Systems](https://www.amazon.com/dp/059615979X/), which I bought in April 2011 as a Kindle edition. I didn’t know who Mr. Farmer was at this time. I just saw a new O’Reilly book on an area of interest, and I thought I’d check it out.


![](https://blog.codinghorror.com/content/images/2025/03/image-142.png)


As the co-founder of Stack Overflow, I know a thing or two about web reputation systems! Out of curiosity, I looked up the author on my own site. And [I found him](https://stackoverflow.com/users/523113/f-randall-farmer), with a *tiny* reputation. So I sent this friendly jibe on Twitter:


![pff, look at @frandallfarmer's tiny rep! LOOK AT IT! http://goo.gl/Gjvrn http://buildingreputation.com/ | @codinghorror lol! Reputation context is everything! Surprise! rpg.stackexchange.com/users/810/f-ra...](https://blog.codinghorror.com/content/images/2025/09/image-16.png)


But the last laugh was on Randy, as it should be, because I didn’t realize he had over [6,000 reputation](https://rpg.stackexchange.com/users/810/f-randall-farmer) on [rpg.stackexchange.com](https://rpg.stackexchange.com/). Turns out, Randy Farmer was already an avid Stack Exchange user. And, as you might guess given his background, a rather *expert* Stack Exchange user at that. The Stack Exchange ruleset is complex, strict, and requires discipline to understand. Kind of like... maybe a *certain role playing game*, if you will.


![](https://blog.codinghorror.com/content/images/2025/03/image-145.png)


Randy is the sort of dad who had his [first edition Dungeons & Dragons books](http://www.reddit.com/r/rpg/comments/xiwir/about_30_years_ago_my_dad_had_his_first_edition/) bound into a single leather tome and handed it down to his son as a family heirloom. How awesome is that?


If we’ve learned anything in the last 25 years since Habitat, it is that **people are the source of, and solution to, all the problems you’ll run into when building social software**. Are you looking to (dungeon) master the art of guiding and nudging your online community through their collective adventure, without violating the continuity of your own little universe? If so, you could do a whole heck of lot worse than reading [Building Web Reputation Systems](https://www.amazon.com/dp/059615979X/) and [following @frandallfarmer on Mastodon](https://fosstodon.org/@frandallfarmer).

[history](https://blog.codinghorror.com/tag/history/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[virtual environment](https://blog.codinghorror.com/tag/virtual-environment/)
