---
title: "How HEAD works in git"
date: 2024-03-08
url: https://jvns.ca/blog/2024/03/08/how-head-works-in-git/
slug: how-head-works-in-git
word_count: 1338
---


Hello! The other day I ran a Mastodon poll asking people how confident they
were that they understood how HEAD works in Git. The results (out of 1700
votes) were a little surprising to me:

- 10% “100%”
- 36% “pretty confident”
- 39% “somewhat confident?”
- 15% “literally no idea”


I was surprised that people were so unconfident about their understanding –
I’d been thinking of `HEAD` as a pretty straightforward topic.


Usually when people say that a topic is confusing when I think it’s not, the
reason is that there’s actually some hidden complexity that I wasn’t
considering. And after some follow up conversations, it turned out that `HEAD`
actually *was* a bit more complicated than I’d appreciated!


Here’s a quick table of contents:

- HEAD is actually a few different things
- the file .git/HEAD
- HEAD as in git show HEAD
- next: all the output formats
  - git status: “on branch main” or “HEAD detached”
  - detached HEAD state
  - git log: (HEAD -> main)
  - merge conflicts: <<<<<<< HEAD is just confusing


### HEAD is actually a few different things


After talking to a bunch of different people about `HEAD`, I realized that
`HEAD` actually has a few different closely related meanings:

1. The file `.git/HEAD`
2. `HEAD` as in `git show HEAD` (git calls this a “revision parameter”)
3. All of the ways git uses `HEAD` in the output of various commands (`<<<<<<<<<<HEAD`, `(HEAD -> main)`, `detached HEAD state`, `On branch main`, etc)


These are extremely closely related to each other, but I don’t think the
relationship is totally obvious to folks who are starting out with git.


### the file `.git/HEAD`


Git has a very important file called `.git/HEAD`. The way this file works is that it contains either:

1. The name of a **branch** (like `ref: refs/heads/main`)
2. A **commit ID** (like `96fa6899ea34697257e84865fefc56beb42d6390`)


This file is what determines what your “current branch” is in Git. For example, when you run `git status` and see this:


```
$ git status
On branch main

```


it means that the file `.git/HEAD` contains `ref: refs/heads/main`.


If `.git/HEAD` contains a commit ID instead of a branch, git calls that
“detached HEAD state”. We’ll get to that later.


### `HEAD` as in `git show HEAD`


It’s very common to use `HEAD` in git commands to refer to a commit ID, like:

- `git diff HEAD`
- `git rebase -i HEAD^^^^`
- `git diff main..HEAD`
- `git reset --hard HEAD@{2}`


All of these things (`HEAD`, `HEAD^^^`, `HEAD@{2}`) are called “revision parameters”. They’re documented in [man
gitrevisions](https://git-scm.com/docs/gitrevisions), and Git will try to
resolve them to a commit ID.


(I’ve honestly never actually heard the term “revision parameter” before, but
that’s the term that’ll get you to the documentation for this concept)


HEAD in `git show HEAD` has a pretty simple meaning: it resolves to the
**current commit** you have checked out! Git resolves `HEAD` in one of two ways:

1. if `.git/HEAD` contains a branch name, it’ll be the latest commit on that branch (for example by reading it from `.git/refs/heads/main`)
2. if `.git/HEAD` contains a commit ID, it’ll be that commit ID


### next: all the output formats


Now we’ve talked about the file `.git/HEAD`, and the “revision parameter”
`HEAD`, like in `git show HEAD`. We’re left with all of the various ways git
uses `HEAD` in its output.


### `git status`: “on branch main” or “HEAD detached”


When you run `git status`, the first line will always look like one of these two:

1. `on branch main`. This means that `.git/HEAD` contains a branch.
2. `HEAD detached at 90c81c72`. This means that `.git/HEAD` contains a commit ID.


I promised earlier I’d explain what “HEAD detached” means, so let’s do that now.


### detached HEAD state


“HEAD is detached” or “detached HEAD state” mean that you have no current branch.


Having no current branch is a little dangerous because if you make new commits,
those commits won’t be attached to any branch – they’ll be orphaned! Orphaned
commits are a problem for 2 reasons:

1. the commits are more difficult to find (you can’t run `git log somebranch` to find them)
2. orphaned commits will eventually be deleted by git’s garbage collection


Personally I’m very careful about avoiding creating commits in detached HEAD state, though some people [prefer to work that way](https://github.com/arxanas/git-branchless).
Getting out of detached HEAD state is pretty easy though, you can either:

1. Go back to a branch (`git checkout main`)
2. Create a new branch at that commit (`git checkout -b newbranch`)
3. If you’re in detached HEAD state because you’re in the middle of a rebase, finish or abort the rebase (`git rebase --abort`)


Okay, back to other git commands which have `HEAD` in their output!


### `git log`: `(HEAD -> main)`


When you run `git log` and look at the first line, you might see one of the following 3 things:

1. `commit 96fa6899ea (HEAD -> main)`
2. `commit 96fa6899ea (HEAD, main)`
3. `commit 96fa6899ea (HEAD)`


It’s not totally obvious how to interpret these, so here’s the deal:

- inside the `(...)`, git lists every reference that points at that commit, for example `(HEAD -> main, origin/main, origin/HEAD)` means `HEAD`, `main`, `origin/main`, and `origin/HEAD` all point at that commit (either directly or indirectly)
- `HEAD -> main` means that your current branch is `main`
- If that line says `HEAD,` instead of `HEAD ->`, it means you’re in detached HEAD state (you have no current branch)


if we use these rules to explain the 3 examples above: the result is:

1. `commit 96fa6899ea (HEAD -> main)` means:
  - `.git/HEAD` contains `ref: refs/heads/main`
  - `.git/refs/heads/main` contains `96fa6899ea `
2. `commit 96fa6899ea (HEAD, main)` means:
  - `.git/HEAD` contains `96fa6899ea` (HEAD is “detached”)
  - `.git/refs/heads/main` also contains `96fa6899ea `
3. `commit 96fa6899ea (HEAD)` means:
  - `.git/HEAD` contains `96fa6899ea` (HEAD is “detached”)
  - `.git/refs/heads/main` either contains a different commit ID or doesn’t exist


### merge conflicts: `<<<<<<< HEAD` is just confusing


When you’re resolving a merge conflict, you might see something like this:


```
<<<<<<< HEAD
def parse(input):
    return input.split("\n")
=======
def parse(text):
    return text.split("\n\n")
>>>>>>> somebranch

```


I find `HEAD` in this context extremely confusing and I basically just ignore it. Here’s why.

- When you do a **merge**, `HEAD` in the merge conflict is the same as what `HEAD` was when you ran `git merge`. Simple.
- When you do a **rebase**, `HEAD` in the merge conflict is something totally
different: it’s the **other commit** that you’re rebasing on top of. So it’s
totally different from what `HEAD` was when you ran `git rebase`. It’s like
this because rebase works by first checking out the other commit and then
repeatedly cherry-picking commits on top of it.


Similarly, the meaning of “ours” and “theirs” are flipped in a merge and rebase.


The fact that the meaning of `HEAD` changes depending on whether I’m doing a
rebase or merge is really just too confusing for me and I find it much simpler
to just ignore `HEAD` entirely and use another method to figure out which part
of the code is which.


### some thoughts on consistent terminology


I think HEAD would be more intuitive if git’s terminology around HEAD were a
little more internally consistent.


For example, git talks about “detached HEAD state”, but never about “attached
HEAD state” – git’s documentation never uses the term “attached” at all to
refer to `HEAD`. And git talks about being “on” a branch, but never “not on” a
branch.


So it’s very hard to guess that `on branch main` is actually the opposite of
`HEAD detached`. How is the user supposed to guess that `HEAD detached` has
anything to do with branches at all, or that “on branch main” has anything to
do with `HEAD`?


### that’s all!


If I think of other ways `HEAD` is used in Git (especially ways HEAD appears in
Git’s output), I might add them to this post later.


If you find HEAD confusing, I hope this helps a bit!
