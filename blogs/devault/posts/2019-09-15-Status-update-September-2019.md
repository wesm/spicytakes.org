---
title: "Status update, September 2019"
date: 2019-09-15
url: https://drewdevault.com/2019/09/15/Status-update-September-2019.html
slug: Status-update-September-2019
word_count: 672
---

Finally home again after a long series of travels! I spent almost a month in
Japan, then visited my sister’s new home in Hawaii on the way eastwards, then
some old friends in Seattle, and finally after 5½ long weeks, it’s home sweet
home here in Philadelphia. At least until I leave for
 [XDC](https://xdc2019.x.org/)  in Montreal 2 weeks from now. Someday I’ll have
some rest… throughout all of these wild travels, I’ve been hard at work on my
free software projects. Let’s get started with this month’s status update!

Great view from a hike on O'ahu

First, Wayland news. I’m happy to share with you that the Wayland book is now
more than halfway complete, and I’ve made the drafts available online for a
discounted price:  [The Wayland Protocol](https://wayland-book.com) . Thanks to
all of my collaborators and readers who volunteered to provide feedback! There’s
more Wayland-related news still, as this month marked the release of  [sway
1.2](https://github.com/swaywm/sway/releases/tag/1.2)  and  [wlroots 0.7.0](https://github.com/swaywm/wlroots/releases/tag/0.7.0) . I like this release
because it’s light on new features - showing that sway is maturing into a stable
and reliable Wayland desktop. The features which were added are subtle and serve
to improve sway’s status as a member of the broader ecosystem - sway 1.2
supports the new  [layer shell support in the MATE panel](https://github.com/mate-desktop/mate-panel/pull/991) , and the
same improvements are already helping with the development of other software.

Rest assured, the weird alignment issues were fixed

On the topic of  [aerc](https://aerc-mail.org) , I still haven’t gotten around to
that write-up responding to  [Greg KH’s post](http://www.kroah.com/log/blog/2019/08/14/patch-workflow-with-mutt-2019/) … but I will. Travels have
made it difficult to sit down for a while and do some serious long-term project
planning. Regardless, the current plans have still been being executed well.
Notmuch support continues to improve thanks to Reto Brunner’s help, completions
are improving throughout, and heaps of little features - signatures, unread
message counts, :prompt, forward-as-attachment - are now supported.

I also spent some time this month working on Simon Ser’s
 [mrsh](https://mrsh.sh) . I cleaned up call frames, implemented the  `return` 
builtin, finished the  `pwd`  builtin, improved readline support, fleshed out job
control, and made many other small improvements. With mrsh nearing completion,
I’ve started up another project:  [ctools](https://git.sr.ht/~sircmpwn/ctools) . This provides the rest of the
POSIX commands required of a standard scripting environment (it replaces
coreutils or busybox). I’m taking this one pretty seriously from the start -
every command has full POSIX.1-2017 support with a conformance test and a man
page, in one C source file and no dependencies. If you’re looking for a good
afternoon project (or weekend, for some utilities), how about picking up your
favorite  [POSIX](https://pubs.opengroup.org/onlinepubs/9699919799/)  tool and
sending along an implementation?

With these projects, along with ~mcf’s  [cproc](https://git.sr.ht/~mcf/cproc) ,
we’re starting to see a simple and elegant operating system come together -
exactly the kind I wish we already had. To track our progress towards this goal,
I’ve put up  [arewesimpleyet.org](https://arewesimpleyet.org) . A day may soon
come when computers become the again elegant and simple tools they were always
meant to be! At least if we assume “within a few decades” as a valid definition
of “soon”.

To cover SourceHut news briefly: we hit 10,000 users this month! And it’s
continued to grow since, up to 10,649 users at the time of writing. On the
subject of feature development, with Denis Laxalde’s help we’re starting to put
together a Debian repository for installing the services on Debian hosts. On
todo.sr.ht, users without accounts can now create and comment on tickets via
email. I also redesigned  [sourcehut.org](https://sourcehut.org) , adding a blog
with a greater breadth of topics than we’ll see on the sr.ht-announce mailing
list.

That’s all for this month! I enjoyed my vacation and some much needed time away
from work… though for me a “day off” is a day where I write less than 1,000
lines of code. Thank you again for your support - it means the world to me. I’ll
see you next month!

Had the best seats at a concert in Tokyo!
