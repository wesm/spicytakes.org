---
title: "Our cloud-exit savings will now top ten million over five years"
date: 2024-10-17
url: https://world.hey.com/dhh/our-cloud-exit-savings-will-now-top-ten-million-over-five-years-c7d9b5bd
slug: our-cloud-exit-savings-will-now-top-ten-million-over-five-years-c7d9b5bd
word_count: 930
---

We
[finished](https://world.hey.com/dhh/we-have-left-the-cloud-251760fb)
pulling seven cloud apps, including
[HEY](https://hey.com/)
, out of AWS and onto our own hardware last summer. But it took until the end of that year for all the long-term contract commitments to end, so 2024 has been the first clean year of savings, and we've been pleasantly surprised that they've been even better than originally estimated.
For 2024, we've brought the cloud bill down from the original $3.2 million/year run rate to $1.3 million. That's a saving of almost two million dollars per year for our setup! The reason it's more than
[our original estimate of $7 million over five years](https://world.hey.com/dhh/we-stand-to-save-7m-over-five-years-from-our-cloud-exit-53996caa)
is that we got away with putting all the new hardware into our existing data center racks and power limits.
The expenditure on
[all that new Dell hardware](https://world.hey.com/dhh/the-hardware-we-need-for-our-cloud-exit-has-arrived-99d66966)
– about $700,000 in the end – was also entirely recouped during 2023 while the long-term commitments slowly rolled off. Think about that for a second. This is gear we expect to use for the next five, maybe even seven years! All paid off from savings accrued during the second half of 2023. Pretty sweet!
But it's about to get sweeter still. The remaining $1.3 million we still spend on cloud services is all from AWS S3. While all our former cloud compute and managed database/search services were on one-year committed contracts, our file storage has been locked into a four(!!)-year contract since 2021, which doesn't expire until next summer. So that's when we plan to be out.
We store almost 10 petabytes of data in S3 now. That includes a lot of super critical customer files, like for Basecamp and HEY, stored in duplicate via separate regions. We use a mixture of storage classes to get an optimized solution that weighs reliability, access, and cost. But it's still well over a million dollars to keep all this data there (and that's after the big long-term commitment discounts!).
When we move out next summer, we'll be moving to a dual-DC
[Pure Storage](https://www.purestorage.com/)
setup, with a combined 18 petabytes of capacity. This setup will cost about the same as a year's worth of AWS S3 for the initial hardware. But thanks to the incredible density and power efficiency of the Pure flash arrays, we can also fit these within our existing data center racks. So ongoing costs are going to be some modest service contracts, and we expect to save another four million dollars over five years.
This brings our total projected savings from the combined cloud exit to well over ten million dollars over five years! While getting faster computers and much more storage.
Now, as with all things cloud vs on-prem, it's never fully apples-to-apples. If you're entirely in the cloud, and have no existing data center racks, you'll pay to rent those as well (but you'll probably be shocked at how cheap it is compared to the cloud!). And even for our savings estimates, the target keeps moving as we require more hardware and more storage as Basecamp and HEY continues to grow over the years.
But it's still remarkable that we're able to reap savings of this magnitude from leaving the cloud. We've been out for just over a year now, and the team managing everything is still the same. There were no hidden dragons of additional workload associated with the exit that required us to balloon the team, as some spectators speculated when we announced it. All the answers in our
[Big Cloud Exit FAQ](https://world.hey.com/dhh/the-big-cloud-exit-faq-20274010)
continue to hold.
It's still work, though! Running apps the size of
[Basecamp](https://basecamp.com/)
and HEY across two data centers (and soon at least one more internationally!) requires a substantial and dedicated crew. There's always work to be done maintaining all these applications, databases, virtual machines, and yes, occasionally, even requesting a power supply or drive swap on a machine throwing a warming light (but
[our white gloves at Deft](https://deft.com/)
take care of that). But most of that work was something we had to do in the cloud as well!
Since we originally announced
[our plans to leave the cloud](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)
, there's been a
[surge of interest](https://x.com/MichaelDell/status/1780672823167742135)
in doing the same across the industry. The motto of the 2010s and early 2020s – all-cloud, everything, all the time – seems to finally have peaked. And thank heavens for that!
The cloud can still make a lot of sense, though. Especially in the very early days when you don't even need a whole computer or are unsure whether you'll still be in business by the end of the year. Or when you're dealing with enormous fluctuations in load, like what motivated Amazon to create AWS in the first place.
But as soon as the cloud bills start to become substantial, I think you owe it to yourself, your investors, and common business sense to at least do the math. How much are we spending? What would it cost to buy these computers instead of renting them? Could we try moving some part of the setup onto our own hardware, maybe using
[Kamal](https://kamal-deploy.org/)
or a similar tool? The potential savings from these answers can be shocking.
At
[37signals](https://37signals.com/)
, we're looking forward to literally deleting our AWS account come this summer, but remain grateful for the service and the lessons we learned while using the platform. It's obvious why Amazon continues to lead in cloud. And I'm also grateful that it's
[now entirely free to move your data out of S3](https://aws.amazon.com/blogs/aws/free-data-transfer-out-to-internet-when-moving-out-of-aws/)
, if you're leaving the platform for good. Makes the math even better. So long and thanks for all the fish!
