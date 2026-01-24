---
title: "New Programming Jargon"
date: 2012-07-20
url: https://blog.codinghorror.com/new-programming-jargon/
slug: new-programming-jargon
word_count: 2286
---

Stack Overflow – like most online communities I’ve studied – naturally trends toward increased strictness over time. It’s primarily a defense mechanism, an immune system of the sort a child develops after first entering school or daycare and being exposed to the wide, wide world of everyday sneezes and coughs with the occasional [meningitis outbreak](http://www.cdc.gov/mmwr/preview/mmwrhtml/mm6113a1.htm). It isn’t always a pleasant process, but it is, unfortunately, a necessary one if you want to survive.


Consider this question from two years ago:


> **New programming jargon you coined? **
> What programming terms have you coined that have taken off in your own circles (i.e. have heard others repeat it)? It might be within your own team, workplace or garnered greater popularity on the Internet.
> Write your programming term, word or phrase in bold text followed by an explanation, citation and/or usage example so we can use it in appropriate context.
> Don’t repeat common jargon already ingrained in the programming culture like: kludge, automagically, cruft, etc. (unless you coined it).
> This question serves in the spirit of communication among programmers through sharing of terminology with each other, to benefit us by its propagation within our own teams and environments.


Is this even a *question*, really? How many answers does it have?


**Three hundred and eighty six!**


A question that invites 386 different “answers” isn’t a question at all. It’s an opinion survey, a poll, a List of X. I suppose you could argue that reading through all those responses would teach you *something* about programming, but it was pretty clear that the bulk of the responses were far more about laughs and GTKY (Getting to Know You) than learning. That’s why it was eventually deleted by experienced Stack Overflow community members. Although it is somewhat borderline in terms of learning, and I didn’t *personally* vote to delete it, I tend to agree that it was correctly deleted. Though [opinions vary](http://meta.stackoverflow.com/questions/122164/can-we-un-delete-new-programming-jargon-you-coined).


I won’t bore you with the entire history, our [so-called “war on fun,”](http://blog.stackoverflow.com/2010/01/stack-overflow-where-we-hate-fun/) and the [trouble with popularity](http://blog.stackoverflow.com/2012/01/the-trouble-with-popularity/). Ultimately, **Stack Overflow is a college, *not* a frat house**. All the content on the site must exist to serve the mission of learning over entertainment – even if that means making difficult calls about removing some questions and answers that fail to meet those goals, plus or minus 10 percent.


In terms of programmer culture, though, there is precedent in the form of [The Jargon File](http://www.catb.org/jargon/). Unfortunately, we don’t have a good designated place for deleted “too fun” questions to live, but all Stack Exchange content is licensed under Creative Commons in perpetuity. Which means, with proper attribution, we can give it a permanent home on our own blogs. So I did. I’ve collected **the top 30 Stack Overflow New Programming Jargon** entries below, as judged by the Stack Overflow community. Enjoy.*


### 1. Yoda Conditions


[zneak](http://stackoverflow.com/users/251153/zneak)


![](https://blog.codinghorror.com/content/images/2025/03/image-40.png)


Using `if(constant == variable)` instead of `if(variable == constant)`, like `if(4 == foo)`. Because it’s like saying “if blue is the sky” or “if tall is the man.”


### 2. Pokémon Exception Handling


[woot4moo](http://stackoverflow.com/users/205426/woot4moo)


![](https://blog.codinghorror.com/content/images/2025/05/image-552.png)


For when you just Gotta Catch ’Em All.


```
try {
}
catch (Exception ex) {
// Gotcha!
}

```


### 3. Egyptian Brackets


[computronium](http://stackoverflow.com/users/215403/computronium)


![](https://blog.codinghorror.com/content/images/2025/05/image-553.png)


You know the style of brackets where the opening brace goes on the end of the current line, e.g. this?


```
if (a == b) {
printf("hello");
}

```


We used to refer to this style of brackets as “Egyptian brackets.” Why? Compare the position of the brackets with the hands in the picture. (This style of brackets is used in Kernighan and Ritchie’s book, [The C Programming Language](http://www.amazon.com/dp/0131103628/), so it’s known by many as K&R style.)


### 4. Smug Report


[aaronaught](http://stackoverflow.com/users/38360/aaronaught)


![](https://blog.codinghorror.com/content/images/2025/05/image-554.png)


A bug submitted by a user who thinks he knows a lot more about the system’s design than he really does. Filled with irrelevant technical details and one or more suggestions (always wrong) about what he thinks is causing the problem and how we should fix it.


Also related to Drug Report (a report so utterly incomprehensible that whoever submitted it must have been smoking crack.), Chug Report (where the submitter is thought to have had one too many), and Shrug Report (a bug report with no error message or repro steps and only a vague description of the problem. Usually contains the phrase “doesn’t work.”)


### 5. A Duck


[kyoryu](http://stackoverflow.com/users/129175/kyoryu)


![](https://blog.codinghorror.com/content/images/2025/05/image-555.png)


A feature added for no other reason than to draw management attention and be removed, thus avoiding unnecessary changes in other aspects of the product.


I don’t know if I actually invented this term or not, but I am certainly not the originator of the story that spawned it.


This started as a piece of Interplay corporate lore. It was well known that producers (a game industry position, roughly equivalent to PMs) had to make a change to everything that was done. The assumption was that subconsciously they felt that if they didn’t, they weren’t adding value.


The artist working on the queen animations for Battle Chess was aware of this tendency, and came up with an innovative solution. He did the animations for the queen the way that he felt would be best, with one addition: he gave the queen a pet duck. He animated this duck through all of the queen’s animations, had it flapping around the corners. He also took great care to make sure that it never overlapped the “actual” animation.


Eventually, it came time for the producer to review the animation set for the queen. The producer sat down and watched all of the animations. When they were done, he turned to the artist and said, *“that looks great. Just one thing - get rid of the duck.”*


### 6. Refuctoring


[Jason Gorman](http://www.codemanship.co.uk/)


![](https://blog.codinghorror.com/content/images/2025/05/image-556.png)


The process of taking a well-designed piece of code and, through a series of small, reversible changes, making it completely unmaintainable by anyone except yourself.


### 7. Stringly Typed


[Mark Simpson](http://stackoverflow.com/users/83891/mark-simpson)


![](https://blog.codinghorror.com/content/images/2025/05/image-557.png)


A riff on strongly typed. Used to describe an implementation that needlessly relies on strings when programmer & refactor friendly options are available.


For example:

- Method parameters that take strings when other more appropriate types should be used.
- On the occasion that a string is required in a method call (e.g. network service), the string is then passed and used throughout the rest of the call graph without first converting it to a more suitable internal representation (e.g. parse it and create an enum, then you have strong typing throughout the rest of your codebase).
- Message passing without using typed messages etc.


Excessively stringly typed code is usually a pain to understand and detonates at runtime with errors that the compiler would normally find.


### 8. Heisenbug


unknown


![](https://blog.codinghorror.com/content/images/2025/03/image-47.png)


A computer bug that disappears or alters its characteristics when an attempt is made to study it. ([Wikipedia](http://en.wikipedia.org/wiki/Unusual_software_bug#Heisenbug))


### 9. Doctype Decoration


[Zurahn](http://stackoverflow.com/users/23666/zurahn)


![](https://blog.codinghorror.com/content/images/2025/05/image-558.png)


When web designers add a doctype declaration but don’t bother to write valid markup.


```
&lt;!DOCTYPE html&gt;
&lt;BLINK&gt;Now on sale!&lt;/BLINK&gt;

```


### 10. Jimmy


[Gord](http://stackoverflow.com/users/12560/gord)


![](https://blog.codinghorror.com/content/images/2025/05/image-559.png)


A generalized name for the clueless/new developer.


Found as we were developing a framework component that required minimal knowledge of how it worked for the other developers. We would always phrase our questions as: *“What if Jimmy forgets to update the attribute?”*


This led to the term: “Jimmy-proof” when referring to well designed framework code.


### 11. Higgs-Bugson


[gingerbreadboy](http://stackoverflow.com/users/231999/gingerbreadboy)


![](https://blog.codinghorror.com/content/images/2025/05/image-560.png)


A hypothetical bug predicted to exist based on a small number of possibly related event log entries and vague anecdotal reports from users, but it is difficult (if not impossible) to reproduce on a dev machine because you don’t really know if it’s there, and if it is there what is causing it. (see [Higgs-Boson](http://en.wikipedia.org/wiki/Higgs_boson))


### 12. Nopping


[Stanislav](http://stackoverflow.com/users/220587/stanislav)


![](https://blog.codinghorror.com/content/images/2025/05/image-561.png)


I’m writing a sci-fi novel from the POV of an AI, and their internal language has a lot of programming jargon in it. One of the more generalizable terms is “nopping,” which comes from assembler NOP for no-operation. It’s similar to ‘nap,’ but doesn’t imply sleep, just zoning out. *“Stanislav sat watching the screensaver and nopped for a while.”*


### 13. Unicorny


[Yehuda Katz](http://stackoverflow.com/users/122162/yehuda-katz)


![](https://blog.codinghorror.com/content/images/2025/05/image-562.png)


An adjective to describe a feature that’s so early in the planning stages that it might as well be imaginary. We cribbed this one from Yehuda Katz, who used it in his closing keynote at last year’s Windy City Rails to describe some of Rails’ upcoming features.


### 14. Baklava Code


[John D. Cook](http://stackoverflow.com/users/25188/john-d-cook)


![](https://blog.codinghorror.com/content/images/2025/05/image-563.png)


Code with [too many layers](http://www.johndcook.com/blog/2009/07/27/baklav-code/).


Baklava is a delicious pastry made with many paper-thin layers of phyllo dough. While thin layers are fine for a pastry, thin software layers don’t add much value, especially when you have many such layers piled on each other. Each layer has to be pushed onto your mental stack as you dive into the code. Furthermore, the layers of phyllo dough are permeable, allowing the honey to soak through. But software abstractions are best when they don’t leak. When you pile layer on top of layer in software, the layers are bound to leak.


### 15. Hindenbug


[Mike Robinson](http://stackoverflow.com/users/43687/mike-robinson)


![](https://blog.codinghorror.com/content/images/2025/05/image-564.png)


A catastrophic data destroying bug. *“Oh the humanity!”*


Also related to Counterbug (a bug you present when presented with a bug caused by the person presenting the bug) and Bloombug (a bug that accidentally generates money).


### 16. Fear Driven Development


[Arnis L.](http://stackoverflow.com/users/82062/arnis-l)


![](https://blog.codinghorror.com/content/images/2025/05/image-565.png)


When project management adds more pressure (fires someone, moves deadlines forward, subtracts resources from the project, etc).


### 17. Hydra Code


[Nick Dandoulakis](http://stackoverflow.com/users/108130/nick-dandoulakis)


![](https://blog.codinghorror.com/content/images/2025/05/image-566.png)


Code that cannot be fixed. Like the [Hydra of legend](http://en.wikipedia.org/wiki/Lernaean_Hydra), every new fix introduces two new bugs. It should be rewritten.


### 18. Common Law Feature


anonymous


![](https://blog.codinghorror.com/content/images/2025/05/image-567.png)


A bug in the application that has existed so long that it is now part of the expected functionality, and user support is required to actually fix it.


### 19. Loch Ness Monster Bug


[russau](http://stackoverflow.com/users/109102/russau)


![](https://blog.codinghorror.com/content/images/2025/05/image-568.png)


I’ve started Loch Ness Monster bug for anything not reproducible / only sighted by one person. I’m hearing a lot of people in the office say it now. (Possible alternates: Bugfoot, Nessiebug.)


### 20. Ninja Comments


[schar](http://stackoverflow.com/users/48928/schar)


![](https://blog.codinghorror.com/content/images/2025/05/image-569.png)


Also known as *invisible comments*, *secret comments*, or *no comments*.


### 21. Smurf Naming Convention


[sal](http://stackoverflow.com/users/13753/sal)


![](https://blog.codinghorror.com/content/images/2025/05/image-570.png)


When almost every class has the same prefix. IE, when a user clicks on the button, a `SmurfAccountView` passes a `SmurfAccountDTO` to the `SmurfAccountController`. The `SmurfID` is used to fetch a `SmurfOrderHistory` which is passed to the `SmurfHistoryMatch` before forwarding to either `SmurfHistoryReviewView` or `SmurfHistoryReportingView`. If a `SmurfErrorEvent` occurs it is logged by `SmurfErrorLogger` to `${app}/smurf/log/smurf/smurflog.log`


### 22. Protoduction


[Chris Pebble](http://stackoverflow.com/users/7264/chris-pebble)


![](https://blog.codinghorror.com/content/images/2025/05/image-571.png)


A prototype that ends up in production. Heard this from a tech at the Fermi lab. He said he didn’t coin the term but had heard it used a number of times at Fermi.


### 23. Rubber Ducking


[wesgarrison](http://stackoverflow.com/users/62140/wesgarrison)


![](https://blog.codinghorror.com/content/images/2025/05/image-572.png)


Sometimes, you just have to talk a problem out. I used to go to my boss and talk about something and he’d listen and then I’d just answer my own question and walk out without him saying a thing. I read about someone that put a rubber duck on their monitor so they could talk to it, so rubberducking is talking your way through a problem.


### 24. Banana Banana Banana


[juliet](http://stackoverflow.com/users/40516/juliet)


![](https://blog.codinghorror.com/content/images/2025/05/image-573.png)


Placeholder text indicating that documentation is in progress or yet to be completed. Mostly used because FxCop complains when a public function lacks documentation.


```
/// <summary>
/// banana banana banana
/// </summary>
public CustomerValidationResponse Validate()

```


Other food-related jargon: Programmer Fuel (Mountain Dew, coffee, Mate, anything which gets you well-caffeinated), Hot Potato (Http and Https respectively. Same number of syllables, but more fun to say), Cake (Marty’s noob cake broke the build), Chunky Salsa (based on the [chunky salsa rule](http://tvtropes.org/pmwiki/pmwiki.php/Main/ChunkySalsaRule), a single critical error or bug that renders an entire system unusable, especially in a production environment).


### 25. Bicrement


[evilteach](http://stackoverflow.com/users/7734/evilteach)


![](https://blog.codinghorror.com/content/images/2025/03/image-64.png)


Adding 2 to a variable.


### 26. Reality 101 Failure


[Loren Pechtel](http://stackoverflow.com/users/10659/loren-pechtel)


![](https://blog.codinghorror.com/content/images/2025/05/image-574.png)


The program (or more likely feature of a program) does exactly what was asked for but when it’s deployed it turns out that the problem was misunderstood and it’s basically useless.


### 27. Mad Girlfriend Bug


[Jeduan Cornejo](http://stackoverflow.com/users/33560/jeduan-cornejo)


![](https://blog.codinghorror.com/content/images/2025/05/image-575.png)


When you see something strange happening, but the software is telling you everything is fine.


### 28. Megamoth


[zolomon](http://stackoverflow.com/users/182153/zolomon)


![](https://blog.codinghorror.com/content/images/2025/05/image-576.png)


Stands for MEGA MOnolithic meTHod. Often contained inside a [God Object](http://en.wikipedia.org/wiki/God_object), and usually stretches over two screens in height. Megamoths of greater size than 2k LOC have been sighted. Beware of the MEGAMOTH!


### 29. Hooker Code


[NullPointerException](http://stackoverflow.com/users/60794/nullpointerexception)


![](https://blog.codinghorror.com/content/images/2025/05/image-577.png)


Code that is problematic and causes application instability (application “goes down” often). *“Did the site go down again? Yeah, Jim must still have some hooker code in there.”*


### 30. Jenga Code


[sumit](http://stackoverflow.com/users/16123/sumit)


![](https://blog.codinghorror.com/content/images/2025/05/image-578.png)


When the whole thing collapses after you alter a block of code.


This is just the top 30, what I consider to be the most likely candidates for *actual* new programming jargon based on community upvotes, not just “funny thing that another programmer typed on a webpage and I felt compelled to upvote for hilarity.” Because that would be *Reddit*. If you’re itching to see even more, there are plenty more answers to read – three hundred and fifty six more to be precise. Longtime Stack Overflow user Greg Hewgill maintained an archive of old deleted Stack Overflow questions, but this one hasn’t quite made it in there yet. In the meantime, try [Stack Printer](http://www.stackprinter.com/export?question=2349378&service=stackoverflow), or if you have the requisite 10k rep on Stack Overflow, you can view the full soft-deleted question on the site.


*But don’t enjoy it *too* much. We will be watching you.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
