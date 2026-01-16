---
title: "The hunt for the Holy Grail"
subtitle: "We always talk about single points of failure. But what is our single point of success?"
date: 2023-08-11T16:14:02+00:00
url: https://benn.substack.com/p/the-hunt-for-the-holy-grail
slug: the-hunt-for-the-holy-grail
word_count: 2500
---


![Ooh, Jay-Z Just Premiered His Video for "Holy Grail" (Bonus: Justin  Timberlake Is Super Hot in It) | Glamour](https://substackcdn.com/image/fetch/$s_!-LAg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42b02be6-bd28-4c59-a4e3-ef362b4296f3_1500x1071.jpeg)


The rock floats, butfor the wrong reasons.


Bummer, I guess. We really could've used that rock,for Antarctica, andfor supersonic trains,1for laptops that don’t melt the lacquer off of a dining room table when you have more than six tabs open in Chrome, and for all the VCs that now have to roll their material sciencesnéegenerative AInéecrypto fundback into a generative AIfund, until that goes bust too and we’re allselling adsagain. RIP, LK-99—atsixteen days, we believed in you for a half-Scaramuccilonger than we believed in Anthony Scaramucci.


Still, while it doesn’t look like we’re going to some magical piece of metal that solves all of our problems out of this fuss, I got at least one thing from it: The knowledge that some magical piece of metalcouldsolve all of our problems. Three weeks ago, I was vaguely aware of what a superconductor was, but didn’t realize that, one, they don’t really exist in everyday life, and, two, if they did, lots of problems would almost instantly vanish. To me, electrical resistance was an abstract and distant coefficient that last mattered in high school science class.2Apparently, however, the entire world is built on the assumption that that coefficient isn’t zero. Change that assumption, andeverything changes.


More generally, the LK-99 drama reminded me that big and messy problems don’t always require big and complicated solutions. Sometimes, they can be solved in one swing, or by breaking one foundational assumption (or, like, one physical law of the universe). Even if actually doing that is impossible, it seems interesting—and maybe instructive?—to know which limitations are at the root of all of our ills.


As a prisoner to the ills of the data industry, this made me wonder if there was a single solution to the things that we struggle with. Is there some Holy Grail—some single point ofsuccess, on which ourtower ofproblemsare built—that, if discovered, would launch us into an analytical paradise of clean data, universal access, and instant insights?3If we could have one miracle materialize out atwenty-year soap opera, what would it be?


# Stacking cache


Instant data processing. I think that having to process data in steps, in batch, is our electrical resistance. It's the cause of nearly all of our problems, and if we could run a computational data pipeline instantly, on demand, from source to final destination, we’d have our utopia.


Everyone already knows this, but very roughly, here’s how we do things with data. Data gets created across thousands of different sources. We extract (or stream) that data from its source and put it somewhere that we can manipulate it more directly—usually a database, but sometimes Excel, or a domain-specific analytical tool. Then, that copy of the source data gets processed through a bunch of intermediate steps—transformed into tables in a warehouse, automatically aggregated into new Parquet files, manually copied into other Excel worksheets, whatever. And somewhere along the way, peopledo somethingwith some of those copies, like query a database to make a chart, or use a table to send an automated marketing email, or export an Excel file to write a financial report to file for the SEC.


It’s tempting, and not entirely wrong, to think of this like a software application. There are data sources; there are models that describe those data sources; there are layers of logic that control what’s done with the data in those sources; there are views of the data that come out of control layers. The analogy with software engineering isright there.


Lots of people noticed this. They also noticed that software, considering the enormity of what it’s asked to do, works remarkably well. Emails get delivered; planes stay in the air; I have complete confidence that the words I type into a Google Doc won’t vanish or mysteriously change themselves when I’m not looking. So over the years, and especially so over the last decade, data people looked at all of this and did the obvious thing: We tried to do our jobs the way software engineers do theirs, so we could build things that work as well as what they've built.


We write more code. We version control that code, and have other people review it when we want to change it.We define APIs and do integration testing.We monitor our work with observability software. We talk about the need foropen-source libraries. We havepetty fights about stupid things.


But…it hasn’t really worked? Things are better, no doubt, but lots of things are still broken. We’re still stumbling over messy and disorganized data; we can’t get dashboards to match; people still worry about stuffchanging without warning. The most popular feature in every data tool is “Export to CSV,” in part because Excel files—static, manually audited, saved on a computer, and guaranteed not to change on their own—are still the only thing people trust without hesitation. Imagine if people trusted Slack this much: “Yes of course, we love it. But if the message is important, we save it as Word doc and email our reply to people, just in case.”


Lots of people have noticed this too, and our collective response has generally been to double down4on engineering principles. Addunit testing!CI/CD bots!Virtual environments, and something apparentlybetter than virtual environments! Eventually, if data teams copy enough from software teams, this stuff will get sorted out.


To the extent that I understand what these things are, sure, they sound useful enough, I guess. But for us to be able to work like engineers—and, more importantly, build things that are as reliable as what engineers can build—I think we need to solve a more fundamental problem. In software development, logical pipelines are processed at once. In data development, people are working off of an infinitely splintering collection of caches.


Consider a basic web application, or some other relatively straightforward piece of software. When you load a web page, a bunch of nested logical calculations are executed, and ultimately determine what you see on your screen. That web of computation is probably much more complicated than most data pipelines—but it all happens at once.If you see a bug, you know that bug happened live. If you update the code to fix the bug, you can rerun the entire program almost instantly, and see if the bug got fixed. You don’t have to worry about fixing bugs across a bunch of different states; everything is always live.


Unless, of course, it’s not, and your program caches data. A lot of applications use caches—and managing them is one of thehardest problemsinsoftware engineering. Though I’m not an engineer, “be mindful of how you use caches” seems like reasonable advice.5


Contrast this with the sketch of how we work with data. The entire job is practically cache management. The source data—a cache. The data that’s been extracted and loaded into the warehouse—another cache. Every intermediate materialization—more caches. CSVs exports and Excel workbooks and files loaded into Python notebooks—also caches. Emailed screenshots of a dashboard that are used by a financial analyst to put together a PowerPoint presentation—kind of a cache, manually transcribed into something else that’s also kind of a cache.


Two weeks ago—in yet another example of doubling down on how we could be more like engineers—I saidthat dbt models are “akin to functions in a piece of software.” To twist that analogy a bit further, imagine if every time you ran a function, it didn’t actually execute the functions nested inside of it; it just took the result from the last time that function ran. This would be basically impossible to work with?6And yet, it’s exactly how much most data infrastructure works today.


No wonder nothing ever makes sense. Every number or chart we see is a cache on a cache on a cache. How many?We have no earthly idea. We just stack it up, and try to keep it DRY.


Of course, we don’t do this because we want to; we do it because we have to. Processing data is expensive and slow; some marketing funnel visualization that sits on top of Stripe data, and Salesforce data, and a stream of a billion events can’t update everything, end-to-end, every time a marketer loads a dashboard.


But what if it could? What if that coefficient was zero, and every pipeline and dashboard could be updated in an instant?


# Fantasyland


It’s hard to overstate how much easier that would make our lives. Think about what happens today when something goes wrong, like a finance report shows a suspicious number. First, teams have to back through a series of caches to figure out where that number came from (caches that may have since updated). Once they find the offending problem, they fix it—but often, not by reviewing if the report itself is fixed, since that would often take too long to fully refresh. They instead just verify that the intermediate step—the source data, ingestion job, the semantic model, whatever—that caused the problem is fixed. And they certainly can’t test, or even spot check, every other report that’s dependent on that piece of the application.


Moreover, even if the problem gets fixed, the original problem could persist. If a result got exported to Excel—i.e., bad data was written to a long-lasting cache—it can be next to impossible to track down, much less fix. Though all software has tech debt, data debt has a unique permanence to it that makes it especially pernicious.


If everything could be updated immediately, most of these problems would go away. To investigate a suspicious number in a dashboard, data teams could investigate code across the stack, change any of it, and instantly see how it affectedeverydashboard. They could debug the problem alongside the business partner, like an engineer working with a designer, where the stakeholder could test the impact of every change. They could update source data and see everything change right away. They could fix the problem and know that it’s fixed everywhere. Problems would no longer be permanent, but corrected by “refreshing the page and seeing if that resolves it.”


To frame this in a different way, think about the internal reporting tools inside of SaaS products likeHubSpotandWorkday. They’re limited in what they can do, but they’re far easier to manage and debug than a modular data stack. That’s partly because they have a narrow scope—but I’d argue it’s more because the reports are always live, with no cache between the source data and the eventual dashboard. Update anything, and you update everything.7


# But, like,why?


But, of course, the rock isn’t real. We don’t have quantum computers that can process data instantly. We have MacBooks, that melt the lacquer off of dining room tables when you open six Chrome tabs. So what’s the point of talking about some hypothetical Holy Grail before an arXiv preprint pops out of a lab?


My first answer8is that if we know that a room-temperature superconductor solves all of our problems, could analmost-superconductor solvemostof them?


For example, morestreaming systemsmight help. Streaming isn’t quite the same thing—it wouldn’t really help you if you fixed an issue that needed to be backfilled—but it could get us closer. Data teams could also be more judicious in exactly where they introduce “caches” and where they try to avoid them. There are some places where they make sense, and some places where they don’t. ELT and its variants have made us relatively lazy about this; there’s probably a lot of low-hanging fruit that could be picked off.9


My second answer is that, perhaps, until we have our superconductor, we can’t actually work like engineers. If engineers still had to do things with punch cards, or had to build everything in assembly language, they probably couldn’t work like modern data engineers either. Similarly, if the bulk of what we have to do—cache management—is the thing that engineers try to avoid doing, we might not want to model our tools and technologies after theirs.


That’s not to say there aren’t lessons to be learned from engineers—I don’t think we make anything better by going back to a world of ping-ponging Excel files back and forth. But we also have to acknowledge that the problems we have to solve have different physical constraints than the ones engineers are trying to solve. Until, of course, the rock floats.

[1](https://benn.substack.com/p/the-hunt-for-the-holy-grail#footnote-anchor-1-135936123)

Copyright2023?So we’re still pretending this is real? (Also, haha,X, lol)

[2](https://benn.substack.com/p/the-hunt-for-the-holy-grail#footnote-anchor-2-135936123)

This tells you how much I know about physics: The last time I learned about it was inscienceclass.

[3](https://benn.substack.com/p/the-hunt-for-the-holy-grail#footnote-anchor-3-135936123)

If I die and I wake up in a world where everyone is excited about clean data and instant “insights,” I’ll know I’m not in heaven; I’m in theGood Place.

[4](https://benn.substack.com/p/the-hunt-for-the-holy-grail#footnote-anchor-4-135936123)

Me, an idiot, in 2013: Hm, yes, I live in San Francisco, the world needs another tech startup to build some software, I will do that.


You, a true American hero: What if, instead of a tech company, we start a bakery. And that bakery will sell muffins. And when you buy a muffin, you can wager it on a coin flip. Lose, and lose your muffin. Win, and get two muffins.And then, you can then wagerthosemuffins, on another coin flip, and win four muffins? And again, for eight? And sixteen? And on and on forever, until we either reverse-Martingaleevery dollar out of San Francisco, or someone wins 131,072 muffins and we go bankrupt? And what if we call the bakeryDouble or Muffin?


(When I first moved to SF, I met someone who knew Double or Muffin's founders. Their website says that you could only wager your first muffin, and you got to keep it even if you lost. However, I was told at the time that you actually had to gamble your muffin, that you could double or muffin as many times as you want, and that the biggest ever winner won 32 muffins. I don’t know which version is true anymore, but I choose to believe the story I was told because it is  incredible.)

[5](https://benn.substack.com/p/the-hunt-for-the-holy-grail#footnote-anchor-5-135936123)

Is it? Is this actually how any of this works? Do I even know what a cache is? I mean, honestly, not really. But I’m gonna run with it until someone tells me it’s wrong.

[6](https://benn.substack.com/p/the-hunt-for-the-holy-grail#footnote-anchor-6-135936123)

This is basically whyJoel Grus famously hates notebooks.

[7](https://benn.substack.com/p/the-hunt-for-the-holy-grail#footnote-anchor-7-135936123)

I’ve made the case anumberoftimesthat a consolidated modern data stack may be better than a modular one. Add this reason to thestrength box. (Or does it go in the opportunity one? I dunno man. The closest I ever came to being a consultant was in October of 2008, when I got a job offer from some mid-tier firm in DC, and they fired me in November before I’d even accepted the offer.Wild time,2008.)

[8](https://benn.substack.com/p/the-hunt-for-the-holy-grail#footnote-anchor-8-135936123)

Well, actually, the first answer is that there isnopointtoanyofthis.We all just entertainers, and I’m just here to entertain myself and tokeep linkingtoGriff bangersuntil she releases the song already.

[9](https://benn.substack.com/p/the-hunt-for-the-holy-grail#footnote-anchor-9-135936123)

“We’ve been saying this for years,” some will say. “IATJK,” I will say.
