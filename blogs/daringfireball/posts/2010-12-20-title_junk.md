---
title: "Title Junk"
date: 2010-12-20
url: https://daringfireball.net/2010/12/title_junk
slug: title_junk
word_count: 983
---


The recent hubbub about Delicious got me thinking about bookmarking in general, and brought to mind a long-standing irritation: poorly designed web page titles.


Here’s an example that I bookmarked last night: [Roger Ebert’s 1968 review of *2001: A Space Odyssey*](http://rogerebert.suntimes.com/apps/pbcs.dll/article?AID=/19680421/COMMENTARY/40312115). The title of that web page is:


> “2001” -- the Monolith and the Message :: rogerebert.com :: News & Comment


That’s not the *headline* of the review. The headline is just fine:


> “2001” -- The Monolith and the Message


(Although it would be an improvement if it used a proper em-dash, rather than two hyphens.)


The title is the string of text in the HTML `<title>` element. This string manifests itself to the user in several ways. It is presented in the title bar of the web browser window on Mac and Windows. It is presented in the tab, if you’re using tabs in your browser. It is presented at the top of the screen in mobile web browsers. It is listed in the “Window” menu of your browser, listing all open browser windows. And, when you choose to bookmark a web page, the title string is used as the default name of the bookmark.


An awful lot of websites use patterns for page titles that are ugly, hard-to-scan, and/or just plain stupid. Consider Ebert’s review again:


> “2001”  --  the Monolith and the Message :: rogerebert.com :: News & Comment


The pattern is obvious: headline, space, double colons, space, “rogerebert.com :: News & Comment”. Why “space double-colon space”? No one punctuates with colons like that. The Chicago Sun-Times would never think of using colons like this in their print edition — but they misuse colons like this, twice, on every single review on Roger Ebert’s website. Why the “News & Comment” detritus at the end?


The new CMS the Sun-Times is using for its main website uses a much better title pattern: *headline, dash, Chicago Sun-Times*. Example:


> [Rahm Emanuel confident he’ll survive residency fight - Chicago Sun-Times](http://www.suntimes.com/2951732-417/emanuel-chicago-police-plan-tif.html)


Nice and simple, no junk. Really, the only two patterns that make sense to me are:

- Source: Headline
- Headline — Source


I personally prefer the “Source: Headline” pattern (hence its use here at Daring Fireball). But I can see one argument for “Headline — Source”: with tabbed browsing, users often only see the first 25 or so characters of the title. If you consume those characters with the name of the site, there may not be room for any characters from the headline.


I could spend all day showing examples of junky title patterns from big-name websites. MSNBC articles have both a category and sub-category in their titles:


> [‘Don’t Ask’ Repealed, but Restrictions Remain - Politics - More Politics - msnbc.com](http://www.msnbc.msn.com/id/40749607/ns/politics-more_politics/)


The MSNBC home page’s title is chock full of SEO crap, and, bafflingly, doesn’t actually contain the string “MSNBC” until the very end:


> [Breaking News, Weather, Business, Health, Entertainment, Sports, Politics, Travel, Science, Technology, Local, US & World News - msnbc.com](http://www.msnbc.msn.com/)


Surely, the name of the site should be the first thing (and in many cases, the only thing) in the title of the home page.


Most websites from big old-media companies have some sort of SEO-inspired title junk on their home pages. CNN:


> [CNN.com - Breaking News, U.S., World, Weather, Entertainment & Video News](http://cnn.com/)


The New York Times:


> [The New York Times - Breaking News, World News & Multimedia](http://www.nytimes.com/)


The New Yorker’s home page title is shamefully sloppy:


> [National and world news, Profiles, culture, reviews, fiction, poetry : The New Yorker](http://www.newyorker.com/)


The New Yorker — arguably the most precisely punctuated and copy-edited publication in the English-speaking world — would never use a colon like that (i.e., with a preceding space) in print. And why in the world is “Profiles” capitalized?


Yahoo News, rather than naming its home page via the title, seems intent on explaining to you what a news web site home page is:


> [The top news headlines on current events from Yahoo! News](http://news.yahoo.com/)


Fox News wants to let you know they’ve got fresh news on their home page:


> [FoxNews.com - Breaking News | Latest News | Current News](http://www.foxnews.com/)


Who are these title-junk keywords aimed at? Google? Do they really think that putting “breaking news” in their home page title makes it more likely that Google will rank them higher when people search for that term? It’s like they’re taking advice out of an SEO book from 1995.


Even worse, from an SEO perspective, is that Google, and all other major search engines, use web page titles as the name for pages in search results. MSNBC is the fourth result at Google in a search for “news”, but its page title is so long that “MSNBC” [doesn’t actually appear in the result entry title](https://daringfireball.net/misc/2010/12/msnbc-google-results.png).


Speaking of Google, the title of [their home page](http://www.google.com/) is simply “Google”. [Apple’s home page](http://www.apple.com/) title: “Apple”. Exactly what you’d want as a bookmark name for those pages.


That’s a good rule of thumb for designing and writing page titles: pick a name (and, for CMS templates, a pattern) that makes sense as the name of a bookmark for that page. Most bookmarking tools — the ones built into web browsers, and bookmarklets for third-party apps — *do* use the page title as the default bookmark name. Tools that help people tweet links to articles use the page title as the default description. So make titles useful. Write them for humans, not search engine spiders. Putting SEO keywords in the page title (a) doesn’t actually help your page’s rank in search engine indexes, and (b) makes things harder for people trying to tweet a link, bookmark your page, or scan it from a list of currently open windows and tabs in their browser. Trust the Googlebot to figure it out.



| **Previous:** | [The Best Laid Plans](https://daringfireball.net/2010/12/the_best_laid_plans) |
| **Next:** | [Emotional Rescue](https://daringfireball.net/2010/12/emotional_rescue) |


PreviousNext