---
title: "Something Rotten in AdSense"
date: 2005-10-24
url: https://www.joelonsoftware.com/2005/10/24/something-rotten-in-adsense/
word_count: 940
---


**Something Rotten in AdSense**


Google [AdSense](https://www.google.com/adsense/) is a system for web publishers of all sizes, from big newspapers to tiny bloggers. They sign up with Google to place a small box full of text ads on their site. You’ve probably seen it, but if you haven’t, check out Michael’s [techInterview](http://www.techinterview.org/) site for an example.


Advertisers pay Google to have their ads appear in little sidebars. Well, that’s not technically correct. Advertisers actually pay Google if anyone *clicks *on those ads. In turn, Google gives a percentage of the money to the web site owner. As a web site owner, you can make some serious spending cash this way. Popular sites make hundreds or thousands of dollars a month.


The minute you put AdSense on your site, you might start thinking, hmm, gosh, what happens if *I* click on the ads on my own site? Will I make more money?


Probably not much. This problem, called *clickfraud*, is a tricky one, and Google claims to have algorithms to prevent it. They won’t tell us what they are, justifiably, I think, because that would it easier to defeat the algorithms. Still, how would you explain complaints like [this one](http://discuss.joelonsoftware.com/default.asp?biz.5.233297.23) from an advertiser:


> When I activate my AdSense campaign, not much more than 5 minutes go by before they are all over it.. Multiple clicks from the same Internet IP’s in Malaysia, Poland, Hongkong etc. (I tried to exclude certain countries in my AdSense account, but they seem to go through proxies, so its not much use)..
> Tried just now and within 2 minutes I had around 20 clicks, which were clearly fraudulent (they seem to use some kind of tool – no pictures on the site were loaded according to my log). I guess that was around €20, which went up in smoke there. The super-duper top secret internal Google clickfraud prevention system, which is supposed to deduct the invalid clicks at the end of the month, only seems to catch an extremely small fraction of the clicks, but not nearly enough. I can’t see which clicks I actually pay for in the invoice from Google, so it’s a bit hard to say.


When you connect the dots, what seems to be happening is that scammers are doing four things.

1. First, they create a lot of fake blogs. There are slimy companies that make [easy to use software](http://www.rsstoblog.com/) to do this for you. They scrape bits and pieces of legitimate blogs and repost them, as if they were just another link blog. It is very hard to tell the difference between a fake blog and a real blog until you read it for a while and realize there’s no human brain behind it, like one of those [Jack Format radio stations](http://www.wired.com/news/digiwood/0,1412,67727,00.html) that fired all their DJs, or maybe FEMA.
2. Then, they sign up for AdSense.
3. Then you buy or rent a network of zombie PCs (that is, home computers that are attached to the Internet permanently which have been infected by a virus allowing them to be controlled remotely).
4. Finally, use those zombie PCs to simulate clicks on the links on your blog. Because the zombie PCs are all over the Internet, they appear to be legit links coming from all over the Internet.


There might be a technical solution to this, although I can’t think of one offhand. The minute companies start cutting checks to “affiliates” at the end of the month that are based on nothing more than clicks, you’re bound to get the AllAdvantage phenomenon. AllAdvantage was probably one of the most spectacularly stupid business ideas to come out of the first Dot Com bubble: a company that paid you to look at ads. That’s because they fell victim to one of the better business ideas from the first Dot Com bubble: hiring armies of low-paid workers to look at AllAdvantage ads.


Eventually, it stops benefiting the advertiser, and the advertiser figures it out, and stops paying for the whole charade.


It is important to remember that AdSense is just one part of Google’s revenue. A more significant part is AdWords, which covers the ads that appear on Google’s own site. [AdWords](https://adwords.google.com/select/) are still susceptible to some fraud, although you can’t make money clicking on those ads, so it’s much less of a problem. There is a minor problem where advertisers hire clickers to click on their competitors’ ads, which cause their competitors to waste money, but that’s penny-ante stuff, and rare enough that advertising through AdWords still works well.


Still, with Google rapidly approaching 50% of the global search market, they can *double* the number of searches they get on their home page, but not much more than that, unless they can get more page views somehow. Which is why they are frantically trying to sign up non-fraudulent web sites for AdSense (they call me every two months) and constantly seeking new sources of ad inventory, which sounds a heck of a lot like what the web portals of the 90s tried to do.


This is where Google is actually hurt by the [long tail](http://www.wired.com/wired/archive/12.10/tail.html) world of millions of small sites. It’s easy to evaluate the top 100 or 1000 web sites to make sure they’re reasonably legit. It’s much harder to monitor 1,000,000 blogs to make sure that none of them were machine generated for the purpose of scamming AdSense revenue. Still, I don’t think Google has a choice: I predict that you’ll see a massive expulsion of smaller AdSense sites by Google, and it better happen soon, or AdSense will ruin Google’s reputation among advertisers, something which could be deadly.
