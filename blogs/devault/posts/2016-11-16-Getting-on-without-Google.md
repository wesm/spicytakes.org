---
title: "Getting on without Google"
date: 2016-11-16
url: https://drewdevault.com/2016/11/16/Getting-on-without-Google.html
slug: Getting-on-without-Google
word_count: 1056
---

I used Google for a long time, but have waned myself off of it over the past
few years, and I finally deleted my account a little over a month ago. I feel so
much better about my privacy now that I’ve removed Google from the equation, and
self hosting my things affords me a lot of flexibility and useful customizations.

## mail.cmpwn.com

This one was the most difficult and time consuming to set up, but it was  *very* 
worth it. I’ve intended for a while to make a new mail server software suite
that’s less terrible to set up, so hopefully that situation will improve in the
future. I want to flesh out  [aerc](https://github.com/SirCmpwn/aerc)  some more
first. A personal mail server was one of the earliest things I set up in my
post-Google life - I’ve operated it for about two years now.

* Postfix to handle incoming and outgoing mail
* Dovecot to handle mail delivery, filtering, and IMAP
* Postfixadmin to provide a nice interface for managing accounts
* mutt to read and compose my emails on the desktop
* K9 to read and compose my emails on Android
* Roundcube for when it’s occasionally necessary to read an HTML email

With my mail server provides a lot of side benefits, too. For one, all of my
email-sending software now uses it. Once Mandrill went kaput, it was easy to
switch everything over to it. I can be sending and receiving email from a new
domain in less than 5 minutes now. Using sieve scripts for filtering emails is
also a lot more flexible than what Google offered - I now have filtering set up
to organize several mailing lists, alerts and notifications sent by my software
and servers, RSS feeds, and more.

My strategy for defeating spam is to use a combination of the spamhaus
blocklist, greylisting, and blacklisting with sieve. I see about 3-5 spam emails
per week on average with this setup. To ensure my own emails get delivered, I’ve
set up SPF and DKIM, reverse DNS, and appealed to have my IP address removed
from blocklists. A great tool in figuring all this out has been
 [mail-tester.com](http://mail-tester.com) .

## YouTube

For YouTube, I “subscribe” to channels by adding their RSS feeds to
 [rss2email](http://www.allthingsrss.com/rss2email/) , combined with sieve scripts
that filter them into a specific folder. I then have a keybinding in mutt that,
when pressed, pulls the YouTube URL out of an email and feeds it to mpv, a
desktop video player. It’s so much easier to access YouTube this way than
through the web browser - no ads, familiar keybindings, remote control support,
and a no-nonsense feed of your videos.

## Music

Instead of Google Music, Spotify, or anything else, I run an internet radio
with my friends. We all keep our music collections (mostly lossless) on NFS
servers, and we mounted these servers on a streaming server that shuffles the
entire thing and keeps a searchable database of music. We have an API that I
pull from to integrate desktop keybindings and a status line on my taskbar, and
an IRC bot for searching the database and requesting songs. I can also stream to
my phone with VLC, as well as use scripts to maintain an offline archive of my
favorite songs. This setup is  *way*  nicer than any commercial service I’ve used
in the past. We’ll be open sourcing version 2 to provide a turnkey solution for
this type of self-hosted music service.

## Web search

[DuckDuckGo](https://duckduckgo.com/) . Even if you think the search results
aren’t up to snuff (you get used to just being a bit more specific anyway), the
bangs feature is absolutely indispensable. I recently patched Chromium for
Android to support DuckDuckGo as a search engine as well:
 [here’s the patch](/l.sr.ht/h4bZ.patch) .

## File hosting

Instead of using Google Drive, I’m using a number of different solutions
depending on what’s most convenient at the time. I operate
 [sr.ht](https://sr.ht)  for me and my friends, which allows me to just have a
place to drop a file and get a link to share. I have scripts and keybindings set
up to make uploading files here second nature, as well as an Android app someone
wrote. I also keep a 128G flash drive on my keychain now that comes in handy all
the time, and a big-ass file server on OVH that I keep mounted with NFS or sshfs
depending on the scenario, and sometimes I just stash files on a random server
with rsync. sr.ht is  [open source](https://gogs.sr.ht/SirCmpwn/sr.ht) , by the
way.

## CyanogenMod

On Android, I use CyanogenMod without Google Play Services, and I use F-Droid to
get apps. When I used Google Now, I found that I most often just asked it for
reminders, which I now do via an open source app called Notable Plus. I also
have open source apps for reading HN, downloading torrents, blocking ads,
connecting to IRC, two factor authentication, YouTube, password management,
Twitter, and more.

## Notably missing: Docs

Hopefully the new LibreOffice thing will do the trick once it’s ready. I’m
looking forward to that.

## Things I self host that Google doesn’t offer

I use ZNC to operate an IRC bouncer, which is great because I use IRC  *a lot* .
It keeps logs for me, keeps me always connected, and gives me a number of nice
features to work with. I also host a number of simple websites related to IRC to
do things like channel stats and rules.

To all sr.ht users I offer access to  [gogs.sr.ht](https://gogs.sr.ht) , which I
personally use to host many private repositories as well as a number of small
projects, and as a kind of staging area for repositories that aren’t quite ready
for GitHub yet.

For passwords, I use a tool called  [pass](https://www.passwordstore.org/) , which
encrypts passwords with my PGP key and stores them in a git repository I keep on
gogs.sr.ht, with desktop keybindings to make grabbing them convenient.

## Help me do this!

Well, that covers most of my major self hosted services. If you’re interested in
more detail about how any of this works so you might set something up yourself,
feel free to reach out to me by  [email](mailto:sir@cmpwn.com) ,
 [Mastodon](https://cmpwn.com/@sir) , or IRC (SirCmpwn on any network). I’d
be happy to help!
