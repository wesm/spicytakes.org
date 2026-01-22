---
title: "Finance and open source"
date: 2013-08-11
url: https://mathbabe.org/2013/08/11/finance-and-open-source/
word_count: 1230
---


I want to bring up two quick topics this morning I’ve been mulling over lately which are both related to [this recent post](http://rajivsethi.blogspot.com/2013/08/the-spider-and-fly.html) by Economist [Rajiv Sethi](http://www.columbia.edu/~rs328/) from Barnard (h/t Suresh Naidu), who happened to be my assigned faculty mentor when I was an assistant prof there. I have mostly questions and few answers right now.


In his post, Sethi talks about former computer nerd for Goldman Sachs Sergey Aleynikov and his trial, which was [chronicled by Michael Lewis recently](http://www.vanityfair.com/business/2013/09/michael-lewis-goldman-sachs-programmer). See also [this related interview](http://www.vanityfair.com/online/daily/2013/08/michael-lewis-on-goldman-sachs-programmer) with Lewis, h/t Chris Wiggins.


I haven’t read Lewis’s piece yet, only his interview and Sethi’s reaction. But I can tell it’ll be juicy and fun, as Lewis usually is. He’s got a way with words and he’s bloodthirsty, always an entertaining combination.


So, the two topics.


First off, let’s talk a bit about high frequency trading, or HFT. My first two questions are, who does HFT benefit and what does HFT cost? For both of these, there’s the easy answer and then there’s the hard answer.


Easy answer for HFT benefitting someone: primarily the people who make loads of money off of it, including the hardware industry and the people who get paid to drill through mountains with cables to make connections between Chicago and New York faster.


Secondarily, market participants whose fees have been lowered because of the tight market-making brought about by HFT, although that savings may be partially undone by the way HFT’ers operate to pick off “dumb money” participants. After all, you say market making, I say arbing. Sorting out the winners, especially when you consider times of “extreme market conditions”, is where it gets hard.


Easy answer for the *costs* of HFT is for the companies that invest in IT and infrastructure and people to do the work, although to be sure they wouldn’t be willing to make that investment if they didn’t expect it to pay off.


A harder and more complete answer would involve how much risk we take on as a society when we build black boxes that we don’t understand and let them collide with each other with our money, as well as possibly a guess at what those people and resources now doing HFT might be doing otherwise.


And that brings me to my second topic, namely the interaction between the open source community and the finance community, but mostly the HFTers.


Sethi said it well (Cathy: see bottom of this for an update) this way in his post:


> Aleynikov relied routinely on open-source code, which he modified and improved to meet the needs of the company. It is customary, if not mandatory(Cathy: see bottom of this for an update) for these improvements to be released back into the public domain for use by others. But his attempts to do so were blocked:


> Serge quickly discovered, to his surprise, that Goldman had a one-way relationship with open source. They took huge amounts of free software off the Web, but they did not return it after he had modified it, even when his modifications were very slight and of general rather than financial use. “Once I took some open-source components, repackaged them to come up with a component that was not even used at Goldman Sachs,” he says. “It was basically a way to make two computers look like one, so if one went down the other could jump in and perform the task.” He described the pleasure of his innovation this way: “It created something out of chaos. When you create something out of chaos, essentially, you reduce the entropy in the world.” He went to his boss, a fellow named Adam Schlesinger, and asked if he could release it back into open source, as was his inclination. “He said it was now Goldman’s property,” recalls Serge. “He was quite tense. When I mentioned it, it was very close to bonus time. And he didn’t want any disturbances.”


This resonates with my experience at D.E. Shaw. We used lots of python stuff, and as a community were working at the edges of its capabilities (not me, I didn’t do fancy HFT stuff, my models worked at a much longer time frame of at least a few hours between trades).


The urge to give back to the OS community was largely thwarted, when it came up at all, because there was a fear, or at least an argument, that somehow our competition would use it against us, to eliminate our edge, even if it was an invention or tool completely sanitized from the actual financial algorithm at hand.


A few caveats: First, I do think that stuff, i.e. python technology and the like *eventually* gets out to the open source domain even if people are consistently thwarting it. But it’s incredibly slow compared to what you might expect.


Second, It might be the case that python developers working outside of finance are actually much better at developing good tools for python, especially if they have some interaction with finance but don’t work inside. I’m guessing this because, as a modeler, you have a very selfish outlook and only want to develop tools for your particular situation. In other words, you might have some really weird looking tools if you did see a bunch coming from finance.


Finally, I think I should mention that quite a few people I knew at D.E. Shaw have now left and are actively contributing to the open source community now. So it’s a lagged contribution but a contribution nonetheless, which is nice to see.


Update: from my Facebook page, a discussion of the “mandatoriness” of giving back to the OS community from my brother Eugene O’Neil,  super nerd, and friend William Stein, other super nerd:


**Eugene O’Neil:** the GPL says that if you give someone a binary executable compiled with GPL source code, you also have to provide them free access to all the source code used to generate that binary, under the terms of the GPL. This makes the commercial sale of GPL binaries without source code illegal. However, if you DON’T give anyone outside your organization a binary, you are not legally required to give them the modified source code for the binary you didn’t give them. That being said, any company policy that tries to explicitly PROHIBIT employees from redistributing modified GPL code is in a legal gray area: the loophole works best if you completely trust everyone who has the modified code to simply not want to distribute it.


**William Stein:** Eugene — You are absolutely right. The “mandatory” part of the quote: “It is customary, if not mandatory, for these improvements to be released back into the public domain for use by others.” from Cathy’s article is misleading. I frequently get asked about this sort of thing (because of people using Sage ([http://sagemath.org](http://sagemath.org/)) for web backends, trading, etc.). I’m not aware of any popular open source license that make it mandatory to give back changes if you use a project internally in an organization (let alone the GPL, which definitely doesn’t). The closest is AGPL, which involves external use for a website. Cathy — you might consider changing “Sethi said it well…”, since I think his quote is misleading at best. I’m personally aware of quite a few people that do use Sage right now who wouldn’t otherwise if Sethi’s statement were correct.
