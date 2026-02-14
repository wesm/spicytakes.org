---
title: "Celebrating the silence of high uptimes"
date: 2022-01-03
url: https://world.hey.com/dhh/celebrating-the-silence-of-high-uptimes-056c4887
slug: celebrating-the-silence-of-high-uptimes-056c4887
word_count: 432
---

It was a very loud year, 2021. Which makes the satisfying silence of technical incidents at Basecamp all the more of a celebration. In the year that went, every single application we offer had at least 99.99% uptime! This is through repeated AWS outages, zero-day security alerts, and the drama of the world in those twelve months.
But it gets better. Basecamp 3 had an uptime of 99.997%. HEY pipped it by a point with 99.998% uptime. And Basecamp 2 hit the mythical five nines with 99.999% uptime! I believe that is the best reliability record we've ever achieved for a full year in our almost twenty year history as a software company. Worth a toast!
It's the result of years of investments in things like active-active double data center deployments for our on-premise apps like Basecamp 2 and 3. A difficult setup that took a long time to get right, but now lets us do major upgrades with relative ease (each center can shoulder the full production peak load). While enjoying an instant ability to deal with any issues in a single data center.
Ditto on the cloud front. We finally shut down the last of our Google Cloud Platform usage, after having been
[burned so badly in 2019](https://m.signalvnoise.com/basecamp-outage-when-it-rains-it-pours/)
by their file storage outages in particular. In its place is an (extreme/excessively?) redundant S3 setup with files being replicated across independent regions, that are each picked to ensure that our major apps don't share their primary region with each other (so there's less apps to fix simultaneously in an outage).
The applications themselves are also distributed across regions in such a way that when aws-east-1 (the oldest, biggest, and, at least recently, most prone to outage region that AWS offers)
[is down again](https://www.zdnet.com/article/aws-suffers-third-outage-of-the-month/)
, we're able to quickly minimize the damage done to our reliability. Often without even a public hitch.
Now I know that superstition demands that if you celebrate your uptime, you're due a calamity of failures shortly thereafter. And while I don't believe in that kind of mumbo jumbo, it totally could happen. Regression to the mean, and all.
But I don't think having a fear of celebrating the crowning achievements of technical operational excellence is wise. Keeping the lights on for a (very broad!) set of applications with hundreds of thousands of users, petabytes of data, across on-premise
*and*
cloud, with software legacies stretching back to the dawn of this millennium? That's not easy! And when the job is done so well, in times so trying, it deserves all of the accolades.
Bravo, Basecamp Ops. Bravo! 👏
