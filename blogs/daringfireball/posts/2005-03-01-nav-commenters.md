---
title: "Kill ‘nav-commenters.gif’"
date: 2005-03-01
url: https://daringfireball.net/2005/03/nav-commenters
slug: nav-commenters
word_count: 995
---


Movable Type 3.0 and later contain a feature with a curious
implementation — a tiny little thing that’s been irritating me ([and
others](http://www.benhammersley.com/weblog/2004/09/03/navcommentersgif_must_die.html)) ever since.


What happens is that each time you rebuild any of your weblogs, MT
creates a file named “nav-commenters.gif” at the root level of the
weblog. E.g., if your weblog is located at `http://example.com/`, MT
will create this file at `http://example.com/nav-commenters.gif`.


It’s a tiny little file — 22 × 15 pixels and a mere 91 bytes. It
looks like this:


MT uses this file as an icon to indicate which comments were written
by users who authenticated via Six Apart’s [TypeKey](http://www.sixapart.com/typekey/) service.
If you see this icon next to the name of a commenter, you can click
it to see that user’s TypeKey profile.


What’s so curious/irritating about it is that (a) the file is
created at the root level of every single weblog in your MT
installation; (b) it’s created whether you use TypeKey or not, and
whether you *even display comments or not*; and (c) if you delete it
by hand, MT will keep re-creating it.


The presence of “nav-commenters.gif” is in fact a half-decent way to
tell whether a given site is powered by Movable Type 3.0 or later.
E.g., each of the weblogs that constitute the different sections of
the new Six Apart web site has its own copy:

- [http://www.sixapart.com/nav-commenters.gif](http://www.sixapart.com/nav-commenters.gif)
- [http://www.sixapart.com/movabletype/nav-commenters.gif](http://www.sixapart.com/movabletype/nav-commenters.gif)
- [http://www.sixapart.com/typekey/nav-commenters.gif](http://www.sixapart.com/typekey/nav-commenters.gif)
- [http://www.sixapart.com/typepad/nav-commenters.gif](http://www.sixapart.com/typepad/nav-commenters.gif)


(But, curiously, not [http://www.sixapart.com/livejournal/nav-commenters.gif](http://www.sixapart.com/livejournal/nav-commenters.gif).)


MT litters your web space with no other such images. Just
“nav-commenters.gif”. In the grand scheme of things, this is,
obviously, not a big deal. But to me, it was maddening, like a
sliver of popcorn caught in my teeth.


So, I’ve fixed it with a plug-in.


## Update: 26 April 2005


Movable Type 3.16 obviates the need for this plug-in, supplying its
own built-in means of suppressing the creation of the
“nav-commenters.gif” file. If you’re already using my plug-in, you
can remove it. To use MT’s new built-in suppression, add the following
line to your “mt.cfg” file:


```
PublishCommenterIcon 0

```


## Download and Installation


Download: [Kill-nav-commenters-gif.zip](https://daringfireball.net/projects/downloads/Kill-nav-commenters-gif.zip) (2 KB) — 28 Feb 2005

1. Copy the “Kill-nav-commenters-gif.pl” file into your Movable
Type “plugins” folder. The “plugins” folder should be in
the same directory as “mt.cgi”; if the “plugins” directory
doesn’t already exist, use your FTP program to create it. Your
installation should look like this:
`(mt home)/plugins/Kill-nav-commenters-gif.pl
`
2. Rebuild each of your weblogs.


That’s it. Uninstallation is just as easy: remove
“Kill-nav-commenters-gif.pl” from your “plugins” folder, then
rebuild.


## How It Works


Part of what’s so maddening about MT’s “let’s keep generating copies
of ‘nav-commenters.gif’” behavior is that this file *already
exists*, in the static images directory of the Movable Type
application itself. That’s the folder where you can find all the
images that constitute the MT web app user interface.
“nav-commenters.gif” is in fact one of the icons in the MT web app
interface:


Hence the name of the file. The icon for the entries button is
“nav-entries.gif”; for categories, “nav-categories.gif”, etc. So my
guess is that when Six Apart was developing the TypeKey integration
for MT 3.0, they decided to re-use the “nav-commenters.gif” icon
rather than create a new one. So far, so good.


The problem is that Movable Type has no built-in means of linking to
an item in your static “images” folder, which is where the existing
copy of “nav-commenters.gif” lives. This folder was meant to contain
images used by the MT web application, not for images referenced by
the weblogs it publishes. In fact, the default templates for MT
don’t use any images; their designs consist entirely of XHTML and
CSS. There is no default “images” folder for the weblogs published
by Movable Type.


Hence the decision to recreate a copy of this folder in the root
public folder of each and every weblog. This way, MT can always
generate a link to “nav-commenters.gif” using:


```
<img src="/nav-commenters.gif" ...

```


Kill-nav-commenters-gif.pl patches two of MT’s built-in routines.
First, it patches `MT::rebuild`, which is the routine that generates
the copies of nav-commenters.gif. Technically, this plug-in doesn’t
suppress MT’s creation/re-creation of “nav-commenters.gif”, but
rather, each time MT creates it, the plug-in deletes it. This way
the plug-in doesn’t need to *replace* the built-in MT routine, but
rather just supplement it.


Second, it redefines the `<$MTCommentAuthorIdentity$>` template tag.
(This tag is used in MT 3.0’s default templates, but as far as I can
tell [it isn’t documented in the MT user manual](http://www.sixapart.com/movabletype/docs/mtmanual_tags.html#comments).) The
handler for this tag is where MT makes the assumption that
“nav-commenters.gif” is located at the root level of every weblog.


Again, instead of re-implementing MT’s internal handler, we call the
original, then look in the output for an `<img>` tag whose `src`
attribute contains “/nav-commenters.gif”; if we find it, we
substitute a reference to the copy of “nav-commenters.gif” in your
static images folder. Building a reference to this folder is the
ever-so-vaguely tricky part.


## Plug-Ins vs. Patching MT’s Source


Ever since MT 1.x, I’ve been wary of any advice that instructs one
to modify MT’s source code. Once you start down that path, you end
up needing to re-apply all such patches *every* time you upgrade
Movable Type. Using plug-ins is a much cleaner way to hack MT’s
internals. This way, instead of modifying MT’s source code, you’re
simply modifying MT’s behavior. The benefits to patching via
plug-ins rather than directly modifying MT’s source are thus:

- You should be able to upgrade to future version of MT as usual,
by simply replacing the old version of MT’s source with the new
version. There’s no need to re-apply your patches with each
revision.
- If you want to uninstall the patch, you simply remove the plug-in.


## Thanks


My thanks to [Brad Choate](http://bradchoate.com/), [Erik Barzeski](http://nslog.com/), and [Ben Hammersley](http://www.benhammersley.com/weblog/) for testing this plug-in (and to Choate, as usual, for suggestions that improved the code itself.)



| **Previous:** | [FireWire Hysteria](https://daringfireball.net/2005/02/firewire_hysteria) |
| **Next:** | [Nerve Touching](https://daringfireball.net/2005/03/nerve_touching) |


PreviousNext