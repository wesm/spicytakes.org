---
title: "On Yaks and Hacks"
date: 2012-07-12
url: https://www.elidedbranches.com/2012/07/on-yaks-and-hacks.html
word_count: 843
---


### A [Yak](http://www.catb.org/jargon/html/Y/yak-shaving.html) Story

Today I released a nice little feature into production that tests promoting a customer's "hearted" items to the top of their search results. I decided that it would be a good test after seeing some analytics data on users of this particular feature, and sold it to the head of analytics and myself as a quick feature to spin up, half a day's dev work for me. We already had the data, I just needed to play with the ordering of the products to display.
Of course, it didn't turn out to be quite that simple. When I opened the code and prepared to add the new feature, I discovered a few things. First, my clean checkout of the code base wouldn't even compile. Apparently in the time I had been away from it, the other devs had renamed a maven dependency, rtr_infra_common, to rtr_services_common, only to discover that they needed both. Instead of starting the new rtr_infra_common from, say, version 2, they started it back at version 1.0. My local maven was very, very confused.
Having figured that out, I finally had a clean, compiling workspace, so time to code. I have all the data I need to do this right here, right? Except, this "score" field that claims to be in the
[DTO](http://en.wikipedia.org/wiki/Data_transfer_object)
for our products is not in fact being serialized by the providing service. Oh and in my absence the package that holds that DTO has also gotten refactored into its own project. And rtr_services_common depends on that. And rtr_infra_common depends on THAT. And I depend on 
rtr_infra_common. So just to get the new data, I have to update the product catalog service, the DTO, and the whole chain of dependent projects.
As an aside, I think maven is kind of nice, but dependency management systems have caused the biggest yaks I've ever shaved, and those couple of hours of annoyance are a small drop in the bucket.
So, got my data. But now I find another problem.
The framework I'm working in was designed to take all of this data and apply experiments to it before returning it to the front end. But we hadn't actually built out a notion of the "user" beyond a userId for logging and bucketing purposes. There was nowhere to put the personalized data I needed to use to enhance the results. I could just save the list of items I needed and add an additional argument to the experiment processor with that data, but I knew that we would want more and different signals in the near future. So I took another couple of hours, refactored all of the code to properly model a user, changed and enhanced all the tests, and finally, finished the job... Except it didn't work. I had forgotten to update the clone method in our DTO to copy the new data I had added. My colleague stepped in for that last bit of belly shaving, as I had now blown my estimate by a good day and my other work was piling up. After going through the irritation of changing 4 projects for 1 line of code, he understood my earlier cursing, and we had our feature finally ready.

### A Hack Story

On Wednesday, I get a report that there's a snag in a release that is supposed to go out this week. We're taking some work that used to be done manually by our email marketing staff and automating it. The developer on the project has hit a bug. Apparently, our email service provider does not support UTF-8 encoding, and of course, being a fashion company, we have designer names with the occasional accent that we need to throw around. He's been struggling with this, trying to figure out why escaping isn't working, and finally discovering that only Latin-1 will suffice. Before he sits down to write this re-encoding of everything, we ask our email marketers how they did this in the past. "Oh, we just change them to plain text characters". How many characters are we talking about? "Just an
é
and a
ë". Would it be easier to just convert them to plain text than to Latin-1? Yes. And so we did.

### Yaks vs Hacks

On the other hand, I thought my new feature would be a quick hack that could give us a bunch of interesting data, and it turned into a minor yak (or perhaps just a shaggy water buffalo) that took a bit too long but was not quite a full-blown project. I couldn't hack the dependency problems, and hacking the code restructuring would have resulted in threading an arbitrary parameter through a bunch of unrelated code just to avoid thinking about the right solution. The upside of the yak shaving was more data, a better code base for making such changes in the future, and a recognition of a serious dependency structure problem that we need to address. So today I celebrate
[Yak Shaving Day](http://www.bcdb.com/cartoon_video/28426-Yak_Shaving_Day.html)
. I hope it only comes once a year!