---
title: "Doing Terrible Things To Your Code"
date: 2015-07-30
url: https://blog.codinghorror.com/doing-terrible-things-to-your-code/
slug: doing-terrible-things-to-your-code
word_count: 1115
---

In 1992, I thought I was the [best programmer in the world](https://blog.codinghorror.com/why-im-the-best-programmer-in-the-world/). In my defense, I had just graduated from college, this was pre-Internet, and I lived in Boulder, Colorado working in small business jobs where I was lucky to even *hear* about other programmers much less meet them.


I eventually fell in with a guy named Bill O’Neil, who hired me to do contract programming. He formed a company with the regrettably generic name of *Computer Research & Technologies*, and we proceeded to work on various gigs together, building line of business CRUD apps in Visual Basic or FoxPro running on Windows 3.1 (and sometimes DOS, though we had a sense by then that this new-fangled GUI thing was here to stay).


Bill was the first professional programmer I had ever worked with. Heck, for that matter, he was the first *programmer* I ever worked with. He’d spec out some work with me, I’d build it in Visual Basic, and then I’d hand it over to him for review. He’d then calmly proceed to utterly *demolish* my code:

- Tab order? Wrong.
- Entering a number instead of a string? Crash.
- Entering a date in the past? Crash.
- Entering too many characters? Crash.
- UI element alignment? Off.
- Does it work with unusual characters in names like, say, `O'Neil`? Nope.


One thing that surprised me was that the code itself was rarely the problem. He occasionally had some comments about the way I wrote or structured the code, but **what I clearly had no idea about is *testing* my code.**


I dreaded handing my work over to him for inspection. I slowly, painfully learned that the truly difficult part of coding is dealing with the thousands of ways things can go wrong with your application at any given time – most of them user related.


![](https://blog.codinghorror.com/content/images/2025/02/image-105.png)


That was my first experience with [the buddy system](https://blog.codinghorror.com/whos-your-coding-buddy/), and thanks to Bill, I came out of that relationship with a deep respect for software craftsmanship. I have no idea what Bill is up to these days, but I tip my hat to him, wherever he is. I didn’t always enjoy it, but learning to develop discipline around testing (and breaking) my own stuff unquestionably made me a better programmer.


It’s tempting to lay all this responsibility at [the feet of the mythical QA engineer](https://www.sempf.net/post/On-Testing1).


> QA Engineer walks into a bar. Orders a beer. Orders 0 beers. Orders 999999999 beers. Orders a lizard. Orders -1 beers. Orders a sfdeljknesv. – Bill Sempf (@sempf) September 23, 2014


If you are ever lucky enough to work with one, you should have a very, *very* [healthy fear of professional testers](https://blog.codinghorror.com/making-developers-cry-since-1995/). They are terrifying. Just scan this [“Did I remember to test” list](https://web.archive.org/web/20110924022339/http://blogs.msdn.com/b/micahel/archive/2004/07/07/did-i-remember-to.aspx) and you’ll be having the worst kind of flashbacks in no time. And that’s the *abbreviated* version of his list.


I believe a key turning point in every professional programmer’s working life is when you realize [you are your own worst enemy](https://blog.codinghorror.com/on-the-meaning-of-coding-horror/), and the only way to mitigate that threat is to embrace it. *Act* like your own worst enemy. **Break your UI. Break your code. Do *terrible* things** **to your software.**


This means programmers need a good working knowledge of at least the *common* mistakes, the frequent cases that average programmers tend to miss, to work against. You are tester zero. This is your responsibility.


Let’s start with Patrick McKenzie’s classic, [Falsehoods Programmers Believe about Names](http://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/):

1. People have exactly one canonical full name.
2. People have exactly one full name which they go by.
3. People have, at this point in time, exactly one canonical full name.
4. People have, at this point in time, one full name which they go by.
5. People have exactly N names, for any value of N.
6. People’s names fit within a certain defined amount of space.
7. People’s names do not change.
8. People’s names change, but only at a certain enumerated set of events.
9. People’s names are written in ASCII.
10. People’s names are written in any single character set.


That’s just the first 10. There are thirty more. Plus a lot in the comments if you’re in the mood for extra credit. Or, how does [Falsehoods Programmers Believe About Time](http://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time) grab you?

1. There are always 24 hours in a day.
2. Months have either 30 or 31 days.
3. Years have 365 days.
4. February is always 28 days long.
5. Any 24-hour period will always begin and end in the same day (or week, or month).
6. A week always begins and ends in the same month.
7. A week (or a month) always begins and ends in the same year.
8. The machine that a program runs on will always be in the GMT time zone.
9. Ok, that’s not true. But at least the time zone in which a program has to run will never change.
10. Well, surely there will never be a change to the time zone in which a program has to run in production.
11. The system clock will always be set to the correct local time.
12. The system clock will always be set to a time that is not wildly different from the correct local time.
13. If the system clock is incorrect, it will at least always be off by a consistent number of seconds.
14. The server clock and the client clock will always be set to the same time.
15. The server clock and the client clock will always be set to around the same time.


Are there more? Of course there are! There’s even a whole [additional list](http://infiniteundo.com/post/25509354022/more-falsehoods-programmers-believe-about-time) of stuff *he* forgot when he put that giant list together.


![](https://blog.codinghorror.com/content/images/2025/02/image-106.png)


I think you can see where this is going. [This is programming](http://www.stilldrinking.org/programming-sucks). We do this stuff for fun, remember?


But in true made-for-TV fashion, wait, there’s more! Seriously, guys, where are you going? Get back here. We have more awesome failure states to learn about:

- [Falsehoods Programmers Believe About Geography](https://wiesmann.codiferes.net/wordpress/archives/15187)
- [Falsehoods Programmers Believe About Addresses](https://www.mjt.me.uk/posts/falsehoods-programmers-believe-about-addresses/)
- [Falsehoods Programmers Believe About Gender](https://medium.com/gender-2-0/falsehoods-programmers-believe-about-gender-f9a3512b4c9c)


At this point I wouldn’t blame you if you decided to [quit programming altogether](https://blog.codinghorror.com/so-you-dont-want-to-be-a-programmer-after-all/). But I think it’s better if we learn to do for each other what Bill did for me, twenty years ago – teach less experienced developers that **a good programmer knows they *have* to do terrible things to their code**. Do it because if you don’t, I guarantee you other people will, and when they do, they will either walk away or create a support ticket. I’m not sure which is worse.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[code review](https://blog.codinghorror.com/tag/code-review/)
[version control](https://blog.codinghorror.com/tag/version-control/)
