---
title: "International Backup Awareness Day"
date: 2009-12-14
url: https://blog.codinghorror.com/international-backup-awareness-day/
slug: international-backup-awareness-day
word_count: 1551
---

You may notice that commenting is currently disabled, and many old Coding Horror posts are missing images. That’s because, sometime early on Friday, **the server this blog is hosted on suffered catastrophic data loss**.


Here’s what happened:

1. The server experienced routine hard drive failure.
2. Because of the hard drive failure, the virtual machine image hosting this blog was corrupted.
3. Because the blog was hosted in a virtual machine, the standard daily backup procedures at the host were unable to ever back it up.
4. Because I am an idiot, I didn’t have my own (recent) backups of Coding Horror. Man, I wish I had read some good [blog entries on backup strategies!](https://blog.codinghorror.com/whats-your-backup-strategy/)
5. Because there were no good backups, there was catastrophic data loss. Fin, draw curtain, exeunt stage left.


At first, I was upset with our provider, CrystalTech.


![](https://blog.codinghorror.com/content/images/2025/04/image-450.png)


I am still confused how the most common, routine, predictable, and mundane of server hardware failures – losing a mechanical hard drive – could cause such extreme data loss carnage. What about, oh, I don’t know, [a RAID array](https://blog.codinghorror.com/beyond-raid/)? Aren’t they *designed* to prevent this kind of single point of failure drive loss catastrophe? Isn’t a multi drive RAID array sort of standard on datacenter servers? I know we have multi-drive RAID arrays on all of [our Stack Overflow servers](http://blog.stackoverflow.com/2009/12/stack-overflow-rack-glamour-shots/).


I also wish their routine backup procedures had greater awareness of virtual machine images. While I’ll grant you that backing up a live virtual machine is somewhat complex, and typically requires special operating system support and API hooks, it is not exactly an unknown science at this point in time. Heck, at the very least, just let us know when the backup has been regularly failing each day, every day, for *years*.


Then I belatedly realized that this was, after all, *my* data. And **it is irresponsible of me to leave the fate of my data entirely in someone else’s hands**, regardless of how reliable they may or may not be. Responsibility for my data begins with me. If I haven’t taken appropriate measures, who am I to cast aspersions on others for not doing the same? Glass houses and all that.


So, I absolve CrystalTech of all responsibility in this matter. They’ve given us a great deal on our dedicated server, and performance and reliability (with one recent, uh... exception) have been excellent to date. **It is completely my fault that I neglected to have proper backups in place for Coding Horror.** Well, technically, I did have a backup but it was on the virtual machine itself. Does that count? No? Halfsies?


Apparently, I was *gambling* that nothing bad would ever happen at the datacenter. Because that’s what you’re doing when you run without your own backups. [**Gambling**](https://www.youtube.com/watch?v=7hx4gdlfamo)**.**


![](https://blog.codinghorror.com/content/images/2025/04/image-449.png)


I’ll add gambling to the long, long list of things I suck at. I don’t know when to hold   ’em *or* when to fold ’em.


Now that I’ve apologized, it’s time to let the healing begin. And by healing, I mean **the excruciatingly painful process of reconstructing Coding Horror from internet caches and the few meager offsite backups I do have**. My first order of business was to ask on SuperUser what strategies people recommend for [recovering a lost website with no back up.](https://superuser.com/questions/82036/recovering-a-lost-website-with-no-backup) Strategies other than berating me for my obvious mistake. Also, comments are currently disabled while the site is being reconstructed from static HTML. Oh, *darn!*


I’ll let [my son](https://blog.codinghorror.com/on-parenthood/) Rock Hard Awesome stand in for the zinger of a comment that I know some of you were *just dying* to leave.


![](https://blog.codinghorror.com/content/images/2025/04/image-448.png)


I’m not saying I don’t deserve it. Consider me totally zingatized.


I mentioned my woes on Twitter and I was humbled by the outpouring of community support. Thanks to everyone who reached out with support of any kind. It is greatly appreciated.


I was able to get a static HTML version of Coding Horror up almost immediately thanks to Rich Skrenta of blekko.com. He kindly provided a tarball of every spidered page on the site. Some people have goals, and some people have [*big hairy audacious goals*](https://web.archive.org/web/20100212070723/http://www.skrenta.com/2008/03/who_will_stop_google_from_goin.html). Rich’s is especially awe-inspiring: taking on Google on their home turf of search. That’s why he just happened to have a complete text archive of Coding Horror at hand. Rich, have I ever told you that [you’re my hero?](http://www.youtube.com/watch?v=oiS8YokFzeY) Anyway, you’re viewing the static HTML version of Coding Horror right now thanks to Rich. Surprisingly, there’s not a tremendous amount of difference between a static HTML version of this site and the live site. One of the benefits of being a minimalist, I suppose.


That pretty much solved all my text post recovery problems in one fell swoop. Through this process, I’ve learned that anything even remotely popular you put on the web will be archived as text, forever, by a dozen different web spiders. **I don’t think you can actually *lose* text you post on the web.** Not in any meaningful sense; I’m not sure it’s possible. As long as you’re willing to spend the time digging through web spider archives in some form (and yes, I did cheat mightily), you can always get textual content back, all of it.


The blog *images*, however, are another matter entirely. I have learned the hard way that **there are almost no organizations spidering and storing images on the web**. Yes, there is [archive.org](https://archive.org/), and God bless ’em for that. But they have [an impossible job they’re trying to do with limited resources](https://blog.codinghorror.com/preserving-the-internet-and-everything-else/). Beyond that, there’s... well, frankly, a whole lot of nothing. A desperate, depressing void of nothing. In fact, if you can only back up one thing on your public website, **it should be the images.** Because that’s the thing you’ll have the most difficulty recovering when catastrophe happens. I’m planning to donate $100 to archive.org as I have a whole new appreciation for how rare an internet-wide full archive service – one that includes images – really is.


That said, There are some limited, painful avenues to explore for recovering lost website images. I started with an ancient complete backup from mid 2006 with full images. And then Maciej Ceglowski of the nifty full-archive bookmarking service [pinboard.in](https://pinboard.in/) generously contributed about 200 blog posts that he had images for.


I also went through a period when I was [going on a bandwidth diet](https://blog.codinghorror.com/reducing-your-websites-bandwidth-usage/) and experimenting with hosting Coding Horror images elsewhere on the web. I’m slowly going through and recovering images locally from there. Beyond that, several avid Coding Horror readers contributed some archived images – so thanks to Yasushi Aoki, Marcin Goabiowski, Peter Mortensen, and anybody else I’ve forgotten.


Also, I should point out that a few enterprising programmers have proposed clever schemes for automatic recovery of images, such as Niyaz with his blog post [Get cached images from your visitors](https://web.archive.org/web/20091214185558/http://www.diovo.com/2009/12/getting-cached-images-in-your-website-from-the-visitors/), and [John Siracusa](https://web.archive.org/web/20091213203017/http://arstechnica.com/staff/fatbits/) with his [highly voted 304 idea](https://superuser.com/questions/82036/recovering-a-lost-website-with-no-backup/82060#82060). I haven’t had time to follow up on these yet but they seem plausible to me.


I’ve restored all the images I have so far, but it’s still woefully incomplete. The most important part of Coding Horror is definitely the text of the posts, but I do have some regrets that I’ve lost key images from many blog posts, including those about [my son](https://blog.codinghorror.com/spawned-a-new-process/). It feels like irresponsible parenting, in the broadest possible sense of the words.

kg-card-begin: html

The process of image recovery is still ongoing. **If you’d like to contribute lost Coding Horror images, please do.** I’d be more than happy to mail stickers on my dime to anyone who contributes an image that is currently a 404 on the site. Update: That was fast. Carmine Paolino, a computer science student at the University of Bologna, somehow had a nearly complete mirror of the site backed up on his Mac! Thanks to his mirror, we’ve now recovered nearly 100% of the missing images and content. I’ve offered to donate $100 to the charity or open source project of Carmine’s choice.

kg-card-end: html

What can we all learn from this sad turn of events?

1. I suck.
2. No, really, I suck.
3. Don’t rely on your host or anyone else to back up your important data. Do it yourself. If you aren’t *personally* responsible for your own backups, **they are effectively not happening.**
4. If something really bad happens to your data, how would you recover? What’s the process? What are the hard parts of recovery? I think in the back of my mind I had false confidence about Coding Horror recovery scenarios because I kept thinking of it as mostly text. Of course, the text turned out to be the *easiest* part. The images, which I had thought of as a “nice to have,” were more essential than I realized and far more difficult to recover. Some argue that we [shouldn’t be talking about “backups,”](https://www.joelonsoftware.com/2009/12/14/lets-stop-talking-about-backups/) but recovery.
5. It’s worth revisiting your recovery process periodically to make sure it’s still alive, kicking, and fully functional.
6. I’m awesome! No, just kidding. I suck.


So when, exactly, is International Backup Awareness Day? Today. Yesterday. This week. This month. This year. It’s a trick question. ***Every* day is International Backup Awareness Day**. And the sooner I figure that out, the better off I’ll be.

[backups](https://blog.codinghorror.com/tag/backups/)
[data loss](https://blog.codinghorror.com/tag/data-loss/)
[server management](https://blog.codinghorror.com/tag/server-management/)
[disaster recovery](https://blog.codinghorror.com/tag/disaster-recovery/)
[virtual machines](https://blog.codinghorror.com/tag/virtual-machines/)
