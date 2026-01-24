---
title: "Nobody Cares What Your Code Looks Like"
date: 2007-12-18
url: https://blog.codinghorror.com/nobody-cares-what-your-code-looks-like/
slug: nobody-cares-what-your-code-looks-like
word_count: 900
---

In [The Problems of Perl](http://avatraxiom.livejournal.com/58084.html): The Future of Bugzilla, Max Kanat-Alexander* laments the state of the Bugzilla codebase:


> Once upon a time, [Bugzilla](http://www.bugzilla.org/) was an internal application at Netscape, written in TCL. When it was open-sourced in 1998, Terry (the original programmer), decided to re-write Bugzilla in Perl. My understanding is that he re-wrote it in Perl because a lot of system administrators know Perl, so that would make it easier to get contributors.
> In 1998, there were few advanced, object-oriented web scripting languages. In fact, Perl was pretty much it. PHP was at version 3.0, python was at version 1.5, Java was just starting to become well-known, ruby was almost unheard of, and some people were still writing their CGI scripts in C or C++.
> Perl has many great features, most of all the number of libraries available and the extreme flexibility of the language. However, Perl would not be my first choice for writing or maintaining a large project such as Bugzilla. The same flexibility that makes Perl so powerful makes it very difficult to enforce code quality standards or to implement modern object-oriented designs.
> Since 1998 there have been many advances in programming languages. PHP has decent object-oriented features, python has many libraries and excellent syntax, Java has matured a lot, and Ruby is coming up in the world quickly. **Nowadays, almost all of our competitors have one advantage: they are not written in Perl.** They can actually develop features more quickly than we can, not because of the number of contributors they have, but because the language they’re using allows it. There are at least two bug-trackers that I can think of off the top of my head that didn’t even exist in 1998 and were developed rapidly up to a point where they could compete with Bugzilla.
> In 1998, Perl was the right choice for a language to re-write Bugzilla in. In 2007, though, having worked with Perl extensively for years on the Bugzilla project, Id say the language itself is our greatest hindrance. Without taking some action, I’m not sure how many more years Bugzilla can stay alive as a product. Currently, our popularity is actually *increasing*, as far as I can see. So we shouldn’t abandon what we’re doing now. But I’m seeing more and more products come into the bug-tracking arena, and I’m not sure that we can stay competitive for more than a few more years if we stick with Perl.


It’s a credit to Max that he cares enough about the future of his work to surface these important issues. Perhaps it would make sense to rewrite Bugzilla in a friendlier, [more modern language](http://wiki.mozilla.org/Bugzilla:Languages).


Neither Perl nor the circa-1998 Bugzilla codebase have aged particularly well over the last 10 years. I don’t think Bugzilla is anyone’s favorite bug tracking product. It is utilitarian bordering on downright ugly. But – and here’s the important part – *Bugzilla works*. It’s actively used today by some of the largest and most famous open source projects on the planet, including the [Linux Kernel](http://bugzilla.kernel.org/), [Mozilla](https://bugzilla.mozilla.org/), [Apache](http://issues.apache.org/bugzilla/), and [many others](http://www.bugzilla.org/installation-list/).


I have a friend who works for an extremely popular open source database company, and he says their code is some of the absolute worst he’s ever seen. This particular friend of mine is no stranger to bad code – he’s been in a position to see some *horrifically* bad codebases. Adoption of this open source database isn’t slowing in the least because their codebase happens to be poorly written and difficult to troubleshoot and maintain. **Users couldn’t care less whether the underlying code is pretty.** All they care about is whether or not it *works*. And it must work – otherwise, why would all these people all over the world be running their businesses on it?


I gave Joel Spolsky a hard time for his [Wasabi language boondoggle](https://blog.codinghorror.com/has-joel-spolsky-jumped-the-shark/), but I’m now reconsidering that stance. Fog Creek Software isn’t funded by the admiration of other programmers. It’s funded by selling their software to customers. And to the customer, [the user interface is the application](https://blog.codinghorror.com/the-user-interface-is-the-application/). I might point and laugh at an application written in some crazy hand rolled in-house language. But language choice is completely invisible to potential customers. As long as the customers are happy with the delivered application and sales are solid, who gives a damn what I – or any other programmers, for that matter – think?


Sure, we programmers are paid to care what the code looks like. We worry about the guts of our applications. It’s our job. We *want* to write code in friendly, modern languages that make our work easier and less error-prone. We’d *love* any opportunity to geek out and rewrite everything in the newest, sexiest possible language. It’s all perfectly natural.


The next time you’re knee deep in arcane language geekery, remember this: **nobody cares what your code looks like**. Except for us programmers. Yes, well-factored code written in a modern language is a laudable goal. But perhaps we should also focus a bit more on things the customer will see and care about, and less on the things they *never* will.


*I desperately want to provide full name attribution here, but I was unable to find Max’s last name on any of his pages – which drives me absolutely bonkers ([see #3](https://blog.codinghorror.com/thirteen-blog-cliches/)).

[perl](https://blog.codinghorror.com/tag/perl/)
[bugzilla](https://blog.codinghorror.com/tag/bugzilla/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
