---
title: "Using Analytics To Improve Your Web Design"
date: 2006-11-15
url: https://www.kalzumeus.com/2006/11/16/using-analytics-to-improve-your-web-design/
slug: using-analytics-to-improve-your-web-design
word_count: 364
---


So if you’re like me, you’ve been obsessively tracking folks through your website using Google Analytics, using the information on what the visitor paths are (home page -> trial explanation -> trial download -> purchase), what the high value paths are (anybody who clicks to read my license terms has a 50-50 shot of buying from me), and whatnot.  If you identify problems doing this (such as “Hmm, nobody who clicks on a screenshot ever comes back”), you’ve fixed them.  But you probably aren’t tracking people leaving your site, for example to go to an offsite payment processor, like Paypal.


Well, you should, and its really easy to accomplish.


You need to manually edit all of your links offsite to include the text


```
onclick="urchinTracker('/local/path/example');
```


where local path example is a non-existent web page on your site.  Google will report someone who clicks on that link as visiting the page /local/path/example, just as if they had visited a page with that name on your site.  I use /paypal/purchasing.htm/top-corner-button, for example, which tells me that somebody clicked on a link to Paypal from purchashing.htm on the top corner button.  This lets me see what part of purchasing.htm is really motivating people — in my case, its NOT the top-corner button (who knew!  I always expected folks would go for the easiest button to reach). but rather the part later on in the text where I describe Paypal as a safe, secure place to shop online.  I guess I understand why Paypal trumpets that so much in their marketing now!  My takeaway lesson from this is that my customers are a bit hesitant to give over their credit card number to somebody they’ve never met before, which fits my mental profile of them, and that I could probably increase conversions by stressing how safe and secure it is to buy through Paypal earlier on the page.  I’m going to do that and see how it pans out.


Anyhow, tagging your outbound links only takes a few seconds per link, and you can learn valuable stuff about your customers’ behavior.  I recommend that everyone does it, most especially to links that are in your conversion pathway.
