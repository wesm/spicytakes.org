---
title: "Web Discussions: Flat by Design"
date: 2012-12-13
url: https://blog.codinghorror.com/web-discussions-flat-by-design/
slug: web-discussions-flat-by-design
word_count: 1514
---

It’s been six years since I wrote [Discussions: Flat or Threaded?](https://blog.codinghorror.com/discussions-flat-or-threaded/) and, despite a bunch of evolution on the web since then, my opinion on this has not fundamentally changed.


If anything, my opinion has strengthened based on the observed data: *precious few threaded discussion models survive on the web*. Putting aside Usenet as a relic and artifact of the past, it is rare to find threaded discussions of any kind on the web today; for web discussion communities that are more than ten years old, the vast majority are flat as a pancake.


I’m game for trying anything new, I mean, I even tried *Google Wave*. But the more I’ve used threaded discussions of any variety, the less I like them. I find precious few redeeming qualities, while threading tends to break crucial parts of discussion like reading and replying in deep, fundamental, unfixable ways. I have yet to discover a threaded discussion design that I can tolerate long term.


A part of me says this is software Darwinism in action: **threaded discussion is ultimately too complex to survive on the public Internet**.


![](https://blog.codinghorror.com/content/images/2025/07/threaded-discussion-example-hacker-news.png)


Before threaded discussion fans bring out their pitchforks and torches, I fully acknowledge that *aspects* of threading can be useful in certain specific situations. I will get to that. I know I’m probably wasting my time even attempting to say this, but please: keep reading before commenting. Ideally, read the *whole article* before commenting. Like PaRappa, [I gotta believe!](http://en.wikipedia.org/wiki/PaRappa_the_Rapper)


![](https://blog.codinghorror.com/content/images/2025/07/parappa-the-rapper-i-gotta-believe.png)


Before I defend threaded discussion, let’s enumerate the many problems it brings to the table:

1. **It’s a tree**.
Poems about trees are indeed lovely, as Joyce Kilmer promised us, but [data of any kind represented as a tree](https://blog.codinghorror.com/trees-treeviews-and-ui/)... isn’t. Rigid hierarchy is generally not how the human mind works, and the strict parent-child relationship it enforces is particularly terrible for fluid human group discussion. Browsing a tree is complicated, because you have to constantly think about what level you’re at, what’s expanded, what’s collapsed… there’s always this looming existential crisis of *where the heck am I?* Discussion trees force me to spend too much time mentally managing that two-dimensional tree more than the underlying discussion.
2. **Where did that reply go?**
In a threaded discussion, replies can arrive any place in the tree at any time. How do you know if there are new replies? Where do you find them? Only if you happen to be browsing the tree at the right place at the right time. It’s annoying to follow discussions over time when new posts keep popping up anywhere in the middle of the big reply tree. And God help you if you accidentally reply at the wrong level of the tree; then you’re suddenly talking to the wrong person, or maybe nobody at all. It absolutely *kills* me that there might be amazing, insightful responses buried somewhere in the middle of a reply chain that I will never be able to find.
3. **It pushes discussion off your screen**.
So the first reply is indented under the post. Fair enough; how else would you know that one post is a reply to another post? But this indentation game *doesn’t ever end*. Reply long and hard enough and you’ve either made the content column impossibly narrow, or you’ve pushed the content to exit, stage right. That’s how endless pedantic responses-to-responses ruin the discussion for everyone. When we play the “indent everything to the right” game, everyone loses. It is natural to scroll *down* on the web, but it is utterly unnatural to scroll *right*. Indentation takes the discussion in the wrong direction.
4. **You’re talking to everyone.**
You think because you clicked “reply” and your post is indented under the person you’re replying to, that your post is talking only to that person? That’s so romantic. Maybe the two of you should get a room. A special, private room at the far, far, far, far, *far* right of that threaded discussion. This illusion that you are talking to one other person ends up harming the discussion for everyone by polluting the tree with these massive narrow branches that are constantly in the way.At an absolute minimum you’re addressing everyone else in that discussion, but in reality, you’re talking to anyone who will listen, for all time. Composing your reply as if it is a reply to just one person is a quaint artifact of a world that doesn’t exist any more. Every public post you make on the Internet, reply or not, is actually talking to *everyone who will ever read it*. It’d be helpful if the systems we used for discussion made that clear, rather than maintaining this harmful pretense of private conversations in a public space.
5. **I just want to scroll down.**Reddit (and to a lesser extent, Hacker News) are probably the best known examples of threaded comments applied to a large audience. While I find Reddit so much more tolerable than the bad old days of Digg, I can still barely force myself to wade through the discussions there, because it’s so much darn *work*. As a lazy reader, I feel I’ve already done my part by deciding to enter the thread; after that all I should need to do is scroll or swipe down.Take what’s on [the top of reddit right now](http://www.reddit.com/r/pics/comments/14svrt/my_little_brother_had_an_interesting_night/). It’s a cool picture; who wouldn’t want to meet Steve Martin and Morgan Freeman? But what’s the context? Who is this kid? How did he get so lucky? To find out, I need to collapse and suppress dozens of random meaningless tangents, and the replies-to-tangents, by clicking the little minus symbol next to each one. So that’s what I’m doing: reading a little, deciding that tangent is not useful or interesting, and clicking it to get rid of it. Then I arrive at the end and find out that information wasn’t even in the topic, or at least I couldn’t find it. I’m OK with scrolling down to find information and/or entertainment, to a point. What I object to is the menial labor of collapsing and expanding threaded portions of the topic as I read. Despite what the people posting them might think, those tangents aren’t so terribly important that they’re worth making me, and every other reader, act on them.


Full bore, no-holds-barred threading is an unmitigated usability disaster for discussion, everywhere I’ve encountered it.


![](https://blog.codinghorror.com/content/images/2025/07/theaded-discussion-as-a-many-headed-hydra-1.jpg)


But what if we didn’t commit to this idea of threaded discussion quite so wholeheartedly?


The most important guidance for non-destructive use of threading is to **put a hard cap on the level of replies that you allow**. Although [Stack Exchange is not a discussion system](http://meta.stackoverflow.com/questions/92107/is-stack-overflow-a-forum) – it’s actually the *opposite* of a discussion system, which we have to explain to people all the time – we did allow, in essence, one level of threading. There are questions and answers, yes, but underneath each of those, in smaller type, are the comments.


![](https://blog.codinghorror.com/content/images/2025/03/image-139.png)


Now there’s a bunch of hard-core discussion sociology here that I don’t want to get into, like different rules for comments, special limitations for comments, only showing the top n of comments by default, and so forth. What matters is that we allow **one level of replies and that’s it**. Want to reply to a comment? You can, but it’ll be at the same level. You can go no deeper. This is by design, but remember: *Stack Exchange is not a discussion system*. It’s a question and answer system. If you build your Q&A system like a discussion system, it will devolve into Yahoo Answers, or even worse, Quora. Just kidding Quora. *You’re great*.


Would Hacker News be a better place for discussion if they capped reply level? Would Reddit? From my perspective as a poor, harried reader and very occasional participant, absolutely. There are many chronic problems with threaded discussion, but capping reply depth is the easiest way to take a giant step in the right direction.


Another idea is to let posts bring their context with them. This is one of the things that Twitter, the company that always does everything wrong and succeeds anyway, gets… shockingly right out of the gate. When I view one of my tweets, it can stand alone, as it should. But it can also bring some context along with it on demand:


![Twitter-threading](https://blog.codinghorror.com/content/images/uploads/2012/12/6a0120a85dcdae970b017ee6399d08970d-800wi.png)


Here, you can see how my tweet can be expanded with a direct link or click to show the necessary context for the conversation. But it’ll only show three levels: the post, my reply to the post, and replies to my post. This idea that tweets – and thus, conversations – should be mostly standalone is not well understood, but it illustrates how Twitter got the *original concept* so fundamentally right. I guess that’s why they can get away with the terrible execution.


I believe **selective and judicious use of threading** is the only way it *can* work for discussion. You should be wary of threading as a general purpose solution for human discussions. Always favor simple, flat discussions instead.

[web development](https://blog.codinghorror.com/tag/web-development/)
[discussion design](https://blog.codinghorror.com/tag/discussion-design/)
[web communities](https://blog.codinghorror.com/tag/web-communities/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
