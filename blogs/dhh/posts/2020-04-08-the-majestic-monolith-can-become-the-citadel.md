---
title: "The Majestic Monolith can become The Citadel"
date: 2020-04-08
url: https://signalvnoise.com/svn3/the-majestic-monolith-can-become-the-citadel/
slug: the-majestic-monolith-can-become-the-citadel
word_count: 574
---


The vast majority of web applications should start life as a [Majestic Monolith](https://signalvnoise.com/svn3/the-majestic-monolith/): A single codebase that does everything the application needs to do. This is in contrast to a constellation of services, whether micro or macro, that tries to carve up the application into little islands each doing a piece of the overall work.


And the vast majority of web applications will continue to be served well by The Majestic Monolith for their entire lifespan. The limits upon which this pattern is constrained are high. Much higher than most people like to imagine when they fantasize about being capital-a Architects.


But. Even so, there may well come a day when The Majestic Monolith needs a little help. Maybe you’re dealing with very large teams that constantly have people tripping over each other (although, bear in mind that many very large organizations use the [monorepo](https://en.wikipedia.org/wiki/Monorepo) pattern!). Or you end up having performance or availability issues under extreme load that can’t be resolved easily within the confines of The Majestic Monolith’s technology choices. Your first instinct should be to improve the Majestic Monolith until it can cope, but, having done that and failed, you may look to the next step.


That next step is The Citadel, which keeps the Majestic Monolith at the center, but supports it with a set of Outposts, each extracting a small subset of application responsibilities. The Outposts are there to allow the Majestic Monolith to offload a particular slice of divergent behavior, either for organizational or performance or implementation reasons.


One example at [Basecamp](https://basecamp.com) of this pattern was our old chat application [Campfire](https://basecamp.com/retired/campfire). It was built back in 2005, when Ajax and other JavaScript techniques were still novel, so it was based on polling rather than the persistent connections modern chat apps use these days. That meant that every client connected to the system would trigger a request every three seconds asking “are there any new messages for me?”. The vast majority of these requests would reply “no, there’s not”, but to give that answer, you still had to authenticate the request, query the database, all that jazz.


This service had vastly different performance characteristics from the rest of the application. At any given time, it would be something like 99% of all requests. It was also a really simple system. In Ruby, it was barely 20 lines long, if I remember correctly. In other words, a perfect candidate for an Outpost!


So an Outpost we made. Over the years, it became a hobby to rewrite this Outpost in every high-performance programming language under the sun, because it could usually be done in a few hundred lines of code, regardless of the language. So we wrote it in C, C++, Go, Erlang, and I’m probably forgetting a few others.


But it was clearly an Outpost! The rest of the application continued as a Majestic Monolith built in [Ruby on Rails](https://rubyonrails.org). We didn’t try to carve the entire app up into little services, each written in a different language. No, we just extracted a single Outpost. That’s a Citadel setup.


As more and more people come to realize that the chase for microservices ended in a blind alley, the pendulum is going to swing back. The Majestic Monolith is here waiting for [microservice refugees](https://www.youtube.com/watch?v=y8OnoxKotPQ). And The Citadel is there to give peace of mind that the pattern will stretch, if they ever do hit that jackpot of becoming a mega-scale app.

