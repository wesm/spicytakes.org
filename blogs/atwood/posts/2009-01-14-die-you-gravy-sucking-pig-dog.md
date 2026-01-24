---
title: "Die, You Gravy Sucking Pig Dog!"
date: 2009-01-14
url: https://blog.codinghorror.com/die-you-gravy-sucking-pig-dog/
slug: die-you-gravy-sucking-pig-dog
word_count: 743
---

In the C programming language, you’re regularly forced to deal with the painful, dangerous concepts of pointers and explicit memory allocation.

kg-card-begin: html

```

b1 = (double *)malloc(m*sizeof(double));

```

kg-card-end: html

In modern garbage collected programming languages, life is much simpler; you simply new up whatever object or variable you need.

kg-card-begin: html

```

Double[] b1 = new Double[m];

```

kg-card-end: html

Use your objects, and just walk away when you’re done. The garbage collector will cruise by periodically, and when he sees stuff you’re not using any more, he’ll clean up behind you and deal with all that nasty pointer and memory allocation stuff on your behalf. It’s totally automatic.


Pretty awesome, right? I’d wager the majority of programmers alive today have never once worried about `malloc()`. I call this progress, [as does Jamie Zawinski](http://www.jwz.org/doc/gc.html):


> Based on my experience using both kinds of languages, for years at a stretch, I claim that a good garbage collector always beats doing explicit malloc/free in both computational efficiency and programmer time.
> However, I also claim that, because of the amount of programmer time that is saved by using GC rather than explicit malloc/free, as well as the dramatic reduction in hard-to-debug storage-management problems, even using a mediocre garbage collector will still result in your ending up with better software faster.
> Most of the time, throwing memory and CPU at the problem is still [cheaper than throwing programmer time](https://blog.codinghorror.com/hardware-is-cheap-programmers-are-expensive/) at the problem, even when you multiply the CPUs/memory by the number of users. This isn’t true all the time, but it’s probably true more often than you think, because [Worse is Better](https://blog.codinghorror.com/is-worse-really-better/).


But even for programmers who have enjoyed automatic garbage collection their whole careers, there are still some... oddities. See if you can spot one here:

kg-card-begin: html

```

sqlConnection.Close();
sqlConnection.Dispose();
sqlConnection = null;

```

kg-card-end: html

That is one hellaciously *closed* database connection. Why don’t you take it out back and shoot it, while you’re at it?


Even with your friendly neighborhood garbage collector making regular rounds on commodity desktops/servers where many gigabytes of main memory are commonplace, there are still times when you need to release precious resources *right now*. Not at some unspecified point in the future, whenever the GC gets around to it. Like, say, a database connection. Sure, your database server may be powerful, but it doesn’t support an infinitely large number of concurrent connections, either.


The confusing choice between setting an object to `null` and calling the `Dispose` method doesn’t help matters any. Is it even clear what state the connection is in after `Close` is called? Could the connection be reused at that point?


Personally, **I view explicit disposal as more of an optimization than anything else**, but it can be a pretty important optimization on a heavily loaded webserver, or a performance intensive desktop application plowing through gigabytes of data.


Of course, your average obsessive-compulsive developer sees that he’s dealing with a semi-precious system resource, and immediately takes matters into his own hands, because he [can do a better job](https://blog.codinghorror.com/im-smarter-than-the-runtime/) than the garbage collector. K. Scott Allen proposes a solution that might mollify both camps in [Disposal Anxiety](http://odetocode.com/Blogs/scott/archive/2004/11/07/605.aspx):

kg-card-begin: html

> What the IDisposable interface needs is a method that promotes self-efficacy in a developer. A method name that can stir up primal urges as the developer types. What we need is a method like the one in BSD’s [shutdown.c](http://www.freebsd.org/cgi/cvsweb.cgi/~checkout~/src/sbin/shutdown/shutdown.c?rev=1.26&content-type=text/plain) module.
> die_you_gravy_sucking_pig_dog()
> {
> char *empty_environ[] = { NULL };
> syslog(LOG_NOTICE, “%s by %s: %s”,
> doreboot ? “reboot” : dohalt ? “halt” : dopower ? “power-down” :
> “shutdown”, whom, mbuf);
> (void)sleep(2);
> (void)printf(“rnSystem shutdown time has arrived0707rn”);
> if (killflg) {
> (void)printf(“rbut you’ll have to do it yourselfrn”);
> exit(0);
> }
> Now, I know this function was written back in the days when steam engines still ruled the world, but we could modernize the function by applying some .NET naming standards.
> sqlConnection.**DieYouGravySuckingPigDog()**;
> Can you feel the passion behind this statement? This statement carries the emotion that is hard to find in today’s code. I hope you’ll support this proposal. Good people will be able to sleep at night once again.

kg-card-end: html

So the next time *you* feel anxious about letting objects fall out of scope, remember: **you could always terminate them with extreme prejudice**, if you feel it’s necessary.


But it probably isn’t.

[c programming](https://blog.codinghorror.com/tag/c-programming/)
[pointers](https://blog.codinghorror.com/tag/pointers/)
[memory allocation](https://blog.codinghorror.com/tag/memory-allocation/)
[garbage collection](https://blog.codinghorror.com/tag/garbage-collection/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
