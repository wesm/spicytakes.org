---
title: "Learn about your package manager"
date: 2018-01-10
url: https://drewdevault.com/2018/01/10/Learn-your-package-manager.html
slug: Learn-your-package-manager
word_count: 357
---

Tools like virtualenv, rbenv, and to a lesser extent npm and pip, are
occasionally useful in development but encourage bad practices in production.
Many people forget that their distro already has a package manager! And there’s
more– you, the user, can write packages for it!

Your distro’s package repositories probably already have a lot of your
dependencies, and can conveniently update your software alongside the rest of
your system. On the whole you can expect your distro packages to be much better
citizens on your system than a language-specific package manager will be.
Additionally, pretty much all distros provide a means for you to host your own
package repositories, from which you can install and update any packages you
choose to make.

If you find some packages to be outdated, find out who the package maintainer is
and shoot them an email. Or better yet - find out how the package is built and
send them a patch instead. Linux distributions are run by volunteers, and it’s
easy to volunteer yourself! Even if you find  *missing*  packages, it’s a simple
matter to whip up a package yourself and submit it for inclusion in your
distro’s package repository, installing it from your private repo in the
meanwhile.

“But what if dependencies update and break my stuff?”, you ask. First of all,
why aren’t you keeping your dependencies up-to-date? That aside, some distros,
like Alpine, let you pin packages to a specific version. Also, using the
distro’s package manager doesn’t necessarily mean you have to use the distro’s
package repositories - you can stand up your own repos and prioritize it over
the distro repos, then release on any schedule you want.

In my opinion, the perfect deployment strategy for some software is pushing a
new package to your package repository, then SSHing into your fleet and running
system updates (probably automatically). This is how I manage deployments for
most of my software. As a bonus, these packages offer a good place to configure
things that your language’s package manager may be ill suited to, such as
service files or setting up new users/groups on the system. Consider it!
