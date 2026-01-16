---
title: "Customer capture"
subtitle: "The perilous promise of a big market."
date: 2023-02-17T17:37:59+00:00
url: https://benn.substack.com/p/customer-capture
slug: customer-capture
word_count: 2016
---


![](https://substackcdn.com/image/fetch/$s_!zols!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5746f7fe-464b-45cf-a749-ed6736b89593_2186x1406.png)

*The cops have kidnapped the liquor store customer.*


Every era has its intellectual institutions. Ancient Greece had Socratic dialogues. The Enlightenment had scientific academies. American revolutionaries hadThe Federalist Papers. And Silicon Valley has brash blog posts: self-published on personal websites and Medium and Substack; full ofsuperficially relevantarXiv citations,appropriated referencesto ancient philosophers and European scientists, and an air of cool detachment; and written, often, in an effort to coin some unnecessary new phrase, like “the fatal pinch” or “wordcel” or “data OS,” meant as something between a joke, a real contribution to the discourse, bait for some Hacker News upvotes, and desperate attempt to put a memorable scratch on Etch-a-Sketch of the internet, andnot be forgotten.1


This is a contribution to that tradition, and the term I’d like to submit for consideration is “customer capture.” Share and like and subscribe.


# Split personality


Audience capture was introduced into the lexicon byGurwinder Bhogal, orEric Weinstein, or maybeAlan Parisse. The phrase describes how influencers’ are, over time, transformed by their audience. When people post on social media, extreme stunts and outlandish opinions generate more engagement than mundane content, which encourages people to push the envelope further. Over many cycles of posting and refining, people evolve towards their online caricatures until, eventually, the person loses track of what’s a persona and what’s real. The person, as the phrase goes, becomes captive to their audience, unable to define who they are anymore, and fully becomes the character their audience wants them to be.


Is it real? I dunno—like any good Silicon Valley Think Piece, it’s compelling and has lots of links to Wikipedia pages about cognitive biases, so, sure. But either way, I’d argue that companies are vulnerable to a similar phenomenon.


Save a fewinstant successes, most startups grow unsteadily. Their launch attracts a burst of users, andmany leave as quickly as they arrived. But some people—those who see beyond the horizon of the initial release, and can imagine what might come next—stick around. They like the product, they say, but they love the vision.


The startup, coached on the canon of Silicon Valley—the four steps to the epiphany;the only thing that matters;do things that don’t scale—humbly listens to their customers. They take the feedback; they tweak their marketing; they twist their product to lean towards the promising prospects and use cases. The roadmap curves away from the one laid out at the company’s founding.


As both common sense and every startup incubator will tell you, these adjustments are not only prudent, but necessary.Companies can’t bend buyers to their will; no matter how brilliant an idea, the marketcan stay stubbornlonger than a startup can stay solvent.


In this sense, a startupwantsto be captured by its customers. Unlike influencers—i.e., people—a company doesn’t need to have an external identity beyond its audience. Who cares if Instagram originally identified as aDartmouth Sigma Nu who can’t believe you’ve never been to the Kentucky Derby? It’s now a photo-sharing app, and nobody, least of all Instagram, is upset by that.2


The problem, however, is that customer capture is rarely so clean. Early products are just sketches and scaffolding; the full building exists only as an artistic rendering. Customers, then, are left to imagine the details on their own. And for complex products, like B2B SaaS tools, each customer’s extrapolation is a bit different. One might be excited for a product’s collaborative potential; another might be imagining it as a power tool for specialized teams; a third plans on customizing it to integrate with other services.


But customers rarely articulate these ideas completely, because they aren’t asked, because they don’t fully see it themselves, or because they assume that’s what’s getting built. Instead, each customer’s vision trickles in through individual feature requests—requests that, to the company, seem complementary to one another. They’re all just a step or two off the roadmap; they all point in the same general direction; they differ by only a few degrees. There’s no harm in indulging each request, either by building it now or by telling the customer we’re building it later. Moreover, customer feedback is important; optionality is valuable; strong revenue retention is critical for raising the next round. In time, we’ll get to what they’re asking for.


In reality, the company doesn’t get to those features; it gets drawn and quartered. The longer diverging visions are entertained, the further they pull apart. Customers, sensing the tension, lose patience; the company, now larger and under more pressure to grow, starts throwing bones at the riskiest renewals. While each decision might make sense on its own—a small feature to save a customer seems like a fair trade3—together, they compound into incoherence. The product and its positioning become a labyrinth, a maze without a floor plan, full ofdoors that don’t open and staircases that lead into the ceiling.


Eventually, the customers fully capture the company, trapping it not in a single identity, but in many. The company loses sight of what it’s doing and who it’s selling to, and has the capacity for one and only one strategy: appeasement.


# Give a customer a cookie


Though this disease is endemic in Silicon Valley, data startups are one of the most vulnerable populations.


The geography of the modern data stack isn’t so much fragmented as it’sshattered. We don’t agree on the categories; we don’t agree on the borders between those disputed categories; we don’t agree on where tools sit among the disputed borders of the disrupted categories. Where does data transformation end and BI begin? Are data quality and data observability the same thing? Is reverse ETL real? And how do all of these products interact with ourmahjong boardofjob titles?


Every customer will answer these questions differently, which creates an environment incredibly vulnerable to customer capture. The crowded landscape forces companies to wedge themselves into tiny slivers of open space in the market. These initial positions are typically too small to support a venture-backed business, so companies look for adjacencies to expand into. Customers all pull in different directions, based on how they’ve built their teams and technology stacks. Almost overnight, a narrow tool that was too small to fund can become too big to build.


Transform, which launched as ametric store, potentially illustrates this problem.4Metric storeswere probably too narrow to stand on their own; they needed to be attached to some other category to be viable. But which one? Semantic layers have historically been part of BI tools;that’s one option. Transform could do more transformation, and compete directly with dbt. Metrics are also key entries indata dictionaries, inobservability tools, and inaugmented analytics platforms; Transform could expand in all of those directions as well.


With so many avenues for expansion—which often looks like promising optionality but is actually deadly variability—you could imagine five teams buying Transform, and all of them anticipating a different roadmap. A midmarket retailer might be moving off of Looker, and is shopping for a LookML replacement. A Fortune 500 media company might want a fast way to define and share simple charts with content partners. An AI startup is adding alerting around infrastructure performance KPIs. A Series B SaaS vendor is trying to create a catalog of metrics for their executive team. A fintech provider needs to centralize their metric logic into a versioned semantic layer prior to their upcoming IPO.


When a startup is looking for traction and product-market fit, it’s enormously difficult to turn away any of these customers, especially when its five-year roadmap would solve many of these problems. But these requests are just thefirst of many cookies, given to five mice, all of whom will have ten more requests that come next. By selling to all five customers, Transform wouldn’t be wiggling along their planned roadmap, but tacitly committing to a dramatic—and almost surely unsustainable—fanout across half of the data ecosystem.5


# Saved souls


In his piece, Gurwinder proposes a defense to audience capture: A strong sense of identity. If you know who you want to be, and have the discipline to stay true to it, you’re less likely to chase the identity that’s projected on you by others.


The same is true of customer capture. Companies with a firm identity—a narrow roadmap, tight market positioning, a clear and well-defined buyer—can resist the tangential feature requests and divergent use cases that tug startups in different directions. Importantly, however, this identity doesn’t need to be fixed—the founding identity may miss the mark—but it can’t be fragmented.


The obvious way to develop this is discipline. Say no to customers; say no to optionality;try to make the plan work, and if it doesn’t, explicitly change it.6


This also means saying no to investors. During the fundraising carnival after the pandemic, a bold vision and a bigTAMwas enough to extract a FOMO round from venture capitalists. That pitch, and the VC money it earned, made aggressively expanding into new categories seem both possible and necessary. But in most cases, it’s better to keep a humble soul than to scatter a sold one across a half-dozen horcruxes.


The other way to maintain an identity is for a company to care about what they’re doing. In Silicon Valley, hundreds of startups exist to be successful and to solve a problem, in that order. They’re trophies, status symbols, learning experiences, lottery tickets, lifelong dreams, and, somewhere down the list, a means for making a particular product. These startups,which shoehorn feigned passions around market opportunities, are ripe for capture, because their missions never mattered anyway. It’s easy for a customer to cleave a company from its identity when that identity was manufactured for the customer in the first place. Consequently, I don’t think it’sill-advised at allto fall in love with a project idea. To the contrary, there are few better ways to do it.


Ultimately, the companies that refine their core identity are richly rewarded, and not only in the market that they serve. The bigger a product gets, the more immune it becomes to customer capture; its mass makes it immovable. Companies that reach this point can experiment with expansion, which is often necessary once a company's revenue passes fifty to a hundred million dollars, with little risk of dislodging their core product.7In a world of captives, the free company is king.

[1](https://benn.substack.com/p/customer-capture#footnote-anchor-1-103516005)

A troubling thought: The writers of past eras were presumably motivated by the same basic impulses, which suggests that at least some of what we think of today as revolutionary thought was, at the time, the badly-researched ramblings of a triggered blogger.

[2](https://benn.substack.com/p/customer-capture#footnote-anchor-2-103516005)

Nor is the Dartmouth Sigma Nu who wants to make sick Reel of hisporta potty run at the Preakness.

[3](https://benn.substack.com/p/customer-capture#footnote-anchor-3-103516005)

iN tHiS eCoNoMy, this dynamic is even more pronounced. When financial markets—i.e., venture capitalists and public market investors—reward efficiency over growth, a dollar retained is worth more than a dollar added (or, put differently, a dollar of churn looks worse than a missed dollar of new business).

[4](https://benn.substack.com/p/customer-capture#footnote-anchor-4-103516005)

Potentially! Hypothetically! This is speculation about what could’ve plausibly happened to Transform, given the dynamic of customer capture. I have no idea if it actually happened or not. It’s just a convenient example, and, because Transform wasrecently acquiredby dbt Labs, one that’s safely less relevant to Transform today.

[5](https://benn.substack.com/p/customer-capture#footnote-anchor-5-103516005)

Again, this is a hypothetical! I have no idea if Transform’s customers wanted these things, or if Transform sold any of them. (If nothing else, “a fintech company is about to IPO” should be a dead giveaway that this isallafantasy.)

[6](https://benn.substack.com/p/customer-capture#footnote-anchor-6-103516005)

As a bit of tactical advice, startups should also be mindful of timelines. If you compare prospects’ requests with where you want to be in five years, it’s easy to convince yourself that everyone is a worthwhile customer. But customer patience is not infinite, product roadmaps are path-dependent, and most startups build a fraction of what they say they will in their founding pitches. By promising customers the features in your stars, even taking them to the moon will seem disappointing.

[7](https://benn.substack.com/p/customer-capture#footnote-anchor-7-103516005)

Dropbox, for instance, had such a polished core experience that the company could swallowHelloSignand launchPaperwithout so much as budging most people’s perceptions of what Dropbox was.
