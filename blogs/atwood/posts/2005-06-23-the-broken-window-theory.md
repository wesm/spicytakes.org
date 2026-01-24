---
title: "The Broken Window Theory"
date: 2005-06-23
url: https://blog.codinghorror.com/the-broken-window-theory/
slug: the-broken-window-theory
word_count: 959
---

In a [previous entry](https://blog.codinghorror.com/pragmatic-programming/), I touched on the broken window theory. You might be familiar with [the Pragmatic Progammers’ take](http://www.artima.com/intv/fixit.html) on this:


> Don’t leave “broken windows” (bad designs, wrong decisions, or poor code) unrepaired. Fix each one as soon as it is discovered. If there is insufficient time to fix it properly, then board it up. Perhaps you can comment out the offending code, or display a “Not Implemented” message, or substitute dummy data instead. Take some action to prevent further damage and to show that you’re on top of the situation.
> We’ve seen clean, functional systems deteriorate pretty quickly once windows start breaking. There are other factors that can contribute to software rot, and we’ll touch on some of them elsewhere, but **neglect accelerates the rot faster than any other factor.**


That’s excellent advice for programmers, but it’s not the complete story.


![](https://blog.codinghorror.com/content/images/2025/05/image-108.png)


The broken window theory is based on an [Atlantic Monthly article](https://www.theatlantic.com/ideastour/archive/windows.html) published in 1982. It’s worth reading the article to get a deeper understanding of the human factors driving the theory:


> Second, at the community level, disorder and crime are usually inextricably linked, in a kind of developmental sequence. Social psychologists and police officers tend to agree that if a window in a building is broken and is left unrepaired, all the rest of the windows will soon be broken. This is as true in nice neighborhoods as in rundown ones. Window-breaking does not necessarily occur on a large scale because some areas are inhabited by determined window-breakers whereas others are populated by window-lovers; rather, one unrepaired broken window is a signal that no one cares, and so breaking more windows costs nothing. (It has always been fun.)
> Philip Zimbardo, a Stanford psychologist, reported in 1969 on some experiments testing the broken-window theory. **He arranged to have an automobile without license plates parked with its hood up on a street in the Bronx and a comparable automobile on a street in Palo Alto, California.** The car in the Bronx was attacked by “vandals” within ten minutes of its “abandonment.” The first to arrive were a family – father, mother, and young son – who removed the radiator and battery. Within twenty-four hours, virtually everything of value had been removed. Then random destruction began – windows were smashed, parts torn off, upholstery ripped. Children began to use the car as a playground. Most of the adult “vandals” were well-dressed, apparently clean-cut whites. **The car in Palo Alto sat untouched for more than a week. Then Zimbardo smashed part of it with a sledgehammer. Soon, passersby were joining in. Within a few hours, the car had been turned upside down and utterly destroyed. Again, the “vandals” appeared to be primarily respectable whites.**
> Untended property becomes fair game for people out for fun or plunder and even for people who ordinarily would not dream of doing such things and who probably consider themselves law-abiding. Because of the nature of community life in the Bronx – its anonymity, the frequency with which cars are abandoned and things are stolen or broken, the past experience of “no one caring” – vandalism begins much more quickly than it does in staid Palo Alto, where people have come to believe that private possessions are cared for, and that mischievous behavior is costly. But vandalism can occur anywhere once communal barriers – the sense of mutual regard and the obligations of civility – are lowered by actions that seem to signal that “no one cares.”


There’s even an [entire book on this subject](http://www.amazon.com/exec/obidos/ASIN/0684837382/). What’s fascinating to me is that the mere *perception* of disorder – **even with seemingly irrelevant petty crimes like graffiti or minor vandalism** – precipitates a negative feedback loop that can result in total disorder:


> We suggest that “untended” behavior also leads to the breakdown of community controls. A stable neighborhood of families who care for their homes, mind each other’s children, and confidently frown on unwanted intruders can change, in a few years or even a few months, to an inhospitable and frightening jungle. A piece of property is abandoned, weeds grow up, a window is smashed. Adults stop scolding rowdy children; the children, emboldened, become more rowdy. Families move out, unattached adults move in. Teenagers gather in front of the corner store. The merchant asks them to move; they refuse. Fights occur. Litter accumulates. People start drinking in front of the grocery; in time, an inebriate slumps to the sidewalk and is allowed to sleep it off. Pedestrians are approached by panhandlers.
> At this point it is not inevitable that serious crime will flourish or violent attacks on strangers will occur. But many residents will think that crime, especially violent crime, is on the rise, and they will modify their behavior accordingly. They will use the streets less often, and when on the streets will stay apart from their fellows, moving with averted eyes, silent lips, and hurried steps. “Don’t get involved.” For some residents, this growing atomization will matter little, because the neighborhood is not their “home” but “the place where they live.” Their interests are elsewhere; they are cosmopolitans. But it will matter greatly to other people, whose lives derive meaning and satisfaction from local attachments rather than worldly involvement; for them, the neighborhood will cease to exist except for a few reliable friends whom they arrange to meet.


Programming is insanely detail oriented, and perhaps this is why: if you’re not on top of the details, the perception is that things are out of control, and it’s only a matter of time before your project spins out of control. **Maybe we should be sweating the small stuff**.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming habits](https://blog.codinghorror.com/tag/programming-habits/)
[clean code](https://blog.codinghorror.com/tag/clean-code/)
[code maintenance](https://blog.codinghorror.com/tag/code-maintenance/)
[software architecture](https://blog.codinghorror.com/tag/software-architecture/)
