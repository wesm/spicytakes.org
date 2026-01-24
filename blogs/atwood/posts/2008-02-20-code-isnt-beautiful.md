---
title: "Code Isn’t Beautiful"
date: 2008-02-20
url: https://blog.codinghorror.com/code-isnt-beautiful/
slug: code-isnt-beautiful
word_count: 875
---

I was thrilled to see the book [Beautiful Code:](http://www.amazon.com/exec/obidos/ASIN/0596510047) Leading Programmers Explain How They Think show up in my Amazon recommendations. It seems like exactly the type of book I would enjoy. So of course I bought a copy.


![](https://blog.codinghorror.com/content/images/2025/04/image-2.png)


Unfortunately, Beautiful Code wasn’t nearly as enjoyable of a read as I had hoped it would be. It is by no means a *bad* book, but there’s something about it that’s not quite right.


Part of the problem is that it’s a compilation of disconnected essays, much like [The Best Software Writing I](https://blog.codinghorror.com/show-dont-tell/). Because there are [thirty-three different authors](https://web.archive.org/web/20080312004809/http://www.oreilly.com/catalog/9780596510046/toc.html), there’s naturally going to be a lot of variance in tone, content, and quality. How you feel about the book is largely dictated by how much you like the individual essays. There’s certainly no lack of quality in the authors. There are plenty of famous, highly regarded programmers represented here: Brian Kernighan, Yukihiro Matsumoto, Jon Bentley, Charles Petzold, and many others.


Despite all that, I loved The Best Software Writing; why can’t I love Beautiful Code? I wasn’t able to put my finger on exactly what the deeper problem was with Beautiful Code until I read [this eloquent reader review](https://web.archive.org/web/20080228083635/http://www.amazon.com/review/R1W0YZZWT53Y9M/ref=cm_cr_rdp_perm) from Dmitry Dvoinikov. I suddenly realized what ultimately trips up Beautiful Code. It was right there in front of me, all along. It’s even in the title: **Code**.

kg-card-begin: html

> With rare exception, the authors don’t even mention the word “beautiful” in their essays. They allude with “There, we have this system, it works like this.” What exactly the author finds beautiful about it, and why, remains a secret.
> The chapter written by Yukihiro Matsumoto, the creator of Ruby, was the most impressive standout. It is three pages in which he simply writes about what he believes beautiful code is. He explains his understanding of beautiful code to you. This is what the book should be!
> Instead, **many chapters just reprint a few pages of code and conclude – see, it is beautiful!**
> Many times I was unable to grasp the problem – what was it that required that so-called beauty to emerge? I couldn’t see the whole picture, but the authors presume I do. Any possible appreciation of beauty requires deep understanding. What if I show you a magnified fragment of Mona Lisa’s background, an area of 3x3 blackish pixels? No doubt Leonardo had to paint them too. But where is the beauty?
> Only a few authors were wise enough to use pseudocode, something that anyone can read, no matter from which camp. It’s just weird when the authors present their beatiful code in Ruby or Perl or Lisp. Look, I haven’t touched Ruby yet, I hate Perl and I can’t imagine using Lisp in practice. Nevertheless the authors repeatedly say something like "It’s easy, I’ll show you, this bracket does this and that character does something else. *Now* do you see how beautiful it is?" **They literally show you a piece of poetry in a foreign language and ask you to appreciate it.**
> A classical example of awful poetry in Russian is (transliterated)
> *Ya poet, zovus’ Neznajka,
> ot menya vam balalajka.*
> Can you tell whether this is good or bad and why? What if I told you it’s beautiful? Would you believe? Does it appeal to your sense of beauty?

kg-card-end: html

Ideas are beautiful. Algorithms are beautiful. Well executed ideas and algorithms are even more beautiful. But the code itself is not beautiful. **The beauty of code lies in the architecture, the ideas, the grander algorithms and strategies that code *represents*.** The code samples presented are indeed clear, readable, and well written. But they are weak evidence of beauty; it’s not the language that is inherently beautiful. Barroom doggerel expressed in French or Russian is never automatically elevated to the level of poetry.


So when the Beautiful Code authors proffer pages of code – real live production code – and ask us to see the beauty, the code doesn’t help. It gets in the way.


> It’s been a long time since I found *dst++ = *src++ beautiful.


Focusing on the code is exactly the wrong approach. It’s like a detailed technical description of the paints, brushes, and techniques used to paint the [Mona Lisa](http://en.wikipedia.org/wiki/Mona_Lisa), without any of the historical or artistic context that makes it such an important painting.


**Can’t we expect readers to see past the language?** I’d ask the very same question of the authors. So many of them got mired in the minute details of the code and language that they never got around to the "why" underneath – the beautiful ideas and concepts that code represents. I’d also ask the same question of every working programmer today. **I can scarcely post any code snippets in Visual Basic today without a slew of comments complaining about how awfully horrible Basic syntax is**, how their eyes are bleeding, it’s unreadable, the horrors of End If versus curly brackets, etcetera, etcetera, ad nauseam. Never mind the language – what about the underlying algorithmic concept I am trying to represent in code? How does *that* look?


Apparently, for many of us, beauty really *is* skin deep.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
