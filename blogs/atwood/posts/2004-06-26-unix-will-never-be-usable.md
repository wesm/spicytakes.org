---
title: "UNIX will never be usable"
date: 2004-06-26
url: https://blog.codinghorror.com/unix-will-never-be-usable/
slug: unix-will-never-be-usable
word_count: 887
---

A few months ago, Eric Raymond, the open source guru best known for his seminal paper, [The Cathedral and the Bazaar](http://www.catb.org/~esr/writings/cathedral-bazaar/), posted a rant about the difficulty he encountered with a [common user printing scenario](http://www.catb.org/~esr/writings/cups-horror.html) in UNIX.


The [follow-up post](http://www.catb.org/~esr/writings/luxury-part-deux.html) is even more intriguing:


> I am informed that an RFE covering the issues I raised has been registered on Red Hat Bugzilla. But quibbles over who is responsible for which piece of the CUPS-configuration mess are, as the letters above reinforce, not merely beside the point but evasions of the actual problem, which is a systemic one that affects thousands of other projects and our entire community.
> Up to now, we haven’t been willing to do the real work of making our software usable. It doesn’t matter whether the the failure of the browsing defaults in CUPS to match the documentation was a CUPS-team screwup or a Fedora screwup – Aunt Tillie doesn’t care which direction that finger points, and I don’t either. No, the real problem is that whoever changed the default didn’t immediately fix the documentation to match it as a matter of spinal reflex.
> It also doesn’t matter a damn whether the shoddy and unhelpful design of the printer-configuration tool came out of a CUPS brainpan or a Fedora brainpan. What matters is that whoever was responsible never audited the interface for usability with a real user.
> The CUPS mess is not a failure of one development team, or of one distribution integrator. In fact, it makes a better example because the CUPS guys and the Fedora guys are both well above the median in both general technical chops, design smarts, and attention to usability. **The fact that this mess is an example of our best in action, rather than our worst, just highlights how appallingly low our standards have been.**
> It’s time for that to change. And the really heartening thing I got from the community response is that maybe we’re ready for it to change. “I thought it was just me” – many, many of you out there are already dissatisfied with the poor quality of open-source UIs. but each of you has tended to think you were alone. No longer. It’s time for each and every one of you out there to become public champions for the luxury of ignorance.
> Good UI design is not a result of black magic, it just requires paying attention. Being task-oriented rather than feature-oriented. Recognizing that every time you force a user to learn something, you have fallen down on your job. And that when Aunt Tillie doesn’t understand your software, the fault – and the responsibility to fix it – lies not with her but with you.


However well intentioned this observation is, and quite frankly, how obvious it is – at least, to everyone outside the insular UNIX community – I think Eric is barking up the wrong tree. **UNIX will never be usable. **It is awfully late in the game for the UNIX crowd to suddenly realize what other computer users have intuitively known since, say, 1984 and the introduction of the Macintosh: nobody gives a damn how technically competent your code is when they can’t figure out how to use it. Without usability, *you have nothing.*


> It’s been twenty years since the GNU Manifesto and nearly seven since The Cathedral and the Bazaar. I think it’s time we stopped congratulating ourselves quite so much on our dedication to freedom and our ability to write technically superior code, and began more often to ask What are we doing to serve the real users? Good UI design, and doing the right thing by Aunt Tillie, ought to be a matter of gut-level pride of craftsmanship.


I think it is comically unrealistic to ask a community predicated on C code, kernel hacking, and the utility of command line tools, to suddenly wake up and get the usability religion. It just ain’t gonna happen, because usability is not a part of the fabric of their culture. The open source and UNIX guys have had almost thirty years to come up with a usable GUI; why should history lead me to believe the next five years are going to be any different?


Usability is easily an order of magnitude harder than writing technically competent code, even harder than writing your own operating system kernel. You have to understand what users are actually doing, versus what they say they are doing. Open-source developers don’t have time for things that are a pain in the ass – like users, their conflicting needs, and their general disdain for computers and technology. They want to work on “the fun stuff,” which doesn’t include users pestering them every day. RTFM!


I expect to see usability enhancements from the companies which have **cultivated a culture that respects usability **–** **primarily Microsoft and Apple. I’d love to see more usability in UNIX and open source, and I am encouraged by this sudden influx of concern, but I won’t be holding my breath.


Related articles:

- [Why Free Software Usability Tends to Suck](https://web.archive.org/web/20040412003554/http://mpt.phrasewise.com/discuss/msgReader$173)
- [Why Free Software Usability Tends to Suck Even More](https://web.archive.org/web/20040404055154/http://mpt.phrasewise.com/discuss/msgReader$182)
- [Ronco Spray-On Usability](http://daringfireball.net/2004/04/spray_on_usability) (this is the first time I’ve seen the “order of magnitude” phrase seconded)

[unix](https://blog.codinghorror.com/tag/unix/)
[usability](https://blog.codinghorror.com/tag/usability/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[open source](https://blog.codinghorror.com/tag/open-source/)
[cups](https://blog.codinghorror.com/tag/cups/)
