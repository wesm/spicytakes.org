---
title: "Only 15% of the Basecamp operations budget is spent on Ruby"
date: 2019-12-18
url: https://signalvnoise.com/svn3/only-15-of-the-basecamp-operations-budget-is-spent-on-ruby/
slug: only-15-of-the-basecamp-operations-budget-is-spent-on-ruby
word_count: 616
---


We spend about $3 million every year to run all the versions of Basecamp and our legacy applications. That spend is spread across several on-premise data centers and cloud operations. It does not include the budget for our 7-person strong operations team, this is just the cost of connectivity, machines, power, and such.


There’s a lot of spend in that bucket. The biggest line item is the million dollars per year we spend storing 4.5 petabyte worth of files. We used to store these files ourselves, across three physical data centers for redundancy and availability, but the final math and operational hassle didn’t pan out. So now we’re just on S3 with a multi-region redundancy setup.


After that, it’s really a big mixed bag. We spend a lot of money on databases, which all run on MySQL. There’s ElasticSearch clusters that power our search. A swarm of Redis servers providing caching. There’s a Kafka pipeline and a Big Query backend for analytics. We have our own direct network connections between the data centers and the cloud.


Everything I’ve talked about so far is infrastructure we’d run and pay for regardless of our programming language or web framework. Whether we run on Python, PHP, Rust, Go, C++, or whatever, we’d still need databases, we’d still need search, we’d still need to store files.


So let’s talk about what we spend on our programming language and web framework. It’s about 15%. That’s the price for all our app and job servers. The machines that actually run Ruby on Rails. So against a $3 million budget, it’s about $450,000. That’s it.


Let’s imagine that there was some amazing technology that would let us do everything we’re doing with Ruby on Rails, but it was TWICE AS FAST! That would save us about ~$225,000 per year. We spend more money than that on the Xmas gift we give employees at Basecamp every year. And that’s if you could truly go twice as fast, and thus require half the machines, which is not an easy thing to do, despite what microbenchmarks might delude you into thinking.


Now imagine we found a true silver bullet. One where the compute spend could be reduced by an order of magnitude. So we’d save about $400,000/year, reducing everything we spend running our app and job servers to an unrealistically low $45,000/year. That reduction wouldn’t even pay for two developers at our average all-in cost at Basecamp!


Now let’s consider the cost of those savings. We spend more money on the 15-strong developer team at Basecamp than our entire operations budget! If we make that team just 15% less productive, it’ll cost us more than everything we spend to run Ruby and Rails at Basecamp!


Working with Ruby and Rails is a luxury, yes. Not every company pay their developers as well as we do at Basecamp, so maybe the rates would look a little different there. Maybe some companies are far more compute intensive to run their apps. But for most SaaS companies, they’re in exactly the same ballpark as we are. The slice of the total operations budget spent running the programming language and web framework that powers the app is a small minority of the overall cost.


For a company like Basecamp, you’d be mad to make your choice of programming language and web framework on anything but a determination of what’ll make your programmers the most motivated, happy, and productive. Whatever the cost, it’s worth it. It’s worth it on a pure cost/benefit, but, more importantly, it’s worth it in terms of human happiness and potential.


This is why we run Ruby. This is why we run Rails. It’s a complete bargain.

