---
title: "Don’t Reinvent The Wheel, Unless You Plan on Learning More About Wheels"
date: 2009-02-07
url: https://blog.codinghorror.com/dont-reinvent-the-wheel-unless-you-plan-on-learning-more-about-wheels/
slug: dont-reinvent-the-wheel-unless-you-plan-on-learning-more-about-wheels
word_count: 761
---

The introduction to [Head First Design Patterns](https://blog.codinghorror.com/head-first-design-patterns/) exhorts us **not to reinvent the wheel**:


> You’re not alone. At any given moment, somewhere in the world someone struggles with the same software design problems you have. You know you don’t want to reinvent the wheel (or worse, a flat tire), so you look to Design Patterns – the lessons learned by those who’ve faced the same problems. With Design Patterns, you get to take advantage of the best practices and experience of others, so that you can spend your time on … something else. Something more challenging. Something more complex. Something more fun.


Avoiding the reinvention of the proverbial wheel is a [standard bit of received wisdom](http://sourcemaking.com/antipatterns/reinvent-the-wheel) in software development circles. There’s certainly truth there, but I think it’s a bit dangerous if taken too literally – if you **categorically deny all attempts to solve a problem with code once any existing library is in place**.


![](https://blog.codinghorror.com/content/images/2025/04/image-299.png)


I’m not so sure. I think reinventing the wheel, if done properly, can be useful. For example, [James Hart reinvented the wheel](https://web.archive.org/web/20090211143931/http://blogs.ipona.com/james/archive/2008/03/17/Reinventing-Linq.aspx). And he liked it:


> I reinvented the wheel last week. I sat down and deliberately coded something that I knew already existed, and had probably also been done by many many other people. In conventional programming terms, I wasted my time. But it was worthwhile, and what’s more I would recommend almost any serious programmer do precisely the same thing.


But who’s James Hart? Just another programmer. If that doesn’t carry enough weight for you, how does it sound coming from Charles Moore, [the creator of FORTH?](http://www.forth.com/resources/evolution/evolve_1.html)


> A second corollary was even more heretical: “Do it yourself!”
> *The conventional approach, enforced to a greater or lesser extent, is that you shall use a standard subroutine. I say that you should write your own subroutines.
> Before you can write your own subroutines, you have to know how. This means, to be practical, that you have written it before; which makes it difficult to get started. But give it a try. After writing the same subroutine a dozen times on as many computers and languages, you’ll be pretty good at it.*
> Moore followed this to an astounding extent. Throughout the 70s, as he implemented Forth on 18 different CPUs, he invariably wrote for each his own assembler, his own disk and terminal drivers, even his own multiply and divide subroutines (on machines that required them, as many did). When there were manufacturer-supplied routines for these functions, he read them for ideas, but never used them verbatim. By knowing exactly how Forth would use these resources, by omitting hooks and generalities, and by sheer skill and experience (he speculated that most multiply/divide subroutines were written by someone who had never done one before and never would again), his versions were invariably smaller and faster, usually significantly so.
> Moreover, he was never satisfied with his own solutions to problems. Revisiting a computer or an application after a few years, he often re-wrote key code routines. He never re-used his own code without re-examining it for possible improvements. This later became a source of frustration to Rather, who, as the marketing arm of FORTH, Inc., often bid jobs on the assumption that since Moore had just done a similar project this one would be easy – only to watch helplessly as he tore up all his past code and started over.


And then there’s [Bob Lee](https://web.archive.org/web/20090211083104/http://crazybob.org/2007/09/why-reinvent-wheel.html), who leads the core library development on [Android](http://android.com/).


> Depending on the context, you can almost always replace “Why reinvent the wheel?” with “Please don’t compete with me,” or “Please don’t make me learn something new.” Either way, the opponent doesn’t have a real argument against building something newer and better, but they also don’t want to admit their unhealthy motivations for trying to stop you.
> More seeds, more blooms, I say. Don’t build houses on kitchen sinks. Reinvent away. **Most of our current technology sucks, and even if it didn’t, who am I to try and stop you?**


Indeed. If anything, “Don’t Reinvent The Wheel” should be used as a call to arms for deeply educating yourself about all the existing solutions – not as a bludgeoning tool to undermine those who legitimately want to build something better or improve on what’s already out there. In my experience, sadly, it’s much more the latter than the former.


So, no, you shouldn’t reinvent the wheel. **Unless you plan on learning more about wheels**, that is.

[design patterns](https://blog.codinghorror.com/tag/design-patterns/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[best practices](https://blog.codinghorror.com/tag/best-practices/)
[coding](https://blog.codinghorror.com/tag/coding/)
[software design](https://blog.codinghorror.com/tag/software-design/)
