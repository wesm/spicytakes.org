---
title: "Google is the Help Menu"
date: 2006-01-26
url: https://blog.codinghorror.com/google-is-the-help-menu/
slug: google-is-the-help-menu
word_count: 855
---

Jensen Harris recently cited some Microsoft Office usability research which produced a rather [counter-intuitive result](https://web.archive.org/web/20060205171439/http://blogs.msdn.com/jensenh/archive/2005/11/29/497861.aspx):


> One of the most interesting epiphanies I’ve had over the last few years seems on the surface like a paradox: “help” in Office is mostly used by experts and enthusiasts.
> How can this be? I think my biased assumption was that experts know how to use the software already and eager novices would be poring over the documentation trying to learn how to be more effective using it.
> Yet, **in usability tests we see it again and again: novices and intermediates click around and experiment, experts try to reason things out and look them up in help**.


Dispelling myths based on actual usability data. I love it. Jensen offers a few potential explanations for this phenomenon:

- Only experts know the right “magic words” to search for.
- Users need a broader scope of help: not a recipe, but a community college course in cooking.
- Help requires a context switch – it’s difficult to look at help side-by-side with the software.


While there’s definitely merit to these observations, Jensen misses the biggest one. You need only read through a few of the many post comments to see what it is:


> It’s been my experience that Office help often doesn’t include anything useful, so I don’t use it. For example, I was using Access and somehow became aware of the DoCmd object. It seemed like it would do what I want, but there is no help for it. How could this object with 100 different features have no online help? Luckily Google came to the rescue, pointing me directly to the microsoft.com page telling me all about it. Why wasn’t the included in the help originally?
> I once found an Excel function in the help that required I install one of the add-in tools to use it, but the help didn’t mention this add-in at all. So I did a google search and found out what I needed to do to use this function.
> I have to agree that the online help in Office is not the best. It is a great product, but when I need help I usually give up after examining the first 50 hits and the move directly to Google.
> Regarding relevance, I would suggest adopting Google’s algorithms for ranking. A Google search for “Excel operators” yields what I was looking for (“About calculation operators”) as the second hit from Microsoft, with another relevant document (differences between 1-2-3 and Excel operators) being first. Excel 2002’s help gives rankings 4 and 14 respectively, with most of the other hits having nothing whatsoever to do with operators.
> I practically never use online help. However, I literally live and die by Google Groups. I am almost never the only person to encounter a problem or misunderstand a feature and Google Groups usually proves a much faster route to success.
> I have stopped using help in Office and just rely on Google. The replies are more relevant and better sorted, and it’s faster. Even if the answer turns out to reside on the Office Assistance site, it’s easier to find it there with Google.


It seems to me that the best “help file” for your software is **no help file at all**. It’s a Google MSN Search query.


Local help simply can’t compete with internet search. I'll go even further – **if you are building local help files for your application, you’re wasting your time.** And more importantly, you are wasting your users’ time.


Smart developers will stop wasting time on useless local help and **build community around their product on the internet**. One of my favorite examples of this is [http://www.regular-expressions.info](http://www.regular-expressions.info/). It’s the top hit for a Google search on the term “regular expressions”. The author, Jan Goyvaerts, is also the author of [RegexBuddy](http://www.regexbuddy.com), a fantastic regular expression tool. The tool is great, but when I need help with my regular expressions, I don’t bother with the local help file. I just type what I’m looking for into MSN Search and bring the full weight of billions of dollars of search optimization to bear on the entire internet. If I happen to be offline, Jan has thoughtfully provided both PDF and CHM versions of the content on regular-expressions.info.


Local help seems rather quaint in comparison.


This kind of online community can easily be linked from the UI, too. One of the few generally helpful “help” features is contextual point-and-help – e.g. clicking on a “what the heck does this do?” button. But even those should spawn generic search engine queries to be truly useful.


If you really want to help your users, set up a wiki for your product. Set up forums for them to participate in. Become an impartial nexus for all information related to your product, whether your company wrote it or not. And most importantly, *have the guts to give your users control over these sites*. You may have written it, but they have to live with it.

[usability](https://blog.codinghorror.com/tag/usability/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
