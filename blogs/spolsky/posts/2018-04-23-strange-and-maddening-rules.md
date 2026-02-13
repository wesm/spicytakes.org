---
title: "Strange and maddening rules"
date: 2018-04-23
url: https://www.joelonsoftware.com/2018/04/23/strange-and-maddening-rules/
word_count: 1425
---


There’s this popular idea among developers that when you face a problem with code, you should get out a rubber duck and explain, to the duck, exactly how your code was supposed to work, line by line, what you expected to see, what you saw instead, etc. Developers who try this report that the very act of explaining the problem in detail to an inanimate object often helps them find the solution.


This is one of many tricks to solving programming problems on your own. Another trick is [divide and conquer debugging](http://markheath.net/post/effective-debugging-with-divide-and-conquer). You can’t study a thousand lines of code to find the one bug. But you can divide them in half and quickly figure out if the problem happens in the first half or the second half. Keep doing this five or six times and you’ll pinpoint the single line of code with the problem.


It’s interesting, with this in mind, to read [Jon Skeet’s](https://stackoverflow.com/users/22656/jon-skeet?tab=profile) checklist for [writing the perfect question](https://codeblog.jonskeet.uk/2012/11/24/stack-overflow-question-checklist/). One of the questions Jon asks is “Have you read the whole question to yourself carefully, to make sure it makes sense and contains enough information for someone coming to it without any of the context that you already know?” That is essentially the Rubber Duck Test. Another question is “If your question includes code, have you written it as a short but complete program?” Emphasis on the *short*—that is essentially a test of whether or not you tried divide and conquer.


What Jon’s checklist can do, in the best of worlds, is to help people try the things that experienced programmers may have already tried, before they ask for help.


Sadly, not everybody finds his checklist. Maybe they found it and they don’t care. They’re having an urgent problem with code; they heard that Stack Overflow could help them; and they don’t have time to read some nerd’s complicated protocol for requesting help.


One of the frequent debates about Stack Overflow is whether the site needs to be open to questions from programming novices.


When Jeff and I were talking about the initial design of Stack Overflow, I told him about this popular Usenet group for the C programming language in the 1980s. It was called [comp.lang.c.](https://groups.google.com/forum/#!forum/comp.lang.c)


C is a simple and limited programming language. [You can get a C compiler that fits in 100K.](http://repo.or.cz/w/tinycc.git) So, when you make a discussion group about C, you quickly run out of things to talk about.


Also. In the 1990s, C was a common language for undergraduates who were learning programming. And, in fact, said undergraduates would have [very basic problems](https://groups.google.com/forum/#!searchin/comp.lang.c/spolsky%7Csort:date/comp.lang.c/BKhAacGNtZI/GLSW-QG_O3MJ) in C. And they might show up on comp.lang.c asking their questions.


And the old-timers on comp.lang.c were bored. *So* bored. Bored of the undergraduates showing up every September wondering why they can’t return a local char array from a function et cetera, et cetera, ad nauseum. Every damn September.


The old timers invented the concept of FAQs. They used them to say “please don’t ask things that have been asked before, ever, in the history of Usenet” which honestly meant that the only questions they really wanted to see were so bizarre and so esoteric that they were really enormously boring to 99% of working C programmers. The newsgroup languished because it catered only to the few people that had been there for a decade.


Jeff and I talked about this. What did we think of newbie questions?


We decided that newbies had to be welcome. Nothing was too “beginner” to be a reasonable question on Stack Overflow… as long as you did some homework before asking the question.


We understood that this might mean that some of the more advanced people might grow bored with duplicate, simple questions, and move on. We thought that was fine: Stack Overflow doesn’t have to be a lifetime commitment. You’re welcome to get bored and move on if you think that the newbies keep asking why they can’t return local char arrays (“but it works for me!”) and you would rather devote the remaining short years of your life to something more productive, like sorting your record albums.


The mere fact that you are a newbie doesn’t mean that your question doesn’t belong on Stack Overflow. To prove the point, I asked “[How do you move the turtle in Logo](https://stackoverflow.com/questions/1003841/how-do-i-move-the-turtle-in-logo),” hoping to leave behind evidence that the site designers wanted to allow absolute beginners.


Thanks to the law of unintended consequences, this caused a lot of brouhaha, but not because the question was too easy. The real problem there was that I was asking the question in bad faith. Jeff Atwood [explained](https://meta.stackexchange.com/questions/158289/why-is-the-how-to-move-the-turtle-in-logo-question-closed#comment457933_158334) it: “Simple is fine. No effort and research is not.” ([Also this](https://en.wikipedia.org/wiki/Wikipedia:Do_not_disrupt_Wikipedia_to_illustrate_a_point).)


To novices, the long bureaucratic rigmarole associated with asking your first question on Stack Overflow can feel either completely unnecessary, or just plain weird. It’s like Burning Man. You just want to go to a nice glittery dance party in the desert, but the Burning People are yammering on about their goddamn [10 principles](https://burningman.org/culture/philosophical-center/10-principles/), and “radical self-expression” and so on and so forth, and *therefore* after washing your dishes you must carefully save the dirty dishwater like a cherished relic and remove every drop of it from the Playa, bringing it home with you, in your check-in luggage if necessary. Every community has lots of rules and when you join the community they either seem strange and delightful or, if you’re just desperately trying to get some code to work, they are strange and maddening.


A lot of the rules that are important to make Burning Man successful are seemingly arbitrary, but they’re still necessary. The US Bureau of Land Management which makes the desert available for Burning Man requires that no contaminated water be poured out on the ground because the clay dirt doesn’t really absorb it so well and it can introduce all kinds of disease and whatnot, but who cares because Burning Man simply will not be allowed to continue if the participants don’t pack out their used water.


Similarly for Stack Overflow. We don’t allow, say, questions that are too broad (“How do I make a program?”). Our general rule is that if the correct length of an answer is *a whole book *you are asking too much. These questions feel like showing up on a medical website and saying something like “I think my kidney has been hurting. How can I remove it?” It’s crazy—and incidentally, insulting to the people who spent ten years in training learning to be surgeons.


One thing I’m very concerned about, as we try to educate the next generation of developers, and, importantly, get more diversity and inclusiveness in that new generation, is what obstacles we’re putting up for people as they try to learn programming. In many ways Stack Overflow’s specific rules for what is permitted and what is not are obstacles, but an even bigger problem is rudeness, snark, or condescension that newcomers often see.


I care a lot about this. Being a developer gives you an unparalleled opportunity to [write the script for the future](https://www.joelonsoftware.com/2016/12/09/developers-are-writing-the-script-for-the-future/). All the flak that Stack Overflow throws in the face of newbies trying to become developers is actively harmful to people, to society, and to Stack Overflow itself, by driving away potential future contributors. And programming is hard enough; we should see our mission as making it easier.


We’re planning a lot of work in this area for the next year. We can’t change everybody and we can’t force people to be nice. But I think we can improve some aspects of the Stack Overflow user interface to encourage better behavior, for example, we could improve the prompts we provide on the “Ask Question” page, and we could provide more tools for community moderation of comments where the snark currently runs unchecked.


We’re also working on new features that will let you direct your questions to a private, smaller group of people on your own team, which may bring some of the friendly neighborhood feel to the big city of Stack Overflow.


Even as we try to make Stack Overflow more friendly, our primary consideration at Stack Overflow has been to build the world’s greatest resource for software developers. The average programmer, in the world, has been helped by Stack Overflow 340 times. That’s the real end-game here. There are other resources for learning to program and getting help, but there’s only one site in the world that developers trust this much, and that is worth preserving—the programming equivalent to the Library of Congress.
