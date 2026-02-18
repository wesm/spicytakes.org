---
title: "What is a fork, really, and how GitHub changed its meaning"
date: 2019-05-24
url: https://drewdevault.com/2019/05/24/What-is-a-fork.html
slug: What-is-a-fork
word_count: 1264
---

The fork button on GitHub - with the little number next to it for depositing
dopamine into your brain - is a bit misleading. GitHub co-opted the meaning of
“fork” to trick you into participating in their platform more. They did this in
a well-intentioned way, for the sake of their pull requests feature, but
ultimately this design is self-serving and causes some friction when
contributors venture out of their GitHub sandbox and into the rest of the
software development ecosystem. Let’s clarify what “fork” really means, and what
we do without GitHub’s concept of one - for it is in this difference that we
truly discover how git is a  *distributed*  version control system.

**Disclaimer** : I am the founder of  [SourceHut](https://sourcehut.org) , a
product which competes with GitHub and embraces the “bazaar 1 ” model described
in this article.

On GitHub, a fork refers to a copy of a repository used by a contributor 2  to
stage changes they’d like to propose upstream. Prior to GitHub (and in many
places still today), we’d call such a repository a “personal branch”. A personal
branch doesn’t need to be published to be useful - you can just  `git clone`  it
locally and make your changes there without pushing them to a public, hosted
repository. Using  [email](https://git-send-email.io) , you can send changes from
your local, unpublished repository for consideration upstream. Outside of
GitHub and its imitators, most contributors to a project don’t have a published
version of their repository online at all, skipping that step and saving some
time.

In some cases, however, it’s useful to publish your personal branch online. This
is often done when a team of people is working on a long-lived branch to later
propose upstream - for example, I’ve been doing this while working on the RISC-V
port of musl libc. It gives us a space to collaborate and work while preparing
changes which will eventually be proposed upstream, as well as a place for
interested testers to obtain our experimental work to try themselves. This is
also done by individuals, such as Greg Kroah-Hartman’s Linux branches, which are
useful for testing upcoming changes to the Linux kernel.

Greg is not alone in publishing a repo like this. In fact, there are  [hundreds of
kernel trees like this](https://git.kernel.org/pub/scm/linux/kernel/git/) . These act as staging areas for long-term
workstreams, or for the maintainers of many subsystems of the kernel.  Changes
in these repositories gradually flow upwards towards the “main” tree,
 [torvalds/linux](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/) . The precise meaning of “linux” is rather loose
in this context. An argument could be made that torvalds/linux is Linux, but
that definition wouldn’t capture the LTS branches. Many distros also apply their
own patches on top of Torvalds, perhaps sourcing them from the maintainers of
drivers they need a bugfix for, or they maintain their own independent trees
which periodically pull in lump sums of changes from other trees - meaning that
the simple definition might not include the version of Linux which is installed
on your computer, either. This ambiguity is a feature - each of these trees is a
valid definition of Linux in its own right.

This is the sense in which git is “distributed”. The idea of a canonical
upstream is not written in stone in the way that GitHub suggests it might be.
After all, open-source software is a collaborative endeavour. What makes Jim’s
branch more important that John’s branch? John’s branch is definitely more
important if it has the bugfixes you need. In fact, your branch, based on Jim’s,
with some patches cherry-picked from John, and a couple of fixes of your own
mixed in, may in fact be the best version of the software for you.

This is how the git community gets along without the GitHub model of “forks”.
This design has allowed the largest and most important projects in the world to
flourish, and git was explicitly designed around this model. We refer to this as
the “bazaar” model, the metaphor hopefully being fairly obvious at this point.
There is another model, which GitHub embodies instead: the cathedral. In this
model, the project has a central home and centralized governance, run by a small
number of people. The cathedral doesn’t necessarily depend on the GitHub idea of
“forks” and pull requests - that is, you can construct a cathedral with
email-driven development or some other model - but on GitHub the bazaar option
is basically absent.

In the introduction I said that GitHub attempts to replace an existing meaning
for “fork”. So what does forking actually mean, then? Consider a project with
the cathedral model. What happens when there’s a schism in the church? The
answer is that some of the contributors can take the code, put up a new branch
somewhere, and stake a flag in the ground. They rename it and commit to
maintaining it entirely independently of the original project, and encourage
contributors, new and old alike, to abandon the old dogma in favor of theirs.
At this point, the history 3  begins to diverge. The new contingent pulls in
all of the patches that were denied upstream and start that big refactoring to
mold it in their vision. The project has been  **forked** . A well known example
is when ffmpeg was forked to create libav.

This is usually a traumatic event for the project, and can have repercussions
that last for years. The precise considerations that should go into forking a
project, these repercussions and how to address them, and other musings are
better suited for a separate article. But this is what “fork” meant before
GitHub, and this meaning is still used today - albeit more ambiguously.

If “fork” already had this meaning, why did GitHub adopt their model? The
answer, as it often will be, is centralization of power. GitHub is a
proprietary, commercial service, and their ultimate goal is to turn a profit.
The design of GitHub’s fork and pull request model creates a cathedral that
keeps people on their platform in a way that a bazaar would not. A distributed
version control system like git, built on a distributed communications protocol
like email, is hard to disrupt with a centralized service. So GitHub designed
their own model.

As a parting note, I would like to clarify that this isn’t a condemnation of
GitHub. I still use their service for a few projects, and appreciate the
important role GitHub has played in the popularization of open source. However,
I think it’s important to examine the services we depend on, to strive to
understand their motivations and design. I also hope the reader will view the
software ecosystem through a more interesting lens for having read this article.
Thank you for reading!

**P.S.**  Did you know that GitHub also captured the meaning of “pull request”
from git’s own  [request-pull](https://www.git-scm.com/docs/git-request-pull) 
tool? git request-pull prepares an email which will ask the recipient to fetch
changes from a public repository and integrate them into their own branch. This
is used when a patch is insufficient - for example, when Linux subsystem
maintainers want to ship a large group of changes to Torvalds for the next
kernel release. Again, the original version is distributed and bazaar-like,
whereas GitHub’s is centralized and makes you stay on their platform.

1. Not the bazaar version control system, but bazaar the concept. This is explained later in the article. ↩︎
2. And by bots to increase their reputation, and by confused users who don’t know what the button means. ↩︎
3. Git history in particular, but also the other kind. ↩︎
