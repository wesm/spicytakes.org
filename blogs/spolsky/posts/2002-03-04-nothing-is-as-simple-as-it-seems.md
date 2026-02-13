---
title: "Nothing is as Simple as it Seems"
date: 2002-03-04
url: https://www.joelonsoftware.com/2002/03/04/nothing-is-as-simple-as-it-seems/
word_count: 1235
---


We had a little usability problem in [CityDesk](http://www.fogcreek.com/CityDesk).


Here was the problem: you could import files from the web using a menu command (“Import Web Page”). And you could import files from a disk into CityDesk by dragging them with the mouse. But there was no menu command to import files from a disk. So either people [didn’t discover](http://discuss.fogcreek.com/citydesk/default.asp?cmd=show&ixPost=2187) that it was possible, or people [tried](http://discuss.fogcreek.com/citydesk/default.asp?cmd=show&ixPost=331) to use the Import Web Page feature to import from disk, which didn’t work right.


I thought that it would be easy to fix with a two page wizard. Roughly speaking, page one of the wizard would ask you “Where do you want to import from?” If you chose “disk,” page two would prompt you for a file. If you chose “web,” page two would prompt you for a URL.


I almost started implementing this, but something stopped me, and instead, I started to write a mini-spec. Here’s the spec, in its entirety:


> **Page One
> **Where do you want to import from? (Disk/Web)
> **Page Two (Disk)**
> Standard File/Open dialog
> **Page Two (Web)
> **URL prompt with mini-web-browser


Suddenly something occurred to me. Can you *put* the Windows standard file open dialog, which is usually supplied in toto by the OS, into a wizard?


Hmm.


I investigated. Yes, you can, but it’s [no fun](http://www.vbaccelerator.com/codelib/cmdlgd/cmdlgtp.htm) and takes a few hours of work. How could I make this not be a wizard? I rewrote the spec:


> **Two Menu Items:**
> **1) Import Web Page From Internet** -> Pops Up URL Dialog
> **2) Import Web Page From Disk** -> Pops Up File Open Dialog


Much better. Three minutes of design work saved me hours of coding.


If you’ve spent more than 20 minutes of your life writing code, you’ve probably discovered a good rule of thumb by now: **nothing is as simple as it seems**.


Something as simple as copying a file is full of perils. What if the first argument is a directory? What if the second argument is a file? What if a file with the same name already exists in the destination? What if you don’t have write permission?


What if the copy fails in the middle? What if the destination is on a remote machine which is available, but which requires authentication to continue? What if the files are large and the link is slow and you need to show a progress indicator? What if the transfer speed slows down to *almost* zero… when do you give up and return an error message?


A good way to interview candidates for testing jobs is to give them a simple operation and ask them to enumerate all the things that can possibly go wrong. A classic Microsoft test interview question: how do you test the File Open dialog box? A good tester will be able to rattle off several dozen weird things to test (“file is deleted by another user between the time it is listed in the box and the time you select it and click **Open**“).


OK, so we have one axiom: nothing is as simple as it seems.


There’s another axiom in software engineering, which is, always try to reduce risk. One particularly important piece of risk to avoid is schedule risk, when something takes longer than expected. Schedule risk is bad because your boss yells at you, which makes you unhappy. If that’s not enough motivation for you, the economic reason why schedule risk is bad is because you decided to do a feature based on information that it would take 1 week. Now that you realize that it has taken 20 weeks to accomplish, that decision might well have been wrong. Perhaps if you knew it was going to take 20 weeks, you would have made a different decision. The more wrong decisions you make, the more likely all those tote bags with your company logo will end up in the liquidator’s [warehouse](http://news.bbc.co.uk/hi/english/business/newsid_1229000/1229279.stm) while your ex-CEO mopes that “what sucks is, we weren’t even successful enough to get mentioned on f***edcompany.com when we shut down!”


The combination of nothing-is-as-simple-as-it-seems and reduce-risk can only lead you to one conclusion:


> **You have to design things before you implement them.**


I’m sorry to disappoint you. Yeah, I know, you read Kent Beck and now you think it’s OK to not design things before you implement them. Sorry, it’s *not* OK. You can **not** change things in code “just as easily” as you could change them in the design documents. People say this all the time and it’s wrong. “We use high-level tools these days, like Java and XML. We can change things in minutes in the code. Why not design it in code?” My friend, you can put wheels on your mama but that doesn’t make her a bus, and if you think you can refactor your wrongly-implemented file-copy function to make it preemptive rather than threaded as quickly as I could write that sentence, you’re in deep denial.


Anyway, I don’t think Extreme Programming really advocates zero design. They just say “don’t do any more design than needed,” which is fine. But that’s not what people *hear*. Most programmers are looking for any excuse they can find not to do basic design before implementing features. So they latch onto the “no-design” idea like flies in a bug zapper. Dzzzzzzt! It’s one of those weird forms of laziness where you end up doing more work than you would have done otherwise. I’m too lazy to design the feature on paper first, so I just write some code, and then it’s not right, so I have to fix it, and I spend more time than I would have otherwise. Or, more commonly, I write some code, and then it’s not right, but it’s too late, and my product is inferior and I spend until the end of time making up excuses for why it “has to be that way.” It’s just sloppy and unprofessional.


When Linus Torvalds [bashes design](http://www.uwsg.iu.edu/hypermail/linux/kernel/0112.0/0004.html), he’s talking about huge systems, which have to evolve, or they become Multics. He’s not talking about your File Copy code. And when you consider that he had a pretty clear road map of exactly where he was going, it’s no wonder Linus doesn’t see much value in design. Don’t fall for it. Chances are it doesn’t apply to you. And anyway, Linus is *much* smarter than we are, so things that work for him don’t work for us normal people.


Incremental design and implementation is good. Frequent releases are fine (although for shrink-wrapped or mass market software, it drives customers crazy, never a good idea — instead do frequent internal milestones.) Too much formality in design is a waste of time — I’ve never seen a project benefit from mindless flowcharting or UMLing or CRCing or whatever the flavor-du-jour is. And those huge 10 million lines-of-code behemoth systems Linus is talking about *should *evolve, because humans don’t really know how to design software on that scale.


But when you sit down to write File Copy, or when you sit down to plan the features of the next release of your software, you gotta design. Don’t let the sirens persuade you otherwise.


*Come argue with me about this in person at the [Cutter Summit](http://www.cutter.com/summit/), April 29-May 1st, in Cambridge, MA, where I’ll be on a panel with Tom DeMarco, Kent Beck, and others.*
