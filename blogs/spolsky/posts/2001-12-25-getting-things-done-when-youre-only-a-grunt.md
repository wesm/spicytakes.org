---
title: "Getting Things Done When You’re Only a Grunt"
date: 2001-12-25
url: https://www.joelonsoftware.com/2001/12/25/getting-things-done-when-youre-only-a-grunt/
word_count: 1554
---


This site is supposed to be about software management*.* But sometimes you don’t have the power to create change in your organization by executive fiat. Obviously, if you’re just a grunt programmer at the bottom of the totem pole, you can’t exactly order people to start creating schedules or bug databases. And in fact even if you’re a manager, you’ve probably discovered that managing developers is a lot like herding cats, only not as fun. Merely saying “make it so” doesn’t make it so.


It can be frustrating when you’re working in an organization that scores low on [The Joel Test](https://www.joelonsoftware.com/articles/fog0000000043.html). No matter how good your code is, your coworkers write such bad code that you’re embarassed to be associated with the project. Or management is making bad decisions about what code to write, so you’re forced to waste your talent debugging the AS/400 version of a retirement-planning game for kids.


You could just leave, I suppose. But presumably, there’s some reason you’re stuck there. The stock options haven’t quite vested, there’s no *better *place to work in Podunk, or perhaps your boss is holding someone you love hostage. In any case, dealing with life on a bad team can be infuriating. But there are strategies for improving your team from the bottom, and I’d like to share a few of them.


**Strategy 1** Just Do It


A lot can be done to improve the project just by one person doing it. Don’t have a daily build server? Make one. Set your own machine up with a scheduled job to make builds at night and send out email results. Does it take too many steps to make the build? Write the makefile. Nobody does usability tests? Do your own hallway usability tests on the mailroom folks with a piece of paper or a VB prototype.


**Strategy 2** Harness the Power of Viral Marketing


Many of the [Joel Test](https://www.joelonsoftware.com/articles/fog0000000043.html) strategies can be implemented by a single person on an uncooperative team. Some of them, if done well, will spread to the rest of the team.


For example, suppose nobody on your team can be persuaded to use a [bug database](https://www.joelonsoftware.com/articles/fog0000000029.html). Don’t let it bother you. Just keep your own. Enter bugs that you find in your own code. If you find a bug that somebody else really should fix, assign the bug to them using the bug database. If you have good [bug tracking software](http://www.fogcreek.com/FogBUGZ), this will send them an email. But now, you can *keep* sending them emails if they don’t fix the bug. Eventually, they’ll see the value of bug tracking and start to use the system as it was intended. If the QA team refuses to input bugs to the bug tracking system, simply refuse to listen to bug reports through any other channel. About the three-thousdandth time that you say to people, “listen, I’d love to fix that, but I’m going to forget. Can you enter a bug in the system?” they’ll start using the database.


Nobody on your team wants to use source control? Create your own CVS repository, on your own hard drive if necessary. Even without cooperation, you can check your code in independently from everybody else’s. Then when they have problems that source control can solve (someone accidentally types rm * ~ instead of rm *~), they’ll come to you for help. Eventually, people will realize that they can have their own checkouts, too.


**Strategy 3** Create a Pocket of Excellence


The team won’t make [schedules](https://www.joelonsoftware.com/articles/fog0000000245.html)? Or [specs](https://www.joelonsoftware.com/articles/fog0000000036.html)? Write your own. Nobody’s going to complain if you take a day or two to write a minimal spec and schedule for the work you’re about to do.


Get better people into the team. Get involved in hiring and [interviewing](https://www.joelonsoftware.com/articles/fog0000000073.html), and recruit good candidates to join the team.


Find the people who are willing to improve and capable of it, and get them on your side. Even on poor teams, you’re likely to have some smart people who just don’t have the experience to create great code. Help them out. Set them up to learn. Read their code checkins. If they do something stupid, don’t send them a snooty email explaining what’s stupid about their checkins. That will just make them angry and defensive. Instead, innocently report the bug that you know is the result of the checkin. Let them figure out what’s causing it. When they find the bug for themselves, they’ll remember that lesson a lot better.


**Strategy 4** Neutralize The Bozos


Even the best teams can have a bozo or two. The frustrating part about having bad programmers on your team is when their bad code breaks your good code, or good programmers have to spend time cleaning up after the bad programmers.


As a grunt, your goal is damage-minimization, a.k.a. containment. At some point, one of these geniuses will spend two weeks writing a bit of code that is so unbelievably bad that it can never work. You’re tempted to spend the fifteen minutes that it takes to rewrite the thing correctly from scratch. Resist the temptation. You’ve got a perfect opportunity to neutralize this moron for several months. Just keep reporting bugs against their code. They will have no choice but to keep slogging away at it for *months* until you can’t find any more bugs. Those are months in which they can’t do any damage anywhere else.


**Strategy 5 **Get Away From Interruptions


All happy work environments are alike (private offices, quiet working conditions, excellent tools, few interruptions and even fewer large meetings). All unhappy work environments are unhappy in their own way.


The bad news is that changing the working environment is almost impossible in virtually any company. Long term leases may mean that even the CEO can’t do anything about it. That’s why so few software developers get private offices. This hurts their companies in at least two ways. First, it makes it harder to recruit top notch developers, who will prefer the firm that gives them cushier conditions (all else being equal). Second, the level of interruptions can dramatically reduce the productivity of developers, who find it impossible to get into the zone and stay in it for any length of time.


Look for ways to get out of this environment. Take a laptop to the company cafeteria, where there are lots of tables that are empty most of the day (and nobody can find you). Book a conference room for the whole day and write code there, and make it clear through the preponderance of checkins just how much more work you get done when you’re in a room by yourself. The next time there’s a crunch on and your manager asks you what you need to Get This Done By Tomorrow, you know what to say. They’ll find you an office for the day. And pretty soon they’ll start wondering what they can do to keep that productive thing going year round.


Come into work late and leave late. Those hours after the rest of the company goes home can be the most productive. Or, if you’re on a team of developers who regularly come in late, get into work at 9 am. You’ll do more work in the two hours before other people come in and start bothering you than you do in the rest of the day.


Don’t keep your email or IM client running. Check your email every hour, if you want, but *don’t keep it running*.


**Strategy 6** Become Invaluable


None of these strategies work if you’re not really an excellent contributor. If you don’t write good code, and lots of it, you’re just going to be resented for messing around with bug databases when you “should be” writing code. There’s nothing more deadly to your career than having a reputation of being so concerned with process that you don’t accomplish anything.


Once, when I started a new job as a grunt programmer at a new company, I discovered that the company was running somewhere around 2 on the [Joel Test](https://www.joelonsoftware.com/articles/fog0000000043.html), and I was determined to fix it. But I also knew that making a good first impression was crucial. So I allocated the first seven hours of every day to just writing code, as was expected of me. There’s nothing like a flurry of checkins to make you look good to the rest of the development team. But I reserved another hour every afternoon before going home to improving the process. I used that time to fix things that made it hard to debug our product. I set up a daily build and a bug database. I fixed all the longstanding annoyances that made development difficult. I wrote specs for the work that I was doing during the day. I wrote a document explaining step-by-step how to create a development machine from scratch. I thoroughly documented an important internal language which had been undocumented. Slowly, the process got better and better. Nobody but me (and my team, when I was put in charge of one) ever did schedules or specs, but other than that we hit about 10 on the Joel Test.


You *can* make things better, even when you’re not in charge, but you have to be Caesar’s Wife: above suspicion. Otherwise you’ll make enemies as you go along.


[Any other ideas?](http://discuss.fogcreek.com/joelonsoftware/default.asp?cmd=show&ixPost=2033)
