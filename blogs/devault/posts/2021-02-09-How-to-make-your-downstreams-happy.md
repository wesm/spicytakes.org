---
title: "How to make your downstream users happy"
date: 2021-02-09
url: https://drewdevault.com/2021/02/09/How-to-make-your-downstreams-happy.html
slug: How-to-make-your-downstreams-happy
word_count: 509
---

There are a number of things that your FOSS project can be doing which will make
the lives of your downstream users easier, particularly if you’re writing a
library or programmer-facing tooling. Many of your downstreams (Linux distros,
pkgsrc, corporate users, etc) are dealing with lots of packages, and some minor
tweaks to your workflow will help them out a lot.

The first thing to do is  *avoid*  using any build system or packaging system
which is not the norm for your language. Also avoid incorporating information
into your build which relies on being in your git repo — most packagers
prefer to work with tarball snapshots, or to fetch your package from e.g. PyPI.
These two issues are definitely the worst offenders. If you do have to use a
custom build system, take your time to document it thoroughly, so that users who
run into problems are well-equipped to address them. The typical build system or
packaging process in use for your language already addressed most of those edge
cases long ago, which is why we like it better. If you must fetch, say, version
information from git, then please add a fallback, such as an environment
variable.

Speaking of environment variables, another good one to support is
 [SOURCE_DATE_EPOCH](https://reproducible-builds.org/docs/source-date-epoch/) ,
for anything where the current date or time is incorporated into your build
output. Many distros are striving for  *reproducible*  builds these days, which
involves being able to run a build twice, or by two independent parties, and
arrive at an identical checksum-verifiable result. You can probably imagine some
other ways to prevent issues here — don’t incorporate the full path to
each file in your logs, for instance. There are more recommendations on the
website linked earlier.

Though we don’t like to rely on it as part of the formal packaging process, a
good git discipline will also help us with the informal parts. You may already
be using  [git tags](https://git-scm.com/docs/git-tag)  for your releases — consider putting a changelog
into your annotated tags (git tag -a). If you have  [good commit discipline](https://drewdevault.com/2019/02/25/Using-git-with-discipline.html) 
in your project, then you can easily use  [git shortlog](https://git-scm.com/docs/git-shortlog)  to generate such a
changelog from your commit messages. This helps us understand what we can expect
when upgrading, which helps incentivize us to upgrade in the first place. In
 [How to fuck up software releases](https://drewdevault.com/2019/10/12/how-to-fuck-up-releases.html) , I wrote about my  [semver](https://git.sr.ht/~sircmpwn/dotfiles/tree/master/bin/semver)  tool, which
you may find helpful in automating this process. It can also help you avoid
forgetting to do things like update the version number somewhere in the code.

In short, to make your downstreams happy:

1. Don’t rock the boat on builds and packaging.
2. Don’t expect your code to always be in a git repo.
3. Consider reproducible builds.
4. Stick a detailed changelog in your annotated tag — which is easy if you
have good commit discipline.

Overall, this is pretty easy stuff, and good practices which pay off in other
respects as well. Here’s a big “thanks” in advance from your future downstreams
for your efforts in this regard!
