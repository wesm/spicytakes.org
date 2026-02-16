---
title: "From Cloudwashing to O11ywashing"
date: 2025-11-24
url: https://charity.wtf/2025/11/24/from-cloudwashing-to-o11ywashing/
word_count: 1422
---


I was just watching a panel on observability, with a handful of industry executives and experts who shall remain nameless and hopefully duly obscured—their identities are not the point, the point is that this is a mainstream view among engineering executives and my head is exploding.


Scene: the moderator asked a fairly banal moderator-esque question about how happy and/or disappointed each exec has been with their observability investments.


One executive said that as far as traditional observability tools are concerned (“are there faults in our systems?”), that stuff “generally works well.”


However, what they *really* care about is observing the quality of their product from the customer’s perspective. EACH customer’s perspective.


![Nines don't matter if users aren't happy](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/11/nines-1.jpeg?resize=231%2C307&ssl=1)

*Nines don’t matter if users aren’t happy*


“Did you know,” he mused, “that there are LOTS of things that can interrupt service or damage customer experience that won’t impact your nines of availability?”


(I begin screaming helplessly into my monitor.)


“You could have a dependency hiccup,” he continued, oblivious to my distress. “There could be an issue with rendering latency in your mobile app. All kinds of things.”


(I look down and realize that I am literally wearing [this shirt](https://www.bonfire.com/nines-dont-matter-stacked/).)


He finishes with,“And that is why we have invested in our own custom solution to measure key workflows through startup payment and success.”


(I have exploded. Pieces of my head now litter this office while my headless corpse types on and on.)


It’s twenty fucking twenty five. How have we come to this point?


## Observability is now a billion dollar market for a meaningless term


My friends, I have failed you.


It is hard not to register this as a colossal fucking failure on a personal level when a group of modern, high performing tech execs and experts can all sit around a table nodding their heads at the idea that “traditional observability” is about whether your systems are UP👆 or DOWN👇, and that the idea of *observing the quality of service from each customer’s perspective* remains unsolved! unexplored! a problem any modern company needs to write custom tooling from scratch to solve.


This guy is literally describing the original definition of observability, and he doesn’t even know it. He doesn’t know it *so hard* that he went and built his own thing.


You guys know this, right? When he says “traditional observability tools”, he means *monitoring tools*. He means the whole three fucking pillars model: metrics, logging, and tracing, all separate things. As he notes, these traditional tools are entirely capable of delivering on basic operational outcomes (are we up, down, happy, sad?). They can DO this. They are VERY GOOD tools if that is your goal.


But they are *not* capable of solving the problem he *wants* to solve, because *that* would require combining app, business, and system telemetry in a *unified way*. Data that is traceable, but not just tracing. With the ability to slice and dice by any customer ID, site location, device ID, blah blah. Whatever shall we call THAT technological innovation, when someone invents it? Schmobservability, perhaps?


So anyway, “traditional observability” is now part of the mainstream vernacular. Fuck. What are we going to do about it? What CAN be done about it?


## From cloudwashing to o11ywashing


I learned a new term yesterday: *cloudwashing*. I learned this from [Rick Clark](https://www.linkedin.com/in/dendrobates/), who tells a hilarious story about the time IBM got so wound up in the enthusiasm for cloud computing that they reclassified their Z series mainframe as “cloud” back in 2008.


(Even more hilarious: asking Google about the precipitating event, and following the LLM down a decade-long wormhole of incredibly defensive posturing from the IBM marketing department and their paid foot soldiers in tech media about how this always gets held up as an example of peak cloudwashing but it was NOT AT ALL cloudwashing due to being an extension of the Z/Series Mainframe rather than a REPLACEMENT of the Z/Series Mainframe, and did you know that Mainframes are bigger business and more relevant today than ever before?)


(Sorry, but I lost a whole afternoon to this nonsense, I had to bring you along for the ride.)


Rick says the same thing is happening right now with observability. And *of course it is*. It’s too big of a problem, with too big a budget: an irresistible target. It’s not just the legacy behemoths anymore. Any vendor that does anything remotely connected to telemetry is busy painting on a fresh coat of o11ywashing. From a marketing perspective, It would be irresponsible not to.


## How to push back on *-washing


Anyway, here are the key takeaways from my weekend research into cloudwashing.

1. This o11ywashing problem isn’t going away. It is only going to get bigger, because the problem keeps getting bigger, because the traditional vendors aren’t solving it, because they *can’t* solve it.
2. The Gartners of the world will help users sort this out someday, maybe, but only after we win. We can’t expect them to alienate multibillion dollar companies in the pursuit of technical truth, justice and the American Way. If we ever want to see “Industry Experts” pitching in to help users spot o11ywashing, as they eventually did with cloudwashing (see exhibit A), we first need to win in the market.
Exhibit A: “How to Spot Cloudwashing”
3. And (this is the only one that really matters.) we have to do a better job of **telling this story to engineering executives**, not just engineers. Results and outcomes, not data structures and algorithms.



(I don’t want to make this sound like an epiphany we JUST had…we’ve been working hard on this for a couple years now, and it’s starting to pay off. But it was a powerful confirmation.)


## Talking to execs is different than talking to engineers


When Christine and I started Honeycomb, nearly ten years ago, we were innocent, doe-eyed engineers who truly believed on some level that if we just explained the technical details of cardinality and dimensionality clearly and patiently enough to the world, enough times, the consequences to the business would become obvious to everyone involved.


It has now been ten years since I was a hands-on engineer every day (say it again, like pressing on a bruise makes it hurt less), and I would say I’ve been a decently functioning exec for about the last three or four of those years.


What I’ve learned in that time has actually given me a lot of empathy for the different stresses and pressures that execs are under.


I wouldn’t say it’s less or more than the stresses of being an SRE on call for some of the world’s biggest databases, but it is a deeply and utterly *different* kind of stress, the kind of stress less expiable via fine whiskey and poor life choices. (You just wake up in the morning with a hangover, and the existential awareness of your responsibilities looming larger than ever.)


## This is a systems problem, not an operational one


There is a lot of noise in the field, and executives are trying to make good decisions that satisfy all parties and constraints amidst the unprecedented stress-panic-opportunity-terror of AI changing everything. That takes storytelling skills and sales discipline on our part, in addition to technical excellence.


Companies are dumping more and more and more money into their so-called observability tools, and not getting any closer to a solution. Nor will they, so long as they keep thinking about observability in terms of operational outcomes (and buying operational tools). **Observability is a systems problem**. It’s the most powerful lever in your arsenal when it comes to disrupting software doom spirals and turning them into positive feedback loops. Or it should be.


As [Fred Hebert](http://ferd.ca) might say, it’s great you’re so good at firefighting, but maybe it’s time to go read the city fire codes.


Execs don’t know what they don’t know, because we haven’t been speaking to them. But we’re starting to.


## What will be the next term that gets invented and coopted in the search to solve this problem?


Where to start, with a project so big? Google’s AI says that “experts suggest looking for specific features to identify true cloud observability solutions versus cloudwashed o11ywashed ones.”


I guess this is a good place to start as any: If your “observability” tooling doesn’t help you understand the quality of your product from the customer’s perspective, EACH customer’s perspective,** it isn’t fucking observability. **


It’s just monitoring dressed up in marketing dollars.


Call it o11ywashing.
