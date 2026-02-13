---
title: "From Podcast 38"
date: 2009-01-31
url: https://www.joelonsoftware.com/2009/01/31/from-podcast-38/
word_count: 1958
---


Here’s a brief conversation between Jeff and I which I transcribed from [Stack Overflow podcast #38](http://blog.stackoverflow.com/2009/01/podcast-38/), starting at [42:28].


**Joel:** There’s a debate over Test Driven Development… should you have unit tests for *everything*, that kind of stuff… a lot of people write to me, after reading [The Joel Test](https://www.joelonsoftware.com/articles/fog0000000043.html), to say, “You should have a 13th thing on here: Unit Testing, 100% unit tests of *all* your code.”


And that strikes me as being just a little bit *too* doctrinaire about something that you *may* not need. Like, the whole idea of agile programming is not to do things before you need them, but to page-fault them in as needed. I feel like automated testing of *everything*, a lot of times, is just not going to help you. In other words, you’re going to write an awful lot of unit tests to insure that code that, really, is *going to work,* and you’re definitely going to find out if it doesn’t work [if you don’t write the tests] does, actually still work, … I don’t know, I’m going to get such flame mail for this because I’m not expressing it that well. But, I feel like if a team really did have *100%* code coverage of their unit tests, there’d be a couple of problems. One, they would have spent an awful lot of time writing unit tests, and they wouldn’t necessarily be able to pay for that time in improved quality. I mean, they’d have *some* improved quality, and they’d have the ability to change things in their code with the confidence that they don’t break anything, but that’s it.


But the real problem with unit tests as I’ve discovered is that the type of changes that you tend to make as code evolves tend to break a constant percentage of your unit tests. Sometimes you will make a change to your code that, somehow, breaks 10% of your unit tests. Intentionally. Because you’ve changed the design of something… you’ve moved a menu, and now everything that relied on that menu being *there*… the menu is now *elsewhere*. And so all those tests now break. And you have to be able to go in and recreate those tests to reflect the new reality of the code.


So the end result is that, as your project gets bigger and bigger, if you really have a lot of unit tests, the amount of investment you’ll have to make in maintaining those unit tests, keeping them up-to-date and keeping them passing, starts to become disproportional to the amount of benefit that you get out of them.


**Jeff: **I think that’s a great point. Although, I do think if you’re working on older code bases that don’t have a lot of churn, …


**Joel:** Yeah.


**Jeff:** To me it’s about churn. If you’re working on an old code base that isn’t going to have that much churn, and you want to change it where you *can’t* break anything, where if you break anything it’s *really really* bad, then it’s probably worth your time to go in and develop a *bunch* of unit tests. You’re building scaffolding around this grand old building, this classic old building that’s not going to change for another 200 years, so sure, build a bunch of scaffolding around the building.


**Joel:** Yeah. They work really for things like a compiler, where the design is not going to change because the language is fixed.


**Jeff:**That’s right.


**Joel:**I might do more black-box tests, sort of like unit tests but more from the perspective of “does this compile all code correctly,” with enormous numbers of tests, than just the internal, “does this *particular* function work in this *particular* way at all times.”


Last week I was listening to a [podcast on Hanselminutes](http://www.hanselminutes.com/default.aspx?showID=163), with Robert Martin talking about the [SOLID principles](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod). (That’s a real easy-to-Google term!) It’s object-oriented design, and they’re calling it agile design, which it really, really isn’t. It’s principles for how to design your classes, and how they should work. And, when I was listening to them, they all sounded to me like extremely bureaucratic programming that came from the mind of somebody that has not written a lot of code, frankly.


And here I am ranting against somebody that doesn’t have a chance to respond. But just to give you one example, a part of the SOLID principles was that if you write a class, that class has contracts with all the other classes that it interacts with, and those contracts should be expressed in interfaces [[PDF](http://www.objectmentor.com/resources/articles/isp.pdf)]. So you shouldn’t just interact with the class, because that class may change. If you have a particular class that you need to use, you should make a custom interface just for what *you’re* going to use in that class. That interface, then, never has to change. And the interface is the only thing that you have to #include.


Does that make sense? So, you’ve got some class, with 40 different little methods on it, and I’m only going to use six of them, so I should make an interface with those six things that I can use, and the class will implement that interface, and that’s my contract with the class, that those are the only six things I’m going to use.


People that say things like this have just never written a heck of a lot of code. Because what they’re doing is spending an *enormous *amount of time writing a lot of extra code, a lot of verbiage, a lot of files, and a million little classes that don’t do anything and thousands of little interface classes and a lot of *robustness* to make each of these classes individually armed to go out into the world alone and do things, and *you’re not going to need it*. You’re spending a lot of time in advance writing code that is just not going to be relevant, it’s not going to be important. It could, theoretically, protect you against things, but, how about waiting until those things happen before you protect yourself against them?


This seems to be where a lot of the Object Oriented Design community went, and if anybody has any strong feelings about this, call in and tell me what you think–tell me if I’m totally off track here–but it seems to me like a lot of the Object Oriented Design principles you’re hearing lately from people like Robert Martin and Kent Beck and so forth have gone off the deep end into architecture for architecture’s sake. It doesn’t seem like you could actually get any code written if you’re spending all your time writing 8,000,000 unit tests, and every single dinky little class that you need to split a URL into four parts becomes an engineering project worthy of making a bridge, where you spend six months defining 1000 little interfaces. They’ve just gone off the deep end, and I don’t think these people write very much code if they’re coming up with these principles, to be honest, it doesn’t even make sense.


**Jeff:** Well, there are places where that level of testing makes sense. If you’re working at Microsoft and you’re working on the .NET Framework…


**Joel:** Yeah.


**Jeff:** … you have a totally different set of obligations to your public …


**Joel:** Correct.


**Jeff:**… Your code’s going to be used millions and millions of times.


**Joel:** Yeah. In fact, if you’re making any kind of API, a plug in API, it is very important to separate things into interfaces and be very very contractual, and tightly engineered. Just like you want to put a lot of effort into your user interface, you also want to put a lot of effort into your API that people are calling… it’s just an interface, and you want it to be good and solid and robust. And that’s fine.


But this idea that *every single class* in your code, all these classes interacting with each other, should be *so tightly defined* …


Listening to this interview on Hanselminutes, there seemed to be an intense obsession with creating lots and lots of little classes that all did one particular thing…


One of the SOLID principles, and I’m totally butchering this, but, one of the principles was that you shouldn’t have two things in the same class that would be changed for a different reason [[PDF](http://www.objectmentor.com/resources/articles/srp.pdf)]. Like, you don’t want to have an Employee class, because it’s got his *name* which might get changed if he gets married, and it has his *salary*, which might get changed if he gets a raise. Those have to be two *separate* classes, because they get changed under different circumstances. And you wind up with millions of tiny little classes, like the EmployeeSalary class, and it’s just… (laughs) idiotic! You can’t build software that way! The way real software works is that you create these very imperfect things, and they work *great*. They really do. And then you have a little problem, and you go and you *fix* the little problem, because it’s *code*, and you have an *editor,* and you *edit* it. These classes are not going to go wander off flying in the universe all by themselves and need to work perfectly and unchanged until the end of time.


**Jeff:** Right. The longer I think about this, the less I care about code hygiene issues (laughs). Because the unit of measure that really matters to me is, how quickly you can respond to real business needs with your code. And by that I mean, how well are you serving the people that are using your code. To me that’s what it’s *all* about. Anything that gets in the way of you *fixing* your code or *improving* your code in a way that your *customers* can appreciate, is a negative. If that means using Ruby, or having lots of unit tests: whatever’s working for you: do that. But if it’s getting in the way, if it becomes friction, like, “I’d love to have this great new feature but I’d have to have 1000 unit tests,” that’s a negative.


**Joel:** Yeah. And the worst thing that happens is that you get people that just stop *thinking* about what they’re doing. “This is the principle, to always write unit tests, so I’m always going to write unit tests,” and then they’re just not thinking about how they’re spending their time, and they wind up wasting a lot of it.


**Jeff:** Yeah, it’s a balancing act. And I don’t want to come out and say I’m against [unit] testing, because I’m really not. Anything that improves quality is good. But there’s multiple axes you’re working on here; quality is just one axis. And I find, sadly, to be completely honest with everybody listening, quality really doesn’t matter that much, in the big scheme of things… There was this quote from Frank Zappa: “Nobody gives a crap if we’re great musicians.” And it really is true. The people that appreciate Frank Zappa’s music aren’t going, “that guitar was really off.” They’re hearing the whole song; they’re hearing the music, they’re not really worried whether your code has the correct object interfaces, or if it’s developed in a pure way, or written in Ruby or PHP… they don’t really care about that stuff. We do internally, but it’s important to balance that, I think, and I think that gets missed a lot, which is, maybe, the point you’re getting at.


**Joel:** Yeah.


**Jeff:** I think over time, more and more, I’ve become really lax on my thinking about this, because what matters is what you deliver to the customer, and how happy the customer is with what you’ve delivered. There’s many, many ways to get there.
