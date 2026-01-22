---
title: "New Jersey at risk of implementing untested VAM-like teacher evaluation model"
date: 2013-05-28
url: https://mathbabe.org/2013/05/28/new-jersey-at-risk-of-implementing-untested-vam-like-teacher-evaluation-model/
word_count: 2335
---


*This is a guest post by Eugene Stern.*


A big reason I love this blog is Cathy’s war on crappy models. She has posted multiple times already about the lousy performance of models that rate teachers based on year-to-year changes in student test scores (for example, read about it [here](https://mathbabe.org/?s=value+added+model)). Much of the discussion focuses on the model used in New York City, but such systems have been, or are being, put in place all over the country. I want to let you know about the version now being considered for use across the river, in New Jersey. Once you’ve heard more, I hope you’ll help me try to stop it.


**VAM Background**


A little background if you haven’t heard about this before. Because it makes no sense to rate teachers based on students’ absolute grades or test scores (not all students start at the same place each year), the models all compare students’ test scores against some baseline. The simplest thing to do is to compare each student’s score on a test given at the end of the school year against their score on a test given at the end of the previous year. Teachers are then rated based on how much their students’ scores improved over the year.


Comparing with the previous year’s score controls for the level at which students start each year, but not for other factors beside the teacher that affect how much they learn. This includes attendance, in-school environment (curriculum, facilities, other students in the class), out-of-school learning (tutoring, enrichment programs, quantity and quality of time spent with parents/caregivers), and potentially much more. Fancier models try to take these into account by comparing each student’s end of year score with a predicted score. The predicted score is based both on the student’s previous score and on factors like those above. Improvement beyond the predicted score is then attributed to the teacher as “value added” (hence the name “value-added models,” or VAM) and turned into a teacher rating in some way, often using percentiles. One such model is used to rate teachers in New York City.


It’s important to understand that there is no single value-added model, rather a family of them, and that the devil is in the details. Two different teacher rating systems, based on two models of the predicted score, may perform very differently – both across the board, and in specific locations. Different factors may be more or less important depending on where you are. For example, income differences may matter more in a district that provides few basic services, so parents have to pay to get extracurriculars for their kids. And of course the test itself matters hugely as well.


**Testing the VAM models**


Teacher rating models based on standardized tests have been around for 25 years or so, but two things have happened in the last decade:

1. Some people started to use the models in formal teacher evaluation, including tenure decisions.
2. Some (other) people started to test the models.


This did not happen in the order that one would normally like. Wanting to make “data-driven decisions,” many cities and states decided to start rating teachers based on “data” before collecting any data to validate whether that “data” was any good. This is a bit like building a theoretical model of how cancer cells behave, synthesizing a cancer drug in the lab based on the model, distributing that drug widely without any trials, then waiting around to see how many people die from the side effects.


The full body count isn’t in yet, but the models don’t appear to be doing well so far. To look at some analysis of VAM data in New York City, start [here](http://garyrubinstein.teachforus.org/2012/02/26/analyzing-released-nyc-value-added-data-part-1/) and [here](http://schoolfinance101.wordpress.com/2012/11/17/on-the-stability-or-not-of-being-irreplaceable/). Note: this analysis was not done by the city but by individuals who downloaded the data after the city had to make it available because of disclosure laws.


I’m not aware of any study on the validity of NYC’s VAM ratings done by anyone actually affiliated with the city – if you know of any, please tell me. Again, the people preaching data don’t seem willing to actually use data to evaluate the quality of the systems they’re putting in place.


Assuming you have more respect for data than the mucky-mucks, let’s talk about how well the models actually do. Broadly, two ways a model can fail are being biased and being noisy. The point of the fancier value-added models is to try to eliminate bias by factoring in everything other than the teacher that might affect a student’s test score. The trouble is that any serious attempt to do this introduces a bunch of noise into the model, to the degree that the ratings coming out look almost random.


You’d think that a teacher doesn’t go from awful to great or vice versa in one year, but the NYC VAM ratings show next to no correlation in a teacher’s rating from one year to the next. You’d think that a teacher either teaches math well or doesn’t, but the NYC VAM ratings show next to no correlation in a teacher’s rating teaching a subject to one grade and their rating teaching it to another –* in the very same year*!  (Gary Rubinstein’s blog, linked above, documents these examples, and a number of others.)  Again, this is one particular implementation of a general class of models, but using such noisy data to make significant decisions about teachers’ careers seems nuts.


**What’s happening in New Jersey**


With all this as background, let’s turn to what’s happening in New Jersey.


You may be surprised that the version of the model proposed by [Chris Christie](http://en.wikipedia.org/wiki/Chris_Christie)‘s administration (the education commissioner is Christie appointee [Chris Cerf](http://www.state.nj.us/education/genfo/overview/bio.htm), who helped put VAM in place in NYC) is about the simplest possible. There is no attempt to factor out bias by trying to model predicted scores, just a straight comparison between this year’s standardized test score and last year’s.  For an overview, see [this](http://www.state.nj.us/education/AchieveNJ/teacher/SGPDetailedGeneralOverview.pdf).


In more detail, the model groups together all students with the same score on last year’s test, and represents each student’s progress by their score on this year’s test, viewed as a percentile across this group. That’s it. A [fancier version](http://www.state.nj.us/education/AchieveNJ/teacher/SGPTechnicalOverview.pdf) uses percentiles calculated across all students with the same score in each of the last several years. These can’t be calculated explicitly (you may not find enough students that got exactly the same score each the last few years), so they are estimated, using a statistical technique called quantile regression.


By design, both the simple and the fancy version ignore everything about a student except their test scores. As a modeler, or just as a human being, you might find it silly not to distinguish between a fourth grader in a wealthy suburb who scored 600 on a standardized test from a fourth grader in the projects with the same score. At least, I don’t know where to find a modeler who doesn’t find it silly, because nobody has bothered to study the validity of using this model to rate teachers. If I’m wrong, please point me to a study.


**Politics and SGP**


But here we get into the shell game of politics, where rating teachers based on the model is exactly the proposal that lies at the end of an impressive trail of doubletalk.  Follow the bouncing ball.


These models, we are told, differ fundamentally from VAM (which is now seen as somewhat damaged goods politically, I suspect). While VAM tried to isolate teacher contribution, these models do no such thing – they are simply measuring student progress from year to year, which, after all, is what we truly care about. The models have even been rebranded with a new name: student growth percentiles, or SGP. SGP is sold as just describing student progress rather than attributing it to teachers, there can’t be any harm in that, right? – and nothing that needs validation, either. And because SGP is such a clean methodology – if you’re looking for a data-driven model to use for broad “educational assessment,” don’t get yourself into that whole VAM morass, use SGP instead!


Only before you know it, educational assessment turns into, you guessed it, *rating teachers*. That’s right: because these models aren’t built to rate teachers, they can focus on the things that really matter (student progress), and thus end up being – wait for it – much better for rating teachers! War is peace, friends. Ignorance is strength.


**Creators of SGP**


You can find a good discussion of SGP’s and their use in evaluation [here](http://njedpolicy.wordpress.com/2013/05/02/deconstructing-disinformation-on-student-growth-percentiles-teacher-evaluation-in-new-jersey/), and a lot more from the same author, the impressively prolific Bruce Baker, [here](http://schoolfinance101.wordpress.com/category/race-to-the-top/value-added-teacher-evaluation/).  Here’s a [response from the creators of SGP](http://www.ednewscolorado.org/voices/student-growth-percentiles-and-shoe-leather). They maintain that information about student growth is useful (duh), and agree that differences in SGP’s should not be attributed to teachers (emphasis mine):


> Large-scale assessment results are an important piece of evidence *but are not sufficient to make causal claims about school or teacher quality*.


**SGP and teacher evaluations**


But guess what?


The New Jersey Board of Ed and state education commissioner Cerf are putting in place a new teacher evaluation code, to be used this coming academic year and beyond. You can find more details [here](http://southbrunswick.patch.com/articles/cerf-goes-public-about-student-test-scores-and-teacher-evaluations) and [here](http://southbrunswick.patch.com/articles/student-test-scores-to-carry-just-a-little-bit-less-weight-for-tenure-decisions).


Summarizing: for math and English teachers in grades 4-8, 30% of their annual evaluation next year would be mandated by the state to come from those very same SGP’s that, according to their creators, are not sufficient to make causal claims about teacher quality. These evaluations are the primary input in tenure decisions, and can also be used to take away tenure from teachers who receive low ratings.


The proposal is not final, but is fairly far along in the regulatory approval process, and would become final in the next several months. In a recent step in the approval process, the weight given to SGP’s in the overall evaluation was reduced by 5%, from 35%. However, the 30% weight applies next year only, and in the future the state could increase the weight to as high as 50%, at its discretion.


**Modeler’s Notes**


Modeler’s Note #1: the precise weight doesn’t really matter. If the SGP scores vary a lot, and the other components don’t vary very much, SGP scores will drive the evaluation no matter what their weight.


Modeler’s Note #2: just reminding you again that this data-driven framework for teacher evaluation is being put in place *without any data-driven evaluation of its effectiveness*. And that this is a feature, not a bug – SGP has not been tested as an attribution tool because we keep hearing that it’s not meant to be one.


In a slightly ironic twist, commissioner Cerf has responded to criticisms that SGP hasn’t been tested by pointing to a Gates Foundation study of the effectiveness of… value-added models.  The study is [here](http://documents.latimes.com/measures-of-effective-teaching/).  It draws pretty positive conclusions about how well VAM’s work.  A number of critics have argued, pretty effectively, that the conclusions are unsupported by the data underlying the study, and that the data actually shows that VAM’s work badly.  For a sample, see [this](http://nepc.colorado.edu/thinktank/review-learning-about-teaching).  For another example of a VAM-positive study that doesn’t seem to stand up to scrutiny, see [this](http://obs.rc.fas.harvard.edu/chetty/value_added.pdf) and [this](http://schoolfinance101.wordpress.com/2012/01/07/fire-first-ask-questions-later-comments-on-recent-teacher-effectiveness-studies/).
**Modeler’s Role Play #1**
Say you were the modeler who had popularized SGP’s.  You’ve said that the framework isn’t meant to make causal claims, then you see New Jersey (and other states too, I believe) putting a teaching evaluation model in place that uses SGP to make causal claims, without testing it first in any way. What would you do?
So far, the SGP mavens who told us that “Large-scale assessment results are an important piece of evidence but are not sufficient to make causal claims about school or teacher quality” remain silent about the New Jersey initiative, as far as I know.
**Modeler’s Role Play #2**
Now you’re you again, and you’ve never heard about SGP’s and New Jersey’s new teacher evaluation code until today.  What do you do?
I want you to help me stop this thing.  It’s not in place yet, and I hope there’s still time.
I don’t think we can convince the state education department on the merits.  They’ve made the call that the new evaluation system is better than the current one or any alternatives they can think of, they’re invested in that decision, and we won’t change their minds directly.  But we can make it easier for them to say no than to say yes.  They can be influenced – by local school administrators, state politicians,  the national education community, activists, you tell me who else.  And many of those people will have more open minds.  If I tell you, and you tell the right people, and they tell the right people, the chain gets to the decision makers eventually.
I don’t think I could convince Chris Christie, but maybe I could convince Bruce Springsteen if I met him, and maybe Bruce Springsteen could convince Chris Christie.
**VAM-anifesto**
I thought we could start with a manifesto – a direct statement from the modeling community explaining why this sucks. Directed at people who can influence the politics, and signed by enough experts (let’s get some big names in there) to carry some weight with those influencers.
Can you help? Help write it, sign it, help get other people to sign it, help get it to the right audience. Know someone whose opinion matters in New Jersey? Then let me know, and help spread the word to them. Use Facebook and Twitter if it’ll help. And don’t forget good old email, phone calls, and lunches with friends.
Or, do you have a better idea? Then put it down. Here. The comments section is wide open. Let’s not fall back on criticizing the politicians for being dumb after the fact.  Let’s do everything we can to keep them from doing this dumb thing in the first place.
Shame on us if we can’t make this right.
