---
title: "Guest Post: how to be a data scientist at a non-profit"
date: 2015-09-30
url: https://mathbabe.org/2015/09/30/guest-post-how-to-be-a-data-scientist-at-a-non-profit/
word_count: 1453
---


*This is a guest post by John Santerre, a 5th year Ph.D. student at the University of Chicago in the Computer Science Department. Previously a photojournalist, John has worked with nonprofits and NGO’s off and on for the last ten years. This summer he served as a Research Programmer at The Eric and Wendy Schmidt Data Science for Social Good Fellowship. His master’s work, under Prof. Lek-heng Lim, involved the use of Hodge Decomposition for rank disambiguation while his Ph.D work is at Argonne National Laboratory and involves scalable Machine Learning techniques for use on Cancer and Anti-Microbial Resistance (AMR).*


The recent mathbabe post *[What can a non-academic mathematician do that makes the world a better place](https://mathbabe.org/2015/09/08/what-can-a-non-academic-mathematician-do-that-makes-the-world-a-better-place/)* struck a chord with me.  Over the last ten years I’ve worked as a photojournalist on and off with nonprofits photographing everything from Sigourney Weaver and Anna Wintour to documenting drug dealers in Puerto Rico, rebel fighters in Burma/Myanmar, and the UN Peacekeeping effort in Haiti. I was so involved with nonprofit work, I founded my own, just to provide photography services to other nonprofits. Most recently I spent the summer as research programer for the [Eric and Wendy Schmidt Data Science for Social Good Fellowship](http://dssg.io/). I thought my experience might offer a small amount insight, at least for those who are truly new to working with nonprofits or “social good” organizations.


The most rewarding and challenging aspect of working at a nonprofit is the responsibility you bear to educate the organization about the limitations and potential you present. This can’t be overstated. The organization you choose to work with will have any number of teachers, secretaries, drivers, programmers, and support staff all with clearly delineated jobs descriptions. As the outsider who, as in T.S. Eliot’s poem, has “Come … to tell you all, I shall tell you all,” you will almost certainly be alone in your role. In fact, that is the explicit reason we seek out such opportunities: working at the “tip of the spear” presents an opportunity for our skills to be uniquely impactful. Offering insights that the organization wouldn’t have access to, or perhaps cannot afford, can be vastly fulfilling.


However, this brings with it an inherent Faustian bargain. Just as the violinist Joshua Bell was ignored in the DC Metro but adored in the philharmonic [1], so too will many of your finely tuned skills fall on comparatively (computationally?) deaf ears. In my experience, you have/get to “check” your craft at the door. In my role as a photographer this often meant my most useful skill was taking comparatively simple photographs [2]. Now it often means my technical contribution to nonprofits is less than my potential. In fact, the clients are more than happy to explicitly express that. Often they are looking for a “sanity check” and understand that I am overqualified for their problem. In fact they often seek out and will only work with someone who they perceive is overqualified. I personally don’t mind this. In the right organization you can build on your own personal skill sets. In fact, I’ve never been challenged in the ways I had expected. Even so, there are a host of fairly common challenges and insights that are orthogonal to my craft that have kept appearing over the last ten years which I’ll share.


**1. You are alone.**


You will likely be a solo consultant who has no one to brainstorm with, no one to advocate for an agenda with, and no one to share the burden of the tumultuous experience of making sense of a new work environment. To top all of that off, you are often working on a necessarily compressed schedule. Ryan Kappadal, a statistics professor at the Air Force Institute of Technology (10+ years of experience in data science) told me this summer that the Air Force integrates its data science teams into other units in pairs. It was instantly obvious to me how much more impressive it is for an organization to watch and interact with two professionals debating approaches and building a strategy out loud rather than listening to a pitch from a single perspective.


**2. You will likely have different metrics of success.**


Currently I work on classifying Anti-Microbial Resistance (AMR) at Argonne National Lab, a topic so important that the UN, POTUS, and WHO have all identified it as a top threat facing global humanity. When I explained my work to a ‘data scientist’ at a start-up I noted a 95% accuracy of one classifier. They responded slightly dismissively “Is 95% high enough?”. Sure it’s “just” the k-means classification accuracy on the MNIST data set, but it’s also high enough to identify consistently (despite low sample size), the gene regions that confer resistance to a particular antimicrobial.This provides evidence of the likely mechanism – i.e., cell wall transport – that has mutated thereby implying possible counter strategies for the biologists.


Perhaps more humorously, I traveled to Cambodia to work with a nonprofit at “Smoke Mountain”, the continually burning garbage dump in Phnom Penh. The most useful service I provided for them was photographing their Christmas card. I climbed atop a nearby building and photographed the children spelling out “Thank You!” in human gymnastic positions. Not exactly what I was expecting after traveling 1/2 way around the world!


I cannot stress this topic enough, so I will harp on one more little point. In my mind, the inculcation required to become a specialist in our craft can blind us to the impact our client requires. In NGO work the objective is to build a shared skill set between you and the organization, rather than develop new insights into the problem. Photographers are constantly looking for new ways to restructure the frame. Similarly, machine Learning people are constantly trying to find new ways to approach the problems. But working with organizations requires a different metric. I have to judge my contribution not by the number of trailing digits of prediction accuracy, but by the impact I have on how biologist’s approach the problem of AMR. I love the craft of both ML and photography, so stepping out of the role where the craft is the most important thing is always hard, but when appropriate it can be vastly rewarding.


**3. Different organizations have surprisingly similar needs.**


This summer at the DSSG, my role, along with another programer was to build a “best practices” pipeline across the DSSG fellows and individual teams [3]. Freed from providing results to a client we could write maintainable clean code, while simultaneously “looking over their shoulders” for similarities between workflows. While each group was different, there was surprisingly consistency across groups, especially in terms of client interaction. That is another way of saying a sampling of 3-5 such organizations will give you a good sense of what this work is actually like.


**4. Social good doesn’t require a 501c3 status.  **


It can be more rewarding and impactful to provide sophisticated technical services to a for-profit start-up preventing relapse in drug addiction (i.e. [TriggrHealth.com](http://triggrhealth.com/)) than providing rudimentary analysis consulting with a nonprofit following bird migrations [4]. It can be more fulfilling working for a growing for-profit but non-partisan organization like [BallotReady.org](http://www.ballotready.org/) targeting voter engagement, than it is to work for an issue-based partisan nonprofit. Or maybe it’s not for you. We are fortunate enough to work in a time where both types of organizations require our services.


—


In summary, with such tremendous need for the intersection of statistics and computer science, I find I am overwhelmed with options, but only if I am flexible in what role I expect to provide. Having “a voice” as a photographer or a focused specialty as an academic are hallmarks of advanced practitioners for good reason. These are the contributions that move the field forward. Conversely, serving as an advocate is a generalist position. Recognizing that helps me to find unique ways to ensure both my professional progress and that the organization’s needs are met.


1.  While people walked past him IRL, he did manage to get [160k](https://www.youtube.com/watch?v=hnOPu0_YWhw) youtube views of his being ignored however!


2.  A.K. Kimoto traveled through northern Afghanistan as photographer for UNICEF taking simple portraits that were very much needed.  Later he used the connections he gained to return and photograph this [work](http://lens.blogs.nytimes.com/2010/06/15/showcase-173/), a far more subtle and evocative collection of imagery that was very close to his heart.


3.  It’s a (not quite alpha stage) python grid search library across models and parameters.  We named [Diogenes](https://github.com/dssg/diogenes) and gave it the tongue in cheek slogan “Searching for an honest classifier”.


4.  Although, I used to watch the fall migrations mountain-side, and .csv’s of the data might make for an interesting weekend!
