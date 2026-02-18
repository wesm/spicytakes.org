---
title: "Dealing with diverged git branches"
date: 2024-02-01
url: https://jvns.ca/blog/2024/02/01/dealing-with-diverged-git-branches/
slug: dealing-with-diverged-git-branches
word_count: 1800
---


Hello! One of the most common problems I see folks struggling with in Git is
when a local branch (like `main`) and a remote branch (maybe also called
`main`) have diverged.


There are two things that make this situation hard:

- If you’re not used to interpreting git’s error messages, it’s nontrivial to
even **realize** that your `main` has diverged from the remote `main` (git
will often just give you an intimidating but generic error message like
`! [rejected] main -> main (non-fast-forward) error: failed to push some refs to 'github.com:jvns/int-exposed'`)
- Once you realize that your branch has diverged from the remote `main`, there
no single clear way to handle it (what you need to do depends on the
situation and your git workflow)


So let’s talk about a) how to recognize when you’re in a situation where a local
branch and remote branch have diverged and b) what you can do about it! Here’s a
quick table of contents:

- what does “diverged” mean?
- recognizing when branches are diverged
  - way 1: git status
  - way 2: git push
  - way 3: git pull
- there’s no one solution
  - solution 1.1: git pull –rebase
  - solution 1.2: git pull –no-rebase
  - solution 2.1: git push –force
  - solution 2.2: git push –force-with-lease
  - solution 3: git reset –hard origin/main


Let’s start with what it means for 2 branches to have “diverged”.


### what does “diverged” mean?


If you have a local `main` and a remote `main`, there are 4 basic configurations:


**1: up to date**. The local and remote `main` branches are in the exact same place. Something like this:


```
a - b - c - d
            ^ LOCAL
            ^ REMOTE

```


**2: local is behind**


Here you might want to `git pull`. Something like this:


```
a - b - c - d - e
    ^ LOCAL     ^ REMOTE

```


**3: remote is behind**


Here you might want to `git push`. Something like this:


```
a - b - c - d - e
    ^ REMOTE    ^ LOCAL

```


**4: they’ve diverged :(**


This is the situation we’re talking about in this blog post. It looks something like this:


```
a - b - c - d - e
        \       ^ LOCAL
         -- f 
            ^ REMOTE

```


There’s no one recipe for resolving this (how you want to handle it depends on
the situation and your git workflow!) but let’s talk about how to recognize
that you’re in that situation and some options for how to resolve it.


### recognizing when branches are diverged


There are 3 main ways to tell that your branch has diverged.


### way 1: `git status`


The easiest way to is to run `git fetch` and then `git status`. You’ll get a message something like this:


```
$ git fetch
$ git status
On branch main
Your branch and 'origin/main' have diverged, <-- here's the relevant line!
and have 1 and 2 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

```


### way 2: `git push`


When I run `git push`, sometimes I get an error like this:


```
$ git push
To github.com:jvns/int-exposed
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'github.com:jvns/int-exposed'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

```


This doesn’t **always** mean that my local `main` and the remote `main` have
diverged (it could just mean that my `main` is behind), but for me it **often**
means that. So if that happens I might run `git fetch` and `git status` to
check.


### way 3: `git pull`


If I `git pull` when my branches have diverged, I get this error message:


```
$ git pull
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.

```


This is pretty clear about the issue (“you have divergent branches”).


`git pull` doesn’t always spit out this error message though when your branches have diverged: it depends on how
you configure git. The three other options I’m aware of are:

1. if you set `git config pull.rebase false`, it’ll automatically start merging the remote `main`
2. if you set `git config pull.rebase true`, it’ll automatically start rebasing onto the remote `main`
3. if you set `git config pull.ff only`, it’ll exit with the error `fatal: Not possible to fast-forward, aborting.`


Now that we’ve talked about some ways to recognize that you’re in a situation
where your local branch has diverged from the remote one, let’s talk about what
you can do about it.


### there’s no one solution


There’s no “best” way to resolve branches that have diverged – it really
depends on your workflow for git and why the situation is happening.


I use 3 main solutions, depending on the situation:

1. I want to **keep both sets of changes** on `main`. To do this, I’ll run `git pull --rebase`.
2. The **remote changes are useless** and I want to overwrite them. To do this,
I’ll run `git push --force`
3. The **local changes are useless** and I want to overwrite them. To do this, I’ll
run `git reset --hard origin/main`


Here are some more details about all 3 of these solutions.


### solution 1.1: `git pull --rebase`


This is what I do when I want to keep both sets of changes. It rebases `main`
onto the remote `main` branch. I mostly use this in repositories where I’m
doing all of my work on the `main` branch.


You can configure `git config pull.rebase true`, to do this automatically every
time, but I don’t because sometimes I actually want to use solutions 2 or 3
(overwrite my local changes with the remote, or the reverse). I’d rather be
warned “hey, these branches have diverged, how do you want to handle it?” and
decide for myself if I want to rebase or not.


### solution 1.2: `git pull --no-rebase`


This starts a merge between the `local` and remote `main`. Here you’ll need to:

1. Run `git pull --no-rebase`. This starts a merge and (if it succeeds) opens a text editor so that you can confirm that you want to commit the merge
2. Save the file in your text editor.


I don’t have too much to say about this because I’ve never done it. I always
use rebase instead. That’s a personal workflow choice though, lots of people have very
legitimate reasons to [avoid rebase](https://jvns.ca/blog/2023/11/06/rebasing-what-can-go-wrong-/).


### solution 2.1: `git push --force`


Sometimes I know that the work on the remote `main` is actually useless and I
just want to overwrite it with whatever is on my local `main`.


I do this pretty often on private repositories where I’m the only committer,
for example I might:

- `git push` some commits
- belatedly decide I want to change the most recent commit
- make the changes and run `git commit --amend`
- run `git push --force`


Of course, if the repository has many different committers, force-pushing in
this way can cause a lot of problems. On shared repositories I’ll usually
enable [github branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
so that it’s impossible to force push.


### solution 2.2: `git push --force-with-lease`


I’ve still never actually used `git push --force-with-lease`, but I’ve seen a
lot of people recommend it as an alternative to `git push --force` that makes
sure that nobody else has changed the branch since the last time you pushed or
fetched, so that you don’t accidentally blow their changes away.


Seems like a good option. I did notice that `--force-with-lease` isn’t
foolproof though – for example [this git commit](https://github.com/git/git/commit/f17d642d3b0fa64879d59b311e596949f2a1f6d2)
talks about how if you use VSCode’s autofetching feature to continuously `git fetch`,
then `--force-with-lease` won’t help you.


Apparently now Git also has `--force-with-lease --force-if-includes`
([documented here](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-force-if-includes)),
which I think checks the reflog to make sure that you’ve already integrated the
remote branch into your branch somehow. I still don’t totally understand this
but I found this [stack overflow conversation](https://stackoverflow.com/questions/65837109/when-should-i-use-git-push-force-if-includes)
helpful.


### solution 3.1: `git reset --hard origin/main`


You can use this as the reverse of `git push --force` (since there’s no `git pull --force`). I do this when I know that
my **local** work shouldn’t be there and I want to throw it away and replace it
with whatever’s on the remote branch.


For example, I might do this if I accidentally made a commit to `main` that
actually should have been on new branch. In that case I’ll also create a new
branch (`new-branch` in this example) to store my local work on the `main`
branch, so it’s not really being thrown away.


Fixing that problem looks like this:


```
git checkout main

# 1. create `new-branch` to store my work
git checkout -b new-branch   

# 2. go back to the `main` branch I messed up
git checkout main            

# 3. make sure that my `origin/main` is up to date
git fetch                    

# 4. double check to make sure I don't have any uncomitted 
# work because `git reset --hard` will blow it away                                       
git status                   

# 5. force my local branch to match the remote `main`                               
#    NOTE: replace `origin/main` with the actual name of the
#    remote/branch, you can get this from `git status`.
git reset --hard origin/main  

```


This “store your work on `main` on a new branch and then `git reset --hard`” pattern can
also be useful if you’re not sure yet how to solve the conflict, since most
people are more used to merging 2 local branches than dealing with merging a
remote branch.


As always `git reset --hard` is a dangerous action and you can permanently lose
your uncommitted work. I always run `git status` first to make sure I don’t
have any uncommitted changes.


Some alternatives to using `git reset --hard` for this:

- check out some other branch and run `git branch -f main origin/main`.
- check out some other branch and run `git fetch origin main:main --force`


### that’s all!


I’d never really thought about how confusing the `git push` and `git pull`
error messages can be if you’re not used to reading them.
