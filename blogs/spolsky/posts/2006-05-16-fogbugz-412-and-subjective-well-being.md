---
title: "FogBugz 4½ and Subjective Well-Being"
date: 2006-05-16
url: https://www.joelonsoftware.com/2006/05/16/fogbugz-412-and-subjective-well-being/
word_count: 1212
---


Let me tell you the story of how we came to be shipping FogBugz 5.0 about six months earlier than expected.


It’s kind of a long story.


It turns out that students in Canada like to organize their own conferences, and a couple of years back they organized one and invited me to speak.


College students make great audiences. They’ll laugh at anything. I gathered together a bunch of random ideas and some funny slides I downloaded from the Internet (one of which is shown at right, proving that there’s life on Mars) and they were rolling in the aisles.


One theme from that speech was based on the most important thing that I learned in Psych 110, the idea that when people are successful at controlling their environment they become happier, and when they can’t control their environment, they get grumpy.


(Actually, using words like “happiness” and “grumpy” tends to inhibit tenure, so a real psychologist would say something like “repeated failure inhibits the experience of agency, decreasing subjective well-being.”)


Put people in direct control of the stuff around them and they will, more or less, on average, be happier. It explains why some people like stick shifts, it explains why lethargic user interfaces make you frustrated and depressed, and it explains why people get so goddamn mad when Sony decides to install viruses on their computers just because they tried to listen to a CD.


If you’re a software designer, *this is it*. This is your big chance to do something meaningful to improve the world. Design software that puts the user in control and you’ll increase happiness, even if your product is the most boring accounting software imaginable. You can do this at the most microscopic levels:

- The bookkeeping software I’ve been using for the last six years makes a beep when you record a transaction.
- The Apple iPod includes a tiny internal speaker so that the thumbwheel sounds like it’s clicking when you rotate it.
- The Sonos digital music system has a handheld controller with a motion sensor built in. The instant you pick it up, the screen lights up.


You can also screw it up:

- Most modern cell phones have mushy on/off buttons that take forever to turn on. It’s hard to tell if you didn’t press hard enough because the phone acts like it’s ignoring you.
- The people who make DVD movies seem to think that it’s OK to disable the Menu and Fast Forward buttons while they’re showing you advertisements and ridiculous FBI warnings.
- Web browsers deal with the security problem by displaying a seemingly endless series of modal popups asking you to confirm that you *really* want to have three NFL linebackers come into your home and force-feed you a football.
- That Sonos controller has a thumbwheel that’s too sensitive to choose menu items without a lot of futzing around. Or maybe it’s just because I have fat thumbs.


In the last year or so a lot of web developers have been working hard on improving their applications using techniques now known as *Ajax*. These applications use JavaScript code so that when you click on something, you get immediate feedback, rather than waiting for the web server to send you a new page at its own leisurely pace. When they do need more information from the server, they often download the small fragment they need, rather than waiting for the server to build a whole new page. The net result is faster, crisper feedback that *makes you feel in control* and creates “subjective well-being,” a.k.a. happiness, a feeling that is biochemically NO DIFFERENT THAN EATING LARGE QUANTITIES OF CHOCOLATE.


Just a minute… I have to pause for some fact checking …


… ok, I’m back. To summarize, Ajax = Chocolate = Happiness, and so we knew, when we started planning FogBugz 5.0, that Ajax features would be an important part of this release.


The two places FogBugz users spend most of their time is in the single case page, where you view and edit cases, and the list page, where you browse, sort, slice and dice cases. With 5.0 we basically took the approach that we would go crazy with those two pages, improving everything we can about the experience using JavaScript and Ajax.


On the list page, for example, Ben added the ability to drag and drop columns, lots of intuitive new ways to select multiple bugs, the ability to resize columns and add arbitrary columns of data. It’s all done on the client and it’s all very fast.


On the single case page, where you’re looking at a single bug or email, Brett made it so that commands like Edit or Reply happen instantaneously, on the client side, in the browser, without a round trip to the server. The net result is that when you’re working through a lot of cases, you need about half as many round-trips to the server making the whole experience feel much, much more responsive. You feel in control, and you are happier. It works!


Brett also snuck in a feature he’s been itching for: lots and lots and lots of keyboard shortcuts. There’s only one keyboard shortcut you have to memorize, though: Ctrl+; switches FogBugz into keyboard mode and little letters light up reminding you what the shortcuts are for various commands around the screen. It’s really pretty cool to be able to work through a bunch of cases, assigning, editing, and reprioritizing, without ever reaching for the mouse. Combined with the speed and responsiveness from Ajax, FogBugz has *almost* reached the level of speed and fluidity of my dry cleaner’s DOS 2.0 character mode database application. And that’s pretty darn responsive for a web app.


Anyway, because FogBugz is not a hosted product—we sell the software to our customers, who install it on their own servers—we try not to have *too* many releases, and we try to make each release really, really solid. But we do have our own FogBugz server which runs the company—it sorts incoming email, tracks bugs and features under development, serves as our recruiting database and resume file, routes incoming faxes, and manages purchase orders; I’m even using FogBugz to edit the next edition of Best Software Writing.


In a rather extreme form of eating our own dogfood, the developers put their latest build up every few days so we can all bang on it.


The more we played with the new Ajax features the more we fell in love, and the more we realized that this was the single greatest thing we had done in FogBugz in a looooong time. So we decided to ship the new features as soon as possible. We would take a few months going through a complete beta cycle, and get this stuff out to our customers right away rather than waiting for the other planned 5.0 features.


And that’s where we are today. What’s shipping today is really something like FogBugz 4½, but we’re calling it 5.0 anyway, because life is confusing enough without fractions. We’re only on year six of the “great software takes ten years” rule, but I’d say we’re more than 60% there. Check out the [FogBugz homepage](http://www.fogcreek.com/fogbugz); there’s an online demo at [try.fogbugz.com](http://try.fogbugz.com/).
