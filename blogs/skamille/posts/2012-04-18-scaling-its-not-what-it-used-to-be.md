---
title: "Scaling: It's Not What It Used To Be"
date: 2012-04-18
url: https://www.elidedbranches.com/2012/04/scaling-its-not-what-it-used-to-be.html
word_count: 539
---

We've seen a lot of interesting stories lately about companies scaling massively from just a few users to millions in a very short period of time. Contrary to expectation, some of them weren't even initally designed for scaling. Take, for example,
[Instagram](http://www.scribd.com/doc/89025069/Mike-Krieger-Instagram-at-the-Airbnb-tech-talk-on-Scaling-Instagram)
(a fabulous slide deck, btw). Their first strategy for scaling was vertical: buy a bigger database server. That didn't last too long, and they found themselves doing horizontal scaling (via sharding) after a few months. But instead of writing their own custom database solution, or using one of the many NoSQL options out there, they stuck with
[Postgres](http://www.postgresql.org/)
and via a clever virtual sharding strategy combined with
[Redis](http://redis.io/)
and
[Memcached](http://memcached.org/)
, they managed to scale.
Then there's
[Draw Something](http://www.gamasutra.com/view/news/168799/Scale_Something_How_Draw_Something_rode_its_rocket_ship_of_growth.php)
. While the engineers designed it to scale, they had no idea that it would hit hundreds of drawings per second in its first few weeks. In contrast to Instagram, they ended up rewriting their backend data store in
[Membase](http://www.couchbase.com/membase)
during their growth spurt, but that combined with sharding and adding hardware (both vertically via more RAM and SSDs, and horizontally via more machines) got them through their growth period.
10 years ago, scaling to millions of users would have probably taken a large, smart team with months of advance planning to achieve. As a point of reference, Livejournal had about 1.5 million active users per month in 2005, a very popular site at the time, and memcached was created to handle its load. I'm sure that the developers at Draw Something, Instagram and other popular tech start ups are very talented, but it's more than talent that is allow this kind of unplanned growth to happen. The common points between these two teams are not what I was expecting when I sat down to write this post. So what are they?
1.
[Redis](http://redis.io/)
. I was at a NoSQL meetup last night when someone asked "if you could put a million dollars behind one of the solutions presented here tonight, which one would you choose?" And the answer that one of the participants gave was "None of the above. I would choose Redis. Everyone uses one of these products and Redis."
2.
[Nginx](http://wiki.nginx.org/Main)
. Your ops team probably already loves it. It's simple, it scales fabulously, and you don't have to be a programmer to understand how to run it.
3.
[HAProxy](http://haproxy.1wt.eu/)
. Because if you're going to have hundreds or thousands of servers, you'd better have good load balancing.
4.
[Memcached](http://memcached.org/)
. Redis can act as a cache but using a real caching product for such a purpose is probably a better call.
And finally:
5. Cloud hardware. Imagine trying to grow out to millions of users if you had to buy, install, and admin every piece of hardware you would need to do such a thing.
Redis, Nginx, HAProxy, Memcached. All free open-source software. AWS and other cloud vendors let any of us grab machines to run our software at the touch of a button. The barriers to entry have gone way down, and we've all discovered that scaling, while hard, isn't nearly as much of a monster as we made it out to be. It's truly an exciting time to be a software engineer.