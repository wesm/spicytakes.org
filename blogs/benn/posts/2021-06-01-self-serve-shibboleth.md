---
title: "The self-serve shibboleth"
subtitle: "We all like to talk about it. But how do we fix it?"
date: 2021-06-01T22:31:14+00:00
url: https://benn.substack.com/p/self-serve-shibboleth
slug: self-serve-shibboleth
word_count: 1569
---


![](https://substackcdn.com/image/fetch/$s_!jHMG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5cec544a-78ea-49f7-a0a0-76ac661bea2f_512x341.jpeg)

*“What exit?”*


I'm convinced that every field has “senior shibboleths:'' ideas that sound contrarian to the uninitiated, but are, among people with more experience, pretty conventional. These ideas, which are sometimes wise, sometimes trite, and sometimes dangerously wrong, might start as novel theories, but they eventually become secret handshakes for sorting who’s in the club and who’s not. When someone shares one of them, we signal our membership by nodding along knowingly. The fastest way to be taken seriously by people who take themselves seriously isn’t coming up with your own ideas, but knowing when to quote-tweet “^ this.”


Spend enough time with industry veterans, and you’ll pick up on their passwords. Senior developers joke that the hard part of engineering isn’t technology, but people. Political talking heads on Twitter wink at each other by saying Beltway intrigue is boring and meaningless to “real” Americans.1Baseball pitchers show they’re in the know by complaining that they’ll forgive a bad umpire, but not an inconsistent one.


Professional data analysts are no different. We tell ourselves thatdashboards are bad, thatSQL is more useful than machine learning, and thatanalytics is as much about asking questions as it is about answering them. And in recent weeks, a new  shibboleth is taking shape on Analytics Twitter:2Self-serve analytics is a mirage.


Grant Winshipfirst shared this idea, andlotsofotherpeopleagreed.3Never too ashamedto shill for some Klout and likes on Twitter,I joined the pile on.


Most of the arguments, including mine, followed the same arc. Self-serve analytics, which promises to open up vast troves of “insight” by making data accessible to everyone at a company, doesn’t actually work. While self-serve tools make it possible for anyone to extract and visualize data, they don’t imbue their users with the skills required to make sense of data and all its complications. Without those skills, data’s not that useful.


This emerging shibboleth is one of the wise ones; these are all good points. Analysisismore than hard math and a spreadsheet. And collectively, we’ve gotten good at making them. But they raise a rather obvious question that we’re not nearly as good at answering:What do we do instead?The problem self-serve is meant to solve—that there are more questions than analysts, and we don’t have time to answer them all—is still a problem, even if self-serve is a lousy solution. To steal an analogy from yetanother personyou should be following on Twitter instead of reading this Substack, we can stop prescribing ineffective medicine, and the patient will still be sick.


# The manic pixie business user


This predicament reminded me, of course, of Zach Braff.4


For at this moment, we’re all Zach Braffat the end ofGarden State. We thought we knew what to do, realized it was a dumb, awful idea, abandoned it, and now have no plan for what’s next other than to breathily whisper “What do we do?” at our (business) partner asLet Gorises in the background.5


Surprisingly enough, Zach Braff also provides some decent advice. We should start by doing exactly what Zach Braff didn’t do inGarden State—we should treat our partners as more thanshallow characters defined by their relationship with us, but as people with depth, needs, and motivations of their own.


The phrase “self-serve” typically refers to some vague process by which people can answer their own questions to make decisions. But we often aren’t terribly specific about which questions they want to answer, the decisions they want to make, or even who “they” are. Instead, self-serve is often better understood vis-à-vis its relationship with the analyst, not the business user (whateverthatmeans) it's purportedly serving. We’re the protagonist; they’re the nameless stock character.


Because we under-develop who they are, we generalize their motivations, which, in the true spirit of the manic pixie dream girl, become extrapolations of our own. They want to do analysis, just as we do. The challenges we face in our analyses—confounding variables, spurious correlations, outliers, and so on—are the challenges they will face in theirs. And because we have to deal with these things, so too must they.


But what if that’s not actually true? What if our motivations and problems are actually different?


A conversation with a prospective Mode customer started to break this fever for me. The prospect—an analyst on a small data team serving a large company—told me that they were looking for a new self-serve tool to help “people use data in a more meaningful way without having to ask his team for help.”


“The classic self-serve trap,” I thought. “This analyst doesn’t see why this is futile. I need to teach him the handshake, and welcome him to the club.”


Before I had a chance to explain to him why he was chasing a mirage, he continued: His biggest concern was making sure that department leaders have access to consistent reporting. He wanted the business to run on a few critical KPIs, and saw his job as making those metrics available to anyone who needed them.


In telling me this, he inadvertently taught me a lesson much bigger than anything I could teach him. He showed me that my reflexive dismissal of self-serve was wrong because my definition of self-serve was wrong. I assumed he meant one thing; he had done the research to figure out he needed a different thing. He wasn’t looking to enable people to do the rich analysis that we analysts do, nor did he want to solve some generic self-serve problem that he poorly understood; he just wanted to provide an easy way to pull metrics.


Any analyst looking for self-serve solutions—or rejecting them as lost causes—should do the same thing this prospect did, and ask what exactly you mean by self-serve. Who’s going to use it? What do people actually want to do? If we answer these questions, we may find that the problem is easier to solve than we thought.


As I’ve said before, I think most people actually want what the prospect wanted: a tool for metric extraction. “They want to choose from a list of understood KPIs, apply it to a filtered set of records, and aggregate it by a particular dimension. It's analytical Mad Libs—show me average order size for orders that used gift cards by month.” Analysis of this form doesn’t end with a new chart built on top of novel manipulations of data; it begins with extracting a set of well-understood charts, laying them out on a desk, and figuring out the story that emerges from them. This problem is much less vulnerable to the pitfalls we commonly attach to “self-serve.”


This is why I believe ametrics layeris such an important piece of the modern data stack. It wouldn’t just fill a gap in our current toolset, but it would also underpin a workable self-serve solution that’s built for the real people who use it, and not an unworkable one for the characters we imagine who might.


# An alternative ending


Just as we can’t generalize business users as superficial reflections of ourselves, we also can’t characterize all of them as mechanical metric extractors. Sometimes, their questions do call for deeper analysis. In these cases, how do we escape between the rock of having too few analysts to answer these questions, and the hard place of analytical thinking being hard?


Bluntly—hire more analysts.6If you want to build a great brand, you invest in great marketers. If you want to build great technology, you invest in great engineers. And if you want to make great decisions with data, you...buy great self-serve tools? No, you hire great analytical thinkers.


The good news is that self-serve tools make this much easier. There are lots of people—economists, sociologists, political scientists, historians—who are trained to think analytically. The only thing preventing them from being great data analysts is the technical training to extract and manipulate data—which is the exact gap that self-serve tools are meant to close. And, if we hired more people like this, we could closeanother notable gapin our industry.7


Until then, though, our club will remain the same, with the same members, the same problems, and the same punchline—self-serve is a lie—as our password.

[1](https://benn.substack.com/p/self-serve-shibboleth#footnote-anchor-1-37078472)

As I said, not all shibboleths areactually correct.

[2](https://benn.substack.com/p/self-serve-shibboleth#footnote-anchor-2-37078472)

Analytics Twitter is the corner of Twitter that spends a third of its timestaning data tools, a third of  its timearguing about SQL formatting, and a third of its time making data dad jokes (I won’t link this one...but you know who you are). This isn’t to be confused with Data Science Twitter, which is a third A/B testing and causal inference, a third topics that my feeble Analytics Twitter brain can’t understand, and a third Google firing their ethics AI researchers for researching ethics in AI.

[3](https://benn.substack.com/p/self-serve-shibboleth#footnote-anchor-3-37078472)

If you’re interested in whatever this Substack is, follow these people. They’re the source from which I steal all of my good ideas; the Reddit to my Instagram meme account. If you follow them, you’ll get the same substance as you do here, but won’t have to parse through 500 words of weird cultural gloss to get it. Which you’ll have to do again in about three paragraphs.

[4](https://benn.substack.com/p/self-serve-shibboleth#footnote-anchor-4-37078472)

Better to be an angsty millennial than a geriatric millennial.

[5](https://benn.substack.com/p/self-serve-shibboleth#footnote-anchor-5-37078472)

It’s probably time for me to look forother sources of inspiration.

[6](https://benn.substack.com/p/self-serve-shibboleth#footnote-anchor-6-37078472)

Emilie Schario, another person I have to shamelessly steal from to write anything,made this point first.

[7](https://benn.substack.com/p/self-serve-shibboleth#footnote-anchor-7-37078472)

These slides are from anold talkabout hiring more analysts.
