---
title: "BI’s third form"
subtitle: "Help us with the hard thing."
date: 2024-04-26T16:51:00+00:00
url: https://benn.substack.com/p/bis-third-form
slug: bis-third-form
word_count: 2536
---


![Which font do they use for these parking signs? And are there maybe  look-a-likes? : r/identifythisfont](https://substackcdn.com/image/fetch/$s_!MZeW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fb09856-c289-498c-b17a-e1e6b526a749_1080x1080.jpeg)

*We can read the signs, but we don’t know what they mean.*


Ten years ago, if you were a jaded forty-something-year-old tech executive, you bought a Porsche and a house in Jackson. You opened a bar in Oakland, or a coffee shop in Mill Valley. You learned a lot about woodworking, Patek Philippe, and divorces. You Benjamin Buttoned yourself—gothair plugs, dressed down bytwo generations, andmet your new 28-year-old fiancée in the middle.1


Today, there are new fads. Today, every jaded forty-something-year-old tech executive has one of three ambitions:

1. Buy some HVAC businesses. Or laundromats. Or family dental offices. “Tech startups are all childish hype,” you say. “They’re kids playing company. Did you know that car washes have a 12 percent EBITDA margin, but are valued at only 3x revenue? I’m raising a $25 million SPV to roll up all the regional car washes in north Florida,2streamline back office redundancies, optimize their digital marketing strategies, introduce a new recurring subscription service, and leverage AI.” You tell your investors that you have a network of experienced industry veterans as advisors, but you know that you won’t need them. You were the CRO of an enterprise infrastructure security company that sold to half of the Fortune 500; how hard can car washes be?3
2. Start a venture studio. “I’ve got a lot of great ideas, but my time is too valuable to gamble it all on just one company. Instead, I’ll incubate a bunch of startups in a venture studio, figure out the best one, and then hire a young, ambitious CEO to take it over. I’m more of a zero-to-one founder; my superpower is strategy and product vision. It’s not that I don’twantto do the work—Jensen Huang and I have both been saying this for years—it’s just that it would beinefficient.”4
3. Bootstrap an AI startup. “Did you seeSam Altman saythat somebody will soon build a one-person billion-dollar company? I wasn’t going to do another startup, but AI changes everything. In my twenties, I cared too much about fundraising announcements and which VC invited me to which parties. That stuff is all a distraction. This time, I want to keep the company lean, focus on profitability from the beginning, and own as much of it as I can. I don’t know what I’m going to build yet, but ChatGPT and I are talking through it.”5


For most people, these are the inevitable attractions. However, if you’re a jaded forty-something-year-old tech executivefrom a data company, you might be tempted by a fourth option: Build a data product, for a specific vertical.


For you, after having spent years making operational middleware for data teams, the grass (and money) in other departments is starting to look greener. “Analytics teams are cost centers,” you might say, “Their budgets get cut too quickly. We have to sell customers on our productandon the value of their data teams. Rather than making yet another BI tool, wouldn’t it be easier to create an analytics application for ecommerce marketing departments? Or a sales forecasting app? I want to get back to the basics—helping the actual business people who provide actual business value.”


In the analytics market, this our version of thebundling and unbundling pendulum. We makegeneric BI tools; we makedepartment-specific applications. When we get tired of making “custom tools [that] help others look at very narrow, specific datasets,” wemake more generic BI tools; then we makedepartment-specific applicationsagain.


Over most of the last decade, general-purpose tools were the cool thing to build. Rather than tracking, storing, and reporting on product usage in Mixpanel and tracking, storing, and reporting on sales metrics in Salesforce, we tried to store all our data in one centralized warehouse, and reporton all of our data using a universal analytics layer. This was one of the motivating beliefs behind the modern data stack:Pivot the vertically-integrated tools sideways, and replace them with horizontal platforms.


Ah, whoops.So now we’re swinging back the other way, and business apps are trendy again. Between 2023 and 2024,Matt Turck’s data landscapegrew by 42 percent, from 1,416 companies to 2,011 companies. The general-purpose analytics categories—BI, data visualization, and data analyst platforms—grew by only 26 percent, but domain-specific categories—product, sales, marketing, finance, HR, legal, and customer experience—grew by 56 percent.6


It’s the circle of life in Silicon Valley: Bundle, unbundle; centralize, decentralize; pivot horizontally, pivot vertically. Build multipurpose analytics and BI platforms that are sold to data teams; build domain-specific tools that prestructure common departmental data sources and predefine popular business metrics. Do your analysis freehand; trace a ready-madetemplate. Alternate between the two forms of BI. Though each cycle works a little better than the last, nothing fundamentally changes.


# Generally accepted analytics principles


There’s another way to describe this oscillation. Afriend of mine7has a theory that all enterprise software should do one of two things:

1. Give people tools to creatively express their ideas, and enable them to be experts in their craft.
2. Keep them from screwing up.


Final Cut Pro and Photoshop are the first type of tool. They make it (relatively) easy for filmmakers and artists to turn the ideas in their head into images on a screen. But Final Cut doesn’t tell editorshowto make those images, and Photoshop doesn’t box in designers around some Adobe-imposed best practices. These tools, and tons more like them, are microphones for their users’ skills—they both amplifygreatness, and are unforgiving ofmistakes.


We use the second type of software for protection. People need to pay our taxes; TurboTax fills out their forms and makes sure they’re right (powered byTurboTax® CompleteCheck™!). Managers need to keep their teams aligned around a set of goals; Lattice not only helps them track those goals, but encourages that they do it in avery particular way. If you try to use Lattice to manage people using somederanged goal-settingframework instead of one they sanctioned, the tool will get in your way. And that’s the point—to tell us what to do, and protect us from our creative flights of fancy.


In the data market, open-ended products like Mode, Hex, and even Excel fit into the first category. These tools give analysts code editors and spreadsheets, and let people do whatever they want with them—model quarterly discounted future cash flows,paint pictures,nuke the global economy, whatever. They’re products for quantitative creativity.


BI, however, is more complicated.Most BI tools have two major components: first, a data model in which people define metrics, and how they should be calculated; and second, an interface where people choose which metrics they want to see and how they want to visualize them. The former thing defines the rules that govern the latter thing.


This creates two different experiences, depending on who you are:

1. If you’re the person who’s trying to answer questions—like an executive who wants to know how much money you made last quarter, or a marketer who wants to see how an ad campaign is performing—BI tools are designed to keep you from messing up. You can only look at a list of predefined metrics, and you can only explore those metrics in pre-approved ways. Just as Lattice is meant to keep managers from improvising how they set goals, BI tools are designed to keep people from creatively expressing what revenue means to them. There are lines, and you have to color in them.
2. If you’re the persondefiningthe metrics, however, you can do whatever you want. If you want todefine your financial metricsin an insane way, your BI tool probably won’t nudge you toward a more generally accepted definition.8Nobody is watching the watchmen.If ananalystwants to creatively express what revenue means tothem, they can.


Most domain-specific templates and data tools—the stuff we’re flirting with again, now—transform the second “creative” experience into a more governed, “protected” experience. For example, Google Analyticsdefines sessionsautomatically, according to some unchangeable internal logic. PostHog, a product analytics tool, calculatesretention cohortsbased on some methodology of their choosing.SaaSGridhas “all the pre-built transformations you need: Date ranges, Live vs Contracted ARR, Trailing Average, Retention Baselines, S&M:Sales Offsets, Expenses Segmentation.”


That’s one way to think of the BI pendulum. When data teams are popular, generic BI tools are popular, because they give analysts more freedom to define the rules. When data teams fall out of favor, domain-specific tools—which outsource those rules to the product’s designers—start to look more appealing.


Which, as a pattern of behavior, I guess makes sense. But I’m not sure it’suseful.


Most of these tools are trying to find the right balance of protection and creativity in how data is modeled and how metrics are defined. The implicit theory here is that companies struggle to turn messy data into consistent and appropriate metrics, and if we can combine the right mix of opinionated best practices with flexible customization, we can all become thedata-driven enterprises that we’ve been promised.9


The problem, however, is that this isn’t what makes successful data-driven companies successful. Amazon isn’t Amazon because it’s great atdefiningmetrics. It’s Amazon because it’s great atinterpretingthem. Sure, sometimes wemiscount how many pizzas we sold, orconflate gross margin with contribution margin. But these aren’t the places where most of us need the most help. We’ve spent thirty years building tools to help us answer our questions. The much harder thing is knowing what to do with those answers once we have them.


# Opinionated business interpretation


A couple weeks ago, Cedric Chin and Sam Taylorlaunched a new tool, called Xmrit, for creating XmR charts. We talked about these chartsa few months ago: They’re a type of time-series chart that uses a handful of simple heuristics to tell you when up-and-down variations are worth paying attention to. It’s a data visualization that tells you how to interpret its results.


In other words, Xmrit is a BI tool that protects you frommisunderstandingdata. There is no restriction on the data that goes into the tool—you can copy and paste any numbers that you want. But once those numbers are in Xmrit, it has strong opinions about how you should interpret them.


Most BI tools are the inverse. They govern inputs, and provide no guidance on how to make sense of the outputs. And so we screw it up. We screw it up because data interpretation is hard; becausethe line wiggles; becausemost analysisis just squinting anddirectional vibes.


Xmrit and XmR charts are one example of what a new approach could look like. There are others:

- Metric trees.Metric treesare a structured set of business metrics that are intended to represent how a company actually functions. A revenue metric tree, for example, might break revenue into subcomponents like number of purchases and average revenue per purchase; the number of purchases might then get split into new customer purchases and repeat customer purchases; and so on. Interpretation is baked into metric trees: When a metric changes, walk down the tree to figure out why it changed.
- The one-page BI tool. A few years ago,Dave Kellogg published the one Excel worksheetthat he recommends startups use to monitor their sales pipeline. It’s a dense table of specific metrics presented over specific time periods. This sort of tightly-defined BI tool—in which the structure and content is not up for debate—forces people to compare metrics in a particular way, and not prevents them wandering aimlessly through different filters and drilldowns.
- ARIA, GEM, etc.ARIAis a framework for measuring and improving product adoption.GEMis a framework for describing how companies grow and make money. Though both of them are built on top of common-used metrics, they’re valuable because they tell people how to make sense of those metrics. They are frameworks for metric interpretation, not metric definition.


Just as tools likeLinearare unafraid to tell us how we should build software, BI tools could be bolder in telling us how to think about our business. Tell us how to interpret a time-series chart; force us to think about decomposing our business into its important components; give us a rigid summary table of our business that encourages us to debate what we do about the numbers on the page and now how we graph them; impose frameworks on us, and make us choose one.


Of course, not every model would be right for every company; Linear’s probably not right for everyone either. But that seems like a better way to buy software—choose it for its strongest opinions, not for its generic features.


If I had to guess, all of this is the real reason why BI toolsare a tar pit:10They solve the wrong problem. They’re focused on protecting us from bad inputs, and don’t do nearly enough to stop us from screwing up the outputs. And until one does that, we’ll keep feeling frustrated, keep churning through tools, and keep wondering why nothing seems to work.


Maybe it’s time to try another approach. Stop giving us more exploratory interfaces to get lost in. Stop waiting for us to become “data literate.” Assume we aren’t, and won’t be for a long time. If we were jaded aboutthat, what would we build then?11

[1](https://benn.substack.com/p/bis-third-form#footnote-anchor-1-144044675)

Yes, this is gendered, but ten years ago (and today, but ten years ago too), tech executives werealmost all men. Back then, if you were a jaded forty-something-year-old techfemaleexecutive, you were probably Sheryl Sandberg, Marissa Mayer, or Meg Whitman.

[2](https://benn.substack.com/p/bis-third-form#footnote-anchor-2-144044675)

Florida?Florida!!!I need to forget, so take me to Florida! I've got some regrets, I'll bury them in Florida! What a crush, what a rush, fuck me up, Florida!

[3](https://benn.substack.com/p/bis-third-form#footnote-anchor-3-144044675)

Hard, it turns out. Yourcorporate rebrandruins each car wash’s quirky charm; customers are upset that the owner Cheryl got replaced by a carpetbagger, and that shop attendant Donna got replaced with an iPad. You eventually realize that you don’t know anything about car washes and that Cheryl actually ran a very tight ship. You end up selling all the car washes toa real private equity firmat a loss, and become the CRO of an enterprise AI security company.

[4](https://benn.substack.com/p/bis-third-form#footnote-anchor-4-144044675)

You never start the venture studio. There were lots of good meetings. We all got excited.The whole thing we got excited about is never going to happen.

[5](https://benn.substack.com/p/bis-third-form#footnote-anchor-5-144044675)

Ok, fine, this one might actually be kind of fun.

[6](https://benn.substack.com/p/bis-third-form#footnote-anchor-6-144044675)

Another way tolie with statistics: Make a point and confidently back it up with some mostly irrelevant numbers.

[7](https://benn.substack.com/p/bis-third-form#footnote-anchor-7-144044675)

This blog is 25 percent Griff hype (speaking of, a new album!Announced yesterday!Out on July 19!), 35 percent overwritten ledes about venture capitalists, and 40 percent ideas that I stole from Nan.

[8](https://benn.substack.com/p/bis-third-form#footnote-anchor-8-144044675)

Or if youdo “not currently, and may never, collect, monitor or report certain key operating metrics used by companies in similar industries” and your management and board “does not anticipate relying on any particular key performance metric to make business or operating decisions,” your BI tool won’t care either.

[9](https://benn.substack.com/p/bis-third-form#footnote-anchor-9-144044675)

Omni, a new BI tool, makes this argument pretty explicitly. They have a Venn diagramon their homepagethat positions Omni as being a combination of being flexible and governed;they saythey’re the “only business intelligence platform that combines the consistency of a shared data model with the speed and freedom of SQL.”

[10](https://benn.substack.com/p/bis-third-form#footnote-anchor-10-144044675)

Well, that anddata visualization black hole.

[11](https://benn.substack.com/p/bis-third-form#footnote-anchor-11-144044675)

I mean, we’d probably a startup studio for incubating AI companies.
