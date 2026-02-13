---
title: "Getting Lookout to run on Outlook 2007 again"
date: 2007-12-24
url: https://www.joelonsoftware.com/2007/12/24/getting-lookout-to-run-on-outlook-2007-again/
word_count: 283
---


The search feature in Microsoft Outlook 2007, frankly, sucks big time.


It’s slow. Searches take about 30 seconds for me. (I  have about 10 years of email).


You have to wait for it to fail to find things in your inbox before you’re permitted to search elsewhere, even if you know the message isn’t in your inbox.


The search quality is atrocious. I regularly get 50% garbage results mixed in that have nothing in common with my search terms, and the message I am looking for often doesn’t come up.


The [patch](http://www.microsoft.com/downloads/details.aspx?familyid=C262BCFD-1E09-49B6-9003-C4C47539DF66&displaylang=en) helps, but it still takes around 30 seconds to do a search.


It didn’t use to be that way. A few years ago, there was a great add-in called [Lookout](https://www.joelonsoftware.com/items/2007/04/19.html) for Outlook, based on Lucene.NET. Searches always took less than a second.


The tiny company that made Lookout was [bought](http://www.news.com/Microsoft%20buys%20Lookout%20to%20boost%20search/2100-1032_3-5271825.html?part=rss&tag=5271825&subj=news.1032.5) by Microsoft. It must have been one of those HR acquisitions, because the Lookout technology was thrown away. Mike Belshe only spent a couple of years at Microsoft before moving on.


When Outlook 2007 came out, it disabled Lookout, and allegedly this wasn’t supposed to be a big deal because Outlook 2007 has search “built in.” But the built-in search is, as mentioned, ghastly.


Last week I had finally had enough. I can’t work like this. I spent some time searching on the net and found that the original author of Lookout, Mike Belshe, had just posted [instructions for getting Lookout to work on Outlook 2007](http://www.belshe.com/2007/12/06/how-to-install-lookout-on-outlook-2007/).


They worked! Lookout is back!


It’s fast! The first search takes about a second. After that something seems to be cached in memory and further searches appear as fast as you hit the “enter” key.
