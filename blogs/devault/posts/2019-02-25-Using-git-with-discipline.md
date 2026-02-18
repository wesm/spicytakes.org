---
title: "Tips for a disciplined git workflow"
date: 2019-02-25
url: https://drewdevault.com/2019/02/25/Using-git-with-discipline.html
slug: Using-git-with-discipline
word_count: 991
---

Basic git usage involves typing a few stock commands to “ [sync everyone
up](https://xkcd.com/1597/) ”. Many people who are frustrated with git become so
because they never progress beyond this surface-level understanding of how it
works. However, mastering git is easily worth your time. How much of your day is
spent using git? I would guess that there are many tools in your belt that you
use half as often and have spent twice the time studying.

If you’d like to learn more about git, I suggest starting with  [Chapter
10](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)  of  [Pro Git](https://git-scm.com/book/en/v2)  (it’s free!), then reading chapters 2, 3,
and 7. The rest is optional. In this article, we’re going to discuss how you can
apply the tools discussed in the book to a disciplined and productive git
workflow.

### The basics: Writing good commit messages

You may have heard this speech before, but bear with me. Generally, you should
not use  `git commit -m "Your message here"` . Start by configuring git to use
your favorite editor:  `git config --global core.editor vim` , then simply run
 `git commit`  alone. Your editor will open and you can fill in the file with your
commit message. The first line should be limited to 50 characters in length, and
should complete this sentence: when applied, this commit will… “Fix text
rendering in CJK languages”. “Add support for protocol v3”. “Refactor CRTC
handling”. Then, add a single empty line, and expand on this in the  *extended
commit description* , which should be hard-wrapped at 72 columns, and include
details like rationale for the change, tradeoffs and limitations of the
approach, etc.

We use 72 characters because that’s  [the standard width of an email](https://tools.ietf.org/html/rfc2822#section-2.1.1) , and
email is an important tool for git. The 50 character limit is used because the
first line becomes the subject line of your email - and lots of text like
“ `[PATCH linux-usb v2 0/13]` ” can get added to beginning. You might find
wrapping your lines like this annoying and burdensome - but consider that when
working with others, they may not be reading the commit log in the same context
as you. I have a vertical monitor that I often read commit logs on, which is not
going to cram as much text into one line as your 4K 16:9 display could.

### Each commit should be a self-contained change

Every commit should only contain one change - avoid sneaking in little unrelated
changes into the same commit 1 . Additionally, avoid breaking one change into
several commits, unless you can refactor the idea into discrete steps - each of
which represents a complete change in its own right. If you have several changes
in your working tree and only need to commit some of them, try  `git add -i`  or
 `git add -p` . Additionally, every commit should compile and run all tests
successfully, and should avoid having any known bugs which will be fixed up in a
future commit.

If this is true of your repository, then you can check out any commit and expect
the code to work correctly. This also becomes useful later, for example when
cherry-picking commits into a release branch. Using this approach also allows
 [git-bisect](https://git-scm.com/docs/git-bisect)  to become more useful 2 ,
because if you can expect the code to compile and complete tests successfully
for every commit, you can pass  `git-bisect`  a script which programmatically
tests a tree for the presence of a bug and avoid false positives. These
self-contained commits with good commit messages can also make it really easy to
prepare release notes with  [git-shortlog](https://git-scm.com/docs/git-shortlog) ,
 [like Linus does with Linux releases](https://lkml.org/lkml/2019/1/6/178) .

### Get it right on the first try

We now come to one of the most important features of git which distinguishes it
from its predecessors: history editing. All version control systems come with a
time machine of some sort, but before git they were mostly read-only. However,
git’s time machine is different: you can change the past. In fact, you’re
encouraged to! But a word of warning: only change a future which has yet to be
merged into a stable public branch.

The advice in this article - bug-free, self-contained commits with a good commit
message - is hard to get right on the first try. Editing your history, however,
is easy and part of an effective git workflow. Familiarize yourself with
 [git-rebase](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)  and use
it liberally. You can use rebase to reorder, combine, delete, edit, and split
commits. One workflow I find myself commonly using is to make some changes to a
file, commit a “fixup” commit ( `git commit -m fixup` ), then use  `git rebase -i` 
to squash it into an earlier commit.

### Other miscellaneous tips

* Read the man pages! Pick a random git man page and read it now. Also, if you
haven’t read the top-level git man page (simply  `man git` ), do so.
* At the bottom of each man page for a high-level git command is usually a list
of low-level git commands that the high-level command relies on. If you want
to learn more about how a high-level git command works, try reading these man
pages, too.
* Learn how to specify the commit you want with  [rev selection](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection)
* Branches are useful, but you should learn how to work without them as well to
have a nice set of tools in your belt. Use tools like  `git pull --rebase` ,
 `git send-email -1 HEAD~2` , and  `git push origin HEAD~2:master` .

1. I could stand to take my own advice more often in this respect. ↩︎
2. In a nutshell, git bisect is a tool which does a binary search between two commits in your history, checking out the commits in between one at a time to allow you to test for the presence of a bug. In this manner you can narrow down the commit which introduced a problem. ↩︎
