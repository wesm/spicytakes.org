---
title: "Speed Still Matters"
date: 2006-11-08
url: https://blog.codinghorror.com/speed-still-matters/
slug: speed-still-matters
word_count: 809
---

I remember switching my homepage from AltaVista to Google back in 2000 for one simple reason: **it was blazingly fast**. It’s the same reason I don't use personalized Google, or Google suggest as my homepage: they’re simply too slow.


Dare Obasanjo* wonders if AJAX apps are [rolling page load speeds back](http://www.25hoursaday.com/weblog/PermaLink.aspx?guid=c19f8a74-c0c9-46c6-b85e-cf7ff125e4c0) six years:


> One big problem with the AJAX craze that has hit the Web is how much slower websites have become now that using Flash and DHTML to add “richness” to Web applications is becoming more commonplace. **My mind now boggles at the fact that I now see loading pages that last several seconds when visiting Web sites more and more these days.**


Dare uses Yahoo! Mail as an example, but I’ve experienced similarly long load times for the new Hotmail beta, too. The load times can be so long that a combination disclaimer/escape hatch appears below the loading animation:


![](https://blog.codinghorror.com/content/images/2025/05/image-407.png)


Maybe I’m just impatient. However, there’s a lot of concrete data to support the theory that **unless you make it load fast, nobody will stick around long enough to find out what you have to offer**. For instance, [a recent study](https://web.archive.org/web/20061205072224/http://www.akamai.com/html/about/press/releases/2006/press_110606.html) found that most shoppers will only wait four seconds for a page to load before abandoning the site entirely.


Dare also cited this [post by Greg Linden](http://glinden.blogspot.com/2006/11/marissa-mayer-at-web-20.html) which provides more quantitative data on page load times from Google and Amazon:


> Google VP Marissa Mayer just spoke at the Web 2.0 Conference and offered tidbits on what Google has learned about speed, the user experience, and user satisfaction.
> Marissa started with a story about a user test they did. They asked a group of Google searchers how many search results they wanted to see. Users asked for more, more than the ten results Google normally shows. More is more, they said. So Marissa ran an experiment where Google increased the number of search results to thirty. Traffic and revenue from Google searchers in the experimental group dropped by 20%.
> Ouch. Why? Why, when users had asked for this, did they seem to hate it?
> After a bit of looking, Marissa explained that they found an uncontrolled variable. The page with 10 results took .4 seconds to generate. The page with 30 results took .9 seconds. **Half a second delay caused a 20% drop in traffic. Half a second delay killed user satisfaction.**
> This conclusion may be surprising – people notice a half second delay? – but we had a similar experience at Amazon.com. In A/B tests, **we tried delaying the page in increments of 100 milliseconds and found that even very small delays would result in substantial and costly drops in revenue.**


And let’s not forget the classic reference on application responsiveness: *Response Time in Man-Computer Conversation Transactions*, written way back in 1968 by R.B. Miller. I know it primarily through Jakob Neilsen’s [Response Times](http://www.useit.com/papers/responsetime.html): The Three Important Limits.

kg-card-begin: html

> **0.1 second** is about the limit for having the user feel that the system is reacting instantaneously, meaning that no special feedback is necessary except to display the result.
> **1.0 second** is about the limit for the user’s flow of thought to stay uninterrupted, even though the user will notice the delay. Normally, no special feedback is necessary during delays of more than 0.1 but less than 1.0 second, but the user does lose the feeling of operating directly on the data.
> **10 seconds** is about the limit for keeping the user’s attention focused on the dialogue. For longer delays, users will want to perform other tasks while waiting for the computer to finish, so they should be given feedback indicating when the computer expects to be done. Feedback during the delay is especially important if the response time is likely to be highly variable, since users will then not know what to expect.

kg-card-end: html

The 10 second number seems too high for today’s world of ubiquitous broadband and quad-core CPUs. That level of delay should be increasingly rare. I’d argue the user attention threshold is now more like 5 seconds. If your application is going to spend more than 5 seconds doing something, you owe your users an estimate of when you’ll be done, and real-time feedback on your progress. A basic hourglass doesn’t cut it.


What’s more important? Getting flash after 5 seconds, or functional no-frills layouts in less than a second? Let’s get our priorities straight. **Speed still matters.** And remember, the *perception* of speed is just as important as *actual* speed. If you can’t be fast, be clever. Exploit [progressive rendering](https://blog.codinghorror.com/the-lost-art-of-progressive-html-rendering/) and [HTTP compression](https://blog.codinghorror.com/http-compression-and-iis-6-0/).


*It’s ironic, then, that [Dare’s blog](http://www.25hoursaday.com/weblog/) is so incredibly slow to load every time I’ve directly visited it. One benefit of RSS aggregators, I suppose, is that I rarely need to.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[performance](https://blog.codinghorror.com/tag/performance/)
[ajax](https://blog.codinghorror.com/tag/ajax/)
[speed](https://blog.codinghorror.com/tag/speed/)
