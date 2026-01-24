---
title: "Disambiguating Search with Quasi-Evil Hierarchies"
date: 2005-11-15
url: https://blog.codinghorror.com/disambiguating-search-with-quasi-evil-hierarchies/
slug: disambiguating-search-with-quasi-evil-hierarchies
word_count: 290
---

Let’s say I was to search Google for the word **Jaguar**:


![](https://blog.codinghorror.com/content/images/2025/05/image-146.png)


There’s an immediate problem. The semantics of **Jaguar** only exist in my head, not in any search box. Did I mean...

- Jaguar the car?
- OSX Jaguar?
- Jaguar the animal?
- The Atari Jaguar?
- Austin Power’s [Shaguar](http://www.idcow.com/etl2039.html)?


Whichever it is, **Google is displaying a lot of search results that are totally irrelevant to me.** Sure, I could type in more words, but that’s at odds with the Google philosophy of simplicity. A single word should get me what I want.


Now compare the same search for Jaguar on eBay:


![](https://blog.codinghorror.com/content/images/2025/05/image-147.png)


Although I get the same poor results initially, I can indicate which kind of Jaguar I *really* meant with an additional click on the categories on the left side of the page. This immediately filters the search results to something relevant with almost no effort on my part.


Search dominates the web now, and for good reason. My apologies to [Yet Another Hierarchically Organized Oracle](https://web.archive.org/web/20051123230529/http://docs.yahoo.com/info/misc/history.html) and the [Open Directory Project](https://web.archive.org/web/20051116004546/http://dmoz.org/about.html), but [rigid hierarchy is evil.](https://web.archive.org/web/20051124190737/http://www.microcontentnews.com/articles/deathofhierarchy.htm) However, a **rigid hierarchy is tremendously powerful as a semantic-narrowing filter on search results.**


In a brave new Google world of “I’ll just type in what I want and hit Enter” search, there may still be room for some [quasi-evil](http://www.imdb.com/title/tt0145660/quotes) hierarchy in there somewhere. For example, **if Google is going to suggest “Did you mean...” corrections when I misspell a search term, why don’t they do the same thing to disambiguate semantics?**


![](https://blog.codinghorror.com/content/images/2025/05/image-148.png)


Unlike the rigid, manual categorizations of eBay and DMOZ, you could probably automate this kind of semantic suggestion engine using Markov chain probabilities on existing web pages.

[search engines](https://blog.codinghorror.com/tag/search-engines/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[search optimization](https://blog.codinghorror.com/tag/search-optimization/)
[information retrieval](https://blog.codinghorror.com/tag/information-retrieval/)
[search filters](https://blog.codinghorror.com/tag/search-filters/)
