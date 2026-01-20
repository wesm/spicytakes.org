---
title: "The potential gap"
subtitle: "There's a difference between what tools can do and what tools do do."
date: 2023-09-29T16:22:38+00:00
url: https://benn.substack.com/p/the-potential-gap
slug: the-potential-gap
word_count: 1875
---


![Limitless - Plugged In](https://substackcdn.com/image/fetch/$s_!MvdN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0088105a-66f4-4569-8fd4-abbd00ce4f65_1912x810.png)

*Bradley Cooper, using 100 percent of Azure Data Factory.*


When I worked at Microsoft, the Office team periodically put out internal “vision” videos that showed how customers could use the suite of products that we were building. They weren’t raw demos, but glossy feature-length commercials that were stylistically similar to everyoverfundedtechcompany’slaunchvideo: Full of sappy narratives, conspicuous diversity, and a small business selling a safely inoffensive product—quirky socks, dog toys, colorful bicycles, environmentally-responsible bags—to customers who want to express themselves in safely inoffensive ways.1A busy architect needed to make it to his daughter’s soccer practice; with SharePoint and Publisher, he could review blueprints on the go. A doctor didn’t want to miss her mother’s birthday; with Outlook andLync, she could still care for her patients from Mexico City. A sixth grader had to write a report on butterflies; with PowerPoint and Internet Explorer, she could make it beautiful. And in aClinkle-worthy twist, the architect is married to the doctor, the sixth grader is their daughter, and they have anOffice Family planthat keeps their crazy, modern lives connected. They were stories about love, humanity, always being home for dinner, and OneDrive from Microsoft 365.


Of course, nobody is like this; it would be insane to be like this. No family has ever perfectly organized everything they do in Office. Our digital lives aren’t beautifully choreographed dances through shared calendars, family Teams chats, collaborative OneNote grocery lists, and loving and supportive comments left in homework assignments. Our digital lives are chaos. The mother keeps her notes on her iPhone, and prefers using the desktop version of Excel. The daughter is copying her report from ChatGPT; she ismaking the periods a bigger font. The father is still trying to figure out how to log in to SharePoint. The dance isn’t a ballet; it’s a mosh pit.


But the fairy tale that Microsoft showed us waspossible. It wasn't built around vaporware—every feature that the family used was generally available; everything that they did with it was well within the bounds of reasonable use. Any family with a license to the Office suite and aproficiency in Microsoft Wordcouldlive the life we saw, if they were sufficiently invested in using Microsoft products, and in learning their way around the features in those products.


Put differently, in some rough sense, all of us are choosing the lives we have over those we saw in the commercials. Office has all the productivity features and collaborative capabilities we could ever need; in them, Microsoft is offering us water that could, I’m certain, make our lives more orderly and organized. But it’s us who are choosing not to drink it.


# A new buffet


A couple weeks ago, I got a demo ofY42. In their words, it’s “the complete analytics engineering platform” that can “build, orchestrate and govern data pipelines end-to-end.” In my words, it’s squarely inthe fourth, “other” category of data tooling: Not a warehouse for storing data; not an import or export pipeline for moving data; not a BI tool for analyzing and sharing data; but a catch-all data management tool that’s meant to ensure that teams can reliably turn the messy data they collect into the clean, organized, and regularly refreshed data that they need.


I had two reactions to the demo. The first was that Y42 is an impressively capable product. You can develop and test dbt models in a rich IDE; you can work across different environments and branches, and quickly deploy and roll back changes; you can create DAGs of data dependencies, from sources like Fivetran to BI tools and operations applications; you can manage and orchestrate the entire operation in a single interface, and manage it all in code. Hundreds of data teams struggle withvarious versions of these problems; though Y42 isn’t perfect, I suspect that a team with a well-managed, well-integrated, and well-maintained Y42 instance at its center can probably do its job more reliably than one without it.


My second reaction was that none of that will matter. Though teamscouldsolve lots of their problems with Y42, very few will. Most teams will never use it; those who do will probably only use a fraction of its features. It’ll be a dbt IDE, or an orchestration tool, or a place for tracking the lineage of data pipelines, but not “the complete analytics engineering platform” that it could be, like it was in the demo, or as it is inside of Y42 itself.


This isn’t a statement about Y42; it’s a statement about us. The market has given us products like Y42 before—not of its exact combination of features, but of some mix of orchestration management, governance configuration, lineage tracking, data development, observability, cataloging, and discovery. Even in the most successful cases, most customers use these tools in relatively basic ways. Alation, Alteryx, Astronomer, Atlan, AWS Glue, and Azure Data Factory—roughly 1/26th of the tools in the “other” category—could all probably make similar claims about being underused relative to their potential. Y42, if I had to bet, is bound for the same fate.


Which is kinda weird! If we pushed these tools to their limits, they could probably solve a lot of stubbornly persistent problems.2Instead, it’s as though we’re hungry, go into a buffet, and never bother to walk past the appetizer station. We keep complaining about how we haven’t had enough to eat; new entrepreneurs keep creating new buffets that reconfigure the stations; we keep only eating what’s by the door, and declaring the restaurant insufficient.


We should probably figure out what that’s about? We invest billions in building new restaurants; we spend billions trying them out; we waste billions by being hungry all the time. Why? Why, just as we all choose to live our chaotic lives instead of the organized one that Office theoretically makes possible, do we continue to grind through problems that tools like Y42 can probably solve? Why do we only usetwenty percentof our (data tooling’s) brain?


# ‘Cause let’s be honest, we kinda do sound the same


One answer is that our products have the features, but they’re poorly built. They’re too convoluted to understand, and too clunky to use. Sure, platforms likeOracleandMicrosoft Fabriccan do everything, but they’re hard to buy, set up, and maintain. The features don’t matter as much as the experience of using them. If ChatGPT was only available on IE7, or if you had to be anindustry-leading distinguished engineerto post a video on TikTok, they’d both be woefully underused too.


So we—i.e., people who talk about this stuff on Substack—segment the market into the startup cinematic universe, where the products are delightful but incomplete, and the Microsoft cinematic universe (or Oracle, or whatever), where the products are cumbersome but comprehensive. We aren’t so much choosing the chaotic life over the organized one; we’re choosing the cloud over big box software; modern over legacy; affordable over expensive; usage-based, month-to-month subscriptions over perpetual licenses; buying on vibes over buying on RFPs.


But that doesn’t feel complete. It doesn’t explain why we use so little of the modern data products that we buy.3Nor does it explain why, when I mentioned Y42, most people's reaction was probably not to think, "oh wow, at last, something that solves this long-standing and painful problem!," but to roll their eyes, wonder if I was an investor shilling for my portfolio (I’m not), and think, “a different tool now, but there’s nothing new.”


That response—myresponse, of skepticism anddéjà vu all over again—suggests to me that we’re collectively held back by self-reinforcing pessimism. Our problems have been around a long time; we’ve been promised solutions for years; we no longer believe those pitches. Unless a new product hits us square in the face with an idea that’s dead simple to test or obviously revolutionary, we won’t believe its potential.4But when that potential requires some investment to realize—when we have to neatly organize everything in Office, or learn all of Y42’s features—we need that initial faith. Without it, we briefly kick the tires, assume we’ll be disappointed again, and move on. And our problems becomeLindy: They persist because they have been persistent.


# I believe that we will make commercials


I'm not sure any of this is right, and I'm even less sure of what to do about it if it is.5It would be a tough trap for the industry, though, because what can startups like Y42 do to change my reaction to their demos? They can't force their customers to invest in making the most of their products. If anything, buyers are demanding the opposite—we wantlow-commitment contracts, to be safe from technical lock-in, and open platforms that are easy to upgrade to the next new thing. But all of these things are anathema to the investments that most data products need from their buyers to be successful.6


For individual vendors and for the market as a whole, it seems as though we’re reaching a point where solving that riddle—which is marketing and storytelling, basically—is becoming more important than cranking out new features. That’s not because the products are done, but because there’s no sense in building more product that won’t get used. And people won’t use products unless theybelieve in them.


Time to make some commercials aboutchairs, I guess.

[1](https://benn.substack.com/p/the-potential-gap#footnote-anchor-1-137508126)

I want more startups to make videos of their products being used by, like, hedge funds and hardened executives at chemical manufacturing conglomerates. Because be honest, you don’t want to sell your newCPQto a design studio in Oakland with eight employees and three office dogs; you want to sell it to the SVP of Corporate Sales Strategy at DuPont. Where’s the product video where the main character isn’t a loving mother who left her job at a law firm to start a ceramics studio, but isJim Young from J.T. Marlin?

[2](https://benn.substack.com/p/the-potential-gap#footnote-anchor-2-137508126)

Case in point: Vendors using their own tool. When Acme Data, Inc. uses the Acme Data Platform inside of Acme Data, Inc., they can usually get a lot more out of it than their customers. I’d argue that most of that comes from a commitment to use the tool, and a willingness to push how far it can go. In other words, internal deployments of tools are decent measures of tools’ limits, and those limits are often pretty far beyond where most customers go.

[3](https://benn.substack.com/p/the-potential-gap#footnote-anchor-3-137508126)

I mean, citation needed, but itfeelsright? (And it’s apotentialgap, in every sense of the word.) It’s certainly possible, however, that the entire premise here is wrong, that we actually redline most of our products, and they’re still insufficient. We’re pushing the limits of our data orchestrators, but we strugglebecause they aren’t declarative. We’re hacking together development workflows on top ofdbt environmentsandzero copy clones, and Y42’svirtual data buildsare the solution we’ve long needed. I doubt that’s the whole story, but what do I know?

[4](https://benn.substack.com/p/the-potential-gap#footnote-anchor-4-137508126)

This seems like why AI-based features are an exception to this. They are often pretty easy to try out, and they appeared, before AI became a ubiquitous buzzword in everything, so otherworldly that they broke through our cynicism.

[5](https://benn.substack.com/p/the-potential-gap#footnote-anchor-5-137508126)

This is a fun four-word sequence.

[6](https://benn.substack.com/p/the-potential-gap#footnote-anchor-6-137508126)

As I’ve said before, I think having one foot out of your current technology stack is far more harmful than having two feet in an inferior one.
