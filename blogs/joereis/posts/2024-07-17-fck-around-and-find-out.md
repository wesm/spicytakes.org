---
title: "F*ck Around and Find Out"
subtitle: "Does your data team really NEED generative AI?"
date: 2024-07-17T18:01:09+00:00
url: https://joereis.substack.com/p/fck-around-and-find-out
slug: fck-around-and-find-out
word_count: 1575
---


![Fuck around and find out — assi cartesiani virali su TikTok | by Marta  Basso | Medium](https://substackcdn.com/image/fetch/$s_!--9l!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf990b8d-c9a9-4c82-93c4-589141016819_1050x1038.png)


By Lindsay Murphy and Joe Reis


You’re undoubtedly bombarded by nonstop pitches, demos, and hype about AI's business-changing (hell, world-changing)potential. But you’re likely wondering what the use cases are and whether any of this AI magic would even work in your current systems and data. You might even feel gaslit for questioningif youneedan LLMin your daily work or in general.


SaaS vendors seem incapable of talking about anything other than GenAI (which now appears to mean all “AI”). Tech founders have latched onto this trend, and “modern data stack” SaaS vendors are no exception. This rapid move of so many to “build AI into the product” (i.e., slap on a ChatGPT plugin) feels likerecord-breakingshiny object syndrome–distracting us from the few good things the data industry was finally gaining traction (governance, software engineering best practices, and good old fashion data modeling). The noise about AI in the data space is deafening at best. At worst, it feels like a money grab by SaaS founders.


Those of us who’ve been around for a bit will recall the not-so-distant past when we’ve been down this road–thebig data hype cycleof the early 2010s and the data science bubble in the mid to late 2010s. Although that cycle eventually diedin a blaze–the current AI hype cycle remainsimmune to logical skepticism. That’s not to say the authors aren’t optimistic of the long term potential of AI. We are. But this short term hype cycle? We are feeling prettyoverit.


2023 was about imagining use cases for GenAI. 2024 is about testing things out in production and figuring out use cases. 2024 is the year of f*cking around and finding out how well GenAI works in production.


# F*cking Around and Finding Out


What the hell happened? Let’s look at this from the supply and demand of “AI.”


On the supply side, every tech, data, and “AI” vendor (often repackaged Modern Data Stack vendors) appears to be throwing AI into their product. At tech and data conferences worldwide, it’s all about AI. Seemingly, every vendor has an AI chatbot or copilot. For instance, a common trope in the data vendor space is LLM’s will allow businesses to “chat with their data.” Our big questions are:who’s asking for this, and how well do these products work in the real world?


The minimum viable product (MVP) mindset is pushed very hard in the SaaS industry–take your product to market, test it out, and improve it based on feedback. In most situations, this approach works to drive forward rapid product innovation. But is it feasible to apply this philosophy to “bolt-on” AI/ChatGPT plugins in B2B SaaS products? In the data industry especially, where accuracy and reliability shouldalwaysbe a top priority, this “MVP” approach is more of a “f*ck around and find out” strategy–introducing significant risks with little regard for the extraneous consequences.


On the demand side, it seems like every company is scrambling to have an “AI story” they can tell their investors, board of directors, and customers who care. We’re curious to see how many companies find a use for integrating generative AI into their businesses. Generative AI is great at…generating things. So, some obvious use cases include programming, customer service, copywriting, generating images (and soon video), audio creation, and anything else where you need to create something new or summarize content.


Here’s the crux. From what we can tell, most companies are still barely getting BI right. Reports don’t match, numbers don’t make sense, and the data teams still spend much time cobbling together data. Remember, these are the same problems BI has faced for several decades. Even though the underlying datasets haven’t changed, companies want to throw an LLM on top of this? What different results do they expect to see? And what about the unused dashboards and reports pervading most companies? But we’re going to suddenly ask more questions from our data. But that won’t stop the rush to bolt AI into every SaaS product.


In the real world, most companies deal with incredible nuance in their data, ever-changing business domain knowledge, data tech debt, unpredictable data quality issues, and general infrastructure “cruft”–all held together by overworked, undervalued data teams. Most forms of data documentation become stale before rolling out to business users. Even data teams who invest significant time and effort in tools like data catalogs still struggle with these issues. Regardless of all these facts, we still see SaaS marketing teams selling AI features with claims like “Now anyone can be a data analyst.” May as well hand a loaded gun to business stakeholders by passing “human in the loop” responsibility over to people who are woefully unprepared to suss out when something is blatantly wrong.


This trend also perpetuates an AI “race to the bottom” across industries. It’s a wave of “innovation” that isn’t genuinely innovative but leads us down a path of SaaSenshittification. Many have stopped focusing on more valuable necessary product use cases and actual problems. It’s a classic case ofMaslow’s Hammer–everything looks like a nail when all you can focus on is your shiny new AI hammer. Many of the problems data teams have aren’t sufficiently solved by the AI capabilities we have at our disposal today.


Maybe you’re thinking, “But wait, these tools help boost the productivity of data teams by writing code for them.” Humans are lazy. People will look for ways to cut corners. Yes, in theory, AI should help drive some productivity gains. Still, the overuse of these AI capabilities exacerbates the skills gap in the data industry. The explosion of “modern data stack” tooling offers higher and higher levels of abstraction to buy things you don’t know how to build, meaning we end up with much fewer technical folks participating in data engineering (orpretendgineering). Pair the existing skills gap with overusing AI, and it becomes another crutch to avoid learning deeper technical skills–this is a recipe for getting collectivelydumberand lazier as an industry (we already have some stellar examples of this fromother industries).


Ask yourself how useful Generative AI has been to your data team’s workflows. “AI helps us add all that missing documentation we never got around to writing.” or “AI helps us find the data and information we need.”–perfect, so we will use the AI written documentation to answer questions about the data–indeed, that circular logic won't end badly. “But AI can write SQL queries for business users, so my data team doesn’t have to.” Do business people want help writing code? Having SQL queries dropped at their feet? No, they want accurate, distilled insights and recommendations that help them improve business performance. Yes, Gen AI can mimic some of these skills and trick uneducated business leaders into thinking these outputs are doing the same thing–but “f*ck around and find out”–time will confirm that these capabilities are not a substitute for your data team.


Pay close attention to these “anyone can talk to their data now” AIdemos, and you can easily spot some flaws in the testing. The questions being fed are always far simpler than “real-life” business questions ever are, and the “anyone can do data stuff now” messaging vastly oversells the capabilities as some kind of “magic data bullet” that they simply just aren’t. Anyone familiar with working with real-world data can pick up that these types of examples are elementary, built using clean demo datasets, and not representative of any useful, real-world insight generation or analysis that a business needs. It’s also still really unclear who the tool was built for–again, the user story for most of these features was probably “As a SaaS vendor, I want to add AI to my product.”


# Decide For Yourself, How Much Do You Want To F*ck Around?


Despite the massive pressure from SaaS vendors telling you that youneedAI features or you’re falling behind the curve, try to resist the FOMO bait and think for yourself. How much risk are you willing to fuck around with to find out the potential value? SaaS vendors are treating AI like a shiny new hammer for every nail. Make sure you think critically about what you’re being sold before assuming they have your best interests in mind regarding AI (this includes the security and privacy of your data). Companies are investing into “AI”, often withlittle to show for it. Don’t be one of those companies. And if that’s not enough,major investorsare alreadycalling bullshiton the AI hype and bubble, so consider where you’d want to be investment-wise in a world where the bubble has burst.


Next time you get a marketing or sales push for new AI features in data tools, ask yourself (or hey, ask the vendor trying to sell it to you!): What measurable value will this drive for my company? Who is the intended user of these features? What workflows and use cases are people using this for? Can I accept low accuracy and reliability for my use cases while still getting value? Does this save resources and time, or is it a technical skill crutch that could lead my team to introduce more errors and mistakes in our work? Is this just the latest money-grab attempt by SaaS founders to remain relevant amongst anungodly number of competitors?


---


Listen to our podcast on this topic here:


Thanks for reading Joe Reis! Subscribe for free to receive new posts and support my work.
