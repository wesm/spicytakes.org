---
title: "The Start-Up Trap"
date: 2013-03-05
url: https://blog.cleancoder.com/uncle-bob/2013/03/05/TheStartUpTrap.html
slug: TheStartUpTrap
word_count: 1124
---

* **You**  have joined a new startup.
* **You**  are a multi-talented mega-being.
* **You**  can work 60, 70, 80 hours per week to get the job done.
* **You**  are a  *top-notch*  coder and designer.
* **You**  won’t fall into the traps that others have fallen into.
* **You**  will make sure that  *this*  time will be different.
* **You**  are  *so*  good that the rules don’t apply to  **you** .
* **You**  are  *fucked* .

###The Start-Up Trap.
It’s a sad story that we’ve seen over and over again.  A young programmer begins with all the best intensions, learns all the right disciplines, develops all the right skills, and then falls prey to  *The Start-Up Trap* .   The Start-Up Trap is the idea that  *your*  situation is different – that everything you’ve learned about how to do software well somehow doesn’t apply to  *this*  particular job.  You think it will apply later, once you’ve succeeded.  But not now.  Not yet.  Not while you are in a race to succeed.

The Start-Up trap is the thought that the start-up phase is  *different* ; and that while you are in that phase success depends upon  *breaking*  the rules.  This is  *stupid* .  The start-up phase is  *not*  different.  The start-up phase is simply the first of many phases, and it sets the tone for all those other phases.  Come back to that company in five years and (if they’ve managed to survive) they’ll still have the same attitude towards the rules that they had in the first phase – except, perhaps, for the overtime. (giggle).

Here’s a little tip:  The disciplines that lead to successful software are always valid, no matter what phase the company is in.  It is laughable to think that good disciplines are less important during the start-up phase.  The truth is that, during the start-up phase, those disciplines are just as critical as they are at any other time.

Of course one of the disciplines I’m talking about is TDD.  Anybody who thinks they can go faster by  *not*  writing tests is smoking some pretty serious shit.  Oh, I know you are a warrior-god.  I know you can write the code perfectly every time.  I know that the deadline looms and you  *just don’t have time to write tests* .  – I’m sorry for your impending failures.  I’m sorry that you’re going slow and just don’t know it yet.  And I’m  *very*  sorry that when you finally brute-force your way to some modicum of success that you will credit your bad behavior, and recommend it to others.  God help us all, because you won’t.

Ask yourself this:  How does the accounting officer of a start-up behave?  This person is responsible for managing the money of the investors.  Do you think that accountant has deadlines?  Do you think he’s under pressure to deliver projections, forecasts, cash-flow reports, etc?  Do you think his bosses tolerate schedule slips in his duties?  I’ll tell you now that the guy managing the investors’ money is under a hell of a lot more pressure than any software developer is.

So how does this accountant behave?  Does he double check his work?  Does he practice double-entry bookkeeping?  Does he follow all his rules and disciplines?  Or are the rules different because he’s in the start-up phase?

What if it was  *your*  company, and  *your*  money.  What would  *you*  think of a start-up accountant who didn’t check his sums; who neglected the debit side of the books and trusted the health and future of  *your*  company to the single unchecked sums of the credit side?

You’d fire his ass!  You’d fire it so fast that the rest of his worthless carcass would be left outside the door wondering where his ass went!

Is your code somehow less important than that account’s spreadsheets?  Are errors in the code somehow more tolerable than errors in those spreadsheets?  Can errors in the code take the company down and ruin it’s reputation with it’s customers, and investors?  You know the answer to these questions.  And you know this:  If accountants can find a way to practice their disciplines in a start-up;  *so can you.*

Is neglecting TDD going to help you go fast?  To quote Captain Sulu when the Klingon power moon of Praxis exploded and a young Lieutenant asked whether they should notify Star-Fleet:  “Are you kidding?”  ARE YOU KIDDING?

NO, you aren’t going to go fast.  You’re going to go  *slow* .  And the reasons are simple, and you already know them.  You’re going to go slow because you won’t be able to refactor.  The code will rot – quickly.  It will get harder and harder to manage.  And  *you will slow down.*

You won’t notice it at first because it still  *feels*  fast.  You are working hard and spending 60, 70, 80 hours per week on the code.  The sheer effort you are applying is enormous; and that  *feels*  fast.

But effort and speed are not related.  It is easy to expend a tremendous amount of effort and make no progress at all.   *Hell* , it’s easy to expend gargantuan effort and make  *negative*  progress.   *Effort equates neither to speed nor direction.*

As time passes your estimates will grow.  You’ll find it harder and harder to add new features.  You will find more and more bugs accumulating.  You’ll start to parse the bugs into critical and acceptable (as if any bug is acceptable!)  You’ll create modules that are so fragile you won’t trust yourself, or anyone else, to modify them; so you’ll work around them.  You’ll build a festering pile of code that, with every passing week, requires more and more effort just to keep running. Forward progress will slow and falter.  It may even reverse as each release becomes buggier and buggier, and less and less stable.  Catastrophes will become more and more common as errors, that should never have happened, create corruptions and damage that take huge traunches of time to repair.

You  *know*  the story.  You  *know*  this is where others have wound up.  If you are old enough,  *you*  have probably wound up there once or twice yourself.  And yet that Start-Up Trap still sings it’s siren song and lures you into destructive, slow, catastrophic behaviors.

If you want to go  *fast* .  If you want the best chance of making all your deadlines.  If you want the  *best*  chance of success.  Then I can give you no better advice than this:   *Follow your disciplines!*   Write your tests.  Refactor your code.  Keep things simple and clean.   *Do Not Rush!*   You hold the life-blood of your start-up in your hands.   *Don’t be careless with it!*

Remember:  *The only way to go fast, is to go well.*
