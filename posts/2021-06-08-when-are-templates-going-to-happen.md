---
title: "When are templates going to happen?"
subtitle: "Do you get deja vu? From trading dashboards, laughing about how small they look on you?"
date: 2021-06-08T19:11:59+00:00
url: https://benn.substack.com/p/when-are-templates-going-to-happen
slug: when-are-templates-going-to-happen
word_count: 1810
---


![](https://substackcdn.com/image/fetch/$s_!roTT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Facec5c36-df63-455d-af3c-648ad3b018d1_640x320.jpeg)

*Templates are so fetch.*


Every six months or so, I have the same conversation I’ve been having for the past seven years. I’m talking with someone about some new data technology or trend, and we notice that whatever we’re talking about is making data more standardized. Years ago, we were all consolidating around the same SaaS apps to manage our businesses. Then we started using the same event tracking frameworks like Segment, and the same ELT tools like Fivetran and Stitch. More recently, we’re adopting similar conventions for modeling data with dbt. With each new development,we say knowingly, our data starts to look more like everyone else’s.


Our businesses are starting to look the same too. We were all tech companies, then we were all internet companies, and now we’re SaaS companies.1


This, it seems, presents an obvious opportunity for both thelazy data analystand the entrepreneur: We should turn our reports and dashboards into reusable templates.


Today, you can set up an entire data stack in a day.2But companies still have to build their own reporting on top of that stack. Even though our data is the same, and our companies are the same, there’s no one-click way to spin out an entire suite of dashboards. We have to build it all ourselves.


If we had community templates for common business concerns, like tracking ad performance, product usage, or SaaS metrics, data teams would no longer have to develop custom versions of the same dashboards everyone else is building. Moreover—and this is when we get really excited—templates could become their own standard. If you buildthereport for measuring support performance, everyone will want to make their products compatible with your dashboard.


Not only does it sound possible, it sounds inevitable. And yet...it hasn’t happened. These dynamics have been the same for nearly a decade, and I’m not aware of a single canonical template like this, or even a popular one. Why hasn’t this happened yet?


One possible answer is that templates are just a hard product to get right. A dashboard isn’t a bunch of text that you can just copy from a webpage. It has to be deployed between your data and a BI tool (or inside the BI tool). Maybe all that’s missing is a way around those logistical obstacles.


It’s also possible that modern data tools are still too fragmented for templates to quite fit. General patterns are popular—SaaS service to ELT to warehouse to transformation to BI—but there are a lot of combinations of vendors in that architecture. That makes it difficult for one template—say, one that works with Stitch, Snowflake, dbt, and Mode—to develop any real gravity. If things consolidate further, we’ll get there.


But there’s a third explanation that I’m partial to: Templates just don’t work.


# When everything is the same, we’re defined by our differences


At Mode, we use Salesforce, like everyone else. Salesforce is our source of truth for customer contracts, as it is for everyone else. We use Stitch and Fivetran to copy Salesforce data into Snowflake, like everyone else. And we're a B2B SaaS business, like everyone else. So why can't we just plug an ARR template on top of a couple Salesforce tables, and have all of the financial reporting we need?


Because we use Salesforce in a way that's specific to our business—like everyone else. We have to decide how to represent multi-year contracts and trials in Salesforce. We have to decide how to represent people, sales opportunities, and companies. We have to decide, when we sell contracts to the subsidiaries of a parent company, if we represent those deals as opportunities on the same account, or on separate accounts. We have to decide if off-cycle upsells are recorded as a new opportunity, or an update to an existing one.


These choices aren’t dictated by data engineering principles or analytical hygiene; they’re modeled after how we sell. Upsells, for example, follow a particular sales motion, determined by the dynamics of how Mode is adopted, how teams budget for it, and how our sales team is equipped to sell it. The bespoke elements of our Salesforce data that distinguish it from that of other B2B SaaS businesses aren’t analytical blemishes to be polished off of a template that just sums the “amount” field on every Salesforce opportunity. They are the foundations of our business.


This is why templates are flawed. The core assumption behind them is that everyone's data is mostly the same, and everyone's business problems are mostly the same. There are differences, sure, but those differences are relatively few and relatively small.


Half of this is true. There are relatively few differences; most people use tools like Salesforce in overwhelmingly similar ways. The problem, however, is that people introduce distinctions for a reason—to capture that which is unique about their business. It’s like a set of golf clubs: From a distance, the differences between a 5 iron and a 9 iron are minuscule—just a few degrees of club head tilt and a couple inches of length. But those differences are the very things that define each club as that club.


This issue exists across nearly every domain a data team works in. Tracking product analytics via Segment? Some companies only have a web client. Some only have mobile clients. Some only have a mobile client for iOS.3Some have mobile clients that are really just web clients. Some have desktop clients. Some, like Substack, are mostly consumed as emails. And some, like Segment itself, have a web client that’s used for intermittent configuration, and most activity in the product happens as interactions between servers, with no humans involved. A daily active user template is useless if everyone defines both activity and users differently.


Want to measure support performance via Intercom? Do you provide 24/7 support, or just during business hours? When are your business hours? Do you use Intercom to proactively reach out to prospects, like some companies do, or exclusively for reactive support? Do agents use it to chat live with customers, to triage email, or both? A generic definition of initial response time makes no sense unless these very fundamental differences are accounted for.


Importantly, more data standardization doesn't help solve these problems. The schemas are already standardized, as are the ELT tools that ingest them. The problem is that, across different companies, a Salesforceopportunitiestable, a Segmentpagestable, and an Intercomconversationstable don't represent the same concepts.


In other words, the shared foundation that templates are supposed to be built on is often only name deep.


# Success is business specific


This is only half the problem. Even if every table represented the same concept across every business—if every company used the same Salesforce model, or instrumented their Segment tracking scheme in exactly the same way—the metrics businesses care about are still different.


Take Slack and Microsoft Teams, two products that are as seemingly identical as products can be. Even Teams’ adsare clones of Slack’s. If there was ever a time for a template, this is it.


But it still doesn’t work. Slack is (so far, still) sold as a standalone product that’s marketed, above all, as a new way to communicate that's faster than email. Teams isbundled with other Office 365 services, including Word, Excel,and Outlook.


![](https://substackcdn.com/image/fetch/$s_!I44y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa91e5f3c-c95b-47fa-aeac-c4ce92f4a5cc_3480x1378.jpeg)

*Definitely not email.*


Despite being nearly indistinguishable services, Teams and Slack almost certainly measure their success in very different ways. Slack, which wants you to live in Slack,emphasizes how much time people spend in Slack. Teams, by contrast, wants you to live anywhere in Office 365, including Outlook. Consequently, Teams promotes “Microsoft 365 daily collaboration minutes,” which tracks engagement across all Office products. Rather than optimizing user time in Teams, Microsoft could prefer the opposite: get people out of Teams and into services like Word or Powerpoint where "real work" gets done—and, I suspect, Microsoft’s real money gets made.


# Will templates ever happen?


I'm skeptical, though I think there’s one approach that still has some hope.


Today, most templates extrapolate semantic meaning from standard source tables. They assume, for example, that the Salesforceopportunitiestable represents contracts in some sort of conventional way. A better method—which is similar to the one taken byNarrator—may be to invert this: ask for meaning, and tell people to provide a table that matches it.


This type of template could require an opportunity-like table as an input. Rather than sitting on top of a raw table, the template would ask for a derived table that meets a required set of parameters: one row per customer, include a contract start date and end date, how much the customer is paying you, and other relevant fields.


This isn’t as punchy as a template that works in one click. Somebody has to translate your schema into the template’s schema. Plus, it doesn’t doesn’t solve the problem of different businesses needing different metrics. But mapping existing data into new tablesis already how analysts work. And within certain domains like finance, where reporting is more rigid and metrics have commonly accepted definitions, formulaic templates may have a place.


Or maybe not—a couple years ago, I got caught up in a moment about templates myself. I built acollection of templates, using this same approach, for the typical finance metrics VCs want to see when they’re evaluating a startup.4


My templates, like every effort before them, didn’t take off. It could be thatI’m a bad marketer. Or it could be a sign that we need tostop trying to make templates happen.

[1](https://benn.substack.com/p/when-are-templates-going-to-happen#footnote-anchor-1-37347490)

As a petty aside, has there ever been a less artfully worded ethos than “software is eating the world?” Not only is it a clumsy phrase, it’s also a bizarre metaphor. It suggests that software is a toxic parasite devouring a healthy host, like “extremists are eating the party” or “TikTok is eating my brain”—which is, presumably, not the intended connotation for the motto of a VC firm that invests mostly in software companies. And there are so many better options! You could actually match the verb to the nouns, with “The world runs on software.” You could come up with a more elegant metaphor, like “Humanity is becoming hardware.” Even if you’re married to “eating” for some inexplicable reason, there’s an obvious alliterative alternative in “Software is eating the earth.” Or, I guess, you could abandon the whole thing and replace it with a line that could’ve been pulled from an awkward press conference for Chuck Schumer to half-heartedly promote another doomed infrastructure bill to a couple dozen Capitol Hill beat reporters: “It’s time to build.” (Ok, nope, stillall in on eating.)

[2](https://benn.substack.com/p/when-are-templates-going-to-happen#footnote-anchor-2-37347490)

Do it live!

[3](https://benn.substack.com/p/when-are-templates-going-to-happen#footnote-anchor-3-37347490)

Not that I’m bitter about anything related to that.

[4](https://benn.substack.com/p/when-are-templates-going-to-happen#footnote-anchor-4-37347490)

These templates were created for a talk I gave on how you can use data to raise money. Theslidesand avideo(if you’re having trouble sleeping) from that talk are both available as well.
