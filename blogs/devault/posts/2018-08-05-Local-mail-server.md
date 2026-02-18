---
title: "Setting up a local dev mail server"
date: 2018-08-05
url: https://drewdevault.com/2018/08/05/Local-mail-server.html
slug: Local-mail-server
word_count: 733
---

As part of my work on  [lists.sr.ht](https://meta.sr.ht) , it was necessary for
me to configure a self-contained mail system on localhost that I could test
with. I hope that others will go through a similar process in the future when
they set up  [the code](https://git.sr.ht/~sircmpwn/lists.sr.ht)  for hacking on
locally or when working on other email related software, so here’s a guide on
how you can set it up.

There are lots of things you can set up on a mail server, like virtual mail
accounts backed by a relational database, IMAP access, spam filtering, and so
on. We’re not going to do any of that in this article - we’re just interested in
something we can test our email code with. To start, install your distribution
of  `postfix`  and pop open that  `/etc/postfix/main.cf`  file.

Let’s quickly touch on the less interesting config keys to change. If you want
the details about how these work, consult the postfix manual.

* *myhostname*  should be your local hostname
* *mydomain*  should also be your local hostname
* *mydestination*  should be  `$myhostname, localhost.$mydomain, localhost`
* *mynetworks*  should be  `127.0.0.0/8`
* *home_mailbox*  should be  `Maildir/`

Also ensure your hostname is set up right in  `/etc/hosts` , something like this:

```
127.0.0.1 homura.localdomain homura
```

Okay, those are the easy ones. That just makes it so that your mail server
oversees mail delivery for the  `127.0.0.0/8`  network (localhost) and delivers
mail to local Unix user mailboxes. It will store incoming email in each user’s
home directory at  `~/Maildir` , and will deliver email to other Unix users. Let’s
set up an email client for reading these emails with. Here’s my development
 [mutt](http://mutt.org)  config:

```
set edit_headers=yes
set realname="Drew DeVault"
set from="sircmpwn@homura"
set editor=vim
set spoolfile="~/Maildir/"
set folder="~/Maildir/"
set timeout=5
color index blue default ~P
```

Make any necessary edits. If you use mutt to read your normal mail, I suggest
also setting up an alias which runs  `mutt -C path/to/dev/config` . Now, you
should be able to send an email to yourself or other Unix accounts with
mutt 1 . Hooray!

To accept email over SMTP, mozy on over to  `/etc/postfix/master.cf`  and
uncomment the submission service. You’re looking for something like this:

```
127.0.0.1:submission inet n       -       n       -       -       smtpd
#  -o syslog_name=postfix/submission
#  -o smtpd_tls_security_level=encrypt
#  -o smtpd_sasl_auth_enable=yes
#  -o smtpd_tls_auth_only=yes
#  -o smtpd_reject_unlisted_recipient=no
#  -o smtpd_client_restrictions=$mua_client_restrictions
#  -o smtpd_helo_restrictions=$mua_helo_restrictions
#  -o smtpd_sender_restrictions=$mua_sender_restrictions
#  -o smtpd_recipient_restrictions=
#  -o smtpd_relay_restrictions=
#  -o milter_macro_daemon_name=ORIGINATING
```

This will permit delivery via localhost on the submission port (587) to anyone
whose hostname is in  `$mydestination` . A good old  `postfix reload`  later and you
should be able to send yourself an email with SMTP:

```
$ telnet 127.0.0.1 587
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
220 homura ESMTP Postfix
EHLO example.org
250-homura
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-ENHANCEDSTATUSCODES
250-8BITMIME
250-DSN
250 SMTPUTF8
MAIL FROM:<sircmpwn@homura>
250 2.1.0 Ok
RCPT TO:<sircmpwn@homura> 
250 2.1.5 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
From: Drew DeVault <sircmpwn@homura>
To: Drew DeVault <sircmpwn@homura>
Subject: Hello world

Hey there 
.
250 2.0.0 Ok: queued as 8267416366B
QUIT
221 2.0.0 Bye
Connection closed by foreign host.
```

Pull up mutt again to read this. Any software which will be sending out mail and
speaks SMTP (for example, sr.ht) can be configured now. Last step is to set up
LTMP delivery to lists.sr.ht or any other software you want to process incoming
emails. I want most mail to deliver normally - I only want LTMP configured for
my lists.sr.ht test domain. I’ll set up some transport maps for this purpose. In
 `main.cf` :

```
local_transport = local:$myhostname
transport_maps = lmdb:/etc/postfix/transport
```

Then I’ll edit  `/etc/postfix/transport`  and add these lines:

```
lists.homura lmtp:unix:/tmp/lists.sr.ht-lmtp.sock
homura local:homura
```

This will deliver mail normally to  `$user@homura`  (my hostname), but will
forward mail sent to  `$user@lists.homura`  to the Unix socket where the
 [lists.sr.ht LMTP
server](https://git.sr.ht/~sircmpwn/lists.sr.ht/tree/master/listssrht-lmtp)  lives.

Add the subdomain to  `/etc/hosts` :

```
127.0.0.1 lists.homura.localdomain lists.homura
```

Run  `postmap /etc/postfix/transport`  and  `postfix reload`  and you’re good to go.
If you have the lists.sr.ht daemon working, send some emails to
 `~someone/example-list@lists.$hostname`  and you should see them get picked up.

1. Mutt crash course: run `mutt`, press `m` to compose a new email, enter the recipient (`$USER@$HOSTNAME` to send to yourself) and the subject, then compose your email, exit the editor, and press `y` to send. A few moments later the email should arrive. ↩︎
