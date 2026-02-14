---
title: "The price of managed cloud services"
date: 2023-10-16
url: https://world.hey.com/dhh/the-price-of-managed-cloud-services-4f33d67e
slug: the-price-of-managed-cloud-services-4f33d67e
word_count: 520
---

One of the common objections to
[our cloud exit](https://world.hey.com/dhh/we-have-left-the-cloud-251760fb)
has been that we shouldn't have expected good outcomes from a lift'n'shift operation. That the real value of the cloud is in managed services and new architectures, not just running the same software on rented cloud instances. It's basically the "you're holding it wrong" argument for the cloud, and it's hogwash.
First of all,
[HEY](https://hey.com/)
was born in the cloud for us. It never lived a life on our own hardware before launch. We went live in 2020 using Aurora/RDS for the databases, OpenSearch for search, and EKS for managing app and job servers. That's a pretty intensive use of the native cloud elements! Not just a bunch of raw VMs rented.
And it's exactly
*because*
we used all the cloud had to offer so extensively that
[the bill](https://dev.37signals.com/our-cloud-spend-in-2022/)
ended up so high. And our disappointment over not being able to operate the system with materially less staff so great. There's no way the answer to this question was "just use more managed services" or wave the serverless magic wand over it.
To illustrate, consider our usage of OpenSearch on AWS. We were spending $43,333/month to power search in Basecamp, HEY, and across our logging infrastructure. Just over half a million dollars per year, just for search.
Now we've
[just shut down](https://twitter.com/dhh/status/1712541981220786606)
the last big logging cluster on OpenSearch, which is a great time to compare it with our replacement spend. It cost about $150,000 to buy the hardware we needed ($75,000 per data center, for full redundancy), and if we depreciate this over five years, that's about $2,500/month. It costs us another ~$2,500/month for the power, space, and networking to operate these machines across our two data centers. So call it an even five grand, which includes a bit of a buffer as well.
That's almost an order of magnitude less than we were spending on OpenSearch!! The $150,000 we spent on the hardware will have been repaid in just over three months, and from there on out, we'll be saving some $40,000/month. Just on search alone!
This is usually when people start asking about staffing costs. Which is a reasonable question. What good is $40,000/month in savings if you have to hire a ton of new people to manage it. Well, first of all, I'd argue it's actually still pretty good. Even if we had to hire someone FULL TIME just to look after search, we'd come out way ahead. But we haven't.
Switching from OpenSearch to running elastic search ourselves did require some initial setup, but we're not changing the size of the team at all in the longterm to accommodate for this switch. Because running things on premise is not a materially different scope of work from running it in the cloud. That's the whole premise behind our overall cloud exit: The team it takes to run our scale of operations in the cloud wasn't any less than what it takes to run that same scale on our own hardware.
That was the theory anyway. It's still surprising, startling even, to see it proven out in reality.
