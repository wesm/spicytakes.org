---
title: "How CPU load averages work (and using them to triage webserver performance!)"
date: 2016-02-07
url: https://jvns.ca/blog/2016/02/07/cpu-load-averages/
slug: cpu-load-averages
word_count: 1549
---


CPU load averages have long been a little mysterious to me. I understood that
low is good, and high is bad, but I thought of them as a mostly inscrutable
number. I have now reached a small epiphany about them, which I would like to
share with you!


I tweeted earlier today:


> I understand CPU load averages now! If I have a load average of 6, and am processing 60 requests/second, then each one takes 6/60=0.1s of CPU time


and someone [responded](https://twitter.com/EitanAdler/status/696386442080030720):


> CPU load average is the number of processes in the runnable state. Little to nothing to do with CPU time.


I thought this was a totally reasonable response. I also still thought I was
*right*, but I needed to do some work first, and it wouldn’t fit in a tweet.


It turns out that I was kinda wrong, but I think also kinda right! What follows will hopefully be correct. When doing calculations, I’m going to assume that your processes using CPU are all doing it for the same reason, and that reason is to serve HTTP requests.


Before I explain what load averages have to do with CPU time (spoiler: we’re
going to do a tiny bit of queueing theory!), I want to tell you what a load
average is, and why the formula I tweeted is awesome.


### What’s a load average?


Modern operating systems (since, like, [4.2BSD in 1983](http://www.cim.mcgill.ca/~franco/OpSys-304-427/lecture-notes/node46.html)) can run more than one process on a single CPU (this is called “CPU scheduling”). My computer is running 300 processes right now! The operating system keeps track of a state for every process. The man page for `ps` lists them:


```
PROCESS STATE CODES
       Here are the different values that the s, stat and state output specifiers (header "STAT" or "S") will display to describe the state
       of a process:
       D    uninterruptible sleep (usually IO)
       R    running or runnable (on run queue)
       S    interruptible sleep (waiting for an event to complete)
       T    stopped, either by a job control signal or because it is being traced.
       W    paging (not valid since the 2.6.xx kernel)
       X    dead (should never be seen)
       Z    defunct ("zombie") process, terminated but not reaped by its parent.

```


The load average is the average, in the last minute / 5 minutes / 15 minutes, of the number of processes in a running or runnable state. As far as I understand, ‘runnable’ means “I’d be running if you’d let me”. Processes that are asleep don’t count. Almost every process on my computer is asleep at any given time.


Given this definition, you may understand why someone would say this has “Little to nothing to do with CPU time”. It doesn’t seem like it would!


### A quick note on multiple CPU cores


If there are 3 processes that want to run on a CPU at the same time, and your computer has 4 CPU cores, then you’re totally okay! They can all run. So a load average of 3 is fine is you have 4 cores, and bad if you have 1 core.


The number of cores you have doesn’t affect the formula we’re going to talk about here, though.


### Why CPU load averages are awesome


The other day at work, I had a server that had a load average of 6. It was processing 60 HTTP requests per second. (the numbers here are all fake)


Both of these numbers are easy to get! The load average is in the output of `top` (for instance `load average: 6.12, 6.01, 5.98`), and I got the requests per second processed (or throughput) by counting log lines in the service’s log file.


So! According to our formula from above, each request was taking 6 / 60 = 0.1s = 100ms of time using-or-waiting-for-the-CPU. I asked my awesome coworker to double check this division to make sure that was right. 100ms is a bajillion years of CPU time, and I was super concerned. That story is for another time! But being able to calculate that number so quickly was SUPER USEFUL to me for understanding the server’s performance.


### Why the formula is correct


So! I posited this formula that tells you CPU time per request = load average / request throughput (requests per second). Why does that work?


There’s this theorem called [Little’s Law](https://en.wikipedia.org/wiki/Little%27s_law), that states:


> The long-term average number of customers in a stable system L is equal to the long-term average effective arrival rate, λ, multiplied by the average time a customer spends in the system, W; or expressed algebraically: L = λW.


This is pretty intuitive: if 10 people per hour (W) arrive at your store, and they spend 30 minutes each there (λ), then on average there will be 5 people (L) at a time in your store.


Now, let’s imagine the CPU is your store, and that HTTP requests are people. The load average tells you how many processes at a time are in line to use the CPU (L). Since in my case I have 1 HTTP request / process, this is the same as the number of requests in line to use the CPU. Note that we care about the steady-state load average – if the load is constantly changing then it’s much harder to reason about. So we want the “average load average”. In my example system at work, the load average had been about 6 for a long time.


If your system is in a steady state (constant load), then the rate of incoming requests will on average, over a long period of time, be the same as the rate of finishing requests. That rate is W.


Lastly, λ is the amount of time each request spends on the CPU (in a running or runnable state).


So:

- L = load average (average # requests in a running or runnable state)
- λ = average total time each request spends in a running or runnable state
- W = throughput (requests per second)


So if we want to do my example from the previous section, we get:


time spent on CPU = λ = L / W = 6 / 60 = 0.1s per request.


### Caveats


There are quite a few assumptions built into this formula, which I’ll make explicit now. First, I told you “The load average tells you how many processes at a time are in line to use the CPU (L)”. This isn’t actually true!


The [Wikipedia page on load averages remarks that](https://en.wikipedia.org/wiki/Load_(computing)):


> However, Linux also includes processes in uninterruptible sleep states (usually waiting for disk activity), which can lead to markedly different results if many processes remain blocked in I/O due to a busy or stalled I/O system.


So, here are the cases when this “CPU time per request = load average / throughput” formula won’t work for you:

- some of your processes are in uninterruptible sleep
- your system has a highly fluctuating load average / throughput
- you’re handling more than 1 HTTP request per thread (for instance if you’re using Node or Go or…).
- the CPU activity on your system is caused by something other than your HTTP request processing
- this time (time running + time waiting for the CPU) includes time spent doing context switches between processes, and time spent on-CPU inside the kernel


It’s also worth noting that the load average is an exponentially decaying average. This means that if your load average is changing over time, it’s hard to know what the non-exponentially-decaying load average is.


There’s likely another caveat I’ve missed, but I think that’s most of them.


### a version for time spent *on* the CPU


We’ve found a formula for “time the request spends on the CPU (or waiting for it to be free)”. But what if we wanted to ignore the time it spent waiting? I have an idea that I made up just now.


If the CPU load is low (like, less than half your number of cores), I think it’s reasonable to assume that any process that wants to be scheduled gets scheduled immediately. So there’s nothing to do.


But what if your CPU is overloaded? Suppose I have 4 CPUs. Then we could instead define

- L = average number of processes in a running state (which should be 4, since the CPU is at capacity)
- λ = average time each request spends in a running state
- W = throughput (requests per second)


Then we can still try to calculate our new λ, from our example from before!


λ = L / W = 4 / 60 = 0.066 s = 66ms per request on the CPU.


I think this math still holds up, but it feels a little shakier to me. I would love comments on this.


### this formula = awesome


I had a good experience with this formula yesterday! Being able to quickly triage the number of milliseconds of CPU time per request was an awesome start to doing some more in-depth performance analysis! (which I won’t go into here)


I hope it will help you as well! If you think I’ve gotten this all wrong, [let me know on twitter](https://twitter.com/b0rk) :)


Thanks to Kamal Marhubi, Darius Bacon, Dan Luu, and Sean Allen for comments
