---
title: "Mercurial Squash Commit"
description: "I've recently had a bit of a fiddle squashing some commits with   Mercurial, so thought it was worth a post in case anyone else is   looking to do this. I don't know whether this is the best procedure"
date: 2009-07-09T00:00:00
tags: ["version control"]
url: https://martinfowler.com/bliki/MercurialSquashCommit.html
slug: MercurialSquashCommit
word_count: 742
---


I've recently had a bit of a fiddle squashing some commits with
  Mercurial, so thought it was worth a post in case anyone else is
  looking to do this. I don't know whether this is the best procedure,
  but it seemed to work pretty well for me.


```
hg clone base working
# tip of base is revision 73
cd working
# do work, committing on the way
cd ..
hg clone working squash
cd squash
hg qimport -r 74:tip
hg qgoto 74.diff
hg qfold $(hg qunapp)
hg qfinish -a
cd ../base
hg pull ../squash
```


The basic task I was doing was some fairly severe moving around
  of files and folders. I wanted to do this in several steps to
  checkpoint my work as I went, but I wanted a single commit in the
  version history. (I gather git does this more easily with rebase.)
  Making a single commit makes it easier to understand what happened -
  particularly since moving files tends to complicate looking at
  repository logs. Moving files also complicates the process - a
  couple of times I ended up with a procedure that didn't work because
  it lost the ability to track the moves - I want to be able to go
  `hg log -f` and see when and what the original commits
  were before the move.


To begin I needed to enable the mq extension (mercurial queues)
  and set my diffs to git style. Git style diffs help to track file
  moves properly.


```

# in ~/.hgrc
[extensions]
mq=

[diff]
git=true 

```


When using Mercurial in this way, it seems the general way of
  working is to have multiple repositories. Mercurial encourages
  different repositories where other systems, eg git or svn, would use
  different branches. People argue about this, but it's the Mercurial
  way of working. For this example I had 'base' as my original repos.


My first step was to clone base into a working repos.


```
hg clone base working
```


At this
  point the tip of base (and working) was revision 73. I did the file
  moves, with several checkpoint revisions as I went.


```
cd working
hg mv foo1 newdir/foo1
.. more hg mv ..
hg ci -m âmoving aroundâ
.. more hg mv ..
hg ci -m âmoving aroundâ
.. more hg mv and hg ci..
cd ..
```


By the time I was done the last revision was 80.


To squash them down into a single commit I cloned another
  repos.


```
hg clone working squash
```


It's important to clone at this point because I was about
  to edit history, so wanted to keep the original history handy until
  I knew it had worked. I now moved into there.


```
cd squash
```


Now I turned all the commits I'd done for the revisions into
  patches for the mercurial patch queue mechanism.


```
hg qimport -r 74:tip
```


I made the first change the current patch


```
hg qgoto 74.diff
```


I squashed all the patches together into a single patch


```
hg qfold $(hg qunapp)
```


The commit message for this folded patch would be all the
  individual commit messages linked together. I wanted a single
  message for my clean commit.


```
hg qrefresh -m âreorganized filesâ
```


I then turned the patch into a regular commit.


```
hg qfinish -a
```


I now had a single commit with all that work. I looked through it
  to see that everything was sane, in particular testing `hg log
  -f` on some moved files to ensure the history was still
  there. Once I was convinced all was well, I pulled the single
  changeset into the base repos.


```
 
cd ../base
hg pull ../squash
  
```


It's interesting to see how the attention on version control
  system has changed over the years. Early on the primary and only
  purpose was audit - to be able to safely go back to older revision -
  mainly to diagnose problems. Then attention switched to how they
  enabled collaboration between people. This didn't replace the need
  for audit, but built on top of it. Now there's more attention to
  using them to provide a narrative of how a code base changes -
  hence the desire for history rewriting commands like this. Again
  this need is built on top of the other two, but introduces new
  capabilities and new tensions.


My thanks to my colleague Chris Turner for his help and I also
  found [this page](http://mercurial.selenic.com/wiki/ConcatenatingChangesets) very useful.
