---
title: "Quantifying The Value Of A College Degree (By Major)"
date: 2011-01-05
url: https://www.kalzumeus.com/2011/01/05/quantifying-the-value-of-a-college-degree-by-major/
slug: quantifying-the-value-of-a-college-degree-by-major
word_count: 1891
---


“Your single best investment is your own education.” “The average new graduate is drowning in $22,000 in debt.” “A degree in English is just as valuable as a degree in Biology — it teaches you critical thinking!” “Follow your dreams and you’ll find financial success whatever your major is!”


You’ve probably heard a thousand pieces of educational/career advice like these, and if your family/friends/advisors are anything like mine they’ve virtually never been substantiated by data.  That is a shame, because choosing a course of study is one of the largest transactions you’ll ever make — the sticker price at my alma mater was close to $140,000 and prices nationwide have risen faster than inflation for virtually a generation now.  We have the Blue Book to tell you what a ten year old beater is worth down to the dollar, there are entire industries devoted to assessing every type of security to determine their valuation, and the closest thing most students have to insight on the degree selection process is getting advice from Aunt Sue.  **This is insane**.


## Information Asymmetry In Employment Outcomes


Any college could rectify this situation virtually overnight: take that lovely list of alumni that they obsessively curate for squeezing donations, send out a two question survey (“What did you major in?” and “What was your salary this year?”), and give a sociology grad student a bowl of ramen to do some very simple number crunching.  **No college will actually do this** because transparency goes directly against their interests: if all degrees from a particular institution are valued at “An uncertain, but certainly large and roughly constant number”, then the standard practice of pricing them all identically makes sense.  If not, it is the academic equivalent of pricing stocks by length of ticker symbol.


(I understand many folks enjoy the non-economic component of their education.  I did and do, too, but since I’ve never spent $120,000 and signed myself up for a decade of debt for the sheer enrichment offered by attending a ballet or reading about the Japanese economy I can only conclude that I don’t value it anywhere near what I paid for my degrees.  Your objection to the narrowness of this study is duly noted, though.)


You might assume that the government would track this, somewhere, but you’d be wrong.  The Census Bureau produces a report every ten years tying level of education (associate’s degree, bachelor’s degree, master’s degree, etc) to salary, which invariably produces the result “More education is better”, but they don’t answer very interesting questions like “Is a bachelor’s degree in computer science better than a master’s in elementary education?” or “Are there fields with a sharply diminishing return to additional education?”


However, the Bureau of Labor Statistics does very comprehensive work in administering a National Compensation Survey, which gathers huge amounts of raw data about employment hours and wages broken down by region, job (over 800 classifications available, from CEOs to ship loaders), and a few other axes.  They use this and other studies to produce a variety of government reports, such as the <a href=”http://www.bls.gov/ooh/”);”>Occupational Outlook Handbook</a>, which does a good job of providing per-career advice but probably intentionally omits comparisons between careers.


The Bureau of Labor Statistics also makes the data from the NCS available for download on their website.  It is hefty — over a gigabyte of plain text — but it contains a virtual treasure trove of value… if you just know how to read the map.


## Liberating Conclusions From Open Data


Recently, a big buzzword in the tech community has been Open Data: the notion that the huge, monstrous streams of raw facts collected by the government can be exploited for our benefit if they are merely shared.  I think this is *mostly* true: the best single example I’ve heard of is that since your local health authorities inspect every restaurant’s premises as a matter of course they must know where they all are located, and therefore one should be able to get those locations from them and jumpstart the creation of a guide to local restaurants without having to find every one by yourself (a monumental undertaking).


However, raw facts are uninteresting.  Here’s a line from the BLS data:


NWU009910010200000000000016260,2008,M07,69.71


Scintillating stuff, right?  What we are really interested in is what those facts can teach us — in particular, what can they teach us that allows us to make decisions such as what to major in.  This is where your friendly neighborhood computer programmer comes in: with a bit of elbow grease and a laptop, you can reduce the 856,000-odd facts in the government’s salary data to some useful conclusions about college majors.


## A Bit Of Science And A Dash of Art


Sadly, there are limitations to what we can accomplish with the BLS data: it groups salary data by occupation rather than by major and degree level.  The BLS separately identifies for each occupation what the probable degree level is, but going from occupation to degree requires a bit of guesswork.  Rather than associating all occupations with sets of related degrees by hand, and injecting my own biases into the analysis, I decided to crowd source the problem: I paid Mechanical Turk workers for their two cents (quite literally) on what degree an e.g. elementary school teacher likely had.  This produced answers like Education, Early Childhood Education, Teaching, English, etc.


I then used an arbitrary level of consensus as a cutoff, and was able to pair ~60 very popular degrees (Computer Science, English, etc) and ~250 less common ones (Vocational Education, Media Technology, etc) with associated occupations.  Some additional number crunching let me construct rough estimate salary-versus-age curves for the occupations, which could then be reduced into a simple net present value calculation.  Long story short: a lot of data, a bit of science, and a dollop of absolute voodoo — it’s sort of like most social science, except I’m going to be honest about the voodoo upfront.


After doing the calculations I used Ruby on Rails and some open source graphing libraries to present the results in a comprehensible, searchable fashion — similar to the data visualizations done by the New York Times, which are some of the best work they produce.  (Check this one on the [geography of the recession](http://www.nytimes.com/interactive/2009/03/03/us/20090303_LEONHARDT.html) for the general feel.)


## Why Go To All This Trouble?


Short story: Intellectual interest plus a nice paycheck.


Longer story: I do very occasional consulting work for a variety of clients.  In case you haven’t noticed from the six-figure sticker prices, offering degrees is a *very big business*.  Any flowing river of cash that large attracts, as if by magic, a variety of service providers around it.  In education, one major problem colleges have is finding prospective customers to sell degrees to.  This is hardly a unique problem for businesses.  (Colleges may prefer to phrase this as “students” to “award” degrees to, because they are intellectually committed to a view of themselves as custodians of the lamp of human knowledge rather than rapacious money-grubbing institutions.  I don’t know of any reason they can’t be both.)


One thing colleges — from the Ivies to state schools to online for-profit institutions — spend absolutely gobsmacking amounts of money on is “lead generation”.  Basically, since a percentage of applicants will eventually matriculate (and pay five or six figures for the privilege), when a qualified prospect fills out an application that is an economically beneficial event.  You can compare this to a conversion to the free trial of a web service.  Universities are willing to pay quite a bit of money if you can induce someone to apply: the payout varies by university and agreement, but payments in the $10+ region just for requesting an application packet are not uncommon.  (And if you had some magic way of generating sought after candidates — say, highly qualified African American students — you could almost certainly negotiate much, much higher payouts.  There might still be some Marxists on the faculty but it is all capitalists in the administrations.)


Anyhow, with universities offering to pay for lead generation, there is an entire value chain created from the ether: sites to capture the leads, affiliate programs to direct folks to the lead capture sites, advertising to attract visitors to the affiliates, publishers to create content which displays advertising, etc.  One of the publishers in the industry, Online Degrees, hired me with an open brief: make something compelling for our website.  I thought since universities, academics, and the government have failed to produce any actionable data on which degrees make sense to go after, I could do some independent research on the subject.  Online Degrees.org will host it on their website, and in the course of providing value to potential students researching the subject, they’ll have an opportunity to display ads for degree programs.


You might be concerned about the impartiality of this.  I don’t blame you.  I’ve got no particular dog in this fight: I get paid by the hour no matter what degree wins.  (Cards on the table: I have degrees in Computer Science — which is in the data set — and East Asian Studies, which is not.)


Online Degrees.org obviously has a vested interest in convincing you that a having a degree is better than not having one, but they’re agnostic about which one you apply for.  Indeed, they’d love to tell you which fields are better than others because somebody in the industry needs to have the credibility to say that e.g. culinary school is tantamount to grand theft (and most of the victims take out loans for the privilege of going through it).


Besides, do you really have a better alternative?  If I had a PhD in Sociology, would that make me a less biased source of information on the desirability of becoming a cheap source of exploitable labor a master’s candidate in Sociology?


Anyhow, I have been intellectually interested in this subject for several years now.


## Quick Overview Of Results


For the results of most particular interest to you, take a gander at the degree value calculator.


Regular readers of this blog are mostly technologists of one flavor or another, and **degrees in technical majors do very, very well**.  Computer Science and Computer Engineering are near the top among all options for bachelor’s degrees.  It is narrowly bested by a handful of degrees tailored around resource extraction: for example, if you study Geology, Big Oil will apparently pay you Big Bucks.


Hard sciences such as Physics and Biology pay rather less well than I would have expected.  Degrees in the humanities perform about as poorly as people often joke.  The largest surprise to me was that degrees, even advanced degrees, in some caring professions (like Social Work) are apparently terrible options.  Looking at the underlying data suggests that this because many social workers do it as a part time job.  (That is a recurring theme among many jobs that I expect people would classify as more likely to be female than the typical occupation.  Food for thought the next time someone brings up the [wage gap](http://www.onlinedegrees.org/calculator/salary/gender-wage-gap).)


You can see the results of this research on their website.  [Edit as of 2/19/2013: You’ll have to search for this directly, due to link rot.]


Questions?  Comments?  Criticisms?  I’d love to hear them.
