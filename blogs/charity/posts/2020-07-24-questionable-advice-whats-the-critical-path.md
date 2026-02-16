---
title: "Questionable Advice: “What’s the critical path?”"
date: 2020-07-24
url: https://charity.wtf/2020/07/24/questionable-advice-whats-the-critical-path/
word_count: 534
---


[Dan Golant](http://twitter.com/dangolant) asked a great question today: “Any advice/reading on how to establish a team’s critical path?”


I repeated back: “establish a critical path?” and he clarified:


> Yea, like, you talk about buttoning up your “critical path”, making sure it’s well-monitored etc. I think that the right first step to really improving Observability is establishing what business processes *must* happen, what our “critical paths” are. I’m trying to figure out whether there are particularly good questions to ask that can help us document what these paths are for my team/group in Eng.


“Critical path” is one of those phrases that I think I probably use a lot. Possibly because the very first real job I ever had was when I took a break from college and worked at criticalpath.net (“we handle the world’s email”) — and by “work” I mean, “lived in SF for a year when I was 18 and went to a lot of raves and did a lot of drugs with people way cooler than me”. Then I went back to college, the dotcom boom crashed, and the CP CFO and CEO actually went to jail for cooking the books, becoming the only tech execs I am aware of who actually went to jail.


Where was I.


Right, critical path. What I said to Dan is this: “What makes you money?”


Like, if you could only deploy three end-to-end checks that would perform entire operations on your site and ensure they work at all times, what would they be? what would they do? “Submit a payment” is a super common one; another is new user signups.


The idea here is to draw up a list of the things that are absolutely worth waking someone up to fix immediately, night or day, rain or shine. That list should be as compact and well-defined as possible. This allows you to be explicit about the fact that *anything else can wait til morning*, or some other less-demanding service level agreement.


And typically the right place to start on this list is by asking yourselves: “what makes us money?” as a proxy for the real questions, which are: “what actions allow us to survive as a business? What do our customers care the absolute most about? What makes us *us*?” That’s your critical path.


Someone will usually seize this opportunity to argue that absolutely any deterioration in service is worth paging someone immediately to fix it, day or night. They are wrong, but it’s good to flush these assumptions out and have this argument kindly out in the open.


(Also, this is really a question about service level objectives. So if you’re asking yourself about the critical path, you should probably consider buying [Alex Hidalgo’s book on SLOs](https://www.amazon.com/Implementing-Service-Level-Objectives-Practical/dp/1492076813), and you may want to look into the [Honeycomb SLO](https://www.honeycomb.io/blog/challenges-with-implementing-slos/) product, the only one in the industry that actually implements SLOs as the Google SRE book defines them (thanks Liz!) and lets you jump straight from “what are our customers experiencing?” to “WHY are they experiencing it”, without bouncing awkwardly from aggregate metrics to logs and back and just … hoping … the spikes line up according to your visual approximations.)


![bed - 13 (1)](https://i0.wp.com/charity.wtf/wp-content/uploads/2020/07/bed-13-1.jpg?resize=198%2C264&ssl=1)

charity.