---
title: "Let That Be a Lesson To You, Son: Never Upgrade."
date: 2008-03-31
url: https://blog.codinghorror.com/let-that-be-a-lesson-to-you-son-never-upgrade/
slug: let-that-be-a-lesson-to-you-son-never-upgrade
word_count: 1146
---

kg-card-begin: html

(Update: This piece originally ran on April Fools’ day; although the content of the post is *not* an April Fools’ joke, the retro styling definitely was. [View a screenshot](https://web.archive.org/web/20081211040237if_/http://www.codinghorror.com/blog/images/coding-horror-april-1-2008.png) of how this post looked on April 1, 2008)

kg-card-end: html

I occasionally follow [Jamie Zawinski’s blog](http://jwz.livejournal.com/). Jamie’s an interesting guy. In the process of researching [an earlier post](https://blog.codinghorror.com/is-worse-really-better/), I discovered that he played a significant role in unearthing the classic [Worse is Better](https://blog.codinghorror.com/worse-is-better/) paper:


> About a year later [1991] we hired a young kid from Pittsburgh named Jamie Zawinski. He was not much more than 20 years old and came highly recommended by Scott Fahlman. We called him “The Kid.” He was a lot of fun to have around: not a bad hacker and definitely in a demographic we didn’t have much of at Lucid. He wanted to find out about the people at the company, particularly me since I had been the one to take a risk on him, including moving him to the West Coast. His way of finding out was to look through my computer directories - none of them were protected. He found the EuroPAL paper, and found the part about worse is better. He connected these ideas to those of Richard Stallman, whom I knew fairly well since I had been a spokesman for the League for Programming Freedom for a number of years. JWZ excerpted the worse-is-better sections and sent them to his friends at CMU, who sent them to their friends at Bell Labs, who sent them to their friends everywhere.


Or, perhaps you’ve read the classic [Teach Yourself Programming in Ten Years](http://norvig.com/21-days.html)? That was written by Peter Norvig, who is now the director of research at Google. It refers to Mr. Zawinski thusly:


> One of the best programmers I ever hired had only a High School degree; he’s produced a lot of great software, has his own news group, and made enough in stock options to buy his own nightclub.


I think you’ll agree that it’s fair to call Jamie Zawinski a world class software engineer. Jamie’s blog documents, in great detail, how he runs his [DNA Lounge](http://www.dnalounge.com/) club in San Francisco. It’s a great read, full of fascinating, often geeky backstage details. The DNA Lounge is powered by open source software, including various flavors of Linux. Sometimes this can be painful. In 2006, Jamie ran into serious problems with the Linux sound architecture:


> You may have noticed that the audio archives have only had one channel for the last few weeks. You would probably assume that’s a simple matter of replacing a cable; turns out, not. As far as we can tell, the audio going into the computer is stereo, and somewhere in there, it drops (most of) the right channel. So, bad connector, right? No, we’ve tried four different sound cards, and checked the mixer settings. At this point it seems like the last time we (accidentally) [upgraded ALSA](https://bugzilla.redhat.com/show_bug.cgi?id=179639), it introduced some software bug that is making one channel go away. I can’t even fathom how such a bug could exist, but that’s Linux for you.
> We seem to have solved the “missing right channel” problem. It was, in fact, a software problem. We were running Fedora 4, and when we installed the latest patches on March 31, that’s when the right channel vanished. We tried downgrading to the version of the kernel and ALSA as of three months ago, and that didn’t fix it. But, Jonathan took all the sound cards home and tried them in his machine, and they all worked fine there. He was running Fedora 5. So we upgraded to that, and the problem went away.
> That’s right: upgrading to the latest FC4: breaks the world. Giving up on FC4 and going to FC5: un-breaks it. Nicely done, guys.
> For years I’ve had it drummed into my head that you always have to keep your systems patched, if you aren’t running the latest security fixes, the script kiddies will eat you alive, running a six month old OS is like leaving your front door wide open, blah blah blah. Well you know what? **F**k that noise. I’m done upgrading anything ever**. The next time I get this s**t into a state that seems even remotely stable, I’m never touching it again. If we get hacked, oh well. I have backups. It has got to be less work to recover from than constantly dealing with this kind of nonsense.


The DNA lounge provides [streaming audio and video webcasts](http://www.dnalounge.com/webcast/) of whatever is going on any time the club is open. So problems like this are especially troubling – Jamie’s business depends on this stuff working.


I was particularly disturbed to find [this recent entry](http://www.dnalounge.com/backstage/log/2008/03.html#26):


> I spent a solid four days trying to upgrade the kiosks from Red Hat 9 + LTSP 4.3 (vintage 2003) to... something newer. In this case, Ubuntu 10.7 + LTSP 5, since it seems like that’s what the cool kids are running these days. Why would I do such a thing? Well, one reason is that the Firefox 3 beta would neither install nor compile on RH9 (missing libraries), and another was that the kiosks are a little crashy (they reboot themselves pretty regularly for no adequately explored reason), and also, it’s “just kinda old,” which some people will tell you might mean, maybe, kinda, less secure. So I figured I’d give it a shot.
> Well, since this is not my first rodeo, when I say “upgrade” what I really mean is “do a fresh install on a spare drive.”
> So, after four days of this nonsense, I gave up, and just put the old drive back in. “Nonsense” in this case is defined as: the upgrade made the machines be even crashier than before (they can barely stay up for an hour) and it’s a far worse kind of crashy: it’s the kind of crashy where you have to press the shiny red button to make them come back to life, instead of them being able to do that themselves.
> So, f**k it. **They’ll be running a 2003 version of Linux forever**, because I frankly have better things to do with my time.


I can’t fault Jamie’s approach. A clean install of an operating system on a new hard drive – for kiosks running controlled hardware, no less – that’s as good as it gets.


Apparently, **Linux is so complex that even a world class software engineer can’t always get it to work**.


I find it highly disturbing that a software engineer of Jamie’s caliber would give up on upgrading software. Jamie lives and breathes Linux. It is his platform of choice. If he throws in the towel on Linux upgrades, then what *possible* hope do us mere mortals have?

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
