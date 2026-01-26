---
title: "Social Media Engagement in Early 2025"
description: "Comparing engagement on two dozen recent social media   posts"
date: 2025-04-04T00:00:00
tags: ["writing", "website"]
url: https://martinfowler.com/articles/2025-social-traffic.html
slug: 2025-social-traffic
word_count: 943
---


A few years ago, whenever I published a new article here, I would just
    announce it on Twitter, which seemed to help attract readers who would find
    the article worthwhile. Since the Muskover, Twitter's importance has
    declined sharply. It now doesn't take very much time at all for me to check
    posts of people I follow on X (Twitter), since most of them have left.
    Instead I'm looking at other social sites, and posting there too. Now when I
    announce a new article, I post on LinkedIn, Bluesky, Mastodon, as well as X
    (Twitter). (I also post into my RSS feed, which is still my favorite way to
    let people know of new material, but that may just reveal I'm stuck in an
    idyllic past.)


While it's one thing to have a gut feel for the importance of these
    platforms, I'd rather gather some more objective data.


One source of data is how many followers I have on the these
    platforms.


![](2025-social-traffic/followers.png)


Here X (Twitter) shows a notable lead, but I strongly suspect that
    many of my followers there are inactive (or bots). Considering I only joined
    LinkedIn about a year ago, it's developed a healthy number.


Given that I decided to look at activity based on my recent posts. Most
    of my posts to social media I make across all these platforms, tweaking them
    a little bit depending upon their norms and constraints.
    For this exercise I took 24 recent posts and looked at what activity they
    generated on each platform.


I'll start with reposts. Although some LinkedIn posts get
    reposted more often than X, the median is pretty close. Bluesky trails a bit
    behind, but nowhere near as far as the follower count would suggest.
    Mastodon, as we'll see with all three stats, is far smaller.


![](2025-social-traffic/reposts-strip.png)


Figure 2: Plot of reposts


This plot is a combined strip chart and box plot. When visualizing data,
    I'm suspicious of using aggregates such as averages, as averages can often
    [hide a lot of important information](https://martinfowler.com/articles/dont-compare-averages.html). I much
    prefer to plot every point, and in this case a [stripchart](https://martinfowler.com/articles/dont-compare-averages.html#strip) does the trick. A strip chart plots
    every data point as a dot on a column for the category. So every dot in the
    linkedIn column is the value for one linkedin post. I add some horizontal
    jitter to these points so they don't print on top of each other. The strip
    charts allow me to see every point and thus get a good feel of the
    distribution. I then overlay a [boxplot](https://martinfowler.com/articles/dont-compare-averages.html#boxplot), which
    allows me to compare medians and quartiles.


Shift over to likes however, and now LinkedIn is far above the others, X
    and Bluesky are about the same.


![](2025-social-traffic/likes-strip.png)


Figure 3: Plot of likes


With replies LinkedIn is again clearly
    averaging more, but bluesky does have a significant number of heavily
    replied posts that push its upper quartile far above the other two services.


![](2025-social-traffic/replies-strip.png)


Figure 4: Plot of replies


That's looking at the data, how might I interpret this in terms of the
    importance of the services? Of the three I'm more inclined to value the
    reposts - after all that is someone thinking the that post is valuable
    enough to send out to their own followers. That indicates a clear pecking
    order with LinkedIn > X > Bluesky > Mastodon. It's interesting that LinkedIn
    is a more singular leader on likes, it seems both higher itself and X is
    lower. I guess that means LinkedIn people are more eager to hit the like button.


As for replies, it's interesting to see that Bluesky has generated quite
    a few posts that have triggered lots of replies. But given that most replies
    aren't exactly insightful, I don't chalk that up as a positive. Indeed I see
    more inane and downright mean replies on Bluesky than I ever got on Twitter.
    In contrast, while Mastodon replies are much fewer, they far more likely to
    be worth reading.


An obvious further question to look at would be how many people click on
    the link and go on to read the article. To track that information, I'd need
    to add tracking attributes to my URLs (eg
    `?utm_source=mastodon&utm_medium=social`). I've not done
    that, partly because I always disliked such cluttered URLs, but mostly
    because I don't think I'd get enough value from the information to be worth the trouble.


What I can do, however, is look at the source information for all traffic
    to the site. Here's a plot of engaged sessions for the first quarter of each
    the last three years.


![](2025-social-traffic/sources-network.png)


As we can see X (Twitter) was the dominant figure in 2023 but in 2025
    LinkedIn has surged to a much greater amount of traffic. Bluesky is hardly
    visible. (I can't track Mastodon this way.)


LinkedIn has indeed shot to #3 source so far this year. But #3 is a long
    way from the first two (google and direct).


![](2025-social-traffic/sources-all.png)


LinkedIn may be #3, but is the source for only 3.3% of the site's traffic.1


1: 
      I'm not sure how much traffic from these networks does not get properly flagged as a
      source in the analytics, so I'm wary of concluding too much from this figure.


One of the reasons for this is that social media posts may drive traffic
    to new articles, but most of my traffic is for older material. 80% of the
    traffic to my site goes to articles that are over six months old.


Overall, I'd say that LinkedIn has taken over as the number one social
      network for my posts, but X (Twitter) is still important. And Bluesky is
      by far the most active on a per-follower basis.


---
