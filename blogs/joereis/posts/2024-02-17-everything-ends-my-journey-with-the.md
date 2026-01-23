---
title: "Everything Ends - My Journey With the Modern Data Stack"
subtitle: "Joe's Nerdy Rants #32 - Weekend reads and other stuff"
date: 2024-02-17T17:34:10+00:00
url: https://joereis.substack.com/p/everything-ends-my-journey-with-the
slug: everything-ends-my-journey-with-the
word_count: 3513
---


![The Garden of Earthly Delights - Wikipedia](https://substackcdn.com/image/fetch/$s_!VEtW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58fdda79-9645-4cda-a2af-b08ac8b95b1e_1200x683.jpeg)

*Hieronymus Bosch’s The Garden of Earthly Delights describes humanity’s descent from Eden into Hell*


The Modern Data Stack got quite the eulogy this week. Tristan Handy’sarticle, “Is the Modern Data Stack Still a Useful Idea?” prompted much discussion in the data world about the demise of the MDS. And it’s not like just anyone wrote an article on the demise of the MDS. Lord knows people (including me) have said we should move on from the MDS for years. But this is different. Tristan helped launch the MDS movement with dbt, the wildly popular open-source data transformation tool. So when the progenitor of a movement says it’s time to move on, people should pay attention.


Yes, we should move on from the MDS. But, this is a chance to reflect on it, good and bad. The aftermath of the MDS isn’t perfect, and there’s a lot of baggage. But having been in the game for a while, I can assure you the world is in a better place because of the MDS. If you disagree, please travel with me in a time machine to 2011, and let’s negotiate an on-prem data warehouse and ETL tooling contract with a giant tech vendor of that era. Otherwise, read on.


# My Early Days With the MDS


I’ll never forget working my 9-5 at the time, sitting at my desk in 2012, and watching the AWS ReInvent announcements pour in. They announced something calledRedshift. “With a few clicks in the AWS Management Console, you can launch a Redshift cluster, starting with a few hundred gigabytes of data and scaling to a petabyte or more, for under $1,000 per terabyte per year.” Get the hell outta here! Before then, purchasing a data warehouse was highly expensive, friction-heavy, and burdensome. I remember seeing the announcement for Redshift - I think it started at $0.25/hour for a data warehouse on AWS - and thought, “holy crap, that’s amazing.” You could certainly roll your own with the various RDBMSs at the time (that’s honestly still a viable option), but scaling those things was quite painful. For columnar OLAP data warehousing, you needed purpose-built tools. The fact that Redshift was available at the click of a few buttons in the AWS Management Console was very cool. I mark Redshift as the start of the MDS. Back then, it was just a cloud data warehouse. The MDS monicker came along a few years later to describe the cloud-native analytical tooling ecosystem that sprouted alongside Redshift (and later Snowflake and other cloud-native analytical platforms).


I recall the founders of some company called Fivetran cold-emailing me back in 2015 or 2016. They described some crazy idea of moving data from Postgres to Redshift (also built on Postgres) and described something called “ELT.” I sat back in my chair and thought ELT was the dumbest thing I’d heard. Why violate the sacred compact of E-T-L? Later that day, I thought some more and figured ELT had utility in certain use cases. It took advantage of cheap cloud computing and storage, something still new for most people from an ETL mindset. Although I passed on their offer because I already had a solution working fine for my Postgres and Redshift data workflow, the idea of a cloud-based data integration and ELTresonated. Years later, my data engineering consultancy,Ternary Data, became a strong partner with Fivetran.


We went on to partner with many MDS companies. One that stands out is Looker. When I first visited their offices in 2014, I was amazed by LookML. I had a Ruby on Rails and Django developer background. I immediately realized that LookML took the MVC paradigm - ORM and page templating - and created a new way to work with analytical data in a pseudo-object-oriented way. This meant defining a variable or query once and reusing it anywhere. Everything is DRY code, in version control?! I’m old enough to have used Crystal Reports when it was a hot product. And Looker is cloud-native, so I don’t have to install or maintain anything. WTF? Game-changing stuff, indeed. We had a great partnership with Looker for years.


Then, some company called Fishtown Analytics came along with something called “dbt.” To me, it took the great parts of Looker and decoupled them from the visualization layer. Again, game changing. If you’ve ever been on a data team and dealt with M number of SQL files from N number of analysts/data scientists, you know the sheer complexity is an N x M x(WTF) problem. Plus, everyone writes SQL differently. Like Looker, dbt streamlined the work data analysts would need to do by templatizing SQL in Jinja. If you’ve worked in Flask, you’ve dealt with Jinja. And again, templating languages come to the rescue for poor analysts stuck in SQL hell. Write once, and re-use anywhere. Except this time, there’s no BI layer coupled to your code. For ELT, dbt was the “T,” allowing you to transform your data in a platform-agnostic way. This was also game-changing because your model logic would be decoupled from the storage or visualization layers. Fishtown became dbtLabs and started commercializing its offering with numerous non-open-source features. dbtLabs is still doing cool stuff, and we occasionally do a roadshow together.


# The Golden Age of the MDS


Circa mid to late 2010s, my experiences with the early MDS companies were very positive. It felt like these companies genuinely wanted to improve the world of analytics. AWS reigned supreme, GCP Big Query was still very immature (no joins and an odd proprietary dialect), and Snowflake was just coming onto the scene.


On a negative note, coming from a hybrid background of ML and analytics, I felt like the early and mid-2010s were also full of turf wars over data science vs analytics, but that’s a story for another day (it’s a big story, too). There was serious discussion that data analytics and data warehousing would be obsolete due to the rise of ML and data science (sound familiar in 2024 with generative AI?). Would Pandas and Spark take over SQL in 2014? Were data analysts obsolete? Wow, the drama.


The world of data analytics was getting its footing in the new world of the cloud. And I fondly remember these times because the data, which for so long lived in the dark shadows of enterprises, started to become widely popular. For a nerd who was used to being treated like Milton from Office Space, this was my time to shine.


# SO MANY MDS companies!


In the late 2010s, the success of Fivetran, Looker, dbtLabs, and others sparked a ton of new entrants in the MDS ecosystem. This coincided with an era of low-ish interest rates, dating back to the Great Financial Crisis. Getting VC funding wasn’t terribly hard. New MDS companies started, but at a clip natural to the era - not too fast or slow. It was an excellent time to start an MDS company because you could grow your customers and revenue alongside other companies benefiting from low-ish (not yet zero) interest rates.


Then COVID happened. Imagine where you were when COVID shut your world down. That was intense! People were locked down in their homes. Entire industries cratered overnight. A global pandemic of unknown impact was happening as fast as the virus could spread. Would we have a job? Would we all be dead tomorrow? In the US, unemployment reached Great Depression levels in a matter of days. The economy was so bad that oil had anegativeprice. Even toilet paper was out of stock! Who would’ve thunk? The movement of things around the world stopped. Governments worldwide acted fast, knowing any delay would mean a total collapse in the global economic system. Endless cash poured into the economy through various paths in the form of literal cash giveaways and very cheap loans. Interest rates were zero. Free money for everyone!


After things stabilized with COVID, the public and private markets went gangbusters. Crypto and Web3 were the rage. In the data space, tons of MDS companies were sprouting up. In 2020 and 2021, I was inundated with requests to “check out our new MDS product.” I spent countless hours demoing tools from companies, big and tiny, doing data integration, data observability, optimized storage, you name it. Most of these companies attached themselves to data ecosystems like Snowflake and the offerings from the big clouds.


I hate to say it, but most companies and products I demoed were not memorable or special. There was a lot of “MDS-washing,” with every company saying they had the secret sauce to make the MDS work (many of these companies have pivoted to “AI”). On top of that, almost everyone seemed to be a graduate of an impressive incubator or quit their Big Tech job to do a startup, raising boatloads of money from impressive VCs. The MDS landscape was a sea of sameness. I couldn’t believe how many companies got funding to compete in the same verticals. If this many smart people with massive amounts of VC funding were competing in these tiny verticals, how would this work out? Would the total addressable market for data integration products magically expand because there were more seed stage and Series A startups in the mix? Matt Turck’sMAD Data Landscapeimage best captures the MDS zeitgeist. Every niche has dozens of players, all jockeying for market leadership. I joke that his graphic of the data and ML landscape requires the James Webb telescope to see the companies' logos!


As time passed, I saw even MORE startups popping up, increasingly looking like features instead of companies. I remember chatting with my business partner, Matt, about how this made zero sense and wouldn’t end well. There’s no conceivable way this many undifferentiated companies with VC funding all win the race. MDS bloat was everywhere. Also, around 2022, interest rates started to rise. My phone and email were busier than ever as startups scrambled to get market validation and traction in an increasingly brutal market. I stopped taking most calls from new MDS startups because the meetings and demos were all the same, and the founders behaved increasingly desperate and one-sidedly.


Every market has a natural growth rate. Throwing more companies into the mix won’t necessarily grow the market, especially when 1-3 players end up dominating each market category. So, you have incumbents, often the big companies like Tableau or PowerBI, who evolve their offering to the cloud and can offer bundling and favors to their customers that startups simply cannot, and a LONG tail of companies who won’t ever gain substantial market share. Some companies like Snowflake would cross the chasm, sell to mature enterprises and become behemoths in their own right. But there’s an asymptote to selling to enterprises, as they simply don’t need to purchase every tool in the MAD Data Landscape. So, the main principle of the MDS - cloud-native analytics - moved across the chasm to the enterprise. Sadly, most MDS startups won’t make it across the chasm. And since these MDS startups primarily sell to other startups, they will suffer a mass extinction as they fight for market share against the backdrop of a dwindling runway and a very challenging funding environment.


# Best Practices Moved Backwards


During peak MDS, I noticed that best practices in data slipped backward. Through my consultancy, I’d seenmanyhorror shows of data teams doing some wild stuff in the MDS. The MDS made it much easier to work with data, and it also made it much easier to do dumb things more quickly. Lots of new data analysts and analytics engineers got jobs during ZIRP. Sadly, I don’t think they were taught proper data practices, as most of those courses just taught the tactics of data - SQL and Python - without the context in which to use those tactics. So, things like data modeling and architecture best practices took a backseat to quickly delivering “insights” and reports. Data teams engaged in pissing contests of artifact sprawl - “I’ve got 1000+ dbt models for my data team of 2 people” and “I’ve got 1000+ DAGs in my orchestration tool.” becoming the equivalent of how many “lines of code” you could write. In data modeling, one big table data model was common in the MDS because “joins are bad,” never mind that the data model itself was garbage and modern data platforms could handle joins just fine. Ask someone about Kimball data modeling, and you’d be met with blank stares or ridiculed as out of touch.


People fixated on using tools instead of how to operate them or the fundamentals of why you’d use them in the first place. I can’t blame the MDS itself, as it’s just a set of tooling. However, some MDS vendors promoted terrible data practices to a new generation of data practitioners. When I looked at courses and tutorials for popular MDS tools, I couldn’t help but shudder as I saw things like one big table promoted as the standard way to model data. Nevermindthinkingabout your underlying data model and whether it reflects your organization’s business rules, vocabulary, or information workflows. Just cobble the data into a massive table and throw more Snowflake compute at your queries. Set up a ton of other MDS tools and workflows to make yourself feel productive. I feel like the MDS made it easy for the data industry to go backward, allowing data teams to have a ton of convenient tooling while adding questionable value to their organization.


Now that the pendulum is swinging back to fundamentals, the conversation is shifting to how data teams can deliver value to their organization. Data teams are being cut left and right. Expensive MDS tool sprawl is being gutted. If they’re still around, data teams are now learning about proper data modeling and architecture principles. Data is a thinking person’s game. We’re finally returning to the discipline and rigor we had in the good old days when we werethoughtfulabout data instead of just throwing more compute and technology at the problem.


# Everything Ends


If a term is lucky enough to get popular, it gets normalized, and the original term becomes obsolete and less commonly used. Tristan says, “the MDS morphed from a descriptive term into a meme.” It certainly did. Toward the end, it became a joke. I’d personally cringe when I’d hear “Modern Data Stack,” as I’d have PTSD from some of the things I earlier described. Matt Housley and I even called out the demise of the Modern Data Stack in our book a couple years ago, and we often had discussions with industry peers about this. So, the sentiment the MDS wasn’t so “modern” isn’t a new one.


The thing is, the MDS won. It normalized what it’s supposed to do - modular, easy-to-use, cloud-based analytical tooling. Now that the MDS is a footnote in our industry, the term can fade into obscurity to be replaced with a name that describes what it solves for. As Tristan says, analytics.


The graveyard of dead or recycled terms in our field is massive, like “Big Data,” “Data Lake,” “Data Mining,” and so on. The death of terms will keep growing, especially as technology hype cycles grow shorter. You’ll see the same thing with “AI” at some point, as it becomes woven into every part of our lives.


Everything ends. This is a good thing.


Listen to the audio clip above on this topic, which is also my5-Minute Friday on Spotify.


---


# Cool Weekend Reads


Here are some cool things I read this week. Enjoy!


### Tech, AI, Data


Sora (OpenAI)


Type a prompt and get a 1080p video for whatever’s on your mind? This is easily the coolest and most impressive demo I’ve seen in alongtime. If it holds up, the possibilities (good and bad) are crazy to comprehend. Related:Video generation models as world simulators(technical paper that dives deeper into Sora)


Is the "Modern Data Stack" Still a Useful Idea? (Tristan Handy)


Tristan Handy - one of the OG’s of the Modern Data Stack - set off quite the ruckus this week with his thoughts on why we need to move on from the Modern Data Stack. He’s right, we need to move on. It doesn’t feel so…modern…anymore


Also, see my thoughts in this week’s rant in this newsletter.


The day Agile came to town: Remembering Utah's Agile Manifesto, 23 years later (KSL)


Did you know the Agile Manifesto was penned in Salt Lake City, UT at my local ski "hill", Snowbird? Read on for a fascinating look at the manifesto that would change the world.


### Biz, Culture, Other Randomness


Thinning The Herd (Investing 101)


“A lot of companies will find that they have less of a war chest, and more of a leaky cash bucket.If you're a founder, and don't have a handle on exactly where cash is going? That's a problem. If you're on an executive team and you're not having discussions about burn? That's a problem. If you're at a company continuing to hire and spend without any discussion of runway? That's a problem.”


This is a really good analysis of the runway (or lack thereof) for startups as money is harder to come by, and valuations are a fraction of what they were in the ZIRP days.


Boeing is a wake-up call (Insider)


Boeing used to be an engineering-led company that produced great aircraft. Then the suits from GE came in and gutted the place, focusing on “efficiencies” and “shareholder value.” While being efficient and delivering results to shareholders is a great goal, especially in companies where safety is paramount, these shouldn’t be the primary goals. Focusing on the bottom line (and high executive pay, share buybacks) at the expense of safety gives you the Boeing of today, a disaster of a company.


Finance Chiefs Chip Away at Expenses Despite Sunnier Economic Outlook (WSJ)


Seems like 2024 is going to be continuation of the cost-cutting from the last couple of years. Read on for some opinions why.


Anecdotally, I was at a Java meetup last night in SLC (I live an exciting life, I know), and a recruiter told the audience about the job market in Utah. Despite historically having a robust tech sector, Utah’s tech job market has flatlined. Jobs are hard to come by, even for senior+ levels. Hopefully things turn around soon, but who the hell knows.


# New Content, Events, and Upcoming Stuff


## Monday Morning Data Chat


#### Coming up…


Joe & Matt, Jean-Georges Perrin, Ethan Aaron, and more!


#### In case you missed it…


Scott Taylor - Explaining Value to the Business (Spotify,YouTube)


Michel Tricot - AI's Impact on Traditional Data Practices and More! (Spotify,YouTube)


Benn Stancil -2024 Predictions, GenAI and Product Development, etc(Spotify,YouTube)


Dave Langer - Dave Langer - Excel in Python, Data Science Without "Data Scientists"(Spotify,YouTube)


Sol Rashidi - Getting Business Value From Data, the CXO Playbook (Spotify,YouTube). Very popular episode with nearly everyone. - PINNED HERE.


## The Joe Reis Show


#### Coming up…


Wendy Turner Williams, Alex Freberg, Christophe Blefari, and many more!


#### This week…


Steve Hoberman - Data Modeling’s Past, Present, and Future (Spotify)


Randy Bean - Why GenerativeAI is Making Companies More Data-Driven (Spotify)


5 Minute Friday - Everything Ends (Spotify)


#### In case you missed it…


Andrew Meister - Removing Clunk (Spotify)


Roy Hasson - Career Progressions in Data & Tech, Open Table Formats, and more (Spotify)


5 Minute Friday - Data Day Texas, Practical Data Modeling Updates, and More (Spotify)


Ari Kaplan  - Data Intelligence, Evangelism, and More (Spotify)


Bill Inmon - History Lessons of the Data Industry. This is a real treat and a very rare conversation with the godfather himself (Spotify) - PINNED HERE.


## Events


Data Meetup (Paris) - February 27-28, TBA


Skiers in Data (Switzerland), March 1-3 -Register here


Deepfest (Saudi Arabia) - March 4-7, TBA


Onepoint (Paris) - March 21, TBA


Data Universe (NYC) - April 10-12, TBA


J On the Beach (Malaga, Spain) - May 6-10


Gitex (Morocco) - May, TBA


GenAI Conference (London) - May, TBA


DAMA Days (Vancouver, BC) - June, TBA


(Taking the Summer off)


Australia - Fall, TBA


Europe - Fall, TBA


Asia - Fall, TBA


Would you like me to speak at your event?Submit a speaking requesthere.


# Thanks! If you want to help out…


Thanks for supporting my content. If you aren’t a subscriber, please consider subscribing to this Substack.


You can also find me here:


Monday Morning Data Chat (YouTube/Spotifyand wherever you get your podcasts). Matt Housely and I interview the top people in the field. Live and unscripted. Zero shilling tolerated.


The Joe Reis Show (Spotifyand wherever you get your podcasts). My other show. I interview guests, and it’s unscripted with no shilling.


Fundamentals of Data Engineering (Amazon,O’Reilly, and wherever you get your books)


Be sure to leave a lovely review if you like the content.


Thanks! - Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.
