---
title: "How do you decide what to work on?"
date: 2016-08-16
url: https://jvns.ca/blog/2016/08/16/how-do-you-work-on-something-important/
slug: how-do-you-work-on-something-important
word_count: 1958
---


So, I work as a programmer. Until pretty recently I was working on
machine learning, which is really fun and interesting. One thing I like
about machine learning is – it’s important (and fun!) to actually spend
time with your data manually and understand it and look at individual
things.


But, ultimately, they did not hire me to do manual work! One week I remember
thinking “right, my job is to build systems that accurately classify millions
of things, not to look at those things manually.”


So the reason programmers sometimes get paid a lot of money, I think, is
because we can build systems that leverage computers to do an
unreasonable amount of work. If you build Gmail’s spam system, you can
remove spam from the inboxes of millions of people! This is kind of
magical and amazing and it’s worth all of the bugs and dealing with
computers.


But it takes a long time! Basically anything interesting that I work on
takes, let’s say, 2-6 months. And it’s not too weird to work on projects
that take even longer! One of my friends worked on the same
thing for more than a year. And at the end he’d built a [system for drawing transit maps that’s better than
Google’s](https://medium.com/transit-app/transit-maps-apple-vs-google-vs-us-cb3d7cd2c362#.mt80iagen). This was really cool.


So this means you can really only do a few things. And if one of those things
doesn’t work out then that means that like a quarter of your work for the year
is gone. This is okay, but it means it’s worth being thoughtful.


And the more time I spend programming, the more time I see that it’s actually
super hard to figure out what would be important to work on. Like, sure, I can
make a computer do a billion things (literally! That’s pretty easy!), but
*which billion things exactly*? What will have a lot of impact? What will help
my company do better?


Once, a little while after I started at my current job,
I told my manager “hey, I’m thinking of doing $thing”. He said “ok, what if
you do $other_thing instead?” So I built the first version of the thing he
suggested (a small system for making it easier to keep track of your machine
learning experiments), and two years later it’s something that the team still
uses and that a bunch of other people have built on top of. It turns out that
it was a good idea!


When I started programming, I thought that people would tell me what code to
write, and then I would write that code, and then that would be all. That is
not how it’s been, even though certainly I get guidance along the way. I work
for a place that gives its engineers a lot of autonomy.


So instead, for me, it’s been more like:

- well we have this one long-term goal, or three, or six
- also a bunch of minor problems of varying urgency
- now it’s up to you to figure out which ones would be good to solve
right now
- also you have to figure out how to solve them
- also the problems might be impossible to solve
- and there are all these other external factors
- you get to talk to a bunch of people who have thought about these
problems for a while to do it though!
- here’s 40 hours a week. go.


### know what your goals are


So, how do you decide what to **do**?


I have a coworker Cory Watson who gave this cool talk at Monitorama
called [Creating a Culture of Observability](http://onemogin.com/observability/stripe/culture/monitoring/monitorama/creating-a-culture-of-observability.html).


He describes what he’s doing as follows on that page:


> In other words, if our sensors — think about metrics, logs and traces —
> are good, then we can learn about how effectively our systems are
> working!


> My job at Stripe is to make this fucking awesome.


It is kind of obvious when working with Cory that he is relentlessly focused
on making it easier to know what our software systems are doing. And it helps!
The company’s dashboards and metrics have gotten way better as a result. It’s
easier to make performance improvements and detect and understand errors.


My friend Anton who made that transit maps app, cares SO MUCH about how to
represent public transit information and he thinks about it all the time so
it’s not that surprising to me that he’s built an awesome way to do it.


I think this kind of focus is incredibly helpful – when I don’t have a clear
goal, I find it really really hard to get things done or decide what to do. I
think of this as kind of the “can I explain my job to someone at a party?”
test. When I can’t pass this test (especially if the person at the party is a
software engineer) I feel uncomfortable.


Obviously you don’t need to always focus on the same thing (jeff dean is
like a legend at Google or something and I think he’s done a ton of
different thing), but having a focus seems really important.


### coming up with a focus is not that easy


At work there are a lot of possible things to think about! And as a single
person (not a manager), there’s only so much you can focus on at a time. Some
things I see people working on:

- Our storage systems are super-reliable and easy to use
- It’s easy to tell what your code is doing, in real time
- Make the development experience really good and easy
- Make the dashboard an awesome place for our users to understand their business


So somehow I need to find a thing that is big enough and important enough to
focus on (can i explain to my colleagues why i’m doing what i’m doing?), but
also small enough that a single person (or small group) can make progress on
it. And then it is way easier to write code towards that vision!


### there’s no one “right thing”


I originally called this post “how do you work on the right thing?” I retitled
it because I think that that’s a wrong (and kind of dangerous) wording –
there is no one right thing to work on. I work with many many excellent people
who are working on many many important things. Not all things are equally
impactful (which is what this post is all about!), but it’s about reliably
finding useful things to work on that are within your capabilities, not
finding a global optimum.


If I only wrote globally optimal blog posts I would literally never publish
anything.


### believe it’s possible


One thing about working on long-term or ambitious projects is – you **have**
to believe that you can do the project. If you start a cool year-long project,
approximately 50 million things will go wrong along the way. Things you didn’t
expect to break will break. And if you give up when you have a bad week or
three weeks or somebody doesn’t believe that what you’re doing is right, you
will never finish.


I think this is a really important thing a mentor / more senior person
can do for someone more junior. A lot of the time you can’t
tell what’s possible and what’s impossible and what obstacles are fine and
what obstacles are insurmountable. But this can be
bootstrapped! If someone tells you “don’t worry, it’ll all work out!”,
then you can start, and hit the problems, and ask for advice, and keep
going, and emerge victorious.


And once you have emerged victorious enough times (and failed enough
times!), you can start to get a sense for which things will work and
which things will not work, and decide where to persevere.


People talk a lot about ‘agile’ and MVPs but I don’t think that’s a complete
answer here – sometimes you need to build a big thing, and you can write
design docs and prototypes, but ultimately you need to decide that damnit,
it’s going to work, and commit to spending a long time building it and showing
intermediate progress when you can.


Also your organization needs to support you in your work – it’s very hard to
get anything done if the people around you don’t believe that you can get it
done.


### I’m not in undergrad anymore


I *loved* being a math/CS undergrad. My professors would give me a series of
challenging assignments which were hard but always within my abilities. I
improved gradually over time! It was so fun! I was awesome at it! But it is
over.


Being employed is more like – I have a series of tasks which range from
totally trivial to I-don’t-even-know-where-to-start and I need to figure out
how to interrogate people and build up my skills so that I can do the hard
things. And I need to decide what “good enough” means for the things I do
decide to do, and nobody will do it for me, not really. There’s an interesting
comment by Rebecca Frankel that Dan Luu pointed me to, on
[this post](http://steve-yegge.blogspot.ca/2008/06/done-and-gets-things-smart.html)


> I agree with Steve Yegge’s assertion that there are an enormously important
> (small) group of people who are just on another level, and ordinary smart
> hardworking people just aren’t the same. Here’s another way to explain why
> there should be a quantum jump – perhaps I’ve been using this discussion to
> build up this idea: it’s the difference between people who are still trying
> to do well on a test administered by someone else, and the people who have
> found in themselves the ability to grade their own test, more carefully,
> with more obsessive perfectionism, than anyone else could possibly impose on
> them.


So somehow working on an important thing and doing it well means you have to
decide what your goals are and also build your own internal standards for
whether or not you’ve met them. And other people can help you get started with
that, but ultimately it’s up to you.


### some disconnected thoughts that feel useful

- Maggie talked about “postmortem-driven development” – look at things that have broken several times! see if you can help them not break again!
- It’s normal (and important!!) to do experiments that fail. Maybe the trick is to timebox those experiments and recognize when you’re doing something risky / new.


### I don’t know!


I feel weird admitting that I really struggle with this, but I really struggle
with this. I do not always have good ideas about what to build. Sometimes I
have ideas that I think are good and I do them and they’re great, and
sometimes I have ideas and I do them and they’re… really not great. Sometimes
I have standards for my work that I cannot figure out how to meet and that’s
really frustrating.


Sometimes other people have ideas and I think they’re great and help build
those ideas and it’s amazing. That’s a really good feeling. So far the best
things I’ve worked on have been other people’s ideas that I got excited about.


Sometimes other people have ideas and I don’t understand what they’re talking
about for months until they build it and I’m like OH THAT IS REALLY COOL WOW
WOW WOW. Even reliably recognizing good ideas is hard!


Some links:

- [Data-Driven Products Now!](http://mcfunley.com/data-driven-products-now) is a talk by Dan McKinley about how to think about building consumer-facing web products.
- [The Secret to Growing Your Engineering Career If You Don’t Want to Manage](http://www.theeffectiveengineer.com/blog/secret-to-growing-software-engineering-career) (thanks to Emil Sit)
- [The Highest-Leverage Activities Aren’t Always Deep Work](http://www.theeffectiveengineer.com/blog/high-leverage-work-isnt-always-deep)
