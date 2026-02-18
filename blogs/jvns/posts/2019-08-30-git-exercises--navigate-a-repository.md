---
title: "git exercises: navigate a repository"
date: 2019-08-30
url: https://jvns.ca/blog/2019/08/30/git-exercises--navigate-a-repository/
slug: git-exercises--navigate-a-repository
word_count: 1122
---


I think the [curl exercises](https://jvns.ca/blog/2019/08/27/curl-exercises/) the other day went
well, so today I woke up and wanted to try writing some Git exercises. Git is a big thing to learn,
probably too big to learn in a few hours, so my first idea for how to break it down was by starting
by **navigating** a repository.


I was originally going to use a toy test repository, but then I thought – why not a real
repository? That’s way more fun! So we’re going to navigate the repository for the Ruby programming
language. You don’t need to know any C to do this exercise, it’s just about getting comfortable with
looking at how files in a repository change over time.


### clone the repository


To get started, clone the repository:


```
git clone https://github.com/ruby/ruby

```


The big different thing about this repository (as compared to most of the repositories you’ll work
with in real life) is that it doesn’t have branches, but it DOES have lots of tags, which are
similar to branches in that they’re both just pointers to a commit. So we’ll do exercises with tags
instead of branches. The way you *change* tags and branches are very different, but the way you
*look at* tags and branches is exactly the same.


### a git SHA always refers to the same code


The most important thing to keep in mind while doing these exercises is that a git SHA like
`9e3d9a2a009d2a0281802a84e1c5cc1c887edc71` always refers to the same code, as explained in this
page. This page is from a zine I wrote with Katie Sylor-Miller called [Oh shit, git!](https://wizardzines.com/zines/oh-shit-git/). (She also has a great site called
[https://ohshitgit.com/](https://ohshitgit.com/) that inspired the zine).


We’ll be using git SHAs really heavily in the exercises to get you used to working with them and
to help understand how they correspond to tags and branches.


### git subcommands we’ll be using


All of these exercises only use 5 git subcommands:


```
git checkout
git log (--oneline, --author, and -S will be useful)
git diff (--stat will be useful)
git show
git status

```


### exercises

1. Check out matz’s commit of Ruby from 1998. The commit ID is `3db12e8b236ac8f88db8eb4690d10e4a3b8dbcd4`. Find out how many lines of code Ruby was at that time.
2. Check out the current master branch
3. Look at the history for the file `hash.c`. What was the last commit ID that changed that file?
4. Get a diff of how `hash.c` has changed in the last 20ish years: compare that file on the master
branch to the file at commit `3db12e8b236ac8f88db8eb4690d10e4a3b8dbcd4`.
5. Find a recent commit that changed `hash.c` and look at the diff for that commit
6. This repository has a bunch of **tags** for every Ruby release. Get a list of all the tags.
7. Find out how many files changed between tag `v1_8_6_187` and tag `v1_8_6_188`
8. Find a commit (any commit) from 2015 and check it out, look at the files very briefly, then go back to the master branch.
9. Find out what commit the tag `v1_8_6_187` corresponds to.
10. List the directory `.git/refs/tags`. Run `cat .git/refs/tags/v1_8_6_187` to see the contents
of one of those files.
11. Find out what commit ID `HEAD` corresponds to right now.
12. Find out how many commits have been made to the `test/` directory
13. Get a diff of `lib/telnet.rb` between the commits `65a5162550f58047974793cdc8067a970b2435c0` and
`9e3d9a2a009d2a0281802a84e1c5cc1c887edc71`. How many lines of that file were changed?
14. How many commits were made between Ruby 2.5.1 and 2.5.2 (tags `v2_5_1` and `v2_5_3`)
15. How many commits were authored by `matz` (Ruby’s creator)?
16. What’s the most recent commit that included the word `tkutil`?
17. Check out the commit `e51dca2596db9567bd4d698b18b4d300575d3881` and create a new branch that
points at that commit.
18. Run `git reflog` to see all the navigating of the repository you’ve done so far


**Question #1: **Check out matz's commit of Ruby from 1998. The commit ID is `3db12e8b236ac8f88db8eb4690d10e4a3b8dbcd4`. Find out how many lines of code Ruby was at that time.

**Solution #1: **

git checkout 3db12e8b236ac8f88db8eb4690d10e4a3b8dbcd4
find . -name '*.c' | xargs wc -l



**Question #2:** Check out the current master branch

**Solution #2:**

git checkout master



**Question #3:** Look at the history for the file `hash.c`. What was the last commit ID that changed that file?
**Solution #3:**

git log hash.c
# look at the first line to get the commit ID. 
# I got 3df37259d81d9fc71f8b4f0b8d45dc9d0af81ab4.




**Question #4:** Get a diff of how `hash.c` has changed in the last 20ish years: compare that file on the master branch to the file at commit `3db12e8b236ac8f88db8eb4690d10e4a3b8dbcd4`.
**Solution #4:**

git diff 3db12e8b236ac8f88db8eb4690d10e4a3b8dbcd4 hash.c



**Question #5:** Find a recent commit that changed `hash.c` and look at the diff for that commit
**Solution #5:**

git log hash.c
# look at the first line to get the commit ID. 
# I got 3df37259d81d9fc71f8b4f0b8d45dc9d0af81ab4.
git show 3df37259d81d9fc71f8b4f0b8d45dc9d0af81ab4



**Question #6:** This repository has a bunch of **tags** for every Ruby release. Get a list of all the tags.
**Solution #6:**

git tags



**Question #7:** Find out how many files changed between tag `v1_8_6_187` and tag `v1_8_6_188`
**Solution #7:**

git diff v1_8_6_187 v1_8_6_188 --stat
# 5 files!



**Question #8:** Find a commit (any commit) from 2015 and check it out, look at the files very briefly, then go back to the master branch.
**Solution #8:**

git log | grep -C 2 ' 2015 ' | head
git checkout bd5d443a56ee4bcb59a0a08776c07dea3ee60121
ls
git checkout master



**Question #9:** Find out what commit the tag `v1_8_6_187` corresponds to.
**Solution #9:**

git show v1_8_6_187



**Question #10:** List the directory `.git/refs/tags`. Run `cat .git/refs/tags/v1_8_6_187` to see the contents of one of those files.
**Solution #10:**

$ cat .git/refs/tags/v1_8_6_187
928e6916b25aee5b2b379999a3fa8816d40db714



**Question #11:** Find out what commit ID `HEAD` corresponds to right now.
**Solution #11:**

git show HEAD



**Question #12:** Find out how many commits have been made to the `test/` directory
**Solution #12:**

git log --oneline test/ | wc



**Question #13:** Get a diff of `lib/telnet.rb` between the commits `f2a91397fd7f9ca5bb3d296ec6df2de6f9cfc7cb` and `e44c9b11475d0be2f63286c1332a48da1b4d8626 `. How many lines of that file were changed?
**Solution #13:**

git diff f2a91397fd7f9..e44c9b11475d0 lib/tempfile.rb



**Question #14:** How many commits were made between Ruby 2.5.1 and 2.5.2 (tags `v2_5_1` and `v2_5_3`) 
**Solution #14:**

git log v2_5_1..v2_5_3 --oneline | wc



**Question #15:** How many commits were authored by `matz` (Ruby's creator)?
**Solution #15:**

git log --oneline --author matz | wc -l



**Question #16:** What's the most recent commit that included the word `tkutil`?
**Solution #16:**

git log -S tkutil
# result is 6c5f5233db596c2c7708d5807d9a925a3a0ee73a



**Question #17:** Check out the commit `e51dca2596db9567bd4d698b18b4d300575d3881` and create a new branch that points at that commit. 
**Solution #17:**

git checkout e51dca2596db9567bd4d698b18b4d300575d3881
git branch my-branch



**Question #18:** Run `git reflog` to see all the navigating of the repository you've done so far
**Solution #18:**

git reflog
