---
title: "Finishing Hotwire with the introduction of Strada"
date: 2023-09-20
url: https://world.hey.com/dhh/finishing-hotwire-with-the-introduction-of-strada-9efdf091
slug: finishing-hotwire-with-the-introduction-of-strada-9efdf091
word_count: 581
---

When
[we announced Hotwire](https://world.hey.com/dhh/stimulus-3-turbo-7-hotwire-1-0-9d507133)
a few years back, it was always meant as a triptych. The center piece is
[Turbo](https://turbo.hotwired.dev)
. That's the drop-in level-up that makes multi-page web apps feel like single-page web apps – without giving up any of the development advantages to server-side programming. Then
[Stimulus](https://stimulus.hotwired.dev)
brought order and structure to JavaScript sprinkles by triggering custom behavior via HTML attributes. And finally, which is what we're revealing today, there's
[Strada](https://strada.hotwired.dev)
: The bridge between native controls and the web app.
Strada continues the
[Majestic Monolith](https://m.signalvnoise.com/the-majestic-monolith/)
story by extending Hotwire onto native controls. Where
[Turbo Native](https://turbo.hotwired.dev/handbook/native)
makes it easy to have native mobile apps driven by fast web views, Strada brings that extra bit of polish only native controls, like native menus, can provide.
This is important for several reasons. First, it further blurs the lines between the web and native parts of a great mobile app. When you use a hybrid application like
[HEY](https://hey.com)
or
[Basecamp](https://basecamp.com)
, it's often quite difficult to tell exactly where the native ends and the web begins, in part because Strada is there to smooth over the transition. While true native nerds can probably still tell the difference, the vast majority of paying customers cannot. And the productivity benefits to not writing everything as custom, native screens are immense.
Second, it shrinks the reliance on the app store permission regimes. One of the reasons that developing for the web feels so magical is because you can roll out changes and fixes to everyone instantly without asking or waiting for permission. You can deploy ten times per day, if that's the pace by which you're able to improve your service. It just doesn't work like that in the mobile world. If you're lucky, permission might come in a few hours, and if you're unlucky, it could take days or even weeks. And every time you submit a new build, you have to factor in the risk that
[a bureaucrat will reject your application](https://www.hey.com/apple/)
for reasons unknown.
Third, it makes your web team that much more self-sufficient. Where smaller shops might have developers who are capable of both updating the web and native apps, lots of companies have some separation. So do we at
[37signals](https://37signals.com)
. We have a crack team of native developers, but a substantially larger team of web developers working the Majestic Monolith. The more power we can give the web developers to introduce new features on the Majestic Monolith that Just Works inside the mobile apps, the less we need to grind gears coordinating releases with the mobile team. That's a huge win.
This has been the mission for Hotwire since the beginning. Supercharge the productivity of individual developers by making them capable of building and delivering complete features across all platforms by themselves. No frontend/backend separation, and as little web/native separation as possible too. Strada makes that second part even better. Web developers driving changes on native controls without the need to tap in mobile developers.
I can't tell you how nice it feels to finish the Hotwire story in public with
[the open source release of Strada](https://dev.37signals.com/announcing-strada/)
. Now it's all out there for anyone willing to seize the opportunity and productivity that we've been able to enjoy while developing Basecamp and HEY across web, iPhone, iPad, Android, macOS, Windows, and email as a single Majestic Monolith. One built with a comparably tiny team for the number of customers, amount of revenue, and breadth of applications that takes. Enjoy!
