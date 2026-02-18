---
title: "Git is already federated & decentralized"
date: 2018-07-23
url: https://drewdevault.com/2018/07/23/Git-is-already-distributed.html
slug: Git-is-already-distributed
word_count: 1104
---

There have always been murmurs about “replacing GitHub with something
decentralized!”, but in the wake of the Microsoft acquisition these murmurs have
become conversations. In particular, this blog post is a direct response to
forge-net (formerly known as  [GitPub](https://github.com/git-federation/gitpub) ). They want to federate and
decentralize git using ActivityPub, the same technology leveraged by Mastodon
and PeerTube. But get this: git is already federated  *and*  decentralized!

I already spoke at length about how a large minority of the git community uses
email for collaboration in my  [previous article](https://drewdevault.com/2018/07/02/Email-driven-git.html)  on the subject.
Definitely give it a read if you haven’t already. In this article I want to
focus on comparing this model with the possibilities afforded by ActivityPub
and provide direction for new forge 1  projects to work towards embracing and
improving git’s email-based collaboration tools.

The main issue with using ActivityPub for decentralized git forges boils down to
email simply being a better choice. The advantages of email are numerous. It’s
already standardized and has countless open source implementations, many in the
standard libraries of almost every programming language. It’s decentralized and
federated, and it’s  *already*  integrated with git. Has been since day one!  I
don’t think that we should replace web forges with our email clients, not at
all. Instead, web forges should embrace email to communicate with each other.

Let me give an example of how this could play out. On my platform,
 [sr.ht](https://meta.sr.ht) , users can view their git repositories on the web
(duh). One of my goals is to add some UI features here which let them select a
range of commits and prepare a patchset for submission via  [git
send-email](https://www.git-scm.com/docs/git-send-email) . They’ll enter an email address (or addresses) to
send the patch(es) to, and we’ll send it along on their behalf.  This email
address might be a mailing list on another sr.ht instance in the wild! If so,
the email gets recognized as a patch and displayed on the web with a pretty diff
and code review tools. Inline comments automatically get formatted as an email
response. This shows up in the user’s inbox and sr.ht gets copied on it, showing
it on the web again.

I think that workflow looks an awful lot like the workflow forge-net hopes to
realize! Here’s where it gets good, though. What if the emails the user puts in
are  `linux-kernel@vger.kernel.org`  and a handful of kernel maintainers? Now your
git forge can suddenly be used to contribute to the Linux kernel! ActivityPub
would build a  *second* , incompatible federation of projects, while ignoring the
already productive federation which powers many of our most important open
source projects.

git over email is already supported by a tremendous amount of open source
software. There’s tools like  [mailman](https://www.gnu.org/software/mailman/)  which provide mailing lists and
public archives, or  [public-inbox](https://public-inbox.org/) , which archives email in git,
or  [patchworks](http://jk.ozlabs.org/projects/patchwork/)  for facilitating code review over email. Some email
clients have grown features which make them more suitable for git, such as
 [mutt](http://mutt.org) . These are the nuts and bolts of hundreds of important projects,
including Linux, *BSD, gcc, Clang, postgresql, MariaDb, emacs, vim, ffmpeg,
Linux distributions like Debian, Fedora, Arch, Alpine, and countless other
projects, including git itself! These projects are incredibly important,
foundational projects upon which our open source empire is built, and the tools
they use already provide an open, federated protocol for us to talk to.

Not only is email  *better* , but it’s also  *easier*  to implement. Programming
tools for email are very mature. I recently started experimenting with building
an ActivityPub service, and it was crazy difficult. I had to write a whole lot
of boilerplate and understand new and still-evolving specifications, not to
mention setting up a public-facing server with a domain and HTTPs to test
federation with other implementations. Email is comparatively easy, it’s built
into the standard library. You can shell out to git and feed the patch to the
nearest SMTP library in only a handful of lines of code. I bet every single
person who reads this article already has an email address, so the setup time
approaches zero.

Email also puts the power in the hands of the user right away. On Mastodon there
are occasional problems of instance owners tearing down their instance on short
notice, taking with them all of their user’s data. If everything is being
conducted over email instead, all of the data already lives in the user’s inbox.
Freely available tools can take their mail spool and publish a new archive if
our services go down. Mail archives can be trivially made redundant across many
services. This stuff is seriously resilient to failure. Email was designed when
networks were measured in bits per second and often connected through a single
unreliable route!

I’m not suggesting that the approach these projects use for collaboration is
perfect. I’m suggesting that we should embrace it and solve these problems
instead of throwing out the baby with the bathwater. Tools like  `git send-email` 
can be confusing at first, which is why we should build tools like web forges
that smooth over the process for novices, and write better docs to introduce
people to the tools (I recently  [wrote a guide](https://man.sr.ht/git.sr.ht/send-email.md)  for sr.ht users).

Additionally, many popular email clients have bastardized email to the point
where the only way to use git+email for many people starts with abandoning the
email client they’re used to using. This can also be solved by having forges
send the emails for them, and process the replies. We can also support open
source mail clients by building better tools to integrate our emails with them.
Setting up the mail servers on the other end can be difficult, too, but we
should invest in better mail server software, something which would definitely
be valuable even setting aside the matter of project forges.

We need to figure out something for bugs as well, perhaps based on Debian’s work
on  [Debbugs](https://www.debian.org/Bugs/) . Other areas of development, such as
continuous integration, I find are less difficult problems. Many build services
already support sending the build results by email, we just need to find a way
to get our patches to them (something I’m working on with sr.ht). But we should
take these problems one step at a time. Let’s focus on improving the patch
workflow git endorses, and as our solutions shake out the best solutions to our
other problems will become more and more apparent.

1. Forge refers to any software which provides comprehensive tools for project hosting. This originally referred to SourceForge but is now a category of software which includes GitHub, BitBucket, GitLab, Gogs/Gitea, etc. ↩︎
