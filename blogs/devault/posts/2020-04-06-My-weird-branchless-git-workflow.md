---
title: "My unorthodox, branchless git workflow"
date: 2020-04-06
url: https://drewdevault.com/2020/04/06/My-weird-branchless-git-workflow.html
slug: My-weird-branchless-git-workflow
word_count: 926
---

I have been using git for a while, and I took the time to learn about it in
great detail. Equipped with an understanding of its internals and a comfortable
familiarity with tools like  [git rebase](https://git-rebase.io)  — and a
personal, intrinsic desire to strive for minimal and lightweight solutions
— I have organically developed a workflow which is, admittedly, somewhat
unorthodox.

In short, I use git branches very rarely, preferring to work on my local master
branch almost every time. When I want to work on multiple tasks in the same
repository (i.e. often), I just… work on all of them on master. I waste no
time creating a new branch, or switching to another branch to change contexts; I
just start writing code and committing changes, all directly on master,
intermixing different workstreams freely. 1  This reduces my startup time to
zero, both for starting new tasks and revisiting old work.

When I’m ready to present some or all of my changes to upstream, I grab git
rebase and reorganize all of these into their respective features, bugfixes, and
so on, forming a series of carefully organized, self-contained patchsets. When I
receive feedback, I just start correcting the code right away, then fixup the
old commits during the rebase. Often, I’ll bring the particular patchset I’m
ready to present upstream to the front of my master branch at the same time, for
convenient access with  [git send-email](https://git-send-email.io) .

I generally set my local master branch to track the remote master branch, 2  so
I can update my branch with  `git pull --rebase` . 3  Because all of my
work-in-progress features are on the master branch, this allows me to quickly
address any merge conflicts with upstream for  *all*  of my ongoing work at once.
Additionally, by keeping them all on the same branch, I can be assured that my
patches are mutually applicable and that there won’t be any surprise conflicts
in feature B after feature A is merged upstream.

If I’m working on my own projects (where I can push to upstream master), I’ll
still be working on master. If I end up with a few commits queued up and I need
to review some incoming patches, I’ll just apply them to master, rebase them
behind my WIP work, and then use  `git push origin HEAD~5:refs/heads/master`  to
send them upstream, or something to that effect. 4  Bonus: this instantly
rebases my WIP work on top of the new master branch.

This workflow saves me time in several ways:

* No time spent creating new branches for new features.
* No time spent switching between branches to address feedback.
* All of my features are guaranteed to be mutually applicable to master, saving
me time addressing conflicts.
* Any conflicts with upstream are addressed in all of my workstreams at once,
without switching between branches or allowing any branch to get stale.

I know that lightweight branches are one of git’s flagship features, but I don’t
really use them. I know it’s weird, sue me.

Sometimes I do use branches, though, when I know that a workstream is going to
be a lot of work — it involves lots of large-scale refactoring, or will
take several weeks to complete. This isolates it from my normal workflow on
small-to-medium patches, acknowledging that the large workstream is going to be
more prone to conflicts. By addressing these separately, I don’t waste my time
fixing up the error-prone branch all the time while I’m working on my smaller
workstreams.

1. I will occasionally use `git add -p` or even just `git commit -p` to quickly separate any changes in my working directory into separate commits for their respective workstreams, to make my life easier later on. This is usually the case when, for example, I have to fix problem A before I can address problem B, and additional issues with problem A are revealed by my work on problem B. I just fix them right away, `git commit -p` the changes separately, then file each commit into their respective patchsets later. ↩︎
2. “What?” Okay, so in git, you have *local* branches and *remote* branches.  The default behavior is reasonably sane, so I would forgive you for not noticing. Your local branches can *track* remote branches, so that when you `git pull` it automatically updates any local *tracking branches*. `git pull` is actually equivalent to doing `git fetch` and then `git merge origin/master` assuming that the current branch (your *local* master) is *tracking* `origin/master`. `git pull --rebase` is the same thing, except it uses `git rebase` instead of `git merge` to update your local branch. ↩︎
3. In fact, I have `pull.rebase = true` in my git config, which makes `--rebase` the default behavior. ↩︎
4. “What?” Okay, so `git push` is shorthand for `git push origin master`, if you have a tracking branch set up for your local master branch to `origin/master`. But this itself is also shorthand, for `git push <remote> <local>:<remote>`, where `<local>` is the local branch you want to push, and `<remote>` is the remote branch you want to update. But, remember that branches are just references to commits. In git, there are other ways to reference commits. `HEAD~5`, for example, gets the commit which is 5 commits earlier than `HEAD`, which is the commit you have checked out right now. So `git push origin HEAD~5:refs/for/master` updates the `origin`’s `refs/for/master` reference (i.e. the master branch) to the local commit at `HEAD~5`, pushing any commits that upstream master doesn’t also have in the process. ↩︎
