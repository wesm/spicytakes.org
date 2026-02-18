---
title: "How to store data forever"
date: 2020-04-22
url: https://drewdevault.com/2020/04/22/How-to-store-data-forever.html
slug: How-to-store-data-forever
word_count: 1915
---

As someone who has been often maligned by the disappearance of my data for
various reasons — companies going under, hard drive failure, etc —
and as someone who is responsible for the safekeeping of other people’s data,
I’ve put a lot of thought into solutions for long-term data retention.

There are two kinds of long-term storage, with different concerns: cold storage
and hot storage. The former is like a hard drive in your safe — it stores
your data, but you’re not actively using it or putting wear on the storage
medium. By contrast, hot storage is storage which is available immediately and
undergoing frequent reads and writes.

## What storage medium to use?

There are some bad ways to do it. The worst way I can think of is to store
it on a microSD card. These fail  *a lot* . I couldn’t find any hard data, but
anecdotally, 4 out of 5 microSD cards I’ve used have experienced failures
resulting in permanent data loss. Low volume writes, such as from a digital
camera, are unlikely to cause failure. However, microSD cards have a tendency to
get hot with prolonged writes, and they’ll quickly leave their safe operating
temperature and start to accumulate damage. Nearly all microSD cards will let
you perform writes fast enough to drive up the temperature beyond the operating
limits — after all, writes per second is a marketable feature — so
if you want to safely move lots of data onto or off of a microSD card, you need
to monitor the temperature and throttle your read/write operations.

A more reliable solution is to store the data on a hard drive 1 . However, hard
drives are rated for a limited number of read/write cycles, and can be expected
to fail eventually. Backblaze publishes some great articles on  [hard drive
failure rates](https://www.backblaze.com/blog/hard-drive-stats-for-2019/)  across
their fleet. According to them, the average annual failure rate of hard drives
is almost 2%. Of course, the exact rate will vary with the frequency of use and
storage conditions. Even in cold storage, the shelf life of a magnetic platter
is not indefinite.

There are other solutions, like optical media, tape drives, or more novel
mediums, like the  [Rosetta Disk](https://en.wikipedia.org/wiki/Rosetta_Project) .
For most readers, a hard drive will be the best balance of practical and
reliable. For serious long-term storage, if expense isn’t a concern, I would
also recommend hot storage over cold storage because it introduces the
possibility of active monitoring.

## Redundancy with RAID

One solution to this is redundancy — storing the same data across multiple
hard drives. For cold storage, this is often as simple as copying the data onto
a second hard drive, like an external backup HDD. Other solutions exist for hot
storage. The most common standard is  [RAID](https://en.wikipedia.org/wiki/RAID) , which offers different
features with different numbers of hard drives. With two hard drives (RAID1), for
example, it utilizes mirroring, which writes the same data to both disks. RAID
gets more creative with three or more hard drives, utilizing  *parity* , which
allows it to reconstruct the contents of failed hard drives from still-online
drives. The basic idea relies on the XOR operation. Let’s say you write the
following byte to drive A:  `0b11100111` , and to drive B:  `0b10101100` . By XORing
these values together:

```
  11100111 A
^ 10101100 B
= 01001011 C
```

We obtain the value to write to drive C. If any of these three drives fail, we
can XOR the remaining two values again to obtain the third.

```
  11100111 A
^ 01001011 C
= 10101100 B

  10101100 B
^ 01001011 C
= 11100111 A
```

This allows any drive to fail while still being able to recover its contents,
and the recovery can be performed online. However, it’s often not that simple.
Drive failure can dramatically reduce the performance of the array while it’s
being rebuilt — the disks are going to be seeking constantly to find the
parity data to rebuild the failed disk, and any attempts to read from the disk
that’s being rebuilt will require computing the recovered value on the fly. This
can be improved upon by using lots of drives and multiple levels of redundancy,
but it is still likely to have an impact on the availability of your data if not
carefully planned for.

You should also be monitoring your drives and preparing for their failure in
advance.  Failing disks can show signs of it in advance — degraded
performance, or via S.M.A.R.T reports. Learn the tools for monitoring your
storage medium, such as smartmontools, and set it up to report failures to you
(and  *test*  the mechanisms by which the failures are reported to you).

### Other RAID failure modes

There are other common ways a RAID can fail that result in permanent data loss.
One example is using hardware RAID — there was an argument to be made for
them at one point, but these days hardware RAID is  *almost always*  a mistake.
Most operating systems have software RAID implementations which can achieve the
same results without a dedicated RAID card. With hardware RAID, if the RAID card
itself fails (and they often do), you might have to find the exact same card to
be able to read from your disks again. You’ll be paying for new hardware, which
might be expensive or out of production, and waiting for it to arrive before you
can start recovering data. With software RAID, the hard drives are portable
between machines and you can always interpret the data with general purpose
software.

Another common failure is  *cascading*  drive failures. RAID can tolerate partial
drive failure thanks to parity and mirroring, but if the failures start to pile
up, you can suffer permanent data loss. Many a sad administrator has been in
panic mode, recovering a RAID from a disk failure, and at their lowest
moment… another disk fails. Then another. They’ve suddenly lost their data,
and the challenge of recovering what remains has become ten times harder. When
you’ve been distributing read and write operations consistently across all of
your drives over the lifetime of the hardware, they’ve been receiving a similar
level of wear, and failing together is not uncommon.

Often, failures like this can be attributed to using many hard drives from the
same batch. One strategy I recommend to avoid this scenario is to use drives
from a mix of vendors, model numbers, and so on. Using a RAID improves
performance by distributing reads and writes across drives, using the time one
drive is busy to utilize an alternate. Accordingly, any differences in the
performance characteristics of different kinds of drives will be smoothed out in
the wash.

## ZFS

RAID is complicated, and getting it right is difficult. You don’t want to wait
until your drives are failing to learn about a gap in your understanding of
RAID. For this reason, I recommend ZFS to most. It automatically makes good
decisions for you with respect to mirroring and parity, and gracefully handles
rebuilds, sudden power loss, and other failures. It also has features which are
helpful for other failure modes, like snapshots.

Set up Zed to email you reports from ZFS. Zed has a debug mode, which will send
you emails even for working disks — I recommend leaving this on, so that
their conspicuous absence might alert you to a problem with the monitoring
mechanism. Set up a cronjob to do monthly scrubs and review the Zed reports when
they arrive. ZFS snapshots are cheap - set up a cronjob to take one every 5
minutes, perhaps with  [zfs-auto-snapshot](https://github.com/zfsonlinux/zfs-auto-snapshot) .

## Human failures and existential threats

Even if you’ve addressed hardware failure, you’re not done yet. There are other
ways still in which your storage may fail. Maybe your server fans fail and burn
out all of your hard drives at once. Or, your datacenter could suffer a total
existence failure — what if a fire burns down the building?

There’s also the problem of human failure. What if you accidentally  `rm -rf / *` 
the server? Your RAID array will faithfully remove the data from all of the hard
drives for you. What if you send the sysop out to the datacenter to decommission
a machine, and no one notices that they decommissioned the wrong one until it’s
too late?

This is where off-site backups come into play. For this purpose, I recommend
 [Borg backup](https://www.borgbackup.org/) . It has sophisticated features for compression and
encryption, and allows you to mount any version of your backups as a filesystem
to recover the data from. Set this up on a cronjob as well for as frequently as
you feel the need to make backups, and send them off-site to another location,
which itself should have storage facilities following the rest of the
recommendations from this article. Set up another cronjob to run  `borg check` 
and send you the results on a schedule, so that their conspicuous absence may
indicate that something fishy is going on. I also use  [Prometheus](https://prometheus.io/)  with
 [Pushgateway](https://github.com/prometheus/pushgateway)  to make a note every time that a backup is run, and
set up an alarm which goes off if the backup age exceeds 48 hours. I also have
periodic test alarms, so that the alert manager’s own failures are noticed.

## Are you prepared for the failure?

When your disks are failing and everything is on fire and the sky is falling,
this is the worst time to be your first rodeo. You should have  *practiced*  these
problems before they became problems. Do training with anyone expected to deal
with failures. Yank out a hard drive and tell them to fix it. Have someone in
sales come yell at them partway through because the website is unbearably slow
while the RAID is rebuilding and the company is losing $100 per minute as a
result of the outage.

Periodically produce a working system from your backups. This proves (1) the
backups are still working, (2) the backups have coverage over everything which
would need to be restored, and (3) you know how to restore them. Bonus: if
you’re confident in your backups, you should be able to replace the production
system with the restored one and allow service to continue as normal.

## Actually storing data  *forever*

Let’s say you’ve managed to keep your data around. But will you still know how
to interpret that data in the future? Is it in a file format which requires
specialized software to use? Will that software still be relevant in the future?
Is that software open-source, so you can update it yourself? Will it still
compile and run correctly on newer operating systems and hardware? Will the
storage medium still be compatible with new computers?

Who is going to be around to watch the monitoring systems you’ve put in place?
Who’s going to replace the failing hard drives after you’re gone? How will they
be paid? Will the dataset still be comprehensible after 500 years of evolution
of written language? The dataset requires constant maintenance to remain intact,
but also to remain useful.

And ultimately, there is one factor to long-term data retention that you cannot
control: future generations will decide what data is worth keeping — not
us.

In summary: no matter what, definitely don’t do this:

1. Or SSDs, which I will refer to interchangeably with HDDs in this article. They have their own considerations, but we’ll get to that. ↩︎
