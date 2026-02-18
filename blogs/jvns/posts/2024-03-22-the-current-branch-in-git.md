---
title: "The 'current branch' in git"
date: 2024-03-22
url: https://jvns.ca/blog/2024/03/22/the-current-branch-in-git/
slug: the-current-branch-in-git
word_count: 1705
---


Hello! I know I just wrote [a blog post about HEAD in git](https://jvns.ca/blog/2024/03/08/how-head-works-in-git/), but I’ve been
thinking more about what the term “current branch” means in git and it’s a
little weirder than I thought.


### four possible definitions for “current branch”

1. It’s what’s in the file **`.git/HEAD`**. This is how the [git glossary](https://git-scm.com/docs/gitglossary#def_HEAD) defines it.
2. It’s what **`git status`** says on the first line
3. It’s what you most recently **checked out** with `git checkout` or `git switch`
4. It’s what’s in your shell’s **git prompt**. I use [fish_git_prompt](https://fishshell.com/docs/current/cmds/fish_git_prompt.html) so that’s what I’ll be talking about.


I originally thought that these 4 definitions were all more or less the
same, but after chatting with some people on Mastodon, I realized that they’re
more different from each other than I thought.


So let’s talk about a few git scenarios and how each of these definitions plays
out in each of them. I used git version `2.39.2 (Apple Git-143)` for all of these experiments.


### scenario 1: right after `git checkout main`


Here’s the most normal situation: you check out a branch.

1. `.git/HEAD` contains `ref: refs/heads/main`
2. `git status` says `On branch main`
3. The thing I most recently checked out was: `main`
4. My shell’s git prompt says: `(main)`


In this case the 4 definitions all match up: they’re all `main`. Simple enough.


### scenario 2: right after `git checkout 775b2b399`


Now let’s imagine I check out a specific commit ID (so that we’re in “detached HEAD state”).

1. `.git/HEAD` contains `775b2b399fb8b13ee3341e819f2aaa024a37fa92`
2. `git status` says `HEAD detached at 775b2b39`
3. The thing I most recently checked out was `775b2b399`
4. My shell’s git prompt says `((775b2b39))`


Again, these all basically match up – some of them have truncated the commit
ID and some haven’t, but that’s it. Let’s move on.


### scenario 3: right after `git checkout v1.0.13`


What if we’ve checked out a tag, instead of a branch or commit ID?

1. `.git/HEAD` contains `ca182053c7710a286d72102f4576cf32e0dafcfb`
2. `git status` says `HEAD detached at v1.0.13`
3. The thing I most recently checked out was `v1.0.13`
4. My shell’s git prompt says `((v1.0.13))`


Now things start to get a bit weirder! `.git/HEAD` disagrees with the other 3
indicators: `git status`, the git prompt, and what I checked out are all the
same (`v1.0.13`), but `.git/HEAD` contains a commit ID.


The reason for this is that git is trying to help us out: commit IDs are kind
of opaque, so if there’s a tag that corresponds to the current commit, `git status` will show us that instead.


Some notes about this:

- If we check out the commit by its ID (`git checkout ca182053c7710a286d72`)
instead of by its tag, what shows up in `git status` and in my shell prompt
are exactly the same – git doesn’t actually “know” that we checked out a
tag.
- it looks like you can find the tags matching `HEAD` by running `git describe HEAD --tags --exact-match` (here’s the [fish git prompt code](https://github.com/fish-shell/fish-shell/blob/a5156e9e0e89bff2bd81ac945a019bad34f14346/share/functions/fish_git_prompt.fish#L521-L527))
- You can see where `git-prompt.sh` added support for describing a commit by a
tag in this way in commit [27c578885 in 2008](https://github.com/git/git/commit/27c578885a0b8f56430c5a24f558e2b45cf04a38).
- I don’t know if it makes a difference whether the tag is annotated or not.
- If there are 2 tags with the same commit ID, it gets a little weird. For
example, if I add the tag `v1.0.12` to this commit so that it’s with both `v1.0.12` and `v1.0.13`, you can
see here that my git prompt changes, and then the prompt and `git status`
disagree about which tag to display:


```
bork@grapefruit ~/w/int-exposed ((v1.0.12))> git status
HEAD detached at v1.0.13

```


(my prompt shows `v1.0.12` and `git status` shows `v1.0.13`)


### scenario 4: in the middle of a rebase


Now: what if I check out the `main` branch, do a rebase, but then there was a
merge conflict in the middle of the rebase? Here’s the situation:

1. `.git/HEAD` contains `c694cf8aabe2148b2299a988406f3395c0461742` (the commit ID of the commit that I’m rebasing onto, `origin/main` in this case)
2. `git status` says `interactive rebase in progress; onto c694cf8`
3. The thing I most recently checked out was `main`
4. My shell’s git prompt says `(main|REBASE-i 1/1)`


Some notes about this:

- I think that in some sense the “current branch” is `main` here – it’s what I most recently checked out, it’s what we’ll go back to after the rebase is done, and it’s where we’d go back to if I run `git rebase --abort`
- in another sense, we’re in a detached HEAD state at `c694cf8aabe2`. But it doesn’t have the usual implications of being in “detached HEAD state” – if you make a commit, it won’t get orphaned! Instead, assuming you finish the rebase, it’ll get absorbed into the rebase and put somewhere in the middle of your branch.
- it looks like during the rebase, the old “current branch” (`main`) is stored in `.git/rebase-merge/head-name`. Not totally sure about this though.


### scenario 5: right after `git init`


What about when we create an empty repository with `git init`?

1. `.git/HEAD` contains `ref: refs/heads/main`
2. `git status` says `On branch main` (and “No commits yet”)
3. The thing I most recently checked out was, well, nothing
4. My shell’s git prompt says: `(main)`


So here everything mostly lines up, except that we’ve never run `git checkout` or `git switch`. Basically Git automatically switches to whatever
branch was configured in `init.defaultBranch`.


### scenario 6: a bare git repository


What if we clone a bare repository with `git clone --bare https://github.com/rbspy/rbspy`?

1. `HEAD` contains `ref: refs/heads/main`
2. `git status` says `fatal: this operation must be run in a work tree`
3. The thing I most recently checked out was, well, nothing, `git checkout` doesn’t even work in bare repositories
4. My shell’s git prompt says: `(BARE:main)`


So #1 and #4 match (they both agree that the current branch is “main”), but `git status` and `git checkout` don’t even work.


Some notes about this one:

- I think `HEAD` in a bare repository mainly only really affects 1 thing: it’s the
branch that gets checked out when you clone the repository. It’s also used when you run `git log`.
- if you really want to, you can update `HEAD` in a bare repository to a
different branch with `git symbolic-ref HEAD refs/heads/whatever`. I’ve never
needed to do that though and it seems weird because `git symbolic ref` doesn’t check if the thing you’re pointing `HEAD` at is
actually a branch that exists. Not sure if there’s a better way.


### all the results


Here’s a table with all of the results:



|  | `.git/HEAD` | git status | checked out | prompt |
| 1. `checkout main` | `ref: refs/heads/main` | `On branch main` | main | `(main)` |
| 2. `checkout 775b2b` | `775b2b399...` | `HEAD detached at 775b2b39` | 775b2b399 | `((775b2b39))` |
| 3. `checkout v1.0.13` | `ca182053c...` | `HEAD detached at v1.0.13` | v1.0.13 | `((v1.0.13))` |
| 4. inside rebase | `c694cf8aa...` | `interactive rebase in progress; onto c694cf8` | main | `(main|REBASE-i 1/1)` |
| 5. after `git init` | `ref: refs/heads/main` | `On branch main` | n/a | `(main)` |
| 6. bare repository | `ref: refs/heads/main` | `fatal: this operation must be run in a work tree` | n/a | `(BARE:main)` |



### “current branch” doesn’t seem completely well defined


My original instinct when talking about git was to agree with the git glossary
and say that `HEAD` and the “current branch” mean the exact same thing.


But this doesn’t seem as ironclad as I used to think anymore! Some thoughts:

- `.git/HEAD` is definitely the one with the most consistent format – it’s
always either a branch or a commit ID. The others are all much messier
- I have a lot more sympathy than I used to for the definition “the current
branch is whatever you last checked out”. Git does a lot of work to remember
which branch you last checked out (even if you’re currently doing a bisect or
a merge or something else that temporarily moves HEAD off of that branch) and
it feels weird to ignore that.
- `git status` gives a lot of helpful context – these 5 status messages say a
lot more than just what `HEAD` is set to currently
  1. `on branch main`
  2. `HEAD detached at 775b2b39`
  3. `HEAD detached at v1.0.13`
  4. `interactive rebase in progress; onto c694cf8`
  5. `on branch main, no commits yet`


### some more “current branch” definitions


I’m going to try to collect some other definitions of the term `current branch` that I heard from people on Mastodon here and write some notes on them.

1. “the branch that would be updated if i made a commit”

- Most of the time this is the same as `.git/HEAD`
- Arguably if you’re in the middle of a rebase, it’s different from `HEAD`,  because ultimately that new commit will end up on the branch in `.git/rebase-merge/head-name`

1. “the branch most git operations work against”

- This is sort of the same as what’s in `.git/HEAD`, except that some
operations (like `git status`) will behave differently in some situations,
like how `git status` won’t tell you the current branch if you’re in a bare
repository


### on orphaned commits


One thing I noticed that wasn’t captured in any of this is whether the
current commit is **orphaned** or not – the `git status` message (`HEAD detached from c694cf8`) is the same whether or not your current commit is
orphaned.


I imagine this is because figuring out whether or not a given commit is
orphaned might take a long time in a large repository: you can find out if
the current commit is orphaned with `git branch --contains HEAD`, and that
command takes about 500ms in a repository with 70,000 commits.


Git will warn you if the commit is orphaned (“Warning: you are leaving 1 commit
behind, not connected to any of your branches…”) when you switch to a
different branch though.


### that’s all!


I don’t have anything particularly smart to say about any of this. The more I
think about git the more I can understand why people get confused.
