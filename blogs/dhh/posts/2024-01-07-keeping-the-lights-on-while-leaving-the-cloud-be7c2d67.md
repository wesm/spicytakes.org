---
title: "Keeping the lights on while leaving the cloud"
date: 2024-01-07
url: https://world.hey.com/dhh/keeping-the-lights-on-while-leaving-the-cloud-be7c2d67
slug: keeping-the-lights-on-while-leaving-the-cloud-be7c2d67
word_count: 534
---

It was a big year for ops at
[37signals](https://37signals.com)
. In 2023, we moved seven major applications
[out of the cloud](https://world.hey.com/dhh/we-have-left-the-cloud-251760fb)
. Including
[HEY](https://hey.com/)
, our email service, which had been born there, and has an extremely high level of uptime criticality. Moving out of the cloud could not interfere with that obligation, and thankfully it did not. In 2023, HEY had a stellar uptime of 99.99%!
That’s really important, because if people can’t get to their emails, they might not be able to check-in for their flight, close on a time-sensitive deal, or learn the results of a medical test. We take that responsibility very seriously. So hitting the hallowed four nines in a year when everything had to change about how we run HEY is a major accomplishment that makes me proud.
But it wasn’t just HEY that got the diligent ops treatment. Every single major application we run had a minimum of 99.99% uptime in 2023! That includes Highrise, Backpack, Campfire, and all the versions of
[Basecamp](https://basecamp.com/)
. It’s not that we had zero issues, but that the team managed to mitigate all of the issues we had so swiftly that the total downtime didn’t exceed 0.01% over the course of the year.
To the question about whether you can ensure reliability and stability outside the cloud, no application makes this point clearer for us than Basecamp 2. This is the version of Basecamp we sold from 2012-2015, and which still has thousands of users, generating millions of dollars in revenue. It’s been running on our own hardware for years, and now for the second year in row had an almost unbelievable uptime of 100%. That’s right, zero downtime in the 365 days that made up 2023. Just like it did in 2022.
I’m not going to pretend that having such a spectacular uptime record is easy, because it is not. It’s not easy to do anything that well, and we have a seriously skilled and dedicated ops team that deserve huge kudos for making this happen. But, it’s also not rocket science!
The magic of Basecamp 2’s incredible two-year 100% uptime, as well as all the other applications hitting 99.99%, come in part from picking boring, basic technologies. We run on F5s, Linux, KVM, Docker, MySQL, Redis, Elastic Search, and of course
[Ruby on Rails](https://rubyonrails.org/)
. There’s nothing fancy about our stack, and very little complexity either. We don’t need people with PhDs in Kubernetes or specialists in exotic data stores. And neither do you, most likely.
But programmers are attracted to complexity like moths to a flame. The more convoluted the systems diagram, the greater the intellectual masturbation. Our commitment to resisting that is the key ingredient in this uptime success.
Now I’m not talking about what it takes to run Netflix or Google or Amazon. At that kind of scale, you hit truly pioneer-level problems to which there are no tried-and-true solutions to pull from. But for the other 99.99% of us? It’s a siren song to model our infrastructure in their image.
You don’t need the cloud to get good uptimes. You need mature technologies run on redundant hardware with good backups. Same as it ever was.
