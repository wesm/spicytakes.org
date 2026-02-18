---
title: "The rc shell and its excellent handling of whitespace"
date: 2023-07-31
url: https://drewdevault.com/2023/07/31/The-rc-shell-and-whitespace.html
slug: The-rc-shell-and-whitespace
word_count: 982
---

*This blog post is a response to Mark Dominus’ “[The shell and its crappy handling of whitespace](https://blog.plover.com/Unix/whitespace.html)”* .

I’ve been working on a shell for Unix-like systems called
 [rc](https://git.sr.ht/~sircmpwn/rc) , which draws heavily from the Plan 9 shell
 [of the same name](http://man.9front.org/1/rc) . When I saw Mark’s post about the
perils of whitespace in POSIX shells (or derived shells, like bash), I thought
it prudent to see if any of the problems he outlines are present in the shell
I’m working on myself. Good news: they aren’t!

Let’s go over each of his examples. First he provides the following example:

```
for i in *.jpg; do
	cp $i /tmp
done
```

This breaks if there are spaces in the filenames. Not so with rc:

```
% cat test.rc
for (i in *.jpg) {
	cp $i subdir
}
% ls
a.jpg   b.jpg  'bite me.jpg'   c.jpg   subdir   test.rc
% rc ./test.rc 
% ls subdir/
a.jpg   b.jpg  'bite me.jpg'   c.jpg
```

He gives a similar example for a script that renames jpeg to jpg:

```
for i in *.jpeg; do
  mv $i $(suf $i).jpg
done
```

This breaks for similar reasons, but works fine in rc:

```
% cat test.rc  
fn suf(fname) {
	echo $fname | sed -e 's/\..*//'
}

for (i in *.jpeg) {
	mv $i `{suf $i}.jpg
}
% ls 
a.jpeg   b.jpeg  'bite me.jpeg'   c.jpeg   test.rc
% rc ./test.rc  
% ls 
a.jpg   b.jpg  'bite me.jpg'   c.jpg   test.rc
```

There are other shells, such as fish or zsh, which also have answers to these
problems which don’t necessarily call for generous quoting like other shells
often do. rc is much simpler than these shells. At the moment it clocks in at
just over 3,000 lines of code, compared to fish at ~45,000 and zsh at ~144,000.
Admittedly, it’s not done yet, but I would be surprised to see it grow beyond
5,000 lines for version 1.0. 1

The key to rc’s design success in this area is the introduction of a second
primitive. The Bourne shell and its derivatives traditionally work with only one
primitive: strings. But command lines are made of  *lists*  of strings, and so a
language which embodies the primitives of the command line ought to also be able
to represent those as a first-class feature. In traditional shells a list of
strings is denoted inline with the use of spaces within those strings, which
raises obvious problems when the members themselves contain spaces; see Mark’s
post detailing the errors which ensue. rc adds lists of strings as a formal
primitive alongside strings.

```
% args=(ls --color /) 
% echo $args(1) 
ls
% echo $args(2) 
--color
% echo $#args 
3
% $args 
bin   dev  home  lost+found  mnt  proc  run   srv      swap  tmp  var
boot  etc  lib   media       opt  root  sbin  storage  sys   usr
% args=("foo bar" baz) 
% touch $args 
% ls 
 baz  'foo bar'
```

Much better, right? One simple change eliminates the need for quoting virtually
everywhere. Strings can contain spaces and nothing melts down.

Let me run down the remaining examples from Mark’s post and demonstrate their
non-importance in rc. First, regarding $*, it just does what you expect.

```
% cat yell.rc
#!/bin/rc
shift
echo I am about to run $* now!!!
exec $*
% ls *.jpg
'bite me.jpg'
% ./yell.rc ls *.jpg
I am about to run ls bite me.jpg now!!!
'bite me.jpg'
```

Note also that there is no need to quote the arguments to “echo” here. Also note
the use of shift; $* includes $0 in rc.

Finally, let’s rewrite Mark’s “lastdl” program in rc and show how it works fine
in rc’s interactive mode.

```
#!/bin/rc
cd $HOME/downloads
echo $HOME/downloads/`{ls -t | head -n1}
```

Its use at the command line works just fine without quotes.

```
% file `{lastdl} 
/home/sircmpwn/downloads/test image.jpg: JPEG image data, JFIF standard 1.01,
aspect ratio, density 1x1, segment length 16, baseline, precision 8,
5000x2813, components 3
```

Just for fun, here’s another version of this rc script that renames files with
spaces to without, like the last example in Mark’s post:

```
#!/bin/rc
cd $HOME/downloads
last=`{ls -t | head -n1}
if (~ $last '* *') {
	newname=`{echo $last | tr ' \t' '_'}
	mv $last $HOME/downloads/$newname
	last=$newname
}
echo $HOME/downloads/$last
```

The only quotes to be found are those which escape the wildcard match testing
for a space in the string. 2  Not bad, right? Like Plan 9’s rc, my shell
imagines a new set of primitives for shells, then starts from the ground up and
builds a shell which works better in most respects while still being very
simple. Most of the problems that have long plagued us with respect to sh, bash,
etc, are solved in a simple package with rc, alongside a nice interactive mode
reminiscent of the best features of fish.

rc is a somewhat complete shell today, but there is a bit more work to be done
before it’s ready for 1.0, most pressingly with respect to signal handling and
job control, alongside a small bit of polish and easier features to implement
(such as subshells, IFS, etc). Some features which are likely to be omitted, at
least for 1.0, include logical comparisons and arithmetic expansion (for which
/bin/test and /bin/dc are recommended respectively). Of course, rc is destined
to become the primary shell of the  [Ares operating system](https://ares-os.org) 
project that I’ve been working on, but I have designed it to work on Unix as
well.

Check it out!

1. Also worth noting that these line counts are, to some extent, comparing
apples to oranges given that fish, zsh, and rc are written respectively in
C++/Rust, C, and Hare. ↩︎
2. This is a bit of a fib. In fact, globbing is disabled when processing the
args of the ~ built-in. However, the quotes are, ironically, required to
escape the space between the * characters, so it’s one argument rather than
two. ↩︎
