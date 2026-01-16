---
title: "The future of operational analytics"
subtitle: "A better way to make daily decisions is already here—just not at work."
date: 2021-10-22T17:13:04+00:00
url: https://benn.substack.com/p/the-future-of-operational-analytics
slug: the-future-of-operational-analytics
word_count: 2460
---


![](https://substackcdn.com/image/fetch/$s_!hgkE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3f769df-7b40-46d2-96df-3944dba5ec12_1200x509.jpeg)

*Choose your fighter.*


For those of us on the far side of thirty, planning a night out used to be a very different experience.1If you wanted to get dinner with your friends, you’d gather people’s opinions and whatever rumors they’d recently heard about new restaurants. You’d then guess how crowded each place might be, and estimate how long a group of your size would have to wait for a table. If it was a particularly important dinner, you’d call a few places, one at a time, to see if they had open reservations. And finally, after making a choice, you’d estimate how long it’d take to get there, adding a buffer for potential traffic or a delayed train, and hope everyone arrived on time.


Dining by intuition and anecdote usually worked, but it wasn’t without its misses. Sometimes, traffic was worse than anticipated and you'd miss your reservation. Sometimes, therestaurant was full, and you had to improvise. And sometimes, the recommendation was bad and you'd end up eating at a place whose signature ingredient wasFlorida.


Today, we do it very differently: We choose where to eat based on data. In fact, data-driven dining has become so natural, we barely even notice we’re doing it.


We start by looking up reviews on Yelp and Google. We don’t just mechanically favor the restaurants with the highest ratings, but assess the data analytically. Restaurants with fewer stars but more reviews might be better than those with just a handful of reviews; we check the recent reviews to make sure places are still good; we adjust star ratings by price. Once we find places we like, we useGoogle’s crowd estimatesto see if we’ll be able to get a table. We flip through Resy to find reservations, which provides another analytical signal: We’re suspicious of a restaurant with too many openings. And finally, to make sure our chosen restaurant fits into the rest of our evening’s plans, we rely on Google Maps to tell us how we should get there and how long it’ll take.


Granted, it’s not always the fastest way to make a decision. But we almost certainly makebetterdecisions. Case in point: If you had to plan animportant dinner, would you rather rely on the gossip networks of yesteryear, or data-driven research from Yelp and Google? Overwhelmingly, it seems, we choose the latter.


For those of us who work in data, particularly those of us who toil away trying to make our organizations and their operations more “data-driven,” this should be breathtaking.


Yelp, Google, and other services like them have converted an intuition-driven process into one in which we consult some form of data before making almost any decision. Even when deciding what to order from apps like Doordash and Caviar, we sometimes lean on the “popular items” section—the data—to help us choose.


Moreover, we don’t just rely on Yelp when we’re dropped into an unfamiliar city; we even use it in our hometowns, in neighborhoods that we know. Data isn’t filling the gaps in our intuition; it’sreplacingit.


Perhaps most remarkably, this experience is universal. People weren’t trained to think this way; nobody was onboarded to Yelp’s schemas; no data team carefully maintained a data dictionary to explain how to interpret Google’s reviews; no data scientist pressured us to be more analytical diners. We just did it, all of us, on our own.


Contrast this with the role data plays within organizations. There’sanentirecottageindustryof “thought leaders” (clowns,allofthem) built around helping organizations better use data. As analysts, we fret about people not using the tools we provide them. If they do, we fret about the analytical crimes they’ll commit on top of them. And we, and theexactsamecottageindustry, fret about how to make people more data literate.


There is no such coordination around Yelp and Google. There is no institutional push for data adoption, no Substacks full of tips and best practices. And yet, we all use Yelp’s and Google’s data, and we all survive.2So what did they figure out that we haven’t? How do we make data fit as naturally into the decisions we make in businesses as it does when we make decisions about what to eat?


# Yelp for the enterprise


The secret, I believe, is in the subtlety. We don’t immediately notice how much we use data in products like Yelp, Google, and Resy because data isn’t detached from the rest of the experience. These services don’t attempt to make you “data-driven.” Instead, they focus on a bigger problem—choosing a restaurant, a means of transit, and a reservation booking—and integrate data alongside other features, like phone numbers, pictures of food, and links to menu, that help you address it. It’s all a single experience, with no clear line where the product ends and the data begins.


Consider what Yelp would look like if it took the same approach that we do inside of our companies. Rather than its current interface, Yelp would be a dashboard, full of options and toggles. To find a place to eat, you’d choose a cuisine from a dropdown; pivot the results by price; filter to a few neighborhoods; average the reviews for the last 90 days; no, compute the percent of reviews over the last year that are at least four stars; find places that have improved the most; write a custom formula to adjust by the number of reviews; make several charts; delete the charts; make a few more—and eventually, decide that finding the best restaurant “depends on what you mean by the best,” that every decision is just a tradeoff anyway, and end up going to your usual late-night Thai place because it’s the only thing still open.


Though this dashboard may be more powerful than the current version of Yelp (and, admittedly, be fun to play with), it’d clearly be worse at solving the problem it’s meant to be solving. In the narrow context of deciding where to eat, dashboards like this would merely create an illusion of quantitative rigor. In practice, it’d make data hard to find, easy to misinterpret, and intimidating to use.


This, however, is the model we follow for corporate decision-making. Most data is accessed through dashboards and BI tools, which are dedicated sites for exploring data that are divorced from decisions themselves. We “do our jobs”—sending emails, writing ad copy, designing products, creating decks—in one place, and use data in another.  It is, in short, a decidedly less seamless3experience.


What would be a better version? The easy answer is to embed charts and tables in our workflows, like a dashboard stuck in Salesforce. Though better than nothing, this is a pretty unimaginative future. To think of how much further we could go, consider a less traditional example: Figma, a design tool.


Many product designers live in Figma, and when they do, they make dozens of small decisions about their work, which are often based on their intuition. When redesigning a user interface, they may make assumptions about how it’s currently used, or about the types of people that use it. When they want to check these assumptions, they turn to a data team or sets of dashboard, a process that is is often expensive and exhausting. As a result, it only happens on occasion, for the most important questions.


What if, instead, we embedded answers to their questions directly in Figma? Can we expose numbers—say, the number of times a button was clicked, or the percent of paying customers who use a feature—on mocks themselves? Could designers look at the current product and see an overlay of simple interaction metrics about its elements? Beyond just helping with decisions they know they have to make, this could also help uncover user behaviors that designers had never considered. The paths people take are not alwaysvisibly worn.


On Yelp, we don’t just look up restaurants we know; we also find new places we’d never heard of.Thisshould be the ambition of operational analytics: to inform decision making so thoroughly that we use it even when we didn’t ask for it.


# The future is an experience


Martin Casado shared asimilar visionin a recent conversation with Sisu’s Peter Bailis. His hope—and his ask as a VC looking to make some investments—is for companies to rebuild the SaaS ecosystem as data apps. In Casado’s view, operational tools should be indistinguishable from data tools.


I’m less certain that the best way forward is to recreate tools like Figma rather than integrate with them. (I think there are a lot of interesting questions about the economics of this, which I’ll save for another day.) But I agree with direction of Casado’s ambition: Data should be as ubiquitous in companies as it is in dining. And for operational analytics experiences to get there, the industry needs to make a few changes.


First, operational data tools need to be focused on solving specific problems. Yelp and Google work because they know exactly what they’re there to do. Yelp’s homepage, for instance, makes it very clear what it's for: Find things near you. There’s no “exploring data” or “discovering insights” on restaurants. Instead, Yelp presents a problem that needs data to be solved.


![](https://substackcdn.com/image/fetch/$s_!k1P9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7cf4220-8530-470f-8318-1629fa5bf6ea_1600x936.jpeg)

*Ok, but state? Who’s searching for “Tacos near Texas?"*


Dashboards are the opposite. They’re often data, looking for a problem. In that light, it’s no wonder that people don’t use them—it’s often not clear what they’re supposed to use them for.


Second, we need to be ruthlessly disciplined. Yelp only exposes two data points: The number of reviews, and a crude star rating, rounded—through some means of aggregation that they don’t tell us—to the nearest half star. There are no options for filtering out old reviews, or for only considering those from a certain demographic; we can’t examine other metrics, like median ratings or average ambiance scores. While we might want these things, their absence clearlydoesn’t stop us from wanting to use Yelp, and Yelp isn’t afraid to tell us we can’t have them.


As corporate analysts, we rarely follow this principle. Taylor Brownlowput this well: “After a dashboard had gone live, we were immediately flooded with requests for new views, filters, fields, pages, everything.” When we acquiesce to these requests, dashboards get cluttered with chart after chart, cohort after cohort, filter after filter. This isn’t serving our customers; it’s serving ourselves, punting the tough decisions about what’s important off to them.4


Third, our ambition shouldn’t be to make decisions automatically. At first glance, a product that tells us where to eat seems like an obvious hit. It’d be relatively straightforward to build, and wereallydon’t like picking restaurants. Yet, the only real attempts to do thisare jokes.


There’s no demand for this, I think, because people are reluctant to cut themselves out of decisions. We want to be guided—we want our options narrowed and ranked—but not fully replaced. If this applies to a decision as inconsequential as where we’ll eat on a Wednesday night in September, it almost surely applies to the expensive decisions we have to make about our companies and careers.


Finally, to make all this possible, I believe we needan “operating system” for the data stack. This layer would provide a single platform to build richer apps in operational tools by providing consistent APIs for interacting with data, by centralizing model and metric governance, and by coordinating changes between those apps.


As an industry, we’re drifting in this direction, but aren’t quite there. As useful as they are (and I’m a big fan), products like Census and Hightouch, which write data into operational sources like Salesforce and Zendesk, are currently pipelines that string data between databases and SaaS apps.5They aren’t yet platforms for building experiences. Moreover, whilemetrics layers, anopen LookML,dbt,lakehouses, and thedata meshall have whiffs of an operating system, they’re still primarily read-only layers that provide, in effect, a governed way to write queries.


But all of these products are starting to scratch at the right idea: Thefuture is an experience, with data integrated into and inseparable from how we do our jobs. The technology underneath those experiences are merely a means to an end, no different than the wiring underneath Yelp’s review infrastructure.


---


# The limits of analogies


As an extended footnote, I recognize that the analogy with Yelp isn’t perfect. Deciding where you take your out-of-town friends for dinner isn’t as consequential or complex as allocating a $10 million advertising budget. While Yelp might be useful for a routine night out, it’s not much good for planning a wedding for a hundred people. For these sorts of events, we need more powerful tools.


The same is true in data. In these cases, narrow, operational tools aren’t sufficient. Important, strategic questions or cross-functional problems need open-ended tools. The future of these tools, however, is the same as the future of the entire stack: They too should be an integrated experience. Rather than fragmenting how we explore dataalong technical boundaries—a dashboard for execs, a BI tool for operations, an advanced analytics tool for data scientists—we should integrate these functions into a single cohesive experience. People should be able to move between different modes of exploration, promoting a Python analysis to a dashboard or unfurling a visual analytics tool into a technical IDE. In addition to making data consumption easier, thiscreates a shared workspacefor analysts and non-analysts alike.

[1](https://benn.substack.com/p/the-future-of-operational-analytics#footnote-anchor-1-42966133)

Consider this post a petition to replace all of ourwater-based termswithfood-basedanalogies. Databases? Cupboards. Self-serve? Buffets. Business people? Diners. Dashboards? Plates. We took all the food out of the cupboard and put it on the buffet, but some of the diners overloaded their plates and accidentally mixed their peas with their chocolate pudding.

[2](https://benn.substack.com/p/the-future-of-operational-analytics#footnote-anchor-2-42966133)

Usually.

[3](https://benn.substack.com/p/the-future-of-operational-analytics#footnote-anchor-3-42966133)

Get it??

[4](https://benn.substack.com/p/the-future-of-operational-analytics#footnote-anchor-4-42966133)

We should be honest with ourselves that this is often what we want data for anyway. Making a decision is hard; it often takes courage to make one. Data gives us an out. If the decision goes well, we can praise ourselves for our smart analysis and clear thinking; if it goes poorly, we can say we were just listening to the data.


Consider this thought experiment. Suppose you’ve got to make a big decision for your team, and you’re considering two options. Someone did a great bit of analysis that convinced your team that option 1 is clearly the best choice. However, you know, definitively, that option 1 has a 40% chance of success, and option 2 has a 60% chance of success. If nobody other than you ever knows those odds, which option do you choose?

[5](https://benn.substack.com/p/the-future-of-operational-analytics#footnote-anchor-5-42966133)

To be fair to these products, their initial focus makes sense; it’s a smarter way to build a business. My point is that the “operational analytics” space will need to expand. Census and Hightouch may well already have plans to do exactly that—I have no idea.
