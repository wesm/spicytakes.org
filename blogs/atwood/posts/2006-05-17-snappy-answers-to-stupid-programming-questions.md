---
title: "Snappy Answers to Stupid Programming Questions"
date: 2006-05-17
url: https://blog.codinghorror.com/snappy-answers-to-stupid-programming-questions/
slug: snappy-answers-to-stupid-programming-questions
word_count: 362
---

Here’s a not-so-gentle reminder from David Pickett that [some programming interview questions](https://web.archive.org/web/20060523055024/http://blogs.msdn.com/davidlem/archive/2006/05/16/598696.aspx) – in this case, “how would you write a routine to copy a file?” – are, well, [stupid](https://web.archive.org/web/20070704122624/http://exold.com/article/stupid-interview-questions):*


> Q. What about the attributes?
> A. Make the attributes the same.
> Q. Should I modify the attributes of the source file? If this file copy is part of a backup or archive operation, it’d probably be a mistake to leave the ‘Archive’ attribute on.
> A. No, leave them as-is.
> Q. What if the source file has the Archive attribute off? If I make it off on the new file as well, it could screw up the user’s backup software.
> A. Just make it the same. I don’t care about the user’s backup software.
> Q. Well, I’m not sure that’s the best approach to take when thinking about designing software FOR users, but if you say so.
> A. ...
> Q. What about compression? It’s a file attribute, but the copy destination may not support compression.
> A. Don’t compress the copy.
> Q. Even if the source is compressed, and the destination supports compression?
> A. YES.
> Q. What about encryption? What if the source file is encrypted, but the destination does not support encryption?
> A. Don’t encrypt the copy if the destination doesn’t support it.
> Q. Mmmmm, sorry, don’t mean to digress, but… that could be a serious security hole. Especially if wherever this file copy function ends up supports arbitrary parameters (directly or indirectly).
> A. **Look, just copy the damn file.**


“How would you write a routine to copy a file?” is just another [interview riddle](http://www.ocf.berkeley.edu/~wwu/riddles/intro.shtml); it doesn’t deserve a face value response. David’s answers are even better – they implode the question under its own weight.


![](https://blog.codinghorror.com/content/images/2025/05/image-284.png)


The only rational answer to “how would you write a routine to copy a file?” is another question: **why would any competent programmer ever write a file copy routine?**


The last time I checked, [moving mount Fuji](http://w-uh.com/articles/030524-moving_Mount_Fuji.html) wasn’t a part of our business plan, either.


*With apologies to Al Jaffee.

[interview questions](https://blog.codinghorror.com/tag/interview-questions/)
[programming interview](https://blog.codinghorror.com/tag/programming-interview/)
[software design](https://blog.codinghorror.com/tag/software-design/)
[file attributes](https://blog.codinghorror.com/tag/file-attributes/)
[software development](https://blog.codinghorror.com/tag/software-development/)
