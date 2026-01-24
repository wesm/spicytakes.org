---
title: "COBOL: Everywhere and Nowhere"
date: 2009-08-09
url: https://blog.codinghorror.com/cobol-everywhere-and-nowhere/
slug: cobol-everywhere-and-nowhere
word_count: 763
---

I’d like to talk to you about [ducts](https://blog.codinghorror.com/mousing-surface-theory/). Wait a minute. Strike that. I meant [COBOL](http://en.wikipedia.org/wiki/COBOL). The Common Business Oriented Language is celebrating its fiftieth anniversary as the language that is [everywhere and nowhere at once](https://web.archive.org/web/20090918144712/http://advice.cio.com/stephen_kelly_micro_focus/cobol_still_doing_the_business):


> As a result, today COBOL is everywhere, yet is largely unheard of among the millions of people who interact with it on a daily basis. Its reach is so pervasive that it is almost unthinkable that the average person could go a day without it. Whether using an ATM, stopping at traffic lights or purchasing a product online, the vast majority of us will use COBOL in one form or another as part of our daily existence.
> The statistics that surround COBOL attest to its huge influence upon the business world. **There are over 220 billion lines of COBOL in existence, a figure which equates to around 80% of the world’s actively used code.** There are estimated to be over a million COBOL programmers in the world today. Most impressive perhaps, is that 200 times as many COBOL transactions take place each day than Google searches - a figure which puts the influence of Web 2.0 into stark perspective.
> Every year, COBOL systems are responsible for transporting up to 72,000 shipping containers, caring for 60 million patients, processing 80% of point-of-sales transactions and connecting 500 million mobile phone users. COBOL manages our train timetables, air traffic control systems, holiday bookings and supermarket stock controls. And the list could go on.


I have a hard time reconciling this data point with the fact that I have never, in my entire so-called “professional” programming career, met *anyone* who was actively writing COBOL code. That probably says more about my isolation as a programmer than anything else, but still. I find the whole situation a bit perplexing. **If these 220 billion lines of COBOL code are truly running out there somewhere, where are all the COBOL programmers?** Did they write software systems so perfect, so bug-free, that all these billions of lines of code are somehow maintaining themselves without the need for legions and armies of COBOL programmers, decades later?


If so, that’s a mighty impressive feat.


And if COBOL is so pervasive, why is it number one in this list of [dead (or dying) computer skills](https://web.archive.org/web/20090813083156/http://www.computerworld.com/s/article/9020942/The_top_10_dead_or_dying_computer_skills?source=rss_news50) compiled in 2007?


> Y2k was like a second gold rush for Cobol programmers who were seeing dwindling need for their skills. But six-and-a-half years later, there’s no savior in sight for this fading language. At the same time, while there’s little curriculum coverage anymore at universities teaching computer science, “when you talk to practitioners, they’ll say there are applications in thousands of organizations that have to be maintained,” says Heikki Topi, chair of computer information services at Bentley College in Waltham, Mass., and a member of the education board for the Association for Computing Machinery.


When you dig in and read about some of these [real world COBOL systems](https://web.archive.org/web/20090814165742/http://www.computerworld.com/s/article/266228/Cobol_Coders_Going_Going_Gone_?taxonomyId=10&pageNumber=1), you can get a glimpse of the sort of difficulties they’re facing.


> Read says Columbia Insurance’s policy management and claims processing software is 20 years old and has 1 million lines of COBOL code with some 3,000 modifications layered on over the years. “Despite everyone pronouncing Cobol dead for a couple of decades, it’s still around,” he says. “We continue to enhance the base system. It’s still green-screen, if you can believe that.”
> Read says getting younger workers to take on Cobol chores is a “real challenge, because that’s not where technology is today.” He simply tells them they must do some Cobol work, promising a switch to other things at the earliest opportunity.


Remember how the common language runtime of .NET promised rich support for a plethora of different languages – but none of that ever mattered because everyone pretty much [just uses C# anyway?](https://blog.codinghorror.com/the-slow-brain-death-of-vb-net/) Well, that CLR didn’t go to waste, because it *is* possible to write code in COBOL.NET.


[See for yourself](http://www.c-sharpcorner.com/UploadFile/rickmalek/dialconv12052005002746AM/dialconv.aspx).

kg-card-begin: html

```

private void button1_Click(object sender, System.EventArgs e)
{
button1.Text = “Call COBOL”;
}

```

kg-card-end: html

That was C#, of course. Here’s the COBOL.NET version of same:

kg-card-begin: html

```

METHOD-ID. button1_Click PRIVATE.
DATA DIVISION.
LINKAGE SECTION.
01 sender OBJECT REFERENCE CLASS-OBJECT.
01 e OBJECT REFERENCE CLASS-EVENTARGS.
PROCEDURE DIVISION USING BY VALUE sender e.
SET PROP-TEXT OF button1 TO “Call COBOL”.
END METHOD button1_Click.

```

kg-card-end: html

Is there anything I could write here that the above code doesn’t make abundantly clear?


COBOL: so vibrantly alive, yet... **so very, *very* dead**.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[cobol](https://blog.codinghorror.com/tag/cobol/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[legacy systems](https://blog.codinghorror.com/tag/legacy-systems/)
