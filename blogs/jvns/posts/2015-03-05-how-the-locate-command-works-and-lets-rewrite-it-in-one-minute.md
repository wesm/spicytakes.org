---
title: "How the locate command works (and let's write a faster version in one minute!)"
date: 2015-03-05
url: https://jvns.ca/blog/2015/03/05/how-the-locate-command-works-and-lets-rewrite-it-in-one-minute/
slug: how-the-locate-command-works-and-lets-rewrite-it-in-one-minute
word_count: 636
---


Sometimes I want to find all the Alanis songs on my computer. There are
(basically) two ways to do this.

1. `find / -name '*Alanis*'`
2. `locate Alanis`


I’ve known for a long time that `locate` is faster than `find`, and that it had
some kind of database, and that you could update the database using `updatedb`.


But I always somehow thought of the locate database as this Complicated Thing.
Until today I started looking at it! On my machine it’s
`/var/lib/mlocate/mlocate.db`. You can probably find it with `locate mlocate`
or `strace -e open locate whatever`. It’s about 15MB on my computer.


When I `cat` it, here’s what part of it looks like.


```
/bin^@^@bash^@^@bunzip2^@^@busybox^@^@bzcat^@^@bzcmp^@^@bzdiff^@^@bzegrep^@^@bzexe^@^@bzfgrep^@^@bzgrep^@^@bzip2^@^@bzip2recover^@^@bzless^@^@bzmore^@^@cat^@^@chacl^@^@chgrp^@^@chmod^@^@chown^@^@chvt
^@^@cp^@^@cpio^@^@dash^@^@date^@^@dbus-cleanup-sockets^@^@dbus-daemon^@^@dbus-uuidgen^@^@dd^@^@df^@^@dir^@^@dmesg^@^@dnsdomainname^@^@domainname^@^@dumpkeys^@^@echo^@^@ed
^@^@egrep^@^@false^@^@fgconsole^@^@fgrep^@^@findmnt^@^@fuser^@^@fusermount^@^@getfacl^@^@grep^@^@gunzip^@^@gzexe^@^@gzip^@^@hostname^@^@ip^@^@kbd_mode^@^@kill^@^@kmod^@^@
less^@^@lessecho^@^@lessfile^@^@lesskey^@^@lesspipe^@^@ln^@^@loadkeys^@^@login^@^@loginctl^@^@lowntfs-3g^@^@ls^@^@lsblk^@^@lsmod^@^@mkdir^@^@mknod^@^@mktemp

```


And here’s what’s in the `/bin` directory:


```
$ ls /bin | head
bash
bunzip2
busybox
bzcat
bzcmp
bzdiff
bzegrep
bzexe
bzfgrep
bzgrep

```


COINCIDENCE THAT ALL OF THESE WORDS ARE THE SAME? I THINK NOT!


It turns out that the locate database is basically just a huge recursive
directory listing (`ls -R /`). (I think it’s actually more complicated than
that; there’s a paper at the end). So a slightly less space-efficient version
of this whole `locate` business would be to create a database with this Very
Sophisticated Command:


```
sudo find / > database.txt

```


This gives us a file that looks like


```
/
/vmlinuz.old
/var
/var/mail
/var/spool
/var/spool/rsyslog
/var/spool/mail
/var/spool/cups
/var/spool/cups/tmp
/var/spool/cron

```


Then we can more or less reproduce `locate`’s functionality by just doing


```
grep Alanis database.txt


```


I got curious about the relative speed of `find` vs `locate` vs our makeshift
locate using `grep`. I have an SSD, so a `find` across all files on my computer
is pretty fast:


```
$ time find / -name blah
0.59user 0.67system 0:01.71elapsed 73%CPU

```


```
$ time locate blah
0.26user 0.00system 0:00.30elapsed 87%CPU

```


```
$ time grep blah database.txt
0.04user 0.02system 0:00.10elapsed 64%CPU

```


Whoa, our homegrown locate using grep is actually way faster! That is
surprising to me. Our homegrown database takes about 3x as much space as
`locate`’s database (45MB instead of 15MB), so that’s probably part of why.


Anyway now you know how it works! This kind of makes me wonder if our database
format which doesn’t use any clever compression tricks might actually be a
better format if you’re not worried about the extra space it takes up. But I
don’t really understand yet why locate is so much slower.


My current theory is that grep is better optimized than locate and that it can
do smarter stuff. But if you know the real answer, or if you get different
results on your computer, please tell me!


update: omg Mark Dominus tweeted at me within seconds and said he [found exactly the same thing 10 years ago](http://perl.plover.com/classes/mybin/samples/slide077.html). Maybe this is really a thing! Or, more likely, there’s just stuff I don’t understand yet here. Either way I’d like to know!


further update: Patrick Collison pointed out this amazingly-titled (and short! 3 pages!)
[Finding Files Fast](http://www.eecs.berkeley.edu/Pubs/TechRpts/1983/CSD-83-148.pdf)
from 1983 which talks about locate’s design, and also claims that the
[source is pretty readable](http://ftp3.usa.openbsd.org/pub/OpenBSD/src/usr.bin/locate/).


The 1983 paper specifically calls out “Why not simply build a list of static
files and search with grep?”, and says that grepping a list of 20,000 files
took 30 seconds (“unacceptable for an oft-used command”), and that their locate
implementation gives them better performance. To compare, I have 700,000 files
on my hard disk, and it takes about 0.05 seconds. It seems to me like the
locate authors’ original issues are really not a problem anymore, 30 years
later.


They’re also pretty worried about saving space in the locate database, which
also isn’t really a concern anymore. This really makes me wonder what other
standard unix programs make design assumptions that aren’t true in 2015.
