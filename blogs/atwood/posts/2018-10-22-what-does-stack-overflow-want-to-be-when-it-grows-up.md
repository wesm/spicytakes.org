---
title: "What does Stack Overflow want to be when it grows up?"
date: 2018-10-22
url: https://blog.codinghorror.com/what-does-stack-overflow-want-to-be-when-it-grows-up/
slug: what-does-stack-overflow-want-to-be-when-it-grows-up
word_count: 3481
---

I sometimes get asked by regular people in the actual real world what it is that I do for a living, and here’s my 15 second answer:


> We built a sort of Wikipedia website for computer programmers to post questions and answers. It’s called [Stack Overflow](https://stackoverflow.com/).


As of last month, it’s been 10 years since Joel Spolsky and I [started Stack Overflow](https://blog.codinghorror.com/stack-overflow-none-of-us-is-as-dumb-as-all-of-us/). I currently [do other stuff now](https://blog.codinghorror.com/civilized-discourse-construction-kit/), and I have since 2012, but if I will be known for anything when I’m dead, clearly it is going to be good old Stack Overflow.


Here’s where I’d normally segue into a bunch of rah-rah stuff about how great Stack Overflow is, and thus how implicitly great I am by association for being a founder, and all.


![](https://blog.codinghorror.com/content/images/2025/02/image-26.png)


I do not care about any of that.


What I do care about, though, is *whether Stack Overflow is useful to working programmers*. Let’s check in with [one of my idols](https://blog.codinghorror.com/you-dont-need-millions-of-dollars/), John Carmack. How useful is Stack Overflow, from the perspective of what I consider to be one of the greatest living programmers?


![@chx @jzy @StackExchange @codinghorror SO has probably added billions of dollars of value to the world in increased programmer productivity.](https://blog.codinghorror.com/content/images/2025/09/image-3.png)


I won’t lie, September 17th, 2013 was a [pretty good day](https://www.youtube.com/watch?v=O_05qJTeNNI). I literally got chills when I read that, and not just because I always read the word “billions” in Carl Sagan’s voice. It was also pleasantly the opposite of pretty much every *other* day I’m on Twitter, scrolling through an oppressive, endless litany of shared human suffering and people screaming at each other. Which reminds me, I should check my Twitter and see who else is wrong on the Internet today.


I am honored and humbled by the public utility that Stack Overflow has unlocked for a whole generation of programmers. But *I didn’t do that*.

- *You* did, when you contributed a well researched question to Stack Overflow.
- *You* did, when you contributed a succinct and clear answer to Stack Overflow.
- *You* did, when you edited a question or answer on Stack Overflow to make it better.


All those “fun size” units of Q&A collectively contributed by working programmers from all around the world ended up building a [Creative Commons resource](https://wiki.creativecommons.org/wiki/Case_Studies/StackOverflow.com) that truly rivals Wikipedia within our field. That’s... incredible, actually.


![stack-overflow-homepage-oct-2018](https://blog.codinghorror.com/content/images/2018/10/stack-overflow-homepage-oct-2018.png)


But success stories are boring. The world is filled with people that [basically got lucky](https://blogs.scientificamerican.com/beautiful-minds/the-role-of-luck-in-life-success-is-far-greater-than-we-realized/), and subsequently can’t stop telling people how it was all of their hard work and moxie that made it happen. I find failure much more instructive, and when building a business and planning for the future, I take on the role of Abyss Domain Expert™ and begin a staring contest. It’s just a little something I like to do, you know... *for me*.


![](https://blog.codinghorror.com/content/images/2025/02/image-27.png)


Thus, what I’d like to do right now is peer into that glorious abyss for a bit and introspect about **the challenges I see facing Stack Overflow for the next 10 years.** Before I begin, I do want to be absolutely crystal clear about a few things:

1. I [have not worked at Stack Overflow](https://blog.codinghorror.com/farewell-stack-exchange/) in any capacity whatsoever since February 2012 and I’ve had zero day-to-day operational input since that date, more or less by choice. Do I have opinions about how things should be done? Uh, have you *met me?* Do I email people every now and then about said opinions? I might, but I honestly do try to keep it to an absolute minimum, and I think my email archive track record here is reasonable.
2. The people working at Stack are amazing and most of them (including much of the Stack Overflow community, while I’m at it) could articulate the mission better — and perhaps a tad less crankily — than I could by the time I left. Would I trust them with my life? No. But I’d trust them with Joel’s life!
3. The whole point of the Stack Overflow exercise is that it’s not beholden to me, or Joel, or [any other Great Person](https://en.wikipedia.org/wiki/Great_man_theory). Stack Overflow works because it empowers regular everyday programmers all over the world, just like you, just like me. I guess in my mind it’s akin to being a parent. The goal is for your children to eventually grow up to be sane, practicing adults who don’t need (or, really, *want*) you to hang around any more.
4. Understand that you’re reading the weak opinions strongly held the [strong opinions weakly held](https://blog.codinghorror.com/strong-opinions-weakly-held/) of a co-founder who spent prodigious amounts of time working with the community in the first four years of Stack Overflow’s life to shape the rules and norms of the site to fit their needs. These are merely my opinions. I like to think they are *informed* opinions, but that doesn’t necessarily mean I can predict the future, or that I am even qualified to try. But I’ve never let being “qualified” stop me from doing anything, and I ain’t about to start tonight.


### Stack Overflow is a wiki first


Stack Overflow ultimately has *much* more in common with Wikipedia than a discussion forum. By this I mean questions and answers on Stack Overflow are not primarily judged by their usefulness to a specific individual, but by **how many *other* programmers that question or answer can potentially help over time**. I tried as hard as I could to emphasize this relationship from launch day in 2008. Note who has top billing in this Venn diagram.


![stack-overflow-venn-diagram](https://blog.codinghorror.com/content/images/2018/10/stack-overflow-venn-diagram.png)


Stack Overflow later added a super neat feature to highlight this core value in user profiles, where it shows how many other people you have potentially helped with your contributed questions and answers so far.


![stackoverflow-people-reached-profile-stat-1](https://blog.codinghorror.com/content/images/2018/10/stackoverflow-people-reached-profile-stat-1.png)


The most common complaints I see about Stack Overflow are usually the result of this fundamental misunderstanding about who the questions and answers on the site are ultimately *for*, and why there’s so much strictness involved in the whole process.


![I wish more people understood that the goal of Stack Overflow is not "answer my question" but "let's collaboratively build an artifact that will benefit future coders". Perhaps SO could be doing more to educate people about this.](https://blog.codinghorror.com/content/images/2025/09/image-4.png)


I’m continually amazed at the number of people, even on Hacker News today, who don’t realize that every single question and answer is editable on Stack Overflow, even as a completely anonymous user who isn’t logged in. Which makes sense, right, *because Stack Overflow is a wiki*, and that’s how wikis work. Anyone can edit them. Go ahead, try it right now if you don’t believe me – press the “improve this answer” or “improve this question” button on anything that can be improved, and make it so.


![stack-overflow-edit-question](https://blog.codinghorror.com/content/images/2018/10/stack-overflow-edit-question.png)


The responsibility for this misunderstanding is all on Stack Overflow (and by that I also mean myself, at least up until 2012). I guess the logic is that “every programmer has surely seen, used, and understands Stack Overflow by now, 10 years in” but... I think that’s a risky assumption. New programmers are minted every second of every day. Complicating matters further, there are three tiers of usage at Stack Overflow, from biggest to smallest, in inverted pyramid style:

1. **I passively search for programming answers. **Passively searching and reading highly ranked Stack Overflow answers as they appear in web search results is arguably the *primary goal of Stack Overflow*. If Stack Overflow is working like it’s supposed to, 98% of programmers should get all the answers they need from reading search result pages and wouldn’t need to ask or answer a single question in their entire careers. This is a good thing! Great, even!
2. **I participate on Stack Overflow when I get stuck on a really hairy problem and searching isn’t helping. **Participating only at those times when you are extra stuck is completely valid. However, I feel this level is where most people tend to run into difficulty on Stack Overflow, because it involves someone who may not be new to Stack Overflow per se, but is new to asking questions, and also at the precise time of stress and tension for them where they *must* get an answer due to a problem they’re facing… and they don’t have the time or inclination to deal with Stack Overflow’s strict wiki type requirements for research effort, formatting, showing previous work, and referencing what they found in prior searches.
3. **I participate on Stack Overflow for professional development. **At this level you’re talking about experienced Stack Overflow users who have contributed many answers and thus have a pretty good idea of what makes a great question, the kind they’d want to answer themselves. As a result, they don’t tend to ask many questions because they self-medicate through exhaustive searching and research, but when they do ask one, their questions are exemplary.


(There’s technically a fourth tier here, for people who want to selflessly contribute creative commons questions and answers to move the entire field of software development forward for the next generation of software developers. But who has time for saints 😇, y’all make the rest of us look bad, so knock it off already, Skeet.)


It wouldn’t shock me at all if people spent *years* happily at tier 1 and then got a big unpleasant surprise when reaching tier 2. The primary place to deal with this, in my opinion, is a **massively revamped and improved ask page**. It’s also fair to note that maybe people don’t understand that they’re signing up for a sizable chunk of work by implicitly committing to the wiki standard of “try to make sure it’s useful to more people than just yourself” when asking a question on Stack Overflow, and are then put off by the negative reaction to what others view as an insufficiently researched question.


Stack Overflow absorbs so much tension from its adoption of wiki standards for content. Even if you know about that requirement up front, it is not always clear what “useful” means, in the same way it’s not always clear what topics, people, and places are deserving of a Wikipedia page. [Henrietta Lacks](https://en.wikipedia.org/wiki/Henrietta_Lacks), absolutely, but what about your cousin Dave in Omaha with his weirdo PHP 5.6 issue?


### Over time, duplicates become vast landmine fields


Here’s one thing I really, really saw coming and to be honest with you I was kinda glad I left in 2012 before I had to deal with it because of the incredible technical difficulty involved: [**duplicates**](https://stackoverflow.blog/2009/04/29/handling-duplicate-questions/). Of all the complaints I hear about Stack Overflow, this is the one I am most sympathetic to by far.


If you accept that Stack Overflow is a wiki type system, then for the same reasons that you obviously can’t have five different articles about Italy on Wikipedia, **Stack Overflow can’t allow duplicate questions on the exact same programming problem**. While there is a fair amount of code to do pre-emptive searches as people type in questions, plus *many* exhortations to search before you ask, with an inviting search field and button right there on the mandatory page you see before asking your first question...


![](https://blog.codinghorror.com/content/images/2025/02/image-29.png)


...locating and identifying duplicate content is an insanely difficult problem even for a company like Google that’s done nothing but specialize in this exact problem for, what, 20 years now, with a veritable army of the world’s most talented engineers.


When you’re asking a question on a site that doesn’t allow duplicate questions, the problem space of a site with 1 million existing questions is rather different from a site with 10 million existing questions... or 100 million. Asking a single unique question goes from mildly difficult to mission almost impossible, because your question needs to thread a narrow path through this vast, enormous field of prior art questions without stepping on any of the vaguely similar looking landmines in the process.


![stackoverflow-asking-duplicate-question](https://blog.codinghorror.com/content/images/2018/10/stackoverflow-asking-duplicate-question.png)


But wait! *It gets harder!*

- Some [variance in similar-ish questions](https://stackoverflow.blog/2010/11/16/dr-strangedupe-or-how-i-learned-to-stop-worrying-and-love-duplication/) is OK, because 10 different people will ask a nearly identical question using 10 different sets of completely unrelated words with no overlap. I know, it sounds crazy, but trust me: humans are amazing at this. We want all those duplicates to exist so they can *point to* the primary question they are a duplicate of, while still being valid search targets for people who ask questions with unusual or rare word choices.
- It can be legitimately difficult to determine if your question is a true duplicate. How much overlap is enough before one programming question is a duplicate of another? And by whose definition? Opinions vary. This is subject to human interpretation, and humans are.. unreliable. Nobody will ever be completely happy with this system, pretty much by design. That tension is baked in permanently and forever.


I don’t have any real answers on the duplicate problem, which only gets worse over time. But I will point out that there is plenty of precedent on [the Stack Exchange network](https://stackexchange.com/sites#traffic) for splitting sites into “expert” and “beginner” areas with slightly different rulesets. We’ve seen this for Math vs. MathOverflow, English vs. English Learners, Unix vs. Ubuntu... **perhaps it’s time for a more beginner focused Stack Overflow** where duplicates are less frowned upon, and conversational rules are a bit more lenient?


### Stack Overflow is a competitive system of peer review


Stack Overflow was indeed built to be a fairly explicitly competitive system, with the caveat that “there’s [always more than one way](http://wiki.c2.com/?ThereIsMoreThanOneWayToDoIt) to do it.” This design choice was based on my perennial observation that the best way to motivate any programmer... is to subtly insinuate that *another* programmer could have maybe done it better.


![](https://blog.codinghorror.com/content/images/2025/02/image-30.png)


This is manifested in the [public reputation](https://blog.codinghorror.com/for-a-bit-of-colored-ribbon/) system on Stack Overflow, the incredible power of a number printed next to someone’s name, writ large. All reputation in Stack Overflow comes from the recognition of your peers, never the “system.”


![stack-overflow-top-rep-by-year](https://blog.codinghorror.com/content/images/2018/10/stack-overflow-top-rep-by-year.png)


Once your question is asked, or your answer is posted, it can then be poked, prodded, edited, flagged, closed, opened, upvoted, downvoted, [folded and spindled](http://www.cs.mun.ca/~harold/Courses/Old/CS1400.W15/Diary/Lubar1992.pdf) by your peers. The *intent* is for Stack Overflow to be a system of peer review and friendly competition, like a code review from a coworker you’ve never met at a different division of the company. It’s also completely fair for a fellow programmer to question the premise of your question, as long as it’s done in a nice way. For example, do you really want to use that [regular expression to match HTML](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags)?


I fully acknowledge that **competitive peer review systems aren’t for everyone**, and thus the overall process of having peers review your question may not always feel great, depending on your circumstances and background in the field – *particularly* when combined with the substantial tensions around utility and duplicates Stack Overflow already absorbed from its wiki elements. Kind of a double whammy there.


I’ve heard people describe the process of asking a question on Stack Overflow as anxiety inducing. To me, posting on Stack Overflow is *supposed* to involve a healthy kind of minor “let me be sure to show off my best work” anxiety:

- the anxiety of giving a presentation to your fellow peers
- the anxiety of doing well on a test
- the anxiety of showing up to a new job with talented coworkers you admire
- the anxiety of attending your first day at school with other students at your level


I imagine systems where there is zero anxiety involved and I can only think of jobs where I had long since stopped caring about the work and thus had no anxiety about whether I even showed for work on any given day. How can that be good? Let’s just say I’m not a fan of zero-anxiety systems.


Maybe competition just isn’t your jam. Could there be a less competitive Q&A system, a system without downvotes, a system without close votes, where there was never any anxiety about posting anything, just a network of super supportive folks who believe in you and want you to succeed no matter what? Absolutely! I think many alternative sites *should* exist on the internet so people can choose an experience that matches their personal preferences and goals. Should Stack build that alternative? Has it already been built? It’s an open question; feel free to point out examples in the comments.


### Stack Overflow is designed for practicing programmers


Another point of confusion that comes up a fair bit is who the intended audience for Stack Overflow actually is. That one is straightforward, and it’s been the same from day one:


![stackoverflow-for-business-description](https://blog.codinghorror.com/content/images/2018/10/stackoverflow-for-business-description.png)


Q&A for **professional and enthusiast programmers**. By that we mean:


> People who either already have a job as a programmer, or could potentially be hired as a programmer today if they wanted to be.


Yes, in case you’re wondering, part of this was an overt business decision. To make money you must have an audience of people already on a programmer’s salary, or in the job hunt to be a programmer. The entire Stack Overflow network may be Creative Commons licensed, but it was never a non-profit play. It was planned as a sustainable business from the outset, and that’s why we [launched Stack Overflow Careers](https://blog.codinghorror.com/stack-overflow-careers-amplifying-your-awesome/) only one year after Stack Overflow itself... to be honest far sooner than we should have, in retrospect. Careers has since been smartly subsumed into Stack Overflow proper at [stackoverflow.com/jobs](https://stackoverflow.com/jobs) for a more integrated and most assuredly way-better-than-2009 experience.


The choice of audience wasn’t meant to be an exclusionary decision in any way, but Stack Overflow was definitely designed as a fairly strict system of peer review, which is great (IMNSHO, obviously) for already practicing professionals, but **pretty much everything you would *not* want as a student or beginner**. This is why I cringe so hard I practically turn myself inside out when people on Twitter mention that they have pointed their students at Stack Overflow. What you’d want for a beginner or a student in the field of programming is almost *the exact opposite* of what Stack Overflow does at every turn:

- one-on-one mentoring
- real time collaborative screen sharing
- live chat
- theory and background courses
- starter tasks and exercises
- playgrounds to experiment in


These are all very fine and good things, but Stack Overflow does *NONE* of them, by design.


*Can* you use Stack Overflow to learn how to program from first principles? Well, technically you can do anything with any software. You could try to have actual conversations on Reddit, if you’re a masochist. But the answer is yes. You could learn how to program on Stack Overflow, in theory, if you are a prodigy who is comfortable with the light competitive aspects (reputation, closing, downvoting) and also perfectly willing to define all your contributions to the site in terms of utility to others, not just yourself as a student attempting to learn things. But I *suuuuuuper* would not recommend it. There are far better websites and systems out there for [learning to be a programmer](https://blog.codinghorror.com/heres-the-programming-game-you-never-asked-for/). *Could* Stack Overflow build beginner and student friendly systems like this? I don’t know, and it’s certainly not my call to make. 🤔


And that’s it. We can now resume our normal non-abyss gazing. Or whatever it is that passes for normal in these times.


I hope all of this doesn’t come across as negative. Overall I’d say the state of the Stack is strong. But does it even matter what I think? [As it was in 2008](https://stackoverflow.blog/2008/11/25/stack-overflow-is-you/), so it is in 2018.


> **Stack Overflow is *you*.**
> This is the scary part, the great leap of faith that Stack Overflow is predicated on: trusting your fellow programmers. The programmers who choose to participate in Stack Overflow are the “secret sauce” that makes it work. You are the reason I continue to believe in developer community as the greatest source of learning and growth. You are the reason I continue to get so many positive emails and testimonials about Stack Overflow. I can’t take credit for that. But you can.
> I learned the collective power of my fellow programmers long ago writing on Coding Horror. The community is far, far smarter than I will ever be. All I can ask — all any of us can ask — is to help each other along the path.
> And if your fellow programmers decide to recognize you for that, then I say you’ve well and truly earned it.


The strength of Stack Overflow begins, and ends, with the community of [programmers that power the site](https://meta.stackoverflow.com/). What should Stack Overflow be when it grows up? **Whatever we make it, together.**


![stackoverflow-none-of-us-is-as-dumb-as-all-of-us](https://blog.codinghorror.com/content/images/2018/10/stackoverflow-none-of-us-is-as-dumb-as-all-of-us.jpg)


p.s. Happy 10th anniversary Stack Overflow!


---


Also see Joel’s take on 10 years of Stack Overflow with [The Stack Overflow Age](https://www.joelonsoftware.com/2018/04/06/the-stack-overflow-age/), [A Dusting of Gamification](https://www.joelonsoftware.com/2018/04/13/gamification/), and [Strange and Maddening Rules](https://www.joelonsoftware.com/2018/04/23/strange-and-maddening-rules/).

[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[stack overflow](https://blog.codinghorror.com/tag/stack-overflow/)
[community collaboration](https://blog.codinghorror.com/tag/community-collaboration/)
