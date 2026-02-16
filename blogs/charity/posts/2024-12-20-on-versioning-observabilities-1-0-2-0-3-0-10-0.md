---
title: "On Versioning Observabilities (1.0, 2.0, 3.0…10.0?!?)"
date: 2024-12-20
url: https://charity.wtf/2024/12/20/on-versioning-observabilities-1-0-2-0-3-0-10-0/
word_count: 2008
---


[Hazel Weakly, you little troublemaker. ](https://hazelweakly.me/blog/the-future-of-observability-observability-3-0/)


As I whined to Hazel over text, after she sweetly sent me a preview draft of her post: “PLEASE don’t post this! I feel like I spend all my time trying to help bring clarity and context to what’s happening in the market, and this is NOT HELPING. Do you *know* how hard it is to try and socialize shared language around complex sociotechnical topics? Talking about ‘observability 3.0’ is just going to *confuse everyone*.”


That’s the problem with the internet, really; the way any asshole can go and name things (she said piteously, self-righteously, and with an astounding lack of self-awareness).


## Semantic versioning is cheap and I kind of hate it


I’m complaining, because I feel sorry for myself (and because Hazel is a dear friend and can take it). But honestly, I actually kind of loathe the 1.0 vs 2.0 (or 3.0) framing myself. It’s helpful, it has explanatory power, I’m using it…but you’ll notice we aren’t slapping “Honeycomb is Observability 2.0” banners all over the website or anything.


Semantic versioning is a cheap and horrendously overused framing device in both technology and marketing. And it’s cheap for exactly these reasons…it’s too easy for anyone to come along and bump the counter again and say it happens to be because of whatever fucking thing they are doing.


I don’t love it, but I don’t have a better idea. In this case, the [o11y 2.0 language](https://charity.wtf/2024/08/07/is-it-time-to-version-observability-signs-point-to-yes/) describes a real, backwards-incompatible, behavioral and technical generational shift in the industry. This is not a branding exercise in search of technological justification, it’s a [technical sea change](https://www.thoughtworks.com/en-us/radar/techniques/observability-2-0) reaching for clarification in the market.


One of the most exciting things that happened this year is that all the new observability startups have suddenly stopped looking like cheaper Datadogs (three pillars, many sources of truth) and started looking like cheaper Honeycombs (wide, structured log events, single source of truth, [OTel-native](https://www.honeycomb.io/resources/the-directors-guide-to-o11y), usually Clickhouse-based). As an engineer, this is so fucking exciting.


(I should probably allow that these technologies have been available for a long time; adoption has accelerated over the past couple of years in the wake of the ZIRP era, as the [exploding cost multiplier](https://www.honeycomb.io/resources/cost-crisis-metrics-tooling) of the [three pillars model](https://www.honeycomb.io/blog/cost-crisis-observability-tooling) has become unsustainable for more and more teams.)


## Some non-controversial “controversial claims”


> Firstly, I’m going to make a somewhat controversial claim in that you can get observability 2.0 just fine with “observability 1.0” vendors. The only thing you need from a UX standpoint is the ability to query correlations, which means any temporal data-structure, decorated with metadata, is sufficient.”


This is not controversial at all, in my book. You can get most of the way there, if you have enough time and energy and expertise, with 1.0 tooling. There are exceptions, and it’s really freaking hard. If all you have is aggregate buckets and random exemplars, your ability to slice and dice with precision will be dramatically limited.


This matters a lot, if you’re trying to e.g. break down by any combination of feature flags, build IDs, canaries, user IDs, app IDs, etc in an exploratory, open-ended fashion. As Hazel says, the whole point is to “develop the ability to ask meaningful questions, get useful answers, and act effectively on what you learn.” A-yep.


However, any time your explanation takes more than 30 seconds, you’ve lost your audience. This is at least a three-minute answer. Therefore, I typically tell people they need [structured log events](https://jeremymorrell.dev/blog/a-practitioners-guide-to-wide-events/).


## “[Observability 2.0](https://www.honeycomb.io/blog/time-to-version-observability-signs-point-to-yes)” describes a sociotechnical sea change that is already well underway


Let’s stop talking about engineering for a moment, and talk about product marketing.


A key aspect of product marketing is simplification. That’s where the 2.0 language grew out of. About a year ago I started having a series of conversations with CTOs and VPEngs. All of them are like, “we already have observability, how is Honeycomb any different?” And I would launch off into a laundry list of features and capabilities, and a couple minutes later you see their eyes glazing over.


You have to have some way of boiling it down and making it pithy and memorable. And any time you do that, you lose some precision. So I actually disagree with very little Hazel has said in this essay. I’ve made most of the same points, in various times and places.


Good product marketing is when you take a strong technical differentiator and try to find evocative, resonant ways of making it click for people. Bad product marketing — and oh my god is there a lot of that — is when you start with the justification and work backwards. Or start with “well we should create our own category” and then try to define and defend one for sales purposes.


Or worst of all — “what our competitors are saying seems to be really working, but building it would take a long time and be very hard, so what if we just say the same words out loud and confuse everyone into buying our shit instead?”


(Ask me how many times this has happened to us, I fucking dare you.)


## Understanding your software in the language of your business


Here’s why I really hate the 3.0 framing: I feel like all the critical aspects that I really really care about are already part of 2.0. They *have* to be. It’s the whole freaking point of the generational change which is already underway.


We aren’t just changing data structures for the fun of it. The whole *point* is to be able to ask better questions, as Hazel correctly emphasizes in her piece.


Christine and I recently rewrote our company’s mission and vision. Our new vision states:


> **Understand your software in the language of your business.**
> Decades on, the promise of software and the software industry remains unfulfilled. Software engineering teams were supposed to be the innovative core of modern business; instead they are order-takers, cost centers, problem children. Honeycomb is here to shape a future where there is no divide between building software and building a business — a future where software engineers are truly the innovation engine of modern companies.


The beauty of high cardinality, high dimensionality data is that it gives you the power to pack dense quantities of application data, systems data, and business data all into the same blob of context, and then explore all three together.


[Austin Parker wrote about this](https://aparker.io/2024/03/re-redefining-observability/) earlier this year (ironically, in response to yet another of [Miss Weakly’s articles on observability](https://hazelweakly.me/blog/redefining-observability/)):


> Even if you’ve calculated the cost of downtime, you probably aren’t really thinking about the relationship between telemetry data and business data. Engineering stuff tends to stay in the engineering domain. Here’s some questions that I’d suggest most people can’t answer with their observability programs, but are **absolutely fucking fascinating questions **(emphasis mine):
> What’s the relationship between system performance and conversions, by funnel stage? Break it down by geo, device, and intent signals.
> What’s our cost of goods sold per request, per customer, with real-time pricing data of resources?
> How much does each marginal API request to our enterprise data endpoint cost in terms of availability for lower-tiered customers? Enough to justify automation work?


Every truly interesting question we ask as engineers is some combination or intersection of business data + application data. We do no one any favors by chopping them up and siloing them off into different tools and data stores, for consumption by different teams.


## Data lake ✅, query flexibility ✅, non-engineering functions…🚫


Hazel’s three predictions for what she calls “observability 3.0” are as follows:


> Observability 3.0 backends are going to look a lot like a data lake-house architecture
> Observability 3.0 will expand query capabilities to the point that it mostly erases the distinction between pay now / pay later, or “write time” vs “read time”
> Observability 3.0 will, more than anything else, be measured by the value that non-engineering functions in the business are able to get from it


I agree with the first two — in fact, I think that’s exactly the trajectory that we’re on with 2.0. We are moving fast and accelerating in the direction of data lakehouse architectures, and in the direction of fast, flexible, and cheap querying. There’s nothing backwards-incompatible or breaking about these changes from a 2.0 -> 3.0 perspective.


Which brings us to the final one. This is the only place in the whole essay where there may be some actual daylight between where Hazel and I stand, depending on your perspective.


## Other business functions already have nice things; we need to get our own house in order


No, I don’t think success will be measured by non-engineering functions’ ability to interrogate our data. I think it’s the opposite. I think it is *engineers* who need to integrate data about the business into our own telemetry, and get used to using it in our daily lives.


They’ve had nice things on the business side for years — for decades. They were rolling out columnar stores for business intelligence almost 20 years ago! Folks in sales and marketing are used to being able to explore and query their business data with ease. Can you even *imagine* trying to run a marketing org if you had to pre-define cohorts into static buckets before you even got started?


No, in this case it’s actually engineering that are the laggards. It’s a very “the cobbler’s children have no shoes” kind of vibe, that we’re still over here warring over cardinality limits and pre-defined metrics and trying to wrestle them into understanding our massively, sprawlingly complex systems.


So I would flip that entirely around. **The success of observability 2.0 will be measured by how well engineering teams can understand their decisions and describe what they do in the language of the business.**


Other business functions already have nice tools for business data. What they don’t have — can’t have — is observability that integrates systems and application data in the same place as their business data. Uniting all three sources, that’s on us.


## If every company is now a technology company, then technology execs need to sit at the big table


Hazel actually gets at this point towards the end of her essay:


> We’ve had multiple decades as an industry to figure out how to deliver meaningful business value in a transparent manner, and if engineering leaders can’t catch up to other C-suites in that department soon, I don’t expect them to stick around another decade


The only member of the C-suite that has no standard template for their role is…CTO. CTOs are all over the freaking map.


Similarly, VPs of Engineering are usually not part of the innermost circles of execs.


Why? Because the point of that inner circle of execs is to **co-make and co-own** all of the decisions at the highest level about where to invest the company’s resources.


And engineering (and product, and design) usually can’t explain their decisions well enough in terms of the business for them to be co-owned and co-understood by the other members of the exec team. R&D is full of the *artistes* of the company. We tell you what we think we need to do our jobs, and you either trust us or you don’t.


(This is not a one-way street, of course; the levers of investment into R&D are often opaque, counter-intuitive and poorly understood by the rest of the exec team, and they *also* have a responsibility to educate themselves well enough to co-own these decisions. I always recommend these folks start by reading “[Accelerate](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339)”.)


But twenty years of free money has done poorly by us as engineering leaders. The end of the ZIRP era is the best thing that could have happened to us. It’s time to get our house in order and sit at the big table.


“Know your business, run it with data”, as Jeff Gray, our COO, often says.


Which starts with having the right tools.


~charity
