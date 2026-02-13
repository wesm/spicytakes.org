---
title: "The Duct Tape Programmer"
date: 2009-09-23
url: https://www.joelonsoftware.com/2009/09/23/the-duct-tape-programmer/
word_count: 1260
---


Jamie Zawinski is what I would call a duct-tape programmer. And I say that with a great deal of respect. He is the kind of programmer who is hard at work building the future, and making useful things so that people can do stuff. He is the guy you want on your team building go-carts, because he has two favorite tools: duct tape and WD-40. And he will wield them elegantly even as your go-cart is careening down the hill at a mile a minute. This will happen while other programmers are still at the starting line arguing over whether to use titanium or some kind of space-age composite material that Boeing is using in the 787 Dreamliner.


When you are done, you might have a messy go-cart, but it’ll sure as hell fly.


I just read an interview with Jamie in the book [Coders at Work](http://www.amazon.com/gp/product/1430219483?ie=UTF8&tag=joelonsoftware&linkCode=as2&camp=1789&creative=390957&creativeASIN=1430219483), by Peter Seibel. Go buy it now. It’s a terrific set of interviews with some great programmers, including Peter Norvig, Guy Steele, and Donald Knuth. This book is so interesting I did 60 minutes on the treadmill yesterday instead of the usual 30 because I couldn’t stop reading. Like I said, go buy it.


Go! I’ll wait.


Here is why I like duct tape programmers. Sometimes, you’re on a team, and you’re busy banging out the code, and somebody comes up to your desk, coffee mug in hand, and starts rattling on about how if you use multi-threaded COM apartments, your app will be 34% sparklier, and it’s not even that hard, because he’s written a bunch of templates, and all you have to do is multiply-inherit from 17 of his templates, each taking an average of 4 arguments, and you barely even have to write the body of the function. It’s just a gigantic list of multiple-inheritance from different classes and hey, presto, multi-apartment threaded COM. And your eyes are swimming, and you have no friggin’ idea what this frigtard is talking about, but he just won’t go away, and even if he *does* go away, he’s just going back into his office to write more of his clever classes constructed entirely from multiple inheritance from templates, without a single implementation body at all, and it’s going to crash like crazy and *you’re* going to get paged at night to come in and try to figure it out because *he’ll* be at some goddamn “Design Patterns” meetup.


And the duct-tape programmer is not afraid to say, “multiple inheritance sucks. Stop it. Just stop.”


You see, everybody else is too afraid of looking stupid because they just can’t keep enough facts in their head at once to make multiple inheritance, or templates, or COM, or multithreading, or any of that stuff work. So they sheepishly go along with whatever faddish programming craziness has come down from the architecture astronauts who speak at conferences and write books and articles and are so much smarter than us that they don’t realize that the stuff that they’re promoting is too hard for us.


Here’s what Zawinski says about Netscape: “It was decisions like not using C++ and not using threads that made us ship the product on time.”


Later, he wrote an email client at Netscape, but the team that was responsible for actually displaying the message never shipped their component. “There was just this big blank rectangle in the middle of the window where we could only display plain text. They were being extremely academic about their project. They were trying to approach it from the DOM/DTD side of things. ‘Oh, well, what we need to do is add another abstraction layer here, and have a delegate for this delegate for this delegate. And eventually a character will show up on the screen.’”


Peter asked Zawinski, “Overengineering seems to be a pet peeve of yours.”


“Yeah,” he says, “At the end of the day, ship the fucking thing! It’s great to rewrite your code and make it cleaner and by the third time it’ll actually be pretty. But that’s not the point—you’re not here to write code; you’re here to ship products.”


My hero.


Zawinski didn’t do many unit tests. They “sound great in principle. Given a leisurely development pace, that’s certainly the way to go. But when you’re looking at, ‘We’ve got to go from zero to done in six weeks,’ well, I can’t do that unless I cut something out. And what I’m going to cut out is the stuff that’s not absolutely critical. And unit tests are not critical. If there’s no unit test the customer isn’t going to complain about that.”


Remember, before you freak out, that Zawinski was at Netscape when they were changing the world. They thought that they only had a few months before someone else came along and ate their lunch. A lot of important code is like that.


Duct tape programmers are pragmatic. Zawinski popularized Richard Gabriel’s precept of [Worse is Better](http://www.jwz.org/doc/worse-is-better.html). A 50%-good solution that people actually have solves more problems and survives longer than a 99% solution that nobody has because it’s in your lab where you’re endlessly polishing the damn thing. Shipping is a feature. A really important feature. Your product must have it.


One principle duct tape programmers understand well is that any kind of coding technique that’s even *slightly* complicated is going to doom your project. Duct tape programmers tend to avoid C++, templates, multiple inheritance, multithreading, COM, CORBA, and a host of other technologies that are all totally reasonable, when you think long and hard about them, but are, honestly, just a little bit too hard for the human brain.


Sure, there’s nothing *officially *wrong with trying to write multithreaded code in C++ on Windows using COM. But it’s prone to disastrous bugs, the kind of bugs that only happen under very specific timing scenarios, because our brains are not, honestly, good enough to write this kind of code. Mediocre programmers are, frankly, defensive about this, and they don’t want to admit that they’re not able to write this super-complicated code, so they let the bullies on their team plow away with some godforsaken template architecture in C++ because otherwise they’d have to admit that they just don’t feel smart enough to use what would otherwise be a perfectly good programming technique FOR SPOCK. Duct tape programmers don’t give a shit what you think about them. They stick to simple basic and easy to use tools and use the extra brainpower that these tools leave them to write more useful features for their customers.


One thing you have to be careful about, though, is that duct tape programmers are the software world equivalent of pretty boys… those breathtakingly good-looking young men who can roll out of bed, without shaving, without combing their hair, and without brushing their teeth, and get on the subway in yesterday’s dirty clothes and look beautiful, because that’s who they are. You, my friend, cannot go out in public without combing your hair. It will frighten the children. Because you’re just not that pretty. Duct tape programmers have to have a lot of talent to pull off this shtick. They have to be good enough programmers to ship code, and we’ll forgive them if they never write a unit test, or if they xor the “next” and “prev” pointers of their linked list into a single DWORD to save 32 bits, because they’re pretty enough, and smart enough, to pull it off.


Did you buy [Coders at Work](http://www.amazon.com/gp/product/1430219483?ie=UTF8&tag=joelonsoftware&linkCode=as2&camp=1789&creative=390957&creativeASIN=1430219483) yet? Go! This was just the *first chapter!*
