---
title: "Birdcage liners"
date: 2018-01-12
url: https://www.joelonsoftware.com/2018/01/12/birdcage-liners/
word_count: 1497
---


My new year’s resolution was to give up on reading Twitter and Facebook.


I gave up on the feeds because they were making me angry. A lot of times I was angry because of politics, but even on non-political things, the feeds seemed like they were full of conflict and stress.


I can’t tell you how much happier I am without them. Am I the only one that hated reading feeds? Do they make everybody unhappy? And if they make people unhappy why are they so popular?


Since I design social software for a living I feel like I should have a professional opinion on why Twitter and Facebook made me unhappy.


Let’s start with Twitter. I used Twitter to keep in touch with friends and colleagues because I cared about them. Unfortunately, those friends mostly didn’t use Twitter to share happy news and tell me how things were going. They used Twitter for bumper sticker flame wars. These were not the thoughtful long essays on blogs of yesteryear. 140 characters is too short for that.


Here’s what happened with the 140 characters. You would start out having some kind of complicated thought. “Ya know, dogs are great and all? I love dogs! But sometimes they can be a little bit too friendly. They can get excited and jump on little kids and scare the bejesus out of them. They wag their tails so hard they knock things over. (PS not Huskies! Huskies are the cats of the dog world!)”


Ok, so now you try to post that on Twitter. And you edit and edit and you finally get it down to something that fits: “Dogs can be too friendly!”


All the nuance is lost. And this is where things go wrong. “@spolsky what about huskies? #dontforgethuskies”


Ten minutes later, “Boycott @stackoverflow. @spolsky proves again that tech bros hate huskies. #shame”


By the time you get off the plane in Africa you’re on the international pariah list and your @replies are full of people accusing you of throwing puppies out of moving cars for profit.


Yeah, I get it, this 140 character limitation was just a historical accident, and now it’s 280 characters anyway, and you can always make a Twitter Story, but the flame wars on Twitter emerged from the fact that we’ve taken a medium, text, which is already bad at conveying emotion and sentiment and high-bandwidth nuance, and made it even worse, and the net result is a lot of outrage and indignation.


The outrage and indignation, of course, are what makes it work. That’s what keeps you coming back. Oooh shade. Oooh flamewar. We rubberneckers can’t keep our eyes off of it. I don’t know what the original idea of Twitter was, but it succeeded because of natural selection. In a world where the tech industry was cranking out millions of dumb little social applications, this one happens to limit messages to 140 characters and that happens to create, unintentionally, a subtlety-free indignation machine, which is addictive as heck, so this is the one that survives and thrives and becomes a huge new engine of polarization and anger. It’s not a coincidence that we got a president who came to power through bumper-sticker slogans, outrageous false statements chosen to make people’s blood boil, and of course Twitter. This is all a part of a contagious disease that is spreading like crazy because we as a society have not figured out how to fight back yet.


But Twitter is small potatoes. Facebook is where the action is. Facebook quickly copied Twitter’s idea of the “feed” as a mechanism to keep you coming back compulsively. But whereas Twitter sort of stumbled upon addictiveness through the weird 140-character limit, Facebook mixed a new, super-potent active ingredient into their feed called Machine Learning. They basically said, “look, we are not going to show everybody every post,” and they used the new Midas-style power of machine learning and set it in the direction of getting people even more hyper-addicted to the feed. The only thing the ML algorithm was told to care about was addiction, or, as they called it, engagement. They had a big ol’ growth team that was trying different experiments and a raw algorithm that was deciding what to show everybody and the only thing it cared about was getting you to come back constantly.


Now, this algorithm, accidentally, learned something interesting—something that dog trainers have always known.


Dog trainers give dogs a treat when they get something right. When they say “come,” and the dog comes, he gets a treat. Woof. I can train any arbitrary dog to do that with some reliability. But here’s what happens. Once, just once, I forget to give the dog a treat. And then the dog thinks, well, heck this, I guess “come” doesn’t always mean “treat.” So the trained behavior goes away. It’s technically called extinction: the trained behavior goes extinct.


How do we prevent extinction? By only giving treats some of the time. So the dog learns something more subtle. When my master says come and I obey, I might get a treat. Sometimes I do, sometimes I don’t. That way, if I obey and don’t get the treat, I shouldn’t panic. I should still always come when he says come because that’s still the best way to get the most treats. Intermittent reinforcement works better.


This sounds like what Facebook was doing to me.


Rather than providing a constant stream of satisfying news and engagement with friends, Facebook’s algorithm had learned to give me a bunch of junk I didn’t need to hear, and only gave me intermittent rewards through the occasional useful nugget of information about friends. Once in a blue moon I would hear about a friend’s accomplishment or I would find out that someone I like is going to be in town. The rest of the time I would just get the kind of garbage newspaper clippings circulated by someone who had too much coffee and is misattributing the kick from the caffeine to something they just read online and now MUST share IMMEDIATELY with EVERYONE because this news story about something that happened to a baby bear is SOOOOO important to THE ENTIRE WORLD. And so 9 of out 10 things in my feed are complete garbage—last week’s newspaper lining the birdcage with the droppings already on it—but then once every two weeks I find out my niece is engaged or my best friend got a great new job or my oldest friend is in town and I should make plans to hang out. And now no matter how full the Facebook feed is of bird droppings I still have to keep going back.


Both Twitter and Facebook’s selfish algorithms, optimized solely for increasing the number of hours I spend on their services, are kind of destroying civil society at the same time. Researchers also discovered that the algorithms served to divide up the world into partisan groups. So even though I was following hundreds of people on social networks, I noticed that the political pieces which I saw were nevertheless directionally aligned with my own political beliefs. But to be honest they were much… shriller. Every day the Twitter told me about something that The Other Side did that was Outrageous and Awful (or, at least, this was reported), and everyone was screeching in sync and self-organizing in a lynch mob, and I would have to click LIKE or RETWEET just to feel like I had done something about it, but I hadn’t actually done anything about it. I had just slacktivated.


What is the lesson? The lesson here is that when you design software, you create the future.


If you’re designing software for a social network, the decision to limit message lengths, or the decision to use ML to maximize engagement, will have vast social impact which is often very hard to predict.


As software developers and designers, we have a responsibility to the world to think these things through carefully and design software that makes the world better, or, at least, no worse than it started out. And when our inventions spin out of control, we have a responsibility to understand why and to try to fix them.


This blog post has a surprise piece of good news. The good news is that Facebook suddenly realized what they had done, and today they [announced](https://www.facebook.com/zuck/posts/10104413015393571) a pretty major change of direction. They want the feed to leave people feeling “more connected and less lonely,” so they have actually decided to sacrifice “engagement.” Mark Zuckerberg posted, “By making these changes, I expect the time people spend on Facebook and some measures of engagement will go down. But I also expect the time you do spend on Facebook will be more valuable.” That’s amazing, but it’s amazing because it demonstrates that Facebook has finally grown up and joined the rest of us in understanding that software developers are designing the future.
