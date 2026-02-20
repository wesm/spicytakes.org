---
title: "What My User Survey Taught Me"
date: 2010-02-07
url: https://www.kalzumeus.com/2010/02/07/what-my-user-survey-taught-me/
slug: what-my-user-survey-taught-me
word_count: 1454
---


Some weeks ago I mentioned that I was [implementing a user survey](https://www.kalzumeus.com/2010/01/17/wufoo-free-incentivization-cheap-effective-user-surveys/) in Bingo Card Creator, using [Wufoo](http://www.wufoo.com).  About forty of my customers have now taken the time to give me detailed advice.  I thought I’d share some things I learned.  A few takeaways may be applicable to your business, and at the very least “detailed, actionable advice can be yours if you just ask for it” should convince you to start a survey this week.


## Incentivize Any Surveys You Do


I ran two A/B tests in taking the survey.  The first selected whether a user was asked to take it at all.  The second tested what prompt was more effective at inducing people to take it.  Half of participants were invited to to take it for altruistic reasons (“Would you like to take a survey about Bingo Card Creator?  We’d like your feedback so that we can improve the website and software for all of our customers.”)  The other half were incentivized (“Would you like to take a survey about Bingo Card Creator?  If you do, we’ll let you print 5 extra free bingo cards.”)


I gave all users who completed the survey the free cards, regardless of whether they had been promised it or not.


I have **never** had a more lopsided A/B test.  The response rate of incentivized users so resoundingly crushed the response rate of non-incentivized users right out of the gate that I was scared of a bug.  It ended up being more than a 2X difference in conversion: 2.51% vs 1.17%, which is significant at 95% confidence.


Thus the conclusion: if you want responses, give away free stuff.  (Incidentally, you might think that you’d get lower quality feedback from incentivized users.  I did not get that impression from reading the results, but I can’t reduce that to a simple statistical measure.)


## Surveys Don’t Cost You Sales


A major worry I had was that putting the survey prominently on the trial version of my application would cost conversions.  Nope — there was no significant difference in sales given to folks asked to take the survey versus folks not asked to take the survey.  (I actually got very, very marginally more sales from the folks asked — but not statistically significant.)


## Opinions Confirmed About My Customers


Prior to instituting the survey I had guessed that my customers were mostly female, older (I was guessing normally distributed around 40), and that they were probably teachers.

1. I was dead on the money on gender.  85% of participants were ladies — this roughly comports with my experience looking at customer names and doing customer support.
2. My customers are, indeed, mostly older: fully half of them are over 40.  Another 30% are in their 30s.  About 10% are in their 20s and a little less than 10% are below that.
3. I now have data to substantiate that most of my users are teachers: 30% of respondents use BCC in elementary schools and another 20% use it in high schools (that number is *much* higher than I would have expected).  I was mildly surprised with the number of people playing with adult family members (~15%).  All other uses are fairly marginal.  Confirming that most of my users are teachers is going to be **very helpful** in crafting my marketing messages.  (Though I suppose I have to worry about stumbling into the local optimum: I might be seeing this because I market to teachers well and market to, e.g., parents poorly.)
4. Two survey takers, as predicted, used the survey free response box to ask customer support questions.  One of them I was able to de-anonimize and fix the issue she had (she had created a new trial account rather than using the old registered account and wondered why it was asking her to purchase).  The other one, sadly, was using an anonymous guest account from an IP I’ve never seen before, so I couldn’t track them to an email address to resolve their issue with the purchase.


## Things I Didn’t Know Prior to Asking

1. A lot of my users are very, very appreciative of Bingo Card Creator.  I mean, I knew it saved them some time and that lots liked it, but I got stories of it saving a lesson plan, brightening the day of a room full of seniors, and teaching a son to read.  A few of the results warrant follow up emails to ask if I can quote them publicly.  (Like, right next to the Buy Now button.)
2. I am terrible at Quality Assurance.  Well, I knew that.  But, specifically, a particular combination of A/B tests would result in a user getting textual instructions on one screen which conflicted with what was written on the buttons on the next screen.  Thank you for the report, ma’am — bug squashed.
3. A few customers reported generalized anxiety about using “new programs” and said they wanted more handholding in the instructions.  I beefed up instructions throughout the application.
4. Surprisingly few of my customers reported problems with ease of use — over 90% rated BCC either “Very easy to use” or “Mostly easy to use”.  I also got a lot of free-form comments praising the daylights out of that — many of my customers compared it favorably to other unpleasantness they had had doing routine computer tasks.
5. Surprisingly many of my customers self-evaluate as comfortable with computers.  50% were “very comfortable”, and 30% were “mostly comfortable”.  These numbers are, candidly speaking, not what I would have assigned on the basis of reading support requests for three years.  It is possible both the survey and I are right, just looking at different segments of reality: 80% of the customers are good with computers and fairly rarely email me, and 80% of my inbox is caused by the remaining 20%.
6. Customers respond very strongly to features I consider so core to the program I scarcely mention them — in particular, I  learned twelve different ways to express the thought “Every card is different!” and another eight for “I love that I can customize the word list for the lessons I am teaching that week”  I will be incorporating additional variations of those into my copy.  Repetition never hurt any teacher.


## The Number One Complaint My Users Have


**Bingo Card Creator isn’t free**.  Some variations on the theme:


**Make it totally free by having advertisers.** Many, many sites that elementary teachers use are kept free by the magic of Google AdWords.  I should know — **I’m the guy paying for the ads**.  While you can keep the free bubble going by passing around VC dollars to Internet firms to Google to Internet firms to Google to Internet firms to Google to … for a while, eventually, if you’re not getting money from customers, everyone dies.  This was, essentially, the last Internet bubble.  I will continue charging because charging keeps the rest of the ecosystem alive.


Relatedly, the fact that Bingo Card Creator is so easy to use is directly related to the fact that I charge money for it.  I obsess over getting customers (or trial users) through the pages to their beautiful bingo cards, because people who see beautiful bingo cards are very inclined to pay me money.  The sites that I advertise on do not optimize for their user experience because **if their website is better than my textual ad, they don’t get paid**.  That is why the experience of using them sucks.  (I won’t out anybody who I essentially have a business relationship with, but take a look at the free options in my market some time, or look at pages which compete with mine in the search results.)


Charging also subsidizes the experience of the 97.3% of trial users who don’t actually pay me money.


“**15 card limit does not allow for a class set in which everyone can have a different card 25 would be more appropriate for teachers**.”  I regularly get asked what my business model is — i.e. how I convince people to pay money for my software when I give so much away for free.  This lady nailed it in one sentence.


Incidentally, I don’t feel any ranchor at folks who believe that everything should be free on the Internet.  I just will not accomodate your preferences.  You’re welcome to use my free competitors if they better fit your needs.  (I actually provide folks  with lists, on request.)


## Takeaway Lesson


What are you waiting for, go sign up for Wufoo (or whatever — they have a few competitors) and do a survey.  You’ll learn stuff that you can use to make helpful decisions for your business.
