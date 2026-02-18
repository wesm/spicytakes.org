---
title: "Spotlight on Spotlight"
date: 2004-07-12
url: https://daringfireball.net/2004/07/spotlight_on_spotlight
slug: spotlight_on_spotlight
word_count: 1106
---


It’s always been a mystery to me why the HFS+ (a.k.a. Mac OS
Extended) file system is so often disrespected.


The first wave of disrespect was when Mac OS X 10.0 shipped, with
support for both UFS and HFS+ disk formats. Despite the fact that
HFS+ was both the default and [strongly recommended by Apple](http://docs.info.apple.com/article.html?artnum=25316),
numerous Unix nerds took it upon themselves to format their startup
volumes using UFS. The guys who did this were the sort of people who
wanted to believe that Mac OS X was more like “Unix with a Mac-like
appearance” than what it really is — the Mac OS with Unix-like
underpinnings.


The reasons cited for using UFS typically included gems such as:

- *I prefer a case-sensitive file system.*
- *I hate resource forks, and they’re going away, anyway.*
- *I hate file type and creator metadata. And they’re going away,
anyway.*
- *HFS-specific features aren’t compatible with command-line tools.*


(The second and third reasons are often conflated by misinformed
individuals who believe that type/creator metadata is stored *in*
the resource fork; it’s not. Just like any other metadata — such as
the filename and the creation/modification dates — type/creator
metadata is stored in the file system, not in the file itself.)


The gist of it boiled down to *I’m a Unix tough guy; I have no need
for that deprecated Mac OS baby stuff.* For typical desktop use,
there were never any actual technical reasons for using UFS in lieu
of HFS+; it just *sounded* like a nerdy thing to do.


Of course, every person I’ve encountered who tried this eventually
repented and reformatted their drive as HFS+. The truth is that HFS+
is — unsurprisingly — much better-suited to Mac OS X than UFS.


The next wave of HFS+ disrespect started two years ago when Apple
hired [Dominic Giampaolo](http://www.nobius.org/~dbg/), renowned file system design expert
and creator of the highly-regarded, metadata-rich Be File System.
*Ah-hah*, exclaimed the peanut gallery, *Apple hired Dominic
Giampaolo to write a brand-new file system to replace HFS+!*


Flash-forward to last week’s WWDC announcements, where Apple
announced that [Mac OS X 10.4 (Tiger) will include an updated suite
of command-line tools](http://www.apple.com/macosx/tiger/unix.html) (e.g. `cp` and `tar`) that fully support
HFS+ resource forks and metadata.


The only negative thing that can be said about this is that it’s
about fucking time. Updating the tools to support HFS features is a
much better solution than trying to ram the less-featured UFS down
everyone’s throat as a sop to the limitations of 30-year-old
command-line tools.


In short, 10.4 is going to offer *more* support for HFS+ features,
not less.


And so what then has Giampaolo been working on? One answer, we now
know, is that he’s been adding metadata features *on top* of HFS+.
Specifically, Spotlight — which is, in the words of one WWDC
attendee, Giampaolo’s “baby”.


“Spotlight” is much more than just the visible UI shown during
Jobs’s keynote: the vibrant blue search field in the top-right
corner of the screen, and accompanying search results window. That’s
[Spotlight, the user-visible keynote-demo-able front-end](http://www.apple.com/macosx/tiger/spotlight.html).


Under-the-hood, however, [Spotlight is also a set of APIs](http://www.apple.com/macosx/tiger/searchtechnology.html)
accessible by third-party developers. It’s an entirely new metadata
database — not replacing the existing HFS+ file system, but instead
built on top of it.


Via email, the aforementioned source who attended the
Spotlight session at WWDC sent me the following report.


> Spotlight is completely, relentlessly focused on files
> and files’ metadata. Files are the only object returned
> to Spotlight queries. Two aspects of Jobs’ keynote were
> thus misleading: 
> The “spotlight” effect on System Preferences was wholly
> unrelated to Spotlight.
> Spotlight’s ability to show results from Apple Mail archives on
> Jobs’ machine was tantamount to a sham. Believe it or not, Tiger
> Mail has switched to an “exploded” [Maildir](http://www.qmail.org/qmail-manual-html/man5/maildir.html)-like storage
> format with a single message per file.


One implication of Spotlight’s file-centricity is that its ability
to search “email” might not apply to clients other than Apple Mail
— it’s the fact that the new Tiger version of Mail stores each
message as a separate file that allows Spotlight to effectively
return individual mail messages as search results. No other major
mail client uses a one-message-per-file storage format.


[**Update:** The current version of Apple Mail — included with Mac
OS X 10.3.x — already uses a one-message-per-file mail storage
format for IMAP accounts (including .Mac accounts). For POP
accounts, however, it uses “mbox” files. Beginning with 10.4, it
will apparently use a one-message-per-file storage format for all
mailboxes. Also, [GyazMail](http://gyazsquare.com/gyazmail/) already uses a one-message-per-file
mailbox storage format.]


> Spotlight’s full-text search is outsourced to [SearchKit](http://developer.apple.com/documentation/UserExperience/Reference/SearchKit/), which will be considerably faster in Tiger (“3×
> indexing, 20× incremental search” over Panther). So,
> Spotlight has three places to look for information about
> files: its own hand-tuned substring-matching metadata store
> (built by Giampaolo, not part of Core Data or anything else),
> Carbon’s HFS+ catalog calls (so Spotlight *will* respond to
> searches for type and creator), and SearchKit’s full-text
> index.
> Both metadata collection and full-text indexing depend on
> cooperating per-file-format Importers, either written by
> Apple or by third parties. Like Google, no matter how much
> text an Importer provides, Spotlight only cares about the
> first 100K of raw text.
> Importers are fired on every file the moment it is created,
> saved, changed, or moved, including when files are made
> available through a newly mounted drive. Performance is
> said to be excellent in every case except network-mounted
> home directories, which are bedeviling on several levels
> and on which they’re still working.


It’s through the default set of Importers that Spotlight is able to
index and search format-specific metadata, such as the ID3 tags in
MP3 files.


What’s cool about this architecture is that Spotlight’s indexes will
thus stay up-to-date automatically. All you need to do is save,
move, or copy a file, and Spotlight’s metadata and content indexes
will note the changes on-the-fly. Compare and contrast to the
full-content file searching previously provided via Sherlock, which
required periodic monolithic re-indexing of the content of your
drives.


> At the API level, Spotlight responds to a range of C-like,
> Google-like query modifiers: `==`, `!`, `-`, `<`, `>`, `<=`, `>=`,
> and both leading/trailing `*`. Queries can toggle
> case-insensitivity, and also diacritical insensitivity. High-level
> Cocoa APIs and comfortably low-level Carbon/CoreServices APIs are
> available in addition to the Finder UI.
> Spotlight is going to kick a great deal of ass.



| **Previous:** | [Status](https://daringfireball.net/2004/07/status) |
| **Next:** | [Membership Keys](https://daringfireball.net/2004/07/membership_keys) |


PreviousNext