---
title: "AI companies are just SaaS companies"
subtitle: "Is OpenAI a wrapper around ChatGPT?"
date: 2024-12-20T18:18:42+00:00
url: https://benn.substack.com/p/ai-companies-are-just-saas-companies
slug: ai-companies-are-just-saas-companies
word_count: 2233
---


![Theranos and Elizabeth Holmes: What to Read, Watch and Listen To - The New  York Times](https://substackcdn.com/image/fetch/$s_!h8bR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f658515-29c6-444e-955c-f38e73f5049c_2048x1365.jpeg)

*A popularSiemens wrapper, valued at $9 billion.*


If you're a distressed data startup—the fifth maker of anaccidental BI tool, the fourth-biggest data observability platform, a data catalog that’s been through three pivots and two bridge rounds—you probably have a spreadsheet of companies that might acquire you. Some of the names on it are the megacorporations you said you were going to disrupt; some of them are competitors;1some of them are prehistoric conglomerates—Infor, Pentaho, ZoomInfo, Quest—that are collectively labeled “Legacy” or “Tier 3” or “the Borg.”


Inevitably, Amazon is also on your list, as a Tier 1 target. They have75 billion dollarsin cash under their mattress, they’re a prestige buyer,2andit just makes sense. They make theworld’s best bare computing metal, but offer only a handful ofbasicapplications on top of it. QuickSight, Amazon’s half-hearted attempt to build a BI tool, hasn’t bothered to make a new product video in almost six years.3CloudWatch, a tool for monitoring AWS logs,is of the devil. Redshift is a has-been; Athena is a never-was. Acquisitions are all about adding one plus one to get three. Amazon already sells billions in data infrastructure platforms; imagine how much more they could sell if they paired it with your G2-leading, Product Hunt-delighting Data Discovery Platform for the Modern Business Cloud™.


Just as inevitably, they’re not going to do that. No matter how cozy you get with their corporate development team, Amazon won’t buy your data discovery platform. They don’t care about your passionate set of 150 customers; to them, the equation is not 1 + 1 = 3; it’s 1 billion + 1 = still 1 billion, basically. And while itseemslike cloud providers like Amazon would want to put some snazzy apps on top of their lower-level computing services to entice people to buy those services from them and not Google, theydon’t need to do that either:


> The “software layer on top” is getting incredibly competitive. There's so many startups going after it, fueled by cheap VC money and willing to burn billions of dollars on building software.Cloud vendors might be pretty happy making money just in the lowest layer. Margins aren't so bad and vendor lock-in is still pretty high.


I’d add a third point to Erik’s list: The cloud providers’ competitive advantage in cloud computing is enormous. AWS isn’t just good software; it’s200 data centers, each costing billions of dollars to build.4Microsoft built 300.Google’s data centersare connected by “more than 3.2 million kilometers of terrestrial and subsea fiber.” These companies’ moats aren’t their amusing UIs andoh-so-relatablebrands; they are literal moats, dug into the Oregon bedrock and Pacific Ocean seafloor. With or without your data discovery platform, they will all be fine.


But another company on your acquisition list is Databricks. They probably won’t save you either—whenhundreds of modern data stack startupsarerunning out of money, the onewith 10 billion dollarsis probably getting a lot of casual calls from founders who just thought it might be a good time to catch up—but theymight. Because, unlike Amazon, Databricks’ nucleus isn’t a half-trillion dollars worth of buildings and computers and wires; it’s afree database. From theWall Street Journal,reporting onDatabricks’ recent fundraise:


> In January 2016, Ghodsi succeeded Stoica [ as Databricks’ CEO], who returned to academia. At the time, Databricks charged for a more user-friendly version of Spark [ an open-source data processing engine, akin to a database ] but was struggling to find large customers who would pay for it. Many were still downloading the software free off the internet.The challenge became clear when a potential customer asked Ghodsi and another co-founder for a selfie before a meeting. When the pair later asked whether he would be willing to pay $10,000 for the software, the customer scoffed. “Why would we ever pay $10,000?” he said. “I’m just going to get it for free.”Under Ghodsi, Databricks added new features to Spark that were only available to the startup’s paying customers. He then hired hundreds of salespeople to sell it to companies, targeting business giants like Capital One and JPMorgan.


Which, yes, of course—when the thing you’re selling is free software, you build a bunch of special things on top of it that make it better, easier, and more blinged out. If the thing you are selling is access toa nuclear submarine full of computers, you don’t need to do any of that. You cannot download a nuclear submarine from the internet.


Anyway, here’s a question I’ve wondered for a while: Which one is OpenAI?


There are arguments for both. It’s like Amazon: While OpenAI isn’t selling its customers access to data centers (yet), it is selling access to a proprietary model that they’ve spent billions of dollars creating. No, it’s like Databricks: People can download (almost) that modelfor free off the internet. Actually, it’s still like Amazon: Even if the model is free, you need a bunch ofreally expensive computersto run it, and those computers arenotoriously hard to buy. Which makes it Databricks: The companies that are like Amazonare the ones leasing serversfull of those computers, and OpenAI is just a fancy application running free software on top of other people’s rented computers.


My guess is that both sides are right; it just depends on when you ask the question. Initially, OpenAI was Amazon: They were the sole gatekeepers to an incredibly popular service that had lots of imitators, but none of them, least of all the free ones, were convincing replacements. Aserver rack in a garageis not the same as a2 billion space station; theearly Alpaca modelswere noticeably worse than the leading ones from OpenAI.


But it seems like that gap is collapsing. The current models arepotentially plateauing, and it’s becoming more and more expensive for OpenAI to take smaller and smaller steps forward. And there isno longer an obvious way to play defense:


> What, then, is an LLM vendor’s moat? Brand? Inertia? A better set of applications built on top of their core models? An ever-growing bonfire of cash that keeps its modelsa nose aheadof a hundred competitors?


This morning,OpenAI finished upthe “12 Days of OpenAI,” a two-week launch blitz in which they released a new feature for twelve straight weekdays.5One was anew model, of sorts;6a handful of them were updates to underlying models, but most of them were, to use the slur that we’d use if anyone else built them, wrappers around ChatGPT: There were multiple integrations with iOS and Apple’s desktop apps; there was a way to call ChatGPT on a telephone; there wasCanvas, a document editor with shortcuts that ask ChatGPT to suggest edits, to make sections shorter or longer, and to add,repulsively, emojis; there wasProjects, which are folders for your Canvases.


I have no idea how much OpenAI cares about these features. Maybe they’re demo apps, meant to show other companies what OpenAI wants them to build on top of ChatGPT. Maybe they’re hack day projects that got shotgunned out the door for the sake of a Christmas carol. Maybe they’re part of no plan at all, and what happens when you give a bunch of engineers18 billion dollarsand tell them to make asimple chatbot UI better.


Still, it’s hard not to wonder if some of these features, especially the now-ubiquitous Notion aesthetic—a minimalist pageless word processor; a few preset font and style options; a left sidebar of “pages” or “projects” or “collections” or some other shapeless noun that unnecessarily rebrands “folders” and “documents;” emojis, again—are the first few foxholes in OpenAI’s ultimate moat: A better set of applications built on top of their core models. Or, more precisely, these features are ways to make models more convenient to access and ergonomic to use. OpenAI can no longer just entice us with foundational infrastructure and anaccidentally successful chat app; they’re now trying to sell us commoditized tech and an increasingly complicated SaaS app.7


Consider the arc of AI-powered coding assistants. The first popular one was GitHub Copilot, which was built on aheavily modified version of an early OpenAI model. Then, Cognition’s Devin, a coding environment combinedwith a custom model, was trendy. Now, it’sCursor, which is muchmore of a SaaS app than AI model:


> …the problem to solve is not how to make LLMs perform well in isolation, but how to make them perform well alongside a human developer.We believe, therefore, the interface between programmers and AI models will soon become one of the most important pieces of the dev stack. …Cursor is a fork of VS Code that’s heavily customized for AI-assisted programming. It works with all the latest LLMs and supports the full VS Code plugin ecosystem. What makes Cursor special are the features designed to integrate AI into developer workflows.


In other words, people want the better software product, not the better model. Which is ironic, I suppose. Silicon Valley has spent the last two years trying to figure out which AI companies are real, and which are just wrappers around ChatGPT. In the end, though, the wrappers may be the only thing that matters—even for OpenAI.


—


Or, alternatively, here is my proposal for Sam Altman:

1. Fire everyone.
2. Shut down all of OpenAI’s research programs.
3. Start sending people’s ChatGPT prompts to Claude, or Gemini, or some server running Meta’s open source Llama model.
4. Don’t tell anyone.


I mean, step 3 is probably fraud, and step 4 would be hard for a company withseveral dozen subredditsdedicated to it. And even if you put those aside, I’m sure that some people would say, no, no, this would never work; people would notice. ChatGPT is the best model, and OpenAI is on track to make11.6 billion dollarsnext year because people want to use the best model.


Except—ChatGPT might notbe the best model. Satya Nadella, who mightown OpenAI, said that leading modelsaren’t all that essential anyway.8And ifnobody can tell the differencebetween human paintings and AI paintings, I’m skeptical that many people can tell if their book report onThe Great Gatsbywas written by GPT-4o or Gemini 1.5 Flash.


Instead, it seems much more likely that OpenAI is going to make 11.6 billion dollars because ChatGPT is popular. It became synonymous with AI, the leading company that no CIO gets fired for buying, and the website that every high schooler has bookmarked. It’s going to make 11.6 billion dollars because it’s got the bestbrand. Two years ago, people’s enthusiasm for OpenAI’s brand was built on their enthusiasm for OpenAI’s products. Now, the brand leads, and the product—which is getting awfully expensive to build—follows.


So how do you keep the brand without burning billions to build an undifferentiated product?Pull a Theranos, and send every ChatGPT prompt to someone else’s Siemens machine rather than their own proprietary one. Nobody’s gonna know.How would they know?

[1](https://benn.substack.com/p/ai-companies-are-just-saas-companies#footnote-anchor-1-153418501)

I.e., the fourth maker of an accidental BI tool, the third-biggest data observability tool, and the data catalog company that’s only been through two pivots and taken one bridge round.

[2](https://benn.substack.com/p/ai-companies-are-just-saas-companies#footnote-anchor-2-153418501)

Maybe a topic for another day, but acquisitions really are a prestige thing. Sell for 500 million dollars in cash a swashbuckling private equity firm? You’re a mercenary; a cheap businessman; something must’ve gone. Sell for 400 million dollars in equity to somehyped-up AI company? A tremendous win; this is why we build.

[3](https://benn.substack.com/p/ai-companies-are-just-saas-companies#footnote-anchor-3-153418501)

The primary element on theQuickSight landing pageis not only a YouTube video from early 2019; it’s a YouTube video that’s primarily stock video of “happy professionals in chic office collaborating on computers,” withsloppy screenshotsof “SpaceNeedle-Alpha”—the codename for QuickSight, I guess—badly superimposed over a people’s monitors.

[4](https://benn.substack.com/p/ai-companies-are-just-saas-companies#footnote-anchor-4-153418501)

In a filing in Oregon,AWS said thatthe buildings cost about $300 million, and the equipment in the buildings—a bunch of computers, presumably—costs $1.95 billion.

[5](https://benn.substack.com/p/ai-companies-are-just-saas-companies#footnote-anchor-5-153418501)

According to Sam Altman, “as far as we know, no tech company has done before.”According to Sam Altman’s ChatGPT, tech companies have definitely done this before. Which I know is true, because Modedid this before. Though technically, Sam Altman is right; we didn’t release one feature for 12 straight weekdays; we released one feature for twelve straightcalendardays. (More like 12 straight weakdays, amirite?) (But in fairness to OpenAI, they don’t haveEmily Ritter—the sort of marketer who’s always a lap ahead of everyone else; who knew that your accidental BI tool was a BI tool years before you did; who you could t-bone with bad ideas that got proven wrong so quickly, and revealed her ideas to be right so quickly, that you were the one who got whiplash—running their launch.)

[6](https://benn.substack.com/p/ai-companies-are-just-saas-companies#footnote-anchor-6-153418501)

The o-series models seem a bit hard to classify, because they aren’t completely new foundational models like the GPT-series models are. They also include internal “reasoning” strategies that, very roughly, let the foundational model iterate its way through a problem. Is that a new model? To a user, who doesn’t really care how it works, probably. To an AI researcher who’s trying to find the limits of LLM pre-training? Probably…not really?

[7](https://benn.substack.com/p/ai-companies-are-just-saas-companies#footnote-anchor-7-153418501)

Though that SaaS app is also becoming commoditized? OpenAI’s Projects feature is more or less a clone of Anthropic’sProjects feature, and Grammarly, which is ChatGPT wrapper-ish,just bought Coda, which is Notion-ish.

[8](https://benn.substack.com/p/ai-companies-are-just-saas-companies#footnote-anchor-8-153418501)

Importantly, note that this isn’t saying new models won’t get better. It’s saying that new models aren’t a durable advantage. Even if something like today’s o3 release is a big step forward, others companies will surely have roughly equivalent versions of the same thing soon.
