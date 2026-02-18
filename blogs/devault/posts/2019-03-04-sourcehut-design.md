---
title: "Sourcehut's spartan approach to web design"
date: 2019-03-04
url: https://drewdevault.com/2019/03/04/sourcehut-design.html
slug: sourcehut-design
word_count: 599
---

[Sourcehut](https://sourcehut.org)  is known for its brutalist design, with its
mostly shades-of-gray appearance, conservative color usage, and minimal
distractions throughout. This article aims to share some insights into the
philosophy that guides this design, both for the curious reader and for the
new contributor to the open-source project.

The most important principle is that sr.ht is an engineering tool first and
foremost, and when you’re there it’s probably because you’re in engineering
mode. Therefore, it’s important to bring the information you’re there for to the
forefront, and minimize distractions. In practice, this means that the first
thing on any page to grab your attention should be the thing that brought you
there. Consider  [the source file view on git.sr.ht](https://git.sr.ht/~sircmpwn/git.sr.ht/tree/master/gitsrht/service.py) . For
reference, here are similar pages on  [GitHub](https://github.com/torvalds/linux/blob/master/init/main.c)  and
 [Gitlab](https://gitlab.freedesktop.org/libinput/libinput/blob/master/src/evdev.c) .

The vast majority of the git.sr.ht page is dedicated to the source code we’re
reading here, and it’s also where most of the colors are. Your eye is drawn
straight to the content. Any additional information we show on this page is
directly relevant to the content: breadcrumbs to other parts of the tree, file
mode & size, links to other views on this repository. The nav can take you away
from this page, but it’s colored a light grey to avoid being distracting and
each link is another engineering tool - no marketing material or fluff. Contrast
with GitHub: a large, dark, attention grabbing navbar with links to direct you
away from the content and towards marketing pages. If you’re logged out, you get
a giant sign-up box which pushes the content halfway off the page. Colors here
are also distracting: note the large line of colorful avatars that catches your
eye despite almost certainly being unrelated to your purpose on this page.

Colors are used much more conservatively on sourcehut. If you log into
builds.sr.ht and visit the index page, you’re greeted with a large blue “submit
manifest” button, and very little color besides. This is probably why you were
here - so it’s made obvious and colorful so your eyes can quickly find it and
get on with your work. Other pages are similar: the todo.sr.ht tracker page has
a large form with a blue “submit” button for creating a new ticket, email views
on lists.sr.ht have a large blue “reply to thread” button, and
 [man.sr.ht](https://man.sr.ht)  has a large green button enticing new users
towards the tutorials. Red is also used throughout for dangerous actions, like
deleting things.  Each button also is unambiguous and relies on the text within
itself rather than the text nearby: the git.sr.ht repository deletion page uses
“Delete $reponame”, rather than “Continue”.

The last important point in sourcehut’s design is the use of icons, or rather
the lack thereof. Icons are used extremely conservatively on sr.ht. Interactive
icons (things you are expected to click) are never shown without text that
clarifies what happens when you click them. Informational icons usually have a
tooltip which explains their meaning, and are quite rare - only used in cases
where real estate limits the use of text. Assigning an icon to every action or
detail is not necessary and would add more distractions to the screen.

I’m not a particularly skilled UI designer, so keeping it simple like this also
helps to make a reasonably nice UI attainable for an engineer-oriented developer
like me. Adding new pages is generally easy and requires little thought by
applying these basic principles throughout, and the simple design doesn’t take
long to execute on. It’s not perfect, but I like it and I’ve received positive
feedback from my users.
