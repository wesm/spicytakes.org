---
title: "Learning at work"
date: 2017-08-06
url: https://jvns.ca/blog/2017/08/06/learning-at-work/
slug: learning-at-work
word_count: 1421
---


I asked on Twitter a while back “how do you invest in you own learning?” ([this tweet](https://twitter.com/b0rk/status/887111177062555648). Some common things people replied with:

- Read blog posts
- Go to conferences
- Read books
- Watch talks while washing the dishes
- Build side projects using the technologies you want to learn


These things all totally work. I see that it’s pretty common to spend time
outside of work working on your career development and learning new skills, and
it’s certainly something I’ve done a lot.


But I know some great programmers who *don’t* program outside of work at all!
So I got to thinking – what if you want to become awesome, but don’t want to
spend a lot of time basically doing extra work after hours?


Here are some things me & people on twitter came up with. Everything in here is
stuff I can do during my workday.


### Don’t learn programming languages/frameworks outside of work


This one is kind of negative but I think it’s useful! My view about learning programming languages is:

- I know a few languages reasonably well (python, scala, ruby)
- Learning a new programming language well takes a fair amount of time
- I don’t feel like spending my free time on it


Right now at work I’m working a bit in Go! That is interesting and I’m happy to
be doing it. But it is not *so* fun that I feel like spending a lot of my
personal time on it. And I don’t really think it’s necessary, I learn languages
by writing them, reading other people’s code to learn about conventions, and
having my code reviewed. I can just do all of those things at work!


To be clear, I don’t think it’s *bad* to learn programming languages outside of
work. I just don’t really do it.


### Choose projects I think I’ll learn from


Some of the things I"ve learned about in the last 3 years at stripe:

- Scala/Ruby/Go
- hadoop/mapreduce/scalding
- How to work with java concurrency libraries, how to profile a java program
- A ton about how various AWS services work
- A lot about machine learning
- How networking / CDNs / TLS work
- docker/containers/rkt/kubernetes
- Service discovery / DNS / jenkins


and a bunch more things.


As an small example of choosing something to work on that I wanted to learn from –
once I was using a program at work that wasn’t parallelizing its work well and
it was a problem. I could have asked the people who wrote it to figure out the
program but I thought – well, I’m interested in learning about concurrent
programming, I can probably do this! So I [learned a bit about how to use thread pools in Java!](https://jvns.ca/blog/2016/03/29/thread-pools-part-ii-i-love-blocking/)


I only worked on that for a few days but I learned new things!


Right now I am working on Kubernetes which I didn’t really pick for its
learning opportunities, but I *am* learning quite a few things about
distributed systems and Go by working with it and I’m happy about that.


I think it’s silly when people are like “hey, we work with X technologies, you
need to have experience with them to work here”. Right now I spend a lot of
time with networking/puppet/kubernetes/docker/AWS and I had never worked with
any of those things before this job.


### Watch more senior people operate


When someone is doing work I really admire, I’ll watch how they do it and then try to emulate them / ask them for advice. For example! When [cory](http://onemogin.com/) joined I noticed that, when introducing new technology, he would

1. find another team that had a related problem that needed solving
2. Work with them to make sure the technology actually worked to solve their problem!


Right now I am working on a newish project, and I’ve been careful about
remembering who exactly I expect it to help & how, and I think that’s made the
work go a lot better.


### Read every pull request


Two quotes I loved from this thread were:


> i’m on a small team so I read & reread every pull request that comes in until
> I understand the problem & solution fully


and


> I did the same! And I stalked checkins to see how people solved various
> problems


I don’t actually read every single pull request on my team. But I **do** find
it useful to pick a few areas I want to keep learning about, and keep track
over time of the work people are doing in that area.


I definitely can’t always do this – for example I used to work on machine
learning and while in theory I’d like to keep track of what people are up to
there because I find it really interesting, in practice it’s too much for me to
pay attention to. But I do try to pay attention to things that are closer to me
(like some of the networking team’s work!)


### Read the source code


> Reading source of what I use is a big one for me. Understand what it does
> internally but mainly *why* it does it a certain way.


I think this is a fantastic tip and super important!! A lot of systems aren’t
really that well documented and you can’t learn how they work without reading
their source code.


### Follow up on bugs I couldn’t figure out


Sometimes I see a bug that I can’t figure out how to fix. And then later,
sometimes somebody else will figure out the answer! When that happens, I like
to really take the time to understand what the answer was and how they figured
it out!


For example recently there was a networking issue that I didn’t manage to debug
and that somebody else just figured out last week. Thinking about it now, I
understand what the bug *was*, but I’m not 100% sure what tools they used to
get the information they needed to debug it. When I get back to work I need to
make sure I go find that out, so that next time I will be better equipped!


Jessica Kerr commented


> Whenever I have to look something up for troubleshooting, I go a little deeper
> or broader than strictly necessary.


which I think is a great philosophy :) :) (it’s not good to go **too** far
down every rabbit hole, but consistently reaching a little further than I have
to pays dividends for sure)


I also liked this answer:


> Sometimes I’ll just dig into a problem that’s work-related but not really
> within my actual duties and see if I can get somewhere.


### Use your commute


I don’t have a commute but a lot of people mentioned using their commute time
to listen to podcasts / read papers / read interesting articles. I think
this seems like an awesome way to keep up with things you’re interested in!


### Take the time at work to learn


Someone on Twitter said “I wish I could take 1 hour a day to learn”. My view is
that it’s my *job* to take time out of my workday to learn things. Like
right now I’m using Kubernetes at work, it’s a complicated system that takes a
long time to understand, and I spend time reading about it at work. For
instance, when we were starting out I spun up a test cluster just to poke
around and try to understand how container networking works. I also make
progress on our projects at the same time!


This is probably a bit easier for me because I work remote so nobody really knows
what I’m doing hour-by-hour anyway, People just care about what I’m getting
done overall.


I actually think I would probably be *more* productive if I took a little more
time to read in advance. Like I just read Kelsey Hightower’s “learn kubernetes
the hard way” document, it didn’t take that long, and it had one really good
idea about how to set up a cluster that would have saved me some time.


Some people take this idea even farther! For example, my friend Dan has
mentioned a few times that he likes to read technical books at work. I
originally found this kind of surprising but it makes sense – there are some
books that are relevant to my work, and there’s no reason really why I
shouldn’t read them at
work.
