---
title: "Using strace to avoid reading Ruby code"
date: 2014-02-26
url: https://jvns.ca/blog/2014/02/26/using-strace-to-avoid-reading-ruby-code/
slug: using-strace-to-avoid-reading-ruby-code
word_count: 266
---


Yesterday I was getting set up, and we were having a problem with an
internal tool written in Ruby that was sshing somewhere. So we wanted
to know exactly what ssh command it was running. The normal way I’d
think about doing this is by, well, reading the code. But that takes
time!


So! My new favorite thing in life is strace (as evidenced by these
[two](http://jvns.ca/blog/2013/12/22/fun-with-strace/)
[posts](http://jvns.ca/blog/2014/02/17/spying-on-ssh-with-strace/))
(when all you have is a hammer…). But I wasn’t sure that we could
use strace to figure out the ssh command.


But then [Evan](https://twitter.com/ebroder) did this (or something equivalent):


`strace -f -e trace=execve [the ruby command]`


This looks at all the system calls that the command runs, filters out
everything that isn’t executing a command, and also looks in all the
child processes. Grepping for ssh spat out the exact ssh command that
it was running!


The looking-in-all-child-processes part (`-f`) is important because it
started some subprocesses.


This is super fun because what I’d usually do is go read the code to
try and figure out what it’s doing, and reading code is hard! strace
is easy!


Also it’s a great example of incidental/accidental learning. I like
working with people who know more (and different!) things than I do :)


I’m trying to put together more examples of when understanding how
system calls work is useful in everyday non-kernel-hacking
programming. If you have suggestions, tell me on Twitter! I’m
[@b0rk](http://twitter.com/b0rk). (or by email!)


(**edit**: [Greg Price](http://web.mit.edu/price/) suggested using
`strace -e process` instead of `strace -e trace=execve`. It’s shorter,
and it also shows you other process-related system calls.)
