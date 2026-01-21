---
title: "Code Reviews, Code Stories"
date: 2012-06-20
url: https://www.elidedbranches.com/2012/06/code-reviews-code-stories.html
word_count: 717
---

Code reviews are a tool that incites a lot of strong emotions from developers. Those who love them write tweets like

> **Code** **review** is hard - both reviewing and being reviewed make people cranky. But I know of no better way to make great software. -- [@yminsky](https://twitter.com/yminsky/status/214884552475279360)

This tweet, even in its adoration, still captures some of what people hate about code reviews. They make people cranky, to put it mildly. I personally don't like code reviews very much. In my experience, they are just as likely used to bully, score points, or waste time on pedantic style notes as they are to produce great software. In fact, I think code reviews are absolutely necessary only in three kinds of situations:
1) You don't have good automated testing practices in place to catch most errors at or before checkin.
2) You work on a big project with a very geographically distant team of developers (most open source).
3) You work in a company of many developers and huge code bases where strict style conformity is very important.
In my company, we have one team that falls into slot number 1, and they do code reviews for all checkins. The rest of the team does ad-hoc code reviews and occasional code walkthroughs, and we rely on the heavy use of testing to ensure quality. In general I feel that this enables a good mix of code correctness and checkin velocity.
The one thing this misses, though, is the required opportunity for developers to learn from each other. I like pair programming, and encourage my developers to do it when they are first starting projects or figuring out tricky bugs. But a lot of the time my developers are working in parallel on different code bases, and I felt that we were missing that learning moment that code reviews and pairing can provide. So I started asking people in interviews how they encouraged their team to work together and learn from each other, and I got a great suggestion: encourage the developers to show off work that they're proud of to other team members. Thus the Power Hour was born.
"Power Hour" is an hour that we do every Friday morning with my team and our sister team of warehouse developers. In that hour every developer pairs up with someone else and they take turns sharing something they did that week. Show off something you're proud of, ask for help with a problem you're stuck on, or get feedback on the way something was or is being designed. The power and choice of what to show lies in the hands of the person showing it, which takes away the punitive nature of code reviews; all they are required to do is to share some code. Show off, get help/feedback, and then switch. It's not about code review, that line-by-line analysis and search for errors big and small. It's about code stories, whether they are war stories, success stories, or stories still being written.
There are a lot of features of code review that this Power Hour doesn't satisfy. It's not a quiet opportunity to evaluate someone else's code without them looking over your shoulder. It's driven by the person that wrote the code and they are encouraged to highlight the good parts and maybe even completely bypass the ugly parts. It's not possible for the other person to fully judge the quality of what they're seeing, because judging isn't the point at all. Power Hour is a learning and sharing opportunity, and it is explicitly not an occasion for judging.
This has turned out to be a smashing success. It's amazing how much you can teach and learn in a concentrated hour of working with another person. Last week I showed off a new
[Redis](http://redis.io/)
-based caching implementation I wrote, and got to see all the code and a demo of a new
[Shiro](http://shiro.apache.org/index.html)
authentication and entitlement system. I caught a few things I still needed to clean up in the process of explaining my work, and so did my partner.
If you, like me, shun formal code reviews, I encourage you to try out a weekly turn at code stories. It's a great way to build up teamwork, encourage excellence, and produce great software, without the crankiness.