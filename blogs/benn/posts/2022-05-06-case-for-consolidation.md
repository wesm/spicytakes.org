---
title: "The case for consolidation"
subtitle: "It’s what the people want."
date: 2022-05-06T16:46:08+00:00
url: https://benn.substack.com/p/case-for-consolidation
slug: case-for-consolidation
word_count: 2076
---


![Crush Them': An Oral History of the Lawsuit That Upended Silicon Valley -  The Ringer](https://substackcdn.com/image/fetch/$s_!Fll-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fedc550a2-cc63-4c2c-88b3-95011a4051c8_1400x830.jpeg)

*Just don’t call it a monopoly.*


We were going to change the world, but for $1.2 billion, we settled for trying to change Microsoft.


My first job in the tech industry was working as a data analyst atYammer, a company that built a social networking and communication tool for businesses. Our mission was to revolutionize workplace collaboration by dragging people out of email chains andreply-all meltdowns,1and into the feeds, groups, and threads that had been pioneered by social media companies. Though I’m generally too ornery to say nice thingsabout starry-eyed visions like these, Yammer, when used to its full potential, lived up to its promise.


Shortly after I joined, however, we wereacquired by Microsoft.2We got absorbed into the Office division, our product roadmap became an integration roadmap, people starting leaving, and eventually,Yammer was relegatedto the "More" line item in the Microsoft 365 product catalog.


We didn’t always think we were doomed to this fate. Microsoft wouldn’t assimilate us, we told ourselves at the time of the acquisition; we’d indoctrinatethem. I still remember the all-hands meeting after our executive team came back from their first meeting in Redmond. We were told how we were going to change how Microsoft built and shipped software; how we were going to make them more data-driven; how we were going to be a beacon of technology, innovation, and culture inside of the buttoned-down, tucked-in, khaki, IT giant.


The presentation struck me as odd. Yammer was collecting revenues in the low eight figures and burning through a bonfire of cash every quarter. Microsoft, by contract, practically ran a printing press in their basement. They made$73 billion in 2012, bringing in more money every five hours than we had in our entire company's history. We were going to tell them how to make software? We were four years old, had a few hundred employees, an HR team of two, and the most defining part of our culture was our weekly, uh, "alcohol"-fueled parties. They employednearly 100,000 people. Their HR team was so big thatits chiefcould afford a WNBA team. We were going to teach her how to build a corporate culture, and how to fix their performance management framework?


To be clear, Microsoft didn't get everything right, and Silicon Valley would crucify me as a traitor to the founder class if I said we should listen to the old guard rather than disrupt them. But Microsoft certainly didn’t get everythingwrong. Even though our brash, opinionated ideals had won us some measure of success, seeing such staggering prosperity, built on an approach that was antithetical to ours, should’ve led us to ask if our doctrines were as bulletproof as we thought they were.


Which brings me to the modern data stack.


# Microscopic


Ashasbeendiscussedatlength, the modern data community talks about tools a lot. If you spend any time around today's data water coolers—on Twitter, in dbt’s and Locally Optimistic’s Slacks, scattered across a few dozen newsletters and Substacks—you'll find endless discussions about startups and the products they build. We hype productsin closed betas;3we ask if it’s time tounbundle and reinvent software that’s been around for seven years; we all aspire tobe the next Snowflake, the crown jewel of the modern data stack.


Microsoft is often nowhere to be found. There are no discussions about the latest Synapse updates,4or what’s on PowerBI’s roadmap. SQL Server comes up from time to time—usually when people are trying to debug some integration with a different tool, or when they want to migrate away from it entirely. In thecountlessdiagramswedrawof the modern data stack, Microsoft is persona non grata.


But in the market, Microsoft is anything but. PowerBI is the—probably overwhelming—leader in business intelligence. Byone estimate, it captures more than a third of the total spend on BI, nearly double second-place Tableau’s share and six times that of Looker.5And PowerBI has opened up aSecretariat-sized leadin Gartner'smagic quadrantfor analytics tools.


SQL Server's numbers are even more impressive. Microsoft reportedlymade $5 billionfrom the databasein 2014. Assuming SQL Server’s been growing by a relatively modest ten percent a year since then, that figure could be as high at $10 billion today, across180,000 customers. By comparison, Snowflakeclosed their yearwith six thousand customers and $1.1 billion in revenue. While these aren’t quite apples-to-apples numbers—SQL Server solves operational and transactional warehousing needs that Snowflake doesn’t yet try to address—the broader point remains: Microsoft is a dominant player in the data industry. SQL Server and PowerBI alone—to say nothing of Synapse, Cosmos, Azure’s analytics and AI tools, and especially Excel—probably make more money than the entire "modern data stack" ecosystem does put together.


And yet, the two communities don't interact. They occupy the same space but pass silently by one another, like matter and dark matter, one in theUpside Downand the other in the Right Side Up (?).6Customers, too, live in these parallel worlds, evaluating modern data stack vendors or evaluating Microsoft, but rarely crossing over.


One explanation for this is boring: The sets of tools solve different problems for different people. Microsoft has historically dominated the mid-market and middle America. Pick a random company from the Russell 2000, likeVitamin Cottage Natural Grocers, and I bet they’re a Microsoft shop. The modern data stack, by contrast, is—or at least, was—by and for the tech industry.


This probably isn’t the only explanation though. Much of Silicon Valley looks at Microsoft in the same way that we did at Yammer: As aging, wooden, and square; as the makers of Sharepoint, Outlook, Internet Explorer,Zune. The tech community—and by extension, the data community that lives in it—doesn’t value things for where they are, but for how fast they're rising. Nobody talks about the CEO of a public company growing at twenty percent a year, or the VP who’s been a VP for six years. We talk about the people and companieson the cusp—the rocketships, the wunderkinds, the new new things.


Like Yammer, we in the data world should pay more attention to Microsoft.7We should ask if it’s us—and not the company that’s worth more thanMarvel Studios would be if it keeps making huge blockbusters for a thousand years—that’s missing something.


# Proprietary, monolithic, locked-in


Over the last several years, a few ideas have become axioms in the data community: Open-source languages are better than proprietary ones; tooling should be modular, so that customers can mix and match their favorites; vendor lock-in is bad. Though we quibble about specifics, these issues are, for all intents and purposes, settled law.8


On one hand, I agree—these principles are noble ambitions, and, all else equal, better than their alternatives.


On the other hand, all else isn’t equal. Building an ecosystem on these ideals comes at a cost. And if Microsoft is any guide, it’s not clear that customers want to pay it.


Because Microsoft—which owns arguably the most successful suite of data tools in the world—represents the opposite point of view. Microsoft’s languages and tools are, though not strictly proprietary or closed off, largely segregated from the rest of the market. Microsofttightlyintegratesits products,aggressively packagesthem together, and generates as much as95 percent of its commercial revenuethrough itsenormous partnership ecosystem. This creates an insular dynamic where, if you use Microsoft infrastructure, you’re strongly incentivized to put Microsoft tooling on top. Unsurprisingly, that’s what data teams do: In the last 12 months, there have beenfour times as many searchesfor “PowerBI Azure” as “PowerBI AWS” and “PowerBI Snowflake.”


This, combined with Microsoft’s dominant position in the market, suggests that customers actuallydon’t care about modularity. They don’t actually mind proprietary languages. They want products that work, and products that work together. Modularity and flexibility are useful to the extent that they’re means to those ends.


Take vendor lock-in, for example. When webought Snowflakea few years ago, we took some comfort in the fact that it supported a vanilla flavor of SQL. If we found ourselves wanting to migrate away from Snowflake, it would be reasonably painless. But how many product improvements would we have traded that optionality for? Would we prefer Snowflake adhere to the ANSI standard, or offer a set of proprietary functions orfeaturesthat we like? The answer then, now, and in the future, is the latter. We don’t want to be locked in, but more than that,we don’t want to have to migrate at all.


The same applies to other principles. I prefer open-source frameworks—unlessFivetranis just more reliable thanStitchorAirbyte. I like modularity—untilit leads to“drops in signal quality, lower data transfer speeds,” and afailing user experience. As they say, a value isn’t a value until it costs you something. And if I’m honest with myself, thinking as a buyer rather than builder of data tools, I’m not willing to pay very much to hold on to them.9


If Microsoft’s customers are any indication, I’m not alone. Quite the opposite—the world appears to be full of people who will pay a premium for a consolidated collection of tools, packaged and bundled into a neat little suite, sold on a single bill.


# The idealist versus the army


Maybe, in the long run, our principles pay off. But there’s an alternative scenario: We’re building the next Slack.


Slack burst onto the scene around the same time as the modern data stack. It, too, was the darling of Silicon Valley, the envy of every startup, and the subject ofbreathless profileschronicling its rise.


And then, it gotbulldozed by Microsoft Teams. Slack’s heralded product-led growth was no match for the reach of the Office bundle and the ruthlessness of Microsoft’s sales legions. Consolidation and convenience—especially for enterprise buyers—sells better than a delightful product.


In Silicon Valley, whereSlack remains popular, this outcome is almost unthinkable. Slack executed perfectly, and built a product everyone loved. How is it not the winner in the space it created?


The answer, I think, is that for those of us who work in software, it’s easy to place undue value oncraftsmanship. In some modified version ofGoodhart’s law, we make the ideal the product, and (unwittingly, I’d say) assume the best products are those that best adhere to those ideals.


In data products, modularity, flexibility, and composability are markers of our craftsmanship. Butmost people“don’t care about the aesthetics of software in the same way non-plumbers don’t care about the aesthetics of plumbing—they just want their information in the right place or their hot water to work.” They just want software that helps them sell more vitamins at the grocery store.


Microsoft, which can provide those ends without our idealistic means, is perfectly happy to cast craftsmanship aside. They’re happy to consolidate everything under one branded, proprietary banner, make it all work together, and send out an army of sales reps to steamroll the rest of us with it.


If this strategy worked against Slack, it could easily work against the disjointed and sprawling modern data stack. Consolidation, it turns out, may be less ofeconomic necessity, and more of a product opportunity.

[1](https://benn.substack.com/p/case-for-consolidation#footnote-anchor-1-53744915)

If you have any friends who worked at Microsoft ten years ago, ask them what they think ofTDD Dojo.

[2](https://benn.substack.com/p/case-for-consolidation#footnote-anchor-2-53744915)

In a story that’s still ridiculous to me, news of the deal leaked becausesomeone tweeted that they overheard peopletalking about it in a coffee shop a few blocks from the Yammer office.

[3](https://benn.substack.com/p/case-for-consolidation#footnote-anchor-3-53744915)

I’m apersonal investorin Modal.

[4](https://benn.substack.com/p/case-for-consolidation#footnote-anchor-4-53744915)

Pop quiz: What’s Synapse?

[5](https://benn.substack.com/p/case-for-consolidation#footnote-anchor-5-53744915)

Ok, real question: What’s the protocol on citing siteslikethese? Or places likeStatista, which look almost reputable, but have a few too many ads and paywalls to be fully trusted? Are these numbers real, or are they just nerdy content farms that generate random charts and blogs programmatically, like thecreepy channels on YouTube Kids? Their numbers seem in the ballpark, but every time I go to one of these sites, I feel like I’m somehow being had.

[6](https://benn.substack.com/p/case-for-consolidation#footnote-anchor-6-53744915)

It’s left to the reader to decide who is who.

[7](https://benn.substack.com/p/case-for-consolidation#footnote-anchor-7-53744915)

After Microsoft acquired us, our collective response to their changes was to say “ok boomer,” and leave. In the ten years since the deal, Microsoft’s stock is up 900%.

[8](https://benn.substack.com/p/case-for-consolidation#footnote-anchor-8-53744915)

Ha.

[9](https://benn.substack.com/p/case-for-consolidation#footnote-anchor-9-53744915)

Put another way, how much more would you pay for Fivetran if the product were exactly the same, but it was built on an open-source framework? How much less would you pay for dbt if it were proprietary? Yes, these changes might make vendors build better or worse software, but that’s the point: Tenets like these are a means to an end, and as a customer, I pay for the ends.
