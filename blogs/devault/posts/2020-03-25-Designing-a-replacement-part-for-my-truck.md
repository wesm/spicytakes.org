---
title: "Designing and 3D printing a new part for my truck"
date: 2020-03-25
url: https://drewdevault.com/2020/03/25/Designing-a-replacement-part-for-my-truck.html
slug: Designing-a-replacement-part-for-my-truck
word_count: 628
---

I drove a car daily for many years while I was living in Colorado, California,
and New Jersey, but since I moved to Philadelphia I have not needed a car. The
public transit here is not great, but it’s good enough to get where I need to be
and it’s a lot easier than worrying about parking a car. However, in the past
couple of years, I have been moving more and more large server parts back and
forth to the datacenter for SourceHut. I’ve also developed an interest in
astronomy, which benefits from being able to carry large equipment to remote
places. These reasons, among others, put me into the market for a vehicle once
again.

I think of a vehicle strictly as a functional tool. Some creature comforts are
nice, but I consider them optional. Instead, I prioritize utility. A truck makes
a lot of sense — lots of room to carry things in. And, given my expected
driving schedule of “not often”, I wasn’t looking to spend a lot of money or
get a loan. There are other concerns: modern cars are very complicated machines,
and many have lots of proprietary computerized components which make end-user
maintenance very difficult. Sometimes manufacturers even use cryptography and
legal threats to bring cars into their dealerships, bullying out third-party
repairs.

To avoid these, I got an older truck: a 1984 Dodge D250. It’s a much simpler
machine than most modern cars, and learning how to repair and maintain it is
something I can do in my spare time.

It’s an old truck, and the previous owners were not negligent, but also didn’t
invest a lot of time or money in the vehicle’s upkeep. The first problem I hit
was the turn signal lever snapping and becoming slack, which I fixed by pulling
open the steering column, re-aligning the lever, and tightening an internal
screw. The more interesting problem, however, was this:

This plastic part holds an arm in place, which is engaged by a lever in the
center of the window which folds closed over the truck bay. It’s used to hold
the window in place and provides a weak locking mechanism. When the arm is
allowed to move freely, it can clang around while I’m driving, and can make
opening the truck bay a frustrating procedure. I have been looking for a reason
to learn how to use  [solvespace](http://solvespace.com/index.pl) , and this
seemed like a great start.

I ordered a caliper 1  and measured the dimensions of the broken part, and took
pictures of it from several angles for later reference. I took some notes:

Then, I used solvespace to design the following part:

This was the third iteration — I printed one version, brought it out to
the truck to compare with the broken part, made refinements to the design, then
rinse and repeat. Here’s an earlier revision being compared with the broken
piece:

Finally, I arrived at a design I liked and sent it to the printer.

I took some pliers to the remaining plastic bits from the broken part, and sawed
off the rivets. I attached the replacement with superglue and ta-da!

If the glue fails, I’ll drill out what’s left of the rivets and secure it with
screws. This may require another revision of the design, which will also give me
a chance to address some minor shortcomings. I don’t expect to need this,
though, because this is not part under especially high stress.

You can get the CAD files and an STL from my  [repository
here](https://git.sr.ht/~sircmpwn/open-dodge-d250) , which I intend to keep
updating as I learn more about this truck and encounter more fun problems to
solve.

1. Oh man, I’ve always wanted a caliper, and now I have an excuse! ↩︎
