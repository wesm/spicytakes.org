---
title: "Work like an analyst"
subtitle: "We’re not so different, business stakeholder and I."
date: 2022-03-04T17:09:57+00:00
url: https://benn.substack.com/p/work-like-an-analyst
slug: work-like-an-analyst
word_count: 1613
---


![](https://substackcdn.com/image/fetch/$s_!H7Al!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fadb05705-75ef-4b5e-b38a-a83632f157cf_1200x800.jpeg)

*Guts. Glory. A mini donut drive-thru. Ram.*


A couple weeks ago, the data community was overtaken by a giant debate, the likes of which not seen since the data mesh entered the chat in 2021, about whether or not the stack is beingunbundledorrebundled,andwhatitallmeans. It was aperiodic flare-upof the only thingwe can ever talk about, and, if nothing else, proof that, no matter how much we fight withGartner and their ilk, we also can't help butput things in their pedantic little boxes.


I’m not here to choose a side in that discussion. In my view, the middle layer of the data stack—say, everything after ingestion and before consumption—is neither being bundled or unbundled; it’s simply being reconstituted. Some components are being pulled apart, others are getting mixed together, and the final product will look nothing like its former parts. We aren’t building a Lego from discrete blocks, or disassembling a set into individual pieces;1we’re making a stew. You could argue, I suppose, that chefs unbundle potatoes from the peel and meat from the bone, and thenrebundle it with a pot and some broth. I’d argue that that’s a weird choice of verb.


But that’s not to say there’s no bundling happening in the data ecosystem. It’s just happening in a different place.


# How companies do analysis


When we first started Mode, we expected our users to fall into two clear categories: Analysts, and everyone else. Analysts, we thought, would live in Mode’s SQL editor, write lots of queries, and distribute their work to their colleagues. Everyone else—the non-analysts2—would look at dashboards and poke at reports, but wouldn’t write queries. Very few people, we assumed, would exist in the middle as occasional query authors. Just as people who aren’t designers create very few assets in Photoshop, we thought people who weren’t analysts would write very few queries in Mode.


![](https://substackcdn.com/image/fetch/$s_!cH8V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6e4ccda-2a7e-441f-b5f7-0a4490ceadeb_1306x762.png)

*What we thought our usage distribution graphs would look like*


We were wrong. Analysis, even SQL-based analysis, isn’t like design, where a handful of people create stuff and everyone else is a consumer, with clear lines between them. It’s much,muchfuzzier. Though analysts were always our first adopters, lots of people—PMs, engineers, marketing managers, executives, support agents, operations leads, and all job titles in between—periodically wrote queries. These people occupied the middle part of the distribution between analysts and non-analysts that we thought would be vacant. Users weren’t bimodal like we expected, but continuous.


![](https://substackcdn.com/image/fetch/$s_!RRXr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8f85bd2c-0942-46f8-ba0f-147b20b40285_1298x770.png)

*What our usage distribution graphs actually looked like.*


Moreover, non-analysts gradually deepened their technical usage (i.e., query writing) over time. After being exposed to their company’s data, people who we didn’t classify as analysts—and, based on their initial behavior, didn’t classify themselves as analysts either—started to display the same behavioral patterns as analysts.


It’s not surprising that most people want to be part of the analytical process. In many ways, we built Mode for that reason—just asFigma createda “way for non-designers to be involved in the design process,” we wanted to do the same for analysis.


Whatissurprising is the lengths people went to be involved. When we first identified these behaviors, Mode didn’t offer much to non-analysts. The product was heavy on SQL and light on code-free, drag-and-drop interfaces. Mode wasn’t drawing people into the analytical process by developing an accessible way for them to participate; instead, people were participating in the same way that analysts did, just at a less frequent cadence.


Though this is a complex phenomenon to interpret, one explanation stands out above others: Analysis is becoming a team sport. Business stakeholders aren’t kicking questions over to their data help desks and waiting to get reports back to review; everyone is contributing together. A few months ago,Tristan predictedthat analytical talent wouldn’t be concentrated in a “select few specialists,” but would “live inside of operational areas of the business.” If Mode’s customers are any indication, this started happening years ago.


As far as paradigm altering shifts go, this one—analysis becoming multi-functional; the democratization of analytical reasoning and technical talent, not just data—is far more foundational than whatever reshuffling happens among the data stack’s middleware. After all, what ultimately mattersis the experiencethat middleware provides. While it’s right and fair to talk about how ourfragmented SaaS landscapeundermines that experience, that’s only half the equation. Applications need to be complementary to one anotherandto the people they’re trying to serve.


For decades, the industry has thought of those people the way we did at Mode in the early days: different, divided, and discrete. This belief is embedded across the entire data ecosystem. Products have technical and non-technical faces; vendors distinguish between analyst and non-analyst seats; brands are built around which side of the spectrum you favor; Gartner tells you you need to buytworeportsand not one.


What do we do if this changes? What happens if, ten years from now, we can’t separate between analysts from their opposite—not because we don’t know what to call the latter group, but because they no longer fill clearly distinct roles?


# Where we’re going, we still need roads


It’s awards season, and let me propose a perennial Oscar snub: The American Truck Commercial. Seemingly thousands of these spots get churned out every year, and all of them follow the same spectacular arc: They show a truck, perfectly polished, bounding through the American West. Over amontage of farmland jingoism, a man—he’s never shown, but we can see him, in his 50s, a smoker with calloused hands, squinting in the late Montana sun, rough but not unkind, beaten down but not broken—talks aboutfreedom,hard work, and how,out here, we don’tdrink oat milkoruse the internet. We see trucksplowing snow; we see trucksdrifting through deserts; we see trucks towingtrees,boats, andheavy machinery; we see trucksforging rivers;3we see trucks offroadingup mountains,through snow, andover rocksin the protected areas of the Badlands National Park. We do not see pavement, women,4or people of color.


Having grown up in a place where people buy a lot of trucks, I can assure you, this is not what people do with them. They don’t haulspace shuttles; they drive their trucks on the interstate and idle them in Wendys’ drive-thrus.


But this paradox is why they’re popular. While trucks can hypothetically “conquer Denali,” roads are pretty useful too. Even if you want to gomuddingat the dirt spot, you can’t drive aswamp buggydown I-85 to get there.5


Trucks, by contrast, can be luxury vehicles while simultaneously embodying America’s pioneer ideals: Offroading on parking lot medians at high school football games.6They’re spacious and comfortable enough to take the family on a road trip to the beach, and rugged enough to (hypothetically)drive in the oceanonce you’re there.


Compare this to the alternative modes of transportation, like traveling by plane, then train, then car, then dirt bike. These vehicles live on their own thoroughfares, each disconnected from the other. And each requires a new set of skills to operate. You need a pilot to fly you from Des Moises to Houston, a conductor to run the train to Galveston, a driver to taxi you to the beach, and a fourth expert to teach you to ride a dirt bike on the beach. With a truck—and an overlapping system of highways and roads—one person, in one machine, can do it all.


For decades, the data industry hasn’t had a truck. We've had power tools for analysts, meant to be driven by elite experts across treacherous and unexplored terrain. And we’ve had simple reporting applications for everyone else, designed to be put on cruise control across well-trafficked highways. Because neither was created for the other’s domain—you can’t drive a four-wheeler across the country, or a Greyhound through theLost Coast—these two sets of roads remained disconnected, as did the people who drive on them.


In practice, this means that people often operate in different tools—and live indifferent realities. People who spend their time looking at dashboards see one view of the business; people who are investigating problems see another. Even if these worlds aren’t contradictory, they’re not often shared.


In the past, when thinking about this technical divide,I’ve assumed it was a product problem. Over the last decade, we’ve created a lot of specialized tools, and segregated our “jobs to be done” as a result. If only we could better connect these tools—if only our criss-crossing BI highways had off-ramps to the detailed city streets, and the ad hoc trails in the countryside beyond—we’d solve this problem.


I’m now realizing that misses the real point: The divisions of labor between analysts and everyone else are fading. Analysis is getting bundled with other functions; the behaviors of analysts and non-analysts are overlapping; analysts are becomingpositionless. The reason to build a “modern data experience” isn’t to unify the disjointed products of a bunch of startups; it’s to serve a world in which far more people want to work like analysts.


That’s a much bigger—and harder—ambition. But fortunately for us, if we need a recommendation on how to bring red and blue people together into apurple center, there’s atruck commercial for that too.

[1](https://benn.substack.com/p/work-like-an-analyst#footnote-anchor-1-49737761)

But if weweretaking apart a Lego,Joelcan tell you whatcolor your pile of pieceswould be.

[2](https://benn.substack.com/p/work-like-an-analyst#footnote-anchor-2-49737761)

Business users? Domain experts? Stakeholders? Non-technical users? People you want to hang out with?SELECT * FROM people p LEFT JOIN analysts a ON a.person_id = p.person_id WHERE a.person_id IS NULL?

[3](https://benn.substack.com/p/work-like-an-analyst#footnote-anchor-3-49737761)

Your F-150 broke an axle, Josephine got dysentery, and everyone died before you made it out of Nebraska. But on the bright side, you did collect four tons of buffalo meat from hunting nine times in two days.

[4](https://benn.substack.com/p/work-like-an-analyst#footnote-anchor-4-49737761)

The truck commercialBechdel test: Do women exist?

[5](https://benn.substack.com/p/work-like-an-analyst#footnote-anchor-5-49737761)

This sentence is, in fact, real.

[6](https://benn.substack.com/p/work-like-an-analyst#footnote-anchor-6-49737761)

Those who drove, say, their grandmother’s1998 Pontiac Grand Amwere confined to concrete roads of communism.
