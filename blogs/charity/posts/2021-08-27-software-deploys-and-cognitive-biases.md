---
title: "Software deploys and cognitive biases"
date: 2021-08-27
url: https://charity.wtf/2021/08/27/software-deploys-and-cognitive-biases/
word_count: 1420
---


There exist some wonderful teams out there who have valid, well thought through, legitimate reasons for enforcing “NO FRIDAY DEPLOYS” week in and week out, for not hooking CI/CD up to autodeploy, and for not shipping one person’s changes at a time.


And then there are the reasons most people have.


### Bad decisions, and the biases they came from

- “It is more dangerous to deploy than not to deploy” (prevention bias, zero-risk bias)
- “It’s *always* riskier to do something than to not do something” (omission bias)
- “Deploys are scary, so we need to slow down and be careful.”([slow motion bias](http://slow-motion-bias))
- “We’ve always done it this way; it works fine, you’re exaggerating, it doesn’t slow us down like those stories you tell.” (plan continuation bias, mere-exposure effect, time-saving bias, status-quo bias, default effect)
- “Maybe that works for some teams, like baby startups, but not *real* software systems that people rely on” (false-uniqueness bias)
- “We’ve already invested a ton of engineering hours into building a deployment framework that doesn’t ship especially fast and doesn’t ship one change at a time, but it works, and we don’t want to have to redo everything from scratch.” (surrogation, ostrich effect, irrational escalation, ikea-effect, law of the instrument)
- “I get why it’s important, but the most important thing *right now* is for us to ship all of these features. At some point we’ll have the spare time to fix our deploys.” (hyperbolic discounting)
- “We tried it once, and the whole site went down. Never again.” (non-adaptive choice switching, selective perception)
- “Everybody says that no Friday deploys is the safe, sane, and caring choice.” (illusory truth effect, surrogation, continued influence effect, conservatism bias)
- “Deploys are just inherently scary; there’s nothing that can be done about that. You should do them sparingly and with someone monitoring it closely.” (availability bias, dread aversion, functional fixedness)
- “The best way to protect people’s personal time is to let merged code pile up between Thursday night and Monday morning, and ship all at once.” (continued-influence effect, plan-continuation bias, pseudocertainty effect, zero-risk bias)
- “There is nothing anyone could say or do to convince me that the best thing I can do as a manager to protect their weekends is not blocking Friday deploys. I just feel it in my gut. I just *know.*” (… I got nuthin)


We’re humans. 💜  We leap to conclusions with the wetware we have doing the best it can based on heuristics that *feel* objectively true, but are ultimately just emotional reactions based on past lived experience. And then we retroactively enshrine those goofy gut feelings with the language of noble motive and moral values.


> *“I tell people not to deploy to production … because I care so deeply about my team and their ability to have a quiet weekend.”*


Barf. 🙄  That’s just like saying you tell your kid not to brush his teeth at night, because you care SO DEEPLY about him and his ability to go to bed calm and happy.


Once the retcon engine in your brain gets running, it comes up with all sorts of reasons. Plausible-sounding reasons! But every single argument of the items in the list above is **materially false**.


Deploy myths are never going away for good; they appeal to too many of our cognitive biases. But what if there was one simple thing you could do that would invert many of these cognitive biases and cause people to grapple with the question in a new way? What if you could kickstart a recalculation?


My next post will pick up right here. I’ll tell you all about the One Simple Trick you can do to fix your deploys and set you on the virtuous path of high-performing teams.


Til then, here’s what I’ve previously written on the topic.


### Footnotes


**Availability bias**: The tendency to overestimate the likelihood of events with greater “availability” in memory, which can be influenced by how recent the memories are or how unusual or emotionally charged they may be.


**Continued influence effect**: The tendency to believe previously learned misinformation even after it has been corrected. Misinformation can still influence inferences one generates after a correction has occurred.


**Conservatism bias:** The tendency to revise one’s belief insufficiently when presented with new evidence.


**Default effect: **When given a choice between several options, the tendency to favor the default one.


**Dread aversion**: Just as losses yield double the emotional impact of gains, dread yields double the emotional impact of savouring


**False-uniqueness bias: **The tendency of people to see their projects and themselves as more singular than they actually are.


**Functional fixedness: **Limits a person to using an object only in the way it is traditionally used


**Hyperbolic discounting:** Discounting is the tendency for people to have a stronger preference for more immediate payoffs relative to later payoffs. Hyperbolic discounting leads to choices that are inconsistent over time – people make choices today that their future selves would prefer not to have made, despite using the same reasoning


**IKEA effect: **The tendency for people to place a disproportionately high value on objects that they partially assembled themselves, such as furniture from IKEA, regardless of the quality of the end product


**Illusory truth effect: **A tendency to believe that a statement is true if it is easier to process, or if it has been stated multiple times, regardless of its actual veracity.


**Irrational escalation: **The phenomenon where people justify increased investment in a decision, based on the cumulative prior investment, despite new evidence suggesting that the decision was probably wrong. Also known as the sunk cost fallacy


**Law of the instrument: **An over-reliance on a familiar tool or methods, ignoring or under-valuing alternative approaches. “If all you have is a hammer, everything looks like a nail”


**Mere exposure effect: **The tendency to express undue liking for things merely because of familiarity with them


**Negativity bias: **Psychological phenomenon by which humans have a greater recall of unpleasant memories compared with positive memories


**Non-adaptive choice switching: **After experiencing a bad outcome with a decision problem, the tendency to avoid the choice previously made when faced with the same decision problem again, even though the choice was optimal


**Omission bias: **The tendency to judge harmful actions (commissions) as worse, or less moral, than equally harmful inactions (omissions).


**Ostrich effect: **Ignoring an obvious (negative) situation


**Plan continuation bias: **Failure to recognize that the original plan of action is no longer appropriate for a changing situation or for a situation that is different than anticipated


**Prevention bias: **When investing money to protect against risks, decision makers perceive that a dollar spent on prevention buys more security than a dollar spent on timely detection and response, even when investing in either option is equally effective


**Pseudocertainty effect: **The tendency to make risk-averse choices if the expected outcome is positive, but make risk-seeking choices to avoid negative outcomes


**Salience bias**: The tendency to focus on items that are more prominent or emotionally striking and ignore those that are unremarkable, even though this difference is often irrelevant by objective standards


**Selective perception bias: **The tendency for expectations to affect perception


**Status-quo bias**: If no special action is taken, the default action that will happen is that the code will go live. You will need an especially compelling reason to override this bias and manually stop the code from going live, as it would by default.


**Slow-motion bias**: We feel certain that we are more careful and less risky when we slow down. This is precisely the opposite of the real world risk factors for shipping software. *Slow is dangerous for software*; *speed is safety*. The more frequently you ship code, the smaller the diffs you ship, the less dangerous each one actually becomes. This is the most powerful and difficult to overcome of all of our biases, because there is no readily available counter-metaphor for us to use. (Riding a bike is the best I’ve come up with. 😔)


**Surrogation: **Losing sight of the strategic construct that a measure is intended to represent, and subsequently acting as though the measure is the construct of interest


**Time-saving bias: **Underestimations of the time that could be saved (or lost) when increasing (or decreasing) from a relatively low speed and overestimations of the time that could be saved (or lost) when increasing (or decreasing) from a relatively high speed.


**Zero-risk bias: **Preference for reducing a small risk to zero over a greater reduction in a larger risk.
