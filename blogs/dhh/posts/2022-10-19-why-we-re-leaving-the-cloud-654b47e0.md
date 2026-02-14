---
title: "Why we're leaving the cloud"
date: 2022-10-19
url: https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0
slug: why-we-re-leaving-the-cloud-654b47e0
word_count: 1016
---

[Basecamp](https://www.basecamp.com/)
has had one foot in the cloud for
[well over a decade](https://signalvnoise.com/posts/947-fun-with-stats-the-s3-edition)
, and
[HEY](https://www.hey.com/)
has been running there exclusively since it was launched two years ago. We've run extensively in both Amazon's cloud and Google's cloud. We've run on bare virtual machines, we've run on Kubernetes. We've seen all the cloud has to offer, and tried most of it. It's finally time to conclude: Renting computers is (mostly) a bad deal for medium-sized companies like ours with stable growth. The savings promised in reduced complexity never materialized. So we're making our plans to leave.
The cloud excels at two ends of the spectrum, where only one end was ever relevant for us. The first end is when your application is so simple and low traffic that you really do save on complexity by starting with fully managed services. This is the shining path that Heroku forged, and the one that has since been paved by
[Render](https://render.com)
and others. It remains a fabulous way to get started when you have no customers, and it'll carry you quite far even once you start having some. (Then you'll later be faced with a Good Problem once the bills grow into the stratosphere as usage picks up, but that's a reasonable trade-off.)
The second is when your load is highly irregular. When you have wild swings or towering peaks in usage. When the baseline is a sliver of your largest needs. Or when you have no idea whether you need ten servers or a hundred. There's nothing like the cloud when that happens, like we learned when launching HEY, and suddenly 300,000 users signed up to try our service in three weeks instead of our forecast of 30,000 in six months.
But neither of those two conditions apply to us today. They never did for Basecamp. Yet by continuing to operate in the cloud, we're paying an at times almost absurd premium for the possibility that it could. It's like paying a quarter of your house's value for earthquake insurance when you don't live anywhere near a fault line. Yeah, sure, if somehow a quake two states over opens the earth so wide it cracks your foundation, you might be happy to have it, but it doesn't feel proportional, does it?
Let's take HEY as an example. We're paying over half a million dollars per year for database (RDS) and search (ES) services from Amazon. Yes, when you're processing email for many tens of thousands of customers, there's a lot of data to analyze and store, but this still strikes me as rather absurd. Do you know how many insanely beefy servers you could purchase on a budget of half a million dollars per year?
Now the argument always goes: Sure, but you have to manage these machines! The cloud is so much simpler! The savings will all be there in labor costs! Except no. Anyone who thinks running a major service like HEY or Basecamp in the cloud is "simple" has clearly never tried. Some things are simpler, others more complex, but on the whole, I've yet to hear of organizations at our scale being able to materially shrink their operations team, just because they moved to the cloud.
It was a wonderful marketing coup, though. Sold with analogies like "well you don't run your own powerplant either, do you?" or "are infrastructure services really your core competency?". Then lathered up with a thick coat of NEW-NEW-NEW paint, and The Cloud has beamed so brightly only the luddites would consider running their own servers in its shadow.
Meanwhile Amazon in particular is
[printing profits](https://www.computerweekly.com/news/252512961/AWS-vs-Amazon-Cloud-giants-revenue-rises-as-parent-companys-profit-falls-during-Q4)
renting out servers at obscene margins. AWS' profit margin is almost 30% ($18.5b in profits on $62.2B in revenue), despite huge investments in future capacity and new services. This margin is bound to soar now that "the firm said it plans to extend the useful life of its servers from four years to five, and its networking equipment from five years to six in the future".
Which is fine! Of course it's expensive to rent your computers from someone else. But it's never presented in those terms. The cloud is sold as computing on demand, which sounds futuristic and cool, and very much not like something as mundane as "renting computers", even though that's mostly what it is.
But this isn't just about cost. It's also about what kind of internet we want to operate in the future. It strikes me as downright tragic that this decentralized wonder of the world is now largely operating on computers owned by a handful of mega corporations. If one of the primary AWS regions go down, seemingly half the internet is offline along with it. This is not what DARPA designed!
Thus I consider it a duty that we at 37signals do our part to swim against the stream. We have a business model that's incredibly compatible with owning hardware and writing it off over many years. Growth trajectories that are mostly predictable. Expert staff who might as well employ their talents operating our own machines as those belonging to Amazon or Google. And I think there are plenty of other companies in similar boats.
But before we more broadly can set sail back towards lower-cost and decentralized shores, we need to turn rudder of our collective conversation away from the cloud-serving marketing nonsense about running your own powerplant. Up until very recently, everyone ran their own servers, and much of the progress in tooling that enabled the cloud is available for your own machines as well. Don't let the entrenched cloud interests dazzle you into believing that running your own setup is too complicated. Everyone and their dog did it to get the internet off the ground, and it's only gotten easier since.
It's time to part the clouds and let the internet shine through.
*Want to know more about how, why, and when we're leaving the cloud? Checkout the*
[Leaving the cloud](https://www.rework.fm/leaving-the-cloud/)
*episode of the REWORK podcast where I discuss all of this with Eron, our Director of Operations, together with our host Kimberly.*
