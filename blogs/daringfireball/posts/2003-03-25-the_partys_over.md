---
title: "The Party’s Over"
date: 2003-03-25
url: https://daringfireball.net/2003/03/the_partys_over
slug: the_partys_over
word_count: 1267
---


Who didn’t see this coming? [CNet reports](http://rss.com.com/2100-1046-993835.html?type=pt&part=rss&tag=feed&subj=news): “Apple Computer has terminated a program that gave some developers access to the latest test versions of its Safari browser, after some testers apparently leaked several prereleases to the public.”


Actually, it seems like *a lot* of people didn’t see it coming, judging by the comments in public forums at [MacSlash](http://www.macslash.org/articles/03/03/23/0226237.shtml) and [Slashdot](http://apple.slashdot.org/article.pl?sid=03/03/22/2343249&mode=nested&tid=107).


If you’re living in a Safari news vacuum, here’s a short summary. In
January, Apple released a public beta of Safari, their brand-new web
browser. They’ve released two or three updated public betas since; the
current public beta at this writing is version v60, from February. Apple has also been releasing other interim versions to select developers and testers, under non-disclosure agreements. These interim builds, which were never intended for release to the general public, have been widely leaked and are in use by everyone other than your grandmother. These leaked builds exploded in popularity when they began including support for tabbed browsing.


Public sentiment regarding Apple’s decision to cease the seed program is widely negative. The gist of these complaints runs along these lines:

1. *Apple is releasing public betas anyway, why not release more? I want tabbed browsing now, goddammit.
*
2. *Safari is based on open source code, so it’s unsportsmanlike for Apple to be so secretive about Safari’s development. Yes, the KHTML rendering library is licensed under the LGPL, not the strict GPL, but that’s like taking advantage of a loophole.
*
3. *Canceling the seed program will adversely affect the progress and quality of Safari, because now everyone won’t be testing and submitting bug reports with the latest software.*


These reasons are all crap.


## The ‘One Beta Is as Good as Another’ Argument


The idea is that since Apple is releasing *some* beta versions of Safari, they might as well release them all. Or more specifically, a cry for “nightly builds”, a popular concept in the open source world, where a project pops out a new binary every night containing that day’s changes. If some builds blow up thanks to bugs in new code — so what? — you were warned that it was a “beta”, right?


Wrong. “Public beta” or not, the fact remains that most people expect software to work as advertised. Developers and smart nerds might be forgiving of buggy pre-release software, but normal people are not. They’re scared of buggy software, and rightly so. But at the same time, people are drawn to publicly released beta software like insects to bug zappers. Rather than simply stay away from nightly builds, they’ll try them and get burned, and then start spreading word that Safari is crashy and contains half-baked interface widgets.


Safari entered a market with two leaders: Internet Explorer, the industry standard from the industry giant; and Camino (then Chimera), the valiantly standards-compliant upstart from the massive and well-publicized Mozilla project. Apple’s goal for Safari is clearly to have it become the Mac’s most popular browser. To achieve that means it needs to be good enough to convince people to switch from IE and Camino (especially IE). We’re talking regular, normal Mac users here, and that means Safari needs to build a reputation.


Public nightly builds are never going to happen for Safari, because they’d harm its reputation. Nerds find this hard to believe, because you shouldn’t have any expectations of stability from a nightly build. If you want stability, use the most recent full release instead. If everyone were perfectly rational, that might work. But people aren’t rational, and normal people will end up downloading the latest and greatest, because they suspect they’re missing out on something when they’re using an older version. Look at how many people are using post-v60 builds of Safari now.


These leaked seeds have put Safari’s development team in an uncomfortable position. Knowing that these seeds were leaking to the public, they were left with only two choices:

- Acknowledge and embrace the fact that all Safari seeds end up in the hands of the general public. To do so would mean to be more conservative with the implementation of new features, and to require more testing before the release of any seed.
- Cancel the seed program.


Noticeably left out from my list is the option to continue the seed program as-is. That can’t happen: you can’t continue releasing software intended for a small audience of developers but is instead being used by a large audience of normal users. Normal users can’t resist. They will get hurt, data may be lost, and the software’s reputation will be harmed.


[Matthew Thomas today released a timely essay](http://mpt.phrasewise.com/2003/03/25#a486) touching on just this topic:


> Frustratingly, it means that as far as the user interface is
> 	concerned, *even with the same number of developer hours, volunteer
> 	software will improve more slowly than professional software*.
> 	This is because the professionals are happy to check in usability
> 	changes in any order, without worrying constantly about the current
> 	coherence of the interface, until the release date for the next
> 	version approaches. And when it *does* approach, they’ll be
> 	much happier to back out half-baked changes if necessary, since
> 	they’re being paid either way.


## The ‘Open Source’ Argument


Contrary to widespread believe, Safari is not “based on open source code”. Safari is an application; KHTML is an HTML rendering library. KHTML *is* open source (not “based on” it). Safari, the application, is not. If you think Safari, the application, is nothing more than a “simple wrapper around KHTML”, then we’ll surely see one or more Safari clones pop up within a few days of the forthcoming release of the [WebKit API](http://www.mozillazine.org/weblogs/hyatt/archives/2003_01.html#001733). Don’t hold your breath.


Apple is under no obligation to run Safari’s development as though it were an open source application, because it isn’t one. Even more laughable is the idea that Apple should feel obligated to release the source code to Safari. The motor is not the car; the rendering library is not the browser.


## The ‘Better Bug Reporting’ Argument


This is the biggest joke of all: the argument — repeated by several MacSlash and Slashdot posters — that Safari’s development was *helped* by the leaking of the seeds, because the people using these leaked seeds were sending Apple valuable bug reports and feature requests.


It’s hard to believe anyone could make these comments with a straight face, let alone believe them. The bug reporting feature built into Safari clearly indicates that Apple is indeed interested in bug reports. But it does not follow that they want feedback on builds other than the publicly released betas, i.e. today, v60. If they wanted feedback on the software post-v60, they would release another public beta. Oh, I get it — Slashdot readers know better how to develop quality software than the Safari engineering team does.


The fact is, the opposite is probably the case — the leaked builds almost certainly *decrease* the overall usefulness of reports from the field. How many people sent Apple complaints and suggestions about the obviously-unfinished and unpolished tabbed-browsing support in v62?


The truth is simply that people wanted tab browsing in Safari, and they wanted it now, ready or not. And it’s a bit hypocritical to excuse impatience under an umbrella of altruism — *I’m doing Apple a favor by using v67* — while ignoring the larger moral issue: that some of the seeded Safari testers acted as though their NDAs were printed on Charmin toilet paper.



| **Previous:** | [Bitmap Like It’s 1989](https://daringfireball.net/2003/03/bitmap_like_its_1989) |
| **Next:** | [Interview: Brent Simmons](https://daringfireball.net/2003/03/interview_brent_simmons) |


PreviousNext