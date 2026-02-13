---
title: "Usability Testing with Morae"
date: 2005-07-30
url: https://www.joelonsoftware.com/2005/07/30/usability-testing-with-morae/
word_count: 845
---


The last time I participated in formal usability testing was at a fancy lab in Colorado, custom built for the purpose at a cost of around $100,000. It was basically a television studio, complete with one-way glass, lots of special video gear, and a giant video console that would have been adequate to broadcast the Superbowl. To do usability testing for Juno, a group of us flew out to Colorado, rented cars, stayed in a hotel, ate at expensive restaurants, and generally consumed massive amounts of money so we could watch people try to sign up for our online service, and, generally, succeed.


At the other extreme, I’ve long been an advocate of hallway usability tests and paper prototypes, which often find some of the biggest usability problems long before they occur for about fifty cents.


Now there’s a middle ground. My friends over at TechSmith in Okemos, Michigan recently released a software product called [Morae](http://www.techsmith.com/products/morae/default.asp) which lets you use cheap webcams to set up a complete usability lab in your office without fancy equipment or one-way glass. I asked them if they would be willing to usability test their own product by running a usability test in the Fog Creek office for [our new remote assistance service](http://www.copilot.com/), and they graciously agreed.


Here’s how Morae works. You set up your usability testing subject in front of a computer with a webcam and a microphone:


Then any number of people can watch the subject from their own computers:


Here Tyler is watching two screens: one is showing the helper and the other is showing the person being helped. He can see their screens, hear everything they say, and see video of the subject in the corner. We happen to have windows between the offices at Fog Creek so he can actually see the helper through his window. Let’s see if I can zoom in on Tyler’s screens:


In [my book on UI design](https://www.joelonsoftware.com/navLinks/BuytheBooks.html), I wrote about a common problem with usability tests:


> In most usability tests, you prepare a list of instructions for the user. For example, if you were usability testing an Internet access provider, you might have an instruction to “sign up for the service.” (I actually did this very usability test, several times, in my career.)
> So far so good. The first user comes in, sits down, starts signing up for the service, and gets to the screen asking them how they want to pay. The user looks at me helplessly. “Do I gotta pay for this myself?”
> “Oh wait,” you interrupt. “Here, use this fake credit card number.”
> The sign up procedure then asks them if they would like to use a regular modem, a cable modem, or a DSL line.
> “What do I put here?” asks the user. Possibly because they don’t know the answer, but possibly because they know the answer for their computer, but they’re not using their computer, they’re using your computer, which they’ve never seen before, in a usability lab, where they’ve never been before.


To work around this problem, usability testers have started trying to do field testing. Instead of giving the subject tasks to do in a highly contrived environment, you conspire to watch the subject doing their own work at their own desk while you hide in a nearby shrub and spy on them. Morae, by the way, would be perfect for that. This method is most useful when you already have a version *n* of your product and you’re trying to figure out how to improve version *n+1*.


The usability test worked great. Our usability test was a little bit uncommon in that we had two subjects, since Fog Creek Copilot involves a helper and a helpee, and Morae only let us hear one subject at a time from one computer. To work around this we just set up two computers with the Morae Remote Viewer so we could get the sound from both subjects.


So far this morning we’ve run two usability test sessions, with great results: we’ve already realized that 2 out of 2 helpers were confused about how to get reconnected, since the Fog Creek Copilot helper application deletes itself when you’re done with it. This is a classic example of the user model not conforming to the program model … most programs don’t delete themselves! … which is the source of virtually every usability problem. From the very first chapter of *UI for Programmers*:


> StartFragment The cardinal axiom of all user interface design:
> **A user interface is well-designed when the program behaves exactly how the user thought it would.**


I should have known this. The program design violated a principle I wrote myself in big bold print in my own book: it didn’t do what you expected. The great thing about usability tests is with a day of usability testing and handful of subjects, even if you’re as senile as I am, you can find the biggest areas where you didn’t realize where the program’s behavior diverges from the user’s expected behavior.
