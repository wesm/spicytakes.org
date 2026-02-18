---
title: "How to write release notes"
date: 2021-05-19
url: https://drewdevault.com/2021/05/19/How-to-write-release-notes.html
slug: How-to-write-release-notes
word_count: 800
---

Release notes are a concept most of us are familiar with. When a new software
release is prepared, the release notes tell you what changed, so you understand
what you can expect and how to prepare for the update. They are also
occasionally used to facilitate conversations:

Many of the people tasked with writing release notes have never found themselves
on that side of the screen before. If that describes you, I would like to offer
some advice on how to nail it. Note that this mostly applies to free and open
source software, which is the only kind of software which is valid.

So, it’s release day, and you’re excited about all of the cool new features
you’ve added in this release. I know the feeling! Your first order of business,
however, is to direct that excitement into the blog or mailing list post
announcing the release, rather than into the release notes. When I read the
release notes, the first thing I need answered is: “what do I need to do when I
upgrade?” You should summarize the breaking changes upfront, and what steps the
user will need to take in order to address them. After this, you may follow up
with a  *short*  list of the flagship improvements which are included in this
release. Keep it short — remember that we’re not advertising the release,
but facilitating the user’s upgrade. This is a clerical document.

That said, you do have a good opportunity to add a  *small*  amount of faffery
after this. Some projects say “$project version $X includes $Y changes from $Z
contributors”. The detailed changelog should follow, including every change
which shipped in the release. This is what users are going to scan to see if
that one bug which has been bothering them was addressed in this version. If you
have  [good git discipline](https://drewdevault.com/2019/02/25/Using-git-with-discipline.html) , you can take advantage of  [git shortlog](https://git-scm.com/docs/git-shortlog)  to
automatically generate a summary of the changes.

Once you’ve prepared this document, where should you put it? In my opinion,
there’s only one appropriate place for it: an annotated git tag. I don’t like
“CHANGELOG” files and I definitely don’t like GitHub releases. If you add “-a”
to your “git tag” command, git will fire up an editor and you can fill in your
changelog just like you write your git commit messages. This associates your
changelog with the git data it describes, and automatically distributes it to
all users of the git repository. Most web services which host git repositories
will display it on their UI as well. It’s also written in plaintext, which
conveniently prevents you from being too extra with your release notes —
no images or videos or such.

I have written a small tool which will make all of this easier for you to do:
“ [semver](https://git.sr.ht/~sircmpwn/dotfiles/tree/master/bin/semver) ”. This
automatically determines the next release number, optionally runs a custom
script to automate any release bookkeeping you need to do (e.g. updating the
version in your Makefile), then generates the git shortlog and plops you into an
editor to flesh out the release notes. I wrote more about this tool in  [How to
fuck up software releases](https://drewdevault.com/2019/10/12/how-to-fuck-up-releases.html) .

I hope this advice helps you improve your release notes! Happy shipping.

P.S. Here’s an example of a changelog which follows this advice:

```
wlroots 0.12.0 includes the following breaking changes:

# New release key

The PGP key used to sign this release has changed to
34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48. A proof of legitimacy signed with the
previous key is available here:

https://github.com/swaywm/wlroots/issues/2462#issuecomment-723578521

# render/gles2: remove gles2_procs global (#2351)

The wlr_gles2_texture_from_* family of functions are no longer public API.

# output: fix blurred hw cursors with fractional scaling (#2107)

For backends: wlr_output_impl.set_cursor now takes a float "scale" instead of an
int32_t.

# Introduce wlr_output_event_commit (#2315)

The wlr_output.events.commit event now has a data argument of type
struct wlr_output_event_commit * instead of struct wlr_output *.

Antonin Décimo (3):
      Fix typos
      Fix incorrect format parameters
      xwayland: free server in error path

Isaac Freund (6):
      xdg-shell: split last-acked and current state
      layer-shell: add for_each_popup
      layer-shell: error on 0 dimension without anchors
      xdg_positioner: remove unused field
      wlr_drag: remove unused point_destroy field
      xwayland: remove unused listener

Roman Gilg (3):
      output-management-v1: add head identifying events
      output-management-v1: send head identifying information
      output-management-v1: send complete head state on enable change

Ryan Walklin (4):
      Implement logind session SetType method to change session type to wayland
      Also set XDG_SESSION_TYPE
      Don't set XDG_SESSION_TYPE unless logind SetType succeeds
      Quieten failure to set login session type

Scott Moreau (2):
      xwm: Set _NET_WM_STATE_FOCUSED property for the focused surface
      foreign toplevel: Fix whitespace error
```

*Note: I borrowed the real wlroots 0.12.0 release notes and trimmed them down
for illustrative purposes. The actual release included a lot more changes and
does not actually follow all of my recommendations.*
