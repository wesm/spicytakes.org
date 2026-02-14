---
title: "Multi-tenancy is what’s hard about scaling web services"
date: 2024-01-14
url: https://world.hey.com/dhh/multi-tenancy-is-what-s-hard-about-scaling-web-services-dd1e0e81
slug: multi-tenancy-is-what-s-hard-about-scaling-web-services-dd1e0e81
word_count: 457
---

Computers have gotten so ridiculously fast that there is scarcely any organization in the world that can overwhelm a web-based information system running on a single server. All the complexity and sophistication required to run web services today stem from multi-tenancy. From having a single system serve millions of users at the same time. But what if we stopped doing that?
That’s essentially the premise of a resurgent interest in sqlite outside of its historic embedded use cases. Sure, you can’t run
[HEY](https://www.hey.com/)
or
[Basecamp](https://www.basecamp.com/)
, let alone
[Shopify](https://www.shopify.com)
or
[GitHub](https://github.com)
, on a single sqlite instance serving all customers. We have really good database systems, like MySQL and PostgreSQL, designed for that purpose. But any individual customer of any of the above-mentioned services absolutely could run on sqlite on a single server. So what does that mean?
We’re trying to find out with
[ONCE](https://once.com/)
. Our upcoming series of web-based systems that you buy as a product rather than rent as service. The idea is that you’ll run this product yourself, either on a cloud VM or on your own hardware, and that you’ll run it
*just*
for yourself. No multi-tenancy, no intermingling of data, much easier scaling dynamics.
We’re still putting the final polish on this concept, so I won’t go into detail yet about what ONCE #1 actually is or does. But it doesn’t even matter. Most web-based information systems that are used today run as SaaS on the multi-tenancy paradigm. This is the style the industry has been perfecting over the past twenty years. It works.
I mean, for some definition of “works”. Perhaps I should say that it’s “possible”. Because it sure as hell isn’t easy, once you get to scale. Part of the original cloud pitch was that it would
*become*
easy, but
[that never panned out](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)
. There’s no major  web-based information system with millions of users that’s “easy” to run. Most of them have serious operations teams constantly tending to these complex beasts, most of which is around data storage and access.
That’s what’s so alluring about single-tenancy, sqlite, and turning services back into products. The possibility of sidestepping much of this complexity for both development and operations.
Not that this is anything new, mind you. Our beloved industry consists of a handful of pendulums that continuously swing back and forth, and distributed clients vs centralized services is one of the biggest.
But rather than use that historical fact to poo-poo this idea, or any other pendulum swing, you could appreciate the fact that progress usually requires revisiting your priors.
I for one am terribly excited about what conceptual compressions might lie just around the corner, if single-tenancy at scale pans out as a strategy. Let’s go find out!
