---
title: "Can we use data analysis to make policing less racist?"
date: 2016-04-19
url: https://mathbabe.org/2016/04/19/can-we-use-data-analysis-to-make-policing-less-racist/
word_count: 620
---


A couple of weeks ago there was a kerfuffle at Columbia, [written up in the Columbia Spectator](http://columbiaspectator.com/opinion/2016/04/04/machine-learning-and-stop-and-think) by Julie Chien. A machine learning course, taught in the CS department by Professor Satyen Kale, was assigned to “Help design RoboCop!” using Stop and Frisk data.


The title was ill-chosen. Kale meant it to be satirical, but his actual wording of the assignment didn’t make that clear at all, which is of course the danger with satire. Given the culture of CS, people misinterpreted and were outraged by it. This eventually led to an organized group of students called [ColorCode](https://www.facebook.com/CUColorCode/) to [issue a statement in protest of the assignment](http://columbialion.com/?p=1701), and then for [Kale to issue an apology](http://www.satyenkale.com/coms4771/statement.html), after which ColorCode [issued a second statement](https://docs.google.com/document/d/1WeRI3T1TTB-wwAOOPAf6LuIHJqsxL6rLjQv8jqlacKk/edit).


I’m really glad this conversation is finally happening, even if the assignment was a disaster. I’ve been saying for years that the CS department at Columbia, like many CS departments everywhere, has an obligation to teach and think about the ethics of machine learning as well as the mathematical techniques. And although this was an awkward way to get it started, it’s absolutely critical that it gets done. Machine learning algorithms are not objective, because the data going into them are historical artifacts of racist police practices.


In other words, we need to revive this topic, and do it right. If I were teaching data science or machine learning at Columbia, I’d want to spend a week on the Stop, Question and Frisk data, which by the way is located [here](http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml); I’ve been playing around with it for a few days now and it’s really not too hard to look into.


What do I think we could accomplish? Well, [here’s something](https://5harad.com/papers/policing-the-police.pdf) I read yesterday that might be expanded upon. Namely, a paper by Sharad Goel, Maya Perelman, Ravi Shroff, and David Alan Sklansky entitled *[Combatting Police Discrimination in the Age of Big Data](https://5harad.com/papers/policing-the-police.pdf)*.


The idea behind this paper, and [a related project housed at Stanford](http://www.stanforddaily.com/2016/02/15/researchers-begin-data-analysis-project-on-police-brutality/), is to use the Stop and Frisk data in order to:

1. gather statistical evidence that the Stop and Frisk practices were racist, by for example showing that the “hit rate” of finding a weapon, for example, was much lower for blacks than it was for whites, even in “high crime” neighborhoods, and
2. develop simple algorithms that the police themselves could use to determine whether their individual biases were overstating the suspiciousness of a given person in a given situation. In other words, it’s an algorithm that is meant to help officers become less racist.


One of the best things about this article is the historical context it gives about the extent to which “reasonable suspicion” is a statistical construction. Judges have been inconsistent with this idea, but there might be an emerging understanding of whether, and in what contexts, it’s considered OK to stop and frisk someone given that the chance you’ll find a weapon is 1% or less.


Personally, I’m not sure it makes sense to equip police with an algorithm to be used in real time. There are obvious issues around gaming such a model, or otherwise learning to evade undesired outcomes. Another way of implementing it, that I think might be more promising, would be at the precinct level. Imagine looking into certain types of stops and frisks and noting the hit rate is too low to warrant the imposition, which would (ideally) change the rules of stop and frisk themselves.


In other words, although I am excited about the idea of using data to track and help prevent racist practices, I don’t think we know exactly what that would look like in practice. But it’s something we desperately need to start thinking about. Let’s have the conversation!
