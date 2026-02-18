---
title: "The advantages of an email-driven git workflow"
date: 2018-07-02
url: https://drewdevault.com/2018/07/02/Email-driven-git.html
slug: Email-driven-git
word_count: 1629
---

[git 2.18.0](https://raw.githubusercontent.com/git/git/master/Documentation/RelNotes/2.18.0.txt)  has been released, and with it my first contribution to
git has shipped! My patch was for a git feature which remains disappointingly
obscure:  [git send-email](https://git-scm.com/docs/git-send-email) . I want to
introduce my readers to this feature and speak to the benefits of using an
email-driven git workflow - the workflow git was originally designed for.

Email isn’t as sexy as GitHub (and its imitators), but it has several
advantages over the latter. Email is standardized, federated, well-understood,
and venerable. A very large body of email-related software exists and is equally
reliable and well-understood. You can interact with email using only open source
software and customize your workflow at every level of the stack - filtering,
organizing, forwarding, replying, and so on; in any manner you choose.

Git has several built-in tools for leveraging email. The first one of note is
 [format-patch](https://git-scm.com/docs/git-format-patch) . This can take a git
commit (or series of commits) and format them as plaintext emails with embedded
diffs. Here’s a small example of its output:

```
From 8f5045c871c3060ff5f5f99ce1ada09f4b4cd105 Mon Sep 17 00:00:00 2001
From: Drew DeVault <sir@cmpwn.com>
Date: Wed, 2 May 2018 08:59:27 -0400
Subject: [PATCH] Silently ignore touch_{motion,up} for unknown ids

---
 types/wlr_seat.c | 2 --
 1 file changed, 2 deletions(-)

diff --git a/types/wlr_seat.c b/types/wlr_seat.c
index f77a492d..975746db 100644
--- a/types/wlr_seat.c
+++ b/types/wlr_seat.c
@@ -1113,7 +1113,6 @@ void wlr_seat_touch_notify_up(struct wlr_seat *seat, uint32_t time,
 	struct wlr_seat_touch_grab *grab = seat->touch_state.grab;
 	struct wlr_touch_point *point = wlr_seat_touch_get_point(seat, touch_id);
 	if (!point) {
-		wlr_log(L_ERROR, "got touch up for unknown touch point");
 		return;
 	}
 
@@ -1128,7 +1127,6 @@ void wlr_seat_touch_notify_motion(struct wlr_seat *seat, uint32_t time,
 	struct wlr_seat_touch_grab *grab = seat->touch_state.grab;
 	struct wlr_touch_point *point = wlr_seat_touch_get_point(seat, touch_id);
 	if (!point) {
-		wlr_log(L_ERROR, "got touch motion for unknown touch point");
 		return;
 	}
 
-- 
2.18.0
```

git format-patch is at the bottom of git’s stack of outgoing email features. You
can send the emails it generates manually, but usually you’ll use git send-email
instead. It logs into the SMTP server of your choice and sends the email for
you, after running git format-patch for you and giving you an opportunity to
make any edits you like. Given that most popular email clients these days are
awful and can’t handle basic tasks like “sending email” properly, I strongly
recommend this tool over attempting to send format-patch’s output yourself.

*
        I put a notch in my keyboard for each person who ignores my advice,
        struggles through sending emails manually, and eventually comes around
        to letting git send-email do it for them.
    *

I recommend a few settings to apply to git send-email to make your workflow a
bit easier. One is  `git config --global sendemail.verify off` , which turns off
a sometimes-annoying and always-confusing validation step which checks for
features only supported by newer SMTP servers - newer, in this case, meaning
more recent than November of 1995. I started a thread on the git mailing list
this week to discuss changing this option to off by default.

You can also set the default recipient for a given repository by using a local
git config:  `git config sendemail.to admin@example.org` . This lets you skip a
step if you send your patches to a consistent destination for that project, like
a mailing list. I also recommend  `git config --global sendemail.annotate yes` ,
which will always open the emails in your editor to allow you to make changes
(you can get this with  `--annotate`  if you don’t want it every time).

The main edit you’ll want to make when annotating is to provide what some call
“timely commentary” on your patch. Immediately following the  `---`  after your
commit message, you can add a summary of your changes which can be seen by the
recipient, but doesn’t appear in the final commit log. This is a useful place to
talk about anything useful regarding the testing, review, or integration of your
changes. You may also want to edit the  `[PATCH]`  text in the subject line to
something like  `[PATCH v2]`  - this can also be done with the  `-v`  flag as well.
I also like to add additional To’s, Cc’s, etc at this time.

Git also provides tools for the recipient of your messages. One such tool is
 [git am](https://git-scm.com/docs/git-am) , which accepts an email prepared with
format-patch and integrates it into their repository. Several flags are provided
to assist with common integration activities, like signing off on the commit or
attempting a 3-way merge. The difficult part can be getting the email to git am
in the first place. If you simply use the GMail web UI, this can be difficult. I
use  [mutt](http://www.mutt.org/) , a TUI email client, to manage incoming
patches. This is useful for being able to compose replies with vim rather than
fighting some other mail client to write emails the way I want, but more
importantly it has the  `|`  key, which prompts you for a command to pipe the
email into. Other tools like  [OfflineIMAP](http://www.offlineimap.org/)  are also
useful here.

On the subject of composing replies, reviewing patches is quite easy with the
email approach as well. Many bad, yet sadly popular email clients have
popularized the idea that the sender’s message is immutable, encouraging you to
 [top post](https://en.wikipedia.org/wiki/Posting_style#Top-posting)  and leave an endlessly growing chain of replies
underneath your message. A secret these email clients have kept from you is that
you are, in fact, permitted by the mail RFCs to edit the sender’s message as you
please when replying - a style called  [bottom posting](https://en.wikipedia.org/wiki/Posting_style#Bottom-posting) . I
strongly encourage you to get comfortable doing this in general, but it’s
essential when reviewing patches received over email.

In this manner, you can dissect the patch and respond to specific parts of it
requesting changes or clarifications. It’s just email - you can reply, forward
the message, Cc interested parties, start several chains of discussion, and so
on. I recently sent the following feedback on a patch I received:

```
Date: Mon, 11 Jun 2018 14:19:22 -0400
From: Drew DeVault <sir@cmpwn.com>
To: Gregory Mullen <omitted>
Subject: Re: [PATCH 2/3 todo] Filter private events from events feed

On 2018-06-11  9:14 AM, Gregory Mullen wrote:
> diff --git a/todosrht/alembic/versions/cb9732f3364c_clear_defaults_from_tickets_to_support_.py b/todosrht/alembic/versions/cb9732f3364c_clear_defaults_from_tickets_to_support_.py
> -%<-
> +class FlagType(types.TypeDecorator):

I think you can safely import the srht FlagType here without implicating
the entire sr.ht database support code

> diff --git a/todosrht/blueprints/html.py b/todosrht/blueprints/html.py
> -%<-
> +def collect_events(target, count):
> +    events = []
> +    for e in EventNotification.query.filter(EventNotification.user_id == target.id).order_by(EventNotification.created.desc()):

80 cols

I suspect this 'collect_events' function can be done entirely in SQL
without having to process permissions in Python and do several SQL
round-trips

>  @html.route("/~<username>")
>  def user_GET(username):
> -    print(username)

Whoops! Nice catch.

>      user = User.query.filter(User.username == username.lower()).first()
>      if not user:
>          abort(404)
>      trackers, _ = get_tracker(username, None)
>      # TODO: only show public events (or events the current user can see)

Can remove the comment
```

Obviously this isn’t the whole patch we’re seeing - I’ve edited it down to just
the parts I want to talk about. I also chose to leave the file names in to aid
in navigating my feedback, with casual  `-%<-`  symbols indicating where I had
trimmed out parts of the patch. This approach is common and effective.

The main disadvantage of email driven development is that some people are more
comfortable working with email in clients which are not well-suited to this kind
of work. Popular email clients have caused terrible ideas like HTML email to
proliferate, not only enabling spam, privacy leaks, and security
vulnerabilities, but also making it more difficult for people to write emails
that can be understood by git or tolerated by advanced email users.

I don’t think that the solution to these problems is to leave these powerful
tools hanging in the wind and move to less powerful models like GitHub’s pull
requests. This is why on my own platform,  [sr.ht](https://sr.ht) , I chose to
embrace git’s email-driven approach, and extend it with new tools that make it
easier to participate without directly using email. For those like me, I still
want the email to be there so you can dig my heels in and do it old-school, but
I appreciate that it’s not for everyone.

I started working on the sr.ht mailing list service a couple of weeks ago, which
is where these goals will be realized with new email-driven code review tools.
My friend  [Simon](https://emersion.fr)  has been helping out with a Python module
named  [emailthreads](https://git.sr.ht/~emersion/python-emailthreads/)  which can
be used to parse email discussions - with a surprising degree of accuracy,
considering the flexibility of email. Once I get these tools into a usable
state, we’ll likely see sr.ht registrations finally opened to the general public
(interested in trying it earlier?  [Email me](mailto:sir@cmpwn.com) ). Of course,
it’s all  [open source](https://git.sr.ht/~sircmpwn/?search=sr.ht) , so you can
follow along and try it on your own infrastructure if you like.

Using email for git scales extremely well. The canonical project, of course, is
the Linux kernel. A change is made to the Linux kernel an average of 7 times per
hour, constantly. It is maintained by dozens of veritable clans of software
engineers hacking on dozens of modules, and email allows these changes to
efficiently flow code throughout the system. Without email, Linux’s maintenance
model would be impossible. It’s worth noting that git was designed for
maintaining Linux, of course.

With the right setup, it’s well suited to small projects as well. Sending a
patch along for review is a single git command. It lands directly in the
maintainer’s inbox and can be integrated with a handful of keystrokes. All of
this works without any centralization or proprietary software involved. We
should embrace this!

Related articles sent in by readers:

[Mailing lists vs Github](https://begriffs.com/posts/2018-06-05-mailing-list-vs-github.html) 
by Joe Nelson

[You’re using git wrong](https://web.archive.org/web/20180522180815/https://dpc.pw/blog/2017/08/youre-using-git-wrong/)  by
Dawid Ciężarkiewicz
