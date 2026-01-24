---
title: "Making Considerate Software"
date: 2006-03-26
url: https://blog.codinghorror.com/making-considerate-software/
slug: making-considerate-software
word_count: 1364
---

I’m currently re-reading the book About Face. I hadn’t revisited this book since I bought the original version way back in 1995. The update, which was published in 2003, is **a significant overhaul – and frankly much better than the original**. Adding the second author, Robert Reimann, was a smart move. Alan Cooper is a usability legend, but he can be bombastic and overbearing at times. Having another viewpoint in the book helps moderate and refine the message.


![](https://blog.codinghorror.com/content/images/2025/09/about-face-the-essentials-of-interaction-design.jpg)


(Since this was written, [About Face 3.0 was released](https://blog.codinghorror.com/the-three-faces-of-about-face/), with yet another author added to the mix, and the [fourth final version as well](https://www.amazon.com/About-Face-Essentials-Interaction-Design/dp/1118766571).)


One part of About Face that I found particularly compelling was the section on considerate software:

1. Considerate software **takes an interest**
To the programmer writing the program, it’s a just-in-time information world, so when the program needs some tidbit of information, it demands that the user provide it. The program then discards that tidbit, assuming it can merely ask for it again if necessary. Not only is the program better suited to remembering than the human, the program is also inconsiderate when, acting as a supposedly helpful tool, it forgets.
2. Considerate software **is deferential**
Inconsiderate software supervises and passes judgment on human actions. Software is within its rights to express its opinion that we are making a mistake, but it is being presumptuous when it judges our actions. Software can suggest that we not not Submit our entry until we’ve typed in our telephone number. It should also explain the consequences, but if we wish to Submit without the number, we expect the software to do as it is told.
3. Considerate software **is forthcoming**
Most software doesn’t attempt to provide related information. Instead, it narrowly answers the precise question we ask it, and it is not forthcoming about other information even if it is clearly related to our goals. When we tell our word processor to print a document, it doesn’t tell us when the paper is low, or when forty other documents are queued up in front of us, or when another nearby printer is free. A helpful human would.
4. Considerate software **uses common sense**
You can easily find menus offering simple, harmless functions adjacent to irreversible ejector-seat-lever expert functions. It’s like seating you at a dining table right next to an open grill. Horror stories abound of customers offended by computer systems that repeatedly sent them checks for $0.00 or bills for $957,142,039.58. One would think that the system might alert a human in the accounts receivable or payable departments when an event like this happens.
5. Considerate software **anticipates needs**
A web browser spends most of its time idling while we peruse web pages. It could easily anticipate needs and prepare for them while we are reading. It could use that idle time to preload all the visible links. Chances are good that we will soon ask the browser to examine one or more of those links. It is easy to abort an unwanted request, but it is always time-consuming to wait for a request to be filled.
6. Considerate software **is conscientious**
If we rely on a word processor to draft a new MicroBlitz Contract and then try to [save it in the same folder as an existing, but older, MicroBlitz Contract], the program offers the choice of either overwriting and destroying the old contract or not saving it at all. The program not only isn’t as capable as [a human assistant who saw the name conflict and appropriately renamed the contracts], it isn’t even as capable as [a human assistant who put the two contracts in the same folder]. It is stupider than a complete idiot. The software is dumb enough to make an assumption that because they have the same name, I meant to throw the old one away.
7. Considerate software **doesn’t burden you with its personal problems**
Software whines at us with error messages, interrupts us with confirmation dialog boxes, and brags to us with unnecessary notifications. We aren’t interested in the program’s crisis of confidence about whether or not to purge its recycle bin. We don’t want to hear its whining about not being sure where to put a file on disk. We don’t need to see information about the computer’s data transfer rates and its loading sequence, any more than we need information about the customer service agent’s unhappy love affair.
8. Considerate software **keeps you informed**
We don’t want our local bartender to grouse about his recent divorce, but we appreciate it when he posts his prices in plain sight and when he writes what time the pregame party begins on his chalkboard, along with who’s playing and the current Vegas spread. Nobody is interrupting us to tell us this information: it’s there in plain sight whenever we need it.
9. Considerate software **is perceptive**
Software should watch our preferences and remember them without being explicitly asked to do so. If we always maximize an application to use the entire screen, the application should get the idea after a few sessions and always launch in that configuration. The same goes for placement of palettes, default tools, frequently used templates, and other useful settings.
10. Considerate software **is self-confident**
Are you sure? Are you really sure? Are you really, *really *sure?
11. Considerate software **doesn’t ask a lot of questions**
Choices can be offered in different ways. They can be offered in the way that we window shop. We peer in the window at our leisure, considering, choosing, or ignoring the goods offered to us – no questions asked. Alternatively, questions can be forced on us like an interrogation by a customs official at a border crossing: “Do you have anything to declare?” Software should never put users through this kind of intimidation.
12. Considerate software **takes responsibility**
Most programs are filled with data and settings. When they crash, that information is normally discarded; the user is left holding the bag. Let’s say you are downloading your email from a server, when your email program runs out of memory at some procedure buried deep in the internals of the program. The program, like most desktop software, issues a message that says, in effect, “You are completely hosed,” and terminates immediately after you click OK. You restart the program, or sometimes the whole computer, only to find that the program lost your email and, when you interrogate the server, you find that it has also erased your mail because the mail was already handed over to your program. This is not what we should expect of good software.
13. Considerate software **knows when to bend the rules**
In most computerized systems, there are only two states: non-existence or full-compliance. No intermediate states are recognized or accepted. In any manual system, there is an important but paradoxical state – unspoken, undocumented, but widely relied upon – of suspense, wherein a transaction can be accepted although still not fully processed. The human operator creates that state in his head or on his desk or in his back pocket. For example, a digital system needs both customer and order information before it can post an invoice. Whereas the human clerk can go ahead and post an order in advance of detailed customer information, the computerized system will reject the transaction, unwilling to allow the invoice to be entered without it.

The characteristic of manual systems that let humans perform actions out of sequence or before prerequisites are satisfied is called fudgeability. It is one of the first casualties when systems are computerized, and its absence is a key contributor to the inhumanity of digital systems. It is a natural result of the implementation model. The programmers don’t see any reason to create intermediate states because the computer has no need for them. Yet there are strong human needs to be able to bend the system slightly.


Lots of food for thought there. So many applications I use fail even the most basic criteria on this list. I wish I could get every working developer to read [Don’t Make Me Think](http://www.amazon.com/exec/obidos/ASIN/0321344758) and [About Face](http://www.amazon.com/exec/obidos/ASIN/0470084111).** **

[usability](https://blog.codinghorror.com/tag/usability/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[software design](https://blog.codinghorror.com/tag/software-design/)
