---
title: "Introduction to POSIX shell"
date: 2018-02-05
url: https://drewdevault.com/2018/02/05/Introduction-to-POSIX-shell.html
slug: Introduction-to-POSIX-shell
word_count: 920
---

What the heck is the POSIX shell anyway? Well, the POSIX (the Portable Operating
System Interface) shell is the standard Unix shell - standard meaning it was
formally defined and shipped in a published standard. This makes shell scripts
written for it portable, something no other shell can lay claim to. The POSIX
shell is basically a formalized version of the venerable Bourne shell, and on
your system it lives at  `/bin/sh` , unless you’re one of the unlucky masses for
whom this is a symlink to bash.

## Why use POSIX shell?

The “Bourne Again shell”, aka bash, is not standardized. Its grammar,
features, and behavior aren’t formally written up anywhere, and only one
implementation of bash exists. Without a standard, bash is defined  *by*  its
implementation. POSIX shell, on the other hand, has many competing
implementations on many different operating systems - all of which are
compatible with each other because they conform to the standard.

Any shell that utilizes features specific to Bash are not portable, which means
you cannot take them with you to any other system. Many Linux-based systems do
not use Bash or GNU coreutils. Outside of Linux, pretty much everyone but Hurd
does  *not*  ship GNU tools, including bash 1 . On any of these systems, scripts
using “bashisms” will not work.

This is bad if your users wish to utilize your software anywhere other than
GNU/Linux. If your build tooling utilizes bashisms, your software will not build
on anything but GNU/Linux. If you ship runtime scripts that use bashisms, your
software will not  *run*  on anything but GNU/Linux. The case for sticking to
POSIX shell in shipping software is compelling, but I argue that you should
stick to POSIX shell for your personal scripts, too. You might not care now, but
when you feel like flirting with other Unicies you’ll thank me when all of your
scripts work.

One place where POSIX shell does  *not*  shine is for interactive use - a place
where I think bash sucks, too. Any shell you want to use for your day-to-day
command line work is okay in my book. I use fish. Use whatever you like
interactively, but stick to POSIX sh for your scripts.

## How do I use POSIX shell?

At the top of your scripts, put  `#!/bin/sh` . You don’t have to worry about using
 `env`  here like you might have been trained to do with bash:  `/bin/sh`  is the
standardized location for the POSIX shell, and any standards-conforming system
will either put it there or make your script work anyway. 2

The next step is to avoid bashisms. There are many, but here are a few that
might trip you up:

* `[[ condition ]]`  does not work; use  `[ condition ]`
* Arrays do not work;  [use IFS](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_05)
* Local variables do not work; use a subshell

The easiest way to learn about POSIX shell is to  [read the
standard](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html)  -
it’s not too dry and shorter than you think.

## Using standard coreutils

The last step to writing portable scripts is to use portable tools. Your system
may have GNU coreutils installed, which provides tools like  `grep`  and  `cut` .
Unfortunately, GNU has extended these tools with its own non-portable flags and
tools. It’s important that you avoid these.

One dead giveaway of a non-portable flag is long flags, e.g.  `grep --file=FILE` 
as opposed to  `grep -f` . The POSIX standard only defines the  `getopt`  function -
not the proprietary GNU  `getopt_long`  function that’s used to interpret long
options. As a result, no long flags are standardized. You might worry that this
will make your scripts difficult to understand, but I think that on the whole it
will not. Shell scripts are already pretty alien and require some knowledge to
understand. Is knowledge of what the magic word  `grep`  means much different
from knowledge of what  `grep -E`  means?

I also like that short flags allow you to make more concise command lines. Which
is better:  `ps --all --format=user --without-tty` , or  `ps -aux` ? If you are
inclined to think the former, do you also prefer  `function(a, b, c) { return a + b + c; }`  over  `(a, b, c) => a + b + c` ?  Conciseness matters, and POSIX shell
supports comments if necessary!

Some tips for using short flags:

* They can be collapsed:  `cmd -a -b -c`  is equivalent to  `cmd -abc`
* If they take additional arguments, either a space or no separation is
acceptable:  `cmd -f"hello world"`  or  `cmd -f "hello world"`

A good reference for learning about standardized commands is, once again,  [the
standard](http://pubs.opengroup.org/onlinepubs/9699919799/) . From this page,
search for the command you want, or navigate through “Shell & Utilities” ->
“Utilities” for a list. If you have  `man-pages`  installed, you will also find
POSIX man pages installed on your system with the  `p`  postfix, such as  `man 1p grep` . Note: at the time of writing, the POSIX man pages do not use dashes if
your locale is UTF-8, which makes searching for flags with  `/`  difficult. Use
 `env LC_ALL=POSIX man 1p grep`  if you need to search for flags, and I’ll speak
to the maintainer of man-pages about this.

1. A reader points out that macOS ships an ancient version of bash. ↩︎
2. *2018-05-15 correction*: `#!/bin/sh` is unfortunately not standardized by POSIX. However, I still recommend its use, as most operating systems will place it there. The portable way to invoke shell scripts is `sh path/to/script`. ↩︎
