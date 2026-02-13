---
title: "The Process of Designing a Product"
date: 2000-05-09
url: https://www.joelonsoftware.com/2000/05/09/the-process-of-designing-a-product/
word_count: 2053
---


We’ve talked about the principles of good design, but principles only give you a way to evaluate and improve an existing design. But… how do you figure out what the dang design should be in the first place? Many people write big, functional outlines of all the features they thought up. Then they design each one, and hang it off of a menu item (or web page). When they’re done, the program (or web site) has all the functionality they wanted, but it doesn’t *flow* right. People sit down and they don’t know what it does, and they don’t know how to accomplish what they want.


Microsoft’s solution to this is something called Activity Based Planning. (As far as I can tell, this concept was invented by [Mike Conte](http://www.conte.org/) on the Excel team, who got bored with that and went on to a second career as a race car driver). The key insight is to figure out the *activity* that the user is doing, and focus on making it easy to accomplish that activity. This is best illustrated with an example.


You’ve decided to make a web site that lets people create greeting cards. Using a somewhat naïve approach, you might come up with a list of features like this:


> 1. Add text to card
> 2. Add picture to card
> 3. Get predesigned card from library
> 4. Send card:
>            a. Using email
>            b. By printing it out


For lack of any better way of thinking about the problem, this might lead itself to a typical Macintosh user interface, circa-1984: a program that starts out with a blank card, with menu items for adding text, pictures, loading cards from a library, and sending cards. And then what the user is going to have to do is sit down and browse through the menus, trying to figure out all the commands available, and then do their own synthesis of how to put these atomic commands together to create a card.


Now, activity based planning says that you need to come up with a list of activities that users might do. So, you talk to your potential users, and you come up with this “top three” list:

1. Birthday Greeting
Party Invitation
Anniversary Greeting


Now, instead of thinking about your program like a programmer (in terms of *what features you need to have to make a card*), you’re thinking about it like the user, in terms of, what activities is the user doing, specifically:

1. Sending a birthday card
Planning a party, and inviting people to it
Sending an anniversary card


Suddenly, all *kinds* of ideas will rush into your head. Instead of starting with a blank card, you might start with a menu like this:


> What do you want to do?  
> Send a birthday card
> Send an anniversary card
> Send a party invitation
> Start with a blank card


Suddenly users will find it *much* easier to get started with your program, without browsing around on the menus, since the program will virtually lead them through the steps to complete the activity. (There is a risk that if you didn’t pick the activities correctly, you will alienate or confuse users who might have been able to use your program, say, to send a Hanukah card, but don’t see that as a choice. So be careful in picking activities that blanket the majority of the market you want to target.)


Just looking at our list of three activities suggests some great features which you might want to add. For example, if you’re sending a birthday or anniversary card, you might want to be reminded next year to send a card to the same person… so you might add a checkbox that says “remind me next year”. And a party invitation needs a way to RSVP, so you might add a feature that lets you collect RSVPs from people electronically. Both of these feature ideas almost fell out of looking at the *activity* that users were performing instead of the *features* in the application.


This example is trivial; for any serious application, the rewards of activity based planning are even greater. When you’re designing a program from scratch, you already have a vision of what activities your users are going to be doing. Figuring out this vision is not hard at all, it takes almost no effort at all to do some brainstorming with coworkers, write down a list of potential activities, and then decide which ones you want to focus on. But forcing yourself to list these activities on paper will help your overall design enormously.


Activity based planning is even more important when you are working on version two of a product that people are already using. Here, it may be a matter of observing a sample of customers to see what they are using your program for.


In the days of Excel 1.0 through 4.0, most people at Microsoft thought that the most common user activity was doing financial *what-if* scenarios, where you do things like change the inflation rate and see how this affects your profitability.


When we were designing Excel 5.0, the first major release to use serious activity-based planning, we only had to watch about five customers using the product before we realized that an enormous number of people just use Excel to keep *lists*. They are not entering any formulas or doing any calculation at all! We hadn’t even considered this before. Keeping lists turned out to be far more popular than any other activity with Excel. And this led us to invent a whole *slew* of features that make it easier to keep lists: easier sorting, automatic data entry, the AutoFilter feature which helps you see a slice of your list, and multi-user features which let several people work on the same list at the same time while Excel automatically reconciles everything.


While Excel 5 was being designed, Lotus had shipped a “new paradigm” spreadsheet called Improv. According to the press releases, Improv was a whole new generation of spreadsheet, which was going to blow away everything that existed before it. For various strange reasons, Improv was first available on the NeXT, which certainly didn’t help its sales, but a lot of smart people believed that Improv would be to NeXT as VisiCalc was to the Apple II: it would be the *killer app* that made people go out and buy all new hardware just to run one program.


Of course, Improv is now a footnote in history. Search for it on the web, and the only links you’ll find are from very over-organized storeroom managers who have, for some reason, made a web site with an inventory of all the stuff they have collecting dust.


Why? Because in Improv, it was almost impossible to just make lists. The Improv designers thought that people were using spreadsheets to create complicated multi-dimensional financial models. Turns out, if they asked people, they would discover that making lists was so much more common than multi-dimensional financial models, and in Improv, making lists was a downright *chore,* if not impossible.


So activity based planning is helpful in the initial version of your application, where you have to make guesses about what people want to do, but it’s even more helpful when you’re planning the upgrade, because you understand what your customers are doing.


Another example, from the web, is the evolution of [deja.com](http://www.deja.com/), which started out as an huge, searchable index of Usenet called dejanews. The original interface basically had an edit box and said “search Usenet for *blah*,” and that was it. In 1999 a bit of activity based planning showed that one common user activity was doing research on a product or service, of the “which car should I buy” nature. Deja was completely reorganized, and today, it is more of a product opinion research service: the Usenet searching ability is almost completely hidden. This annoyed the small number of users who were using the site to search for whether their Matrox video card worked with Redhat Linux 5.1, but it delighted the much larger population of users who just wanted to buy the best digital camera.


The other great thing about activity based planning is that it lets you make a list of what features *not* to do. When you create *any* kind of software, the reality is that you will come up with three times as many features as you have time to do. And one of the best ways to decide which features get done, and which features get left out, is to evaluate *which features support the most important user activities*.


### **Imaginary Users.**


The very best UI designers in the industry all agree on one thing: you have to invent and describe some imaginary users before you can design your UI. You may remember back in the [introduction to this book](https://www.joelonsoftware.com/uibook/chapters/fog0000000057.html), I introduced an imaginary user Pete:


> Pete is an accountant for a technical publisher who has used Windows for six years at the office and a bit at home. He is fairly competent and technical. He installs his own software; he reads PC Magazine, and he has even programmed some simple Word macros to help the secretaries in his office send invoices. He’s getting a cable modem at home. Pete has never used a Macintosh. “They’re too expensive,” he’ll tell you. “You can get a 700 Mhz PC with 128 Meg RAM for the price of…” OK, Pete. We get it.


When you read this, you can almost *imagine* a user. I could also have invented quite another type of user:


> Patricia is an English professor who has written several well-received books of poetry. She has been using computers for word processing since 1980, although the only two programs she ever used are Nota Bene (an ancient academic word processor) and Microsoft Word. She doesn’t want to spend time learning the theory of how the computer works, and she tends to store all her documents in whatever directory they would go in if you didn’t know about directories.


Obviously, designing software for Pete is quite different from designing software for Patricia, who in turn is quite different from Mike, a 16 year old who runs Linux at home, talks on IRC for hours, and uses no “Micro$oft” software.


When you invent these users, thinking about whether your design is appropriate becomes much easier. For example, a lot of programmers tend to overestimate the ability of the typical user to figure things out. Whenever I write something about command line interfaces being hard to use, I get the inevitable email barrage saying that command line interfaces are ultra-powerful because you can do things like ‘gunzip foo.tar.gz | tar xvf -‘. But as soon as you have to think about getting Patricia to type “gunzip…” it becomes obvious that that kind of interface just isn’t going to serve her needs, ever. Thinking about a “real” person gives you the empathy you need to make a feature that serves that person’s need. (Of course, if you’re making Linux backup software for advanced sysadmins, you need to invent a character like “Frank” who refuses to touch Windows, which he only refers to as an “operating system” in quotation marks, uses his own personally modified version of tcsh, and runs X11 with four tiled xterms all day long. And about 11 xperfs.)


**To summarize**, designing good software takes about six steps:

1. Invent some users 

Figure out the important activities 

Figure out the *user model* — how the user will expect to accomplish those activities 

Sketch out the first draft of the design 

Iterate over your design again and again, making it easier and easier until it’s well within the capabilities of your imaginary users 

Watch real humans trying to use your software. Note the areas where people have trouble, which probably demonstrate areas where the program model isn’t matching the user model.


Good UI sells software, but it also *makes people happy*, because people are happy when they accomplish the task they wanted to accomplish. Which is why UI design is such a satisfying field to be in. Where else are you going to get a chance to make millions of people just a little bit happier?
