---
title: "Markov and You"
date: 2008-06-11
url: https://blog.codinghorror.com/markov-and-you/
slug: markov-and-you
word_count: 1195
---

In [Finally, a Definition of Programming I Can Actually Understand](https://blog.codinghorror.com/finally-a-definition-of-programming-i-can-actually-understand/) I marveled at particularly strange and wonderful comment left on this blog. Some commenters wondered if that comment was generated through [Markov chains](http://en.wikipedia.org/wiki/Markov_chain). I considered that, but I had a hard time imagining a text corpus input that could possibly produce output so profoundly weird.


So **what are these Markov chains** we’re talking about?


One example of Markov chains in action is [Garkov](http://joshmillard.com/garkov/), where the long running [Garfield](http://en.wikipedia.org/wiki/Garfield) cartoon strip meets Markov chains. I present below, for your mild amusement, two representative strips I found on the [Garkov hall of fame](https://web.archive.org/web/20080620142918/http://joshmillard.com/garkov/famehall.cgi):


![](https://blog.codinghorror.com/content/images/2025/04/image-140.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-139.png)


Garfield’s an easy target, though:

- [Garfield Minus Garfield](http://garfieldminusgarfield.net/). What it says on the tin. Surprisingly cathartic.
- [Lasagna Cat](http://www.lasagnacat.com/). Almost indescribably strange live action recreations of Garfield strips. If you only click one link in this post, make it this one. Sanity optional.
- [Garfield Variations](https://web.archive.org/web/20080701055543/http://www.garfieldvariations.com/). Hand-drawn versions of Garfield in underground “comix” style, usually on paper napkins.
- [Barfield](http://www.thereverend.com/barfield/index.html). Garfield strips subtly modified to include amusing bodily functions.
- [Permanent Monday](http://permanent-monday.blogspot.com/). Literary commentary on selected strips.
- [Arbuckle](http://www.tailsteak.com/arbuckle/). Strips faithfully redrawn by random internet “artists,” with one dramatic twist: Jon can’t actually *hear* Garfield, because he is, after all, a cat.
- [Garfield Randomizer](https://web.archive.org/web/20080615215844/http://www.dougshaw.com/garfield.html). Sadly defunct – combined random panels to form “new” Garfield strips.


So let’s proceed to the “kov” part of Garkov. The best description of Markov chains I’ve ever read is in [chapter 15](https://web.archive.org/web/20080513071917/http://www.cs.bell-labs.com/cm/cs/pearls/strings.html) of [Programming Pearls](http://www.amazon.com/exec/obidos/ASIN/0201657880):

kg-card-begin: html

> A generator can make more interesting text by making each letter a random function of its predecessor. We could, therefore, read a sample text and count how many times every letter follows an A, how many times they follow a B, and so on for each letter of the alphabet. When we write the random text, we produce the next letter as a random function of the current letter. The Order-1 text was made by exactly this scheme:
> **t I amy, vin. id wht omanly heay atuss n macon aresethe hired boutwhe t, tl, ad torurest t plur I wit hengamind tarer-plarody thishand.**
> We can extend this idea to longer sequences of letters. The order-2 text was made by generating each letter as a function of the two letters preceding it (a letter pair is often called a digram). The digram TH, for instance, is often followed in English by the vowels A, E, I, O, U and Y, less frequently by R and W, and rarely by other letters.
> **Ther I the heingoind of-pleat, blur it dwere wing waske hat trooss. Yout lar on wassing, an sit.” “Yould,” “I that vide was nots ther.**
> The order-3 text is built by choosing the next letter as a function of the three previous letters (a trigram).
> **I has them the saw the secorrow. And wintails on my my ent, thinks, fore voyager lanated the been elsed helder was of him a very free bottlemarkable,**
> By the time we get to the order-4 text, most words are English, and you might not be surprised to learn that it was generated from a Sherlock Holmes story ( [“The Adventure of Abbey Grange”](http://sherlock-holmes.classic-literature.co.uk/the-adventure-of-the-abbey-grange/)).
> **His heard.” “Exactly he very glad trouble, and by Hopkins! That it on of the who difficentralia. He rushed likely?” “Blood night that.**

kg-card-end: html

So the text in Garkov strips is generated in exactly this way, but using words instead of letters. The input corpus is, as you’d expect, the text of many old Garfield strips.


What’s amazing to me about Markov chains is how unbelievably *simple* they are. A Markov chain has no memory of previous states: the next state (word, in our case) is chosen based on a random dice roll and a lookup into a table of the states that tend to historically follow the current state in the input corpus. Given an adequate input corpus, they work almost uncannily well, a testament to the broad power of rudimentary statistical inference. Garfield’s been around since 1978, and still going str... well, going, so there’s no shortage of material to work with.


Now let’s try it ourselves. I fed the text of the last twelve [Paul Graham essays](http://www.paulgraham.com/articles.html) to [this online Markov generator](https://web.archive.org/web/20080624034742/http://www.beetleinabox.com/mkv_input.html), using two word groupings – what Bentley refers to as “Order-2.” Here’s what I got back:


> You can feel the need to take advantage of increased cheapness, however. You’re not all playing a zero-sum game. There’s not some fixed number of startups; we fund startups we fund to work on matters of passing importance. But I’m uncomfortably aware that this is part of any illusions about the problem of overeating by stopping eating. I couldn’t simply avoid the Internet had become, because the company is the new trend of worrying obsessively about what it meant for someone, usually an outsider, who deliberately stirred up fights in a startup than just start it. You know how the A List is selected. And even that is more work.


But Markov chains aren’t just useful for automatically generating Paul Graham essay parodies. They’re also quite practical. You might even say Markov chains are a large part of what powers today’s internet. Most remarkably, to me at least, Markov chains underlay Google’s trillion dollar [PageRank formula](http://en.wikipedia.org/wiki/PageRank):


> The [PageRank] formula uses a model of a random surfer who gets bored after several clicks and switches to a random page. The PageRank value of a page reflects the chance that the random surfer will land on that page by clicking on a link. **[PageRank] can be understood as a Markov chain in which the states are pages, and the transitions are all equally probable and are the links between pages.**
> As a result of Markov theory, it can be shown that the PageRank of a page is the probability of being at that page after lots of clicks. This happens to equal t-1 where t is the expectation of the number of clicks (or random jumps) required to get from the page back to itself.


Incidentally, if you haven’t read the original 1998 PageRank paper, titled The PageRank Citation Ranking: Bringing Order to the Web (pdf), you really should. It’s remarkable how, ten years on, so many of the predictions in this paper have come to pass. It’s filled with interesting stuff; the list of the top 15 PageRank sites circa 1996 in Table 1 is an eye-opening reminder of how far we’ve come. Plus, there are references to pornographic sites, too!


Markovian models – specifically, hidden Markov Models – are also related to our old friend, [Bayesian spam filtering](https://blog.codinghorror.com/the-nigerian-spammer-anthem/). They’re *even better!* The most notable example is the [CRM114 Discriminator](http://crm114.sourceforge.net/), as outlined in this [excellent presentation](https://web.archive.org/web/20090420024324/http://crm114.sourceforge.net/docs/Plateau99.pdf) (pdf).


![](https://blog.codinghorror.com/content/images/2025/04/image-138.png)


If you play with the Markov text synthesizer, you’ll quickly find that Markov methods are only as good as their input corpus. Input a bunch of the same words, or random gibberish, and that’s what you’ll get back.


But it’s sure tough to imagine a more ideal input corpus for Markovian techniques than the unimaginable vastness of web and email, isn’t it?

[markov chains](https://blog.codinghorror.com/tag/markov-chains/)
[programming](https://blog.codinghorror.com/tag/programming/)
[garfield](https://blog.codinghorror.com/tag/garfield/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[humor](https://blog.codinghorror.com/tag/humor/)
