---
title: "Lock In Cost"
description: "In my recent client engagement, I foresaw that serverless architecture was   a perfect fit. The idea of adopting serverless architecture, though, didn’t   fly to our client well due to the fear of ven"
date: 2019-03-05T00:00:00
tags: ["project planning", "application architecture"]
url: https://martinfowler.com/bliki/LockInCost.html
slug: LockInCost
word_count: 567
---


In my recent client engagement, I foresaw that serverless architecture was
  a perfect fit. The idea of adopting serverless architecture, though, didn’t
  fly to our client well due to the fear of vendor lock-in. It was an
  interesting time for retailers as staying in AWS might mean that Amazon, as
  another retail business, will be given a competitive advantage. Given the idea
  of not supporting a competitor, my client was interested to ensure that the
  solution chosen by us is fully portable to other cloud vendors.


From a technical perspective, ensuring that we have the ability to move our
  system from one platform to another is definitely desirable. With the advent
  of containerization, why would one be interested to be locked in a specific
  platform? A high lock-in cost is not something that we would like to show back
  to the business when we have decided to move another platform. We, therefore,
  need to make sure that the migration cost is as low as possible when this
  scenario happens. If I’m about to make a simple formula for lock-in cost with
  our current understanding, it would look like this:


**Lock-in cost = Migration cost (?)**


This formula is correct when we are looking at it only from a technical
  perspective. A business perspective, however, should not be overlooked.
  Remember that the technical solutions we deliver are always designed to solve
  business problems. Most of the times the business get a benefit when a
  particular technology is adopted. One of the significant benefits is a faster
  time to market. Faster time to market can be formulated into opportunity
  gain:


**Lock-in cost = Migration cost - Opportunity gain**


Opportunity gain is very difficult to measure because you are dealing with
  an unknown unknown. Migration cost can be analyzed and reasoned. Opportunity
  gain, in contrast, is not as easy to analyze. You can theorize and analyze how
  to migrate from one platform to another, but how would you calculate the gain
  of seizing your competitors’ market opportunity? By looking at your
  decision-making process from a holistic view, combining both the technical and
  business perspective, the lock-in decision you are taking might result in a
  profit.


Let’s have a look into an example of building an event-driven architecture.
  You will need to choose a distributed messaging system in the architecture. If
  you are already chosen AWS as your platform, you would have the option of
  vendor-specific services like Kinesis. These services are fully managed and
  you can get it running in no time, hence giving you an opportunity gain. In
  comparison with a vendor-agnostic system like Kafka, these vendor-specific
  services will incur a higher migration cost. Setting up your own distributed
  messaging system, however, will take more time to harden and for it to be
  made production ready, especially when you are not experienced in building
  such platform yet. Instead of looking at your decision from just migration
  cost, focus on how you can reduce the migration cost by making your system
  more adaptable. Especially in this example of using a cloud, this is
  a similar reason on why we recommend to avoid the practice of
  [
  generic cloud usage.](https://www.thoughtworks.com/radar/techniques/generic-cloud-usage)


## Acknowledgements


Thanks to Chris Ford, Matt Newman, Luciano Ramalho, Tobias Vogel, Zhamak Dehghani, Kitson Kelly, and Peter Gillard-Moss
 for their inputs.


Special thanks to Martin Fowler for his support, suggestions, and time spent with the content and help with publishing.
