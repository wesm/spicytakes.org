---
title: "Stuff costs money"
subtitle: "The many temptations of software businesses. Plus, a hackquisition?"
date: 2025-09-05T17:41:53+00:00
url: https://benn.substack.com/p/stuff-costs-money
slug: stuff-costs-money
word_count: 2490
---


![](https://substackcdn.com/image/fetch/$s_!JXQZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5819a87-7390-43b0-8f87-523dce483baa_1384x1082.png)

*From left to right: Open source; complaining about open source; the context layer; taking a little peek; a chatbot for actionable insights.*


If you want to build a big software business, there are two ways to do it:

1. Build a new product, and charge people to use it.

1. Build a new product. But start small, in a narrow niche. Make some helpful utility, for a very specific set of people with a very specific problem. Downplay your ambitions; talk about how you’re solving a problem for yourself; how you’re building the thing you always wanted. Acknowledge your product’s rough edges; its odd opinions. Put it on Github; say it’s free, open source, forever. Go viral on Hacker News; talk to people on Twitter, on Reddit, never on LinkedIn. Create an online space for your users; call it your community. Open issues; debate them; ask for contributions. Build in public—for the people; of the people; by the people.Then, gently launch a paid version. Talk about how these are necessary updates to pay the bills; that they only affect a tiny fraction of users; that these small price increases will make it possible to improve the product for everyone. Talk about how reluctant you are to do it. Internally, with your coworkers, debate if this is the right move. Wrestle with what it means to raise money from eager venture capitalists. Wrestle with what is and isn’t selling out. Wrestle with the weight of your soul. Launch an enterprise plan; launch a new SaaS app; launch a rebrand. Slowly strip your website of old blog posts. Update your pricing model. Update your pricing model again. Pause the update to your pricing model. Go on a listening tour. Get called a fraud. Get accused of crimes. Get off of Reddit, says your therapist. Wonder if it is all worth it.Lose business, because other companies are selling forks of your open source library. Miss your annual targets, because prospective customers are choosing to use your free product. Lose your best sales reps, because they’re sick of selling against themselves. Tinker with your open source licensing. Worry about a new competitor that says they’re the better version of you, but free, open source,forever.Write a heartfelt note to the community. Edit out the parts that you really want to say. Post it on LinkedIn.Eventually, wear down. Your customers wear down more. Find a battered equilibrium. Constitute an open source committee; elect members from the community. Fund it with corporate money; call it a marketing expense. Announce a new vision; a bold new direction.Build a new product, and charge people to use it.


Nevertheless! Option two has its temptations. The first part sounds fun! It’s full of character! It’s spunky! The mercenary manufactures and sells. The iconoclastbuilds, with a capital B; for the community; for the craft; for the right reasons.


But eventually—in the best case, if things go well—two things will inevitably happen. One is that the first paragraph of option two shudders into the second. Because, of course it does! Not only is software very expensive to build; not only is itexpensive to maintain; not only are companies commercial ventures; not only do they need money to operate; not only do companies that raise money need to pay back their investors; not only are the people who build softwarepeople, who want to get paid for their work, to be able to buy food, a house, maybe two, and perhaps a yacht; not only might all of these things compel a company to charge people to use the thing it built, but also, whyshouldn’tthey?


Still, that leads to the second inevitability, if a company chooses option two: At some point, people will get mad about it.


Anyway, earlier this week, Fivetran, a commercial vendor that sells software for money,bought Tobiko Data, a commercial vendor that gives away software for free (but also,you know):


> Fivetran, the global leader in automated data movement, today announced it has acquired Tobiko Data, the open source transformation company behind SQLMesh and SQLGlot.


And peoplewere upset:


> Hell nah man, what a disappointment. dbt went right to the trash with their rugpull this year and I really hoped, Tobiko would stay on their path and save us. BUT WHAT DID YOU DO TOBIKO. Sell to Fivetran with absolutely 0 open sourced... Any other alternatives guys?


As the next commenter says,what did you expect was going happen?Forget the history of open source software; just consider the direct series of events that led to this acquisition:

1. Ten years ago, Fivetran’s primary competitor was a company called Stitch, which built a nearly identical product. Stitch was built onopen source connectors; Fivetranwas not. Now, Fivetranis worth billions. Stitch wassold to Talend for $60 millionand iseffectively defunct.
2. dbt, Tobiko’s primary competitor, began as an open source project. As it became more popular, dbt Labs began charging for features.Peoplegotupset.
3. Recently, dbt Labs bought SDF Labs, whichwas free to useand offered features competitive with Tobiko’s. dbt Labs began packaging a lot of those features in their paid plans.Peoplegotupset.
4. Now, presumably to compete with all of this, Fivetran bought Tobiko.1And people gotupset.


Nobody is upset at Costco for charging people to shop there because they give away free samples! Nobody pouts about having to buy movie tickets even though movie trailers are free! Why are we righteous about paying for our software?


Writing about memecoins,Matt Levine was similarly miffed: “People are complaining that this is a ‘rug pull’ or a ‘pump and dump,’ but I cannot understand what different thing they thought would happen.” Right!Open coreis abusinessmodel for themonetizationofcommerciallyproduced open-source software; of course it will eventually cost money! What different thing did anyone think was going to happen?


But it is fun to be mad, and someone istrying to make moneyon the internet. So there will be temptations.2


---


# Hackquisition


In the early days of the generative artificial intelligence boom, there was a cliché that your AI is only as good as your data. “There's no AI strategy without a data strategy,”said Snowflake CEO Frank Slootman. “Data is your differentiator,”said Satya Nadella, Microsoft’s CEO and OpenAI’s rich uncle. “You may think that AI is powered by some incomprehensible alien math, but its actual foundation is the boring mechanical work of carefully collecting and cleaning data,”saidmanypeoplewho worked for companies that sold stuff to make the boring mechanical work of carefully collecting and cleaning data easier.


People still saythese sorts of things, and when they do, theyare mostly talking abouthaving good data to train or prompt models. But if you are an AI company, there are other kinds of data that can be useful. For example, it might be helpful to have data about how people are using your product. How often do they log in? What do they do when they use it? Which features do they seem to like, and which ones do they ignore? What are the patterns and relationships among all of these things?


These are pretty standard questions that people have been trying to answer about their software products for decades, and there’s a robust market ofproduct analytics toolsthat try to help people do it. So, a couple days ago,OpenAI bought one:


> We’re acquiring Statsig, one of the most trusted experimentation platforms in the industry—powering A/B testing, feature flagging, and real-time decisioning3for some of the world’s most innovative companies, including OpenAI. …The Statsig platform has already played a central role in how we ship and learn quickly. Bringing it in-house will strengthen our ability to accelerate experimentation across our Applications org and build even better, more responsive experiences for the people and businesses we serve.


Sure, why not? If you’re a$500 billion companythat’s used by700 million peopleevery week, you don’t want your feature requests to be stuck in some queue behind every other customer. Might as well just buy the whole thing, and build exactly what you want.


But if you’re a big AI company, there’s a third kind of data that might also be valuable: How do people useyour competitors’products? How often do they log in? What do they do when they use them? Which features do they seem to like, and which ones do they ignore? What are the patterns and relationships among all of these things?


Of course, this data is hard to find. You might be able to hack it, or steal it, or pay a mole to smuggle you a USB drive.Which happens, but,you know. You could alsobuy itfrom companies that track things like credit card purchases, but that will only tell you what people spend. It won’t tell youhowthey use a product—the features they use, the buttons they click, the experiments they run and how they performed—because most companies are pretty stingy with that sort of product telemetry data, and are very careful not to share it.


But they do share it with a few people. Here’s Anthropic,on who they share theirs with:4


> Claude Code connects from users’ machines to the Statsig service to log operational metrics such as latency, reliability, and usage patterns.


Ahaha, oops.


No, I mean, of course I’m not saying that OpenAI bought Statsig as an alternative to hacking into Anthropic’s databases. I’m not saying they did it so that they could sniff around how people are using Claude Code. (Notably, Anthropic “does not include any code or file paths” in what they send to Statsig, so, even if they wanted to, OpenAI can’t use Claude Code data to improve their own coding models.) Maybe they really did buy Statsig just for the product; maybe it was actually an acquihire.5Or maybe it was because OpenAI also sends data to Statsig, and when your principal competitor is worth$183 billion and just raised $13 billion, you’re worried thattheymight buy Statsig so thattheycould sniff around how people useyourproducts. But Statsigdoeshave records of the actions people take in Claude Code, and Statsig’s terms of servicedosay that Statsig has the right to look at it.6And if you worked for OpenAI, there must be temptations.


---


# Man, everything really does becomes BI


If you want to build a big software business in data, there are also two ways to do it:

1. Build a BI product, and charge people to use it.

1. Build a new product. But start small, in a narrow niche—as, say, adata orchestration tool for developers.7Put iton Github; say it’s free, open source, forever. Create an online space for your users; call ityour community. Open issues; debate them; ask for contributions. Build in public—for the people; of the people; by the people.Then, eventually, inevitably,build a BI product, and charge people to use it:Dagster Labs has been cooking up something new: Compass, an analytics tool that makes it easier than ever to get insights from your data warehouse.


If you build an open source data orchestration tool, you will eventually want to charge money for it. If you build an open source data orchestration toolin 2025, not only will you eventually want to charge money for it; you will also realize that your toolunderstands business context, that business contextis what makes LLMs better at answering questions, and that people seem to pay a lot of money forchartsandchatbots. And so,there seem to be a lot of temptations.

[1](https://benn.substack.com/p/stuff-costs-money#footnote-anchor-1-172885854)

Ok, but whydidFivetran buy Tobiko? Is it to compete directly with dbt? My rough guess is, sort of?

1. Historically, both Fivetran and dbt were primarily used to move and transform data so that it could be used in reporting and analysis. Pull data from sources A, B, and C, transform it, and put a chart on top using some BI tool; that sort of thing.
2. Over the last few years, I’d imagine their customers are also trying to put AI applications on top of Fivetran and dbt. They want to move data between different apps so that bots in one can use data from another. They wanta context layer: Let A pull data from B and C, B from A and C, and so on.
3. Neither dbt nor Fivetran can quite do this yet, but both of them could reasonably claim that they’re the natural place for that functionality to exist. Fivetran hastwo-way connectionsto hundreds of software products; dbt has a platform for defining how all of those systems are related. If the point of a context layer is to intermediate communication between different bots and systems of record, it could be tempting for either Fivetran and dbt to be responsible for that intermediation.
4. With Tobiko, Fivetran could build a service like this, in which Fivetran directly facilitates data movement between tools. Which wouldn’t exactly compete with dbt’s core offering of transforming data inside of databases, but probably tries to solve a problem that dbt could eventually try to solve too.

[2](https://benn.substack.com/p/stuff-costs-money#footnote-anchor-2-172885854)

Shoutout to Matt Levinefor this whole temptation conceit.

[3](https://benn.substack.com/p/stuff-costs-money#footnote-anchor-3-172885854)

Butwhy?

[4](https://benn.substack.com/p/stuff-costs-money#footnote-anchor-4-172885854)

Shoutout toJosh Fergusonfor noticing this.

[5](https://benn.substack.com/p/stuff-costs-money#footnote-anchor-5-172885854)

This is how theOpenAI announcementof the transaction opens:


> Vijaye Raji to become CTO of Applications with acquisition of StatsigWe’re expanding our Applications leadership, the org responsible for how our research reaches and benefits the world.As we scale ChatGPT and build new applications to serve hundreds of millions of people and businesses around the world, our ambition is to push the frontier of AI research and turn it into intuitive, safe, and useful tools that people love. That takes strong engineering systems, fast iteration, and a long-term focus on quality and reliability.Vijaye Raji will step into a new role as CTO ofApplications⁠, reporting to Fidji Simo, following the acquisition of Statsig. As a hands-on builder and trusted leader, Vijaye will head product engineering for ChatGPT and Codex, with responsibilities that span core systems and product lines including infrastructure and Integrity.


And then, later:


> As part of this transition, we’re acquiring Statsig.


Normally, it would be very bizarre for a company to spend $1.1 billion tohire an executive, which is definitely how OpenAI frames this deal. But now, these sorts ofmegacquihiresare becoming routine. And if companies are paying billions to hire researchers, I suppose it makes sense to pay billions to hire executives to manage those researchers as well. (In contrast to everything here, Statsig’s own announcementmakes no mention of any of this, and instead offers theusual promisesabout “carrying the vision forward” and “joining forces” and how “customers will remain a top priority.”)

[6](https://benn.substack.com/p/stuff-costs-money#footnote-anchor-6-172885854)

According to Statsig’sterms of service, access to customer data is “restricted to employees and contractors who have a need to know this information to perform their job function. For example, to provide customer support, maintain infrastructure, enhance product or to understand how an engineering change affects a group of customers.” On one hand, this is all pretty boilerplate stuff, and what nearly every SaaS service says. On the other hand, every SaaS service says it because it’s permissive, and they want the right to sniff around.

[7](https://benn.substack.com/p/stuff-costs-money#footnote-anchor-7-172885854)

I’m a small personal investor in Dagster.
