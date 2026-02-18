---
title: "Status update, April 2020"
date: 2020-04-15
url: https://drewdevault.com/2020/04/15/Status-update-April-2020.html
slug: Status-update-April-2020
word_count: 403
---

Wow, it’s already time for another status update? I’m starting to lose track of
the days stuck inside. I have it easier than many - I was already used to
working from home before any of this began. But, weeks and weeks of not spending
IRL time with anyone else is starting to get to me. Remember to call your
friends and family and let them know how you’re doing. Meanwhile, I’ve had a
productive month - let’s get you up to date!

In the Wayland world, I’ve made some more progress on the book. The input
chapter is now finished, including the example code. The main things which
remain to be written are the XDG positioner section (which I am dreading), drag
and drop, and protocol extensions. On the code side of things, wlroots continues
to see gradual improvements — the DRM (not the bad kind) implementation
continues to see improvements, expanding to more and more use-cases with even
better performance. Sway has also seen little bug fixes here and there, and
updates to keep up with wlroots.

For my part, I’ve mostly been focused on SourceHut and Secret Project this
month. On the SourceHut side of things, I’ve been working on hub.sr.ht, and on
an experimental GraphQL-based API for git.sr.ht. The former is progressing quite
well, and I hope to ship an early version before the next status update. As for
the latter, it’s still very experimental, but I am optimistic about it. I have
felt that the current REST API design was less than ideal, and the best time to
change it would be during the alpha. The GraphQL design, while it has its
limitations, is a lot better than the REST design and should make it a lot
easier for services to interop with each other - which is a core design need for
sr.ht.

Here’s a little demo of hub.sr.ht as of a few weeks ago to whet your appetite:

As far as the secret project is concerned, here’s another teaser:

```
fn printf (fmt: str, ...) int;

fn f (ptr: &int) int =
{
	let x: int = *ptr;
	free ptr;
	printf("value: %d\n", x)
};

export fn main int =
{
	let x = alloc &int 10;
	f(^x);
	0
};
```

```
$ [redacted] -o example [redacted...]
$ ./example
value: 10
```

That’s all for today! I’ll see you again next month. Thank you for your support!
