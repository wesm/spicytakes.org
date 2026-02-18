---
title: "Some Tweaks to the @daringfireball Twitter Account"
date: 2014-05-16
url: https://daringfireball.net/2014/05/daringfireball_twitter_tweaks
slug: daringfireball_twitter_tweaks
word_count: 350
---


I made a few tweaks to the bot that runs the [@daringfireball](https://twitter.com/daringfireball/) Twitter account today. Until now, I’d been posting links using my own homegrown URL shortener, like so: [http://df4.us/mr0](http://df4.us/mr0). ([Originally](https://twitter.com/daringfireball/statuses/1887730374), I was using a clever IDN domain name, but gave that up years ago because too many Twitter clients couldn’t deal with unicode characters in a URL.)


The reason I wrote my own URL shortener instead of using something like Bit.ly was twofold. First, to maintain control. My short URLs should work for as long as Daring Fireball itself is online. Second, by rolling my own, I could make URLs that were *really* short — 17 characters, including the “http://” protocol. That left more space in the tweets for long entry titles than if I were using most public link shortening services.


But Twitter long ago started wrapping all URLs, regardless of length, with its built-in t.co link shortening service. [All t.co URLs are now 22 characters in length](https://blog.twitter.com/2012/upcoming-tco-changes), which means that for my df4.us URLs, t.co was actually a URL *lengthener*, not a shortener. It also means that when you clicked a link in the DF Twitter feed, it would first redirect from t.co to df4.us, and only then to daringfireball.net — a needless extra hop. Plus, modern Twitter clients don’t display the shortened t.co URLs; they expand them to the original URL for display purposes.


In short, since the entire reason I’m using short URLs at all is for Twitter, it makes sense to simply use Twitter’s own shortener. I get [better analytics](https://analytics.twitter.com/) this way, too.


One more change I made while I was futzing with the posting bot’s code: When an item has a title that is [too long](http://daringfireball.net/linked/2014/05/16/heathrow-samsung-translation) to fit in a tweet, the bot trims words one at a time from the end of the title [until it’s short enough](https://twitter.com/daringfireball/status/467417333279887361) to fit, along with an ellipsis to indicate the truncation. Previously, I just lazily [truncated the tweet mid-word](https://twitter.com/daringfireball/status/347825448673214464) — and worse, I had a bug that left some long-titled items un-tweeted.



| **Previous:** | [Titles](https://daringfireball.net/2014/05/titles) |
| **Next:** | [WWDC 2014 Prelude](https://daringfireball.net/2014/06/wwdc_2014_prelude) |


PreviousNext