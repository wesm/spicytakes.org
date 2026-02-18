---
title: "High Sierra Root Login Bug Was Mentioned on Apple’s Support Forums Two Weeks Ago"
date: 2017-11-29
url: https://daringfireball.net/2017/11/high_sierra_root_login_two_weeks_ago
slug: high_sierra_root_login_two_weeks_ago
word_count: 894
---


It’s natural to speculate how a bug as egregious as the now-fixed High Sierra root login bug could escape notice for so long. It seems to have been there ever since High Sierra 10.13.0 shipped on September 25, and may have existed in the betas through the summer. One explanation is that logging in with the username “root” and a blank password is so bizarre that it’s the sort of thing no one would think to try. Like [the classic “1-2-3-4-5” scene in *Spaceballs*](https://www.youtube.com/watch?v=a6iW-8xPw3k), but with the ultimate weak password — none at all.


More insidious though, is the notion that it might not have escaped notice prior to its [widespread publicization yesterday](https://twitter.com/lemiorhan/status/935578694541770752) — but that the people who had heretofore discovered it kept it to themselves.


This exploit was in fact [posted to Apple’s own support forums on November 13](https://forums.developer.apple.com/thread/79235). It’s a bizarre thread. The thread started back on June 8 when a user ran into a problem after installing the WWDC developer beta of High Sierra:


> I am hoping someone might know how to fix this - after updating to
> High Sierra, the two admin accounts on this machine are all of a
> sudden standard accounts. There is no admin account at all, which
> means I can’t seemingly fix this problem because there is no admin
> I can log into. Any changes to the system or software installs I
> try to do that require admin approval, I have no way to grant it.
> And no way to create a new admin user without an existing.


A user posted a solution involving [Single-User mode](https://support.apple.com/en-us/HT201573), and the thread mostly died down. But on November 13, a user under the handle “chethan177” [posted the following](https://forums.developer.apple.com/thread/79235#277225):


> Note: This solution might be specific to High Sierra
> Try this:
> Solution 1:
> On startup, click on “Other”
> Enter username: root and leave the password empty. Press
> enter. (Try twice)
> If you’re able to log in (hurray, you’re the admin now),
> then head over to System Preferences → Users & Groups and
> create a new Admin account.
> Now restart and login to the new Admin Account (you may need
> a new Apple Id). Once you’re logged into this new Admin Id,
> you can again proceed to your System Preferences → Users &
> Groups. Open the Lock Icon with your new Admin ID/Password.
> Assign “Allow user to administer this computer” to your
> original Apple ID. Restart. […]
> Solution 2:
> If you’re unable to login at startup using username: root
> and empty password, then login with your existing account
> (standard user).
> Again, head over to System Preferences → Users & Groups.
> Click on the Lock Icon. When prompted for username and
> password, type username: root and leave the password empty.
> Press enter. This might throw an error, but try again
> immediately with the same username: root and empty password.
> This should unlock the Lock Icon. If it does, try Solution 1
> next.
> P.S. Solution 2 worked for me. No idea how or why. Hope this
> helps.


That’s yesterday’s bug. And in fact, this forum post is where


> A week ago the infrastructure staff at the company I work for
> stumbled on the issue while trying to help one of my colleagues
> recover access to his local admin account. The staff noticed the
> issue and used the flaw to recover my colleague’s account. On Nov
> 23, the staff members informed Apple about it. They also searched
> online and saw the issue mentioned in a few places already, even
> in Apple Developer Forum from Nov 13. It seemed like the issue had
> been revealed, but Apple had not noticed yet.


Yesterday, after the issue exploded, “chethan177” was asked in the thread how he discovered the exploit. His response:


> Hey guys,
> Didn’t realise this was a full blown security issue. I’d messed my
> login credentials trying to change my apple id and voila I was no
> longer an admin. Then began my extensive search on all Apple
> related forums for a solution. Tried everything, didn’t work.
> As to how I stumbled on this, the answer is simple. Pure
> frustration. I’d read on one of the forums where in a user
> suggested we try using “root” for username and leaving the
> password field empty. I did, it failed. Out of sheer frustration,
> I tried again, and voila the **** thing unlocked my admin account
> much to my relief.
> Then I posted it here assuming someone stuck just like me might
> find it useful. It was purely accidental.


Which forum was that, where he found this suggestion? Alas:


> Unfortunately, I don’t remember. I looked up several forums trying
> to look for a solution. Trying the “root” username entry method
> without a password was definitely mentioned somewhere. I just
> happened to try it twice.


So the exploit was floating around, under the radar, for weeks at least, but it seems as though no widespread harm came of it.



| **Previous:** | [Twitter’s 280-Character Own Goal](https://daringfireball.net/2017/11/twitter_280) |
| **Next:** | [First Impressions of the New iMac Pro](https://daringfireball.net/2017/12/imac_pro_first_impressions) |


PreviousNext