---
title: "How do you do capacity planning?"
date: 2016-03-20
url: https://jvns.ca/blog/2016/03/20/how-do-you-do-capacity-planning/
slug: how-do-you-do-capacity-planning
word_count: 1032
---


I’ve been wondering recently about capacity planning. For example! Suppose you run a concert ticket website.


One day, you’re hit with a bunch of extra load. Your server can’t handle it, and your customers are sad (they were trying to buy tickets for the Beyonce concert that just got announced and they couldn’t!!!). You’re sad. Everyone is sad.


How do you fix it so that when Jay Z’s tickets go on sale next week, everything will be fine? Or how to you plan server purchases for the next year of huge ticket sales now that you’ve signed a lot of awesome new deals? CAPACITY PLANNING.


I don’t know a lot about how to do capacity planning. But here’s what I do know! warning: i am not a magical performance architect or whatever. I’m just here trying to make sense of computers.


### Resources


Your application uses resources. The main ones I know are

- disk I/O
- network bandwidth
- CPU
- databases, probably
- locks (which we’ll get into in a bit)


The first step when capacity planning is (or when doing performance work, generally) is to figure out which resource(s) you’re the most limited by, how much of that resource you’re using right now, and how much capacity have you there. For example! If every request takes 2s of CPU time (whoa.), then you can only handle 0.5 of them per CPU every second!


To figure out which resource you’re most limited by, the easiest method I’ve seen so far is

- watch your program explode (BOOM HUGE TICKET SALE)
- look at a lot of graphs
- go “welp, looks like the CPU graph was the saddest this time”
- conclude that you’re limited by your CPU usage


This sucks because your application has to explode but it seems pretty easy otherwise. (I would love to learn about non-application-exploding techniques if you know any). Once I have a vague idea of which resource is sad, I find it helpful to collect a bit more information.


It’s pretty easy to measure how much CPU your application is using (you can use [the `clock_gettime` system call](http://jvns.ca/blog/2016/02/20/measuring-cpu-time-with-clock-gettime/)). Network is also not too hard – you can use some system monitoring tool like `dstat` of `iftop`, see how much network gets used after 20 minutes or an hour, and then figure out what the average usage is. Similarly for disk usage.


Databases are quite a bit more tricky. If I wanted to know how query load my database could sustain, I’d probably spin up a new instance of that database and load test it until it stopped working. That’s a lot more time intensive, though!


You’ll notice in all of these examples, I’ve assumed that your program has consistent usage patterns (that one Jay-Z ticket won’t take 100x more resources than another). This often totally isn’t true in practice! I do not have a cool answer for how to deal with this.


### locks: a weird resource


Kelsey [very correctly noted on twitter](https://twitter.com/_K_E_L_S_E_Y/status/711648081545003008) that if you’re selling tickets, it’s SUPER IMPORTANT to not sell more tickets than you actually have. So you need to create some kind of lock so that every ticket machine can check and make sure that this new person can actually get a ticket. Locks are not a kind of resource you can just get more of, since they’re about synchronization! I will not say more about this here but it’s super super important.


### Load balancing


Okay, awesome. You went back and looked at the graphs from the Beyonce sale, and you noticed that the database servers went BOOOM. You do not know how to make them faster, but you do know how to add more servers! Right now you have 7 servers. Maybe you need 14? Huh.


This is where we get to talk about cool things like utilization and load balancing. So. Suppose you have 7 identical database servers you’re sending queries to, and you always pick a random server.


Now, suppose you have 100 queries per second that you’re making. I did a cool simulation of how the “pick a random server” strategy distributes load:


```
db     number of queries
db1    16
db2    16
db3    14
db4    12
db5    16
db6    18
db7     8

```


db7 has *half* as much work to do as db1! That’s not fair at all! This means you can end up in situations where one machine gets too much work to do (say 30% more than it can handle) while another machine is sitting mostly idle. So you’re paying for machines that aren’t helping you solve your problem! Ugh. No fun.


So load balancing strategies actually matter.


There’s a cool paper that says that the following algorithm:

- pick 2 random machines
- figure out which machine has less load
- send your request to that one


is actually an awesome and very stable load balancing strategy. I do not have a link right now but I will put one up when I get it.


### how much do load balancing strategies actually matter?


How bad is it to use a random load balancing strategy? I feel like this is something I should be able to solve with a math degree, but I don’t know! Does it mean you need 25% more machines than if you had a good strategy? 50% more? I have no idea. Do you?


### reasoning is cool


I’m very slowly starting to realize that, when you’re trying to make computers do a lot of stuff, there are maybe easier strategies than “just throw more computers at it until you are no longer on fire”. My job got quite a bit less confusing when I realized I could actually **measure** how much CPU I was using, and scale CPU resources accordingly.


So maybe you can actually measure and determine in advance how many computers you need to not be on fire! Also it seems like there’s some connection to autoscaling here, but I really know nothing about autoscaling here.


If you know how to do capacity planning (or know a good blog post/book I should read) please let me know! I am [on twitter as always](https://twitter.com/b0rk/).
