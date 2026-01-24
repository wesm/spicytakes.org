---
title: "Here’s The Programming Game You Never Asked For"
date: 2016-04-15
url: https://blog.codinghorror.com/heres-the-programming-game-you-never-asked-for/
slug: heres-the-programming-game-you-never-asked-for
word_count: 1454
---

You know what’s universally regarded as un-fun by most programmers? Writing [assembly language code](https://en.wikipedia.org/wiki/Assembly_language).


![](https://blog.codinghorror.com/content/images/2016/04/assembly-language.png)


As Steve McConnell [said back in 1994](http://www.amazon.com/dp/0735619670/):


> Programmers working with high-level languages achieve better productivity and quality than those working with lower-level languages. Languages such as C++, Java, Smalltalk, and Visual Basic have been credited with improving productivity, reliability, simplicity, and comprehensibility by factors of 5 to 15 over low-level languages such as assembly and C. **You save time when you don’t need to have an awards ceremony every time a C statement does what it’s supposed to.**


Assembly is a language where, for performance reasons, every individual command is communicated in excruciating low level detail directly to the CPU. As we’ve gone from fast CPUs, to faster CPUs, to multiple absurdly fast CPU cores on the same die, to “gee, we kinda stopped caring about CPU performance altogether five years ago,” there hasn’t been much need for the kind of hand-tuned performance you get from assembly. Sure, there are [the occasional heroics](https://blog.codinghorror.com/i-happen-to-like-heroic-coding/), and they are amazing, but in terms of Getting Stuff Done, assembly has been well off the radar of mainstream programming for probably twenty years now, and for good reason.


So who in their right mind would take up tedious assembly programming today? Yeah, nobody. But wait! What if I told you your Uncle Randy had just died and left behind this mysterious old computer, [the TIS-100](http://www.zachtronics.com/tis-100/)?


![](https://blog.codinghorror.com/content/images/2016/04/aunt-doris-note-tis-100.jpg)


And what if I also told you the only way to figure out what that TIS-100 computer was used for – and what good old Uncle Randy was up to – was to read a (blessedly short 14 page) photocopied reference manual and fix its corrupted boot sequence… *using assembly language?*


![](https://blog.codinghorror.com/content/images/2025/02/image-77.png)


Well now, by God, it’s time to learn us some assembly and get to the bottom of this mystery, isn’t it? As [its creator](http://www.zachtronics.com/) notes, **this is the assembly language programming game you never asked for!**


I was surprised to discover my co-founder [Robin Ward](https://eviltrout.com/) liked TIS-100 so much that he not only played the game (presumably to completion) but wrote a [TIS-100 emulator in C](https://github.com/eviltrout/tis-100). This is apparently the kind of thing he does for fun, in his free time, when he’s not already working full time with us programming [Discourse](http://www.discourse.org/). Programmers gotta… program.


Of course there’s a long history of programming games. What makes TIS-100 unique is the way it fetishizes assembly programming, while most programming games take it a bit easier on you by easing you in with general concepts and simpler abstractions. But even “simple” programming games can be quite difficult. Consider one of my favorites on the Apple II, [Rocky’s Boots](https://en.wikipedia.org/wiki/Rocky%27s_Boots), and its sequel, Robot Odyssey. [I loved this game](https://blog.codinghorror.com/programming-4-fun/), but in true programming fashion it was so difficult that finishing it in any meaningful sense was [basically impossible](http://www.slate.com/articles/technology/bitwise/2014/01/robot_odyssey_the_hardest_computer_game_of_all_time.html):


> Let me say: Any kid who completes this game while still a kid (I know only one, who also is one of the smartest programmers I’ve ever met) is guaranteed a career as a software engineer. Hell, any adult who can complete this game should go into engineering. **Robot Odyssey is the hardest damn “educational” game ever made.** It is also a stunning technical achievement, and one of the most innovative games of the Apple IIe era.
> Visionary, absurdly difficult games such as this gain cult followings. It is the game I remember most from my childhood. It is the game I love (and despise) the most, because it was the hardest, the most complex, the most challenging. The world it presented was like being exposed to Plato’s forms, a secret, nonphysical realm of pure ideas and logic. The challenge of the game—and it was one serious challenge—was to understand that other world. Programmer Thomas Foote had just started college when he picked up the game: “I swore to myself,” he told me, “that as God is my witness, I would finish this game before I finished college. I managed to do it, but just barely.”


![](https://blog.codinghorror.com/content/images/2025/02/image-79.png)


I was happy dinking around with a few robots that did a few things, got stuck, and moved on to other games. I got a little turned off by the way it treated programming as electrical engineering; messing around with a ton of AND OR and NOT gates was just not my jam. I was already [cutting my teeth on BASIC](https://blog.codinghorror.com/everything-i-needed-to-know-about-programming-i-learned-from-basic/) by that point and I sensed a level of mastery was necessary here that I probably didn’t have and I wasn’t sure I even *wanted*.


![](https://blog.codinghorror.com/content/images/2016/04/robot-odyssey-chip.png)


I’ll take a COBOL code listing over *that* monstrosity any day of the week. Perhaps Robot Odyssey was so hard because, in the end, it was a bare metal CPU programming simulation, like TIS-100.


A more gentle example of a modern programming game is Tomorrow Corporation’s excellent [Human Resource Machine](http://tomorrowcorporation.com/humanresourcemachine).


It has exactly the irreverent sense of humor you’d expect from the studio that built World of Goo and Little Inferno, both excellent and highly recommendable games in their own right. If you’ve ever wanted to find out if someone is truly interested in programming, recommend this game to them and see. It starts with only 2 instructions and slowly widens to include 11. Corporate drudgery has never been so… er, fun?


I’m thinking about this because I believe there’s a strong connection between programming games and being a talented software engineer. It’s that essential sense of *play*, the idea that you’re experimenting with this stuff because you enjoy it, and you bend it to your will out of the sheer joy of creation more than anything else. As [I once said](https://blog.codinghorror.com/programming-love-it-or-leave-it/):


> Joel implied that good programmers love programming so much they’d do it for *no pay at all*. I won’t go quite that far, but I will note that the best programmers I’ve known have all had a **lifelong passion for what they do**. There’s no way a minor economic blip would ever convince them they should do anything else. No way. No how.


I’d rather sit a potential hire in front of Human Resource Machine and time how long it takes them to work through a few levels than [have them solve FizzBuzz](https://blog.codinghorror.com/why-cant-programmers-program/) for me on a whiteboard. Is this interview about demonstrating competency in a certain technical skill that’s worth a certain amount of money, or showing me how you can *improvise and have fun?*


That’s why I was so excited when Patrick, Thomas, and Erin founded Starfighter.


![](https://blog.codinghorror.com/content/images/2025/02/image-80.png)


If you want to know how competent a programmer is, give them a real-ish simulation of a real-ish system to hack against and experiment with – and see how far they get. In security parlance, this is [known as a CTF](https://www.defcon.org/html/links/dc-ctf.html), as popularized by Defcon. But it’s rarely extended to programming, until now. Their first simulation is [StockFighter](https://www.stockfighter.io/).


Participants are given:

- An interactive trading blotter interface
- A real, functioning set of limit-order-book venues
- A carefully documented JSON HTTP API, with an API explorer
- A series of programming missions.


Participants are asked to:

- Implement programmatic trading against a real exchange in a thickly traded market.
- Execute block-shopping trading strategies.
- Implement electronic market makers.
- Pull off an elaborate HFT trading heist.


This is a *seriously* next level hiring strategy, far beyond anything else I’ve seen out there. It’s so next level that to be honest, I got really jealous reading about it, because **I’ve felt for a long time that Stack Overflow should be doing yearly programming game events exactly like this**, with special one-time badges obtainable only by completing certain levels on that particular year. Stack Overflow is [already a sort of game](https://blog.codinghorror.com/for-a-bit-of-colored-ribbon/), but people would go *nuts* for a yearly programming game event. Absolutely *bonkers*.


I know we’ve talked about giving lip service to the [idea of hiring the best](https://blog.codinghorror.com/we-hire-the-best-just-like-everyone-else/), but if that’s *really* what you want to do, the best programmers I’ve ever known have excelled at exactly the situation that Starfighter simulates — live troubleshooting and reverse engineering of an existing system, even to the point of [finding rare exploits](https://blog.codinghorror.com/why-isnt-my-encryption-encrypting/).


![](https://blog.codinghorror.com/content/images/2016/04/stockfighter-hardware.jpg)


Consider the dedication of this participant who built a complete wireless trading device for StockFighter. Was it necessary? Was it practical? No. **It’s the programming game we never asked for.** But here we are, regardless.


An arbitrary programming game, particularly one that goes to great lengths to simulate a fictional system, is a wonderful expression of the inherent joy in *playing* and *experimenting* with code. If I could find them, I’d gladly hire a dozen people just like that any day, and set them loose on our very real programming project.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[assembly language](https://blog.codinghorror.com/tag/assembly-language/)
[high-level languages](https://blog.codinghorror.com/tag/high-level-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[productivity](https://blog.codinghorror.com/tag/productivity/)
