---
title: "If data is a product, what is production?"
subtitle: "We can’t build something unless we know what it is."
date: 2022-09-09T16:05:12+00:00
url: https://benn.substack.com/p/what-is-production
slug: what-is-production
word_count: 2029
---


![](https://substackcdn.com/image/fetch/$s_!-HSf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3164af5-f7ee-4cc6-bcd2-8728fae98a12_899x598.png)

*An “ad hoc” traffic patternin San Francisco.*


We did it, y’all—the “data as a product” hype cycle is officially complete. Over the last few years, the idea rocketed through thematurity curve, starting somewhere unknown, made its wayonto Medium, and graduated topopular talkat a popular conference before eventually coalescing into aseminal blog post. People wroteexplainersabout it; other peoplewrote explainers to summarize the explainers. Vendorscreated guideswithunique, accurate page titlesand many frequently-searched keywords. Thecriticspublishedcontrarian takes. And now, in the inevitable closing phase, the once-novel proposal—that data teams should think like product teams—jumped the final corporate shark:McKinsey wrote a report about it.1


Still, I’m glad the idea had its moment. As useful as it is for data teams to learn from engineering departments, they’re animperfect guide. Sourcing inspiration from product teams (anddesign teams, andsupport teams) surely makes for a better collection of best practices than getting all of our ideas from one place.


But before the concept of data as a product retires to its final sterile form—co-opted for a Teradata billboard on the 101 or for the vision statements of a dozen YC applications, presumably—I’d like to slip one last thought in under the deadline: If data is a product, we should have a better definition of production.


# Everything, everywhere, all at once


When companies create a product like a website, or a car, or a movie, it’s usually pretty straightforward to define what’s in production and what isn’t. It’s the website that people on the internet use; it’s the mass-produced car that people drive off the lot; it’s the sequence of pictures and sounds that people see when they’re in the theater. Though various things might get worked on that don’t make the final cut—features that bomb in internal testing, clay concept cars that never make it past the dramatic shot in a commercial of Cadillic reinventing itself from the road up, movie scenes that get edited out—there’s a clear line between development and production.


This makes sense. Tech companies have to support and update the products they ship, and need to be thoughtful about which features are worth that investment. A movie would never hold together if the plot had to include every idea from the writer’s room. Production has to be a protected space, to make it feasible to build, functional to use, and affordable to maintain.


Data teams, unfortunately, haven’t developed the same habit. Production is a fuzzy concept, with a wide and blurry boundary between it and development. Some things are obviously in production, such as core dashboards that are used by an executive team and customer-facing features, like Spotify’s algorithmic playlists.2And some things obviously never make it out of development, like the hundreds of one-off queries that I write in the course of trying to remember how various tables are supposed to be joined together. But a huge percentage of a data team’s work sits somewhere in a muddy middle. We share one-off reports to answer one-off questions. We create new dashboards for a product launch, or to fill an urgent demand from an executive. We copy existing dashboards to make new versions that tweak some calculation for a specific customer or marketing campaign. We build data apps that solve narrow problems, like reconciling revenue figures for a financial audit. We ship report after report around the business, each of them addressing something specific, none of them meant to last forever.


When I send a report like this to someone, there’s an implicit contract attached to it: It works now, for the thing I said it would work for. It is, at that moment,in production.But that contract has an undefined scope and an uncertain expiration date. Will it work in the future? For how long? Can the report be extended to answer related questions? People don’t usually ask these questions, and data teams don’t usually volunteer answers.3


As a result, production becomes an expansive, nebulous Frankenstein.4An analyst sends a report to an account manager who’s putting together a monthly business review for an important prospect; the account manager finds it useful, bookmarks it, and keeps returning to it well beyond its intended (but unstated) “best before” date. A designer finds an old analysis on customer segments and uses it to make decisions about their upcoming user study. An operations analyst builds their own reporting on a few tables they find in Tableau, and never tells the data team. A product manager creates a series of new user engagement metrics to assess a recent release, and starts regularly reporting on them to the executive team.5


And everyone eventually ends up frustrated. Data teams lose control over what they’re expected to maintain, and can’t make changes without upsetting at least one side of theseven-dimensional Rubik’s cubeof canonical dashboards and lingering ad hoc reports.6Everyone else loses track of what they trust. And the problem compounds, because data teams can’t fix production if they’re never sure what’s in it; all we can do is add to it.


So what’s a data team to do? Think like a product team, and start defining production.


# Commit more, less often


I’ll take a hard line here: Data teams should be explicit and comprehensive in defining what’s in production. Whenever we create something with an external edge—a dashboard, an explorable dataset, an operational pipeline with a user or system on the other end—we should make a choice: Is this a production asset? If it is, it should be marked, recorded, and supported until decided otherwise.


Admittedly, this would be somewhat onerous, and could make people reluctant to declare something as a production thing—but that’s the point. A company with a few dashboards and a handful of key metrics can focus on what’s important; a company with hundreds can’t focus on anything. A data team that supports a small collection of production reports can keep them freshandwork on other projects; a data team with reports everywhere can’t do either.


This doesn’t mean we shouldn’t answer questions quickly, or turn around one-off dashboards to explore tangential curiosities. We should—speedis a big partof what makes analysts valuable. But we should be realistic about what happens to things after we make them: They expire. We stop supporting them. They should probablyself-destruct. We might as well be honest about this, and neither confuse people who stumble on them six months in the future, nor burden ourselves with wondering if we need to update them when we make some change to the tables they sit on.


In exchange for this peace of mind, we get a new responsibility: We actually have to support the smaller set of things that we officially designate as being in production. We have to stand behind them, just as a product team stands behind features they ship. When some data source or dbt model changes, we have to make sure these things still work. And when we want to stop supporting something, we have to actually deprecate it, rather than letting it drift into slow decay.7


Of course, data teams already do this; it’s just not usually that explicit. Though that may seem like a minor distinction, the guarantee makes all the difference. Imagine a ski resort with vaguely defined runs: Resorts would never quite know which slopes people expect them to keep clear, and skiers could never be sure if they were somewhere safe or dangerous.8This would be chaos, for everyone. To paraphrase afavorite data cliché, that which is defined is maintained.9


# De facto production


Without a clear definition of production, data teams risk getting caught in another trap: They can lose control of their own roadmaps.


For most data teams, production is a de facto state. Something gets created; it gets used; it gets maintained out of necessity; it is, for all intents and purposes, now in production. Though data teams can push the reports and dashboards they think are most valuable, they can still get caught chasing the behaviors of their users. Our runs becomethe paths people ski, not the runs we want to groom.


For example, suppose a data team has created a set of user engagement metrics that provide, in their view, a good summary of how people are using a product. A financial analyst who’s building an account health model asks for an adjusted set of metrics that they think will be useful predictors of customer churn. As a data team, we’ve got a choice: We can say no, and shoot down a potentially valuable project. Or we can say yes, and create the new metrics. However, without a firm line around what we consider production, these metrics could easily drift from a one-time exploration into something that we’re expected to regularly support. The new report could also undercut our existing engagement metrics, and confuse people about which ones they should be focused on.


Product teams can handle these sorts of “feature requests” pretty easily. They tell their customers that they always love to hear from them, that their feedback will be taken into consideration, and in the meantime—and maybe indefinitely—to do their best with the product as it is. And then the product team makes a choice: Can they not only build the feature, but also maintain it and support future updates? Does the feature fit into the vision of what they want the product to be? If it does, they build it; if it doesn’t, they don’t.


If production for data teams was better delineated, we could take the same approach. We could decide up front if the financial analyst’s request fit into our roadmap or not. If it didn’t, we could still help them without accidentally signing up for a long-term maintenance commitment. We could still create new metrics without threatening the primacy of our existing ones. We could stay true to our vision—these should be our key metrics, these are our core dashboards—without having to say no to anything that might overlap with it. And if new reports become so valuable that we want to elevate them to production assets, we could—but the choice would be ours.


# Always be shipping


Data teams and product teams do differ in one very fundamental way though. Product teams are built to ship stuff. Yes, they sometimes have research arms, and yes, people build prototypes that are meant to be thrown away, but all of this is in service of eventually delivering something to production.


Data teams shouldn’t have this mindset. Lots of the work we do—answering one-off questions, sharing self-destructing dashboards, creating new metrics for a financial analyst’s churn model—should never make it to production. We should keep production narrow and exclusive, and be content going days and weeks at a time without ever shipping anything to it.


How do we develop that approach, and build processes that support this way of working? The answer to that question, I suspect, is something we can’t borrow from another department. It’s one we’re going to figure out for ourselves.

[1](https://benn.substack.com/p/what-is-production#footnote-anchor-1-72583378)

The boomers are trying to stay hip.

[2](https://benn.substack.com/p/what-is-production#footnote-anchor-2-72583378)

TIL that you can see your “top tracks this month” and my ego did not need that.

[3](https://benn.substack.com/p/what-is-production#footnote-anchor-3-72583378)

A report is like Velveeta. It won’t go bad right away, and it definitely won’t be goodforever. But how long does it last? It depends ona lot of confusing factors, it’s hard to tell when it does go bad, and most of the ingredients are artificial.

[4](https://benn.substack.com/p/what-is-production#footnote-anchor-4-72583378)

I know what you pedants want this footnote to say about Frankenstein, and I won’t do it.

[5](https://benn.substack.com/p/what-is-production#footnote-anchor-5-72583378)

To be clear, these aren’t complaints about the people using dashboards or creating things. How are they supposed to do anything else? If we tell someone they can trust it today, why should they assume they can’t trust it tomorrow? It’s a problem with the world they work in, not with what they’re trying to do in it.

[6](https://benn.substack.com/p/what-is-production#footnote-anchor-6-72583378)

Unless that data team employs my former colleagueNan Ma, who actually solved one of these things.

[7](https://benn.substack.com/p/what-is-production#footnote-anchor-7-72583378)

My my, hey hey, it’s better to deprecate than fade away.

[8](https://benn.substack.com/p/what-is-production#footnote-anchor-8-72583378)

Either way, you’regetting eaten by the Abominable Snowman.

[9](https://benn.substack.com/p/what-is-production#footnote-anchor-9-72583378)

Given what he wasmeasuring and trying to improve, we should probably come up with another favorite cliché.
