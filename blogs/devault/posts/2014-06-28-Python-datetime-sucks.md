---
title: "Python's datetime sucks"
date: 2014-06-28
url: https://drewdevault.com/2014/06/28/Python-datetime-sucks.html
slug: Python-datetime-sucks
word_count: 502
---

I’ve been playing with Python for about a year now, and I like pretty much
everything about it. There’s one thing that’s really rather bad and really should
not be that bad, however - date & time support. It’s ridiculous how bad it is in
Python. This is what you get with the standard datetime module:

* The current time and strftime, with a reasonable set of properties
* Time deltas with days, seconds, and microseconds and nothing else
* Acceptable support for parsing dates and times

What you don’t get is:

* Meaningful time deltas
* Useful arithmetic

Date and time support is a rather tricky thing to do and it’s something that the
standard library should support well enough to put it in the back of your mind
instead of making you do all the work.

We’ll be comparing it to C# and .NET.

Let’s say I want to get the total hours between two  `datetime` s.

```
// C#
DateTime a, b;
double hours = (b - a).TotalHours;
```

```
# Python
a, b = ...
hours = (b - a).seconds / 60 / 60
```

That’s not so bad. How about getting the time exactly one month in the future:

```
var a = DateTime.Now.AddMonths(1);
```

```
a = date.now() + timedelta(days=30)
```

Well, that’s not ideal. In C#, if you add one month to Janurary 30th, you get
Feburary 28th (or leap day if appropriate). In Python, you could write a janky
function to do this for you, or you could use the crappy alternative I wrote
above.

How about if I want to take a delta between dates and show it somewhere, like a
countdown? Say an event is happening at some point in the future and I want to
print “3 days, 5 hours, 12 minutes, 10 seconds left”. This is distinct from the
first example, which could give you “50 hours”, whereas this example would give
you “2 days, 2 hours”.

```
DateTime future = ...;
var delta = future - DateTime.Now;
Console.WriteLine("{0} days, {1} hours, {2} minutes, {3} seconds left",
    delta.Days,
    delta.Hours,
    delta.Minutes,
    delta.Seconds);
```

```
# ...mess of math you have to implement yourself omitted...
```

Maybe I have a website where users can set their locale?

```
DateTime a = ...;
Console.WriteLine(a.ToString("some format string", user.Locale));
```

```
locale.setlocale(locale.LC_TIME, "sv_SE") # Global!
print(time.strftime("some format string"))
```

By the way, that Python one doesn’t work on Windows. It uses system locales names
which are different on Windows than on Linux or OS X. Mono (cross-platform .NET)
handles this for you on any system.

And a few other cases that are easy in .NET and not in Python:

* Days since the start of this year
* Constants like the days in every month
* Is it currently DST in this timezone?
* Is this a leap year?

In short, Python’s datetime module could really use a lot of fleshing out. This
is common stuff and easy for a naive programmer to do wrong.
