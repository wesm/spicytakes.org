---
title: "Aunt Pythia’s advice"
date: 2013-11-09
url: https://mathbabe.org/2013/11/09/aunt-pythias-advice-29/
word_count: 1402
---


Aunt Pythia is well-slept and excited to be here to answer your wonderful and thoughtful ethical conundrums. Please do comment on my answers, if you disagree but especially if you agree wholeheartedly and want me to keep up the good work. *Love* that kind of encouraging comment.


**And please, don’t forget to ask me a question at the bottom of the page!**


By the way, if you don’t know what the hell I’m talking about, go [here](https://mathbabe.org/category/aunt-pythia/) for past advice columns and [here](https://mathbabe.org/2012/11/03/ask-aunt-pythia/) for an explanation of the name Pythia.


——


*Dear Aunt Pythia,*


*What is your text editor of choice? The most popular ones, the ones in which I know die-hard fans, are for Emacs, Vi/Vim, and Sublime. I am personally an Emacs user, but I haven’t given any other editors a chance, to be honest. Which do you prefer to use, and why?*


*Text Editor*


Dear TE,


I use [emacs](http://en.wikipedia.org/wiki/GNU_Emacs) mostly, and [xemacs](http://en.wikipedia.org/wiki/Xemacs) when it’s available. It’s easy, it “knows” about python and other languages, and the drop-down menu is easier than remembering keystroke commands. I’ve been known to use an [IDE or two](http://en.wikipedia.org/wiki/Integrated_development_environment) depending on codebase context. For me it’s all about ease of use and, since I’ve never been a professional engineer and so I’ve never spent a large majority of my time with source code, vim doesn’t attract me, even though everything is keystroke and you never need to use your mouse.


As an aside, I’d like to argue this point, because it’s often shrouded in weird macho crap: why not use your mouse? Does it really waste that much time? I honestly have never been prevented from coding efficiently because my arm is too tired from moving from the keyboard to the mouse and back. Is the goal really to be able to stay in the exact same position for as long as possible? I’m the kind of person that is too fidgety for such ideas. I take the “stand up and walk around every 20 minutes” rule seriously, at least before 4pm, when I become a zombie.


Good luck, young padawan!


Aunt Pythia


——


*Dear Aunt Pythia,*


*What are your thoughts on the famous (infamous?) [two-daughter problem](http://vishal12.wordpress.com/2010/08/03/the-two-daughter-problem/)? I have three PhDs who give different answers all of which appear to be statistically correct. Modinow says the answer is 1/2. The chair of the stats department at local university says the answer is 3/7, and a chap at Fl Coastal College has yet a 3rd answer which I have lost.*


*How can this be? *


*Tombs*


Dear Tombs,


OK I’m pretty sure there’s only one answer to this if it’s stated precisely. So let’s try to do that. Here’s the question:


> Suppose I have two children. One of them is a girl who was born on a Friday. What are the chances of both children being girls?


Now I’m a big fan of making things incredibly easy and visual. So what I’m going to do here is identify the fact that, as far as children go, there are two attributes of interest in this question, namely gender and day of birth. I will assume that all options are equally likely and that they are independent from each other as well as between kids, and in my first iteration I’ll draw up a list of equally likely bins for a given child, namely of either gender and of any day born. That’s 14 equally likely bins for a given single child, and that means they happen with probability 1/14.


Now, for the second iteration, let’s talk about having two kids. You have a 2-dimensional array of bins, which you arrange to be 14-by-14, and you assume that any of those 14*14 = 196 bins is *a priori* equally likely.


Label the bins with ordered pairs (gender, day). The x-axis is first kid, y-axis is 2nd kid. Each bin equally likely.


If you label the first bin as “(Female, Friday)” and the second bin as “(Female, Saturday)” and so on, you realize that the condition that “one of the two kids is a girl who was born on Friday” means that we already know we are working in the context where we are either in the left-most column or the bottom row. Here’s my awesome rendition of this area:


The pink parts show where there’s a girl born on a Friday among the two children.


Specifically, the left bottom corner is the case where there are two girls, both born on Friday. The one to the right and above that corner refers to the case where there are two girls, one born on Friday and one born on Saturday. The stuff on the right and in the upper part of the column refers to the case where there’s a Friday girl and a boy.


Altogether we have 13 pink bins with two girls and 14 pink bins of a boy and a girl. So the overall chances of two girls, given one Friday girl, is 13/27.


I hope that’s convincing!


Aunt Pythia


——


*Dear Auntie P,*


*What do you think about topological data analysis (some info [here](http://en.wikipedia.org/wiki/Topological_data_analysis)). Should we trust people who can’t tell the difference between their rear end and a coffee cup because the two are topologically equivalent?*


*Topological Fear*


Dear TF,


Geez I don’t know about you but my rear end is not topologically equivalent to my coffee cups. You either need to go to a doctor or buy some coffee cups that don’t leak.


So, I don’t know very much about this stuff, but I do think it’s potentially interesting, and it’s maybe close to an idea I’ve had for a while now but for which I haven’t found a practical use. Yet.


The idea I have had, if it’s close to this idea, and I think from short conversations with people that it is, is that if you draw a bunch of scatter plots of, say, two attributes x1 and x2 and an outcome y (so you need numerical data for this), then you’ll notice in the resulting 3-dimensional blob of points some interesting topological properties. Namely, there seem to be pretty well-defined boundaries, and those boundaries might have certain kinds of curves, and there may possibly even be well-defined holes in the blob, at least if you “fatten up” the points (sufficiently but not more than necessary) and then take the union of all of the resulting spheres to be some kind of 3-d manifold. You can then play with the relationship between, say, the radius of these fattened points and the topological properties of the resulting blob.


Anyhoo, the idea could be that, if you see x1 and x2 then you can exclude a y that lives in a hole, or rather where point (x1, x2, y) would live in a hole. This is more than most kinds of modern models can do for you, but even so I’ve never seen this actually come in handy.


I hope that helps, and please do see a doctor!


Auntie P


——


*Dear Aunt Pythia,*


*This is a reaction to a previous post (maybe Oct 12?) where you said the following: *


> *My kids, to be clear, hate team sports and suck at them, like good nerds.*


*Now, as a nerd whose parents never let play team sports growing up and now plays one in college (a “nerd” sport, but still…), I have a question for you: Why do “good nerds” have to hate sports and/or suck at them? What classifies a “good nerd”? Does this generalize to other things that nerds are stereotypically bad at, like sex lives? Is there another category that should be created for nerdy type people that are also jocky-er, like a nerock or a jord?*


*With Love,*

*A “Bad Nerd”*


Dear Bad Nerd,


Great question, and you’re not the only nerd that called me out on my outrageous discrimination. I wasn’t being fair to my nerock and jord friends, and that ‘aint cool. Although, statistically I believe I still have a point, there’s no reason to limit people in arbitrary ways like that, and it’s fundamentally un-nerdy of me to do so.


For all you nerocks and jords out there: you go, girls! and boys!


But just for the record, nerds are categorically excellent at sex. We all know that. Say yes.


Love,


Aunt Pythia


——


Please submit your well-specified, fun-loving, cleverly-abbreviated question to Aunt Pythia!
