---
title: "On the Behavior of the iPhone Mute Switch"
date: 2012-01-13
url: https://daringfireball.net/2012/01/iphone_mute_switch_design
slug: iphone_mute_switch_design
word_count: 449
---


Daniel J. Wakin, [reporting for the NYT](http://www.nytimes.com/2012/01/13/nyregion/ringing-finally-stopped-but-concertgoers-alarm-persists.html?_r=1):


> The unmistakably jarring sound of an iPhone marimba ring
> interrupted the soft and spiritual final measures of Mahler’s
> Symphony No. 9 at the New York Philharmonic on Tuesday night. The
> conductor, Alan Gilbert, did something almost unheard-of in a
> concert hall: He stopped the performance. But the ringing kept on
> going, prompting increasingly angry shouts in the audience
> directed at the malefactor.


Ends up there’s an interesting design problem at the root of the incident:


> Actually, Patron X said he had no idea he was the culprit. He said
> his company replaced his BlackBerry with an iPhone the day before
> the concert. He said he made sure to turn it off before the
> concert, not realizing that the alarm clock had accidentally been
> set and would sound even if the phone was in silent mode.
> “I didn’t even know phones came with alarms,” the man said.


[As Jim Biancolo notes](http://www.biancolo.com/articles/bad-ui-stops-symphony):


> Ouch! I certainly understand the design tradeoff: would you rather
> put people at risk of public humiliation when their silent phones
> makes noise, or would you rather have somebody sleep through an
> important meeting because they silenced their phone, forgetting
> about their alarm clock?
> I’d vote for silencing *everything* when you mute the phone, but
> pop a warning if you mute the phone with alarms pending. Or maybe
> a warning that lets you choose whether you want to also silence
> alarms or not?


I agree with Biancolo that this is a tricky trade-off, but I disagree with his suggestions. Adding alerts and confirmation prompts is seldom a good idea, and would not help at all when you toggle the mute switch without even looking at the iPhone. (I frequently toggle that switch without taking the phone out of my pocket.)


I think the current behavior of the iPhone mute switch is correct. You can’t design around every single edge case, and a new iPhone user who makes the reasonable but mistaken assumption that the mute switch silences everything, with an alarm set that he wasn’t aware of, and who is sitting in the front row of the New York Philharmonic when the accidental alarm goes off, is a pretty good example of an edge case.


Whereas if the mute switch silenced everything, there’d be thousands of people oversleeping every single day because they went to bed the night before unaware that the phone was still in silent mode.



| **Previous:** | [The Church of Market Share](https://daringfireball.net/2012/01/the_church_of_market_share) |
| **Next:** | [Why Are Android Smartphones Bigger Than the iPhone?](https://daringfireball.net/2012/01/why_are_android_phones_bigger) |


PreviousNext