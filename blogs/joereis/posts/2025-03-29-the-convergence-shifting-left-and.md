---
title: "The Convergence - Shifting Left AND Right"
subtitle: "Joe's Nerdy Rants #71 - Weekend reads, podcasts, and other stuff"
date: 2025-03-29T19:48:52+00:00
url: https://joereis.substack.com/p/the-convergence-shifting-left-and
slug: the-convergence-shifting-left-and
word_count: 1763
---


![](https://substackcdn.com/image/fetch/$s_!C7HB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd636b0a3-eaf1-4b01-a981-2eed5e3ef12d_1357x673.png)

*The Data Engineering Lifecycle (Fundamenals of Data Engineering). What happens when data engineers are more invovled with Generation and Serving?*

0:00
-9:52

While speaking on a panel at theShift Left Conferencethe other day (shoutout toGable), I thought that while data engineers are “Shifting Left,” they’re also shifting RIGHT. Before I get into the latter, let me interpret what it means to Shift Left1.


Until recently, lamenting about poor data quality and dismissive interactions with upstream engineering teams were considered normal. In this scenario, data teams maintain certain infrastructure (ETL, data warehouses, BI tools, etc.) to serve dashboards, reports, and data for downstream analysis. These data teams rely upon data from various upstream source systems, such as ERP, CRM, and various transactional databases and APIs. They largely work in isolation from “the business”. In the rare cases where data teams demonstrate “business value,” they’re lauded as heroes, invited to reveal their secrets to eager audiences on podcasts, guest articles, and keynoting data conferences around the globe. “Oh wow, you worked with the business and delivered something of value?! Holy shit! That’s amazing. Tell us more!” I’m not exaggerating, and this should tell you howraresuccess actually is in the data profession under the traditional ways of doing things.


While data teams are still mostly an internal-facing IT cost center (Enterpriseland, as I called it in an article last year), this is changing. Things are shifting left. What does this mean? Like many terms in our field, Shift Left means different things to people. For me, Shifting Left means the producers and consumers are structurally and culturally aligned to create value for end customers (those who keep your firm in business). Structural alignment means there’s technology and systems in place to guarantee the delivery of data, through machinations, to the service of end customers. Cultural alignment means that no matter where in the data lifecycle one works, everyone is working toward the same goal of end-customer satisfaction. This aligns with lean thinking, where every action should intentionally and ultimately serve the end customer. Notice this mindset drastically differs from the cost-center mentality typical in traditional data teams. Gone are the notions of “us vs them.” Shifting Left is about delivering a quality product - using data - to satisfy a customer.


A few things contributed to the Shift Left change in the data industry. DataOps borrowed many ideas from DevOps (which borrowed from Lean) and brought continuous delivery and waste elimination to data practices. Data Mesh revolutionized the thinking of the data industry, taking the philosophy of microservices to data. This woke the data industry from its internal-facing stupor and mainstreamed the idea of data products. Finally, Data Contracts recognized that data teams will always be in reaction mode until we address upstream data quality problems and surprises. I’m sure I’m leaving out some other key events. But it’s the weekend, and I’m writing a rant, not a comprehensive tome. If I leave something out, it’s not on purpose. Feel free to point out my omissions in the comments.


The core framework of the Fundamentals of Data Engineering is the Data Engineering Lifecycle. The tl;dr of the lifecycle is data engineers get data from source systems and make it useful for downstream use cases like analytics, ML/AI, and more. Shifting Left more tightly integrates data engineers with source systems. This is a net positive since software and data engineers work together rather than the traditional way where data engineers work with whatever turds the software engineers happen to throw over the proverbial wall.


Back to Shifting RIGHT. These days, I see data engineers doing more ML/AI work, particularly with AI. Whether it’s creating AI-powered Streamlit apps, data pipelines for unstructured data, AI integrations, agentic workflow, etc, this wasn’t the sort of work data engineers would do in the Serving layer of the data engineering lifecycle. Data engineers are creating these and incorporating the (ideally) high-quality data they’re getting from their left-facing producers. Does this mean that data engineers are moving more toward being ML or AI engineers? I’m unsure yet, as it’s too soon to tell. At the same time, I’m seeing software engineers becoming way more active in ML/AI. This wasn’t happening nearly as much three years ago.


What does this mean? The world is changing rapidly, and data engineers (and others in the data discipline) will need both producer and end-customer-facing roles. This is a big part of why I’m writing Mixed Model Arts, my upcoming book on cross-disciplinary data modeling.  Shift Left AND Shift Right inevitably means the old days of being singly focused will inevitably disappear and the siloes between software, data, and ML/AI blur and eventually merge. I call this The Convergence2. Humans and machines deliver products and actions powered by data and AI.Over the last several years, I’ve written and talked about The Convergence in various forms. I’ll have more about the Convergence, mostly in my upcoming book. If you’re not subscribed toPractical Data Modeling, please check it out. There, I’m writing early draft sections of my book and the occasional data modeling rant, too. The book is planned for publication sometime in late Summer/early Fall 2025.


Please listen to the audio above or on Spotify (or your podcast platform of choice).


Have a wonderful weekend,


Joe


---


# Cool Weekend Reads & Listens


How Software Engineers Actually Use AI | WIRED


Databricks Has a Trick That Lets AI Models Improve Themselves | WIRED


China built hundreds of AI data centers to catch the AI boom. Now many stand unused. | MIT Technology Review


Oracle customers confirm data stolen in alleged cloud breach is valid


AI Agents Are a Moment of Truth for Tech


Is America falling behind in the AI race?


Majority of AI Researchers Say Tech Industry Is Pouring Billions Into a Dead End


Superhyperbola


## Podcast


Freestyle Fridays - Shifting Left AND Right. The Data Engineering Lifecycle in 2025. - (Spotify)


Mark Freeman - Shifting Left in Data, Startup Rocket Ships, and More (Spotify)


Vaibhav Gupta - BAML and AI-First Tools (Spotify)


Freestyle Fridays - Figuring Out Your Next Move (Spotify)


Willis Nana - Navigating Data Engineering Leadership, YouTube, and More (Spotify)


Salma Bakouk - Data Observability, the Balance of Running a Startup, and More(Spotify)


Freestyle Fridays - Public Speaking Tips w/ Jordan Morrow (Spotify)


Simon Späti - The Art of Writing about Data Engineering (Spotify)


Todd Beauchene - The Early Days at Snowflake, Modern Data Platforms, and More (Spotify)


Freestyle Friday -  How I Use AI for Writing (Spotify)


Matthew Kelliher-Gibson - The Data Cynic (Spotify)


Carly Taylor - The True Cost of Replacing Engineers with AI (Spotify)


Freestyle Friday - The Cult of Scrum (Spotify)


John Thompson - The Path to AGI, Writing Books, and More (Spotify,YouTube)


Freestyle Friday - The Great Pacific Garbage Patch of AI Data Slop (Spotify)


Eric Broda - AI Agent Ecoysystems, the Death of Consulting, and More (Spotify,YouTube)


Way more episodes over at the Joe Reis Show, available onSpotify,Apple Podcasts, or wherever you get your podcasts. Also available onYouTube.


# Upcoming Events


Atlanta, HEDW Conference. Data Engineering Workshop - April 6.Register here.


This is a very rare chance to learn about data engineering from me, live and in person.


---


## Are you attending Google Cloud Next?


Curious about how top teams are building AI-ready systems with trusted data?


![](https://substackcdn.com/image/fetch/$s_!9EVQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2467829f-bf6c-4831-8e55-000d55e73cbb_1440x809.png)


Join me for an exclusive evening of networking, drinks, and dinner, insightful discussions atTender Steakhouse at the Luxor on April 9th at 6pm PT. We’ll explore how industry leaders are preparing for AI by focusing on the right people, processes, and technologies—ensuring data trust to unlock value, mitigate risk, and drive success in analytics, data products, and AI initiatives.


Space is limited— secure your spot today!


Register for the Serving Data Event here


After keep the momentum going at Data + AI: The After Party atHazel Kitchen & Cocktails at 9:30pm PT—a night where AI, data, and innovation meet craft cocktails and great company.


![](https://substackcdn.com/image/fetch/$s_!GkxZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d1c6fef-d558-4ea9-bf5e-107545981b16_1280x800.png)


Join fellow cloud pioneers, data wizards, and AI enthusiasts at Hazel Kitchen & Cocktails for an evening of networking, deep tech discussions, and laid-back vibes. Whether you’re raising a glass to your latest deployment or just unwinding after a day of insights, this is your space to connect, sip, and sync.


Register Here for the Next Level After Party


---


## Other Upcoming Events


Webinar w/ Data Galaxy - April TBA


Webinar w/ Monte Carlo - April TBA


Deep Dish Data w/ Matillion - April TBA


London - May TBA


Snowflake and/or Databricks - June TBA


Iceland - Global Data Summit, June 23-24.Register here


Australia (Sydney, Melbourne) - Data Eng Bytes, July 24-30.Register here


UK - Big Data London, September 24-25.Register here


Helsinki Data Week - October TBA


More to be announced soon…


# Thanks! If you want to support this newsletter

- The Data Engineering Professional Certificate is one of the most popular courses on Coursera! Learn practical data engineering with lots of challenging hands-on examples. Shoutout to the fantastic people at Deeplearning.ai and AWS, who helped make this a reality over the last year. Enrollhere.
- Practical Data Modeling. Great discussions about data modeling with data practitioners. This is also where early drafts of my new data modeling book will be published.
- Fundamentals of Data Engineering by Matt Housley and I, available atAmazon,O’Reilly, and wherever you get your books.
- The Data Therapy Session calendar is postedhere. It’s an incredible group where you can share your experiences with data - good and bad - in a judgment-free place with other data professionals. If you’re interested in regularly attending, add it to your calendar.
- My other show is The Joe Reis Show (Spotifyand wherever you get your podcasts). I interview guests on it, and it’s unscripted, always fun, and free of shilling.
- Want me to speak at your event? Pleasesubmit a speaking requestif you want me to speak or give a workshop at your event.
- If you’d like to sponsor my newsletter or podcast, pleasereach out to me.


Be sure to leave a lovely review if you like the content.


Thanks!


Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.

[1](https://joereis.substack.com/p/the-convergence-shifting-left-and#footnote-anchor-1-160128662)

Yes, I’m capitalizing these words on purpose.

[2](https://joereis.substack.com/p/the-convergence-shifting-left-and#footnote-anchor-2-160128662)

One could also call this a divergence since things are moving in opposite directions. This assumes you’re only thinking the current mode of doing things is a linear flow from left to right. But it’s also a convergence of roles into a feedback loop. So, I’ll stick with The Convergence.
