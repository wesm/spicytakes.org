---
title: "How Much Should My Observability Stack Cost?"
date: 2021-08-18
url: https://charity.wtf/2021/08/18/how-much-should-my-observability-stack-cost/
word_count: 881
---


*First posted on 2021-08-18 at *[*https://www.honeycomb.io/blog/how-much-should-my-observability-stack-cost*](https://www.honeycomb.io/blog/how-much-should-my-observability-stack-cost)


What should one pay for observability? What should your observability stack cost? What should be in your observability stack?


How much observability is enough? How much is too much, or is there such a thing?


Is it better to pay for one product that claims (dubiously) to do everything, or twenty products that are each optimized to do a different part of the problem super well?


It’s almost enough to make a busy engineer say “Screw it, I’m spinning up Nagios”.


(Hey, I said a*lmost.)*


All of these service providers can give you sticker shock when you begin investigating them. The biggest reason is always that we aren’t used to considering the price of our own time.  We act like it’s “free” to just take an hour and spin something up … we don’t count the cost of maintenance, context switching, and opportunity costs of not using the time to build something of business value.  Which is both understandable and forgivable, as a starting point.


Considerably less forgivable is the vagueness–and sometimes outright misdirection and scare tactics–some vendors offer around pricing. It’s not ok for a business to optimize for revenue at the expense of user experience. As users, we have the right to demand transparency and accurate information.  As vendors, we have the responsibility to provide it.  Any pricing scheme that doesn’t align with best practices and users’ interests will be a drag on reputation and growth.


The core question, rarely addressed outright, is: **how much *should* you pay?** In this post I’ll talk about what your observability costs include, and in the next post, what you should consider including in your “observability stack”.


But I’ll give you the answer to your question right off the bat: you should probably spend 20-30% of infra costs on observability.


## O11y spend should be 20-30% of infra spend


Rule of thumb: your observability spend should come to 20-30% of your infra spend. (I’ve seen 10% a few times from reasonable-seeming shops, but they have been edge cases and outliers. I have also seen 50% or more, but again, outliers.)


Full disclosure: this isn’t based on any particular science.  It’s just based on my experience of 15+ years working in operations engineering, talking to other engineers and managers, and a couple of informal Twitter polls to satisfy my own curiosity.


Nevertheless, it’s a pretty solid rule. There are exceptions, but in general, if you’re spending less than 20%, you’re “saving money” at the expense of engineering time, or being silently dragged underwater by a million little time leaks and quality of service issues — which you could eliminate completely with a bit of investment.


Consider the person who told me proudly that his o11y spend was just 1-3%. (He meant the PagerDuty bill and Pingdom checks, actually.) He wasn’t counting the dedicated hardware for their ELK cluster (80k/month), or the 2-3 extra engineers they had to recruit, train and hire (250-300k/year apiece) to run the many open source tools they got for “free”.


And ultimately, it didn’t meet their needs very well. Few people knew how to use it, so they leaned on the “observability team” to craft custom views, write scripts and ETL one-offs, and serve as the institutional hive mind and software usability tutors.  They could have used better tools, ones under active development by large product teams.  They could have used that headcount to create core business value instead.


## Engineers cost money


Engineers are expensive. Recruiting them is hard. The good ones are increasingly unwilling to waste time on unnecessary labor. This manager was “saving” maybe a million dollars a year (he mentioned a vendor quote of less than 100k/month)–but spending a couple million *more* than that in less-visible ways.


Worse, he was driving his engineering org into the ground by wasting so much of their time and energy on non-mission-critical work, inferior tooling, one-offs, frustrating maintenance work, etc, *all of which had nothing to do with their core business value.*


If you want to know if an org hires and retains good engineers, you could do worse than to ask the question: “What tools do you use, and why?”

- Good orgs use good tools. They know engineering cycles are their scarcest and most valuable resource, and they want to train maximum firepower on their core business problems.
- Mediocre orgs use mediocre tools, have no discipline or consistency around adoption and deprecation, and leak lost engineering cycles everywhere.


So back to our rule of thumb: observability amounting to 20-30% of total spend is where most shops should fall. This refers to cloud-native infrastructure, using third-party services to instrument and monitor code, with the basics covered — resource utilization graphs, end to end checks, paging, etc.


## So, what do I need in my “observability stack”?


What are the basics? Well, obviously “it depends”. It depends on your requirements, your components, your commitments, your budget, sunk costs and skill sets, your teams, and most expensive of all — customer expectations and the cost of violating them. You should think carefully about these things and try to **draw a straight line** from the business case to the money you spend (or don’t spend). And don’t forget to factor in those invisible human costs.
