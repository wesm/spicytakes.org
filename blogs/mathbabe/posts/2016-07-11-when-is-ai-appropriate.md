---
title: "When is AI appropriate?"
date: 2016-07-11
url: https://mathbabe.org/2016/07/11/when-is-ai-appropriate/
word_count: 1013
---


I was invited last week to an event co-sponsored by the White House,Microsoft, and NYU called [AI Now: The social and economic implications of artificial intelligence technologies in the near term](https://artificialintelligencenow.com/). Many of the discussions were under “[Chatham House Rule](https://www.chathamhouse.org/about/chatham-house-rule),” which means I get to talk about the ideas without attributing any given idea to any person.


Before I talk about some of the ideas that came up, I want to mention that the definition of “AI” was never discussed. After a while I took it to mean anything that was technological that had an embedded flow chart inside it. So, anything vaguely computerized that made decisions. Even a microwave that automatically detected whether your food was sufficiently hot – and kept heating if it wasn’t – would qualify as AI  under these rules.


In particular, all of the algorithms I studied for my book certainly qualified. And some of them, like predictive policing and [recidivism risk models](https://artificialintelligencenow.com/schedule/conference), google search and resume filtering algorithms, were absolutely talked about and referred to as AI.


One of the questions we posed was, when is AI appropriate? Is there a class of questions that AI should not be used for, and why? More interestingly, is there AI working and making decisions right now, in some context, that should be outlawed? Or at least put on temporary suspension?


[Aside: I’m so glad we’re actually finally discussing this. Up until now it seems like wherever I go it’s taken as a given that algorithms would be an improvement over human decision-making. People still automatically assume algorithms are more fair and objective than humans, and sometimes they are, but they are by no means perfect.]


We didn’t actually have time to thoroughly discuss this question, but I’m going to throw down the gauntlet anyway.


—


Take recidivism risk models. [Julia Angwin and her team at ProPublica recently demonstrated](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) that the COMPAS model, which was being used in Broward County Florida (as well as many other places around the country), [is racist](https://mathbabe.org/2016/05/24/propublica-report-recidivism-risk-models-are-racist/). In particular, it has very different errors for blacks and for whites, with high “false positive” rates for blacks and high “false negative” rates for whites. This ends up meaning that blacks go to jail for longer, since that’s how recidivism rates are being used.


So, do we throw out recidivism modeling altogether? After all, judges by themselves are also racist; a models such as the COMPAS model might actually be improving the situation. Then again, it might be making it worse. We simply don’t know without a monitor in place. (So, let’s get some monitors in place, people! Let’s see some academic work in this area!)


I’ve heard people call for removing recidivism models altogether, but honestly I think that’s too simple. I think we should instead have a discussion on what they show, why they’re used the way they are, and how they can be improved to help people.


So, if we’re seeing way more black (men) with high recidivism risk scores, we need to ask ourselves: why are black men deemed so much more likely to return to jail? Is it because they’re generally poorer and don’t have the start-up funds necessary to start a new life? Or don’t have job opportunities when they get out of prison? Or because their families and friends don’t have a place for them to stay? Or because the cops are more likely to re-arrest them because they live in poor neighborhoods or are homeless? Or because the model’s design itself is flawed? In short, what are we measuring when we build recidivism scores?


Second, why are recidivism risk models used to further punish people who are already so disadvantaged? What is it about our punitive and vengeful justice system that makes us punish people in advance for crimes they have not yet committed? It keeps them away from society even longer and further casting them into a cycle of crime and poverty. If our goal were to permanently brand and isolate a criminal class, we couldn’t look for a better tool. We need to do better.


Next, how can we retool recidivism models to help people rather than harm them? We could use the scores to figure out who needs resources the most in order to stay out of trouble after release, to build evidence that we need to help people who leave jail rebuild their lives. How do investments in education inside help people once they get out land a job? Do states that make it hard for employers to discriminate based on prior convictions – or for that matter on race – see better results for recently released prisoners? To what extent does “broken windows policing” in a neighborhood affect the recidivism rates for its inhabitants? These are all questions we need to answer, but we cannot answer without data. So let’s collect the data.


—


Back to the question: when is AI appropriate? I’d argue that building AI is almost never inappropriate in itself, but interpreting results of AI decision-making is incredibly complicated and can be destructive or constructive, depending on how well it is carried out.


And, as was discussed at the meeting, most data scientists/ engineers have little or no training in thinking about this stuff beyond optimization techniques and when to use linear versus logistic regression. That’s a huge problem, because part of AI – a big part – is the assumption that AI can solve every problem in essentially the same way. AI teams are, generally speaking, homogenous in gender, class, and often race, and that monoculture gives rise to massive misunderstandings and narrow ways of thinking.


The short version of my answer is, AI can be made appropriate if it’s thoughtfully done, but most AI shops are not set up to be at all thoughtful about how it’s done. So maybe, at the end of the day, AI really *is* inappropriate, at least for now, and until we figure out how to involve more people and have a more principled discussion about what it is we’re really measuring with AI.
