---
title: "There Ain’t No Such Thing as the Fastest Code"
date: 2008-02-19
url: https://blog.codinghorror.com/there-aint-no-such-thing-as-the-fastest-code/
slug: there-aint-no-such-thing-as-the-fastest-code
word_count: 920
---

I was tickled to see that James Hague chose [The Zen of Assembly Language Programming](http://www.amazon.com/exec/obidos/ASIN/0673386023) as one of [five memorable books about programming](http://prog21.dadgum.com/19.html). I wholeheartedly agree. Even if you **never plan to touch a lick of assembly code in your entire professional career**, this book is a fantastic and thoroughly useful read. I was a mere *Visual Basic* programmer when I found this book (along with [The Zen of Code Optimization](http://www.amazon.com/exec/obidos/ASIN/1883577039)), picked it up on a lark, and I could barely put it down. It’s that good.


Abrash isn’t just [a seminal figure](http://en.wikipedia.org/wiki/Michael_Abrash) in the software engineering community, he’s also one of the best technical writers you’ll ever find. That’s why he’s one of [my programming heroes](https://blog.codinghorror.com/on-managed-code-performance/), directly alongside Steve McConnell.


His [Graphics Programming Black Book](http://www.amazon.com/exec/obidos/ASIN/1576101746) is similarly great, and covers topics so general and wide ranging that the title becomes a bit of a misnomer. Best of all, it’s [available online for free](https://web.archive.org/web/20080304111943/http://www.byte.com/abrash/) courtesy of Byte, so you can sample it yourself.


![](https://blog.codinghorror.com/content/images/2025/04/image-1.png)


I know what you’re thinking. “This book is about graphics. And assembly language. Plus it’s from, like, 1996, which is approximately 1928 in computer years. It’s of no interest to me as a programmer.” Admit it. You are. But you know what you’re going to do? You’re going to click through anyway and read some of it. Just like in college, **the class topic doesn’t matter when the instructor is a brilliant teacher**. And that’s exactly what Abrash is.


Abrash is a world class coder and technical writer, but he’s also not shy about explaining the perils and dangers of our craft, including **the biggest problem of all – the one that sits behind the keyboard**. Allow me to illustrate with one of my very favorite Abrash passages, from Chapter 16 of the Graphics Programming Black Book.


> Not so long ago, Terje Mathisen, who I introduced earlier in this book, wrote a very fast word-counting program, and posted it on [BIX](http://en.wikipedia.org/wiki/Byte_Information_Exchange). When I say it was fast, I mean *fast*; this code was optimized like nobody’s business. We’re talking top-quality code here.
> When the topic of optimizing came up in one of the BIX conferences, Terje’s program was mentioned, and he posted the following message: “I challenge BIXens (and especially mabrash!) to speed it up significantly. I would consider 5 percent a good result.” The clear implication was, “That code is as fast as it can possibly be.”
> Naturally, it wasn’t; there ain’t no such thing as the fastest code (TANSTATFC? I agree, it doesn’t have the ring of TANSTAAFL).
> [assembly language tricks and useful optimization approaches elided – [see PDF](https://web.archive.org/web/20081115161315/http://www.byte.com/abrash/chapters/gpbb16.pdf) for full detail]
> The biggest optimization barrier that Terje faced was that **he thought he had the fastest code possible**. Once he opened up the possibility that there were faster approaches, and looked beyond the specific approach that he had so carefully optimized, he was able to come up with code that was a lot faster. Consider the incongruity of Terje’s willingness to consider a 5 percent speedup significant in light of his later **near-doubling of performance**.


In the same chapter, Mr. Abrash relates a similar anecdote based on a word counting program. It was published as a challenge in his “Pushing the Envelope” column:


> That initial challenge was sparked by a column David Gerrold wrote concerning the matter of counting the number of words in a document; David turned up some pretty interesting optimization issues along the way. David did all his coding in Pascal, pointing out that while an assembly language version would probably be faster, his Pascal utility worked properly and was fast enough for him.
> It wasn’t, however, fast enough for me. The logical starting place for speeding up word counting would be David’s original Pascal code, but I’m much more comfortable with C, [so I created] a loose approximation of David’s word count program, translated to C.


Mike proceeds to do what he does best – optimize the word count program into assembly and explain along the way in an easy going, highly articulate way. His results are as follows:

kg-card-begin: html


| C conversion | 4.6 sec |
| C + assembly conversion | 2.4 sec |
| C + assembly conversion with lookup table | 1.6 sec |


kg-card-end: html

He then posted his program as a challenge for readers of PC Techniques-- **can this optimized assembly word count program, from an acclaimed industry expert on assembly optimization, be made even *faster*?** Well, I think you can guess what happened next.


> So how did the entrants in this particular challenge stack up? More than one claimed a speed-up over my assembly word-counting code of more than three times. On top of the three-times speedup over the original C code that I had already realized, we’re almost up to **an order of magnitude faster**. You are, of course, entitled to your own opinion, but *I* consider an order of magnitude to be significant.
> Truth to tell, I didn’t expect a three-times speedup; around two times was what I had in mind. Which just goes to show that any code can be made faster than you’d expect, if you think about it long enough and from many different perspectives.


Like Mike said, *there ain’t no such thing as the fastest code*. If you think there is, *you’re* probably the barrier standing in the way of further performance, not the code itself.

[assembly language](https://blog.codinghorror.com/tag/assembly-language/)
[code optimization](https://blog.codinghorror.com/tag/code-optimization/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
[technical writing](https://blog.codinghorror.com/tag/technical-writing/)
[graphics programming](https://blog.codinghorror.com/tag/graphics-programming/)
