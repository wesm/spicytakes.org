---
title: "How To Successfully Compete With Open Source Software"
date: 2009-03-06
url: https://www.kalzumeus.com/2009/03/07/how-to-successfully-compete-with-open-source-software/
slug: how-to-successfully-compete-with-open-source-software
word_count: 3019
---


(This post recently got linked on Japanese blogs.  英語より日本語の方が楽な方：これを和訳しようとしています。日本語版は[こちら](https://www.kalzumeus.com/2009/03/18/competing-with-oss-japanese/)です。)


Every once in a while, somebody on the Business of Software forums asks whether there is any point to trying to compete with open source software (OSS — essentially, software anyone can use and modify without needing to pay money or receive permission).  This is very possible, as folks such as Joel Spolsky [pointed out](http://discuss.joelonsoftware.com/default.asp?biz.5.737375.29) in the ensuing discussion.    I particularly liked [one comment](http://news.ycombinator.com/item?id=505571) on Hacker News about how to compete as Enterprise software.  However, relatively few people in the discussion mentioned B2C (Business To Consumer — you know, the stuff that isn’t paid for by an expense account) software, which people often tell me is doomed, doomed, doomed.  Seeing as how I run a small B2C software business, and am experiencing a crushing shortage of doom, I thought I would explain why this is possible.


**My bona fides:** I run [Bingo Card Creator](http://www.bingocardcreator.com), which makes educational bingo cards for teachers and parents.  It is about as B2C as you can get.  Sales last year were in the $20,000 range, sales this year are up substantially, and I expect profits will exceed my day job salary/benefits/etc by the end of April.  I started the business in July 2006, when there were already at least two OSS projects which did roughly the same thing: [BingoCardMaker](http://sourceforge.net/projects/BingoCardMaker) and [bingo-cards](http://sourceforge.net/projects/bingo-cards).  (You can tell we really spend a lot of time thinking about naming in my niche, can’t you.)


Thus, my comments are about *the other* 99% of OSS projects, the low-profile projects which a) do useful things for people and b) you have never heard of.  All OSS is not Firefox in the same way that all proprietary software is not Microsoft Office.


**I like OSS, too**: I make extensive use of OSS in my business and at my day job.  I routinely contribute code to projects, OSS my own software when it makes competitive sense (you can [download my shopping cart](http://www.bingocardcreator.com/articles/developing-shopping-cart.htm)), and generally love the stuff.  I don’t see OSS and proprietary software as existential threats to each other.


Thus, when I give developers advice on how to compete with OSS, its not in the sense that I want to trample over the movement’s corpse, burn their homes, and hear the lamentations of their women.  I just believe in getting people to the right tools for the right problems, and often, that tool is going to cost money.  (Nothing wrong with that!)


## Places Where Software Developers Can Outdo OSS:


## 1)  Marketing


Software solves problems.  Customers have problems.  Customers do not know that their problems are sometimes solvable with software.


**Less than 1% of customers perceive their problem as a software problem**: Whether your software makes bingo cards or [drafts table plans](http://www.perfecttableplan.com) or [helps people improve their poker game](http://www.pokercopilot.com/), all it is doing is helping someone get around a problem they had long before they sat down at the computer.  After getting frustrated with their existing attempted solution to the problem, they probably Googled something pretty generic like [how do I make bingo cards].  Empirically, only about 800 people out of the 147,000 who found me from Google in the last year were specifically looking for software.  Add in another 1,600 who were looking for a download, and that’s still 97% who had a bingo problem, not a software problem.


**OSS concentrates on the software, not the problems the software can solve**: Take a look at an OSS site, any OSS site.  You’ll see a whole lot of talking about the software, the implementation of the software, the source code for the software, how you can contribute to the software, etc.  You’ll almost never see anything about the problem domain — the assumption is that, if you’ve stumbled upon the site, *you already know you have a software problem*.


If your marketing is premised around your user knowing they have a software problem, you won’t SEO to capture people looking for solutions for the issues in their problem domains.  Your evangelists will talk with other people who are enthusiastic about software, not with people who consider software about as intrinsically interesting as toasters.  (Many of my most enthusiastic customers *despise every minute* of using their computers.  They put up with it because it gets them back to their kids faster than any non-computer alternative.)


## 2) Design


OSS projects, particularly the 99% that are relevant to this discussion, routinely do not allocate resources to creating attractive designs.  For whatever reason, opened source graphical work is still rather rare, most developers (myself included) have the artistic skill of inept mole rats, and the obvious pay-somebody-who-does-it-better solution runs into the problem that the typical OSS project has no budget and no patience to deal with “unfree” licenses, which are the only kind commercially available stock icons have.


This results in a lot of OSS software looking something like:


That design is nice and clean.  However, it looks like the properties dialog box in Eclipse — lots of functionality optimized for packing as many things onto one screen as possible.  There is little thought given to incorporating color into the design, giving the program its own logo or visual identity, or arranging the 13 controls in a user-centric fashion.  Even with those criticisms, this is a good design for OSS software.  I have seen far, far worse.  But we could do so much better, and when we have an incentive to, we do.


**The importance of design**: I don’t personally use Macs but I think everyone in B2C software needs to take lessons from Apple and the Mac community.  They have proven, again and again, that people will pay a premium for products which are attractive.  Often in B2C the first glimpse of the software makes the sale and everything after that is just justifying to the customer that their gut decision was the right one.  (Same with publishing, incidentally: people really do judge books based on their cover.)


Example: I [doubled sales](https://www.kalzumeus.com/2006/08/26/the-visual-impact-stock-icons-make/) of Bingo Card Creator waaaaay back in August 2006 by adding some [more attractive stock icons](http://www.icons-icons.com/roma-icons.php) to it than the [fairly staid Java icons](http://java.sun.com/developer/techDocs/hi/repository/) I had been using previously.  (That first link has the before/after shots if you want to see it.)


The workflow is fundamentally different than BingoCardMaker (more about that later), but you can see that this design makes use of bright, pleasing colors.  (Its absolutely amazing how a few bucks worth of icons makes a bog-standard Swing app look so little like a Swing app, isn’t it?)  This is more inviting to the primarily non-technical users who make up the core of my market: it promises to be fun, not painful, to use.


## 3)  User Experience


“User experience” is easiest to define as “that touchy-feely stuff that Apple does really freaking well”.  The more formal description is that all stages of interaction with the software — from downloading it, to installing it, to using it the first time, to using it the 400th time, and all points in between — should induce joy and contentment, not frustration and rage.


Here’s a bit of homework: find yourself a non-technical person.  Tell them the name of a piece of software on, say, Sourceforge.  Then tell them to download and run it.  Stay in the room but don’t help with completion of the task.


This is so frustrating to most users that the test should probably not be allowed by the human subjects board at most universities.  Somebody might get killed.


Here’s a true story for you.  BingoCardMaker supports one feature which my program does not (picture bingo cards), and which I have no intentions of adding, despite the fact that it is the most requested feature by far.  Accordingly, I used to tell customers who needed that feature “I’m very sorry I can’t help you, but this software can — why don’t you try it?” and I would direct them [straight to the download page](http://sourceforge.net/project/showfiles.php?group_id=148249&package_id=163575&release_id=370153).


One customer (who is by no means unintelligent) was furious because she spent fifteen minutes on the page unsuccessfully trying to download before deciding it was broken.  Here’s the section of the page: can you tell me what went wrong?


Those words architecture or operating system are pretty confusing, but the word “download” is not.  My customer knew she had to “download”.  So she clicked it, and “the screen blinked away”.  (Clicking download takes you to a list of packages published by the product — totally obvious to a non-technical user, right?)  Then she got back and clicked on options, figuring that it would offer “options for downloading”, but nothing she clicked there worked either.  Finally, frustration mounting rapidly, she clicked Bingo Card Maker because that was what she wanted… and the screen “blinked” again.  (It collapses the tree of options for that package, causing the BingoCardMaker-5.5.1.jar link to vanish.  That link is the one you have to click.  This is quite obvious if you are a Java developer — not quite so obvious if you hold a PhD in English Literature.)


**Do not bury the goal**: I should mention that if you’re coming from the project page at Sourceforge, the above is three clicks deep after clicking download.  By comparison, downloading Bingo Card Creator takes one click for most people — its the big, blue button that says Download Free Trial.  Folks whose browsers don’t support that are showed the following:


That was once described as “big pancake buttons” by one of the international developers on the Business of Software forums, and the name sort of stuck.  **Pancake buttons work**.  They are far, far, far more effective at helping users complete their task (downloading the software) that unobtrusive text links or smaller download buttons — the pancake buttons outperformed by smaller buttons by a factor of 3, and those buttons were themselves much improved successors of my original buttons which had outperformed plain text links by a factor of two.


Wow, it sounds that I’m saying that most prospective users of OSS can’t even manage to download it.  Let me be clear: **that is exactly what I am saying**.  It isn’t their fault — when our users can’t use our software (and websites are just a special case of software), that means we have failed in our jobs, whether we’re proprietary or OSS developers.


**On to installation**: User experience scarcely ends with the download.  Oh no, the *opportunities to frustrate and enrage* are just beginning!  For example, that JAR file they just downloaded got dumped in a downloads folder somewhere and… well… that is about it.  To execute it, you need to be able to find your downloads folder and double click on it.  The next time you want to execute it, you have to do that again.


By comparison, if you were downloading Bingo Card Creator, you’d get a prompt from your browser asking if you wanted to run it.  It would then take you through a Windows installer which, in a very simple fashion with sensible defaults, would put links on your desktop and start menu to the program, then start it up for you.  At no point do you have to learn any irrelevant trivia like “JAR files are special things created by Java which are sort of like programs, except when they aren’t, and sometimes double clicking on them runs them, except when it causes nasty errors.”


There is a JAR file sitting at the heart of Bingo Card Creator, too — and if my users need to know that then I have failed.  Incidentally, if you do desktop Java development for Windows, please use [JET](http://www.excelsior-usa.com/jet.html) or [Launch4j](http://launch4j.sourceforge.net/) or something.  Java developers deploying to Mac should use the JAR bundler.  (You can even do this from a Windows machine with [an OSS ant task](http://sourceforge.net/projects/jarbundler).  It is a lifesaver for all of us committed Vista users who need to deploy to OS X.)


**User Experience never ends**: All interaction with your program, with your site, with your community has user experience implications.  There are many, many opportunities to flub it.  I can’t cover all of them in this article, but I hope to expand on ways to not flub them at a later date.


## 4) Speaking the users’ language


In keeping with the “Users do not have a software problem” and “Users do not care about your technology choices” points covered above, users fundamentally do not talk like developers.  See this description for one of my OSS competitors:


GPL bingo card printing program (numeric, letter bingo and picture bingo). Also prints a calling sequence (equivalent to the output from a barrel full of balls). XML output for later linking to multimedia engine.


Let’s try that again with the technobabble removed:


GPL bingo card printing program (numeric, letter bingo and picture bingo). Also prints a calling sequence (equivalent to the output from a barrel full of balls). XML output for later linking to multimedia engine.


Those two surviving sentence fragments are all the publicly available description of this program.  Yep, that’s it.  You might have heard that OSS is weak on documentation?  That is only a problem if there is enough of a reason to suspect that the program will work for you in the first place, and two sentences is probably not enough to do it.


I want to quote a real customer of mine, who captures the B2C mindset about installing software very eloquently: “Before I download yet another program to my poor old computer, could you let me know if I can…”  Painful experience has taught this woman that downloading software to her computer is a risky activity.  Your website, in addition to making this process totally painless, needs to establish to her up-front the benefits of using your software and *the safety of doing so*.  (Communicating safety could be an entire article in itself.)


Incidentally, the **Internet sucks the literacy out of people**, so be prepared to explain the same thing several times to get the message across.  The most common question I have is “Is every bingo card unique?”  Yep, they’re randomized — that is the only reason you’d use the program and that feature has been the core of it since v1.0.  That fact is mentioned ***twice in bold*** on my front page, printed on the main UI of the program itself, etc.  And people still manage to ignore all that, find my email address, and ask me.


Can you imagine how confused users would be if key features were documented only in blog postings distilled from commit logs, and present nowhere on the product site itself?


(**I’m looking at you,** **[Rails](http://stackoverflow.com/questions/138311/how-do-i-turn-off-csrf-protection-in-a-rails-app/138372#138372)**.)


## 5) Support


If you’ve been around OSS for any length of time, you know that almost every community has members who are caring, helpful, and patient.  Unfortunately, they’re not the only people handling support.  I get a lot of questions which sound something like “I clicked the button and it didn’t work” or “plz help can’t print” or “I downloaded the program to my printer and now my screen is grey.  Did you give me a virus?”


(If you don’t understand the significance of the screen being grey, [look at the photo here](http://www.joelonsoftware.com/articles/AardvarkMidtermReport.html).)


You can probably imagine how well those would go over on the typical OSS mailing list.  To say nothing of basic computer operation questions like “I bought a new computer last week and need to put your software on it.  What do I need to do?  Its not the old computer, which has your software on it, its a new computer.”


Most customers with B2C software — in my experience, about 95% as of late — don’t actually *need* to ask a question of you, ever.  You can handle all of their needs with well-thought-out automatic processes, FAQs, help files, rigorous improvement of any part of the software that routinely causes confusion, and the like.  However, users like know that there is someone who will be happy to help them out if they need it.  That is the main purpose of offering customer support — decreasing the perceived risk of using your software by demonstrating that there is a safety net.  (This is one reason you should write your [support page ](http://www.bingocardcreator.com/support.htm)with an eye to it being seen by someone who isn’t even using your software.)


## 6)  Technical superiority


You’ll notice I’ve been concentrating mostly on the 90% of the software busines that happens outside of the IDE.  However, there is no reason to assume that OSS is superior on a technical front, either.  I know, a million eyes makes all bugs shallow, yadda yadda yadda.  Back in my reality:

- the median number of developers per OSS project hosted on Sourceforge is 1.
- Perhaps one project in five will ever leave beta.
- All software has bugs, OSS is no exception.
- The average software, commercial or OSS, is a usability nightmare.
- Many programs have not been updated in years and lack the benefit of significant improvements in the state of the art made recently, from modern interface design to first-class integration with the Internet.
- Some OSS tries to be everything for everybody and ignores niche markets with pressing specific issues.
- Other OSS is hyper-adapted to the problems of a handful of developers scratching their own itches and is unusable by anyone with other requirements.


In other words, you can compete with OSS on a technical level the same way you compete with proprietary software on a technical level: execute better.  There’s really no magic to that.


## Conclusion


All of these are opportunities for commercial developers to compete with OSS.


The world is changing all the time, but plain-ol’ commercial desktop software still has a place in it.  Don’t get worried — concentrate on doing what you do well, from development to marketing to support, and the market will take care of the rest.


If you found this article interesting, try looking around the blog or [signing up for the RSS feed](https://www.kalzumeus.com/feed/).  There’s a lot more where this came from.

if (typeof window.Delicious == "undefined") window.Delicious = {};
    Delicious.BLOGBADGE_DEFAULT_CLASS = 'delicious-blogbadge-line';
//