---
title: "Become shell literate"
date: 2020-12-12
url: https://drewdevault.com/2020/12/12/Shell-literacy.html
slug: Shell-literacy
word_count: 979
---

Shell literacy is one of the most important skills you ought to possess as a
programmer. The Unix shell is one of the most powerful ideas ever put to code,
and should be second nature to you as a programmer. No other tool is nearly as
effective at commanding your computer to perform complex tasks quickly —
or at storing them as scripts you can use later.

In my workflow, I use Vim as my editor, and Unix as my “IDE”. I don’t trick out
 [my vimrc](https://git.sr.ht/~sircmpwn/dotfiles/tree/master/.vimrc)  to add a
bunch of IDE-like features — the most substantial plugin I use on a daily
basis is  [Ctrl+P](https://github.com/ctrlpvim/ctrlp.vim) , and that just makes it
easier to open files. Being Vim literate is a valuable skill, but an important
detail is knowing when to drop it. My daily workflow involves several open
terminals, generally one with Vim, another to run builds or daemons, and a third
which just keeps a shell handy for anything I might ask of it.

The shell I keep open allows me to perform complex tasks and answer complex
questions as I work. I find interesting things with  [git grep](https://git-scm.com/docs/git-grep) ,
perform bulk find-and-replace with  [sed](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/sed.html#top) , answer questions with
 [awk](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#top) , and perform more intricate tasks on-demand with ad-hoc shell
commands and pipelines. I have the freedom to creatively solve problems without
being constrained to the rails laid by IDE designers.

Here’s an example of a problem I encountered recently: I had a bunch of changes
in a git repository. I wanted to restore deleted files without dropping the rest
of my changes, but there were hundreds of these. How can I efficiently address
this problem?

Well, I start by getting a grasp of the scale of the issue with git status,
which shows hundreds of deleted files that need to be restored. This scale is
beyond the practical limit of manual intervention, so I switch to git status
-s to get a more pipeline-friendly output.

```
$ git status -s
 D main/a52dec/APKBUILD
 D main/a52dec/a52dec-0.7.4-build.patch
 D main/a52dec/automake.patch
 D main/a52dec/fix-globals-test-x86-pie.patch
 D main/aaudit/APKBUILD
 D main/aaudit/aaudit
 D main/aaudit/aaudit-common.lua
 D main/aaudit/aaudit-repo
 D main/aaudit/aaudit-server.json
 D main/aaudit/aaudit-server.lua
 ...
```

I can work with this. I add grep '^ D' to filter out any entries which were
not deleted, and pipe it through awk '{ print $2 }' to extract just the
filenames. I’ll often run the incomplete pipeline just to check my work and
catch my bearings:

```
$ git status -s | grep '^ D' | awk '{ print $2 }'
main/a52dec/APKBUILD
main/a52dec/a52dec-0.7.4-build.patch
main/a52dec/automake.patch
main/a52dec/fix-globals-test-x86-pie.patch
main/aaudit/APKBUILD
main/aaudit/aaudit
main/aaudit/aaudit-common.lua
main/aaudit/aaudit-repo
main/aaudit/aaudit-server.json
main/aaudit/aaudit-server.lua
...
```

Very good — we have produced a list of files which we need to address.
Note that, in retrospect, I could have dropped the grep and just used awk to the
same effect:

```
$ git status -s | awk '/^ D/ { print $2 }'
main/a52dec/APKBUILD
main/a52dec/a52dec-0.7.4-build.patch
main/a52dec/automake.patch
main/a52dec/fix-globals-test-x86-pie.patch
main/aaudit/APKBUILD
main/aaudit/aaudit
main/aaudit/aaudit-common.lua
main/aaudit/aaudit-repo
main/aaudit/aaudit-server.json
main/aaudit/aaudit-server.lua
...
```

However, we’re just writing an ad-hoc command here to solve a specific,
temporary problem — finesse is not important. This command isn’t going to
be subjected to a code review. Often my thinking in these situations is to solve
one problem at a time: “filter the list” and “reword the list”.  Anyway, the
last step is to actually use this list of files to address the issue, with the
help of  [xargs](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html#top) .

```
$ git status -s | awk '/^ D/ { print $2 }' | xargs git checkout --
```

Let’s look at some more examples of interesting ad-hoc shell pipelines.
Naturally, I wrote a shell pipeline to find some:

```
$ history | cut -d' ' -f2- | awk -F'|' '{ print NF-1 " " $0 }' | sort -n | tail
```

Here’s the breakdown:

* `history`  prints a list of my historical shell commands.
* `cut -d' ' -f2-`  removes the first field from each line, using space as a
delimiter.  `history`  numbers every command, and this removes the number.
* `awk -F'|' '{ print NF-1 " " $0 }`  tells awk to use | as the field delimiter
for each line, and print each line prefixed with the number of fields. This
prints every line of my history, prefixed with the number of times the pipe
operator appears in that line.
* `sort -n`  numerically sorts this list.
* `tail`  prints the last 10 items.

This command, written in the moment, finds, characterizes, filters, and sorts my
shell history by command complexity. Here are a couple of the cool shell
commands I found:

Play the 50 newest videos in a directory with
 [mpv](https://github.com/mpv-player/mpv) :

```
ls -tc | head -n50 | tr '\n' '\0' | xargs -0 mpv
```

I use this command all the time. If I want to watch a video later, I will
 [touch](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/touch.html#top)  the file so it appears at the top of this list. Another command
transmits a tarball of a patched version of  [Celeste](http://www.celestegame.com/)  to a friend using
netcat, minus the (large) game assets, with a progress display via  [pv](http://www.ivarch.com/programs/pv.shtml) :

```
find . ! -path './Content/*' | xargs tar -cv | pv | zstd | nc 204:fbf5:... 12345
```

And on my friend’s end:

```
nc -vll :: 12345 | zstdcat | pv | tar -xv
```

tar, by the way, is an under-rated tool for moving multiple files through a
pipeline. It can read and write tarballs to stdin and stdout!

I hope that this has given you a tantalizing taste of the power of the Unix
shell. If you want to learn more about the shell, I can recommend
 [shellhaters.org](http://shellhaters.org/)  as a great jumping-off point into
various shell-related parts of the POSIX specification. Don’t be afraid of the
spec — it’s concise, comprehensive, comprehensible, and full of examples.
I would also  *definitely*  recommend taking some time to learn awk in particular:
 [here’s a brief tutorial](https://ferd.ca/awk-in-20-minutes.html) .
