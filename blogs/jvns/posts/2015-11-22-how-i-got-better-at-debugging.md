---
title: "How I got better at debugging"
date: 2015-11-22
url: https://jvns.ca/blog/2015/11/22/how-i-got-better-at-debugging/
slug: how-i-got-better-at-debugging
word_count: 830
---


I had a performance review last week where I was told, among other things, that I’m very good at debugging, especially difficult & confusing problems. I thought about this and I was like YEAH I AM. But I didn’t used to be. What happened?!


I sometimes hear advice to be extremely systematic and organized. I think that’s good advice and I told my partner this and he laughed because I am not the most systematic and organized person. But here are some things that I think have helped me anyway:


**Remember that the bug is happening for a logical reason**


Sometimes when I hit a bug, especially a nondeterministic and difficult to reproduce bug, it’s tempting to think “oh you know, things just happen, who knows”. But everything on a computer does in fact happen for a logical reason (however much the computer may try to convince you otherwise). Reminding myself of that helps me fix bugs. Also known as “OK JULIA IT IS NOT FAIRIES WHAT ACTUAL REASON COULD BE CAUSING THIS?”


**Be unreasonably confident in my ability to fix the bug**


I recently dealt with a performance problem in a job at work that took me 3 weeks to fix (see [a millisecond isn’t fast](http://jvns.ca/blog/2015/09/10/a-millisecond-isnt-fast-and-how-we-fixed-it/)). If I hadn’t been able to fix it, I would have felt pretty bad and like it was a waste of 3 weeks.


But we were processing a relatively small number of records, and it was taking 15 hours to do it, and it was NOT REASONABLE and I knew that the job was too slow. And I figured it out, and now it’s faster and everyone is happy.


(since I can now often actually fix bugs I tackle, perhaps this confidence is now reasonable :D)


**Know more things**


This [TCP bug](http://jvns.ca/blog/2015/11/21/why-you-should-understand-a-little-about-tcp/) I talked about yesterday? I wouldn’t have been able to fix that in my first job out of grad school. I just didn’t understand enough about how computer networks work, or computers (I had an awesome math & theoretical CS degree and I did not learn anything about computers there.). And I didn’t know strace.


There’s a service at work that sometimes takes a long time to respond because of JVM garbage collection pauses. If you don’t know that a common source of latency issues on the JVM is garbage collection pauses (or worse, if you don’t know that garbage collection pauses are even a thing that happen), then you’re going to have a really bad day trying to figure that out.


Understanding the structure of the system I’m trying to debug and what some of the common failure modes are has been really indispensable to me.


**Talk to other people**


I sometimes just ramble into the Slack channel at work about the problem I’m working on, which sometimes looks like


```
julia: i have no idea why this bug is happening
julia: i mean I tried X and it is still happening
julia: and also W
julia: and also Z
julia: OH RIGHT I FORGOT ABOUT ABC
julia: yayy
someone else: :)

```


Also sometimes if I start talking about it then someone will come and talk to me and say something helpful! It’s the best.


I got really stuck on that 3 week bug we talked about before and got on the phone to [Avi](https://twitter.com/avibryant), which was VERY USEFUL because he wrote the code that I was optimizing. So in that case I didn’t just need a rubber duck, I needed to talk to someone who knew more about the code (“oh yeah we haven’t optimized that part at all yet so it’s not a surprise that it’s slow!”).


I’ve gotten way better at figuring out what I don’t understand, articulating it, and asking about it.


**Use strace**


Seriously I could not fix bugs without strace.


More generally, being able to observe directly what a program is actually doing is incredibly valuable. I was trying to debug recently why a request I was sending to Redis was invalid. And I read the code, and asked other people, and they were like “huh that looks right”. AND THEN I REMEMBERED ABOUT TCPDUMP. (tcpdump shows you the TCP traffic coming in and out of a machine. it’s the best.)


So I ran tcpdump on a machine that I knew was sending (valid) requests to Redis, just looked at it as ASCII in my terminal, and then all the information was right there! And I copied the valid thing into what I was testing, and it totally worked and explained everything.


**I like it more**


I used to not really like debugging. But I started being able to solve harder bugs, and now when I find a thorny debugging problem it’s way more exciting to me than writing new code. Most of the code I write is really straightforward. A difficult bug is way more likely to teach me something I didn’t know before about how computers can break.


❤ debugging ❤
