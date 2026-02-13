---
title: "A Dusting of Gamification"
date: 2018-04-13
url: https://www.joelonsoftware.com/2018/04/13/gamification/
word_count: 1162
---


*[This is the second in a series of posts about Stack Overflow. The first one is [The Stack Overflow Age](https://www.joelonsoftware.com/2018/04/06/the-stack-overflow-age/).]*


Around 2010 the success of Stack Overflow had led us into some conversations with VCs, who wanted to invest.


The firm that eventually invested in us, [Union Square Ventures](https://www.usv.com/), told us that they were so excited by the power of gamification that they were only investing in companies that incorporated some kind of game play.


For example, Foursquare. Remember Foursquare? It was all about making your normal post-NYU life of going to ramen noodle places and dive bars into a fun game that incidentally generated wads of data for marketers. Or Duolingo, which is a fun app with flash cards that teaches you foreign languages. Those were other USV investments from that time period.


At the time, I had to think for a minute to realize that Stack Overflow has “gamification” too. Not a ton. Maybe a *dusting* of gamification, most of it around reputation.


Stack Overflow reputation started as a very simple score. The original idea was just that you would get 10 points when your answers were upvoted. Upvotes do two things. They get the most useful answers to the top, signaling that other developers who saw this answer thought it was good. They also send the person who wrote the answer a real signal that their efforts helped someone. This can be incredibly motivating.


You would lose points if your questions were downvoted, but you actually only lose 2 points. We didn’t want to punish you so much as we wanted to show other people that your answer was wrong. And to avoid abuse, we actually make you *pay* one reputation point to downvote somebody, so you better really mean it. That was pretty much the whole system.


Now, this wasn’t an original idea. It was originally inspired by Reddit Karma, which started out as an integer that appeared in parentheses after your handle. If you posted something that got upvoted, your karma went up as a “reward.” That was it. Karma [didn’t do a single thing](https://www.zdnet.com/article/collaborative-filtering-comparing-reddits-karma-system-to-digg/) but still served as a system for reward and punishment.


What reputation and karma do is send a message that this is a community with norms, it’s not just a place to type words onto the internet. (That would be 4chan.) We don’t really exist for the purpose of letting you exercise your freedom of speech. You can get your freedom of speech somewhere else. Our goal is to get the best answers to questions. All the voting makes it clear that we have standards, that some posts are better than others, and that the community itself has some norms about what’s good and bad that they express through the vote.


It’s not a perfect system (more on the problems in a minute), but it’s a reasonable first approximation.


By the way, Alexis Ohanian and Steve Huffman, the creators of Reddit, were themselves inspired by a more primitive karma system, on Slashdot. This system had real-world implications. You didn’t get karma so that other people could see your karma; you got karma so that the system knew you weren’t a spammer. If a lot of your posts had been flagged for abuse, your karma would go down and you might lose posting or moderation privileges. But you weren’t really supposed to show off your high karma. “Don’t worry too much about it; it’s just an integer in a database,” Slashdot told us.


To be honest, it was initially surprising to me that you could just print a number after people’s handles and they would feel rewarded. Look at me! Look at my four digit number! But it does drive a tremendous amount of good behavior. Even people who aren’t participating in the system (by working to earn reputation) buy into it (e.g., by respecting high-reputation users for their demonstrated knowledge and helpfulness).


But there’s still something of a mystery here, which is why earning “magic internet points” is appealing to anyone.


I think the answer is that it’s nice to know that you’ve made a difference. You toil away in the hot kitchen all day and when you serve dinner it’s nice to hear a compliment or two. If somebody compliments you on the extra effort you put into making radish roses, you’re going to be very happy.


This is a part of a greater human need: to make an impact on the world, and to know that you’re contributing and being appreciated for it. Stack Overflow’s reputation system serves to recognize that you’re a human being and we are super thankful for your contribution.


That said, there is a dark side to gamification. It’s not 100% awesome.


The first problem we noticed is that it’s very nice to get an upvote, but getting a downvote feels like a slap in the face. Especially if you don’t understand why you got the downvote, or if you don’t agree. Stack Overflow’s voting has made many people unhappy over the years, and there are probably loads of people who felt unwelcome and who don’t participate in Stack Overflow as a result. (Here’s an old blog post explaining [why we didn’t just eliminate downvotes](https://stackoverflow.blog/2009/03/09/the-value-of-downvoting-or-how-hacker-news-gets-it-wrong/)).


There’s another problem, which is that, to the extent that the gamification in Stack Overflow makes the site feel less inclusive and welcoming to many people, it is disproportionately off-putting to programmers from underrepresented groups. While Stack Overflow does have many amazing, high reputation contributors who are women or minorities, we’ve also heard from too many who were apprehensive about participating.


These are big problems. There’s a lot more we can and will say about that over the next few months, and we’ve got a lot of work ahead of us trying to make Stack Overflow a more inclusive and diverse place so we can improve the important service that it provides to developers everywhere.


Gamification can shape behavior. It can guide you to do certain things in certain ways, and it can encourage certain behaviors. But it’s a very weak force. You can’t do that much with gamification. You certainly can’t get people to do something that they’re not interested in doing, anyway. I’ve heard a lot of crazy business plans that are pinning rather too high hopes on gamification as a way of getting people to go along with some crazy scheme that the people won’t want to go along with. Nobody’s going to learn French just to get the Duolingo points. But if you are learning French, and you are using Duolingo, you might make an effort to open the app every day just to keep your streak going.


I’ve got more posts coming! The next one will be about the obsessive way Stack Overflow was designed for the artifact, in other words, we optimized everything to create amazing results for developers with problems arriving from Google, not just to answer questions that people typed into our site.
