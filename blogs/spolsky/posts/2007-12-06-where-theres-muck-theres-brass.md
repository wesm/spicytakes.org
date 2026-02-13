---
title: "Where there’s muck, there’s brass"
date: 2007-12-06
url: https://www.joelonsoftware.com/2007/12/06/where-theres-muck-theres-brass/
word_count: 1306
---


When I was a kid working in the bread factory, my nemesis was dough. It was sticky and hard to remove and it got everywhere. I got home with specks of dough in my hair. Every shift included a couple of hours of scraping dough off of machinery. I carried dough-scrapers in my back pocket. Sometimes a huge lump of dough would go flying someplace where it shouldn’t and gum up everything. I had dough nightmares.


I worked in the production side of the factory. The other side did packing and shipping. Their nemesis was crumbs. Crumbs got everywhere. The shipping crew went home with crumbs in their hair. Every shift included a couple of hours of brushing crumbs out of machinery. They carried little brushes in their back pockets. I’m sure they had crumb nightmares, too.


Pretty much any job that you can get paid for includes dealing with one gnarly problem. If you don’t have dough or crumbs to deal with, maybe you work in a razor blade factory and go home with little cuts all over your fingers. Maybe you work for VMWare and have nightmares about emulating bugs in sophisticated video cards that games rely on. Maybe you work on Windows, and your nightmare is that the simplest change can cause millions of old programs and hardware devices to stop working. That’s the gnarly part of your job.


One of our gnarly problems is getting FogBugz to run on our customers’ own servers. Jason Fried over at [37signals](http://www.37signals.com/) has [a good summary](http://www.37signals.com/svn/posts/724-ask-37signals-installable-software) of why this is no fun: “You have to deal with endless operating environment variations that are out of your control. When something goes wrong it’s a lot harder to figure out why if you aren’t in control of the OS or the third party software or hardware that may be interfering with the install, upgrade, or general performance of your product. This is even more complicated with remote server installs when there may be different versions of Ruby, Rails, MYSQL, etc. at play.” Jason concludes that if they had to sell installable software, they “definitely wouldn’t be as happy.” Yep. Work that makes you unhappy is what I mean by “a gnarly problem.”


The trouble is, the market pays for solutions to gnarly problems, not solutions to easy problems. As the Yorkshire lads say, “[Where there’s muck, there’s brass](http://www.phrases.org.uk/meanings/408900.html).”


We offer both kinds of FogBugz–hosted and installable–and our customers opt 4 to 1 to install it at their own site. For us, the installable option gives us five times the sales. It costs us an extra salary or two (in tech support costs). It also means we have to use Wasabi, which has some serious disadvantages compared to off-the-shelf programming languages, but which we found to be the most cost-effective and efficient way, given our code base, to ship software that is installable on Windows, Linux, and Mac. Boy, I would love nothing more than to scrap installable FogBugz and run everything on our servers… we’ve got racks and racks of nice, well-managed Dell servers with plenty of capacity and our tech support costs for the hosted version are zero. Life would be much easier. But we’d be making so much less money we’d be out of business.


The one thing that so many of today’s cute startups have in common is that all they have is a simple little Ruby-on-Rails Ajax site that has no barriers to entry and doesn’t solve any gnarly problems. So many of these companies feel insubstantial and fluffy, because, out of necessity (the whole company is three kids and an iguana), they haven’t solved anything difficult yet. Until they do, they won’t be solving problems for people. People pay for solutions to their problems.


Making an elegantly-designed and easy-to-use application is just as gnarly, even though, like good ballet, it seems easy when done well. Jason and 37signals put effort into good design and get paid for that. Good design seems like the *easiest* thing to copy, but, watching Microsoft trying to copy the iPod, turns out to be not-so-easy. Great design *is *a gnarly problem, and can actually provide surprisingly sustainable competitive advantage.


Indeed Jason probably made a good choice by picking the gnarly problem where he has a lot of talent (design) to solve, because it doesn’t seem like a chore to him. I’ve been a Windows programmer for ages, so making a Windows Setup program for FogBugz, from scratch in C++ doing all kinds of gnarly COM stuff, doesn’t seem like a chore to me.


The only way to keep growing–as a person and as a company–is to keep expanding the boundaries of what you’re good at. At some point, the 37signals team might decide that hiring one person to write the Setup script and do installation support would pay for itself, and generate substantially more profit than it costs. So unless they deliberately want to keep the company small, which is a perfectly legitimate desire, they might eventually lose their reluctance to do things that seem gnarly.


Or maybe they won’t. There’s nothing wrong with choosing the fun part of your business to work on. I’ve certainly been guilty of that. And there’s nothing wrong with deciding that you only want to solve a specific set of problems for a small, select group of people. Salesforce has managed to become big enough by sticking to hosted software. And there are plenty of smaller software shops providing a fantastic lifestyle for their crew with no desire to get any bigger.


But the great thing is that as you solve each additional gnarly problem, your business and market grows substantially. Good marketing, good design, good sales, good support, and solving lots of problems for customers all amplify each other. You start out with good design, then you add some good features and triple your customer base by solving lots of problems, and then you do some marketing and triple your customer base again because now lots of people learn about your solution to their pain, and then you hire sales people and triple your customer base yet again because now the people who know about your solution are reminded to actually buy it, and then you add more features to solve more problems for even more people, and eventually you actually have a chance to reach enough people with your software to make the world a better place.


P.S. I’m not claiming here that 37signals would sell 5 times as many copies if they offered Installable Basecamp. First of all, one of the reasons we may sell so many more installable versions of FogBugz is that it appears, to some customers, to be cheaper. (It’s not cheaper in the long run because you have to pay for the server and administer it yourself, but that’s subjective.) Also, our support costs for the installable version are only as low as they are because 80% of our customers opt to run on Windows Server. Because Windows systems are so similar, it’s much easier for us to support the lowest common denominator. The vast majority of our tech support costs are caused by the diversity in Unix platforms out there–I’d guess that the 20% of our Unix sales result in 80% of our support incidents. If an installable version of Basecamp required Unix, the support cost would be disproportionately expensive compared to a hypothetical installable Windows version. Finally, another reason our experience might not translate to 37signals is that we’ve been selling installable software for seven years now; the hosted version has only been out for about six months. So we have a big installed base used to running FogBugz on their own servers. If you only look at *new* FogBugz customers, the ratio of installable to hosted goes down to 3 to 1.
