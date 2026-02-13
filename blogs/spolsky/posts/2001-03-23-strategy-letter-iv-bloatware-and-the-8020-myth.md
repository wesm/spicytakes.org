---
title: "Strategy Letter IV: Bloatware and the 80/20 Myth"
date: 2001-03-23
url: https://www.joelonsoftware.com/2001/03/23/strategy-letter-iv-bloatware-and-the-8020-myth/
word_count: 1168
---


Version 5.0 of Microsoft’s flagship spreadsheet program Excel came out in 1993. It was positively *huge*: it required a whole *15 megabytes* of hard drive space. In those days we could still remember our first 20MB PC hard drives (around 1985) and so 15MB sure seemed like a lot.


By the time Excel 2000 came out, it required a whopping 146MB … almost a tenfold increase! Dang those sloppy Microsoft programmers, right?


Wrong.


I’ll bet you think I’m going to write one of those boring articles you see all over the net  bemoaning “bloatware”.  Whine whine whine, this stuff is so bloated, oh woe is me, edlin and vi are *so* much better than Word and Emacs because they are svelte, etc.


Ha ha! I tricked you! I’m not going to write that article again, because it’s not true.


In 1993, given the cost of hard drives in those days, Microsoft Excel 5.0 took up about $36 worth of hard drive space.


In 2000, given the cost of hard drives in 2000, Microsoft Excel 2000 takes up about $1.03 in hard drive space.


(These figures are adjusted for inflation and based on hard drive price data from [here](http://www.littletechshoppe.com/ns1625/winchest.html).)


In real terms, it’s almost like Excel is actually *getting smaller*!


What is bloatware, exactly? [The Jargon File](http://www.tuxedo.org/~esr/jargon/html/entry/bloatware.html) snidely defines it as “software that provides minimal functionality while requiring a disproportionate amount of diskspace and memory. Especially used for application and OS upgrades. This term is very common in the Windows/NT world. So is its cause.”


I guess those guys just hate Windows. I haven’t run out of memory in more than a decade, ever since virtual memory appeared in Windows 386 (1989). And hard drive space is down to $0.0071 per megabyte and still plummeting like a sheep learning to fly by jumping out of a tree.


Maybe Linus Åkerlund can explain it. On his web page, he [writes](http://user.tninet.se/~uxm165t/bloatware.html), “The big disadvantage of using these bloated programs is that you have to load this very large program, even if you just want to accomplish one tiny little thing. It eats up all your memory… you’re not using your system in an efficient way. You make the system seem more inefficient than it really is, and this is totally unnecessary.”


Ohhh. It eats up all your memory. I see. Actually, well, no, it doesn’t. Ever since Windows 1.0, in 1987, the operating system only loads pages as they are used. If you have a 15MB executable and you only use code that spans 2MB worth of pages, you will only ever load 2MB from disk to RAM. In fact if you have a modern version of Windows, the OS will automatically rearrange those pages on the hard drive so that they’re consecutive, which makes the program start even faster next time.


And I don’t think anyone will deny that on today’s overpowered, under-priced computers, loading a huge program is still faster than loading a small program was even 5 years ago. So what’s the problem?


[RA Downes](http://www.blu.org/faq/bloat.html) gives us a clue. It looks like he spent *hours* dissecting a small Microsoft utility, apparently enraged that it was a whole megabyte in size. (That’s 3.15 cents of hard drive space at the time he wrote the article). In his opinion, the program should have been around 95% smaller. The joke is that the utility he dissected is something called RegClean, which you’ve probably never heard of. This is a program that goes through your Windows registry looking for things that aren’t being used and deleting them. You have to be a little bit on the obsessive-compulsive side to care about cleaning up unused parts of your registry. So I’m starting to suspect that fretting about bloatware is more of a [mental health problem](http://www.mentalhealth.com/dis/p20-an05.html) than a software problem.


In fact there are lots of great reasons for bloatware. For one, if programmers don’t have to worry about how large their code is, they can ship it sooner. And that means you get more features, and features make your life better (when you use them) and don’t usually hurt (when you don’t). If your software vendor stops, before shipping, and spends two months squeezing the code down to make it 50% smaller, the net benefit to you is going to be imperceptible. Maybe, just maybe, if you tend to keep your hard drive full, that’s one more Duran Duran MP3 you can download. But the loss to you of waiting an extra two months for the new version *is* perceptible, and the loss to the software company that has to give up two months of sales is even worse.


A lot of software developers are seduced by the old “80/20” rule. It *seems *to make a lot of sense: 80% of the people use 20% of the features. So you convince yourself that you only need to implement 20% of the features, and you can still sell 80% as many copies.


Unfortunately, it’s never the same 20%. Everybody uses a *different* set of features. In the last 10 years I have probably heard of *dozens* of companies who, determined not to learn from each other, tried to release “lite” word processors that only implement 20% of the features. This story is as old as the PC. Most of the time, what happens is that they give their program to a journalist to review, and the journalist reviews it by writing their review using the new word processor, and then the journalist tries to find the “word count” feature which they need because most journalists have precise word count requirements, and it’s not there, because it’s in the “80% that nobody uses,” and the journalist ends up writing [a story](http://www.zdnet.com/anchordesk/stories/story/0,10738,2681437,00.html) that attempts to claim simultaneously that lite programs are good, bloat is bad, and I can’t use this damn thing ’cause it won’t count my words. If I had a dollar for [every](http://washingtonpost.com/wp-srv/tech/reviews/finder/rev_1030.htm) time this has happened I would be very happy.


When you start marketing your “lite” product, and you tell people, “hey, it’s lite, only 1MB,” they tend to be very happy, then they ask you if it has *their* crucial feature, and it doesn’t, so they don’t buy your product.


Bottom line: if your strategy is “80/20”, you’re going to have trouble selling software. That’s just reality. This strategy is as old as the software industry itself and it just doesn’t pay; what’s surprising is how many executives at [fast companies](http://www.fuckedcompany.com/) think that it’s going to work.


Jamie Zawinski says it best, [discussing](http://www.jwz.org/doc/easter-eggs.html) the original version of Netscape that changed the world. “Convenient though it would be if it were true, Mozilla [Netscape 1.0] is not big because it’s full of useless crap. Mozilla is big because your needs are big. Your needs are big because the Internet is big. There are lots of small, lean web browsers out there that, incidentally, do almost nothing useful. But being a shining jewel of perfection was not a goal when we wrote Mozilla.”
