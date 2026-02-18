---
title: "A few reasons to be skeptical of machine learning"
date: 2016-05-19
url: https://jvns.ca/blog/2016/05/19/a-few-reasons-to-be-skeptical-of-machine-learning-results/
slug: a-few-reasons-to-be-skeptical-of-machine-learning-results
word_count: 782
---


I’m giving a talk at PyData Berlin on Friday, and it’s about

- why machine learning is fun and awesome
- [how to trick a neural network](https://codewords.recurse.com/issues/five/why-do-neural-networks-think-a-panda-is-a-vulture)
- why, even though machine learning is really awesome and cool and you can do super powerful and interesting things with it – why you should still be skeptical


I wanted to put some of my ideas together, so as usual I’m writing a blog post. These are all pretty basic ideas but maybe they are helpful to people who are new to thinking about machine learning! We’ll see.


### machine learning models are only as good as the data you put into them


When explaining what machine learning is, I’m giving the example of predicting the country someone lives in from their first name. So John might be American and Johannes might be German.


In this case, it’s really easy to imagine what data you might want to do a good job at this – just get the first names and current countries of every person in the world! Then count up which countries Julias live in (Canada? The US? Germany?), pick the most likely one, and you’re done!


This is a super simple modelling process, but I think it’s a good illustration – if you don’t include any data from China when training your computer to recognize names, it’s not going to get any Chinese names right!


This also applies when you have Big Datasets – maybe you have bajillions of data points in the US, but very few in the rest of the world. This means your model will represent your US data but not the rest!


### machine learning programs can have bugs.


So, machine learning is usually implemented with, well, computer programs. As we all know, computer programs sometimes (dare I say “usually”?) have bugs.


At work it’s definitely happened that someone’s said to me “hey julia, why did the machine learning make this decision? it seems wrong?” and I’ve said “oh, you know, machine learning! it’s probably doing something cool and smart”.


But then I look into it anyway. And then, rather than something cool and smart, the program I work on just had a bug. And then I was really happy that the people asking the questions didn’t assume that the machine learning was Correct and Smart, but that instead told us “hey, this looks wrong”.


If you want to read more on the topic of “machine learning programs have bugs, maybe more bugs than regular programs”, [Machine Learning: The High Interest Credit Card of Technical Debt](http://research.google.com/pubs/pub43146.html) is a fantastic paper from Google.


### machine learning models often are just totally wrong


Okay, so let’s supposed you trained your model on a reasonable dataset, and your program has no bugs. Awesome. Here’s the results of a search in my Google Photos for the string “baby”. I’m assuming they’re using machine learning to classify my images and automatically attach keywords to them.


![](https://jvns.ca/images/baby.png)


These are all pictures of me and none of them are pictures of babies. It’s totally fine that Google Photos’ machine learning is doing a bad job here – it’s not a mission critical application of machine learning, and there are actually a few pictures of adorable babies in those search results.


But there are also mysteriously/hilariously donald trump pinatas.


![](https://jvns.ca/images/donald-trump-pinata.png)


Google Photos does awesome when I search for “fire hydrant” and “beach” and lots of other things, so, to be clear – this is totally a useful feature and I like it. But it’s definitely not perfect and sometimes it’s absurd.


Again, this is something which is totally familiar to machine learning practitioners, but I think it’s a good reminder to be skeptical of individual machine learning predictions.


### be skeptical!


[Cathy O’Neil’s blog](https://mathbabe.org) is one of my favorites, because she constantly talks about the need to assume that just because something came out of a statistical model it isn’t “objective” or even necessarily correct.


Carina Zona has a great talk called [Consequences of an insightful algorithm](http://www.slideshare.net/cczona/consequences-of-an-insightful-algorithm) which talks about a few cases where machine learning models that did what they were supposed to do had unintended negative consequences (like the famous Target pregnancy case).


One of my favorite things is when a person (not a machine learning specialist! just anyone!) is like “hey, your machine learning? it did something I didn’t expect”. Often they’re right, and there *is* something weird going on, or something that could be improved.


Machine learning is super powerful and you can build models that do amazing things, but they can also tell you that a donald trump pinata is a picture of a baby, and that makes no sense.
