---
title: "And we're feature complete"
date: 2006-06-28
url: https://www.kalzumeus.com/2006/06/28/and-were-feature-complete/
slug: and-were-feature-complete
word_count: 701
---


Finishing up the tweaking on printing took 6.5 hours, about what I expected.  Much of it was banging my head into the wall — I’ve got a particular sample data set which I want to provide to my customers as a “freebie” with the full version of the software.  Its the sort of thing I hope will motivate someone to buy my product, as none of my competitors have it and its off-the-shelf ready to make you a lesson plan and save you hours of work.  The problem is this particular data set excercizes an edge case: but what if someone includes a really, really long word in a place we’ve sized for words of more moderate length(say, 10 characters).


What if indeed.  The answer depends on what flavor of JComponent you are using to display the word, what container that component is in, what the layout manager of that container is, what your locale is, and a whole host of factors.  In the typical case most JComponents, including JLabel and JText area (the obvious choices for formatable text), will truncate the word.  And they will unfortunately do it without firing any special notifications or causing getText() to return a different value than the one you originally provided it.  The first chance you’ll have to notice “Hey, that looks funny” is when the word appears on the screen like “Java decided to tr…” (“Java decided to truncate me!), or worse, when that appears in your print output.  Luckily, I have a virtual printer which outputs to PDF, so I saved myself wasting ~50 reams of paper fixing this sucker.


In case anyone is searching the Internet looking how to fix **JLabels with chopped off text**, here’s the best I came up with:  first, identify the Container one level above your component that is experiencing truncation.  Then, change that component’s LayoutManager to be a custom subclass of whatever you were doing before.  Override the layoutContainer method to both call super and do the following:


Check to see if your component which can have problems is having problems by calling its getFontMetric() method, and use FontMetric.getWidth(insert correct text here) to figure out how many pixels that takes to display.  If thats less than the width of your component (include a fudge factor or you’ll see some pixels get chopped off on occasion), you need to change the font on that component to one of a smaller size.  How you do that is up to you, but I used a while loop with a safety cutout at 6pt because otherwise you will get an **infinite loop** on the next step for extremely large strings.  After you’ve set the font to the new smaller font you need to call your super.layoutContainer method again, or else you may not see any changes.  I chose 6 pts arbitrarily because I thought anything smaller than that would be totally useless and I needed *some* safety value.


This was pure pain to have to discover but I think its worth the price of admission for this week by itself.  I got a tour of a section of Swing that I never had dealt with before (LayoutManagers under the hood), and got a coding gem out of the deal which I can reuse again later *and* which solves a vexing problem in my line of work (localizing Japanese to English and English to Japanese makes for some very fun times with anything that relies on any assumptions about physical width of strings, let me tell you!)


Anyhow, the upshot is, fixing two little edge cases in one little data set in a freebie I’m giving to customers took me four hours.  Was this productive use of my time, given that I could have achieved the same effect just by not including that data set and hoping customers didn’t notice on their own?  I think it was — while its entirely likely that many prospects will never see the edge cases during their time with the demo unless they use input I supply, this adds a bit of spit-and-polish my competitors in many cases lack *and* allows me to make use of more “freebies” than I would be able to otherwise.
