---
title: "Women in Machine Learning 2015 (fun!!!)"
date: 2015-12-07
url: https://jvns.ca/blog/2015/12/07/women-in-machine-learning-2015-fun/
slug: women-in-machine-learning-2015-fun
word_count: 868
---


I went to the [Women in Machine Learning](http://wiml2015.weebly.com/) conference yesterday (part of [NIPS](http://nips.cc)). It was SO FUN. I never go to academic conferences, and talking to grad students about their research and what methods they think are exciting is amazing. I actually liked it a lot more than an industry conference because everything was so alien & unfamiliar to me and everyone knew way more about their field than me. I learned more than I did by going to (for instance) PyCon, which is a fantastic industry conference.


It really made me want to reconsider what conferences I go to, and to go to more conferences in fields I’m less familiar with.


The organizers did a great job putting it together and the talks were really good.
Here is some stuff I thought was especially exciting! All of these talk descriptions are heavily paraphrased and I have probably misunderstood things. But I thought they were super cool and here’s what I got out of them.


### Is it all in the phrasing? (by [Lillian Lee](https://www.cs.cornell.edu/home/llee/))


She talked about her research on how phrasing affects the impact of, say, a tweet! Here’s [a classifier where you can write two tweets](https://chenhaot.com/retweetedmore/) and it’ll tell you which one it thinks will be retweeted more! And there’s a [corresponding quiz](https://chenhaot.com/retweetedmore/quiz)! And a paper! I have not yet read the paper.


I really loved this talk because guessing which tweet will get more RTs is a task that humans are ok at (they can guess right something like 75% of the time), but it’s not a trivial task! So it’s a pretty interesting place to try machine learning. And the methodology they used makes a lot of sense to me (pick tweets tweeted by the same person, that link to the same URL). And then they actually make progress using machine learning to do it! Neat.


I feel like most ML I see is about tasks that humans can get 95% or 100% correct (like distinguishing cats from dogs, or whatever). So doing ML on tasks that have something intrinsically hard about them – where you maybe **can’t** ever get to 100% accuracy – is really interesting to me.


She said she makes her talks intentionally not very technical, which I LOVED – she said she prefers to work hard to make the material easy to understand & interesting (without sacrificing rigor), and referred people to read the papers for numbers. a++ this is also what I love to do <3. (convince people to be interested and that your work is obvious, not that you’re smart and your work is difficult)


### Interpretable machine learning & human-machine interaction (by [Been Kim](http://people.csail.mit.edu/beenkim/))


OMG. I’m trying really hard to make machine learning results more interpretable & debuggable at work (because people need to use the outputs of it!), and when she was like “that’s my research” I really wanted to be best friends.


She showed [this YouTube video](https://www.youtube.com/watch?v=8PwHigCDdW8&feature=youtu.be) of a system that automatically clusters students’ assignments and then shows you the ‘prototype’ assignments representing each segment! This seems really cool to me – if I were a teacher and had a system like this that worked well, I could imagine using this to get a sense for what kinds of solutions my students were using, and possibly even as an aid to grading.


She was also super pragmatic about her research! The metric she used to decide whether the interactive system was helpful or not was – did it cause the human to perform better on the classification task they were working on? All I want is to help humans do better work & save them time so this made me super happy. I think there’s a lot of room in ML to enable people and not just replace them.


### [Corinna Cortes](http://research.google.com/pubs/author121.html)


omg. She’s the head of Google Research NY. omg. She talked about how her team scrapes the web and tries to discover facts (like Barack Obama is married to Michelle Obama). This was an incredibly refreshing talk for me because instead of saying “well at Google we do magic”, the impression I got was “dude this stuff is really hard and involves a lot of really boring HTML and tables”. BUT IN THE END WE WON.


She talked about using interpretable models and how they manually look at examples where their algorithm isn’t performing well to decide where to focus their efforts. I asked her at the end how important good ML debugging tools were and she was like SO IMPORTANT IF YOU’RE NOT LOOKING AT YOUR DATA WHAT ARE YOU EVEN DOING. So now I’m even more motivated to build the random forest debugging tool I’ve been prototyping on the side.


I’ve been doing machine learning for ~3 years now and I still find it so hard, so it’s amazing to hear from someone’s an expert and talks honestly about how time-intensive building a good model is. I get really mad when people pretend that ML is easy or that if you’re smart you can just get good results like magic. </rant> :)


(sometimes ML really does work that way and the results are magical! those are the most fun days)
