---
title: "(E)Git Pain, Git Joy"
date: 2012-01-06
url: https://www.elidedbranches.com/2012/01/egit-pain-git-joy.html
word_count: 442
---

**Pain**
I've been using git in anger for about a week now, after we migrated our repos at work to github. I thought that after half a day of struggle, accidental bad merges, and confusion I finally managed to get the hang of EGit. Lots of right-clicks (hey, it's Eclipse so whatever), remember to commit, then push, great.
Today, a coworker and I do a little pairing, write the skeleton of some new features. I commit and push my changes and leave to go to a meeting that ends up going for 2 hours, only to return to a request that I add a new file that had gotten missed in the commit. Why, why, why do I need to ADD this file? I understand that commandline git (and svn) require "add" before commit, but using Subversive for the last few years I've gotten out of the habit because, seriously, if I highlight it to be checked in just add it for me.
I also seem to keep hitting problems with merging when I've made changes to files that have subsequently been changed. No matter how unrelated and auto-mergeable the changes are, EGit doesn't seem to let me pull them.
These may (probably) be user error but it is so tiresome to be yet again at a place where the tools have not caught up with the cool new thing and don't bother to streamline the common case.
**Pleasure**
On the other hand, we had a production issue tonight. Right now, the production release process for this particular code is "check out trunk, restart" (yeah, yeah, I'm working on it, it's only been a month ok?). At some point I realize that this change is bad enough that I just need to go back in time to where the code was more stable, and deploy from there. Despite a lack of tags or branches involved in the current process, this was quite easy to do.
git branch rollback_0106
git checkout rollback_0106
git reset --hard <checkin>
Then push the branch, and release from that branch. It's incredibly fast, and very easy. I also was easily able to create a branch with some failing tests for my coworker to look at, without much hassle or annoyance.
So the jury is still out for me, but really I suspect the problem is just that the tooling has not caught up to the technology. Sadly, it seems you only get a little time in the sweet spot of good tooling and good technology before being forced to move to the next hot thing. I guess this is why most people just stick with the command line...