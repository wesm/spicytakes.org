---
title: "2028 - THE GREAT DATA RECKONING"
subtitle: "A Macro Memo on the Collapse of the Data Industrial Complex"
date: 2026-02-24T22:04:21+00:00
url: https://joereis.substack.com/p/2028-the-great-data-reckoning
slug: 2028-the-great-data-reckoning
word_count: 3112
---


What if AI disruption hits the data industry hardest — and what if data professionals built the tools that made it possible?


What follows is a scenario, not a prediction.This isn’t a LinkedIn doom post or a subtweet aimed at your favorite data influencer. The sole intent of this piece is modeling a scenario specific to the data industry that’s been underexplored amid the broader AI displacement discourse. Our friends at Citrini Research published their “2028 Global Intelligence Crisis“ thought exercise in February 2026, and while it painted a compelling picture of economy-wide disruption, it treated the data industry as background scenery. We think it deserves its own post-mortem.


Because if anyone should have seen this coming, it was us. We built the dashboards. We had the data. We just never pointed it at ourselves.


Hopefully, reading this leaves you more prepared for the possibility that the industry you work in is simultaneously the most essential and most vulnerable layer of the AI economy.


This is the Reis Megacorp, Inc. Data Industry Memo from March 2028, detailing the progression and fallout of the Great Data Reckoning.


---


The unemployment rate for data professionals printed 14.7% this morning. Or 3.2%. It depends on which dashboard you check and whether the person who built it is still employed.


The irony is not lost on us. An industry that spent two decades insisting it could measure everything failed to see this coming, despite generating approximately 47,000 blog posts per quarter about “the future of data.”


Two years.That’s how long it took to get from “data is the new oil” to “data is the new asbestos — technically everywhere, occasionally useful, and the subject of a growing number of lawsuits about who’s responsible for cleaning it up.”


This memo is our attempt to reconstruct the sequence of events that brought the data industry from peak hype to what the Financial Times recently called “a $200 billion lesson in confusing infrastructure with value.”


---


## How It Started: The Tool Rapture


To understand what happened to the data industry, you first need to understand what the data industrywas, because in hindsight, it’s genuinely unclear whether anyone knew at the time.


By early 2026, the average enterprise data stack contained 37 tools. Not because 37 tools were needed, but because each one had a venture-backed sales team, a conference booth at Snowflake Summit, and a CEO who appeared on at least two podcasts per month explaining why their particular variety of moving data from one place to another was, in fact, transformative.


The Modern Data Stack — a phrase that somehow survived for years without anyone agreeing on what it meant — had become less an architecture and more a full-employment program for developer advocates. Every layer of the stack had between four and eleven funded competitors, each differentiated by increasingly theological distinctions. Was your data “transformed” or “modeled”? Was it “orchestrated” or “scheduled”? Was your catalog a “catalog” or a “discovery platform” or a “data intelligence layer”? Nobody knew. Everyone had opinions. The opinions were monetized.


The tool vendors operated in what economists would later call the “Conference-Content-Capital Cycle”: raise venture capital, sponsor conferences, produce content explaining why your tool was essential, use conference leads to close deals, and show revenue growth to raise more venture capital. The data never needed to be useful. It just needed to move, preferably through your product.


We knew this at the time. We just thought it was funny.


---


## The First Domino: When AI Agents Learned SQL


The Citrini Research team published their “2028 Global Intelligence Crisis” piece in February 2026, and while they got the broad strokes directionally correct — white-collar displacement, the feedback loops, the SaaS compression — they made the classic financial analyst mistake of modeling the data industry as if it were a single, coherent sector.


It wasn’t. It was three industries wearing a trenchcoat.


Industry 1: Data Tooling.The vendors. The SaaS companies are selling picks and shovels to the gold rush. This is where Citrini’s thesis landed hardest, and where they were most right.


Industry 2: Data Practitioners.The engineers, analysts, and scientists are doing actual work. This is where the story got weird.


Industry 3: Data Theater.The conferences, the content, the thought leadership, the LinkedIn engagement ecosystem. This is where the story got hilarious.


The first crack appeared in late 2026, when Claude, Gemini, and GPT became genuinely competent at writing not just SQL, but entire pipeline configurations. Not demo-quality. Production-quality. A product manager who had never heard of Airflow could now describe what they wanted in plain English and receive a working DAG, tested, documented, and deployed—in about 11 minutes.


This was, of course, the nightmare scenario that data engineers had been dismissing for years with the confident refrain: “AI can write code, but it doesn’t understand thebusiness context.”


They were right. AI didn’t understand the business context.


The problem was that a disturbing percentage of data engineers didn’t either. They understood dbt. They understood Snowflake. They understood the stack. What many had never actually done was sit with a business user and ask, “What decision are you trying to make?” The AI couldn’t answer that question, but neither could the junior data engineer whose entire career had been spent moving data from Postgres to Snowflake and back again because someone on Medium said it was best practice.


---


## The Bifurcation


By mid-2027, the data job market had split into two completely different realities.


The top 20%— engineers who understood data modeling, architecture, business context, and could make genuine tradeoffs — saw their compensationincrease. They became force multipliers. One senior data architect with AI tools could now do what previously required a team of eight. Companies didn’t need fewer of these people. They needed the same number, but each one was worth dramatically more. Salaries for principal-level data architects and engineers with genuine domain expertise exceeded $400K at multiple Fortune 500 companies.


The bottom 40%— engineers whose primary skill was knowing which YAML configuration made Fivetran talk to dbt, which in turn talked to Snowflake — discovered that this was, in fact, an AI-automatable skill. The tools they had built their careers around could now be configured by the very AI agents that had partially rendered them obsolete in the first place. A magnificent ouroboros of technological unemployment.


The middle 40%experienced something arguably worse: they kept their jobs, but at lower salaries, doing work that felt increasingly like supervising machines. “Data engineer” became “AI pipeline reviewer,” a role that consisted primarily of approving or rejecting AI-generated configurations and explaining to management why the AI’s work was only 94% correct and that the last 6% would take a human three days to fix. Management, having read an article about how AI was 10x more productive, could not understand why they were paying a human $150,000 to do 6% of a job.


Citrini’s article described a displaced Salesforce PM driving for Uber. The data industry equivalent was the mid-level analytics engineer who pivoted to “AI Data Quality Auditor,” a role that paid 40% less and consisted of staring at AI-generated data models and flagging the ones that joined on the wrong key. The AI was right 96% of the time. The auditor existed for the other 4%. The existential question of whether a human should be paid $90,000 a year to catch 4% of errors was left to the reader.


---


## The Great Tool Extinction


Citrini predicted SaaS margin compression. What they underestimated was thevelocityof compression in the data tooling market, specifically, because data tools had an additional vulnerability that general enterprise software didn’t: most of them were already somewhat unnecessary.


This sounds harsh. Let us be specific.


The Modern Data Stack had been built on a premise that turned out to be architecturally reasonable but economically indefensible: that every stage of moving data from point A to point B required a separate, funded, publicly traded (or trying to be) company. Ingestion was a company. Transformation was a company. Orchestration was a company. Quality was a company. Cataloging was a company. Observability was a company. Governance was a company. Each of these companies charged $50,000 to $500,000 per year. Each had a Slack community. Each had stickers. So many stickers.


When AI agents became capable of handling end-to-end multi-step data workflows, the question shifted from “which tool should we use for orchestration?” to “why do we have a separate tool for orchestration?” The answer, it turned out, was “because someone raised $40 million in Series B funding specifically for orchestration.” This was not a compelling answer.


The warehouse platforms — Snowflake, Databricks, BigQuery — survived and in some cases thrived, because they held the actual data. Everythingaroundthem entered a Darwinian elimination event. The long tail of data tooling lost 60-70% of its value in eighteen months. Not because the tools were bad, but because AI agents made thecategory boundariesbetween them meaningless. Why pay for separate ingestion, transformation, and orchestration tools when an AI agent treats the whole pipeline as a single optimization problem?


A data industry analyst (one of the few still employed) described it as “the tools didn’t die — the seams between them did.”


The venture investors who had funded 11 competing data observability startups were, in retrospect, not thrilled.


---


## The Content Apocalypse


Of the three data industries wearing the trenchcoat, the one that collapsed most completely was Data Theater.


By 2026, “data thought leadership” had become its own economy. Conference keynotes, Substack newsletters, YouTube channels, LinkedIn carousels, podcast appearances, vendor-sponsored webinars, “community” Slack channels that were actually marketing funnels. The data industry had more content creators per practitioner than any sector in technology, possibly in human history.


The content existed in a symbiotic relationship with the tool vendors: vendors paid for sponsorships, speaking slots, and “partnerships” that were functionally advertisements. Content creators (ourselves included — we have no illusions about our place in this food chain) produced material that ranged from genuinely useful to “what if I made a 47-slide LinkedIn carousel about why you should care about data contracts?”


When the tool vendors’ budgets collapsed, the content economy collapsed with them. Conference attendance dropped 60% between 2026 and 2027. The major data conferences consolidated from approximately 340 annual events to around 40. The Data Twitter/X/LinkedIn ecosystem, which had sustained hundreds of semi-professional influencers, contracted sharply.


Substack was littered with the remains of data newsletters that had been publishing tri-weekly hot takes about the future of the lakehouse since 2022 and suddenly had nothing to write about because the lakehouse had been automated by an AI agent that didn’t need to read their newsletter.


The few content creators who survived were the ones who had been writing about fundamentals, principles, and architecture rather than tools. It turns out that “understand the business problem before you pick a tool” is advice that ages well. “Here’s why you should migrate from Redshift to Snowflake in 2024” does not.


In a twist that surprised absolutely no one who had been paying attention, the people who had been loudly warning that the industry was over-indexed on tools and under-indexed on fundamentals were correct. They were also, in many cases, the ones still employed.


---


## What Citrini Got Right


The broad thesis of the intelligence premium unwinding was correct, and it hit data professionals harder and faster than most white-collar categories because of an uncomfortable truth: a large portion of data work wasalreadycloser to “following documented procedures” than “exercising irreplaceable judgment.” The industry had spent years building tools that abstracted away complexity, which made the work more accessible and automatable. The tools designed to democratize data work succeeded — they just democratized it first for machines.


The negative feedback loop was real. Data tool vendors cut their own data teams, reducing their need for their own tools and revenue, which in turn required more cuts. Data consultancies saw project cancellations accelerate as clients realized they could use AI agents to do the migration work the consultants had quoted at $2 million.


The wage compression dynamic was brutal and accurate. Displaced data engineers flooded adjacent roles — business intelligence, reporting, analytics — pushing down wages across the entire spectrum. A senior data engineer from a Series C startup who’d been making $200K found themselves competing for a $95K BI analyst role against 400 other applicants, half of whom were also displaced data engineers.


And the mortgage point, while dramatized, had a kernel of truth in tech-heavy metros. Data professionals in San Francisco, Seattle, and Austin had taken on housing costs calibrated to tech salaries that no longer existed. The “$180K product manager driving Uber” from Citrini’s piece had a direct analog: the $195K senior data engineer now doing contract Fivetran-to-Airbyte migrations for $65/hour, wondering whether this counts as the “reskilling” that McKinsey had promised would happen.


---


## What Citrini Got Wrong


First, the timeline.Citrini compressed everything into two years. In the data industry, the disruption was both faster and slower than predicted. Faster in tooling (the vendor shakeout was genuinely rapid). Slower in practice (enterprises are still running Informatica jobs from 2014, and those jobs will outlive us all). The gap between “AI can replace this” and “this Fortune 500 has actually replaced it” turned out to be filled with procurement processes, SOC 2 audits, change management committees, and a VP of Data who was not going to admit that the $3 million Snowflake contract he championed was now being questioned.


Second, they underestimated the cockroach resilience of legacy systems.The entire article assumed a world where enterprises make rational decisions at the speed of technology. In reality, the data industry’s biggest job preservation program turned out to be technical debt. Companies that had spent fifteen years building Rube Goldberg data architectures couldn’t just replace them with AI agents, because the AI agents looked at the architecture, tried to understand it, and experienced what we can only describe asmachine confusion. The AI could build a new pipeline from scratch in hours. Understanding why the existing pipeline had a hardcoded filter that excluded all transactions from New Jersey on Tuesdays? That required a human who’d been at the company since 2016 and vaguely remembered a conversation with a business analyst who had since left.


Third, they completely missed the data quality crisis.As companies rushed to deploy AI agents across their operations, they discovered something the data industry had been quietly screaming about for a decade:their data was terrible.AI agents are only as good as the data they consume, and most enterprise data was a patchwork of duplicates, missing values, conflicting definitions, and tables named final_v2_FIXED_actually_final_USE_THIS_ONE. The AI displacement wave generated a counterwave of demand for data quality, governance, and stewardship, partially offsetting job losses in other areas. Not enough to prevent net displacement, but enough to make the picture more complicated than “everyone gets fired.”


Fourth, and most fundamentally, they treated the data industry as a subset of the software industry.It isn’t. Or rather, it wasn’t. The data industry has always been partly a consulting and services industry, wearing a software costume. The value wasn’t just in the tools or even the engineering — it was in understanding messy, ambiguous, organization-specific business logic that defied clean automation. The data teams that survived weren’t the ones with the best tools. They were the ones who had spent years building institutional knowledge aboutwhythe data looked the way it did.


It turns out that “tribal knowledge” — the thing every data governance framework promised to eliminate — was the one thing AI couldn’t replicate. The data professionals who had been hoarding context in their heads rather than documenting it in Confluence were, against all principles of good engineering practice, the most secure in their jobs.


We are not sure what lesson to draw from this.


---


## Where We Are Now


The data industry in March 2028 employs roughly 40% fewer people than it did in January 2026. The people still employed are, on average, more senior, better compensated, and do work that bears little resemblance to what a “data engineer” did three years ago.


The job title “data engineer” still exists, but the role has shifted so dramatically that someone from 2024 wouldn’t recognize it. Modern data engineers spend perhaps 10% of their time writing code or configuring tools. The rest is architecture, governance, business translation, AI supervision, and what one practitioner memorably called “being the last human who knows where the bodies are buried in the data warehouse.”


The tool landscape has consolidated from 400+ vendors to perhaps 80, with the major cloud platforms absorbing most functionality. The surviving independent vendors are the ones that solved genuinely hard problems — real-time processing, complex event processing, domain-specific data challenges — rather than the ones that put a UI on top of SELECT * FROM.


The conference circuit is a shadow of its former self, which is not entirely a bad thing. The remaining conferences are smaller, more technical, and notably free of the “data mesh vs. data fabric: FIGHT” panel discussions that defined the 2022-2025 era.


And the thought leaders? A few pivoted successfully. Most discovered that their audiences had been a function of their ecosystem’s size rather than their individual brilliance. The ones who survived were those who had been saying things that were true rather than popular.


The smartest thing anyone said during this entire period came from a data Substacker and educator/author in Salt Lake City who, when asked in early 2026 what data engineers should do to prepare for AI disruption, replied:“Learn what a business is.”


We wish more people had listened.


---


But you’re not reading this in March 2028. You’re reading it in February 2026.


Your Snowflake bill is still $400,000 a quarter. Your team still has 12 people. Your backlog still has 200 tickets. The dbt models still run every morning, and someone still pages you when they break at 3 AM.


The disruption hasn’t started. Or rather, it has, but it still feels like a LinkedIn discourse rather than a restructuring notice.


You still have time to become the kind of data professional who survives this. The one who understands the business, not just the stack. The one who can explain why the data looks the way it does, not just how to move it somewhere else.


The fundamentals haven’t changed. They never do. That’s why they’re called fundamentals.


The tools, on the other hand…well. You know what’s coming.


---


Subscribe for more dispatches from the end of the world as we knew it.


Thanks for reading! Subscribe for free to receive new posts and support my work.
