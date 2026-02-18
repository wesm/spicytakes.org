---
title: "Asking good questions is hard (but worth it)"
date: 2016-08-31
url: https://jvns.ca/blog/2016/08/31/asking-questions/
slug: asking-questions
word_count: 1669
---


I just read this wonderful article by Duretti Hirpa “[Confronting Jargon
](https://medium.com/@duretti/confronting-jargon-7d39c8dd9353)” which talks about (among other things) asking questions and not knowing things at work.


One thing about asking questions that I think doesn’t always get enough
appreciation is that asking good questions is a **skill**. It’s something that
you can practice and get better at.


Asking questions is super hard. Sometimes if there’s a topic I’m really
confused about, I need to concentrate for like 10 minutes to actually come up
with a more coherent question that “what? I don’t get it?”.


Every month or two, I go to the Papers We Love meetup in Montreal, where
people present on computer science papers they loved. And every meetup, the
organizer starts by saying “this is a meant to be a discussion, please feel
free to ask questions, even stupid questions”.


The last paper was about compiler optimizations (“the nanopass compiler”)! The
presenter (who did a great job) started out by talking about how when Erlang
compiler compiles your Erlang into bytecode, it goes through 5 phases (erlang
source, the AST, some intermediate representation, some other intermediate
representation, bytecode). I knew that other compilers had less intermediate
representations, so I asked why Erlang was different! He said it helped them do
more compiler optimizations.


I really like asking questions at meetups like this because I get to learn
about cool computer science papers, and I think asking relatively basic
questions helps other people see that they can also ask! Usually I try to ask
a couple of questions early on and then if I see that other people are asking
lots of questions I stop unless I have something I really want to
know.


### some questions are better than others


Finding questions to ask that get people to tell you AMAZING THINGS isn’t
always easy. But sometimes I stumble upon MAGICAL QUESTIONS that unearth
hidden huge amounts of knowledge. For example! The question
[Why do we use the Linux kernel’s TCP stack?](http://jvns.ca/blog/2016/06/30/why-do-we-use-the-linux-kernels-tcp-stack/) resulted in:

- a great post on the Cloudflare blog [Why we use the Linux kernel’s TCP stack](https://blog.cloudflare.com/why-we-use-the-linux-kernels-tcp-stack/)
- some quite good [comments on HN](https://news.ycombinator.com/item?id=12021195)


So! Given that many questions don’t result in interesting new knowledge (“is
vim or emacs better?” being perhaps the worst offender), how do we find ones
that are good? Here are some ideas for questions to ask.


### Summarize your understanding


“how does X work?” is actually a really hard question to answer. The answerer has to figure out
what you already know about how X works, and what else you might need to know,
and maybe X is really complicated and they only have 10 minutes right now, and…


When I’m trying to get someone to explain a system to me at work, I like to
start by explaining my current understanding to them. This can look like

- me: so, we have 2 different DNS servers, right?
- them: oh actually we have 3!
- me: oh! what is the third one?


I really like this because it helps reveal misunderstandings I have (me: “so,
the 2 most important things about $system are A and B?” them: “the most
important thing is probably actually W”).


### be humble & curious


There’s this really delightful post by Erin Ptacek called [“be coachable”](http://sockpuppet.org/blog/2015/08/21/be-coachable/) about learning roller derby in her 40s. I think about this post a lot when someone who knows a lot more than me is trying to teach me a thing.


Every so often I will be asking questions about a THING and someone will say
(in a nice way!!) “Julia, you do not know how this thing works. You need to
learn how it works and then everything will be a lot more clear.” For instance
I used to work with Hadoop and for a while I had NO IDEA how Hadoop worked.
When I learned the basic Hadoop computation model everything got a lot easier.


When I discover yet another new thing that I need to know that I know
practically nothing about, sometimes it feels embarrassing! I sometimes feel
like “ugh, I’m practically 30, and I started learning to program when I was
15, and will I ever learn how computers work?”


The answer is probably that no, there will always be new computer things to
learn. And I mostly like that, even if I feel dumb sometimes! When I find out
that I don’t know an Important Thing that apparently everybody except me knew
I just take a deep breath and am like WELL I GUESS TODAY IS THE DAY I’M GOING
TO LEARN IT THEN. And the people are never jerks about it, because they all
have stuff that they don’t know, and it’s normal.


These days I’m learning a lot faster than I was when I was 15, so that’s
something :). Having a ton of awesome people to learn (hi, coworkers. hi,
internet) from makes a huge difference.


### How does THING work?


I said before that “How does X work?” isn’t the best question. But I do like
to ask about how things work.


One thing I really like to do on this blog is to write a small explanation
about how something works (“here are the first 5 things to know!”), and then
people often respond with a lot of extra interesting information that I didn’t
know.


For example, [how does strace work?](http://blog.packagecloud.io/eng/2016/02/29/how-does-strace-work/) [SQLite?](http://jvns.ca/blog/2014/09/27/how-does-sqlite-work-part-1-pages/) [gzip?](http://jvns.ca/blog/2013/10/24/day-16-gzip-plus-poetry-equals-awesome/).


### Is THING hard? Why is THING hard?


Some things are surprisingly hard (for instance, [benchmarking, printing floating point numbers](http://jvns.ca/blog/2016/07/23/rigorous-benchmarking-in-reasonable-time/), and getting people to work together effectively). Some other things are surprisingly easy! Like training a machine learning model is a complicated thing but actually logistic regression is pretty simple and sometimes it all Just Works.


It’s a really common saying that “there are two hard problems in programming – cache invalidation and naming things”. But why is cache invalidation hard, actually? What kinds of things normally go wrong?


It turns out that writing a really basic TCP stack (enough to let you get a website) is [surprisingly easy](http://jvns.ca/blog/2014/08/12/what-happens-if-you-write-a-tcp-stack-in-python/), something you can do in about a week, and once you know that, it turns out that writing a TCP stack that can actually handle the range of traffic you see on the internet is [surprisingly hard](https://news.ycombinator.com/item?id=12021195).


Once you learn more about which things are hard and which things are easy, you
can make more informed decisions about what projects to jump into, which is
the best.


### What did THING look like when it first existed?


I once needed to write an introduction to the Stripe API for new Stripe
employees. We ended up looking at the very first commit to the main repository
and seeing what it said. It turned out to be a surprisingly good introduction
to the codebase – some of the core objects hadn’t really changed since the
first commit.


Often asking questions about the history of something really helps me
understand how it came to be where it is today.


### What happens if you poke THING with a stick?


One of my very favorite kinds of questions to ask / things to investigate is – what if you take a normal thing, and do something weird to it? For example! Kamal has a really great talk called [Storing your data in kernel space](https://www.youtube.com/watch?v=gg0xNgHrAAc) where he puts a bunch of data inside pipe buffers in the kernel. This is not a normal thing to do.


It turns out when you use a lot of memory in this way, the Linux kernel will start killing processes. This is called the OOM killer! Creating weird edge cases on systems that aren’t important gives you a better sense of the edges of your system and how the underlying things work, which sometimes is Extremely Useful. [Rachel By The Bay](https://rachelbythebay.com/w/) is a great blog that talks about a lot of weird edge cases.


### Why is THING slow?


Performance benchmarking/analysis is a really fun rabbit hole, that can
unearth a lot of really weird behavior and interesting facts.


Investigating performance problems has taught me about [Java garbage collection](http://jvns.ca/blog/2016/04/22/java-garbage-collection-can-be-really-slow/) and [TCP_NODELAY](http://jvns.ca/blog/2015/11/21/why-you-should-understand-a-little-about-tcp/) and a bunch of other things.


And then often if I tell someone a performance story, they will tell me their
stories and I’ll learn something new!


### partial answers = amazing


I really frequently ask a question and provide a partial answer to give people
an idea of what I’m looking for. Often people will chime in with (“oh, you
missed this! you didn’t mention [amazing thing]”). And then I learn SO MUCH!


### asking questions is a service


And asking questions can be a huge service to other people. I sometimes review
other people’s talks and writing, and one of my favorite ways to do it is just
to give them questions that they haven’t answered that I think might help
their reader. Then they can decide if that’s a question they want to address
or not!


Once I wrote a guest blog post on Cathy O’Neil’s blog. She is hella good at
asking questions, and I didn’t know what to write, and she sent me a list of 5
questions she thought it would be useful for me answer in my post. Then
suddenly writing the guest blog post was SUPER EASY.


Or sometimes I’ll be in a meeting, and somebody will ask a super incisive
question that frames the problem in a way I hadn’t thought about before and
it’ll totally change the way I think about everything.


### practice helps.


I think it’s really fun and it’s been super valuable to me at work.


The more questions I ask, the better I get at asking questions that move the
conversation forward, that teach me (and other people!) something new, or
that help someone clarify what they’re saying.


And I think I’m getting better! One of my coworkers told me recently “julia,
you ask really good questions. I always want to take the time to answer them
properly” <3.
