---
title: "Backups & redundancy at sr.ht"
date: 2019-01-13
url: https://drewdevault.com/2019/01/13/Backups-and-redundancy-at-sr.ht.html
slug: Backups-and-redundancy-at-sr.ht
word_count: 1148
---

[sr.ht](https://sr.ht) 1  is  [100% open source](https://git.sr.ht/~sircmpwn?search=sr.ht)  and I encourage
people to install it on their own infrastructure, especially if they’ll be
sending patches upstream. However, I am equally thrilled to host sr.ht for you
on the “official” instance, and most users find this useful because the
maintenance burden is non-trivial. Today I’ll give you an idea of what your
subscription fee pays for. In this first post on ops at sr.ht, I’ll talk about
backups and redundancy. In future posts, I’ll talk about security, high
availability, automation, and more.

As sr.ht is still in the alpha phase, high availability has been on the
backburner. However, data integrity has always been of paramount importance to
me. The very earliest versions of sr.ht, from well before it was even trying to
be a software forge, made a point to never lose a single byte of user data.
Outages are okay - so long as when service is restored, everything is still
there. Over time I’m working to make outages a thing of the past, too, but let’s
start with backups.

There are several ways that sr.ht stores data:

* Important data on the filesystem (e.g. bare git repositories)
* Important persistent data in PostgreSQL
* Unimportant ephemeral data in Redis (& caches)
* Miscellaneous filesystem storage, like the operating system

Some of this data is important and kept redundant (PostgreSQL, git repos), and
others are unimportant and is not redundant. For example, I store a rendered
Markdown cache for git.sr.ht in Redis. If the Redis cluster goes  *poof* , the
source Markdown is still available, so I don’t bother backing up Redis. Most
services run in a VM and I generally don’t store important data on these - the
hosts usually only have one hard drive with no backups and no redundancy. If the
host dies, I have to reprovision all of those VMs.

Other data is more important. Consider PostgreSQL, which contains some of the
most important data for sr.ht. I have one master PostgreSQL server, a dedicated
server in the space I colocate in my home town of Philadelphia. I run sr.ht on
this server, but I also use it for a variety of other projects - I maintain many
myself, and I volunteer as a sysadmin for more still. This box (named Remilia)
has four hard drives configured in a ZRAID (ZFS). I buy these hard drives from a
variety of vendors, mostly Western Digital and Seagate, and from different
batches - reducing the likelihood that they’ll fail around the same time. ZFS is
well-known for it’s excellent design, featureset and for simply keeping your
data intact, and I don’t trust any other filesystem with important data. I take
ZFS snapshots every 15 minutes and retain them for 30 days. These snapshots are
important for correcting the “oh shit, I rm’d something important” mistakes -
you can mount them later and see what the filesystem looked like at the time
they were taken.

On top of this, the PostgreSQL server is set up with two additional important
features: continuous archiving and streaming replication. Continuous archiving
has PostgreSQL writing each transaction to log files on disk, which represents a
re-playable history of the entire database, and allows you to restore the
database to any point in time. This helps with “oh shit, I dropped an important
table” mistakes. Streaming replication ships changes to an off-site standby
server, in this case set up in my second colocation in San Francisco (the main
backup box, which we’ll talk about more shortly). This takes a near real-time
backup of the database, and has the advantage of being able to quickly failover
to it as the primary database during maintenance and outages (more on this
during the upcoming high availability article). Soon I’ll be setting up a second
failover server as well, on-site.

So there are multiple layers to this:

* ZFS & zraid prevents disk failure from causing data loss
* ZFS snapshots allows retrieving filesystem-level data from the past
* Continuous archiving allows retrieving database-level data from the past
* Streaming replication prevents datacenter existence failure from causing data
loss

Having multiple layers of data redundancy here protects sr.ht from a wide
variety of failure modes, and also protects each redundant system from itself -
if any of these systems fails, there’s another place to get this data from.

The off-site backup in San Francisco (this box is called Konpaku) has a whopping
52T of storage in two ZFS pools, named “small” (4T) and “large” (48T). The
PostgreSQL standby server lives in the small pool, and  [borg
backups](https://www.borgbackup.org/)  live in the large pool. This has the same
ZFS snapshotting and retention policy as Remilia, and also has drives sourced
from a variety of vendors and batches. Borg is how important filesystem-level
data is backed up, for example git repositories on git.sr.ht. Borg is nice
enough to compress, encrypt, and deduplicate its backups for us, which I take
hourly with a cronjob on the machines which own that data. The retention policy
is hourly backups stored for 48 hours, daily backups for 2 weeks, and weekly
backups stored indefinitely.

There are two other crucial steps in maintaining a working backup system:
monitoring and testing. The old wisdom is “you don’t have backups until you’ve
tested them”. The simplest monitoring comes from cron - when I provision a new
box, I make sure to set  `MAILTO` , make sure sendmail works, and set up a
deliberately failing cron entry to ensure I hear about it when it breaks. I also
set up zfs-zed to email me whenever ZFS encounters issues, which also has a test
mode you should use. For testing, I periodically provision private replicas of
sr.ht services from backups and make sure that they work as expected. PostgreSQL
replication is fairly new to my setup, but my intention is to switch the primary
and standby servers on every database upgrade for HA 2  purposes, which
conveniently also tests that each standby is up-to-date and still replicating.

To many veteran sysadmins, a lot of this is basic stuff, but it took me a long
time to learn how all of this worked and establish a set of best practices for
myself. With the rise in popularity of managed ops like AWS and GCP, it seems
like ops & sysadmin roles are becoming less common. Some of us still love the
sound of a datacenter and the greater level of control you have over your
services, and as a bonus my users aren’t worrying about $bigcorp having access
to their data.

The next ops thing on my todo list is high availability, which is still
in-progress on sr.ht. When it’s done, expect another blog post!

1. sr.ht is a software project hosting website, with git hosting, ticket tracking, continuous integration, mailing lists, and more. [Try it out!](https://sr.ht) ↩︎
2. High availability ↩︎
