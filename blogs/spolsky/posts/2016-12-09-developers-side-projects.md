---
title: "Developers’ side projects"
date: 2016-12-09
url: https://www.joelonsoftware.com/2016/12/09/developers-side-projects/
word_count: 1745
---


Pretty much 100% of developers working for other people end up signing some kind of “proprietary invention agreement,” but almost all of them misunderstand what’s going on with that agreement. Most developers think that the work they do at work belongs to their employer, but anything they work on at home or on their own time is theirs. This is wrong enough to be dangerous.


So let’s consider this question: if you’re a developer working for software company, does that company own what you do in your spare time?


Before I start: be careful before taking legal advice from the Internet. I see enough wrong information that you could get in trouble. Non-US readers should also be aware that the law and legal practice could be completely different in their country.


There are three pieces of information you would need to know to answer this question:


1. What state (or country) are you employed in?


There are state laws that vary from state to state which may even override specific contracts.


2. What does *your* contract with your employer say?


In the US, in general, courts are very lenient about letting people sign any kind of contract they want, but sometimes, state laws will specifically say “even if you sign such and such a contract, the law overrides.”


3. Are you a contractor or an employee? In the US there are two different ways you might be hired, and the law is different in each case.


But before I can even begin to explain these issues, we gotta break it down.


Imagine that you start a software company. You need a developer. So you hire Sarah from across the street and make a deal whereby you will pay her $20 per hour and she will write lines of code for your software product. She writes the code, you pay her the $20/hour, and all is well. Right?


Well… maybe. In the United States, if you hired Sarah as a contractor, she still owns the copyright on that work. That is kind of weird, because you might say, “Well, I paid her for it.” It sounds weird, but it is the default way copyright works. In fact, if you hire a photographer to take pictures for your wedding, you own the *copies* of the pictures that you get, but the photographer still owns the copyright and has the legal monopoly on making more copies of those pictures. Surprise! Same applies to code.


*Every* software company is going to want to own the copyright to the code that its employees write for them, so *no* software company can accept the “default” way the law works. That is why *all* software companies that are well-managed will require *all* developers, at the very least, to sign an agreement that says, at the very least, that

- in exchange for receiving a salary,
- the developer agrees to “assign” (give) the copyright to the company.


This agreement can happen in the employment contract or in a separate “Proprietary Invention Assignment” contract. The way it is often expressed is by using the legal phrase *[work for hire](http://en.wikipedia.org/wiki/Work_for_hire)*, which means “we have decided that the copyright will be owned by the company, not the employee.”


Now, we still haven’t said anything about spare time work yet. Suppose, now, you have a little game company. Instead of making software, you knock out three or four clever games every few months. You can’t invent all the games yourself. So you go out and hire a game designer to invent games. You are going to pay the game designer $6,000 a month to invent new games. Those games will be clever and novel. They are patentable. It is important to you, as a company, to own the *patents* on the games.


Your game designer works for a year and invents 7 games. At the end of the year, she sues you, claiming that she owns 4 of them, because those particular games were invented between 5pm and 9am, when she wasn’t on duty.


Ooops. That’s not what you meant. You wanted to pay her for *all* the games that she invents, and you recognize that the actual *process of invention* for which you are paying her may happen at any time… on weekdays, weekends, in the office, in the cubicle, at home, in the shower, climbing a mountain on vacation.


So before you hire this developer, you agree, “hey listen, I know that inventing happens all the time, and it’s impossible to prove whether you invented something while you were sitting in the chair I supplied in the cubicle I supplied or not. I don’t just want to buy your 9:00-5:00 inventions. I want them all, and I’m going to pay you a nice salary to get them all,” and she agrees to that, so now you want to sign something that says that all her inventions belong to the company for as long as she is employed by the company.


This is where we are by default. This is the *standard* employment contract for developers, inventors, and researchers.


Even if a company decided, “oh gosh, we don’t want to own the 5:00-9:00 inventions,” they would soon get into trouble. Why? Because they might try to take an investment, and the investor would say, “prove to me that you’re not going to get sued by some disgruntled ex-employee who claims to have invented the things that you’re selling.” The company wants to be able to pull out a list of all current and past employees, and show a contract from *every single one of them* assigning inventions to the company. This is expected as a part of due diligence in every single high tech financing, merger, and acquisition, so a software company that isn’t careful about getting these assignments is going to have trouble getting financed, or merging, or being acquired, and that ONE GUY from 1998 who didn’t sign the agreement is going to be a real jerk about signing it now, because he knows that he’s personally holding up a $350,000,000 acquisition and he can demand a lot of money to sign.


So… every software company *tries* to own *everything* that its employees do. (They don’t *necessarily* enforce it in cases of unrelated hobby projects, but on paper, they probably can.)


Software developers, as you can tell from this thread, found this situation to be upsetting. They always imagined that they should be able to sit in their own room at night on their own computer writing their own code for their own purposes and own the copyright and patents. So along came state legislators, in certain states (like California) but not others (not New York, for example). These state legislatures usually passed laws that said something like this:


> Anything you do on your own time, with your own equipment, that is not related to your employer’s line of work is yours, even if the contract you signed says otherwise.


Because this is the law of California, this particular clause is built into the standard Nolo contract and most of the standard contracts that California law firms give their software company clients, so programmers all over the country might well have this in their contract even if their state doesn’t require it.


Let’s look at that closely.


*On your own time.* Easy to determine, I imagine.


*With your own equipment.* Trivial to determine.


*Not related to your employer’s line of work.* Um, wait. What’s the definition of *related?* If my employer is Google, they do *everything.* They made a goddamn HOT AIR BALLOON with an internet router in it once. Are hot air balloons related? Obviously search engines, mail, web apps, and advertising are related to Google’s line of work. Hmmm.


OK, what if my employer is a small company making software for the legal industry. Would software for the accounting industry be “related”?


I don’t know. It’s a big enough ambiguity that you could drive a truck through it. It’s probably going to depend on a judge or jury.


The judge (or jury) is *likely* to be friendly to the poor employee against Big Bad Google, but you can’t depend on it.


This ambiguity is meant to create enough of a chilling effect on the employee working in their spare time that for all intents and purposes it achieves the effect that the employer wants: the employee doesn’t bother doing any side projects that might turn into a business some day, and the employer gets a nice, refreshed employee coming to work in the morning after spending the previous evening watching TV.


So… to answer the question. There is unlikely to be substantial difference between the contracts that you sign at various companies in the US working as a developer or in the law that applies. All of them need to purchase your copyright and patents without having to prove that they were generated “on the clock,” so they will all try to do this, unless the company is being negligent and has not arranged for appropriate contracts to be in place, in which case, the company is probably being badly mismanaged and there’s another reason not to work there.


The only difference is in the stance of management as to how hard they want to *enforce* their rights under these contracts. This can vary from:

- We love side projects. Have fun!
- We don’t really like side projects. You should be thinking about things for us.
- We love side projects. We love them so much we want to own them and sell them!
- We are kinda indifferent. If you piss us off, we will look for ways to make you miserable. If you leave and start a competitive company or even a half-competitive company, we will use this contract to bring you to tears. BUT, if you don’t piss us off, and serve us loyally, we’ll look the other way when your iPhone app starts making $40,000 a month.


It may vary depending on whom you talk to, who is in power at any particular time, and whether or not you’re sleeping with the boss. You’re on your own, basically—the only way to gain independence is to be independent. Being an employee of a high tech company whose *product* is intellectual means that you have decided that you want to sell your intellectual output, and maybe that’s OK, and maybe it’s not, but it’s a free choice.
