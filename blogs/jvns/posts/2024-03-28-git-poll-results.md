---
title: "Some Git poll results"
date: 2024-03-28
url: https://jvns.ca/blog/2024/03/28/git-poll-results/
slug: git-poll-results
word_count: 1889
---


A new thing I’ve been trying while writing this Git zine is doing a bunch of polls on Mastodon to learn about:

- which git commands/workflows people use (like “do you use merge or rebase more?” or “do you put your current git branch in your shell prompt?”)
- what kinds of problems people run into with git (like “have you lost work because of a git problem in the last year or two?”)
- which terminology people find confusing (like “how confident do you feel that you know what HEAD means in git?”)
- how people think about various git concepts (“how do you think about git branches?”)
- in what ways my usage of git is “normal” and in what ways it’s “weird”. Where am I pretty similar to the majority of people, and where am I different?


It’s been a lot of fun and some of the results have been surprising to me, so
here are some of the results. I’m partly just posting these so that I can have
them all in one place for myself to refer to, but maybe some of you will find
them interesting too.


### these polls are highly unscientific


Polls on social media that I thought about for approximately 45 seconds before
posting are not the most rigorous way of doing user research, so I’m pretty
cautious about drawing conclusions from them. Potential problems include: I
phrased the poll badly, the set of possible responses aren’t chosen very
carefully, some of the poll responses I just picked because I thought they were
funny, and the set of people who follow me on Mastodon is not representative of
all git users.


But here are a couple of examples of why I still find these poll results useful:

- The first poll is “what’s your approach to merge commits and rebase in git”?
600 people (30% of responders) replied “I usually use merge, rarely/never
rebase”. It’s helpful for me to know that there are a lot of people
out there who rarely/never use rebase, because I use rebase all the time –
it’s a good reminder that my experiences isn’t necessarily representative.
- For the poll “how confident do you feel that you know what HEAD means in
git?”, 14% of people replied “literally no idea”. That tells me to be careful
about assuming that people know what `HEAD` means in my writing.


### where to read more


If you want to read more about any given poll, you can click at the date at the
bottom – there’s usually a bunch of interesting follow-up discussion.


Also this post has a lot of CSS so it might not work well in a feed reader.


Now! Here are the polls! I’m mostly just going to post the results without
commenting on them.


### merge and rebase


poll: what's your approach to merge commits and rebase in git?

- 41%usually rebase, rarely/never create merge commits
- 29%usually merge, rarely/never rebase
- 24%i do both all the time
- 4%other / show results

1872 people
·
[Dec 14, 2023, 21:06](https://social.jvns.ca/@b0rk/111580808091928044)

### merge conflicts


poll: if you use git, how often do you deal with nontrivial merge conflicts? (like where 2 people were really editing the same code at the same time and you need to take time to think about how to reconcile the edits)

- 10%~every week or so
- 33%~every month or so
- 52%very rarely/never (a few times a year at most)
- 4%other/show results

2009 people
·
[Jan 03, 2024, 18:43](https://social.jvns.ca/@b0rk/111693491747888221)

another merge conflict poll:


have you ever seen a bug in production caused by an incorrect merge conflict resolution? I've heard about this as a reason to prefer merges over rebase (because it makes the merge conflict resolution easier to audit) and I'm curious about how common it is

- 14%yes, many times
- 47%yes, but only once or twice
- 32%no
- 5%other/show results

1482 people
·
[Jan 03, 2024, 18:59](https://social.jvns.ca/@b0rk/111693554375140434)

I thought it was interesting in the next one that “edit the weird text file by hand” was most people’s preference:


poll: when you have a merge conflict, how do you prefer to handle it?

- 58%edit the weird text file by hand
- 34%use a merge conflict tool
- 5%delete your work and start over
- 1%other

2380 people
·
[Feb 22, 2024, 15:17](https://social.jvns.ca/@b0rk/111975796153138514)

merge conflict follow up: if you prefer to edit the weird text file by hand instead of using a dedicated merge conflict tool, why is that?

- 24%most merge conflicts are simple
- 23%it's infrequent, not worth learning another tool
- 38%prefer to use my usual text editor
- 13%other

1093 people
·
[Feb 23, 2024, 20:22](https://social.jvns.ca/@b0rk/111982657794956944)

poll: did you know that in a git merge conflict, the order of the code is different when you do a merge/rebase?


merge:


<<<<<<< HEAD
    YOUR CODE
=======
    OTHER BRANCH'S CODE
>>>>>>> c694cf8aabe


rebase:


<<<<<<< HEAD
    OTHER BRANCH'S CODE
=======
    YOUR CODE
>>>>>>> d945752 (your commit message)


(where "YOUR CODE" is the code from the branch you were on when you ran `git merge` or `git rebase`)

- 15%yes
- 14%yes, mostly
- 48%no
- 21%what?

1511 people
·
[Mar 11, 2024, 14:17](https://social.jvns.ca/@b0rk/112077480397781920)

### git pull


poll: do you prefer `git fetch` or `git pull`?


(no lectures about why you think `git pull` is bad please but if you use both I'd be curious to hear in what cases you use fetch!)

- 12%only `git fetch`
- 37%only `git pull`
- 48%mix of both
- 1%other

2036 people
·
[Mar 18, 2024, 20:07](https://social.jvns.ca/@b0rk/112118493083676573)

### commits


[poll] how do you think of a git commit?


(sorry, you can't pick “it’s all 3”, I'm curious about which one feels most true to you)

- 50%a **diff** from the previous commit
- 42%a **snapshot** of the current state
- 3%a **history** of every past commit
- 2%other/show results

2466 people
·
[Dec 11, 2023, 18:18](https://social.jvns.ca/@b0rk/111563158717698550)

### branches


poll: how do you think about git branches? (I'll put an image in a reply with pictures for the 3 options)


as with all of these polls obviously all 3 are valid, I'm curious which one feels the most true to you

- 58%1. just the commits that "branch" off
- 22%2. the history of every previous commit
- 15%3. just the commit at the end ("branch = pointer")
- 3%other / show results

1966 people
·
[Jan 06, 2024, 14:24](https://social.jvns.ca/@b0rk/111709458396281239)

### git environment


poll: do you put your current git branch in your shell prompt?

- 71%yes
- 22%no
- 3%no, but I don't use git on the command line
- 1%other/show results

2365 people
·
[Jan 18, 2024, 15:38](https://social.jvns.ca/@b0rk/111777697732765132)

poll: do you use git on the command line or in a GUI?


(you can pick more than one option if it’s a mix of both, sorry magit users I didn't have space for you in this poll)

- 80%command line, regularly
- 29%GUI, regularly
- 13%command line, occasionally
- 16%GUI, occasionally

2661 people
·
[Feb 29, 2024, 12:38](https://social.jvns.ca/@b0rk/112014805256252757)

### losing work


poll: have you lost work because of a git problem in the last year or two? (it counts even if it was "your fault" :))

- 17%yes
- 76%no
- 4%no, but git did something else unforgivable
- 1%other

1475 people
·
[Feb 14, 2024, 14:14](https://social.jvns.ca/@b0rk/111930248586728989)

### meaning of various git terms


These polls gave me the impression that for a lot of git terms (fast-forward,
reference, HEAD), there are a lot of git users who have “literally no idea”
what they mean. That makes me want to be careful about using and defining those
terms.


poll: how confident do you feel that you know what HEAD means in git?

- 10%100%
- 36%pretty confident
- 38%somewhat confident?
- 14%literally no idea

1783 people
·
[Mar 06, 2024, 15:02](https://social.jvns.ca/@b0rk/112049348927204770)

another poll: how do you think of HEAD in git?

- 67%a pointer to the current commit
- 25%a pointer to the current branch (usually)
- 6%other

1386 people
·
[Mar 06, 2024, 17:57](https://social.jvns.ca/@b0rk/112050034752815560)

poll: when you see this message in `git status`:


”Your branch is up to date with 'origin/main’.”


do you know that your branch may not actually be up to date with the `main` branch on the remote?

- 63%yes
- 15%mostly yes
- 7%no
- 13%what?

2332 people
·
[Mar 08, 2024, 19:04](https://social.jvns.ca/@b0rk/112061622761219585)

poll: how confident do you feel that you know what the term "fast-forward" means in git, for example in this error message:


`! [rejected]        main -> main (non-fast-forward)`


or this one:


fatal: Not possible to fast-forward, aborting.


(I promise this is not a trick question, I'm just writing a blog post about git terminology and I'm trying to gauge how people feel about various core git terms)

- 25%100%
- 31%pretty confident
- 20%somewhat confident?
- 21%literally no idea

1629 people
·
[Mar 11, 2024, 17:59](https://social.jvns.ca/@b0rk/112078355085525822)

poll: how confident do you feel that you know what a "ref" or "reference" is in git? (“ref” and “reference” are the same thing)


for example in this error message (from `git push`)


error: failed to push some refs to 'github.com:jvns/int-exposed'


or this one:  (from `git switch mybranch`)


fatal: invalid reference: mybranch

- 9%100%
- 28%pretty confident
- 31%somewhat confident?
- 29%literally no idea

1117 people
·
[Mar 13, 2024, 13:41](https://social.jvns.ca/@b0rk/112088664114767341)

another git terminology poll: how confident do you feel that you know what a git commit is?


(not a trick question, I'm mostly curious how this one relates to people's reported confidence about more "advanced" terms like reference/fast-forward/HEAD)

- 32%100%
- 50%pretty confident
- 15%somewhat confident?
- 1%literally no idea

1294 people
·
[Mar 15, 2024, 13:15](https://social.jvns.ca/@b0rk/112099886480664238)

poll: in git, do you think of "detached HEAD state" and "not having any branch checked out" as being the same thing?

- 52%yes
- 27%no
- 17%what?
- 2%other

1278 people
·
[Mar 21, 2024, 18:34](https://social.jvns.ca/@b0rk/112135116065832096)

poll: how confident do you feel that you know what the term "current branch" means in git?


(deleted & reposted to clarify that I'm asking about the meaning of the term)

- 26%100%
- 49%pretty confident
- 18%somewhat confident?
- 4%literally no idea

1282 people
·
[Mar 21, 2024, 19:24](https://social.jvns.ca/@b0rk/112135312540813733)

### other version control systems


I occasionally hear “SVN was better than git!” but this “svn vs git” poll makes
me think that’s a minority opinion. I’m much more cautious about concluding anything from the hg-vs-git poll but it does seem like some people prefer git
and some people prefer Mercurial.


poll 2: if you've used both svn and git, which do you prefer?


(no replies please, i have already read 300 comments about git vs other version control systems today and they were great but i can't read more)

- 3%svn
- 91%git
- 3%depends
- 1%other

1642 people
·
[Mar 19, 2024, 21:16](https://social.jvns.ca/@b0rk/112124427045371322)

gonna do a short thread of git vs other version control systems polls just to get an overall vibe


poll 1: if you've used both hg and git, which do you prefer?


(no replies please though, i have already read 300 comments about git vs other version control systems today and i can't read more)

- 21%hg
- 65%git
- 7%depends
- 5%other

684 people
·
[Mar 19, 2024, 21:15](https://social.jvns.ca/@b0rk/112124423512955698)

### that’s all!


It’s been very fun to run all of these polls and I’ve learned a lot about how
people use and think about git.
