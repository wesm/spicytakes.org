---
title: "Principles for C programming"
date: 2017-03-15
url: https://drewdevault.com/2017/03/15/How-I-learned-to-stop-worrying-and-love-C.html
slug: How-I-learned-to-stop-worrying-and-love-C
word_count: 1090
---

In the words of Doug Gwyn, “Unix was not designed to stop you from doing stupid
things, because that would also stop you from doing clever things”. C is a very
powerful tool, but it is to be used with care and discipline. Learning this
discipline is well worth the effort, because C is one of the best programming
languages ever made. A disciplined C programmer will…

**Prefer maintainability** . Do not be clever where cleverness is not required.
Instead, seek out the simplest and most understandable solution that meets the
requirements. Most concerns, including performance, are secondary to
maintainability. You should have a performance budget for your code, and you
should be comfortable spending it.

As you become more proficient with the language and learn about more features
you can take advantage of, you should also be learning when not to use them.
It’s more important that a novice could understand your code than it is to use
some interesting way of solving the problem. Ideally, a novice will understand
your code  *and*  learn something from it. Write code as if the person maintaining
it was you, circa last year.

**Avoid magic** . Do not use macros 1 . Do not use a typedef to hide a pointer or
avoid writing “struct”. Avoid writing complex abstractions. Keep your build
system simple and transparent. Don’t use stupid hacky crap just because it’s a
cool way of solving the problem. The underlying behavior of your code should be
apparent even without context.

One of C’s greatest advantages is its transparency and simplicity. This should
be embraced, not subverted. But in the fine C tradition of giving yourself
enough rope to hang yourself with, you can use it for magical purposes. You
must not do this. Be a muggle.

**Recognize and avoid dangerous patterns** . Do not use fixed size buffers with
variable sized data - always calculate how much space you’ll need and allocate
it. Read the man pages for functions you use and handle their failure modes.
Immediately convert unsafe user input into sanitized C structures. If you later
have to present this data to the user, keep it in C structures until the last
possible moment. Learn of and use extra care around sensitive functions like
strcat.

Writing C is sometimes like handling a gun. Guns are important tools, but
accidents with them can be very bad. You treat guns with care: you don’t point
them at anything you love, you exercise good trigger discipline, and you treat
it like it’s always loaded. And like guns are useful for making holes in things,
C is useful for writing kernels with.

**Take care organizing the code** . Never put code into a header. Never use the
 `inline`  keyword. Put separate concerns in separate files. Use static functions
liberally to organize your logic. Use a coding style that gives everything
enough breathing room to be easy on the eyes. Use single letter variable names
when their purpose is self-evident and descriptive names when it’s not, and
avoid neither.

I like to organize my code into directories that implement some group of
functions, and give each function its own file. This file will often contain
lots of static functions, but they all serve to organize the behavior this file
is responsible for implementing. Write up a header to give others access to
this module. And use the Linux kernel coding style, god dammit.

**Use only standard features** . Do not assume the platform is Linux. Do not
assume the compiler is gcc. Do not assume the libc is glibc. Do not assume the
architecture is x86. Do not assume the coreutils are GNU. Do not define
_GNU_SOURCE.

If you must use platform-specific features, describe an interface for it,
then write platform-specific support code separately. Under no circumstances
should you ever use gcc extensions or glibc extensions. GNU is a blight on this
Earth, do not let it infect your code.

**Use a disciplined workflow** . Have a disciplined approach to version control,
too. Write thoughtful commit messages - briefly explain the change in the first
line, and add justification for it in the extended commit message. Work in
feature branches with clearly defined goals, and do not include changes that
don’t serve that goal. Do not be afraid to rebase and edit your branch’s history
so that it presents your changes clearly.

When you have to return to your code later, you will be thankful for the
detailed commit message you wrote. Others who interact with your code will be
thankful for this as well. When you see some stupid code, it’s nice to know what
the bastard was thinking at the time, especially when the bastard in question
was you.

**Do strict testing and reviews** . Identify the different possible code paths
that your changes may take. Test each of them for the correct behavior. Give it
incorrect input. Give it inputs that could “never happen”. Pay special attention
to error-prone patterns. Look for places to simplify the code and make the
processes clearer.

Next, give your changes to another human to review. This human should apply the
same process and sign off on your changes. Review with discipline as well,
taking all of the same steps. Review like it’ll be your ass on the line if
there’s a problem with this code.

**Learn from mistakes** . First, fix the bug. Then, fix the real bug: your
process allowed this mistake to happen. Bring your code reviewer into the
discussion - this is their fault, too. Critically examine the process of
writing, reviewing, and deploying this code, and seek out the root cause.

The solution might be simple, like adding strcat to the list of functions that
should trigger your “review this code carefully” reflex. It might be employing
static analysis so a computer can detect this problem for you. Perhaps the code
needs to be refactored so it’s simpler and easier to spot errors in. Failing to
reflect on how to avoid future fuck-ups would be the real fuck-up here.

It’s important to remember that rules are made to be broken. There may be cases
where things that are discouraged should be used, and things that are encouraged
disregarded. You should strive to make such cases the exception, not the norm,
and carefully justify them when they happen.

C is the shit. I love it, and I hope more people can learn to see it the way I
do. Good luck!

1. Defining constants with them is fine, though ↩︎
