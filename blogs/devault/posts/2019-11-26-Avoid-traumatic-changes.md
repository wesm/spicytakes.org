---
title: "Software developers should avoid traumatic changes"
date: 2019-11-26
url: https://drewdevault.com/2019/11/26/Avoid-traumatic-changes.html
slug: Avoid-traumatic-changes
word_count: 755
---

A lot of software has gone through changes which, in retrospect, I would
describe as “traumatic” to their communities. I recognize these sorts of changes
by their effect: we might have pulled through in the end, but only after a lot
of heartbreak, struggle, and hours of wasted hacking; but the change left a scar
on the community.

There are two common cases in which a change risks introducing this kind of
trauma:

1. It requires everyone in the community, or nearly everyone, to overhaul their
code to get it  **working**  again
2. It requires everyone in the community, or nearly everyone, to overhaul their
code to get it  **idiomatic**  again

Let’s call these cases, respectively, strong and weak trauma. While these are
both traumatic changes, the kind of trauma they inflict on the community is
different. The first kind is more severe, but the latter is a bad idea, too. We
can examine these through two case-studies in Python: the (in)famous transition
to Python 3, and the less notorious introduction of asyncio.

In less than one month, Python 2 will reach its end of life, and even as a
staunch advocate of Python 3, I too have some software which is not going to
make it to the finish line in time 1 . There’s no doubt that Python 3 is much,
much better than Python 2. However, the transition was poorly handled, and
upgrading can be no small task for some projects. The result has been hugely
divisive and intimately familiar to anyone who works with Python, creating
massive rifts in the community and wasting millions of hours of engineer time
addressing. This kind of “strong” trauma is fairly easy to spot in advance.

The weaker kind of traumatic change is more subtle, and less talked about. It’s
a slow burn, and it takes a long time for its issues to manifest. Consider the
case of asyncio: clearly it’s an improvement for Python, whose previous attempts
at concurrency have fallen completely flat. The introduction of async/await and
coroutines throughout the software ecosystem is something I’m generally very
pleased about. You’ll see me reach for threads to solve a problem when hell
freezes over, and no earlier, so I’m quite fond of first-class coroutines.

Unfortunately, this has a chilling effect on existing Python code.  The
introduction of asyncio has made large amounts of code idiomatically obsolete.
Requests, the darling of the Python world, is effectively useless in a
theoretical idiomatic post-asyncio world. The same is true of Flask, SQLAlchemy,
and many, many other projects. Just about anything that does I/O is unidiomatic
now.

Since nothing has actually  *broken*  with this change, the effects are more
subtle than with strong traumatic changes. The effect of asyncio has been to
hasten the onset of code rot. Almost all of SourceHut’s code pre-dates asyncio,
for example, and I’m starting to feel the limitations of the pre-asyncio model.
The opportunity to solve this problem by rewriting with asyncio in mind,
however, also presents me a chance to rewrite in anything else, and reevaluate
my choice of Python for the project entirely. It’s a tough decision to think
about — the mature and diverse ecosystem of libraries that help to make a
case for Python is dramatically reduced when asyncio support is a consideration.

It may take years for the trauma to fully manifest, but the rift is still there
and can only grow. Large amounts of code is rotting and will have to be thrown
away for the brave new asyncio world. The introduction of asyncio has made
another clear “before” and “after” in the Python ecosystem. The years in between
will be rough, because all new Python code will either leverage the rotting
pre-asyncio ecosystem or suffer through an immature post-asyncio ecosystem.
It’ll likely turn out for the better — years from now.

And sometimes these changes  *are*  for the better, but they should be carefully
thought out, and designed to minimize the potential impact. In practical terms,
it’s for this reason that I urge caution with ideas like adding generics to
Go. In a post-generics world, a large amount of the Go ecosystem will suddenly
become unidiomatic, and breaking changes will required to bring it up to spec.
Let’s think carefully about it, eh?

1. Eh, kind of. I’m theoretically behind the effort to drop Python 2 from Alpine Linux, but the overhaul is tons of work and the time I can put into the effort isn’t going to be enough to finish before 2020. ↩︎
