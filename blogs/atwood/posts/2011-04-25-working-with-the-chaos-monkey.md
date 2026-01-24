---
title: "Working with the Chaos Monkey"
date: 2011-04-25
url: https://blog.codinghorror.com/working-with-the-chaos-monkey/
slug: working-with-the-chaos-monkey
word_count: 823
---

Late last year, the Netflix Tech Blog wrote about [five lessons they learned](http://techblog.netflix.com/2010/12/5-lessons-weve-learned-using-aws.html) moving to Amazon Web Services. AWS is, of course, the preeminent provider of so-called “cloud computing,” so this can essentially be read as **key advice for any website considering a move to the cloud**. And it's great advice, too. Here's the one bit that struck me as most essential:


> We’ve sometimes referred to the Netflix software architecture in AWS as our Rambo Architecture. Each system has to be able to succeed, no matter what, even all on its own. We’re designing each distributed system to expect and tolerate failure from other systems on which it depends.
> If our recommendations system is down, we degrade the quality of our responses to our customers, but we still respond. We’ll show popular titles instead of personalized picks. If our search system is intolerably slow, streaming should still work perfectly fine.
> One of the first systems our engineers built in AWS is called the Chaos Monkey. **The Chaos Monkey’s job is to randomly kill instances and services within our architecture. **If we aren’t constantly testing our ability to succeed despite failure, then it isn’t likely to work when it matters most – in the event of an unexpected outage.


Which, let's face it, seems like insane advice at first glance. I'm not sure many companies even understand why this would be a good idea, much less have the guts to attempt it. Raise your hand if where you work, *someone deployed a daemon or service that randomly kills servers and processes in your server farm*.


Now raise your other hand if that person is still employed by your company.


Who in their right mind would willingly choose to work with a Chaos Monkey?


![](https://blog.codinghorror.com/content/images/2025/04/image-519.png)


Sometimes you don't get a choice; the Chaos Monkey chooses you. At [Stack Exchange](http://stackexchange.com/), we struggled for months with a bizarre problem. **Every few days, one of the servers in the **[**Oregon web farm**](http://blog.stackoverflow.com/2010/01/stack-overflow-network-configuration/)** would simply stop responding to all external network requests.** No reason, no rationale, and no recovery except for a slow, excruciating shutdown sequence requiring the server to bluescreen before it would reboot.


We spent months – literally *months* – chasing this [problem](http://serverfault.com/questions/104791/windows-server-2008-r2-network-adapter-stops-working-requires-hard-reboot) down. We walked the list of everything we could think of to solve it, and then some:

- swapping network ports
- replacing network cables
- a different switch
- multiple versions of the network driver
- tweaking OS and driver level network settings
- simplifying our network configuration and removing TProxy for more traditional `X-FORWARDED-FOR`
- switching virtualization providers
- changing our [TCP/IP host model](http://en.wikipedia.org/wiki/Host_model)
- getting Kernel hotfixes and applying them
- involving high-level vendor support teams
- some other stuff that I've now forgotten because I blacked out from the pain


At one point in this saga our team almost came to blows because we were so frustrated. (Well, as close to “blows” as a [remote team](https://blog.codinghorror.com/on-working-remotely/) can get over Skype, but you know what I mean.) Can you blame us? Every few days, one of our servers – no telling which one – would randomly wink off the network. **The Chaos Monkey strikes again!**


Even in our time of greatest frustration, I realized that there was a positive side to all this:

- Where we had one server performing an essential function, we switched to two.
- If we didn't have a sensible fallback for something, we created one.
- We removed dependencies all over the place, paring down to the absolute minimum we required to run.
- We implemented workarounds to stay running at all times, even when services we previously considered essential were suddenly no longer available.


Every week that went by, we made our system a tiny bit more redundant, because we had to. Despite the ongoing pain, it became clear that Chaos Monkey was actually doing us a big favor by forcing us to become extremely resilient. Not tomorrow, not someday, not at some indeterminate “we'll get to it eventually” point in the future, but *right now where it hurts*.


Now, none of this is new news; our problem is long since solved, and the Netflix Tech Blog article I'm referring to was posted last year. I've been meaning to write about it, but [I've been a little busy](http://stackexchange.com/sites). Maybe the timing is prophetic; AWS had a [huge multi-day outage last week](http://www.zdnet.com/blog/btl/amazons-web-services-outage-end-of-cloud-innocence/47731), which took several major websites down, along with a constellation of smaller sites.


Notably absent from that list of affected AWS sites? Netflix.


When you work with the Chaos Monkey, you quickly learn that everything happens for a reason. Except for those things which happen completely randomly. And that's why, even though it sounds crazy, **the best way to avoid failure is to fail constantly.**

kg-card-begin: html

(update: Netflix released [their version of Chaos Monkey](https://github.com/Netflix/SimianArmy) on GitHub. Try it out!)

kg-card-end: html
[cloud computing](https://blog.codinghorror.com/tag/cloud-computing/)
[aws](https://blog.codinghorror.com/tag/aws/)
[software architecture](https://blog.codinghorror.com/tag/software-architecture/)
[distributed systems](https://blog.codinghorror.com/tag/distributed-systems/)
[fault tolerance](https://blog.codinghorror.com/tag/fault-tolerance/)
