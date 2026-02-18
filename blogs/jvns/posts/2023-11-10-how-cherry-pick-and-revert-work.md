---
title: "How git cherry-pick and revert use 3-way merge"
date: 2023-11-10
url: https://jvns.ca/blog/2023/11/10/how-cherry-pick-and-revert-work/
slug: how-cherry-pick-and-revert-work
word_count: 1965
---


Hello! I was trying to explain to someone how `git cherry-pick` works the other
day, and I found myself getting confused.


What went wrong was: I thought that `git cherry-pick` was basically applying a
patch, but when I tried to actually do it that way, it didn’t work!


Let’s talk about what I thought `cherry-pick` did (applying a patch), why
that’s not quite true, and what it actually does instead (a “3-way merge”).


This post is extremely in the weeds and you definitely don’t need to understand
this stuff to use git effectively. But if you (like me) are curious about git’s
internals, let’s talk about it!


### cherry-pick isn’t applying a patch


The way I previously understood `git cherry-pick COMMIT_ID` is:

- calculate the diff for `COMMIT_ID`, like `git show COMMIT_ID --patch > out.patch`
- Apply the patch to the current branch, like `git apply out.patch`


Before we get into this – I want to be clear that this model is mostly
right, and if that’s your mental model that’s fine. But it’s wrong in some
subtle ways and I think that’s kind of interesting, so let’s see how it works.


If I try to do the “calculate the diff and apply the patch” thing in a case
where there’s a merge conflict, here’s what happens:


```
$ git show 10e96e46 --patch > out.patch
$ git apply out.patch
error: patch failed: content/post/2023-07-28-why-is-dns-still-hard-to-learn-.markdown:17
error: content/post/2023-07-28-why-is-dns-still-hard-to-learn-.markdown: patch does not apply

```


This just fails – it doesn’t give me any way to resolve the conflict or figure
out how to solve the problem.


This is quite different from what actually happens when run `git cherry-pick`,
which is that I get a merge conflict:


```
$ git cherry-pick 10e96e46
error: could not apply 10e96e46... wip
hint: After resolving the conflicts, mark them with
hint: "git add/rm <pathspec>", then run
hint: "git cherry-pick --continue".

```


So it seems like the “git is applying a patch” model isn’t quite right. But the
error message literally does say “could not **apply** 10e96e46”, so it’s not quite
*wrong* either. What’s going on?


### so what is cherry-pick doing?


I went digging through git’s source code to see how `cherry-pick` works, and
ended up at [this line of code](https://github.com/git/git/blob/dadef801b365989099a9929e995589e455c51fed/sequencer.c#L2353-L2358):


```
res = do_recursive_merge(r, base, next, base_label, next_label, &head, &msgbuf, opts);

```


So a cherry-pick is a… merge? What? How? What is it even merging? And how does merging even work in the first place?


I realized that I didn’t really know how git’s merge worked, so I googled it
and found out that git does a thing called “3-way merge”. What’s that?


### how git merges files: the 3-way merge


Let’s say I want to merge these 2 files. We’ll call them `v1.py` and `v2.py`.


```
def greet():
    greeting = "hello"
    name = "julia"
    return greeting + " " + name

```


```
def say_hello():
    greeting = "hello"
    name = "aanya"
    return greeting + " " + name

```


There are two lines that differ: we have

- `def greet()` and `def say_hello`
- `name = "aanya"` and `name = "julia"`


How do we know what to pick? It seems impossible!


But what if I told you that the original function was this (`base.py`)?


```
def say_hello():
    greeting = "hello"
    name = "julia"
    return greeting + " " + name

```


Suddenly it seems a lot clearer! `v1` changed the function’s name to `greet`
and `v2` set `name = "aanya"`. So to merge, we should make both those changes:


```
def greet():
    greeting = "hello"
    name = "aanya"
    return greeting + " " + name

```


We can ask git to do this merge with `git merge-file`, and it gives us exactly
the result we expected: it picks `def greet()` and `name = "aanya"`.


```
$ git merge-file v1.py base.py v2.py -p
def greet():
    greeting = "hello"
    name = "aanya"
    return greeting + " " + name⏎

```


This way of merging where you merge 2 files + their original version is called
a **3-way merge**.


If you want to try it out yourself in a browser, I made a little playground at
[jvns.ca/3-way-merge/](https://jvns.ca/3-way-merge/). I made it very quickly so it’s not mobile friendly.


### git merges changes, not files


The way I think about the 3-way merge is – git merges **changes**, not files.
We have an original file and 2 possible changes to it, and git tries to combine
both of those changes in a reasonable way. Sometimes it can’t (for example if
both changes change the same line), and then you get a merge conflict.


Git can also merge more than 2 possible changes: you can have an original file
and 8 possible changes, and it can try to reconcile all of them. That’s called
an octopus merge but I don’t know much more than that, I’ve never done one.


### how git uses 3-way merge to apply a patch


Now let’s get a little weird! When we talk about git “applying a patch” (as you
do in a `rebase` or `revert` or `cherry-pick`), it’s not actually creating a
patch file and applying it. Instead, it’s doing a 3-way merge.


Here’s how applying commit `X` as a patch to your current commit corresponds to
this `v1`, `v2`, and `base` setup from before:

1. The version of the file **in your current commit** is `v1`.
2. The version of the file **before commit X** is `base`
3. The version of the file **in commit X**. Call that `v2`
4. Run `git merge-file v1 base v2` to combine them (technically git does not
actually run `git merge-file`, it runs a C function that does it)


Together, you can think of `base` and `v2` as being the “patch”: the diff between
them is the change that you want to apply to `v1`.


### how cherry-pick works


Let’s say we have this commit graph, and we want to cherry-pick `Y` on to `main`:


```
A - B (main)
 \
  \
   X - Y - Z

```


How do we turn that into a 3-way merge? Here’s how it translates into our `v1`, `v2` and `base` from earlier:

- `B` is v1
- `X` is the base, `Y` is v2


So together `X` and `Y` are the “patch”.


And `git rebase` is just like `git cherry-pick`, but repeated a bunch of times.


### how revert works


Now let’s say we want to run `git revert Y` on this commit graph


```
X - Y - Z - A - B

```

- `B` is v1
- `Y` is the base, `X` is v2


This is exactly like a cherry-pick, but with `X` and `Y` reversed. We have to
flip them because we want to apply a “reverse patch”.


Revert and cherry-pick are so closely related in git that they’re actually
implemented in the same file:
[revert.c](https://github.com/git/git/blob/dadef801b365989099a9929e995589e455c51fed/builtin/revert.c).


### this “3-way patch” is a really cool trick


This trick of using a 3-way merge to apply a commit as a patch seems really
clever and cool and I’m surprised that I’d never heard of it before! I don’t
know of a name for it, but I kind of want to call it a “3-way patch”.


The idea is that with a 3-way patch, you specify the patch as 2 files: the file
before the patch and after (`base` and `v2` in our language in this post).


So there are 3 files involved: 1 for the original and 2 for the patch.


The point is that the 3-way patch is a much better way to patch than a normal
patch, because you have a lot more context for merging when you have
both full files.


Here’s more or less what a normal patch for our example looks like:


```
@@ -1,1 +1,1 @@:
- def greet():
+ def say_hello():
    greeting = "hello"

```


and a 3-way patch. This “3-way patch” is not a real file format, it’s just
something I made up.


```
BEFORE: (the full file)
def greet():
    greeting = "hello"
    name = "julia"
    return greeting + " " + name
AFTER: (the full file)
def say_hello():
    greeting = "hello"
    name = "julia"
    return greeting + " " + name

```


### “Building Git” talks about this


The book [Building Git](https://shop.jcoglan.com/building-git/) by James Coglan
is the only place I could find other than the git source code explaining how
`git cherry-pick` actually uses 3-way merge under the hood (I thought Pro Git might
talk about it, but it didn’t seem to as far as I could tell).


I actually went to buy it and it turned out that I’d already bought it in 2019
so it was a good reference to have here :)


### merging is actually much more complicated than this


There’s more to merging in git than the 3-way merge – there’s something
called a “recursive merge” that I don’t understand, and there are a bunch of
details about how to deal with handling file deletions and moves, and there are
also multiple merge algorithms.


My best idea for where to learn more about this stuff is Building Git, though I
haven’t read the whole thing.


### so what does `git apply` do?


I also went looking through git’s source to find out what `git apply` does, and it
seems to (unsurprisingly) be in `apply.c`. That code parses a patch file, and
then hunts through the target file to figure out where to apply it. The core logic
seems to be [around here](https://github.com/git/git/blob/dadef801b365989099a9929e995589e455c51fed/apply.c#L2684):
I think the idea is to start at the line number that the patch suggested and
then hunt forwards and backwards from there to try to find it:


```
	/*
	 * There's probably some smart way to do this, but I'll leave
	 * that to the smart and beautiful people. I'm simple and stupid.
	 */
	backwards = current;
	backwards_lno = line;
	forwards = current;
	forwards_lno = line;
	current_lno = line;
  for (i = 0; ; i++) {
     ...

```


That all seems pretty intuitive and about what I’d naively expect.


### how `git apply --3way` works


`git apply` also has a `--3way` flag that does a 3-way merge. So we actually
could have more or less implemented `git cherry-pick` with `git apply` like
this:


```
$ git show 10e96e46 --patch > out.patch
$ git apply out.patch --3way
Applied patch to 'content/post/2023-07-28-why-is-dns-still-hard-to-learn-.markdown' with conflicts.
U content/post/2023-07-28-why-is-dns-still-hard-to-learn-.markdown

```


`--3way` doesn’t just use the contents of the patch file  though! The patch file starts with:


```
index d63ade04..65778fc0 100644

```


`d63ade04` and `65778fc0` are the IDs of the old/new versions of that file in
git’s object database, so git can retrieve them to do a 3-way patch
application. This won’t work if someone emails you a patch and you don’t have
the files for the new/old versions of the file though: if you’re missing the
blobs you’ll get this error:


```
$ git apply out.patch
error: repository lacks the necessary blob to perform 3-way merge.

```


### 3-way merge is old


A couple of people pointed out that 3-way merge is much older than git, it’s
from the late 70s or something. Here’s a [paper from 2007 talking about it](https://www.cis.upenn.edu/~bcpierce/papers/diff3-short.pdf)


### that’s all!


I was pretty surprised to learn that I didn’t actually understand the core way
that git applies patches internally – it was really cool to learn about!


I have [lots of issues](https://jvns.ca/blog/2023/11/01/confusing-git-terminology/) with git’s UI but I think this particular thing is not
one of them. The 3-way merge seems like a nice unified way to solve a bunch of
different problems, it’s pretty intuitive for people (the idea of “applying a
patch” is one that a lot of programmers are used to thinking about, and the
fact that it’s implemented as a 3-way merge under the hood is an implementation
detail that nobody actually ever needs to think about).
