---
title: "We stand to save $7m over five years from our cloud exit"
date: 2023-02-21
url: https://world.hey.com/dhh/we-stand-to-save-7m-over-five-years-from-our-cloud-exit-53996caa
slug: we-stand-to-save-7m-over-five-years-from-our-cloud-exit-53996caa
word_count: 566
---

Since declaring
[our intention to leave the cloud](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)
in October, we've been busy at work making it so. After a brief detour down
[a blind alley with an enterprise Kubernetes provider](https://world.hey.com/dhh/the-only-thing-worse-than-cloud-pricing-is-the-enterprisey-alternatives-854e98f3)
, we found our stride building our own tools, and successfully moved the first small application out of the cloud a few weeks ago. Now our sights are set on a total cloud exit by the end of the Summer, and by our preliminary calculations, we stand to save about $7m in server expenses over five years from doing so. Without changing the size of our ops team.
The rough math goes like this:
[We spent $3.2m on cloud in 2022](https://dev.37signals.com/our-cloud-spend-in-2022/)
. Just under a million of that was on storing 8 petabytes of files in S3, fully replicated across several regions. So that leaves ~$2.3m on everything else: app servers, cache servers, database servers, search servers, the works. That's the part of the budget we intend to bring to zero in 2023. Then we'll worry about exiting the 8PB from S3 in 2024.
After much deliberation, many benchmarks, and much aweing at the speed of AMD's new Zen4 chips combined with Gen 4 NVMe drives, we're almost ready to place our monster order with Dell. Somewhere in the region of $600,000. We're still fine-tuning exactly what configurations we need, but whether we end up ordering 8 machines running dual 64-core CPUs (for a total of 256 vCPUs per box!) in each data center or 14 machines running single-socket CPUs at a higher clock frequency doesn't really matter to the overall math. We need to add about 2,000 vCPU per data center, and we run in two data centers, so 4,000 vCPUs for performance and redundancy. All rough numbers.
Spending $600,000 on a bunch of hardware might sound like a lot in the age of cloud. But if you amortize that over a conservative five years, it's just $120,000 per year! And we have lots of boxes still running at seven years.
But that's of course just the boxes. They also have to be connected to power and bandwidth. We currently spend about $60,000/month on eight dedicated racks between our two data centers through
[Deft](https://deft.com)
. We purposely over-provisioned our space, so we can actually fit all of these many new servers in the existing racks without needing more space or power. Thus the spend remains around $720,000/year.
That's a total of $840,000/year for everything. Bandwidth,  power, and boxes on an amortization schedule of five years. Compared to $2.3m in the cloud. And we'll have much faster hardware, many more cores, incredibly cheaper NVMe storage, and room to expand at a very low cost (as long as we can still fit in four racks per DC).
In round numbers, let's call it saving a million and a half dollars per year. Put aside half a million to unforeseen expenses over the period, and that's still SEVEN MILLION DOLLARS SAVED OVER FIVE YEARS!!
Any mid-sized SaaS business and above with stable work loads that does not benchmark their rental bill for servers in the cloud against buying their own boxes is committing financial malpractice at this point. I suggest you call Dell, then call Deft. Get some real world numbers. Make up your own mind.
We'll continue to share our lessons, our tooling, and our math as we complete the cloud exit (sans S3) in 2023.
