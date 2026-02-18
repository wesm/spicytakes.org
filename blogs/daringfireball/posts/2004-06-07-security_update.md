---
title: "Security Update"
date: 2004-06-07
url: https://daringfireball.net/2004/06/security_update
slug: security_update
word_count: 372
---


Short and sweet:


Apple today released [Security Update 2004-06-07](http://docs.info.apple.com/article.html?artnum=61798) (for both
10.3.4 and 10.2.8). The easiest way to install it is via Software
Update. Judging by the changes documented in the [release notes](http://docs.info.apple.com/article.html?artnum=25785), this update closes all the URI/Launch Services-related
vulnerabilities that have been publicized in the last month. I’ve
tested the update on three Macs, and indeed, it closes every
vulnerability I’m aware of.


This is excellent news.


Even better, the release notes contain useful descriptions of the
updated components and the vulnerabilities that have been closed.
It’s not just better-documented than usual, it’s just flat-out
well-documented. Read both of the above-linked documents, and you’ll
know everything you need to know about the update. Documentation
like this is exactly what I wished for in “[Security Cannot Be Spun](https://daringfireball.net/2004/05/security_cannot_be_spun)”.


The gist of Apple’s solution is that when Launch Services attempts
to *automatically* launch an app that you’ve never before manually
launched, it presents a confirmation dialog before launching the app.
This solves the vulnerability where unknown apps could be launched automatically, and does so without removing any functionality.


I’ve updated my page of [instructions](https://daringfireball.net/2004/05/ounce_of_prevention) for dealing with these
vulnerabilities; the short version is that you simply need to update
to the latest version of Panther or Jaguar (10.3.4 or 10.2.8), and
then install all recent security updates.


If you previously used RCDefaultApp or More Internet to disable
vulnerable URI protocols, you can re-enable them if you want. Note,
however, that Security Update 2004-06-07 *removes* the ‘disk’ and
‘disks’ protocols from your Launch Services database. These
protocols simply no longer exist. In addition, DiskImageMounter has
been modified such that it will no longer mount volumes via these
protocols, even if you were to re-enable them (the protocols).


If you want to turn Safari’s “Open ‘safe’ files” preference back on,
it’s probably safe. I.e., there are no known remaining
vulnerabilities you’d be exposed to. However, I think one of the
lessons of this saga has been that it’s unwise to think there exists
such a thing as a “safe file” that can be opened automatically after
it’s been downloaded. In the spirit of “better safe than sorry”, I’m
leaving this preference off.



| **Previous:** | [Broken Windows](https://daringfireball.net/2004/06/broken_windows) |
| **Next:** | [Misregistered](https://daringfireball.net/2004/06/misregistered) |


PreviousNext