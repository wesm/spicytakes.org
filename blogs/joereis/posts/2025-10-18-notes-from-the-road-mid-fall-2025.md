---
title: "Notes From The Road, Mid-Fall 2025 Edition"
subtitle: "The Weekend Windup #6 - Cool Reads, Events, and More"
date: 2025-10-18T13:08:11+00:00
url: https://joereis.substack.com/p/notes-from-the-road-mid-fall-2025
slug: notes-from-the-road-mid-fall-2025
word_count: 2162
---


![](https://substackcdn.com/image/fetch/$s_!cj7z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25ee7d25-3d73-45eb-85e9-c39864c5e3b2_2048x1536.jpeg)

*In lovely Montenego, overlooking Tivat and the Gulf of Kotor*


Back home for a bit. I’ve been on the road nonstop since the beginning of September. This schedule will end sometime in early December. And who knows what next year brings. Every time I think I’ll take a break, my schedule fills up. So it goes.


My typical routine is to arrive at a location, meet with local leaders and practitioners, deliver a talk, and then have dinner and drinks with additional leaders and practitioners. I’ll usually visit an organization or two along the way, because I like field trips.


This gives me access to a very unique view of what’s happening in various pockets of the world. What’s become clear over the last two months is that the data industry is facing a dual shock: a massive consolidation of the old guard and a stark reality check for the new.


# Fivetran + dbt


The biggest news, which dropped just this past week, is the all-stock merger of Fivetran and dbt Labs. This is the talk of every dinner and meeting. The new combined entity is valued at a massive scale (approaching $600 million in ARR). It will be led by Fivetran’s George Fraser as CEO, with dbt’s Tristan Handy as President/Co-Founder. This move, combined with Fivetran’s recent acquisitions of Census and Tobiko, signals a massive roll-up of the modern data stack (MDS). Consolidation is here, and the debates over bundling versus unbundling can be put to rest, at least for the MDS 1.0 era.


The implications are enormous, and these are the questions dominating my conversations:

- What happens to dbt Core? The official line is a full-throated commitment to keeping dbt Core open-source under its current license. However, the practitioner community is skeptical. The question I keep hearing is, “For how long?” There’s a strong sentiment that dbt Core was too good and was dbt Labs’ biggest competitor to dbt Cloud. The fear is a slow pivot to an “open-core” model, where the most valuable new features are firewalled for the paid, integrated platform.
- How many employees will be left? While no official layoff numbers have been announced, a consolidation of this size, especially with overlaps in G&A, sales, and marketing, inevitably means “synergies.” This is a major consolidation play, and redundant roles will be the first to go.
- What does this combo look like for customers? The customer reaction is split down the middle. For new or leaner teams, the promise of a “single pane of glass” for ELT (ingestion and transformation) is very appealing. It means less “glue code” and fewer vendors to manage. But for the thousands of practitioners who deliberately built a modular, best-of-breed stack, the fear is palpable: vendor lock-in.


Who do they buy next? This is the new parlor game. The combined Fivetran+dbt entity has gaps in its quest to become an all-in-one platform, competing with Databricks and Snowflake (assuming this is their goal). The consensus is that they must acquire an orchestration platform and a data observability player to own the entire pipeline from source to consumption.


Also, what new players step in to fill the void? And now that the MDS 1.0 era is history, what comes next? This is what I’m most excited about.


# “Everything AI” and The Hype Correction


The second dominant theme is, unsurprisingly, AI. But the conversation has matured significantly from a year ago.


The question “Is AI in a bubble?” has shifted. There are two separate bubbles.

- The Financial Bubble: This one is real and shows signs of stretching thin. Financial leaders from the Bank of England to the IMF havewarnedthat valuations of AI companies are “stretched” and “reminiscent of the dot-com bubble.” Just this month, a Bank of Americasurveyfound a record 54% of global fund managers believe AI stocks are in a bubble. Even OpenAI’s Sam Altmanadmittedback in August that investors are “overexcited.” Who the hell knows, but it seems awfully frothy right now, with the Warren Buffett Fear Indicator at record highs.
- The Utility Bubble: This is where the “hype correction” comes in. The consensus from practitioners is that the 2023-2024 “chat-with-your-data” euphoria has slammed into the hard realities of 2025, where chatting with data is a nice-to-have, but not a necessity.


The data backs this up. A widely cited MITstudyfrom this year found that a staggering 95% of enterprise AI pilots are failing to deliver any measurable ROI. There’s a lot of nuance to this study I’ve written about a few times, so I think this headline is a bit misleading. But no matter, perception is often reality, and people cite this study to justify why AI initiatives are failing in their organizations. This echoes what I’m hearing on the ground. AI is a mixed bag so far, with some companies having spent fortunes on proof-of-concepts that go nowhere. Others are reaping significant benefits from AI.


A few key realities are driving this GenAI divide:

- Fuzzy ROI and “Workslop”. That 95% failure rate is the definition of fuzzy ROI. A recent Harvard Business Reviewstudyeven coined a new term for the output: “workslop.” This is content that “masquerades as good work but lacks the substance,” effectively creating more editing and verification work, not less. We’ve probably all felt the pain of this, where AI will generate content or code, and then we’re spending our time sifting through it for accuracy and substance.
- Staggering & Hidden Costs. The cost isn’t just in the model APIs. A CloudZeroreportnoted that average monthly AI spend is up 36% year-over-year (to over $85,000). Still, companies are struggling with “hidden costs” in cloud expenses, data maintenance, and the complexity of even attributing those costs. AI just adds more complexity to spend, but these hidden fees are the same as ever, which is why success in the cloud is also a mixed bag.
- Security & Compliance Nightmares. Security is a top concern for executives when choosing an AI provider and implementing it. And the regulatory landscape is a minefield. With new, stringent AI laws taking effect in 2025 and 2026 in states such as California, Colorado, and Delaware, legal and compliance teams are concerned about data misuse, algorithmic bias, and the potential legal liability of a “black box” making an incorrect decision. And don’t even get me started on Europe, where the EU AI Act has many organizations petrified to make a move with AI.


# Careers and Making the Transition to AI


Ultimately, some companies are implementing AI with great results, while others cannot get started. Most IT and digital transformation projects fail, no matter how great the technology. In the spectrum of people, process, and technology, it’s always the first two that trump the tech’s adoption. This reality is causing a lot of concern, and no matter where I go, I’m hearing about careers. Blame it on AI, or simple economic uncertainty. There’s a level of fear about the future I haven’t seen, even during the Great Financial Crisis. This flies in the face of “low” unemployment numbers and a record stock market, but the fear is real among juniors and leaders alike.


For juniors, the fundamental question is, “How do I find work?” The market is undeniably tough for new entrants. Companies are reducing the number of entry-level roles, and most job postings now require several years of experience. Companies, especially in the US, are hiring for specific, immediate needs rather than training generalists. If you’re a junior candidate who’s invested in hot AI skills like AI coding, context engineering, and building agents, you’ve got a fighting chance.


For senior practitioners, the focus is “How do I transition to an AI-first world?” For seniors, the path is about adaptation. It’s no longer enough to be a “data plumber” who just knows SQL and Python. The most valuable and in-demand engineers are “versatile professionals” who are bridging the gap. The in-demand skills for late 2025 are all about leveraging AI and one’s deep expertise to move faster.


Leaders face an interesting choice. I’m seeing some leaders embrace AI in every aspect of their work. In myrecent interviewwith Nexla CEO Saket Saraubh, he says he’s using vibe coding tools like Lovable to create prototypes of what he thinks should be in the product. He’ll show this to his product and engineering team and get their feedback. From conversations I’ve had, this is common for tech CEOs, especially in the Bay Area. Other AI-enthusiastic leaders are encouraging their staff to experiment with AI, investing in their team’s upskilling, and are supportive of transitioning to an AI-first company.


Other leaders are reluctant to embrace AI. This is especially prevalent in Europe, where organizations tend to be conservative, highly regulated, and generally several years behind their American counterparts. This is a personal observation and possibly an overgeneralization, but this is what I’ve seen over the years. For the AI-reluctant crowd, I can only say the future is coming fast, and sitting this out is a choice you might soon regret. The people who can transition their careers to become AI-first are in the driver’s seat for shaping the future. Those who wait this out will likely be left very far behind.


Thanks to everyone I’ve met along the way1.


Can’t wait to see everyone else!


For now, have a fun weekend,


Joe


Thanks for reading! Subscribe to receive new content, usually every week.


# Awesome Upcoming Events


![](https://substackcdn.com/image/fetch/$s_!KoJK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F394e1f27-f333-470f-a660-119156959fa2_1588x2245.png)


Welcome to Hel..sinki. I’m back once again, and this is shaping up to be one of the best indie data conferences not just in Europe, but globally.


Helsinki has become an adopted city, so it’s great to be back very soon.


Register here.


---


![](https://substackcdn.com/image/fetch/$s_!z2N2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1c26e8c-702c-4a10-8f14-5c57d485f693_1200x628.png)


Beyond BI…Yes,waybeyond.


The next wave of analytics isn’t just faster dashboards or bolted-on GenAI features. It’s a foundational shift to agentic systems that can think, act, and explain. AI agents don’t stop at visualizing what happened. They reason about why, recommend what’s next, and do it with clarity and traceability.


Join me and a roster of great minds in the field as we discuss what’s beyond BI.


Register here.


---


![](https://substackcdn.com/image/fetch/$s_!LLot!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F131051e6-39e4-407d-916d-05191591187a_3375x4219.png)


San Francisco - I’m back on November 4-5, 2025 for Small Data SF!What’s up with “small data”? Isn’t BIG data always better than small data? This event is awesome because it brings together developers and data practitioners for two days of workshops and talks that challenge the “bigger is always better” mentality in data and AI. Join us to explore the philosophy that’s reshaping how we think about data processing!


Day 1 (November 4):Hands-on workshops where you’ll learn practical techniques for efficient data processing, local-first development, and building AI applications that don’t require a cluster to run.


Day 2 (November 5):A full day of talks from industry leaders who are redefining what’s possible when you optimize for simplicity, speed, and developer experience rather than theoretical scale.


🐥


Register here.


---


### But wait, there’s more!


![a man is standing in front of a shelf full of oxi clean](https://substackcdn.com/image/fetch/$s_!4qey!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d44e0de-1a94-480d-b88d-4830733cd743_404x270.gif)


My other upcoming events are postedhere.


# Cool Reads


Here are some things I read this week that you might enjoy.


A.I. Companion Ads for Friend.com Flood NYC Subway, Fueling Backlash and Vandalism - The New York Times


California becomes first state to regulate AI companion chatbots - TechCrunch


Why AI for good depends on good data - Amazon Science


The Great Software Quality Collapse: How We Normalized Catastrophe - From the Trenches


The era of open data infrastructure - dbt Labs


The AI Bubble Is Far Worse Than We Thought - Will Lockett


Import AI 431: Technological Optimism and Appropriate Fear - Import AI


How much should you spend on AI tools in 2026? - GetDX


The Pragmatic Engineer 2025 Survey: What’s in your tech stack? Part 3 - Pragmatic Engineer


Clouded Judgement 10.17.25 - From Data Quantity to Data Quality - Clouded Judgement


AI Is Juicing the Economy. Is It Making American Workers More Productive? - WSJ


# Find My Other Content Here


📺YouTube- Interviews, tutorials, product reviews, rants, and more.


🎙️Podcasts- Listen on Spotify or wherever you get your podcasts


📝Practical Data Modeling- This is where I’m writing my upcoming book, Mixed Model Arts, mostly in public. Free and paid content.


# The Practical Data Community


The Practical Data Community is place for candid, vendor-free conversations about all things tech, data, and AI. We have regular events such as book clubs, lunch and learns, Data Therapy, and much more.


🤖Join on Discord


# Closing Question


Do you think AI is in a bubble? Drop a note in the comments.


# Want your article or event featured here?


Go an article or upcoming event you want featured here? Please themhere.


Thanks for reading! Subscribe for free to receive new posts and support my work.

[1](https://joereis.substack.com/p/notes-from-the-road-mid-fall-2025#footnote-anchor-1-176483862)

Special shoutout to Nemanja Pavicevic for taking good care of me in Montenegro, and Karl Ivo for being an awesome host in Vienna and Slovakia.
