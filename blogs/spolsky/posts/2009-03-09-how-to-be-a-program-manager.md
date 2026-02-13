---
title: "How to be a program manager"
date: 2009-03-09
url: https://www.joelonsoftware.com/2009/03/09/how-to-be-a-program-manager/
word_count: 2892
---


Having a good program manager is one of the secret formulas to making really great software. And you probably don’t have one on your team, because most teams don’t.


Charles Simonyi, the brilliant programmer who co-invented WYSIWYG word processing, dated Martha Stewart, made a billion dollars off of Microsoft stock and went into space, first tried to solve the [Mythical Man Month](http://www.amazon.com/gp/product/0201835959?ie=UTF8&tag=joelonsoftware&linkCode=as2&camp=1789&creative=390957&creativeASIN=0201835959) problem of organizing really big software teams by creating one super duper überprogrammer writing the top-level functions, while handing off the implementation of the lower-level functions to a team of grunt junior-programmers as needed. They called this position *program manager. *Simonyi is brilliant, but this idea, not so much. Nobody wanted to be a grunt junior programmer, I guess.


> For more on the history, read William Poundstone’s [How Would You Move Mount Fuji?](http://www.amazon.com/gp/product/0316778494?ie=UTF8&tag=joelonsoftware&linkCode=as2&camp=1789&creative=9325&creativeASIN=0316778494)


Jabe Blumenthal, a programmer on the Mac Excel team in the late 80s, recycled the title for a different job. He had noticed that software development was getting so complicated that none of the programmers had the time to figure out how to make software that was either usable or useful. The marketing team was ranting and raving about customer needs and nobody had time to talk to them or translate their MBA-speak into actual features. There was a lot of product design stuff that took a lot of work: talking to users, running usability tests, reviewing competitive products, and thinking hard about how to make things easier, and most programmers just didn’t have the time (nor were they particularly good at it). Blumenthal took the title “Program Manager,” but reinvented the job completely.


### What does a program manager do?


Henceforth, a program manager would:

1. Design UIs
2. Write functional specs
3. Coordinate teams
4. Serve as the customer advocate, and
5. Wear Banana Republic chinos


On small products, you might just have one program manager, but on larger products, you would probably have more than one. Each can be responsible for some subset of the features. A good rule of thumb is that it takes about one program manager for every four programmers. If you’re having trouble dividing up the work, one approach I learned from Mike Conte is to [divide up the product according to user activities](https://www.joelonsoftware.com/uibook/chapters/fog0000000065.html). For example, Twitter could be divided into four user activities:

1. Registering and getting started
2. Posting messages and reading replies
3. Configuring your account
4. Searching for news


Tyler Griffin Hicks-WrightMy first program management assignment at Microsoft was on Excel, working on the user activity called “customization,” i.e., scripting and macros. The first thing I had to do was figure out what customers needed, which I did by talking to as many customers as I could until I started to get kind of bored because I kept hearing the same thing. I spent a lot of time talking to the development team to figure out what would be possible and reasonable to implement in a single 18 month release, and I spent a lot of time talking to the Visual Basic team to see if they could supply a compiler, code editor, and dialog box editor that could be used in Excel for our macro language. I also had to talk to Apple, which was developing their own universal macro language called AppleScript, and the other application teams at Microsoft, mainly Word, Access, Project, and Mail, who generally did whatever Excel did. Most of this process consisted of talking. Meetings, email, phone calls. I am scarred for life from this, and now cower in my office in fear that the phone will ring.


The second step was writing a vision statement: sort of a broad document that said, this is how Visual Basic would work in Excel, this is what some sample macros would look like, these are the major pieces we would need to build, and this is how it would solve customers’ problems. When that didn’t generate too many objections, I started working on a much more detailed spec, which explained, down to the smallest detail, how everything looked to the user.


This was a functional spec, not a technical spec, which means, all it talked about was what the user saw, not how it was implemented. ([Read all about functional specs here](https://www.joelonsoftware.com/articles/fog0000000036.html).) A program manager doesn’t care how the development team implements things internally. As I sent chapters of the spec to Ben Waldman, the development lead, he and his team sat down and figured out what they had to do internally to make it work. They came up with a rather brilliant and very compact table that mapped the object-oriented interface I was defining onto internal Excel functions, but that really wasn’t my business. I didn’t know too much about Excel internals and didn’t really know how things should be implemented.


Truth be told, I didn’t know anything about anything. Fresh out of college, I didn’t have enough experience to develop the code, test the code, write the documentation, market the product, or do the usability tests. Luckily, Microsoft had seriously experienced gurus in each of those positions, who taught me everything I know today, and who did the real work of producing an awesome product. For example, I knew that users would want to copy the value of a spreadsheet cell into a variable:


```
 x = [A1]  
```


had to work. The trouble was that a cell could hold a number or a string, but Basic was early bound… you had to DIM x as an Integer, Float or String before you could use it.


Basic had to get some kind of dynamic types, but I wasn’t smart enough to figure out how to do that. Didn’t matter. Tom Corbett, a programmer on the Visual Basic team, [figured out how](http://www.patentstorm.us/patents/5689709/description.html). And thus Variants and IDispatch were born, and Basic became a dynamic language with what you kids now call “duck typing”. The point being, my job wasn’t necessarily to solve problems, it was to figure out what customers needed and make sure that programmers figured out how to solve them.


Once the spec was finished and the development team got down to work, I had two responsibilities: resolving any questions that came up about the design, and talking to all the other teams so that the developers didn’t have to. I met with the testers explaining how things were supposed to work and helping them plan how to test everything. I met with the documentation team, making sure they understood how to write a good tutorial and reference for Excel Basic. I met with localization experts to figure out a localization strategy. I sat down with marketing to explain the marketing benefits of VBA. I worked with usability experts to set up usability tests.


A program manager does go to a lot of meetings, but doesn’t produce much other than that written spec, which is why as a twerp fresh out of school I was still able to do the job. You don’t have to be a 14-year veteran programmer to work as a program manager (in fact, with 14 years of programming experience, you might know too much to be a good user advocate.)


### Conflict


[Tom Chi and Kevin Cheng](http://www.ok-cancel.com/comic/4.html)Lacking a program manager, your garden-variety super-smart programmer is going to come up with a completely baffling user interface that makes perfect sense IF YOU’RE A VULCAN (cf. git). The best programmers are notoriously brilliant, and have some trouble imagining what it must be like not to be able to memorize 16 one-letter command line arguments. These programmers then have a tendency to get attached to their first ideas, especially when they’ve already written the code.


One of the best things a program manager can add to the software design process is a second opinion as to how things should be designed, hopefully one that is more empathetic to those DOUBLE SUPER UNSMART USERS with their pesky mental feebleness requiring that an application be usable without reading the man page, writing a custom emacs-lisp function, or translating numbers into octal in your head.


A good program manager will come with her own ideas for how the UI should work, which might be better, or worse, than the developer’s idea. And then there’s a long debate. Typically, the program manager wants something simple and easy to understand for the users, featuring a telepathic user interface and a 30″ screen that nonetheless fits in your pocket, while the developer wants something that is trivial to implement in code, with a command-line interface (“what’s so unusable about that?”) and Python bindings.


One of the most monumental debates I remember from the Excel 5 project was between a developer who wanted pivot tables to float on the drawing layer above the spreadsheet, and the program manager, who insisted that pivot tables live right in the cells on the spreadsheet. This debate went on for a really, really long time, and eventually, the program manager prevailed, but the final design came out much much better than any one individual’s design would have been.


To make sure that the debate happens respectfully and on a rational basis of facts, it’s absolutely critical that the program managers and developers be *peers*. If developers report to the program manager, at some point during the debate the program manager is going to get sick of the whole thing and just say, “OK, enough talking, now we do it my way.” When they’re peers, this can never happen. It’s a little bit like courts of law: we don’t allow a lawyer for one side to be the judge, and we work on the theory that the truth is most likely to be uncovered through a process of debate between equals. The debate can only be a fair one if neither side has an unfair advantage.


This is an important point, so if you were daydreaming about Sally in 11th grade, wondering where she is now, snap out of it. She’s a biotherapist in Scottsdale, and a Republican. Now pay attention. Programmers *can’t report to program managers* which means, among other things, that the development lead, or the CTO, or the CEO, can’t be the person who writes the specs.


The *number one mistake* most companies make is having the manager of the programmers writing the specs and designing the product. This is a mistake because the design does not get a fair trial, and is not born out of conflict and debate, so it’s not as good as it could be.


I learned this the hard way. At Fog Creek Software, I did a lot of the program management myself, and it was a constant battle to remind people that they were supposed to argue with me when I said wrong things. We’re not a big company but we are finally big enough to have real program managers now, Dan and Jason, and the programmers *love* arguing with them.


Of course, when programmers are peers of the program managers, the programmers tend to have the upper hand. Here’s something that has happened several times: a programmer asks me to intervene in some debate he is having with a program manager.


“Who is going to write the code?” I asked.


“I am…”


“OK, who checks things into source control?”


“Me, I guess, …”


“So what’s the problem, exactly?” I asked. “You have absolute control over the state of each and every bit in the final product. What else do you need? A tiara?”


You see, it turns out that this system puts the burden on the program manager to persuade the programmer, because at some point, the program manager runs the risk that the programmer will give up and just do whatever the heck the programmer feels like. Thus, being effective as a program manager means you have to (a) be right, and (b) earn the respect of the programmers so that they concede that you’re right.


How do you earn this respect?


It helps, as a program manager, to be pretty good at coding yourself. This is unfair. Program managers aren’t supposed to write code. But programmers tend to respect programmers a lot more than non-programmers, no matter how smart they are. It is possible to be an effective program manager without being a coder, but the burden of earning the respect of the programming team will be higher.


> flip the bozo bit v. Decide that someone is a clown, and stop listening to them.


The other way to earn the programming team’s respect is to demonstrate intelligence, open-mindedness, and fairness in any debates that come up. If a program manager says dumb things, the programmer might flip the bozo bit on them. If a program manager becomes personally or emotionally attached to a certain way of doing things, to the point at which they’re being unreasonable, they’re going to lose a lot of credibility… both sides, but especially the program manager, need to be emotionally detached from the debate and willing to consider new evidence and change their opinions when the facts merit it. Finally, if a program manager is seen as playing politics, having private meetings with the boss or trying to divide-and-conquer to win a debate instead of debating on the merits, they’re going to lose a lot of trust of the programmers.


And when a program manager loses the programming team’s trust, it’s over. They’re not going to be effective. The programmers are going to tune them out and do whatever they want anyway. This leads to worse code and wasted time, since not only are you paying an ineffective program manager a salary, but that ineffective program manager is calling meetings and soaking up everybody else’s time even though they’re not really making the code any better.


### Specs? Really? That’s so *unagile*


There are so many development organizations where specs are a monument to mindless bureaucratic paperwork that entire movements sprung up organized around the idea of not writing specs. These people are misguided. Writing a functional specification is at the very heart of agile development, because it lets you iterate rapidly over many possible designs before you write code. Compared to code, a written spec is trivial to change. The very act of writing a specification forces you to think through the design you thought you had in your head, and helps you see the flaws in it quickly so that you can iterate and try more designs. Teams that use functional specifications have better designed products, because they had the opportunity to explore more possible solutions quickly. They also write code faster, because they have a clearer picture when they start of what’s going to be needed. Functional specifications are so important one of the few hard and fast rules at Fog Creek is “No Code Without Spec.”


The exact form the functional specification takes may vary. All a functional specification has to do is explain how the program will behave. It doesn’t say anything about how the code will work internally. You start at the highest level: a vision statement, no more than one page explaining the gist of the new feature. Once that’s nailed down, you can develop storyboards… mockups of the screens showing the user’s progression through the application, with detailed notes showing how they work. For many types of functionality, especially UI-heavy functionality, once you have these storyboards, you’re done. That’s your spec. [Jason Fried, you can go now](http://gettingreal.37signals.com/ch11_Theres_Nothing_Functional_about_a_Functional_Spec.php).


> To learn how to write good functional specifications, read my [four part series](https://www.joelonsoftware.com/articles/fog0000000036.html). If you want to see a typical spec I wrote, you can download the full [Fog Creek Copilot spec](https://www.joelonsoftware.com/articles/AardvarkSpec.html).


For more complex functionality with hidden behavior that’s not expressed in the UI storyboards, you’re going to want more details written down. In any case, the very act of writing down a spec helps you discover problems, conflicts, and design issues long before the first line of code is written, so when you do write the code, you have far fewer unexpected issues popping up which might force a rewrite or, worse, a suboptimal design.


### How do you learn to be a Program Manager?


Mostly, becoming a program manager is about learning: learning about technology, learning about people, and learning how to be effective in a political organization. A good program manager combines an engineer’s approach to designing technology with a politician’s ability to build consensus and bring people together. While you’re working on that, though, there are a few books you should read:


As far as I can tell, Scott Berkun’s book [Making Things Happen](http://www.amazon.com/gp/product/0596517718?ie=UTF8&tag=joelonsoftware&linkCode=as2&camp=1789&creative=390957&creativeASIN=0596517718) is the only book that’s been written that pretty much covers exactly what a program manager has to do, so start with that. Scott was a program manager on the Internet Explorer team for many years.


Another big part of the program manager’s job is user interface design. Read Steve Krug’s [Don’t Make Me Think](http://www.amazon.com/gp/product/0321344758?ie=UTF8&tag=joelonsoftware&linkCode=as2&camp=1789&creative=390957&creativeASIN=0321344758), then my own book [User Interface Design for Programmers](http://www.amazon.com/gp/product/1893115941?ie=UTF8&tag=joelonsoftware&linkCode=as2&camp=1789&creative=390957&creativeASIN=1893115941).


Finally, and I know it sounds cheesy, but Dale Carnegie’s 1937 book [How to Win Friends & Influence People](http://www.amazon.com/gp/product/0671027034?ie=UTF8&tag=joelonsoftware&linkCode=as2&camp=1789&creative=390957&creativeASIN=0671027034) is actually a fantastic introduction to interpersonal skills. It’s the first book I make all the management trainees at Fog Creek read, before anything else, and they always snicker when I tell them to read it, and love it when they’re done.
