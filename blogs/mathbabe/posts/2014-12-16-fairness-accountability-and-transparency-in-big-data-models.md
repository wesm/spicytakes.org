---
title: "Fairness, accountability, and transparency in big data models"
date: 2014-12-16
url: https://mathbabe.org/2014/12/16/fairness-accountability-and-transparency-in-big-data-models/
word_count: 1691
---


As I wrote about already, last Friday I attended a one day workshop in Montreal called [FATML](http://fatml.org/index.html): Fairness, Accountability, and Transparency in Machine Learning. It was part of the [NIPS](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CB4QFjAA&url=http%3A%2F%2Fnips.cc%2FConferences%2F2014%2F&ei=QTWQVKiOLvWPsQSL2oHAAw&usg=AFQjCNH7MGDqV-O_wIPHiEaAXbB2X51hjw&sig2=GJrp5tsvtI4BxLGZIkverw) conference for computer science, and there were tons of nerds there, and I mean *tons*. I wanted to give a report on the day, as well as some observations.


First of all, I am super excited that this workshop happened at all. When I left my job at Intent Media in 2011 with the intention of studying these questions and eventually writing a book about them, they were, as far as I know, on nobody’s else’s radar. Now, thanks to the organizers [Solon](http://solon.barocas.org/) and [Moritz](http://www.moritzhardt.com/), there are communities of people, coming from law, computer science, and policy circles, coming together to exchange ideas and strategies to tackle the problems. This is what progress feels like!


OK, so on to what the day contained and my copious comments.


**Hannah Wallach**


Sadly, I missed the first two talks, and an introduction to the day, because of two airplane cancellations (boo American Airlines!). I arrived in the middle of Hannah Wallach’s talk, the abstract of which is located [here](http://fatml.org/details.html#hanna). Her talk was interesting, and I liked her idea of having social scientists partnered with data scientists and machine learning specialists, but I do want to mention that, although there’s a remarkable history of social scientists working within tech companies – say at Bell Labs and Microsoft and such – we don’t see that in finance at all, nor does it seem poised to happen. So in other words, we certainly can’t count on social scientists to be on hand when important mathematical models are getting ready for production.


Also, I liked Hannah’s three categories of models: predictive, explanatory, and exploratory. Even though I don’t necessarily think that a given model will fall neatly into one category or the other, they still give you a way to think about what we do when we make models. As an example, we think of recommendation models as ultimately predictive, but they are (often) predicated on the ability to understand people’s desires as made up of distinct and consistent dimensions of personality (like when we use PCA or something equivalent). In this sense we are also exploring how to model human desire and consistency. For that matter I guess you could say any model is at its heart an exploration into whether the underlying toy model makes any sense, but that question is dramatically less interesting when you’re using linear regression.


**Anupam Datta and Michael Tschantz**


Next up Michael Tschantz reported on work with Anupam Datta that they’ve done on Google profiles and Google ads. The started with google’s privacy policy, which I can’t find but which claims you won’t receive ads based on things like your health problems. Starting with a bunch of browsers with no cookies, and thinking of each of them as fake users, they did experiments to see what actually happened both to the ads for those fake users and to the google ad profiles for each of those fake users. They found that, at least sometimes, they did get the “wrong” kind of ad, although whether Google can be blamed or whether the advertiser had broken Google’s rules isn’t clear. Also, they found that fake “women” and “men” (who did not differ by any other variable, including their searches) were offered drastically different ads related to job searches, with men being offered way more ads to get $200K+ jobs, although these were basically coaching sessions for getting good jobs, so again the advertisers could have decided that men are more willing to pay for such coaching.


An issue I enjoyed talking about was brought up in this talk, namely the question of whether such a finding is entirely evanescent or whether we can call it “real.” Since google constantly updates its algorithm, and since ad budgets are coming and going, even the same experiment performed an hour later might have different results. In what sense can we then call any such experiment statistically significant or even persuasive? Also, IRL we don’t have clean browsers, so what happens when we have dirty browsers and we’re logged into gmail and Facebook? By then there are so many variables it’s hard to say what leads to what, but should that make us stop trying?


From my perspective, I’d like to see more research into questions like, of the top 100 advertisers on Google, who saw the majority of the ads? What was the economic, racial, and educational makeup of those users? A similar but different (because of the auction) question would be to reverse-engineer the advertisers’ Google ad targeting methodologies.


Finally, the speakers mentioned a failure on Google’s part of transparency. In your advertising profile, for example, you cannot see (and therefore cannot change) your marriage status, but advertisers can target you based on that variable.


**Sorelle Friedler, Carlos Scheidegger, and Suresh Venkatasubramanian**


Next up we had Sorelle talk to us about her work with two guys with enormous names. They think about how to make stuff fair, the heart of the question of this workshop.


First, if we included race in, a resume sorting model, we’d probably see negative impact because of historical racism. Even if we removed race but included other attributes correlated with race (say zip code) this effect would remain. And it’s hard to know exactly when we’ve removed the relevant attributes, but one thing these guys did was define that precisely.


Second, say now you have some idea of the categories that are given unfair treatment, what can you do? One thing suggested by Sorelle et al is to first rank people in each category – to assign each person a percentile in their given category – and then to use the “forgetful function” and only consider that percentile. So, if we decided at a math department that we want 40% women graduate students, to achieve this goal with this method we’d independently rank the men and women, and we’d offer enough spots to top women to get our quota and separately we’d offer enough spots to top men to get our quota. Note that, although it comes from a pretty fancy setting, this is essentially affirmative action. That’s not, in my opinion, an argument against it. It’s in fact yet another argument for it: if we know women are systemically undervalued, we have to fight against it somehow, and this seems like the best and simplest approach.


**Ed Felten and Josh Kroll**


After lunch Ed Felton and Josh Kroll jointly described their work on making algorithms accountable. Basically they suggested a trustworthy and encrypted system of paper trails that would support a given algorithm (doesn’t really matter which) and create verifiable proofs that the algorithm was used faithfully and fairly in a given situation. Of course, we’d really only consider an algorithm to be used “fairly” if the algorithm itself is fair, but putting that aside, this addressed the question of whether the same algorithm was used for everyone, and things like that. In lawyer speak, this is called “procedural fairness.”


So for example, if we thought we could, we might want to turn the algorithm for punishment for drug use through this system, and we might find that the rules are applied differently to different people. This algorithm would catch that kind of problem, at least ideally.


**David Robinson and Harlan Yu**


Next up we talked to David Robinson and Harlan Yu about their work in Washington D.C. with policy makers and civil rights groups around machine learning and fairness. These two have been active with civil rights group and were an important part of both the Podesta Report, which I blogged about [here](https://mathbabe.org/2014/05/05/podestas-big-data-report-to-obama-good-but-not-great/), and also in drafting the [Civil Rights Principles of Big Data](https://mathbabe.org/2014/05/07/inside-the-podesta-report-civil-rights-principles-of-big-data/).


The question of what policy makers understand and how to communicate with them came up several times in this discussion. We decided that, to combat cherry-picked examples we see in [Congressional Subcommittee meetings](https://mathbabe.org/2013/05/31/technocrats-and-big-data/), we need to have cherry-picked examples of our own to illustrate what can go wrong. That sounds bad, but put it another way: people respond to stories, especially to stories with innocent victims that have been wronged. So we are on the look-out.


**Closing panel with Rayid Ghani and Foster Provost**


I was on the closing panel with Rayid Ghani and Foster Provost, and we each had a few minutes to speak and then there were lots of questions and fun arguments. To be honest, since I was so in the moment during this panel, and also because I was jonesing for a beer, I can’t remember everything that happened.


As I remember, Foster talked about an algorithm he had created that does its best to “explain” the decisions of a complicated black box algorithm. So in real life our algorithms are really huge and messy and uninterpretable, but this algorithm does its part to add interpretability to the outcomes of that huge black box. The example he gave was to understand why a given person’s Facebook “likes” made a black box algorithm predict they were gay: by displaying, in order of importance, which likes added the most predictive power to the algorithm.


[Aside, can anyone explain to me what happens when such an algorithm comes across a person with very few likes? I’ve never understood this very well. I don’t know about you, but I have never “liked” anything on Facebook except my friends’ posts.]


Rayid talked about his work trying to develop a system for teachers to understand which students were at risk of dropping out, and for that system to be fair, and he discussed the extent to which that system could or should be transparent.


Oh yeah, and that reminds me that, after describing my book, we had a pretty great argument about whether credit scoring models should be open source, and what that would mean, and what feedback loops that would engender, and who would benefit.


Altogether a great day, and a fantastic discussion. Thanks again to Solon and Moritz for their work in organizing it.
