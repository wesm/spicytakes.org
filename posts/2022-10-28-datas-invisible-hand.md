---
title: "Data's invisible hand"
subtitle: "An inquiry into the nature and causes of the wealth of data teams."
date: 2022-10-28T17:05:58+00:00
url: https://benn.substack.com/p/datas-invisible-hand
slug: datas-invisible-hand
word_count: 2613
---


![](https://substackcdn.com/image/fetch/$s_!_EjC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9187eb77-0ca8-4444-9b5c-684b489e0f02_747x420.png)

*Adam Smith wasweird.*


Externally, startups are the ultimate capitalist enterprise. They fight in raw competition with no political clout; they benefit from no regulatory capture; they are afforded no unfair advantages. Their survival depends entirely on their ability to win users and customers. Their reward is unimaginable wealth; their punishment is destitution and bankruptcy. The market is the only true meritocracy; may the best company win.


But internally, startups are the ultimatecollectivistenterprise. They urge employees to make personal sacrifices for the greater good; they preach about shared ownership; they promote the needs of the company over individual careerism. They instruct everyone to disagree, but commit. They make decisions by consensus when they’re small, then by executive edict when they’re large. They are values driven; they are a team; they are highly collaborative.


Data teams often live this collectivist ethos. We function as a service organization, built to enable others. We build self-serve tools that try to meet others where they are—from each according to his ability, to each according to his needs. We take requests from the company and prioritize them, inartificially quantifiedtwo-by-twomatricesthat compareimpact and effort, to determine how we can best promote the welfare of our corporate society. We areProject Cybersyn, sitting in our command center of dashboards and statistics, attempting to figure out what the company needs.


It’s a stressful and challenging role. We get asked too many questions, and have to decide what to do and what to discard based on incomplete information—how valuable was that critical dashboard, really?—and loose heuristics that favor things due today over things due tomorrow, and favor things from executives over things from managers.


What if, instead, we acted like our companies act, and let the market decide?1What if we built an internal economy for data work so that everyone pursues their own self-interests, andin doing so, “promotes that of the society more effectually than when he really intends to promote it?”


It’s Friday; let’s invent some wild ideology and see where it takes us.


# Cap and trade


Here’s how an analytical economy might work. Every quarter, everyone at the company is given a set number of credits that they can use to “buy” work from the data team. Each week, or on whatever sprint cadence makes sense, the data team holds an open auction. People submit bids for work. Each bid includes a project proposal and an offer price. During the auction, the data team asks questions, and bidders answer them to fill in missing details about their proposals. The two sides then negotiate: Analysts and data team members choose which projects they want to do, and the bidders haggle over prices to make sure their proposals get chosen. At the end of the whole exercise, rejected proposals get shelved and winning bidders pay up. The data team delivers the work they sold. Next week, everyone does it all over again.


It’s a tidy little economy, and,as is always true with these miniature markets, has—in theory—a lot of elegant properties.


First and foremost, a bid-and-ask model like this should prioritize work much more efficiently than a data team that makes decisions on their own. Nobody is a better judge of a data asset’s worththan its consumer. But today, those consumers communicate that worth by lobbying the data team for their time, meaning the squeaky stakeholders—or the most convincing ones—get the grease.


Credits level the playing field. People can’t demonstrate the value of their request through an impassioned Slack message; they can’t inflate a project’s urgency or exaggerate its impact. Instead, they can only spend a scarce resource. That’s a much truer signal of value, in both directions—people would only pay high prices for truly important work, and won’t pay much for indulgent curiosities.2


An open auction doesn’t just create a market for the work itself, however; it also prices in a lot of other intangible tradeoffs that data teams often have to make. Urgency is priced in: If someone needs something immediately, they would pay more for it. On the extreme end, bidders could buy an all-nighter—everyone’s 4 a.m. has a price.3Long-term versus short-term tradeoffs are priced in: Since every project is traded on the same market, buyers can explicitly decide how to value a long-needed revamp to a core dashboard relative to an immediate fix that duct tapes over a problem. Speculation is priced in: People can choose if they want to spend their credits on exploratory research that may come up empty, or if they’d rather buy less risky projects that have a lower ceiling.


None of this is directly controlled by external stakeholders though; data teams are still autonomous. If they want to focus on a strategic initiative over the rote dashboard updates that people want, they can—they’ll just get paid less to do it. Similarly, desirable work—that fun ML project, launching a new experimentation platform, working with the marketing team on field research—would trade at a discount compared to the interminable Salesforce reconciliation project.4But that’s the beauty of the open market: If something is valuable enough, prices adjust, someone eventually accepts the bid, andthe market clears.


Prices could even account for team dynamics like performance and team organization. Congenial and collaborative stakeholders could buy work at lower prices than rude ones. Good analysts could command higher prices than bad ones, and analysts who are experts in a particular domain could price their work in that area at a premium. If analysts wanted to change their focus—to move from operations work to product, or shift from being an analyst to an analytics engineer—they’d be free to accept bids in those areas; they’d just get paid fewer credits to do so. The same is true for assigning who gets to work on the best projects. Every bid is open to everyone; it’s just a matter of what price you’re willing to take.


# Hitting quota


There is one blaring question in the center of this whole scheme: Why would members of the data team want to collect credits in the first place? Everyone else can use credits to buy work from the data team. But what good are they if youarethe data team? If all you can buy withSchrute bucksare beets, what are Schrute bucks worth to a beet farmer?


One option, if we wanted to completely reinvent how companies work, is to create the same cap-and-trade schemes for other departments. Need engineering help debugging a data pipeline? Pay in credits. Want design help on a slide deck? Pony up. Trying to schedule a meeting? Buy the time of all the attendees. I have no idea what the implications of this would be, nor do I have the money to spend on aJSTOR subscriptionto figure them out.


The other, much simpler option is that data team members carry credit quotas, much like sales reps and account managers do. Every quarter, members on the team are assigned a quota, with more senior members carrying a higher quota than junior members. People retire their quota by selling their work in the weekly auction. If team members’ earnings exceed their quota, they get paid a cash bonus; if individuals fall short, it’s considered a performance problem. And if the entire team misses their aggregate quota, it’s a performance problem for the team’s leadership.5


A program like this also offers a third option in the forever war in Silicon Valleyoverworkinghours. Data team members would get paid for the projects they deliver, with each of those projects priced at a value set by the market. High performers could close out their quota quickly and in fewer hours; if they want a bigger bonus, they accept more bids, clock in more time, collect more credits, and get paid. Struggling analysts could still beat or exceed their quotas, though they might have to work more hours to earn the same amount.6


# The economics of the firm


The fun7part of this proposal, however, comes from its corollaries and extensions. Once you have a core market in place—once there are buyers, sellers, and credits that both parties want—a whole bunch of other interesting possibilities start to fall out.


For example, one implication is that a credit-and-quota economy like this puts an explicit price on analytical work. Companies can use the bonus payout rate to convert credits into cash equivalents; this conversion rate can then be used to figure out the cost of every accepted analytical project. If companies feel that these prices are too high—i.e., if the company is shipping dashboard updates for $10,000 and a few new dbt models for $35,000—they can cool the analytical economy by lowering the number of credits in circulation. Conversely, if projects are underpriced—i.e., the company is spending $500 on strategic research that’s easily worth ten times that—the company can issue more credits. This would stoke demand for analytical work by giving stakeholders more money to spend, and encourage data teams to expand their supply, by working more or by working faster, since they would have a larger bonus pool to chase.8


Companies could also intervene in more direct ways. Leaders could be given more credits than other people at the company, creating a more structured and transparentHIPPO effect. Additionally, teams that are supporting key initiatives, like a marketing organization has a big launch or a finance team that is leading a fundraise, could also get extra credits. These adjustments give leadership some sway over what data teams work on without having to dictate it outright, and without fully freezing everyone else out. Even when there are urgent priorities, anyone can still bid for work; the price is just higher.


There are other wild ideas: Data teams could charge subscription fees to keep their time on retainer, in case unexpected questions come up in the normal course of business. Buyers could pool their credits to create joint proposals. Analysts could pair on projects, and share the revenue. Project proposals could have tiered payouts, where part of the bid is paid upfront, and part is paid on delivery.9Data teams could market their services, and offer discounts on projects that are complementary with one another.10


I suspect there are countless other extensions and permutations and secondary effects. Some might work; some might be a disaster; some might just be weird. But that’s how we progress: Byletting a hundred flowers bloom, and letting a hundred schools of thought content.11


# Would it actually work?


Admittedly, when I first had this idea, I thought it’d be an interesting thought experiment that hangs a few compelling suggestions off of a fundamentally broken foundation. But now the opposite seems true: It could actually work, if you sand down some rough edges.


For example, companies would have to create some system of arbitration to resolve the inevitable arguments between a buyer who says they didn’t get what they paid for, and an analyst who says that some detail wasn’t properly specified in the original agreement.12But, to avoid contract disputes, bidders would be incentivized to be transparent about exactly what they want to buy. Do they want a one-off answer, aself-destructing dashboard, or aproduction datasetthat needs to be maintained forever? What quality and latency expectations do they have? We already ask these questions inrequest intake forms; tying them to a contractual bid just forces a bit more honesty—and more accountability from the data team to deliver on them.


A free market economy could also turn what should be a collaborative work environment into a cutthroat one, where stakeholders are bidding against one another, data team members are competing against one another, and data teams and stakeholders are negotiating against one another. This already happens though; the fight is just unstructured and underhanded. Projects get prioritized through DMs and executive vetoes. A transparent bidding system in which everyone can see what bids the team accepts and at what cost they accept them may actually create a healthier dynamic than one built on argument and influence.


Still, fully embracing a free-for-all open marketfeelsoff—if for no other reason than to protect ourselves from removing the guardrails that keep us from periodicallycareening us into a ditch. As John Maynard Keynes (never) said, “capitalism is the extraordinary belief that the nastiest of men for the nastiest of motives will somehow work for the benefit of all.” As promising as a free market for analysis might be,on today of all days, I’m still voting for a bit more regulation.

[1](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-1-81216506)

For thesecond time, this entire post is cribbed froma conversationwith Boris Jabes, the CEO ofCensus.

[2](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-2-81216506)

This is one way to eliminate open-ended wild goose chases. People are much less likely to send data teams down rabbit holes if they’re paying to dig the tunnel.

[3](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-3-81216506)

This also encourages buyers to ask for work early. Like booking a plane ticket eighteen hours before takeoff, indecision—or “flexibility” as those of us who routinely buy tickets and check in at the same time prefer to call it—comes at a cost.

[4](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-4-81216506)

Another benefit: If data teams charge more for painful projects, stakeholders—or “data producers”—are incentivized to make their data easier to work with. A marketing ops team that keeps Hubspot clean could buy a lot more of the data team’s time than one that leaves Hubspot as a disorganized mess.

[5](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-5-81216506)

Team quota attainment is toteam NPSas revealed preferences are to stated preferences.

[6](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-6-81216506)

One one hand, this definitely feels like a ruthless and impersonal way to resolve impossibly sticky questions about work-life balance (the invisible hand is fair, but it’s not tender). On the other hand, sales teams have operated this way forever, and sales organizations are generally accepting of it as a reasonable way to work and get compensated.

[7](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-7-81216506)

Look, I write a weekly blog about databases and ETL tools. My idea about what’s fun has gotten pretty warped at this point.

[8](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-8-81216506)

In determining the credits in circulation, the leadership team is, in effect, setting monetary policy. (Twenty-six year old startup founders setting monetary policy; what could go wrong?) Removing credits from the economy would lower prices; if credits have fixed dollar equivalents—for example, if analysts are paid $500 for every credit they collect over their quota—lower prices for analytical services would discourage analysts from offering these services. Adding credits to the economy would have the opposite effect. If analysts could charge more for the same work, production would increase.


At least I think this would happen. The fixed conversion rate kind of looks like agold standardor adollar peg, in which fiat currencies (credits, in this case) areconvertibleinto something of stable value. These monetary systems normally don’t allow for expansionary monetary policies. However, I don’t think this internal economy would function the same way, because companies can arbitrarily change the conversion rate—i.e., the dollar amount they pay out for each credit—without running the risk of running out of reserves. But they aren’t strictly fiat economies either, since credits can always be converted to some cash equivalent. So I’m not sure how you would best model this. Here’s to hoping I never get bored enough to writethatblog post.

[9](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-9-81216506)

Investigative work could be paid for in this way, to hedge against the risk that the exploration goes nowhere and turns up nothing of value.

[10](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-10-81216506)

The bleakest of futures: One analyst runs ads in Slack promoting their services. They buy anad attribution studyfrom another analyst. The data teameats itself.

[11](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-11-81216506)

Ok, so maybe Mao isn’t the right person to quote in my closing argument for turning data teams into unchecked capitalists. But it’s a good quote.

[12](https://benn.substack.com/p/datas-invisible-hand#footnote-anchor-12-81216506)

That’s a true data contract: A forty page tome of legalese that lays out, in painful lawyerly detail, exactly how to build a new marketing lead funnel dashboard.
