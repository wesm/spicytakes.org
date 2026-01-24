---
title: "Automated Continuous Integration and the BetaBrite LED Sign"
date: 2005-03-13
url: https://blog.codinghorror.com/automated-continuous-integration-and-the-betabrite-led-sign/
slug: automated-continuous-integration-and-the-betabrite-led-sign
word_count: 802
---

In the spirit of [Java Lava Lamp build monitoring](http://www.artima.com/weblogs/viewpost.jsp?thread=67492):


> *A few months ago, on April 1 2004 to be precise, I posted *[*an article on eXtreme Feedback*](https://web.archive.org/web/20060222091435/http://www.developertesting.com/archives/month200404/20040401-eXtremeFeedbackForSoftwareDevelopment.html)*.
> The article was on a relatively serious subject: “How do you get your team to pay attention to the software/project status and metrics that you care about?”, but one of my solutions for getting the team to pay attention was to “invent” and implement eXtreme Feedback Devices (XFDs) that would be very visible, fun, and hard to ignore.
> One of these XFDs consists of a pair of Lava lamps (one green and one red) remotely connected to our build and test system in such a way that **a successful build (all tests pass) turns on the green lava lamp, and a failed build (or failed tests) turns on the red one**.
> The original Java Lava Lamps have been glowing red and green for the past several months in our offices, and have achieved something of a cult status. They are included in Mike Clark’s excellent book, *[*Pragmatic Project Automation*](http://www.amazon.com/exec/obidos/ASIN/0974514039/002-1437771-2723220)*, and have recently received *[*a fair amount of buzz*](http://developers.slashdot.org/developers/04/08/26/1550255.shtml)* on Slashdot.
> The interesting thing, for me, is that something that I started as something of a joke (it was April 1st after all) actually turned out to be a very useful tool in more ways than one. Sure, I could go to our CruiseControl page to see if they build is broken, or set-up email alerts, but keeping track of the lamps (which are centrally located in our development area) is easier, faster, and gives me an ongoing view into the current status and ebb-and-flow of our build and test cycles.*


And Michael Swanson’s [Automated Continuous Integration and the Ambient Orb](https://web.archive.org/web/20051222075206/http://blogs.msdn.com/mswanson/articles/169058.aspx):


> *So I had this idea that we could configure an *[*Ambient Orb*](https://web.archive.org/web/20050404003753/http://www.ambientdevices.com/cat/orb/orborder.html)* to reflect the current status of our NxOpinion continuous integration build. **A slowly pulsing green would mean that the build is currently okay, and a quickly pulsing red would indicate a build failure. I planned to put the Orb in the middle of our project team so that everyone would be aware of the build status.** I hoped that by raising its visibility, everyone on the project team (including the customer) would be more aware of the project “health.”
> Now, when the build breaks and the Orb pulses red, it’s like a fire alarm around here. The first question out of everyone’s mouth is “who broke it?” After appropriate developer guilt has been piled on by the development team (all in good fun, of course), it’s usually a relatively trivial matter to discover and fix the problem. Because we continuously integrate our code and the automated build potentially runs every 15 minutes, determining what caused the failure is as simple as looking at what has been checked-in since the last successful build. Fortunately, CruiseControl.NET includes this information (along with check-in comments) in its e-mail and web page summaries.
> To-date, our solutions contain approximately 175,000 lines of C# code and over 600 unit tests. Since we consider the failure of a single unit test to be a failure of the entire build, if one test fails, the Orb pulses red. As you’d guess, CruiseControl.NET also includes unit test results in its e-mail and web page summaries which makes it easy to identify the problem.*


These things are all cool, but I think we can do better. I’ve been playing with the BetaBrite one-line electronic LED sign:


![BetaBrite LED sign](https://blog.codinghorror.com/content/images/uploads/2005/03/6a0120a85dcdae970b0128776fb901970c-pi.jpg)


This thing, for my money (and it was my money, for the record) beats the heck out of retro-kitsch novelty status indicators. You can put full text build status information on there, in eight colors and 12 different font styles. Including animations! It’s way cool; I have yet to see someone walk by my desk who isn’t mesmerized by its hypnotic animation and colors. Sam’s Club has the BetaBrite sign for a reasonable $160, and that includes the serial communication cable, remote, and software.


I’m currently working on some .NET classes that wrap a BetaBrite-specific subset of the [Alpha Sign Communications Protocol](https://web.archive.org/web/20050404030338/http://www.ams-i.com/Pages/97088061.htm). This requires serial communication via a 25 or 50 foot RS-232 serial to RJ-12 cable, so you’ll need a physical PC with either a serial port or a USB-to-Serial adapter to get this working.


With the flexibility of the BetaBrite, [Continous Integration](http://www.martinfowler.com/articles/continuousIntegration.html) monitoring is merely the tip of the iceberg:

- Show webtrends style reporting in real time for your website
- List exceptions and errors as they occur
- Monitor server load, network throughput in realtime
- List checkins by developer name as items are checked in


I can’t make any promises, but this could just be [that extra bit of cowbell](https://web.archive.org/web/20050324061239/http://www.geekspeakweekly.com/cowbell/) your project needs to succeed.

[java](https://blog.codinghorror.com/tag/java/)
[continuous integration](https://blog.codinghorror.com/tag/continuous-integration/)
[build monitoring](https://blog.codinghorror.com/tag/build-monitoring/)
[automation](https://blog.codinghorror.com/tag/automation/)
[devops](https://blog.codinghorror.com/tag/devops/)
