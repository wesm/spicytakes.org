---
title: "The Joy of Deletion"
date: 2004-08-20
url: https://blog.codinghorror.com/the-joy-of-deletion/
slug: the-joy-of-deletion
word_count: 265
---

I generally dislike these kinds of “Me, too!” posts, but I have to make an exception for Ned Batchelder’s excellent [blog entry on deleting code](http://www.nedbatchelder.com/text/deleting-code.html?). I’ve often run into this phenomenon with other developers, and it bugged the heck out of me, although I couldn’t quantify exactly why. Well, now I can:

kg-card-begin: html

> If you have a chunk of code you don’t need any more, there’s one big reason to delete it for real rather than leaving it in a disabled state: to reduce noise and uncertainty. Some of the worst enemies a developer has are noise or uncertainty in his code, because they prevent him from working with it effectively in the future. 
>   A chunk of code in a disabled state just causes uncertainty. It puts questions in other developers’ minds: 
> Why did the code used to be this way?
> Why is this new way better?
> Are we going to switch back to the old way?
> How will we decide?
>  If the answer to one of these questions is important for people to know, then write a comment spelling it out. Don’t leave your co-workers guessing.

kg-card-end: html

I have been angrily accused of deleting someone’s commented code on more than one occasion. I say, give me a reason not to delete it, and I won’t. Otherwise, it’s fair game. In my experience this kind of “oh, I’ll get back to it” code just sits in the codebase forever, junking up the works for every future developer.

[code organization](https://blog.codinghorror.com/tag/code-organization/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
[code maintenance](https://blog.codinghorror.com/tag/code-maintenance/)
[technical debt](https://blog.codinghorror.com/tag/technical-debt/)
