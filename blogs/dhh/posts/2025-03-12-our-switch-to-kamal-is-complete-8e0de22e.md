---
title: "Our switch to Kamal is complete"
date: 2025-03-12
url: https://world.hey.com/dhh/our-switch-to-kamal-is-complete-8e0de22e
slug: our-switch-to-kamal-is-complete-8e0de22e
word_count: 388
---

In a fit of frustration, I wrote the first version of
[Kamal](https://kamal-deploy.org/)
in six weeks at
[the start of 2023](https://world.hey.com/dhh/introducing-kamal-9330a267)
.
[Our plan to get out of the cloud](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)
was getting bogged down in
[enterprisey pricing](https://world.hey.com/dhh/the-only-thing-worse-than-cloud-pricing-is-the-enterprisey-alternatives-854e98f3)
and Kubernetes complexity. And I refused to accept that running our own hardware had to be that expensive or that convoluted. So I got busy building a cheap and simple alternative.
Now, just two years later, Kamal is deploying every single application in our entire heritage fleet, and everything in active development. Finalizing a perfectly uniform mode of deployment for every web app we've built over the past two decades and still maintain.
See, we have this obsession at
[37signals](https://37signals.com)
: That the modern build-boost-discard cycle of internet applications is a
[scourge](https://killedbygoogle.com/)
. That users ought to be able to trust that when they adopt a system like
[Basecamp](https://basecamp.com)
or
[HEY](https://hey.com)
, they don't have to fear eviction from the next executive re-org. We call this obsession
[Until The End Of The Internet](https://world.hey.com/dhh/until-the-end-of-the-internet-439ccfce)
.
That obsession isn't free, but it's worth it. It means we're still operating the very first version of Basecamp for thousands of paying customers. That's the OG code base from 2003! Which hasn't seen any updates since 2010, beyond security patches, bug fixes, and performance improvements. But we're still operating it, and, along with every other app in our heritage collection, deploying it with Kamal.
That just makes me smile, knowing that we have customers who adopted Basecamp in 2004, and are still able to use the same system some twenty years later. In the meantime, we've relaunched and dramatically improved Basecamp many times since. But for customers happy with what they have, there's no forced migration to the latest version.
I very much had all of this in mind when designing Kamal. That's one of the reasons I really love Docker. It allows you to encapsulate an entire system, with all of its dependencies, and run it until the end of time. Kind of how modern gaming emulators can run the original ROM of Pac-Man or Pong to perfection and eternity.
Kamal seeks to be but a simple wrapper and workflow around this wondrous simplicity.
[Complexity is but a bridge](https://www.youtube.com/watch?v=iqXjGiQ_D-A&t=1289s)
— and a fragile one at that. To build something durable, you have to make it simple.
