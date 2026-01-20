---
title: "Data is for dashboards"
subtitle: "Animating an abstract world is hard, valuable, and worthy of celebration."
date: 2021-12-03T17:13:32+00:00
url: https://benn.substack.com/p/data-is-for-dashboards
slug: data-is-for-dashboards
word_count: 2029
---


![](https://substackcdn.com/image/fetch/$s_!y-5c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe20652d4-17a3-4952-977a-c608c1517398_900x704.jpeg)

*The perfect crime.*


Thecounty I grew up inis known for three things:Fred Durst, serving as the inspiration forTalladega Nights: The Ballad of Ricky Bobby,1and being the home of several people whostole $17 millionfrom Loomis Fargo in 1997.


The Loomis Fargo heist—which Hollywood also turned into anunflattering portraitof Gaston County2—was one of the largest and most absurd bank robberies in American history. One of the suspects, David Ghantt, was identified nearly immediately: He worked for Loomis Fargo, disappeared right after the money was stolen, and was caught on video loading "cubes of cash" into a van for over an hour.3Needless to say, he got caught.


The other perpetrators would’ve been harder to find, but within three weeks of the robbery, they moved from a mobile home into a $600,000 house in a gated communitytwenty minutes from the scene of the crime. They also made a number of large purchases, in cash, of, among other things, a BMW Z3, a velvet Elvis painting, and a statue of a dog dressed like General Patton. One of the final straws came from a tip from a bank tellerwho alerted the FBIthat a woman showed up with a suitcase full of $200,000 bundled in Loomis Fargo wrappers, and asked, "How much can I deposit without the bank reporting the transaction?"


As ridiculous as the story is, its outline is similar to numerous other cases of fraud: People try to present one story, and small inconsistencies (or half-million dollar homes) put cracks in that reality. Elizabeth Holmes was a wildly successful and transformative CEO—untilJohn Carryrou became suspiciousof her “comically vague” description of Theranos’ technology in aNew Yorkerprofile. A few years laters, Theranos collapsed in scandal. Robert Hanssen was a senior FBI agent—until acounterintelligence officer read a transcriptof a conversation between an American mole and a KGB agent, and realized that the mole used the same General Patton quotes that Hanssen did.4A few years later, Hanssen was convicted of being a Russian spy.


When we want to make people believe that something is real, details matter. Inconsistencies in those details, from offhand remarks halfway through a six-thousand word profile in theNew Yorkerto alimo ride to a Western Steer buffet, do more than just raise questions about what seems out of place. They raise questions about everything.


# "Data is for decisions"


Ask ten analysts a question, and you’ll get eleven opinions—unless your question is about dashboards. On dashboards, the consensus is universal: They’re bad. Dashboards areoutdated,brittle,poorly built, andrarely used. Even our defenses of dashboardsare lukewarm.


We all know how analysts and data scientists talk about dashboards: People who ask for them are analytical Philistines; businesses that show them off are a primitive company’s idea of a sophisticated company. Enlightened data teams shouldn’t be dashboard factories; theyshould help people make better decisions.Data is for understanding which market to expand into, what to charge for a new product, how tomodel stock tradesthat always make money, orwhere to put a new headquarters. And dashboards are a distraction from this much more important work.


I’ve saidlotsofthingslike this before, and, strictly speaking, I don’t think they’re wrong. But I’ve come to realize that this reflexive dismissal of dashboards—and more generally, the discounting of old-school “reporting”—undersells something that we need data for that’s even more foundational than helping us make decisions: Data and the dashboards that display it create a shared sense of reality.


Unlike you and I, companies don't exist in the physical world. When we walk down the street, we can see what's in front us, we can feel the sidewalk underneath us, and we can hear the cars driving past us. If we have to decide if it’s safe to cross the road, the data that goes into that decision—the speed of the traffic, the width of the street, and so on—are measures of that physical world, and generally not controversial. If I choose to cross and you choose to wait, the difference is explained by our analysis of the situation, not because we disagree about the presence of a passing bus.


For companies, there is no physical street. There is no actual bus. These things only exist as abstractions. Data and metrics—revenues, retention rates, product usage patterns—don’t measure a company’s world; theyareits world.


Take ARR, for instance. Though ARR is related to the amount of money in a physical bank account, ARR is a construct.5The code that says that ARR is the sum of the amount field on the Salesforce contract object, that overage fees are excluded, that contracts from partners are included, and that ARR is recognized on the date a contract starts rather than when it closes isn’t measuring ARR; itisARR. If that code changes, our understanding of ARR itself changes.


In other words, the Salesforce calculations or dbt models that encode an ARR metric areaccounting identities: They are true by definition. The code is the concept, and the concept is the code.


In this way, companies don’t live in a physical world, but in a virtual one, like those in Pixar movies. The landscape around a company is artificial, and exists only as a rendered representation of the calculations that define it. And to make decisions in that world, you have to create it first.


For example, suppose a company is trying to decide which product to build next. They want to make a good choice; metaphorically, they want to safely cross the street. To do this, they’d first define the street by setting a goal, such as increasing product adoption. Next, they identify what represents the traffic, or the various factors that might be obstacles to their goal, like product NPS, customer churn rates, and measures of development cost. Finally, in order toassess their path to the other side of the road, they then have to render this world by turning data into metrics. But likeToy Story, none of this is real; it’s an interpretation of numbers and a representation of code. If we define market share differently, we change the road under our feet. If we compute churn with a different formula, we couldconjure an oncoming bus out of thin air.


If this happens, is there really a bus? We can’t actually say, no more than we can say what the true color of a car is in a Pixar movie. If it’s white in half the scenes and black in the other half, all we can do is reconcile the differences in the code that defines it. But until that happens, neither is more true than the other.


You could make the argument that the true color of the car is what’s in the script—or, analogously, the true value of a metric is the GAAP-approved definition of it. But what do we do when the script doesn’t specify the color, and it’s up to the animator writing the code to choose? Most metrics work this way too. Like a car, “daily active users,” for example, has a generally understood shape, but the details often left to those who actually create it.


As data professionals,thisis our first job—to be reliable animators for our companies.


# The corporate metaverse


For better or for worse, dashboards are the best tool we have for this. Every dashboard is a window into a Pixar scene, and every metric is a rendering of it. Strategic analysis, for all of its necessary benefits, is more like a magnifying glass: It’s great for uncovering detail and texture, but to get our bearings—to safely cross the road—we also need a wider lens.


A broader view alone, however, isn’t enough. That view also needs to be consistent, across people and time. If a bus is flickering in and out of existence in the distance, or I see a bus and you don’t, nobody will be confident enough to step into the street.


This is why questions like “Why doesn't this dashboard match what I see in Google Analytics?" are both irritating and pernicious.6Looking at two dashboards that don’t match is like looking out two adjacent windows and not seeing the same thing. Even small or seemingly insignificant discrepancies—one dashboard says 107,102 people visited the homepage this month, and another says 106,988; the car down the street looks white outside of one window and black outside of another—do more than make us suspicious of a small, out-of-place detail. They’reglitches in the Matrix, orhosts off their loops: They make usquestion the nature of our reality. And for companies, with no physical world to fall back on, the reality that data teams create is the only one they have.


In this light, defining metrics and creating dashboards isn’t banal busywork thatgets in the way of “the more rewarding aspects”of analysts’ jobs. It’s one of the most important things that we do. And as an industry, rather than casting dashboarding aside is a necessary evil, we should recognize and celebrate its importance, just as we do for strategic analysis.


The good news is we already have a model for how to do this: analytics engineering.


At its core, analytics engineering should be a mundane role. Analytics engineers spend most of their time tediouslymaintaining data and managing code, filling an unglamorous gap between the workengineers don’t want to doand the workanalysts do want to do. Just as we belittle building dashboards, analytics engineering could easily be tarred as a dull prerequisite to a more interesting job.


And yet, it’s gone in the opposite direction. Rather than running away from analytics engineering, people areeagerly signing up for it.


Why? The attraction, I think, comes from how much the community values the work. Instead of toiling away in the data stack’s lonely salt mines, analytics engineers—largely through the dbt community—can congregate, celebrate, and commiserate together. They can proudly share their accomplishments, and joke about their frustrations. By creating a home and identity for analytics engineers, dbt and its community leaders created a career for analytics engineers.


As data scientists and analysts keen on breaking away from the BI developer roles of yesteryear, we take a lot of shots at dashboards. Weimplore peopleto make their jobs about something more. We disparage building dashboards as being beneath us.


It’s not. Building consistent dashboards is hard.7Creating a reliable rendering of a company’s world is enormously valuable. The only thing it’s not is cool.


We should make it cool. We should embrace our responsibility to create dashboards just as we’ve embraced analytics engineering. We should praise those who are good at it, give those people credit for the impact they have, and encourage them to take pride in doing it well. Because bad dashboards, just like the bad data that analytics engineers valiantly fix,break stuff.

[1](https://benn.substack.com/p/data-is-for-dashboards#footnote-anchor-1-44900034)

I played soccer and Little Leagueat the elementary schoolwherethis scenewas shot.

[2](https://benn.substack.com/p/data-is-for-dashboards#footnote-anchor-2-44900034)

Which itself was turned into themost incredible engagement photosI’ve ever seen.

[3](https://benn.substack.com/p/data-is-for-dashboards#footnote-anchor-3-44900034)

To hide the robbery, Ghantt removed the tapes from two security cameras. Unfortunately for him, he left the tapes in...sixteen other cameras.

[4](https://benn.substack.com/p/data-is-for-dashboards#footnote-anchor-4-44900034)

If you commit a crime, avoid anything to do with General Patton, apparently.

[5](https://benn.substack.com/p/data-is-for-dashboards#footnote-anchor-5-44900034)

And yes, I get that money is all code now, and it too is just an abstract concept on a Wells Fargo-leased server in an AWS data center somewhere. But whatever, if you want to talk about that, I’m sure there’s some crypto Telegram channel full of bored ape avatars that’ll gladly tell you that U.S. dollars are just a construct too.

[6](https://benn.substack.com/p/data-is-for-dashboards#footnote-anchor-6-44900034)

Substack,what’s up?

[7](https://benn.substack.com/p/data-is-for-dashboards#footnote-anchor-7-44900034)

To create a consistent reality with dashboards, you have to do a lot more than skim a couple Tufte books. You have to be disciplined: The more dashboards and metrics we build, the more opportunities we have to create inconsistent views. You have to be stern: If people ask for a new metric, even as a one-off request to “pull the numbers,” we are better off directing them to one that already exists. You have to be organized: Good metrics are built on smartly architected data models in dbt (and hopefully, clean definitions in soon-to-bemetrics layers). And you have to be communicative: Some apparent inconsistencies—like differences inrevenue, bookings, and billings—aren’t glitches, butfeel like they are. We have to keep people confident in what they’re seeing, despite these quantitative illusions.
