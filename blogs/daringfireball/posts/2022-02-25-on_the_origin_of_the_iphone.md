---
title: "On the Origin of the iPhone"
date: 2022-02-25
url: https://daringfireball.net/2022/02/on_the_origin_of_the_iphone
slug: on_the_origin_of_the_iphone
word_count: 3697
---


Last month [The Information published an intriguing report](https://www.theinformation.com/articles/meta-platforms-halts-vr-and-ar-operating-system-project) about Facebook’s decision to cancel its own ground-up OS for virtual and augmented reality — a project known internally as “XROS” — in favor of “VROS”, the Android-derived system that already powers their Oculus headsets. [When I linked to the story](https://daringfireball.net/linked/2022/01/05/information-meta-xros), I compared Facebook’s bake-off between two internal OS projects to that of the original iPhone OS at Apple:


> I wonder if this is sort of like the early days of Apple’s iPhone
> efforts, when [there were two competing OS teams inside
> Apple](https://daringfireball.net/linked/2022/01/05/apples-dueling-iphone-os-projects): a Scott Forstall/Bertrand Serlet-led team trying to
> shrink Mac OS X down to run on a phone, and a Tony Fadell/Jon
> Rubinstein/Steve Sakoman-led team trying to scale the iPod’s
> embedded Linux OS up to serve as a phone OS. Maybe what happened
> at Facebook isn’t so much “*We give up on our own new OS, let’s
> just use Android,*” but more like “*Our effort to build our own OS
> atop Android is working better, let’s go with that one.*”


I realized the next day that this wasn’t a good or fair comparison. I also realized that my description of the embedded Linux project as “Tony Fadell/Jon Rubinstein/Steve Sakoman-led” was wrong — in particular, Fadell’s role in that project.


As far as I can tell, the germ of Fadell’s supposed championing of that project was Businessweek’s 2011 profile of Scott Forstall (“[The Sorcerer’s Apprentice at Apple](https://www.bloomberg.com/news/articles/2011-10-12/scott-forstall-the-sorcerers-apprentice-at-apple)”) by Adam Satariano, Peter Burrows, and Brad Stone, [which NBC News has a non-paywalled version of](https://www.nbcnews.com/id/wbna44904886):


> Leading the other group was Fadell, who helped create the iPod.
> Another boy wonder, Fadell in 2005 had become one of Apple’s
> youngest-ever senior vice-presidents at 36. The competition,
> according to former Apple employees, turned explosive, with Fadell
> and Forstall arguing over talent, resources, attention and credit.


When I linked to and quoted from that story again last month, I omitted its inclusion of this adamant statement from Fadell, from the end of the story:


> “I inherited the competitive iPhone OS project from Jon Rubinstein
> and Steve Sakoman when they left Apple. I quickly shuttered the
> project after assessing that a modified Mac OS was the right
> platform to build the iPhone upon. It was clear that to create the
> best smartphone product possible, we needed to leverage the
> decades of technology, tools and resources invested in Mac OS
> while avoiding the unnecessary competition of dueling projects.”


[Fadell himself chimed in on Twitter](https://twitter.com/tfadell/status/1479227925476130816):


> Don’t believe everything you read, especially this post by
> @gruber. It couldn’t be farther from the truth. Typically he has
> good ones and I agree. Tried several times to contact him but…


I did get in touch with Fadell after that. But I realized I should have known better even before getting in touch with him. Apple operates in secrecy, but the origin story of the iPhone has been told [several times](https://www.amazon.com/Becoming-Steve-Jobs-Evolution-Visionary/dp/0385347421) from [several sources](http://creativeselection.io/). A very long story rendered very short: Fadell’s story adds up; Businessweek’s description of the embedded Linux project being led by Fadell does not. (Businessweek’s description of Forstall and Fadell as political rivals *definitely* adds up, though. The cutthroat internal politics of Apple under Steve Jobs — strong personalities with large egos — amidst tumultuous technical drama (see timeline below) sounds like the makings for a damn good show like *Succession*.1)


Ken Kocienda — who created the original iPhone touchscreen keyboard while at Apple and whose book *[Creative Selection](http://creativeselection.io/)* is both a compelling read and terrific historical resource — [linked to my post on Apple’s “dueling iPhone OS projects” and tweeted](https://twitter.com/kocienda/status/1479119272290832390):


> From the linked article: “Rather than pick an approach right away,
> however, Jobs pitted the teams against each other in a bake-off.”
> When people hear “bake-off” they probably imagine two teams who
> each produce a complete item for tasting and testing. That wasn’t
> the case here.
> I recall the phone OS bake-off period lasted only a scant few
> months (somewhere from 2-4?), while the whole iOS development
> cycle was just a little more than a year and a half from the
> first lines of code in UIKit to Steve Jobs holding up the iPhone
> on stage.
> Our search for a phone OS was more like dueling proofs of concept — so I agree with the DF headline. Given the timescales for a
> project as significant as an OS, the choice was made quickly, and
> as we did the follow-on work on what became iOS, we weren’t
> looking over our shoulder.


A longtime engineering source at Apple wrote to me, in private, with a link to Fadell’s tweet:


> The dueling OS thing was a common trope. Really didn’t happen that way.


Steve Jobs was famously good at picking the winning horse early. A few sources I contacted mentioned missing Jobs’s decisiveness. His good taste is famous, but his faith in his *intuition* was extraordinary too. His decision to back Forstall’s project to use Mac OS X as the basis for the iPhone’s OS was obviously correct, but also was made quickly.


It’s entirely possible that Facebook’s years-long equivocation over its AR/VR OS strategy isn’t a sign of indecision on Mark Zuckerberg’s part, per se, but rather an indicator of an industry-wide trend. A fear of shutting ideas down. That every idea should be explored in depth — why not, with so much money available to spend? FOMO, at the level of giant corporations, with trillion-dollar stakes.


But the “bake-off” period at Apple for the iPhone’s OS lasted only a few months and involved, at most, a few dozen engineers and designers. According to The Information, Facebook’s XROS project lasted over four *years* and involved over 300 employees by the time it was shuttered in November. It is interesting to compare the two bake-offs, but only insofar as how *differently* they were conducted.


Fadell was — and remains — a hardware guy, and by all accounts he led the iPhone hardware project. As a product, the original iPhone exemplified Apple’s holistic approach to hardware and software that are designed for each other, yet, at the engineering level, the iPhone hardware and software teams were almost completely siloed, with only Jobs and a handful of his most trusted (and talented) senior executives knowing the whole story.


Another source, who worked on iPod software for several years, via email:


> The iPod OS was always a mess. It was based on code from Portal
> Player, Pixo, and code we wrote, all mashed together. It didn’t
> have memory protection or separate processes, it was just one big
> ball of code, like classic Mac OS. When one thread crashed, the
> whole thing died. Schedules were always tight, and we were always
> told to do whatever was necessary to ship now, and clean it up
> later. Except later never came, and the code just became more and
> more unmaintainable.
> Apple owned the Pixo code, having bought the IP from the Pixo
> bankruptcy. But Apple and Portal Player were fighting. Portal
> Player wanted to be bigger and more successful than mere wholesale
> vendors of ARM components and supporting software. Apple decided
> to dump Portal Player, so we started removing all the PP code, and
> rewriting it ourselves.
> This opened an opportunity for the iPod Linux enthusiasts to ask
> what if we dumped the kludgy iPod OS altogether, and replaced it
> with Linux, which they kind of had running already. There is a
> certain kind of Linux enthusiast who thinks the answer to any
> technical problem can be found in Linux. There was a project to
> create a Linux iPod OS that could replace the creaky old iPod OS
> we’d been shipping. I think [Steve] Sakoman was in charge of this
> effort. They got it to a demo stage, but a realistic examination
> of how much work was involved to go from cool tech demo to
> shipping OS was discouraging. Management decided to stick with the
> devil they knew, which was probably the right decision.
> Around the same time, Apple started to develop a phone. Fadell was
> in charge of producing the hardware. He had a real knack for
> designing hardware that could be produced with high yields. Fadell
> had designed the original iPod for ease of manufacturing, and it
> had some of the highest yields of any hardware Apple ever built,
> which translates into high profits.


---


As best I have been able to put it together, a rough timeline of the creation of the original iPhone goes something like this:

- **Early 2004:** Apple commits to collaborating with Motorola, and eventually Cingular, for what will become [the ill-fated Rokr](https://daringfireball.net/linked/2009/09/20/cnet-rokr-video), a phone designed and developed by Motorola with support for music from the iTunes Store. (But not over-the-air downloads or purchases!) Jobs’s thinking at the time was that they didn’t want to make a phone themselves because he didn’t think Apple could do it *their* way, building exactly the phone they themselves wanted to build, because of the complete control exerted by the carriers over every detail related to handsets. But, Apple didn’t want to lose their rapidly growing music business to music-playing cell phones. Thus the compromise: let Motorola design and make a phone that played music from iTunes. (Jobs repeatedly, [in public](http://www.brianstorms.com/archives/000574.html), [referred to the cellular carriers as “orifices”](https://allthingsd.com/20120530/steve-jobs-at-d-podcasts/).)
- **First half of 2005:** Apple, realizing just how crummy a phone the Rokr was going to be, decides to go full-speed ahead to make a true Apple phone. (See chapter 12 of Brent Schlender and Rick Tetzeli’s *[Becoming Steve Jobs](https://www.penguinrandomhouse.com/books/223401/becoming-steve-jobs-by-brent-schlender-and-rick-tetzeli-with-a-new-foreword-by-marc-andreessen/)*.) But they have no firm idea what any aspect of it would be. There was a brief bake-off between the embedded Linux project and the stripped-down MacOS project. The embedded Linux project was spearheaded by Sakoman, but had backing internally by Jon Rubinstein.2
- **June 2005:** Apple announces [the Mac’s surprise transition](https://daringfireball.net/2005/06/) from [PowerPC to Intel’s x86 architecture](https://daringfireball.net/linked/2005/06/). This wasn’t directly related to the phone project, but it emphasizes just how much was going on inside Apple at this time. Far from neglected while Apple’s senior executives were spinning up the hardware, software, and design efforts to create the iPhone, the Mac simultaneously underwent a radical architectural change that wound up propelling it to theretofore unseen popularity and success.3
- **Summer 2005:** Apple commits to Forstall’s stripped down MacOS project for the iPhone’s software, and a touchscreen-based hardware design. No click wheels, no hardware keyboard, no stylus — just a touchscreen and a few hardware buttons (home, power, audio volume). Kocienda documents this timeline in chapter 6 (“The Keyboard Derby”) of *Creative Selection* — Apple was fully committed to a software-based method of text input for the iPhone before they had any good designs for how that *might* even work. They bet that they would figure something out — and won that bet.
- **September 6, 2005:** [Apple introduces the iPod Nano, iTunes 5, and the Motorola Rokr](https://www.macworld.com/article/176908/special-4.html) at an event in San Francisco. Unbeknownst to the public — or Motorola, or Cingular — Apple was already fully committed to building its own phone. On stage demo glitches aside, it’s no wonder Jobs’s enthusiasm for the Rokr [was lacking](https://daringfireball.net/linked/2009/09/18/siegler-jobs), to say the least. He’d moved on to Apple’s own phone project months before the Rokr even got announced.
- **October 14, 2005:** [Apple announces](https://www.apple.com/newsroom/2005/10/14Tim-Cook-Named-COO-of-Apple/) Tim Cook’s promotion to COO, Jon Rubinstein’s retirement (effective March 31, 2006), and Tony Fadell’s promotion to senior vice president of the iPod division, cementing Fadell’s position in charge of hardware engineering for the phone project. (Rubinstein [joined Palm](http://www.elevation.com/EP_news.asp) as executive chairman in October 2007, and [became CEO](https://web.archive.org/web/20110725232601/http://investor.palm.com/releasedetail.cfm?ReleaseID=389058) in 2009.)
- **November 2005:** [Steve Sakoman leaves Apple](https://apple.fandom.com/wiki/Steve_Sakoman).4
- **2006: Hard work.**
- **Late 2006:** Convergence. Shortly before the holidays, the software team finally sees their work running on a prototype of the actual iPhone. (See *Creative Selection*, p. 208.) Prior to this they’d been testing their work on [bulky “Wallaby” prototype devices](https://twitter.com/kocienda/status/880451736049139712) that bore little resemblance to the actual iPhone. Presumably, most of the iPhone hardware engineering team first saw the actual iPhone software around this same time.
- **January 9, 2007:** Steve Jobs announces the iPhone at Macworld Expo.
- **June 29, 2007:** [The iPhone goes on sale](https://www.flickr.com/photos/gruber/662408737/in/photolist-21x2pn-21x23i-21x1PH/).


---


[Fadell left Apple in November 2008](https://www.theguardian.com/technology/blog/2008/nov/05/apple-ipod-inventor-tony-fadell-leaves), and founded Nest Labs in 2010. The personal animus between him and Forstall was famous within the company. The kernel of the widely held but incorrect notion that Fadell backed the embedded Linux OS project for the iPhone starts and ends with their political rivalry within Apple. If the embedded Linux project had won out, Forstall — whose expertise and experience were entirely on the Mac OS X side, [dating back to his days as an early employee at NeXT](https://www.vertexreport.com/2020/05/former-apple-exec-scott-forstall-shares-how-he-was-hired-by-steve-jobs/) — likely would have been out of the picture for the phone project, and the iPhone’s software might well have fallen under Fadell’s purview. So: Fadell and Forstall were rivals, there was a bake-off between two projects to produce an OS for a phone, Forstall spearheaded one of them, ergo Fadell must have backed the other. Sounds good. And then that one throwaway paragraph [in the 2011 Businessweek profile of Forstall](https://www.nbcnews.com/id/wbna44904886) said it was so, and a myth was born.


It even makes sense that if Fadell *had* championed the embedded Linux/iPod OS effort, that he’d downplay/retcon his role in hindsight, given how spectacularly successful the decision to base the iPhone OS on Mac OS X turned out to be. But even putting Fadell’s own version of events aside, it just doesn’t add up. Sakoman and Rubinstein, who did spearhead the embedded Linux OS effort, left Apple in late 2005/early 2006, when the iPhone project was taking off inside the company. At that same time Fadell was *promoted* to the company’s [very short list of senior vice presidents](https://web.archive.org/web/20070108222659/https://apple.com/pr/bios/) and put in charge of the iPhone’s hardware engineering. Fadell and Forstall might not have liked each other, but they were the hardware *yin* and software *yang* of the iPhone’s creation — winners both, but also neither to last long within Apple.


Two stories to illustrate their rivalry. During the introduction of the original iPhone, [Jobs demoed adding and removing contacts to the Phone app’s Favorites list](https://www.youtube.com/watch?v=0wQ7oL9pIIU) (a feature that remains largely unchanged today). The number he added was Phil Schiller’s. The number he deleted: Tony Fadell’s. [From a 2017 profile of Fadell for Wired by Adam Fisher](https://www.wired.com/story/tony-fadell-revenge-on-silicon-valley-from-paris/):


> When Jobs was demonstrating the iPhone’s contact list, he showed
> that he could delete a contact with one tap — and the contact he
> deleted was “Tony Fadell.” The public may not have thought twice
> about the gesture, but the Apple engineers in the audience
> understood exactly what was going on. “People laughed about it,
> but everybody knew,” Grignon says. “Steve was in many ways
> diabolical, and Tony and Steve’s relationship had grown
> increasingly rocky.” Fadell insists that his relationship with
> Jobs remained solid, but he seems to have been pretty decisively
> outmaneuvered. “That demo script,” Fadell says, “was created by
> Scott Forstall.” (A source closely involved with the presentation
> says Jobs was ad-libbing.)


I can’t verify that Forstall created the demo script (or even just that part of it), but my understanding, from several sources, is that nothing in that demo was ad-libbed by Jobs. In January 2007, iPhone OS was still buggy enough — [and incomplete](https://web.archive.org/web/20070120225408/http://www.suntimes.com/technology/ihnatko/215441,CST-FIN-Andy18.article) — that *nothing* was left to chance in the demo. Even with Jobs following the demo script to a T, most engineers who worked on the iPhone were surprised, or at least greatly relieved, that it never once crashed on stage. That it was Fadell’s contact that Jobs removed from his Favorites list might have been nothing more than a subtle jab from Forstall, but it wasn’t just Apple engineers in the audience who noticed. There could have been a fictional “Johnny Appleseed” contact in the list for Jobs to delete, but there wasn’t.5


On the flip side of the iPhone’s January 9 introduction is this story about the iPhone’s launch day on June 29, from Fred Vogelstein’s 2013 book *[Dogfight](http://www.fredvogelstein.com/)* (p. 80):


> Apple helped create and then took full advantage of all the hype.
> On launch day it sent top executives to various stores in big
> cities to witness it all and help whip up the crowds. Head of
> Global Marketing Phil Schiller went to Chicago. Jony Ive and his
> design crew went to San Francisco.
> Steve Jobs’s store was, naturally, the one in downtown Palo Alto
> at the corner of University Avenue and Kipling Street. It was a
> mile and a half from his house and he often showed up there
> unannounced when he was in town. The appropriate high-tech
> luminaries had already gathered when he arrived. Apple cofounder
> Steve Wozniak and early Apple employees Bill Atkinson and Andy
> Hertzfeld were already standing on line. But it also seemed as if
> Jobs had some internal flames to fan of his own, said one of the
> engineers who was there along with Grignon and many others who had
> worked on the project, including Fadell and Forstall. “So there’s
> this reunion of the original Mac guys, and it’s really cool. And
> then Steve goes up to Tony [Fadell] and proceeds to go over in a
> corner of the store and talk to him for an hour and ignore
> Forstall just to fuck with him.”
> “Up until that day, for the previous six months, everything had
> been Tony’s fault. Any hardware problems or ship delays or
> manufacturing problems — all Tony’s fault. Scott could do no
> wrong. But that was the day the press reviews came out, and the
> iPhone’s email [software] wasn’t working for people, but
> everyone loved the hardware. So now Scott was the bad boy, and
> Tony was the golden boy. And it was funny, because Steve did it in
> a way in which his back was to Forstall so that Tony got to look
> at Scott while it was all happening. I’m not joking. The look on
> Scott’s face was incredible. It was like his daddy told him he
> didn’t love him anymore.”


That’s one story, from one book, attributed to one unnamed engineer, but — well, Jobs *was* mercurial.


One final anecdote, from the same source I quoted above, who worked at Apple for several years as an iPod software engineer:


> Rubinstein was perfectly nice to working engineers at my level,
> but I’m sure he was ruthlessly effective with his peers. I
> remember we were late shipping the iPod one year, there was a bad
> cache control bug that we just couldn’t track down. It was
> Saturday night at midnight, and the building was full of engineers
> trying to track down this bug. Ruby comes walking down the hall,
> poking his head into offices, casually asking what progress we’re
> making. I’m sure he was getting intense pressure from Steve to
> ship the thing, but having your senior VP watching over your
> shoulder as you debug is not helpful. He was smart enough to
> realize this, and left.
> Fadell was different. His ambition was too obvious. He didn’t
> suffer fools. If you disappointed him, you wouldn’t get a chance
> to ever disappoint him again. Fadell and Forstall butted heads,
> and Forstall won. Fadell left Apple.


---

1. Presumably, such a show would not be on Apple TV+. But it would be pretty bold if it were — unbowdlerized. ↩︎
2. There were also early hardware prototypes with an iPod-style click wheel, [but that idea was abandoned rather quickly](https://www.theverge.com/2017/1/11/14240918/apple-interview-ipod-iphone-prototype-tony-fadell). Not only could Apple find no good way to type text using a click wheel, there was no good way to even dial a phone number — which, at the time, was considered the most essential task for a cell phone. ↩︎︎
3. For Steve Jobs in particular, this period was even more unbelievable when you consider that he was in the midst of contentious negotiations with Disney over the development and distribution of future Pixar movies (negotiations in which Disney already owned the rights to the pictures Pixar had already made — Jobs was negotiating with a figurative gun being held to the heads of Buzz and Woody). Bob Iger took over as Disney’s CEO in September 2005, replacing Michael Eisner ([whom Jobs despised](https://medium.com/mind-cafe/disneys-ceo-dug-his-own-grave-with-the-delusion-of-power-1c3e7ce5d5a0)). In January 2006, [Disney acquired Pixar for $7.4 billion](https://money.cnn.com/2006/01/24/news/companies/disney_pixar_deal/). ↩︎︎
4. Sakoman had a fascinating run, and was clearly a visionary regarding handheld computing. [He started and led Apple’s Newton project](https://gizmodo.com/the-story-behind-apples-newton-5452193) in the late 1980s. [He co-founded Be with Jean-Louis Gassée](https://mondaynote.com/50-years-in-tech-part-15-be-from-concept-to-near-death-f69c64d8725e) after both of them left Apple in 1990. Sakoman wound up at Palm when they acquired Be in 2001, then rejoined Apple in 2003 and was an early adamant proponent of Apple making its own phone. After retiring from Apple in late 2005, though, he seemingly dropped off the map. ↩︎︎
5. The full list of Jobs’s demo favorites, in order, before adding Schiller (and moving him to the top of the list to demonstrate drag-and-drop reordering): Scott Forstall, Bertrand Serlet, Eddy Cue, Tony Fadell, Jony Ive. Curiously absent: Tim Cook. Fadell’s removal may or may not have been a subtle sign of his waning political status within Apple, but Cook’s omission certainly was not. [Jobs had put Cook in charge of day-to-day leadership of the company in 2004](https://www.sfgate.com/news/article/Apple-s-Jobs-has-cancerous-tumor-removed-He-ll-2736823.php) while he recuperated from his surgery for pancreatic cancer, and, last I checked, Cook’s stature within Apple remains high to this day. ↩︎︎



| **Previous:** | [My 2021 Apple Report Card](https://daringfireball.net/2022/02/my_2021_apple_report_card) |
| **Next:** | [Twitter’s Confusing New, but Hopefully Now Abandoned, ‘Home/Latest’ Timeline](https://daringfireball.net/2022/03/twitter_bananas) |


PreviousNext