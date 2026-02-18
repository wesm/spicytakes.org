---
title: "Have high expectations for your computers"
date: 2016-02-10
url: https://jvns.ca/blog/2016/02/10/have-high-expectations-for-computers/
slug: have-high-expectations-for-computers
word_count: 1578
---


I gave a talk at [CUSEC](http://cusec.net) (a conference for software engineering students) in January where I talked about performance. One of the points I wanted to make in that talk was – [computers are fast](http://computers-are-fast.github.io/), and you should have high expectations for how fast they can be.


When I was in undergrad I didn’t know **anything** about how fast a computer or a disk was. I was awesome at algorithms but I probably would have believed you if you told me it was impossible to do more than a million square roots in a second.


Now I know a little more, and I have higher expectations, and it’s been really useful to me! For instance: if you have a machine that’s crawling and unable to do more than 10 requests per second? You should probably expect more. Let me try to convince you of that, and we’ll start high.


### a million QPS


What if you wanted to handle a million requests per second (aka QPS) on your computer?


First, that’s totally possible. I was originally alerted to this possibility by the amazing [Kelly Sommers](https://twitter.com/kellabyte) and her Haywire web server. As I understand it, it was originally a toy project for her to experiment with writing high-performance C code. According to [its README](https://github.com/haywire/haywire), Haywire can process **9 million** HTTP requests per second.


When I first read that I thought it was a typo. Surely nothing can do a million anythings per second? It wasn’t a typo.


But Haywire is a toy project, right? If we’re talking about doing a million requests per second, we should talk about a real project that people use in production. Great! Let’s talk about [nginx](https://www.nginx.com/).


There’s a great blog post by Datacratic, a little ad tech company here in Montreal, called [1M QPS with nginx and Ubuntu 12.04 on EC2](http://datacratic.com/site/blog/1m-qps-nginx-and-ubuntu-1204-ec2). They say it was pretty easy to reach 500K QPS, and then they did some extra tuning to get to a million. Welp.


### Java: 50,000 QPS


Okay, let’s add an extra couple of layers of difficulty. First, let’s use a Java server, which we’d expect to be maybe a little slower, and secondly, let’s have our service actually do something nontrivial. For this I visited [Netty’s testimonials page](http://netty.io/testimonials)


That page says:


> During our lab testing, the library has displayed excellent performance characteristics, allowing us to service 50,000+ messages per second from approximately 30,000 connected clients on a commodity Intel server costing approximately $850


50,000 QPS on a single server is still not shabby. I wish I had that! I imagine you could probably serve hundreds of thousands of requests per second in Java if you did practically nothing and were really careful about your memory usage. (if nginx can do it, why not netty? is there a reason?) But I’m making that up – I’m not a Java performance wizard (yet).


### Python, 1,000 QPS


Okay, Python is slow, right? Way slower than Java. I’m going to get into way sketchier territory here – we’ve resorted to a [tumblr post benchmarking a toy Python server against Go](http://dustinmm80.tumblr.com/post/58656259972/python-vs-go-requests-per-second)


I tested this one on my laptop. You can really do 1,000 HTTP requests per second in a toy Python HTTP server! Neat.


### Reasons your webserver might be slow


Okay! We’re now in charge of performance at an Important Web Startup. Let’s say you want to serve 500 requests per second on a single server. I’m talking about throughput here – I’m supposing it’s okay if it takes a long time to serve each request, you just need to finish 500 every second.


First: **your CPU can slow you down**


Let’s say you have 4 cores, and you want to serve 500 requests per second (throughput). Then your CPU budget per request is 8 milliseconds. That’s just CPU budget – if you’re waiting for a database, that doesn’t count.


I’m finding CPU budgets real useful to think about right now because I just found out that my service that I thought was slowed down by its network/database latency was ACTUALLY BEING SLOWED DOWN BY UNNECESSARY CPU ACTIVITY. I was mad.


So, 8 milliseconds. We already know that [a millisecond is a really long time in Java](http://jvns.ca/blog/2015/09/10/a-millisecond-isnt-fast-and-how-we-fixed-it/). It’s a million CPU instructions! But honestly – even if you’re in Python, 8 milliseconds is kind of a long time! If you have a webserver where the requests take more than 8ms of CPU time, it might be worth understanding why! It was super worth it for me to understand this.


Second, **you can have worker starvation**


I hate worker starvation. It is the worst. Worker starvation is when you have, say, 100 workers that can work on requests, and they’re all busy. Then when the 101st request that second comes in, it has to wait! Even if you have extra CPU to spare! This SUCKS.


I’m not going to pretend I know the answer to how to fix this for everyone. It sucks though. Maybe you can add more workers! Maybe you can do more work asynchronously! Maybe you can use threading! This stuff isn’t easy but sometimes you can make progress.


Third, **you can saturate your network connection**


If you have a web service, that means you need to receive network requests and send responses! If you run out of network bandwidth (perhaps because you’re doing huge database queries?), you can’t do any more! You either need a new machine, or more bandwidth, or figure out how to make your damn requests smaller. Sorry.


Amazon EC2 has relatively inexpensive machines that do **1Gbps** of network activity, according to this [random blog post](http://epamcloud.blogspot.ca/2013/03/testing-amazon-ec2-network-speed.html). I don’t have a lot to say about that, but that seems like a lot of network to me.


Fourth, **your database might not be able to handle the load**


You can’t fix this by adding more machines! Here you need to put your database on a bigger computer or replicate it or run less expensive queries or something.


Fifth, **you only have so much disk I/O**


If you can read from your disk at 200MB/s – that’s it. You can’t read more. This is like the network saturation problem. No good!


**There are a lot more things that can go wrong**


I stopped at 5, but there’s a lot of reasons your server can be slow! I’ve probably missed a bajillion things. There are a lot of resources that you can be stuck waiting for (like other external services!). You could have a problem with locks! You can’t know until you investigate.


### understand why your webserver can’t do a million QPS


I’m kind of joking here, but kind of not! Suppose your server gets super sad when you throw more than 10 requests per second at it. Why can’t it do 10 times that?


some possible responses:

- it’s because it’s in Python! (are you really doing more than 100ms of CPU per request? that’s a lot! why is that happening?)
- it’s because of the database! (cool! databases are really fast though! can you get a list of the most expensive queries and understand why those are happening?)
- I need to read a lot from disk and I have no more disk bandwidth. (do you know for sure why you’re reading so much?)
- it’s because of my network connection! (maybe just run `dstat` to make sure your network activity is what you think it is? You can break it down by process!)


I’ve found that it’s really easy to be wrong about why something is slow. Taking an hour or a day to look closely and make sure my assumptions about why my server is slow has been an awesome use of time. Spending a day setting up profiling feels terrible but then is AWESOME when you make everything faster and everybody loves you.


### believing in my computers is really useful to me


I have this mission to develop an absolute sense of how fast computers are. Instead of “Go is faster than Python”, I want to be able to know things like “I should be able to easily do 100 QPS in Python”.


Sometimes I tell someone about a programming problem I solved in a millisecond, and they say “I can solve it in a microsecond!”. As long as they’re not a jerk, I actually find this totally delightful – if computers can do a thing 1000 times faster than I thought, that’s amazing! I can add it to my list of magical computer facts.


Raising my expectations about how fast computers can and should be has been super useful to me. Now when I see that it takes a hour to process a million records, I get mad. If an HTTP request takes 100ms of CPU time to process, I get mad. I try to restrict my anger to cases where it actually matters – if the processing job is in my way, or if web performance is actually a problem.


But when performance becomes a problem, I find my slowly-building intuitions about performance are incredibly useful. I can feel way more confident spending time profiling and optimizing the problem if I’m sure that the program can be faster. And so far it’s worked! I’ve been able to make a couple of things much much faster.


Maybe there will be more interesting optimizations in my future! Maybe having high expectations about computers will be useful to you too! A toast to fast programs :)
