---
title: "It's five grand a day to miss our S3 exit"
date: 2025-03-26
url: https://world.hey.com/dhh/it-s-five-grand-a-day-to-miss-our-s3-exit-b8293563
slug: it-s-five-grand-a-day-to-miss-our-s3-exit-b8293563
word_count: 403
---

We're spending just shy of $1.5 million/year on AWS S3 at the moment to host files for
[Basecamp](https://basecamp.com/)
,
[HEY](https://hey.com/)
, and
[everything else](https://world.hey.com/dhh/until-the-end-of-the-internet-439ccfce)
. The only way we were able to get the pricing that low was by signing a four-year contract. That contract expires this summer, June 30, so that's our departure date for the final leg of
[our cloud exit](https://world.hey.com/dhh/we-have-left-the-cloud-251760fb)
.
We've already racked the replacement from
[Pure Storage](https://www.purestorage.com/)
in our two primary data centers. A combined 18 petabytes, securely replicated a thousand miles apart. It's a gorgeous rack full of blazing-fast NVMe storage modules. Each card in the chassis
[capable of storing 150TB now](https://www.tomshardware.com/pc-components/storage/pure-storage-exec-teases-150tb-ssd-modules-volume-shipments-of-75tb-ssd-modules-have-only-just-begun)
.
Pure Storage comes with an S3-compatible API, so no need for CEPH, Minio, or any of the other object storage software solutions you might need, if you were trying to do this exercise on commodity hardware. This makes it pretty easy from the app side to do the swap.
But there's still work to do. We have to transfer almost six petabytes out of S3. In an earlier age, that egress alone would have cost hundreds of thousands of dollars in fees alone. But now AWS offers
[a free 60-day egress window](https://aws.amazon.com/blogs/aws/free-data-transfer-out-to-internet-when-moving-out-of-aws/)
for anyone who wants to leave, so that drops the cost to $0. Nice!
It takes a while to transfer that much data, though. Even on the fat 40-Gbit pipe we have set aside for the purpose, it'll probably take at least three weeks, once you factor in overhead and some babysitting of the process.
That's when it's good to remind ourselves why June 30th matters. And the reminder math pens out in nice, round numbers for easy recollection: If we don't get this done in time, we'll be paying a cool
*five thousand dollars a day*
to continue to use S3 (if all the files are still there). Yikes!
That's $35,000/week! That's $150,000/month!
Pretty serious money for a company of our size. But so are the savings. Over five years, it'll now be almost five million! Maybe even more, depending on the growth in files we need to store for customers. About $1.5 million for the Pure Storage hardware, and a bit less than a million over five years for warranty and support.
But those big numbers always seem a bit abstract to me. The idea of paying $5,000/day, if we miss our departure date, is awfully concrete in comparison.

![pure-storage.jpeg](https://world.hey.com/dhh/b8293563/representations/eyJfcmFpbHMiOnsiZGF0YSI6MjA1NzgwOTYyNSwicHVyIjoiYmxvYl9pZCJ9fQ--3def762c174200fffc7081f9c8a90d728dd40cdd73927ab02e6b3277cbcd2fdc/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGVnIiwicmVzaXplX3RvX2xpbWl0IjpbMzg0MCwyNTYwXSwicXVhbGl0eSI6NjAsImxvYWRlciI6eyJwYWdlIjpudWxsfSwiY29hbGVzY2UiOnRydWV9LCJwdXIiOiJ2YXJpYXRpb24ifX0--86fa621099aa99aa0c7ae156d97d21b387d30fa6ac57aa5c89948af503464a06/pure-storage.jpeg)

