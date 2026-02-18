---
title: "The Abiopause"
date: 2020-03-03
url: https://drewdevault.com/2020/03/03/Abiopause.html
slug: Abiopause
word_count: 886
---

The sun has an influence on its surroundings. One of these is in the form of
small particles that are constantly ejected from the sun in all directions,
which exerts an outward pressure, creating an expanding sphere of particles that
moves away from the sun. These particles are the solar wind. As the shell of
particles expands, the density (and pressure) falls. Eventually the solar wind
reaches the  *interstellar medium*  — the space between the stars —
which, despite not being very dense, is not empty. It exerts a pressure that
pushes inwards, towards the sun.

Where the two pressures balance each other is an interesting place. The sphere
up to this point is called the  *heliosphere*  — which can be roughly
defined as the zone in which the influence of the sun is the dominant factor.
The  *termination shock*  is where the change starts to occur. The plasma from the
sun slows, compresses, and heats, among other changes. The physical interactions
here are interesting, but aren’t important to the metaphor. At the
termination shock begins the  *heliosheath* . This is a turbulent place where
particles from the sun and from the interstellar medium mix. The interactions in
this area are complicated and interesting, you should read up about it later.

Finally, we reach the  *heliopause* , beyond which the influence of the
interstellar medium is dominant. Once crossing this threshold, you are said to
have left the solar system. The Voyager 1 space probe, the first man-made object
to leave the solar system, crossed this point on August 25th, 2012. Voyager 2
completed the same milestone on November 12th, 2018 1 .

In the world of software, the C programming language clearly stands out as the
single most important and influential programming language.  Everything
forming the critical, foundational parts of your computer is written in it:
kernels, drivers, compilers, interpreters, runtimes, hypervisors, databases,
libraries, and more are almost all written in C. 2  For this reason, any
programming language which wants to get anything useful done is certain to
support a C FFI (foreign function interface), which will allow programmers to
communicate with C code from the comfort of a high-level language. No other
language has the clout or ubiquity to demand this level of deference from
everyone else.

The way that an application passes information back and forth with its
subroutines is called its  *ABI* , or application binary interface. There are a
number of ABIs for C, but the most common is the System-V ABI, which is used on
most modern Unix systems. It specifies details like which function parameters to
put in which registers, what goes on the stack, the structure and format of
these values, and how the function returns a value to the caller. In order to
interface with C programs, the FFI layers in other programs have to utilize this
ABI to pass information to and from C functions.

Other languages often have their own ABIs. C, being a different programming
language from $X, naturally has different semantics. The particular semantics of
C don’t necessarily line up to the semantics the language designers want $X to
have, so the typical solution is to define functions with C “linkage”, which
means they’re called with the C ABI. It’s from this that we get keywords like
 `extern "C"`  (C++, Rust), Go’s Cgo tooling,  `[DllImport]`  in C#, and so on.
Naturally, these keywords come with a lot of constraints on how the function
works, limiting the user to the mutually compatible subset of the two ABIs, or
else using some kind of translation layer.

I like to think of the place where this happens as the “abiopause”, and draw
comparisons with the solar system’s heliopause. Within the “abiosphere”, the
programming language you’re using is the dominant influence. The idioms and
features of the language are used to their fullest extent to write idiomatic
code. However, the language’s sphere of influence is but a bubble in a sea of C
code, and the interface between these two areas of influence is often quite
turbulent. Directly using functions with C linkage from the abiosphere is not
pleasant, as the design of good C APIs do not match the semantics of good
$X APIs. Often there are layers to this transition, much like our solar
system, where some attempt is made to wrap the C interface in a more idiomatic
abstraction.

I don’t really like this boundary, and I think most programmers who have worked
here would agree. If you like C, you’re stuck either writing bad C code or using
poorly-suited tools to interface badly with an otherwise good API. If you like
$X, you’re stuck writing very non-idiomatic $X code to interface with a foreign
system. I don’t know how to fix this, but it’s interesting to me that the
“abiopause” appears to be an interface full of a similar turbulence and
complexity as we find in the heliopause.

1. It took longer because Voyager 2 went on to see Uranus and Neptune. Voyager 1 just swung around Saturn and was shot directly up and out of the solar system. Three other man-made objects are currently on trajectories which will leave the solar system. ↩︎
2. Even if you don’t like C, it would be ridiculous to dismiss its influence and importance. ↩︎
