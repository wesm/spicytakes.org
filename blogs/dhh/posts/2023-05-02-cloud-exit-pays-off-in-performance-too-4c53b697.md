---
title: "Cloud exit pays off in performance too"
date: 2023-05-02
url: https://world.hey.com/dhh/cloud-exit-pays-off-in-performance-too-4c53b697
slug: cloud-exit-pays-off-in-performance-too-4c53b697
word_count: 483
---

Last week, we successfully pulled off our biggest
[cloud exit](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)
yet for Basecamp Classic. This is the original app that started it all for us from
[way back in 2004](https://signalvnoise.com/archives/000542.php)
. And now, after a couple of years running on AWS, it's back on
[our own hardware](https://world.hey.com/dhh/the-hardware-we-need-for-our-cloud-exit-has-arrived-99d66966)
, using
[Kamal](https://kamal-deploy.org)
, and holy smokes is it fast! Just look at these charts:

![cloud-exit-performance.png](https://world.hey.com/dhh/4c53b697/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTIwNTg5NzI2NSwicHVyIjoiYmxvYl9pZCJ9fQ--1f226c01a330ec1972ac4f9f07eadb9b7b5bc1f405ca975effec3ad6c47d77ad/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/cloud-exit-performance.png)

The median request now runs in just 19ms, compared to 67ms before. The mean request in 95ms vs 138ms. The median query time has dropped in half (which adds up when you do a lot of queries per request!). Basecamp Classic was no slouch in the cloud before, but now 95% of all requests are below that magic 300ms cut-off.
(But take these comparisons with a pound of salt. It's not exactly a clean-room, scientific test. Just a peak at the reality of leaving a fine-tuned cloud setup for a fully-owned hardware alternative.)
Basecamp Classic ran on EKS in AWS (that's their managed Kubernetes setup) using a mix of c5.xlarge and c5.2xlarge instances for the application itself. The databases were running on db.r4.2xlarge and db.r4.xlarge instances via RDS. Now home, we're running on Dell R7625's with dual AMD EPYC 9454 CPUs.
This new home setup was specced with the same number of vCPUs as we ran in the cloud using KVM, so about 122 for the application and jobs. But looking at our load levels, we can probably shrink that a fair bit, and still keep these excellent performance figures.
In fact, given that each of our new Dell R7625s have 196 vCPUs, we could actually run the entire Basecamp Classic application, including databases and Redis, on a single such machine! That's just astounding. Of course, you wouldn't actually do that for redundancy reasons, but it's a testament to the fact that
[hardware is fun again](https://world.hey.com/dhh/hardware-is-fun-again-b819d0b4)
and that we've come full circle. Basecamp launched in 2004 on a single machine (with 1 vCPU!) and can now, in 2023, run on a single machine again.
Each of these machines were less than $20,000. Amortize that over five years. That's $333/month for all the hardware (minus routers etc) needed to run Basecamp Classic today. And this is still a large SaaS app that's generating literally millions of dollars in revenue per year! The vast majority of SaaS businesses out there would require far less firepower to service their customers.
Now, we didn't pin our
[cloud exit strategy](https://world.hey.com/dhh/five-values-guiding-our-cloud-exit-638add47)
on increasing performance, but it's nice to see that it did anyway. Especially since Basecamp Classic, this twenty-year old OG of our business, is still serving a large, loyal, and satisfied customer base that haven't received any new features in over a decade. But hey, speed is a feature too, so I guess you could say we just shipped one!
Next up on the cloud exit schedule is the big one:
[HEY](https://www.hey.com/)
! Stay tuned.
