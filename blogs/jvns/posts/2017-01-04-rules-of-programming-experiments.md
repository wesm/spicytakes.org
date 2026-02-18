---
title: "Rules of programming experiments"
date: 2017-01-04
url: https://jvns.ca/blog/2017/01/04/rules-of-programming-experiments/
slug: rules-of-programming-experiments
word_count: 291
---


Rules of programming experiments:

- it doesn’t have to be good
- it doesn’t have to work
- you have to learn something


I wrote this in a talk slide once:


![](https://jvns.ca/images/rust-talk/slide_08.png)


and I wanted to say a tiny bit more about it. I think one other thing
that defines “programming experiments” for me is – often the
experiment doesn’t take that much time (maybe 4 hours on a Wednesday
evening), and when I’m done I don’t have to maintain it or
anything. This makes it a lot more tractable for me than stuff like
“work on actual real open source projects” which I have exactly 0 energy
for after programming at work.


I also spent 12 weeks doing programming experiments full time at the [recurse
center](https://www.recurse.com/) and it was awesome. These days I have
substantially less time to devote to them :)


A few examples of things that have fallen into this category for me:

- [Spending some time on a train running strace on “killall”](http://jvns.ca/blog/2013/12/22/fun-with-strace/)
- [writing an operating system in rust](http://jvns.ca/blog/2014/03/12/the-rust-os-story/) (this took 3 weeks which is a pretty long time, but fell very far short of “operating system”, and I learned a ton. huge success.)
- investigating Hadoop by stracing some code that interacts with HDFS ([diving into HDFS](http://jvns.ca/blog/2014/05/15/diving-into-hdfs/))
- [how does SQLite work?](http://jvns.ca/blog/2014/09/27/how-does-sqlite-work-part-1-pages/)
- [learning about LD_PRELOAD](http://jvns.ca/blog/2014/11/27/ld-preload-is-super-fun-and-easy/)


and, well, a bunch more on this blog. I think it’s an interesting
reason to write programs because the program itself is totally
incidental (I usually put them on the internet, but certainly not for
anyone to *use* or anything). It’s more about

- does this work?
- what happens if I do *this*?
- can I write a small program that helps me look at
IMPORTANT_NEW_CONCEPT? (like threading?)
