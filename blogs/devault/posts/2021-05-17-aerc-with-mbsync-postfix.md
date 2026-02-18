---
title: "aerc, mbsync, and postfix for maximum comfy offline email"
date: 2021-05-17
url: https://drewdevault.com/2021/05/17/aerc-with-mbsync-postfix.html
slug: aerc-with-mbsync-postfix
word_count: 562
---

I am the original author of the  [aerc mail client](https://aerc-mail.org) , though my official
relationship with it today is marginal at best. I think that, with hindsight,
I’ve come to understand that the “always online” approach of aerc’s IMAP
implementation is less than ideal. The next email client (which will exist at
some point!) will improve on this design, but, since it’s still my favorite
email client despite these flaws, they will have to be worked around.

To this end, I have updated my personal aerc setup to take advantage of its
 [Maildir](https://en.wikipedia.org/wiki/Maildir)  support instead of having it use IMAP directly, then delegate IMAP
to  [mbsync](https://isync.sourceforge.io) . This brings a much-needed level of robustness to the setup, as
my Maildirs are available offline or on a flaky connection, and postfix will
handle queueing and redelivery of outgoing emails in similar conditions. 1 
This allows me to read and reply to email entirely offline, and have things sync
up automatically when a connection becomes available.

The mbsync configuration format is kind of weird, but it is pretty flexible. My
config file ended up looking like this:

```
IMAPAccount migadu
Host imap.migadu.com
User sir@cmpwn.com
Pass [...]
SSLType IMAPS

MaildirStore local
Path ~/mail/
INBOX ~/mail/INBOX
SubFolders Verbatim

IMAPStore migadu
Account migadu

Channel primary
Far :migadu:
Near :local:
Patterns INBOX Archive Sent Junk
Expunge Both
```

The password can be configured to run an external command if you prefer to
integrate this with your keyring or password manager. I updated my aerc
 `accounts.conf`  as well, which was straightforward:

```
[Drew]
source = maildir://~/mail
outgoing = /usr/sbin/sendmail
from = Drew DeVault <sir@cmpwn.com>
copy-to = Sent
```

Running  `mbsync primary`  at this point is enough to fetch these mailboxes from
IMAP and populate the local Maildirs, which can then be read with aerc. I set up
a simple cronjob to run this every minute to keep it up to date:

```
* * * * * chronic mbsync primary
```

chronic is a small utility from  [moreutils](https://joeyh.name/code/moreutils/)  which converts reasonably behaved
programs that return a nonzero exit status into the back-asswards behavior cron
expects, which is that printing text to stdout means an error occurred and any
status code, successful or not, is disregarded. You might want to tweak this
further, perhaps by just directing all output into /dev/null instead, if you
don’t want failed syncs to fill up your Unix mail spool.

mbsync is bidirectional (it is recommended to leave  `Expunge both`  out of your
config until you’ve tested the setup), so deleting or archiving emails in aerc
will mirror the changes in IMAP as well.

Postfix is a lot more annoying to configure. You should assume that what I did
here isn’t going to work for you without additional changes and troubleshooting.
I started with an  `/etc/postfix/sasl_passwd`  file like this:

```
[smtp.migadu.com]:465   sir@cmpwn.com:password
```

The usual  `postmap /etc/postfix/sasl_passwd`  applies here to create or update
the database file. Then I moved on to  `main.cf` :

```
# Allows localhost to relay mail
mynetworks = 127.0.0.0/8

# SMTP server to relay mail through
relayhost = [smtp.migadu.com]:465

# Auth options for SMTP relay
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = lmdb:/etc/postfix/sasl_passwd

# ¯\_(ツ)_/¯
smtp_tls_security_level = encrypt
smtp_tls_wrappermode = yes
smtp_use_tls = yes
smtp_sasl_security_options = 
```

Good luck!

**Updated 2021-05-25** : isync is not a fork of mbsync.

1. Postfix is probably overkill for this, but hey, it’s what I know. ↩︎
