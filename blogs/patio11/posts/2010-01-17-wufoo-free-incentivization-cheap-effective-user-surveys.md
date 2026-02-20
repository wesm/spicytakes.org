---
title: "Wufoo + Free Incentivization = Cheap, Effective User Surveys"
date: 2010-01-17
url: https://www.kalzumeus.com/2010/01/17/wufoo-free-incentivization-cheap-effective-user-surveys/
slug: wufoo-free-incentivization-cheap-effective-user-surveys
word_count: 2594
---


The prototypical customer of [Bingo Card Creator](http://www.bingocardcreator.com) is a woman between the ages of 30 to 50 who plays bingo with her classroom. I like to think of her as Martha.  However, unlike most statements I make here about my business, this is far **more a guess than it is a fact substantiated by data**.


I can substantiate, for example, that in excess of 90% of BCC customers are female.  (A quick Ruby script checking names on credit cards against a dictionary of common American names reports 90%+ are female.)


They generally *seem* to be on the older side, too.  Sidenote: If you grew up in America you probably have the accurate impression that someone named Ethyl is likely not 18 years old.  You might not know that most names go through ups and downs in popularity.  I’m going to bet that over a few thousand customers I can probably reconstruct the average age just by inspection of first names, but that is an experiment for another day.  The US  Social Security Administration will give you [name popularity data](http://www.socialsecurity.gov/OACT/babynames/), by the by.


However, the bit about Martha being a schoolteacher?  Yeah, that is just a guess.  An educated guess, but still a guess.


## Why Not Knowing These Things Matters


Prior to releasing Bingo Card Creator the core customer I had in mind was an elementary schoolteacher, and the software and site was built with that assumption.  I wrote my copy so that I would sound like a sympathetic colleague (as opposed to, say, a twenty-something WoW raid leader, or a Japanese salaryman, either of which would have been equally as true).  I concentrated the lion’s share of my content creation on the needs of schoolteachers.  I even picked designs for the website and software that looked like something a schoolteacher would like, as opposed to the “That button doesn’t have a glossy finish, reflection, and drop shadow yet, but we’ll fix that!” Web 2.0 aesthetic that I prefer.


Roughly contemporaneous with launch I changed a bit of the copy to address both parents and teachers, but parents were a nice bonus audience I could satisfy with the free trial (and get links from) while trying to separate teachers from their money.


That was my customer hypothesis, to use a buzzword much remarked on lately, and 3.5 years later I’m still not really sure if it is accurate.  On the one hand, I have received email from many, many teachers.  On the other hand, sometimes I get empirical evidence that I’ve been myopic: for example, I put [Baby Shower bingo](http://www.bingocardcreator.com/bingo-cards/parties-and-events/baby-shower) on the back burner for *years* before realizing that the top 25 words used by customers were *all* baby related.


So should I be making a massive overhaul to my copy to target a wider audience than teachers?  Or should I mostly keep doing what I’m doing?  Well, time to supplement my intuition and non-representative guesstimate based on support requests: I need to run a survey.


## HTML Forms: Not Quite As Bad As Visiting An Ill-Tempered Nazi Dentist


I generally work from the hard parts first, and the hard part of doing a customer survey is:

- figuring out what questions to ask
- getting customers to actually take it
- analyzing results
- writing HTML forms.


I am very, very bad at writing HTML forms.  The input markup I can handle, but making them not look insanely ugly takes me literally days.  (Visual design is not my baliwick and what little talent I have for it gets vaporized when it meets the harsh reality of CSS.)  However, I don’t want to have to book my designer for a day just to get a few multiple choice questions coded up.


Enter [Wufoo](http://www.wufoo.com), one of my favorite SaaS providers.  They do one thing really, really well: create web forms for people who would otherwise need to pay somebody with an expensive degree to do it.  I have a Wufoo account lying around since I bought it for my younger brother, who wanted to survey readers of his [superhero writing blog](http://www.superheronation.com) (my family loves niche subjects, what can I say).


It only took me about half an hour to mock up a quick survey.


## What I Asked


Since users get less likely to complete forms with length, I kept it fairly short:

- Gender  (I’m pretty sure I know the answer to this one, but if half my *users* are men and 90% of my *customers* are women that would be a very important thing to know.)
- Age  (<20, 20 ~ 29, …, 60+)  (Here I’m much less certain.  Normally distributed with an average of 40ish, maybe?)
- Who they expect to play bingo with  (“My children”, “My (adult) family”, “My coworkers”, “My class (elementary)”, etc etc)
- Whether they feel “comfortable with computers”  (For years I have presumed that the answer to this is a resounding “no”, and it drives development choices.  For example, I can’t offer picture bingo — my #1 requested feature — if users cannot routinely succeed with finding an image file on their machine and cropping it.  If most users report facility with computers, I might consider moving picture bingo off the “To be implemented after Chinese democracy” list.)
- Whether they find BCC easy to use or not (I prefer data on task success to subjective sentiment, but I can’t afford to ignore sentiment if the sentiment is negative.)
- “What is your favorite thing about BCC?”  (Free response.  I figure it might tell me something I don’t know, and probably will elicit testimonial-worthy quotes.)
- “How can we make BCC better?”  (A nice open-ended way to get users to complain without making them feel like they are complaining.)


## Clever Survey Integration


There are a couple of ways to ask people to take a survey.

- Put a discrete link on your site that no one will click.
- Use a pop-up window, because you spend entirely too much on bandwidth and need to drive some users away.
- Email your mailing list, offering an interruption that doesn’t improve their day.


I wanted to do something a bit trickier: integrate the survey intelligently into my site, such that users would *want* to take it.

- Offer users a freebie just for taking the survey.
- Let users dismiss the message if they want to.
- Stop bothering users after they take it.
- A/B test the effects of the survey on sales.
- A/B test the effects of the freebie on survey taking.


**A note on incentivizing users**: Programmers live in a world where data is available in infinite abundance, and hence we often assume that data is valueless.  (If you doubt this, try asking a programmer for opinions on software pricing.  Yes, I am talking to you, Mr. Three Dollars Is Too Much For A Game On My Six Hundred Dollar Phone.)  We sometimes forget that users live in a world of scarcity, where data has definite value.  For example, you and I know that it makes *no difference whatsoever* to me whether Martha can print out 15 cards or 20 cards during her free trial: the marginal bits are too cheap to even calculate the cost of.  However, Martha definitely does not perceive things that way: 20 cards is *33% more of something she wants*, **of course** that is a good thing!


This means I can give Martha something she wants, very easily, at no marginal cost to me.  That is a good carrot to use in a lot of marketing activities, from incentivizing people to take surveys to incentivizing them to link to you.


## Implementation Details


This turned out to be pretty easy to do with Rails, my [A/B testing framework](http://www.bingocardcreator.com/abingo), and MemcacheDB.  (I could have persisted survey state in the MySQL database with most of my user-specific data.  However, I really hate having to migrate my user model just to accomodate a feature that I may well rip out in two weeks, so a key/value store makes an excellent choice.  If I no longer care about the data, all I have to do is stop requesting it and *bam* it is like it never existed in the first place.)


First I adjusted my users’ dashboards (the main page that they are sent to right after logging in) to include an inducement to take the survey.  I set it to ask all paying customers to take the survey.  My reasoning for this was it is free for me and, if they don’t want to, it costs a maximum of one click to dismiss permanently.  However, giving trial users the survey potentially costs money through lost conversions, so I set up an A/B test to see if offering a survey is very expensive.  This could affect my desire to do them in the future.


Additionally, for trial users, I set up an A/B test on the call to action text: half are given altruism as the reason to take the survey, the other half are offered the aforementioned freebie.  (All survey takers will actually be given the freebie whether promised it or not — it is just as easy to implement either way, but I tend to default to being generous to my users unless I have a darn good reason otherwise, and I don’t here.)  I’m doing this mostly for my own curiosity.


Wufoo has a setting where you can redirect folks to a URL after taking the survey.  I set this to an action which performs housekeeping (setting the user’s survey status to “Completed”, tracking results of the A/B test, setting a thank you message, and redirecting to the dashboard).  If the user bails from the survey with the back button rather than completing it, they’ll be right back at the dashboard and nothing will have changed.


I also added a quick link to hide the survey (it sets their survey status to “Declined”, which will surpress the survey call to action forever), on the theory that users should be able to have an uncluttered experience if they wish to.  This could have been done with AJAX and link_to_remote fairly easily, but doing it the old fashioned way worked fine and only took two lines of code, so I did it that way.


Finally, implementing the freebie took a bit of surgery to some validation code.  It wasn’t very difficult at all — I copy/pasted my existing validator, added “has taken the survey” to the :unless clause to disable it, and pasted in a new copy with the higher limit.  I love the way Rails tends to make minor logical tweaks like this easy.


The total change it took to implement this intelligent, incentivized survey (plus two A/B tests) was ~20 lines of code and ~20 lines of HTML for three alternatives in the view.  It was actually quicker to write and test the code than it was to make the survey in Wufoo’s drag and drop interface.  At no time did I have to waste a week nudging CSS files around to get something that wasn’t horrendous.


Incidentally, I think this is a good demonstration of how Rails, crafty application of cheap software, and the related bag of tricks let you be more nimble than you would be if you were e.g. running on enterprise Java.  I’ve implemented surveys for the universities who are clients of my day job, and surveys of roughly comparable complexity typically require *planning meetings* so that we can *add them to the schedule* and eventually *detail an engineer or two* to get them started.  There’s a place for that in the world, don’t get me wrong, but **I’m already collecting data**.


## Pictures of Implementation


Here’s the variant for trial users which offers the incentive for taking the survey:


If I had a bone of artistic ability in my body there would be a box around that with a red X in the top right corner to dismiss in addition to the textual link, but oh well.


## A Possibly Controversial Note On User Privacy


Normal users don’t really want privacy.  There, I said it.


Users will *say* they want privacy, if you phrase the question the right way.  (“Do you want multinational corporations to put data on your machine that will let them track your visits to sites on the Internet?”  “Oh my good heavens, no!  That’s monstrous!”  “That is necessary to implement things you take for granted, like ‘Remember me’ .”  “That’s totally not the same thing!”  “Google gives you personalized search results the same way, and sells ads against what you searched for early this morning.”  “Well I *like* Google!”) Given the choice between privacy and convenience, they’ll choose convenience every single time, and if you prioritize their privacy over their convenience it is *your* problem.


I said the usual pieties about the survey being totally anonymous.  This is literally true and yet says less than what you might think it says.  Consistent with my [privacy policy](http://www.bingocardcreator.com/privacy.htm) (that no one reads because *no one cares about privacy*), I will make no particular attempt to link users with their answers.  However, I can work backwords from a copy of the survey to personally identifying information (an email address, if they’ve provided it).  And that is a good thing:


The above is a slightly anonymized composite of actual support requests I have gotten over the years.  (I try my level best to satisfy people, but you can’t win every time.)  If that user submits the survey and I can’t identify who he is, I’ve *essentially stolen from him*, because I promised him a refund any time any time he asks for it and I have not delivered on the promise.  Granted, he didn’t ask for it in a very technically savvy fashion, but I try to make it as easy as possible for my users to succeed at the things they clearly intended to do.  Even if their clear intent is to ask for a refund.


If you think this example is far fetched: Google Checkout will, some time after the transaction has happened, mail your customers to request that they write a review of your product.  Reviews are posted in an electronic Siberia and no notification is sent to the merchant when they happen.  However, because it has a text box and is occuring in the context of a commercial relationship, customers assume you are hanging on their every word.  They’ll use the “review” to communicate time-sensitive information like “Oh by the way I need this shipped to …” or “It has been two weeks and my CD hasn’t arrived.”


My theory for why Google didn’t anticipate this failure mode is that Google assumes you care about your customers about as much as Google cares about its customers, and at Google forwarding customer complaints to Siberia would double the likelihood they were actually read.  (Do I sound [bitter](https://www.kalzumeus.com/2009/08/01/my-adwords-are-turned-off-scary-stuff/)?)


Anyhow, the EFF can burn me in effigy if they want to, but given the choice between giving customers ironclad privacy and giving them what their actions demonstrate they actually want, I’ll give them what they actually want.


## Analyzing Results


Since I started writing this post it appears that a user has taken the survey.  Take that, planning meeting.


After I have a bit more data, I’ll grab it from Wufoo, segment it by user type (trial user vs. customer, etc), and started asking the data questions to guide the further development and marketing efforts.  If I find anything interesting, I’ll post about it.
