---
title: "New zine: Bite Size Command Line!"
date: 2018-08-05
url: https://jvns.ca/blog/2018/08/05/new-zine--bite-size-command-line/
slug: new-zine--bite-size-command-line
word_count: 337
---


I released a new zine last week! It’s called “Bite Size Command Line”, and it’s explains the basics
of a bunch of Unix command line tools! I learned some useful new things by writing it, and I hope
you do too. You can get it for $10 at [https://wizardzines.com/zines/bite-size-command-line](https://wizardzines.com/zines/bite-size-command-line). It’s the sequel to
[Bite Size Linux](https://wizardzines.com/zines/bite-size-linux) which I released in April.


If you want to get an idea of what’s in it, I’ve been posting the work-in-progress comics along the
way on Twitter. You
can [see some of them on Twitter here](https://twitter.com/i/moments/1026078161115729920).


Here’s the table of contents:


### why I’m excited about this zine


Originally when I started working on this, I kind of didn’t think it was that exciting – I thought
“whatever, I know command line tools, I’ve been using Linux for 15 years”.


It turns out that I learned quite a few fun new tricks! I learned about:

- bash process substitution (`diff <(ls) (ls -a)`) which lets you avoid creating temporary files
- `sort -h` (“human sort”) which lets you sort the output of `du -sh` correctly
- the `w` option to ps will show all command line args, and `f` will show you a process tree (!!)
- and a bunch more nice tidbits!


### teaching the unix command line with less trial and error


But I’m particularly excited about the possibility that this can help **beginners** learn Linux!
Most command line tools have a TON of command line arguments, and it’s often hard to tell by reading
the man page which ones are crucial to know and which ones hardly anyone uses. I think a lot of this
knowledge often gets passed down verbally, which makes it harder to learn if you don’t know many
command line users. (if this is you, [https://tldr.sh/](https://tldr.sh/) is also a cool resource!)


So the goal of this zine is basically to be your helpful, more experienced friend who’s been using
these tools for a while and can tell you which bits are the most important.
