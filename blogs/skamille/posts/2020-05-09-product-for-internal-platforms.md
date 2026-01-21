---
title: "Product for Internal Platforms"
date: 2020-05-09
url: https://www.elidedbranches.com/2020/05/product-for-internal-platforms.html
word_count: 2035
---

For the past 3 years, I have been running a platform engineering organization. Since that term is vague, where I work it means the software side of infrastructure. Compute platforms like kubernetes, storage systems, software development tools, and frameworks for services are part of the mandate. Our customers are other engineers at the company.
I also oversee the product team for this area. Now, I’m not a product manager (which I’ll shorten to PM for the rest of this post, not to be confused with project manager), and I rely on my PM team heavily for their expertise. But that doesn’t mean that I can personally neglect the product side, and indeed I spend a lot of time thinking about the products and strategy for my org as part of my day-to-day work.
These are some things I’ve observed and learned in this process. I share them with you because I think many folks in platform-type teams, especially engineers and those of you on platform teams without formal product managers, might benefit from understanding how to approach these problems.

## What’s so hard about product for (internal) platform?


### Customer Group Size

Platform product decision-making is something of a unique discipline. When many people think about product managers, the image that springs to mind is a product manager for large consumer-facing products. Metrics, metrics, metrics! A/B tests and user studies and KPIs and design sprints and revenue models. I’m sure that any time you are building products for a large user base, this is a factor, and PMs for AWS probably have a lot of metrics to guide them. But A/B testing for an audience of hundreds doesn’t usually teach you much. When you’re building platform for internal customers at a small-to-midsized company, a metrics-driven strategy is harder to apply.

### Captive Audience

Not only do we have a small group of customers, we have a captive audience. Other teams can and sometimes do decide to go off on their own and build their own platforms, but for many types of products, we provide the only option. You can ask customers what they want or how they like your products, but they may not want to complain to their colleagues. Of course, platform products also suffer from the problem that some engineers always think they could build something better, if only they had the time, so you also have a customer segment that seems to never be satisfied no matter how hard you work.
A captive audience leads us to believe that basic metrics for customer adoption are not interesting, which in turn leads us to ignore them, sometimes to our peril. Many platform teams end up with several overlapping half-finished products because they assumed a captive audience would lead to product success.

### It’s Hard To Think Like Your Customer

Finally, there is the universal challenge of platforms. Good software products for engineers tend to come from someone with a clear problem in front of them, who built specifically to solve that problem. They are intimately familiar with the customer because they are the customer. They are building for one person or one team, and they can clearly see what needs to be solved. But the platform team doesn’t build solutions for only one user. The whole value of a platform team is providing broadly-useful systems, so we are rarely presented with a well-specified need to fill.
When you are on a platform team, it is easy to lose the feel for what it is like to use your own products, because you are deep in the details. You spend your day living and breathing the ins and outs of git, and your users know the 3 commands they have to memorize and otherwise rely on ohshitgit to get themselves out of trouble. In a perfect world, platform product managers are regularly using the products they support in order to identify pain points and gaps that engineers might miss and users may not complain about. In the real world it’s hard to find time to use your products in anger when you are also dealing with all the other parts of the PM job.
You can observe this dilution of focus and quality in a lot of open source platform products that are created by big companies in order to sell you on their cloud solution or to create an industry standard. It starts look like software that is building to be built. And you absolutely see it in internal platform projects at companies big and small. When platform teams build to be building, especially when they have grand visions of complex end goals with few intermediary states, you end up with products that are confusing, overengineered, and far from beloved.

## So how do you solve this?

If the challenges can be summed up as: a small, captive audience, that is hard to truly empathize with, and a tendency to build thoughtlessly, what can you do? Here are a few approaches I’ve found to help:

### Assimilate and Expand

You don’t have a huge customer base to test things on, so how do you find a successful product? Don’t be ashamed to take over a system from a team that built it with themselves in mind, if that system seems to be the right general concept for the wider company. A lot of platform teams don’t like doing this, because they think that it means they will have to live with decisions that they don’t agree with. They forget that when you take a product from a team that built it, you already have a reasonably satisfied customer to start with! For better or worse, someone showed that they had a problem, and they solved it, and you wouldn’t be taking it over if you didn’t think this problem was worth solving in a holistic fashion, right?
I did this when I built a global service discovery solution long ago. Another team had first identified the problem and created their own version of a solution using ZooKeeper. The solution was fine for their needs, but didn’t solve the general needs of everyone at the company for global scaling. So I took over the idea of the project, and turned it into true platform infrastructure, built for a big company and not just one team therein. There were plenty of product decisions to make as part of that work, but the core identification of the problem as worth solving was done for me. There is a lot of interesting work in taking a solution that is locally-optimized and turning it into something that can be used by a diverse set of applications.

### Partner to Prototype

Another way to identify promising new opportunities is to partner with another team, and even embed someone into that team, to understand a problem better. Partner teams are likely to come by and ask if you are planning to build something to solve their various problems. When you believe that this is a good specific example of something that will become a general pattern, take advantage of this request to learn more! In fitting with the goal of really understanding the feel of a problem, having platform engineers build an application with a prototype idea for a platform within it, then using the lessons from that project to extract a more general system, is a productive way to quickly iterate an idea into something that is usable. After all, the hardest part of the product side of platform engineering is figuring out usability. Want to know how people will actually write code around this offering? Well, writing code around the offering yourself is a good way to figure that out.

### Make a Migration Strategy Early

In platform teams a lot of the product job is figuring out how to make open source products or popular strategies work for your company. Take kubernetes. The product challenges around internal kubernetes are in the decisions you make on how to integrate it into the existing ecosystem in order to get people to adopt it without too much argument. If you are a company of a certain age, you may already have an old private cloud solution running around. Everyone is used to running on VMs, but you think kubernetes will give you some operational improvements and also encourage the company to start to rethink its software practices to be a bit more modern.
That is all well and good, but the product work is not “tell everyone you have kubernetes now and they have to use it.” Instead, the product work is to identify different types of customers and figure out what will make it easy for them to migrate. What are the carrots you can provide to get people to do work that they don’t care about doing? Perhaps the carrots are efficiencies in getting access to compute or storage. Perhaps you can offer a higher SLO with the new product. Perhaps it is faster, more secure. But these things don’t just happen. You have to choose which features you are highlighting to your customers, you have to help them understand the offering and advantages, and you have to deliver on those promises.
Despite having captive audiences, platform teams are notorious for creating half-finished product offerings that somehow fail to get adopted. When your platform organization is running three different generations of solutions to the same problem with no clear plan to remove any of them, and your customers are both confused by the offerings and dissatisfied with them, you have a serious product failure on your hands. The migration strategy must be a primary part of the product planning.

### You Aren’t Google, So Don’t Build When You Don’t Have To

My final piece of product advice to platform teams is to remember that you aren’t Google (unless you are, in which case, hi!). When you have a platform team of 7, or even 100, you must be extremely thoughtful about what you choose to build. Platform teams of all sizes can get bogged down trying to imitate systems that have been built up over years at big companies. Even when those big companies provide their solutions as open source software, they often encode all kinds of assumptions about the surrounding ecosystem of available products and the culture and needs of the engineers using the product that may not work well in your company. It is not good product management to say “Google does it, therefore we should.”
Instead, start with a clear understanding of the problem, and an accounting of your existing ecosystem and culture, before diving into a technical solution. Your data volume is out of control. You might need to solve this with a better storage solution, or you might need to solve it by identifying the top data producers, and asking whether the data they’re storing is actually valuable. You’ll often find that the data is garbage, or the developers can change their workflow, or a little bit of query performance tuning makes this application scale just fine in a normal RDBMS. Only build when you have exhausted the alternatives.

## Summing Up

Great platform teams can tell a story about what they have built, what they are building, and why these products make the overall engineering team more effective. They have strong partner relationships that drive the evolution of the platform with focused offerings that meet and anticipate future needs of the rest of the company. They are admired as strong engineers who build what is needed, to high standards, and they are able to invest the time to do that because they don’t overbuild.
Whether you are a platform engineer, engineering manager, or PM, it pays to remember that you still need to be customer-focused and strategic about your platform offerings. Without a clear strategy for showing impact and value, you end up overlooked and understaffed, and no amount of cool new technology will solve that problem.
Thanks to my darling product and platform friends for their feedback on drafts, especially Renee and Pete.
Enjoy this post? You might like my book,
[The Manager’s Path](http://amzn.to/2nw1QN5)
, available on Amazon and Safari Online!