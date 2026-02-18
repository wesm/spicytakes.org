---
title: "How to abandon a FLOSS project"
date: 2018-12-04
url: https://drewdevault.com/2018/12/04/How-to-abandon-a-FLOSS-project.html
slug: How-to-abandon-a-FLOSS-project
word_count: 663
---

It’s no secret that maintaining free and open source software is often
a burdensome and thankless job. I empathise with maintainers who lost interest
in a project, became demotivated by the endless demands of users, or are no
longer blessed with enough free time. Whatever the reason, FLOSS work is
volunteer work, and you’re free to stop volunteering at any time.

In my opinion, there are two good ways to abandon a project: the  *fork it* 
option and the  *hand-off*  option. The former is faster and easier, and you can
pick this if you want to wash your hands of the project ASAP, but has a larger
effect on the community. The latter is not always possible, requires more work
on your part, and takes longer, but it has a minimal impact on the community.

Let’s talk about the easy way first. Start by adding a notice to your README
that your software is now unmaintained. If you have the patience, give a few
weeks notice before you really stop paying attention to it. Inform interested
parties that they should consider forking the software and maintaining it
themselves under another name. Once a fork gains traction, update the README
again to direct would-be users to the fork. If no one forks it, you could
consider directing users to similar alternatives to your software.

This approach allows you to quickly absolve yourself of responsibility. Your
software is no worse than it was yesterday, which allows users a grace period to
collect themselves and start up a fork. If you revisit your work later, you can
also become a contributor to the fork yourself, which removes the stress of
being a maintainer while still providing value to the project. Or, you can just
wash your hands of it entirely and move on to bigger and better things. This
“fork it” approach is safer than giving control of your project to passerby,
because it requires your users to acknowledge the transfer of power, instead of
being surprised by a new maintainer in a trusted package.

The “fork it” approach is well suited when the maintainer wants out ASAP, or for
smaller projects with little activity. But, for active projects with a patient
maintainer, the hand-off approach is less disruptive. Start talking with some of
your major contributors about  [increasing their involvement](/2018/06/01/How-I-maintain-FOSS-projects.html) 
in the administrative side of the projects. Mentor them on doing code reviews,
ticket triage, sysadmin stuff, marketing - all the stuff you have to do - and
gradually share these responsibilities with them.  These people eventually
become productive co-maintainers, and once established you can step away from
the project with little fanfare.

Taking this approach can also help you find healthier ways to be involved in
your own project. This can allow you to focus on the work you enjoy and spend
less time on the work you don’t enjoy, which might even restore your enthusiasm
for the project outright! This is also a good idea even if you aren’t planning
on stepping down - it encourages your contributors to take personal stake in the
project, which makes them more productive and engaged. This also makes your
community more resilient to  [author existence failure](https://tvtropes.org/pmwiki/pmwiki.php/Main/AuthorExistenceFailure) , so
that when circumstance forces you to step down the project continues to be
healthy.

It’s important to always be happy in your work, and especially in your volunteer
work. If it’s not working, then change it. For me, this happens in different
ways. I’ve abandoned projects outright and sent users off to make their own fork
before.  I’ve also handed projects over to their major contributors. In some
projects I’ve appointed new maintainers and scaled back my role to a mere
contributor, and in other projects I’ve moved towards roles in marketing,
outreach, management, and stepped away from development. There’s no shame in
any of these changes - you still deserve pride in your accomplishments, and
seeking constructive solutions to burnout would do your community a great
service.
