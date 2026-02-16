---
title: "Got opinions on observability? I could use your help (once more, with feeling)"
date: 2025-10-13
url: https://charity.wtf/2025/10/13/got-opinions-on-observability-i-could-use-your-help-once-more-with-feeling/
word_count: 1446
---


Last month I dropped a desperate little [plea for help](https://charity.wtf/2025/09/19/are-you-an-experienced-software-buyer-i-could-use-some-help/) in this space, asking people to email me any good advice and/or strong opinions they happened to have on the topic of buying software.


I wasn’t really sure what to expect — desperate times, desperate measures — but holy crap, you guys delivered. To the many people who took the time to write up your experiences and expertise for me, and suffer through rounds of questions and drafts: ✨**thank you**✨. And thank you, too, to those of you who forwarded my queries along to experts in your network and asked for help on my behalf.


I learned a LOT about buying software and managing vendor relationships in the process of writing this. Honestly, this chapter is shaping up to be one of the things I’m most excited about for the second edition of the book.


## Why I’m excited about the software buying chapter (& you should be too)


I’m imagining you reading this with a skeptical expression and an arched eyebrow. “*Really*, Charity…‘how to buy software’ doesn’t exactly suggest peak engineering prowess.”


Au contraire, my friends. I’ve come to believe that vendor engineering is one of the subtlest and most powerful practical applications of deep subject matter expertise, and some of the highest leverage work an engineer can do. How often do you get to make decisions that leverage the labor of hundreds or thousands of engineers per year, for fractions of pennies on the dollar? How many of the decisions you make will have an impact on every single engineer you work with and their ability to do their jobs well, as well as the experience of every single customer?


If you think I’m hyperventilating a bit, nah; this is entry level shit. In the book, I tell the story of the best engineer I ever worked with, and how I watched him alter the trajectory of multiple other companies, *none of which he was working for, buying from, or formally connected to in any way* — in the space of a few conversations. It upended my entire worldview about what it can look like for an engineer to wield great power.


Doing this stuff well takes both technical depth and technical breadth, in addition to systems thinking and knowledge of the business. It is one of the *only* ways a staff+ engineer can acquire and develop executive-level communication, strategy, and execution skills while remaining an individual contributor.


I’ve been wanting to write about this for YEARS. Anyway — ergh! — I’m rambling now. That was not what I came here to talk about, I’m just excited. Back to the point.


## My second (and final) round of questions


I got *so much* out of your thoughtful responses that I thought I’d press my luck and put a few more questions out to the universe, before it’s too late.


These questions speak to areas where I worry that my writing may be a little weak or uninformed, or too far away from the world where people are using the “three pillars” model ([aka multiple pillars](https://charity.wtf/2025/03/24/another-observability-3-0-appears-on-the-horizon/) or o11y 1.0) and *happy* about it. I don’t know many (any??) of those people, which suggests some pretty heavy selection bias.


I don’t expect anyone to answer *all* the questions; if one or two resonate with you, write about those and ignore the rest. If there’s something I didn’t ask that I should have asked, answer that. Something I’ve written in the past that bugged you that you hope I won’t say again? Tell me! We are almost out of time ⌛ so gimme what you got. 🙌


### On migrations:


📈 Have you ever migrated from one observability vendor to another? If so, what did you learn? What was the hardest part, what took you by surprise? What do you wish you could go back in time and tell your self at the start?


📈 If you ran (or were involved in) a large scale migration or tool change… how did you structure the process? Like, was it team by team, service by service, product by product? Did you have a playbook? What did you do to make it fun or push through organizational inertia? How long did it take?


### On managing costs for the traditional three pillars:


📈 For orgs that are using Datadog, Grafana, Chronosphere, or another traditional three pillars architecture.. How would you describe your approach to cutting and controlling costs? Pro tips and/or comprehensive strategy.


📈 Alternately, if there are particular blog posts with advice you have followed and can personally vouch for, would you send me a link?


📈 How do you guide your software engineers on which data to send to which place — metrics, logs, traces, errors/exceptions, profiling, etc? How do you manage cardinality? How do you work to keep the pillars in sync, or are there any particular tips and tricks you have for linking / jumping between the data sources?


📈 How many ongoing engineering cycles does it take to manage and maintain costs, once you’ve gotten them to a sustainable place?


### On managing costs at massive scale:


(Especially for people who work at a large enterprise, the kind with multiple business units, but others welcome too!):

- Do you use tiers of service for managing costs? How do you define those?
- How do new tools get taken for a spin? (Like, sometimes there is an office of the CTO with carte blanche to try new things and evaluate them for the rest of the org)
- How do you use telemetry pipelines?


### Observability teams (quick poll):


📈 If you have an observability team, how big is it? What part of the org does it report up into? Roughly how many engineers does that team support?


📈 If you don’t have an observability team — and you have more than, say, 300 engineers — who owns observability? Platform? SRE? Other?


### A grab bag:


📈 **Build vs Buy: **If you built your own observability tool(s)…. What were the reasons? What does it do? Would you make the same decision today?


📈 **OpenTelemetry: **If your team has weighed the pros and cons of adopting OTel and ultimately decided not to, for technical or philosophical reasons (i.e. not just “we’re too busy”) — what are those reasons?


📈 **Instrumentation:** what do you do to try and remove cognitive overhead for engineers? How much have you been able to make automatic and magical, and where has the magic failed?


📈 **Consolidation: **I would love to hear any thoughts on tool consolidation vs tool proliferation. Is this primarily driven by execs, or do technical users care too? Is it driven by cost concerns, usability, or something else?


edited on 2025-10-15 to add… oh crap, one last question:


📈 **Open source**: Are you using open source observability tools, and if so, are these your primary tools or one piece of a comprehensive tooling strategy? If the latter, could you describe that strategy for me?


## Send it to me in an email


Please send me your opinions or answers in an email, to my first name at honeycomb dot io, with the subject line “Observability questions”.


If I end up cribbing from your material, it okay for me to print your name? (As in, “thanks to the people who informed my thinking on this subject, abc xyz etc”). I will not mention your employer or where you work, don’t worry.


If you send it to me more than a week from now, I probably won’t be able to use it. Augh, I wish I had thought of this in JUNE!!! #ragrets


## ✨THANK YOU✨


I know this is an incredibly time consuming thing to ask of someone, and I can’t express how much I appreciate your help.


P.S. Yes, the title is absolutely a reference to the Buffy musical. Hey, I had to give you guys something fun to read along with my second bleg in less than a month (do people still say “bleg”??).


P.P.S. **Grammar quiz of the day**: should my title read “opinions ABOUT observability” or “opinions ON observability” ??


GREAT QUESTION — and, as it turns out, the preposition you choose may reveal more than you realized.


“About” is used to introduce a topic or subject in a broad, vague, or approximate sense, while “on” is used to signal more detailed, specific, formal or serious subject matter (as well as physical objects). “Let’s talk about dinner” vs “she delivered a lecture on why AI is trying to kill babies.”


Or as Xander says, “To read makes our English speaking good.”


The earth is doomed,

~charity
