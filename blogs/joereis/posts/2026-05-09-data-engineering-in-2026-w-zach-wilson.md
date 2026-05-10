---
title: "Data Engineering in 2026 w/ Zach Wilson"
subtitle: "The Weekend Windup #32 - Cool reads, events, links, and more"
date: 2026-05-09T11:29:12+00:00
url: https://joereis.substack.com/p/data-engineering-in-2026-w-zach-wilson
slug: data-engineering-in-2026-w-zach-wilson
word_count: 1333
---


![](https://substackcdn.com/image/fetch/$s_!YRJ8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F688e95e8-c24c-4d08-ac6e-c597baa7e07a_1200x627.jpeg)


Are your Snowflake costs going crazy? Most data teams spend months analyzing Snowflake costs. You can reclaim up to 50% of yours in just hours.


Talk to aRevefi experttoday


Thanks toRevefifor partnering on this newsletter.


---


# Data Engineering in 2026 w/ Zach Wilson


I was on a rooftop in Stockholm last night with Zach Wilson recording an impromptu Freestyle Friday podcast, and somewhere between the sunset and the third spicy take, we hit on a few things worth pulling out of the transcript. This post will be a little different, as I’m stepping out of the limelight and instead sharing some of Zach’s thoughts.


## Surprise (/s) - AI is Happening Outside of SF


Zach toured the Lovable office and walked away thinking the Bay should be nervous. The first cafe he stepped into in Stockholm sounded like Hayes Valley - laptops everywhere, the word “agent” tossed around five times in his first hour. Lovable has the revenue numbers to back the energy. The vibe is real.


San Francisco has been running the same line for a decade:we’re the only city doing AI right.That story is breaking (I’m also seeing this in various parts of Europe and Asia). Stockholm has the talent, the energy, and (Zach’s words)  the mental health that comes from “get rich and maybe relax in the social safety net” rather than “get rich or die trying.”


## Where to Focus in 2026


If you’re a founder or an engineer trying to figure out where to be, the map has more dots on it than the narrative suggests. But the part I want to dwell on is data engineering, since that’s what Zach and I are best known for. Here are some of Zach’s takeaways.


First, dashboards are cooked. Those jobs aren’t disappearing tomorrow. But they’re going to pay less, and they’re not where you want to be. Building a Tableau viz so an exec can stare at it for ten seconds is not a future-proof career. The work has moved on.


The Three Vs are your moat. Here’s Zach’s framing, and it’s the cleanest I’ve heard. Volume, velocity, variety. The more of these you work with, the safer your role.

- Volume. Big data doesn’t fit in AI’s context windows. If you’re moving petabytes, the model can’t just eat your job for breakfast.
- Velocity. Real-time has too many gotchas. Kafka, ClickHouse, streaming systems, and AI isn’t there yet. Long runway.
- Variety. This is the big one. Rows and columns are the past. PDFs, images, audio, transcripts (like the one this post came from) - that’s the work that matters now. The more your pipelines handle messy, multimodal stuff, the more leverage you have.


If you’re a data engineer working only with low-volume, batch, structured data, you are exposed. Pick a V and go deep. Preferably, stack two of them.


## For People Just Starting Out - Build Things!


I get this question constantly. So does Zach. We landed in the same place. Reading is great, but building is better. Even though I wrote the book, I’ll tell you straight up that books are not enough. Ask Claude to help you build an orchestration tonight. Move some data. Break it. Fix it. See what happens. Fundamentals matter, but they only stick when your hands are on the thing, building it. Thankfully, AI makes it easier than ever to build, iterate, break things, and learn.


## Why AI is harder to teach than data engineering


This is something I’ve been chewing on for months, and Zach said it cleanly. AI is hard to teach because the best practices haven’t been established.


In data engineering, there are decades of patterns. Clearer right and wrong. In AI, the gap betweenwhat actually worksandwhat vendors are selling you is wide, and vendors are very happy to live in it. Be skeptical of anyone who tells you they’ve nailed the right way to prompt, the right way to build agents, the right way to evaluate. We’re all figuring it out in public.


That said, according to Zach, two things hold up:

1. Specify your prompts. Most people type “fix this” and wonder why the model is bad. Give it 10% more context, and you get 80% better output. This is not subtle. Under-specified prompts are the single biggest skill gap he sees.
2. Stop defaulting to Opus or other high-powered models. Using the most expensive model for every one-plus-one task is asking Einstein to do basic arithmetic. The AI will get it right. It will also cost a lot. Match the model to the job. If everyone did this, Zach jokes, Anthropic would lose a billion a year. (Sorry, Anthropic.)


Anyway, this is a very short post because it’s my last day in Stockholm, and I want to go enjoy the beautiful weather in this amazing city.


Have a great weekend,


Joe


---


Here’s this week’s Freestyle Friday podcast. Available on Spotify, Apple, and wherever else you get your podcasts.


Please support the show with a review.It means a lot.


---


# Awesome Upcoming Events


Here are a couple of things I’m up to. Much more to come, so stay tuned.


---


![](https://substackcdn.com/image/fetch/$s_!rYyu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F027b6038-2c0f-4046-ae3f-342f87e99f29_2100x1182.png)


AI CouncilThe technical conference for humans who shipFor 10+ years, AI Council has been gathering the world’s top AI infrastructure minds to share what’s working (and where we’re headed next). You’re invited for 3 days of high-quality discourse with 1,200+ technical experts, including office hours, small groups, and zero marketing keynotes. Speakers include: The co-inventor of ChatGPT, Creator of DuckDB and Codex, Engineers behind ClickHouse, Databricks, Datadog, and LangChain.


Join usMay 12-14inSan Francisco.


→See the full speaker lineup


I’ll be there too, but not speaking. If you want to grab a beer with me and see amazing talks from amazing people, register now.Disclosure: They’re giving me a ticket to attend. AI Council is one of the last indie data/AI events around, and they do great work. I support non-vendor events as much as I can, and so should you.


---


![](https://substackcdn.com/image/fetch/$s_!Jene!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5d6df69-f48c-499c-8332-259705bbccfa_430x90.png)


London! I’ll be at Confluent Current London. See you there!


When: May 19 to 20


Where: Excel London


Register here.


---


# Cool Videos and Reads


Josh Wills has spent 25 years writing data pipelines, with a career spanning Cloudera, as Director of Data Engineering at Slack, on the dbt DuckDB adapter, and now training foundation models at Datology AI. He uses coding agents every day. And he keeps running into the same wall: the agents jump to conclusions, fix the wrong thing, and ship pipelines no one understands.In this conversation, we unpack why AI agents struggle with the messiest, highest-stakes parts of data work, and what it means for the engineers managing them.


---


### Here are some things I read this week that you might enjoy.


The AI Great Leap Forward


What the 1920s Can Teach Us About Surviving the AI Revolution


Crashing Waves vs. Rising Tides: Preliminary Findings on AI Automation from Thousands of Worker Evaluations of Labor Market Tasks


AI Is Forcing CEOs to Make a Stark Choice: Lay Off Workers or Make Them Do More


Mira Murati’s deposition pulled back the curtain on Sam Altman’s ouster | The Verge


Opinion | Speak, Yuppie - The New York Times


How Everest Has Changed Since Into Thin Air


# Find My Other Content Here


📺YouTube- Interviews, tutorials, product reviews, rants, and more.


🎙️Podcasts- Listen on Spotify or wherever you get your podcasts


📝Practical Data Modeling- This is where I’m writing my upcoming book, Mixed Model Arts, mostly in public. Free and paid content.


If you’re interested in sponsoring my newsletter and podcast, H2 2026 is opening up. Please message me for details.


# The Practical Data Community


The Practical Data Community is a place for candid, vendor-free conversations about all things tech, data, and AI. We host regular events such as book clubs, lunch-and-learns, Data Therapy, and more.


🤖Join on Discord


Thanks for reading! Subscribe for free to receive new posts and support my work.
