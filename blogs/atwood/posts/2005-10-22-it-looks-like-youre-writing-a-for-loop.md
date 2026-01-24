---
title: "It looks like you’re writing a for loop!"
date: 2005-10-22
url: https://blog.codinghorror.com/it-looks-like-youre-writing-a-for-loop/
slug: it-looks-like-youre-writing-a-for-loop
word_count: 363
---

Even the best programmers [make shitty software, with bugs](https://blog.codinghorror.com/we-make-shitty-software-with-bugs/). But **some programmers are naturally proficient at creating this special kind of software**, as illustrated by a [Croatian developer known as Stinky:](https://web.archive.org/web/20060105132405/http://www.sampioni.com/en/Legenda/stinky.htm)

kg-card-begin: html

> *
> The anecdote that best reveals how little Stinky knew about programming started when he asked Bojan to help him solve the following problem:
> “I have a function that returns Boolean value. Well, I would like to call that function and store the opposite value in some variable. I could code it like this: If function = true Then variable = false Else variable = true. But I have a feeling that it can be even simpler than that. Can you tell me how?”
> After Bojan recovered from the shock of realizing that Stinky didn’t know the basics of logical algebra, he replied that it was enough to put variable = Not function. Stinky went to check it out and after few minutes he cheerfully shouted: “It works!”. Bartol was a witness to the whole scene. A few moments later he said to Bojan, “You see, my friend, to hell with education, your degree in computer science and the tons of books you read. You don’t need any of that to be a champion developer like Stinky. Just learn the copy-paste method, remember all the properties of Janus Gridex and ActiveBar control, and the world is yours.”
> *

kg-card-end: html

Sure, Microsoft’s [Office Assistant](http://en.wikipedia.org/wiki/Clippy), Clippy, gets a lot of flak – but wouldn’t it be nice if Clippy could assist Stinky with his code?


![](https://blog.codinghorror.com/content/images/2025/03/image-335.png)


Or, if the IDE could detect this kind of code as it’s being typed and offer some helpful advice* to Stinky?


![](https://blog.codinghorror.com/content/images/2025/03/image-334.png)


VS.NET 2005 also offers just-in-time intellisense for exceptions, which can be customized by [editing the underlying XML](http://odetocode.com/Blogs/scott/archive/2005/09/14/2201.aspx). The intellisense for a NullReferenceException isn’t very helpful for a developer like Stinky; here’s one way K. Scott Allen improved it:


![](https://blog.codinghorror.com/content/images/2025/03/image-333.png)


*Despite extensive use of my google-fu, I couldn’t find the original source of this image. If anyone knows who originally created it, let me know so I can attribute it properly.

[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
[logical algebra](https://blog.codinghorror.com/tag/logical-algebra/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
