---
title: "When Writing Code Means You’ve Failed"
date: 2005-04-27
url: https://blog.codinghorror.com/when-writing-code-means-youve-failed/
slug: when-writing-code-means-youve-failed
word_count: 384
---

I was chatting with a fellow developer yesterday, who recently adopted the very cool [Busy Box ASP.NET progress indicator](https://web.archive.org/web/20060223203940/http://blogs.crsw.com/mark/archive/2005/02/16/737.aspx) that I recommended:


> *We often need to provide a user message informing the user that their request is “processing.” Like the hour-glass mouse pointer lets the Windows user know the system is busy processing their last request, I have a simple, clean, and effect solution to providing this on web pages: *[*The BusyBox Demo*](https://web.archive.org/web/20051001052246/http://blogs.crsw.com/mark/samples/BusyBoxDemo/Default.aspx)


He was quite pleased with the results, as their app has to churn through some HR queries that take in excess of 30 seconds even after hand optimization. The psychological [effect of a progress indicator](http://www.useit.com/papers/responsetime.html) is quite profound:


> *In cases where the computer cannot provide fairly immediate response, continuous feedback should be provided to the user in form of a percent-done indicator [Myers 1985]. As a rule of thumb, **percent-done progress indicators should be used for operations taking more than about 10 seconds.** Progress indicators have three main advantages: They reassure the user that the system has not crashed but is working on his or her problem; they indicate approximately how long the user can be expected to wait, thus allowing the user to do other activities during long waits; and they finally provide something for the user to look at, thus making the wait less painful. This latter advantage should not be underestimated and is one reason for recommending a graphic progress bar instead of just stating the expected remaining time in numbers.*


My Busy Box recommendation came after that team made several abortive attempts to implement different kinds of progress feedback. And this got me thinking: **sometimes, writing code means you’ve failed**. So much of what we do already exists, and in more mature, complete form. The real challenge in modern programming isn’t sitting down and writing a ton of code; it’s figuring out what existing code or frameworks you should be hooking together. This is also something [Scott Swigart has observed](http://swigartconsulting.blogs.com/tech_blender/2005/04/legos_and_glue.html):


> *Venkatarangan points out all the stuff that Sauce Reader uses, showing that in software development today, 1/2 the work is finding the building blocks, and the other 1/2 is writing the glue.*


The real development skill is **correctly identifying which half is Legos and which half is glue.**

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[progress indicators](https://blog.codinghorror.com/tag/progress-indicators/)
