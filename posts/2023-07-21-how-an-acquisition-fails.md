---
title: "How an acquisition fails"
subtitle: "And the simple story for how it doesn’t."
date: 2023-07-21T19:32:47+00:00
url: https://benn.substack.com/p/how-an-acquisition-fails
slug: how-an-acquisition-fails
word_count: 2604
---


![](https://substackcdn.com/image/fetch/$s_!E4VU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F666cab90-c7ad-4e6c-9214-ca5fb767ee93_1280x720.png)


Last fall, I wrote ahandfulofpostsabout how some of today's most popular data products might fail. The point of those posts wasn't to argue that theywouldfail; it was instead to speculate about how theymight. It was to be the devil’s advocate, thetenth man, the host of apre-mortem. It was to assume that we’d been visited by our future selves, and instead ofgetting an almanac, all we got was a look atMatt Turck’s data landscapefrom20331—and Snowflake, dbt, and Fivetran were all missing. We didn’t know why; we only knew they were gone. Those posts were my guesses as to what would explain their hypothetical disappearance.


I wrote them for the same reason I write most things on this blog: Because I found it fun to think about, and because there was a Friday those weeks. It was an excuse to live in my head for a minute, to look up someGriffandTaylor Swiftbangers to link to, and to play every talking head’s favorite role: That asmug critic, fastidious and unfit for doingthe rough work of a workaday world, withno skin in the game.


Play for blood, theysaid. I’m just foolin’ about, I said.


Karma2, it seems, tracked me down. A new BI company launched this week—ThoughtSpot and Mode, under one roof,officially.3Though neither Mode nor ThoughtSpot is (yet!) the ubiquitous community staple that dbt is, and we haven’t (yet!) gone public in thebiggest software IPOin history like Snowflake, the combined operation is substantial: Booking more than $150 million in annual recurring revenue, supported by $750 million in funding, and serving customers from Wells Fargo, Verizon, and CVS, to Snowflake,4Capital One, Anheuser-Busch, and VMware. If the modern data stack is to produce an enduring and independent business intelligence company—if there is at least one IPO among the72 companiesvying for the ticker symbol of BI5—ThoughtSpot and Mode now have as good of a shot at it as anyone.


But that also means we could be the next major disappointment. As a company’s promise grows, its outcomes become more binary—IPO or bust; runaway success or cautionary flop; generational triumph or catastrophic collapse.


So, for the sake of avoiding it, here’s how we find ourselves on the latter path.


# The usual suspects


Tech acquisitions arenotoriously temperamental. Big visions are easierto sell than deliver; technology stacks are sometimes incompatible; cultures don’t mix. Innovative roadmaps turn into interminable integration efforts that are more expensive, slower moving, and less rewarding than all of the projections on the spreadsheets. Some idiot with a blog torpedoes the whole thing two days after it closes for a clickbait headline and some likes.


These are the inevitable dangers lurking in any acquisition. You can be aware of them, push on them during due diligence, and be mindful when you’re slipping into one of their slow traps. But you’ll never know if you’re fully compatible until the deal is done and everyone is working together—until you’re not just dating, but married and moved in.


Like any leap of faith, it’s a gamble. Sometimes, though, the potential reward is worth the risk—and you’ve to believe you’re the kind of companythat rolls a six.


# The bad track record


Outside of those routine challenges, however, this acquisition can’t miss. Just look at the strategic fit!


> [It will create] a complete data science and analytics platform for customers…The two companies’ CEOs met about 18 months ago at a conference, and running similar kinds of companies, hit it off. They began talking and, after a time, realized it might make sense to combine the two startups because each one was attacking the data problem from a different angle.One company tends to serve business intelligence requirements either for internal use or externally with customers. The other looks at the data science end of the business. Both CEOs say they could have eventually built these capabilities into their respective platforms, but after meeting they decided to bring the two companies together instead, and they made a deal.“I realized over the last 18 months [as we spoke] that we’re actually building leadership positions into two unique areas of the market that will slowly become one as industries and technologies evolve…”“[We have been] pulled into this broader business intelligence conversation, and it has put us in a place where as we do this merger, we are able to instantly leapfrog the three years it would have taken us to deliver that to our customers…”The two executives say this is part of a larger trend about companies becoming more data-driven, a phrase that seems trite by now, but as a recent Harvard Business School study found, it’s still a big challenge for companies to achieve.They recognize that many acquisitions don’t succeed, but they believe they are bringing together two like-minded companies.


Except—this isn’t a story about ThoughtSpot and Mode; it’s from an article from 2019about Sisense buying Periscope. And that deal, which has a very similar outline to this one, is widely regarded as a dud. It didn’t vault Sisense to the front of the BI market;6Periscope, one of the early success stories in the modern data stack, has beentwicerebrandedout of existence. With this as the most recent precedent, the question to ask might not be how does our acquisition fail, but how can it possibly succeed?


On one hand, it’s easy to overfit on one example, no matter how similar it seems on the surface. Every acquisition, like every company, is an idiosyncratic mix of technologies, personalities, and circumstances. What doesn’t work in 2019, early in the modern data stack’s hype cycle, may work very differently in 2023, as that cycle is receding and generative AI is emerging.


On the other hand, it’d be foolish to entirely dismiss it. The logic behind Sisense acquiring Periscope is sound; if their customers told them the same things ours tell us—”our SQL writers love Mode, but we also want more self-serve BI”—the promise of pairing the two products together is clear. So why did it still not work out? Without knowing the specific details,7I have two general hypotheses.


# The devil is in the details


The first is that strategic fit can only take you so far. As compelling as the headline sounds—BI and analytics, all in one place!—it omits a lot of experiential details. How do you reconcile two charting systems that look different? How do you promote a SQL query written in one tool to a dashboard in the other? Do both tools share the same caching layer, or do they remain independent?


These are messy questions, and it can be tempting to answer them in the most technically orderly way possible: Tuck one product into another; refactor everything into tidy and DRY codebases; simplify overlapping org charts into linear pyramids; all the features,mise en place.


This, I suspect, is a trap. Data consumption tools aren’t infrastructure; they’re productivity tools. People buy them for their user experiences as much as their technical features. Protecting that experience across the two products has to be the first priority of any acquisition like this; enhancing it has to be the second; and neatly sorting through the technical details of how to do it has to be a distant third.


# The devil is in the entire plan


The second possible explanation behind the Periscope and Sisense result is thatthe products don’t actually fit together.


There are two ways to read the relationship between general BI tools like Sisense and ThoughtSpot, and data team-focused tools like Periscope and Mode. The first is that most customers want both sets of features, but have to choose one. The second is that customers see the two categories as representing competing philosophies, and they choose the one they like over the one they don’t. In this case, they might want a well-structured and tightly controlled data model and explicitlydon’twant a free-for-all SQL editor; or they might want a tool that can be deployed quickly on top of raw data, and explicitlydon’twant to deal with modeling data first.


If most customers fall into the latter category, almost no product integration makes sense. The acquisition can still work, as a combination of business units, but the products are best kept at an arm’s length from one another. Fox News and MSNBC could be owned by one (very chaotic) parent, but they can’t commingle their lineups.


My view is that it’s not that extreme; very few customers are religiously opposed to one side of the spectrum or the other. However, it suggests that one way these acquisitions go wrong is by imposing the philosophy of one product on the other. Instead of doing that, each philosophy, to the extent that they’re competing, should be optional and additive, available to customers when they need it.8


# The modern data suite


An easy future to imagine is one where the modern data stack is replaced by a few modern data suites—all-in-one, end-to-end platforms of warehouses, ETL, and BI, sold by a single vendor. This is Microsoft’sapparent ambition; it should beGoogle’s ambition;Frank Slootmanmay yetcome for us alltoo.


By bundling related products into a singlecluster, suite vendors can usually offer their customers both lower prices and an easier buying experience than independent vendors can. The market couldcome to preferthis offering over today’s more modular one; if that happens, Mode and ThoughtSpot wouldn’t struggle because we consolidated too much, but because we didn’t consolidateenough.


For smaller vendor, this can be a huge problem. The bigger a seller, the more they can dictate the market standard. Google, for example, can set everyone’s expectations for how search on the internet should work. It doesn’t matter if some small startup builds a better search engine, because nobody will use it; if nobody uses it, nobody will know that they want it. But when that search engine gets big enough, people will notice, and start expecting more out of Google.


If bundled suites become more common, that’ll be the challenge for independent vendors—to be big enough and be differentiated enough that people at least question if the easy default is the right choice. My sense is that Mode and ThoughtSpot are already there, but,never turn your back on the Microsoft sales team.


# The AI tsunami


Both Mode and ThoughtSpot are, at their core, BI tools. They’re centered around charts and dashboards; they let people explore data; they’re all about operational metrics and insight discovery. Both of us have added significant twists—ThoughtSpot lets people ask questions with natural language; Mode lets analysts bypass traditional data models and work directly in SQL and Python—but we’re still descendants of products like MicroStrategy and Tableau.


Though it may seem counterintuitive in Silicon Valley, I’ve long viewed this connection to the past as an advantage. For years, any product that’s similar to a BI—new visualization tools, exploratory data science environments, chatbots that write SQL queries—eventually becomes BI, and has to buildeverything that goes with it. This protects established players who already check most of the BI boxes from narrow upstarts that sell just one reinvented sliver of the category.


So far, generative AI hasn’t altered this pattern. If anything, it’s reinforced it, by allowing companies like ThoughtSpot and PowerBI to get more leverage out of their BI tooling. But if the AI wave is revolutionary enough, it could finally break that cycle, by creating entirely new paradigms for interacting with data. Analysis could become entirely conversational, removing the need for querying data directly at all. We could stop storing data in warehouses, but dump it all into vector databases that are modeled by GPT-6. Bots could simply start telling us what to do, and dashboards could become an obsolete middleman.


If any of these things happen, the deep moat of features that protects today’s BI tools’ would suddenly become a cage, trapping us all in the past as the world moved on.


# “I’m your huckleberry”


For almost two years, I never told anyone inside of Mode what I was going to write about before I published it. I did that partly because I'm an anti-social hermit and egomaniacal perfectionist; partly because of founder privilege, and I could get away with it; and partly because I was afraid of being edited out of my own posts.9If I was putting my name on it, I wanted to own it, for better or for worse.


This post was the first exception. For obvious reasons, yesterday, I asked a handful of folks at ThoughtSpot if they were ok with its rough thesis. Though it may be better to ask for forgiveness than permission, my thinking went, that only works if you don’t get told to leave before you can plead your case on the company Slack.


I was toldto fire away.10


They didn’t have to give me that leash. They could’ve tapped the sign, and reminded me that$4.2 billionis a lot more than$200 million. Instead, they’ve consistently reminded me that 4.2 is a lot smaller than15.7, or57.8. Until we’rethere, they said, we’re all upstarts, together.


There are lots of convoluted reasons that companies can fail. A market shift can expose an obscure vulnerability; a competitor can outflank a key messaging beachhead; one product strategy can compound in weird ways with another, in a dynamic best explained by a cable news analogy.


These things are fun to talk about. But most companies aren’t killed by some obscure threat lurking in the weeds that they never see; they’re killed by the thing that everyone knew about, everyone saw, everyone felt, andnobody fully faced. They’re killed by a product that never finds a market; by chronically low user adoption; by a buggy product with high churn; by unsustainable and broken unit economics. When you’re a critic, it’s fun to find more creative narratives. When you’re in the arena,everyone already knows what’s wrong—and it’s courage that you need, not cleverness.


Like Snowflake, dbt Labs, Fivetran, ThoughtSpot and Mode could fail. I’m optimistic, though. And not because of 3,000-words of indulgent analysis, but because when I asked ThoughtSpot what they thought of that analysis, theydidn’t shy away from the fight.

[1](https://benn.substack.com/p/how-an-acquisition-fails#footnote-anchor-1-135341191)

Will this ever work?Do I want it to ever work?

[2](https://benn.substack.com/p/how-an-acquisition-fails#footnote-anchor-2-135341191)

A definite banger.

[3](https://benn.substack.com/p/how-an-acquisition-fails#footnote-anchor-3-135341191)

Just in case, I worked for Mode, and as of Wednesday, now work for ThoughtSpot. When I say “we,” I typically mean the combined company.

[4](https://benn.substack.com/p/how-an-acquisition-fails#footnote-anchor-4-135341191)

Until, of course, karma catches up to them too, andtheir business is sunk by its capital letters.

[5](https://benn.substack.com/p/how-an-acquisition-fails#footnote-anchor-5-135341191)

Or do you dance on your ancestor’s grave, and go withDATA?

[6](https://benn.substack.com/p/how-an-acquisition-fails#footnote-anchor-6-135341191)

This is entirely based on two terrible metrics: rumors, and Sisense’s declining position on the Gartner’s magic quadrant from2019to2023. Could I be entirely wrong, and could Sisense be making money hand over fist, and about to IPO under the tickerCANT_STOP_WONT_STOP? Maybe!

[7](https://benn.substack.com/p/how-an-acquisition-fails#footnote-anchor-7-135341191)

I also don’t know any specifics about the Periscope acquisition, or what happened in the years that followed. If you do, and there are things we should learn from it, let me know!benn@mode.com! Or if you don’t, but you want to make up stories to sabotage us, email me atbenn+hot-acquisition-tips@mode.com.

[8](https://benn.substack.com/p/how-an-acquisition-fails#footnote-anchor-8-135341191)

This extends beyond the product. Arguably, the most damaging thing that Google and Salesforce did to Looker and Tableau was to impose a corporatecommunityandsupportphilosophy onto companies that had taken very different—and successful—approaches to those areas of the business. Customers weren’t upset at these changes just because they lost a periodically useful service; they were mad because they felt a company they loved was losing its identity.

[9](https://benn.substack.com/p/how-an-acquisition-fails#footnote-anchor-9-135341191)

Nobody at Mode ever actually did this. It’s probably PTSD from when I worked in DC, and everything we published had to go through at least three editors.

[10](https://benn.substack.com/p/how-an-acquisition-fails#footnote-anchor-10-135341191)

Not Taylor Swift, butstill a low-key banger.
