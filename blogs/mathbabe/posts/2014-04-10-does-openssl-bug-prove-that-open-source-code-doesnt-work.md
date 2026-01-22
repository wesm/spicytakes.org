---
title: "Does OpenSSL bug prove that open source code doesn’t work?"
date: 2014-04-10
url: https://mathbabe.org/2014/04/10/does-openssl-bug-prove-that-open-source-code-doesnt-work/
word_count: 456
---


By now most of you have read about the major bug that was found in OpenSSL, an open source security software toolkit. The bug itself is called the Heartbleed Bug, and there’s lots of information about it and how to fix it [here](http://heartbleed.com/). People are super upset about this, and lots of questions remain.


For example, was it intentionally undermined? Has the [NSA deliberately inserted weaknesses](http://www.nytimes.com/2013/09/06/us/nsa-foils-much-internet-encryption.html?pagewanted=all) into this as well? It seems like the [jury is out right now](https://www.schneier.com/blog/archives/2014/04/heartbleed.html), but if I’m the guy who put in the bug, I’m changing my name and going undercover just in case.


Next, how widely was the weakness exploited? If you’re super worried about stuff, or if you are a particular target of attack, the answer is probably “widely.” The frustrating thing is that there’s seemingly no way to measure or test that assumption, since the [attackers would leave no trace](http://mashable.com/2014/04/09/heartbleed-what-to-do/).


Here’s what I find interesting the most interesting question: what will the long-term reaction be to open source software? People might think that open source code is a bust after this. They will complain that something like this should never have been allowed to happen – that *the whole point of open software* is that people should be checking this stuff as it comes in – and it never would have happened if there were people getting paid to test the software.


First of all, it *did work as intended*, even though it took two years instead of two days like people might have wanted. And maybe [this shouldn’t have happened](https://news.ycombinator.com/item?id=7549888) like it did, but I suspect that people will learn this particular lesson really well as of now.


But in general terms, bugs are everywhere. Think about [Knight Capital’s trading debacle](http://online.wsj.com/news/articles/SB10000872396390443866404577564772083961412) or the ObamaCare website, just two famous recent problems with large-scale coding projects that aren’t open source.


Even when people are paid to fix bugs, they fix the kind of bugs that cause the software to stop a lot sooner than the kind of bug that doesn’t make anything explode, lets people see information they shouldn’t see, and leaves no trace. So for every Knight’s Capital there are tons of other bugs in software that continue to exist.


In other words it’s more a question of who knows about the bugs and who can exploit them. And of course, whether those weaknesses will ever be exposed to the public at all.


It would be great to see the OpenSSL bug story become, over time, a success story. This would mean that, on the one hand the nerds becoming more vigilant in checking vitally important code, and learning to think like assholes, but also the public would need to acknowledge how freaking hard it is to program.
