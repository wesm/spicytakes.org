---
title: "Why Is Adobe Soundbooth Intel-Only?"
date: 2006-11-02
url: https://daringfireball.net/2006/11/soundbooth_intel
slug: soundbooth_intel
word_count: 3287
---


Last week, Adobe released a public beta of a new sound editing application for Mac OS X and Windows, [Soundbooth](http://labs.adobe.com/technologies/soundbooth/). Curiously, the Mac version *only* runs on Intel-based Macs.


## A Wee Bit of Technical Background for Non-Developers, With the Goal of Explaining the Difficulty of Developing for Multiple Computer Architectures, but Which Will Be Kept Relatively Brief Because Wikipedia Has Excellent Entries on All This Stuff


A computer processor reads and executes instructions in *machine code*. An instruction might be to store a certain value on a [register](http://en.wikipedia.org/wiki/Processor_register) (a register is a small amount of very fast memory), or to add the values of two registers. Modern processors execute billions of instructions *per second*.


Machine code is, even for most programmers, inscrutable. Almost no one writes machine code by hand, even though machine code is the *only* thing a computer processor accepts as input. [Assembly language](http://en.wikipedia.org/wiki/Assembly_language) is a low-level language that, more or less, is a more human-friendly syntax for machine code. Today, very few programmers write assembly language, but it *is* still used for code where every last ounce of efficiency is needed.


One problem with assembly language is that it’s hard. And even if you’re a gifted enough programmer that you don’t find it hard, it’s certainly tedious — there are few conveniences or shortcuts and no abstractions. Another problem is that each family of computer processors uses a different *instruction set* for its machine code, and, therefore, a different assembly language. So, for example, the Motorola 680x0 family of processors — the ones used by the original Macintosh — understands its own brand of machine code. Machine code for the 68000 processor could run on the 68020 and 68030, but it couldn’t run on, say, the x86 family of processors from Intel.1


But most programmers don’t write assembly language, they write in higher-level languages like C, C++, and Objective-C. A *compiler* is what turns C code into machine code. If you write portable C, where by “portable” I mean code that doesn’t rely on proprietary or non-standard APIs, you can simply recompile the same code using a different compiler to produce machine code for a different processor. This is how most Unix software works, actually. You download an archive of C code, compile it, and it should “just work”, no matter which type of processor your system is using.


The trick with universal binaries is that the GCC compiler at the heart of Xcode is now capable of producing executable files that contain *both* PowerPC and x86 machine code, and the Mac OS X kernel knows which half of a universal binary is the one meant for your computer.


Another low-level problem is that of [endianness](http://en.wikipedia.org/wiki/Endianness). Read the Wikipedia entry for details, but a nutshell description will suit us just fine. Some processor architectures are big-endian, including the PowerPC and Motorola 68000 families. Others are little-endian, most notably the Intel x86 family. The difference is the order in which bytes are arranged in a multi-byte sequence; on a big-endian system bytes are ordered from most to least significant; on a little-endian system, they’re ordered from least to most significant. Wikipedia uses the analogy of the difference between left-to-right languages like English and right-to-left languages like Hebrew — neither is more efficient than the other, it’s just an arbitrary decision.


But dealing with endianness-related issues is tricky — unlike English and Hebrew, which are easily identified at a glance, bytes are just sequences of ones and zeroes. You can’t just look at a chunk of bytes and know their endianness. In some ways it’s more like telling the difference between ambiguous date formats — “1/2/2006” means 2 January 2006 in the U.S., but means 1 February 2006 in Europe. You can’t tell what the intent is just by looking at “1/2/2006”.


Differences in endianness can lead to problems when software makes assumptions about byte order. If your software assumes big-endian byte order, and you recompile for a little-endian architecture like x86, the software won’t work as intended.


Apple’s switch from PowerPC to Intel processors meant that Mac developers had to deal with both these issues: a new instruction set for software machine code, and a different endianness. When Apple switched from 68000 processors to the PowerPC in the 90s, developers only had to deal with the new instruction set — both of those architectures are big-endian.


## Regarding Soundbooth and the Difficulty of Producing Universal Binaries


One source of problems some Mac developers faced (and in certain notable cases, still face) moving to universal binaries is that you need to use GCC as your compiler. Large software products written using CodeWarrior couldn’t just be recompiled as universal binaries — they first needed to be migrated from CodeWarrior to Xcode. For huge projects like, say, Microsoft Office and Adobe Creative Suite, this migration, in and of itself, is a huge task.


Other potential problems include endianness issues and processor-specific assembly code. In most cases, you can simply recompile C code to produce machine code for a different instruction set, but you have to completely rewrite any assembly code (the same goes for code that targets processor-specific extensions like the PowerPC’s [AltiVec](http://en.wikipedia.org/wiki/AltiVec)).2


So, Mac developers who were already using Xcode, and whose code made few, if any, assumptions about endianness, were generally able to produce universal binary versions of their software in short order: a few days for something beta quality, a few weeks for something tested and vetted. Developers still using CodeWarrior had a longer haul in front of them.


But these are the problems facing developers of *existing* PowerPC-only Mac software. Developers of *new* software, started after the Intel announcement at WWDC 2005, already know the deal: use Xcode, and don’t make assumptions about the underlying processor architecture. The way Apple has set things up with Xcode, once you’re compiling a universal binary, it’s not that much more work to keep producing universal binaries than it would be to produce binaries for a single architecture.


That’s what makes the Intel-only requirement for Soundbooth so curious. The only other Intel-only Mac apps I’m aware of are things like [Parallels Desktop](http://www.parallels.com/en/products/desktop/), and it’s obvious why Parallels only works on Intel-based Macs — what it does is host, in a virtual machine, other operating systems that are compiled for x86-compatible processors.


A few Adobe employees have offered explanations for this, but none of them are satisfying. [In a forum post](http://www.adobe.com/cfusion/webforums/forum/messageview.cfm?forumid=72&catid=619&threadid=1208711&enterthread=y), Peter Green, a program manager for Adobe audio applications, wrote:


> It actually would have been very expensive for us to support both
> PPC and Intel Mac. We would have no application to show today had
> we decided to do this.
> From a coding standpoint, the architectures and environments
> needed nearly double the time it takes to write, build, integrate,
> and test.
> From a testing standpoint, again, the time is nearly doubled to
> check everything in both platforms.


Writing, building, and testing are very different tasks. It *does* take double the time to build (a.k.a. compile) a universal binary, because the compiler needs to generate machine code for both architectures. But, during development, programmers using Xcode can compile development builds, not meant for distribution, which target only their native architecture. I.e. if you’re writing code on a MacBook, you can compile development builds that only contain Intel-specific code. You only need to compile a full universal binary when you compile a production build of your software.


In short, increased build times do not seem to be a problem for any other Mac developers. A minor inconvenience, at worst.


Testing a universal binary also takes more time than testing a single-architecture binary. A good testing process should now include some sort of checks for endianness-related bugs, for example. But *double*? No developers I know agree with this assessment.


And then there’s writing code. If Soundbooth is written entirely in standard C or C++, and they’re using GCC, no extra writing is necessary: the same C code can be compiled for both architectures.


Those are two big *if*s, though. My best guess is that Soundbooth is *not* written entirely in standard C or C++, but instead, that parts of it are written in x86 assembly and/or that parts are vectorized, with C code written specifically for the Intel [SSE instruction set](http://en.wikipedia.org/wiki/Streaming_SIMD_Extensions). (SSE is Intel’s rough equivalent to the PowerPC’s AltiVec — same basic idea, and suited for the same general problems, but totally different from a programming source code level.)


x86 assembly and SSE-specific C code cannot simply be recompiled for PowerPC.


If it’s not that, though, it’s something — because the simple explanation that developing universal binaries takes double, or even *nearly* double the time, just isn’t true for most applications.


## Adobe’s Explanations


The worst explanation I’ve seen from Adobe regarding Soundbooth’s lack of PowerPC support is from Adobe program manager John Nack, who [wrote a weblog entry on the topic](http://blogs.adobe.com/jnack/2006/10/why_no_powerpc.html):


> Here’s the reality: Apple’s migration to Intel chips means that
> it’s easier to develop for both Mac and Windows, because instead
> of splitting development resources optimizing for two different
> chip architectures, you can focus on just one.  That’s all good,
> and it makes Mac development more attractive.


Easier cross-platform development is certainly of interest to Adobe, but it’s not something most Mac users care about. This translates to “we’re too lazy”. I don’t think that’s the case — that Adobe’s engineers are too lazy — but that’s what this excuse sounds like.


> Now, if you were Adobe and had started developing a new
> application at exactly the time when Apple told you, “This other
> chip architecture is dead to us,” would you rather put your
> efforts into developing for that platform, or would you focus
> elsewhere?


Perhaps Nack should ask the Lightroom team?


I don’t mean to be cute here, but, seriously — Nack’s remarks seem to imply that it’s an obvious decision for Adobe to develop a brand-new media-editing Mac app as Intel-only, when Lightroom — which is a universal binary — is right there as existence proof to the contrary. Lightroom also refutes Nack’s notion that Adobe customers are unreasonable for expecting new software to still support PowerPC.


I also think it’s somewhat disingenuous to say that Apple’s take on the PowerPC is that it was “dead to them”. They were selling PowerPC-based systems up through August of this year. I don’t think the PowerPC is any more “dead” to Apple than the G3 was when they switched to an all-G4 line-up. I’m not saying Apple is planning to jump back to the PowerPC any time soon — but I don’t think it’s entirely impossible, either. I think the lesson Apple tried to impart upon developers is *not* to think of the Mac, or Mac OS X, as being targeted at a single computer architecture.


Nack writes:


> If you’re a Mac user, I think it’s important to ask yourself,
> “Would I rather encourage software developers to bring their
> titles to the Mac, or would I rather jump down their throats given
> any opportunity?  If Adobe were to bring other Windows-only apps
> to the Mac, would I be happy about that, or would I rather give
> them hell for focusing on features & functionality rather than a
> discontinued chip architecture?”


This is a little insulting — and defensive — if you ask me. First, the beginning is a classic [straw man](http://www.crazyapplerumors.com/?p=664) argument. Clearly there are other options than “encouraging software developers to bring their titles to the Mac” and “jumping down their throats given any opportunity”. That’s a little close to “If you’re not with us, you’re against us.”


Second, it implies that Mac users should be grateful that Adobe is developing Mac software. News flash: the [Mac is doing great](http://www.apple.com/pr/library/2006/oct/18results.html). You either see the value in developing Mac software or you don’t, but Mac users aren’t going to thank you just for developing Mac software at all.


Third, calling the PowerPC a “discontinued chip architecture” isn’t false, but it’s certainly slanted. It’s also true to call it “the $3000 Power Mac G5 I bought just a few months ago”. Now, it’s not like G5-based Power Macs were burning up the sales chart in 2006, but they *were* selling fairly respectably, considering the writing on the wall.


The irony here is that many of the people buying these recent Power Mac G5s did so because they’re creative professionals *who use Adobe software* — software that doesn’t run natively on Intel hardware and isn’t going to until sometime in 2007. I.e., Adobe, more than any other software developer, is responsible for creative professionals buying late-model high-end PowerPC hardware.


The news that Apple was switching to Intel x86 processors is a year and a half old. But there are excellent, high-end Power Macs that were sold just a few months ago. It’s not the least bit ridiculous for PowerPC-owning Mac users, especially those with G5s, to expect their computers to remain fully viable for the next few years.


The point isn’t that Adobe is *obligated* to include PowerPC support in Soundbooth — but it certainly isn’t unreasonable to ask why it doesn’t.


On the flip side, the best answer from Adobe to date is from Soundbooth product manager Hart Shafer. Shafer, responding to a commenter on Nack’s weblog entry who wonders why Adobe can’t just “flip a checkbox in Xcode” to generate a universal binary, writes:


> As I said originally, we really wanted to make a PPC version but
> the “make universal” checkbox simply wouldn’t work for us. If it
> would I’d be in there yelling for our engineers to check it and
> get me a PPC version — I’m not in the habit of passing up
> potential customers! However, as has been pointed out elsewhere
> we have buckets of Intel-specific code for modules in Soundbooth
> that would all have to be re-written to work on PPC chips. The
> spectral view and the edits you can do there are a good example
> of something that could work on the PPC but would be so dog slow
> as to be worthless without this kind of work. We leverage this
> sort of Intel expertise all over the application.


Shafer isn’t saying what exactly it is about this code that is “Intel-specific”, but the plain statement that they have “buckets” of existing Intel-specific code that would have to be rewritten to achieve non-“dog-slow” performance on PowerPC suggests that it’s not an issue of code that makes assumptions about the endianness of the underlying architecture. That means either x86 assembly code, SSE vector code, or both. My guess is SSE code, but that’s just a guess.


[**Update:** Soundbooth is apparently based in large part upon code from Audition, Adobe’s Windows-only sound editing application, and whose [system requirements](http://www.adobe.com/products/audition/systemreqs.html) clearly indicate that it requires an SSE-enabled processor.]


Shafer continues:


> Even if we could check the box to produce a PPC version, and
> dedicate engineers to re-write all that Intel-specific code, most
> people don’t consider the impact that has on testing and quality
> assurance — which is a non-trivial part of getting a release out.
> (Just ask our QA team who worked through the weekend tracking
> down issues to get the public beta out last week). A different
> chip architecture means a different test bed, which in turn
> means a lot of additional testing time.


Two points: (a) this don’t seem to be stopping anyone else from producing universal binaries, including audio editors ranging from Apple’s own [Soundtrack Pro](http://www.apple.com/finalcutstudio/soundtrackpro/) (part of the $1,300 Final Cut Studio) to consumer-level editors like [Rogue Amoeba’s $32 Fission](http://rogueamoeba.com/fission/); and (b) it doesn’t seem to be stopping any other teams at Adobe from producing universal binaries.


The question is, what’s different about Soundbooth than Lightroom? They’re both new, they’re both cross-platform, and they both deal with computationally intensive media. One difference is that audio has stringent real-time requirements — you can pause or hiccup briefly while displaying or processing photographs, but you can’t while playing back audio. So let’s just give them the benefit of the doubt and assume that Soundbooth requires low-level architecture-specific optimizations that Lightroom does not.


Well, so what? I’m not saying there isn’t hard work involved. Isn’t that Adobe’s job? Or, rather, isn’t that the job of Adobe’s engineers? To write difficult code? All these excuses about how much extra work PowerPC support would entail might resonate more deeply if it weren’t for the fact that Adobe’s Soundbooth team is the only one making them.


I asked Paul Kafasis, “CEO / Lackey” of Rogue Amoeba Software, how much work it was to make Fission a universal binary. He said, “We all had PowerPC code that got rewritten and it’s not *that* hard, it’s just time-consuming. Rogue Amoeba has six people, and we managed to port from one platform to another. Adobe has almost 6,000 people and they can’t pull it off?”


You might argue that comparing Fission to Soundbooth isn’t fair — that Fission, as a consumer- or low-end-prosumer-level iApp-ish application, is far less complicated or intensive than Soundbooth. But I’d argue that the comparison is completely fair: however less complex Fission is than Soundbooth is more than compensated for by how much larger a company Adobe is than Rogue Amoeba. (I’d also argue that it’s hard to design an application that makes audio editing seem simple.)


What galls is that this is a *marketing* decision, but the explanations from Nack and Shafer are attempts to cast it in technical terms. *We have so much existing Intel-optimized code! We’d have to do more QA testing! It would take a few more weeks before we could ship!* What it boils down to is this: Adobe doesn’t see Power Mac G5 users as being worth supporting. We’re not talking about support for *older* PowerPC systems, or even not-really-that-old but comparatively slow G4 systems, such as PowerBooks; we’re talking about support for the G5 systems that are indisputably capable of providing good performance for professional audio editing.


Kafasis said, “From a pointy-haired boss point-of-view, I can see how you might simply say ‘ditch PowerPC support’ — it’s losing users every day, as Intel gains them. But if you know anything about the Mac platform at all, it’s far too early to be doing it. The goodwill you would gain (or at least, not lose) from creating universal would more than pay for the time and energy expended in supporting PowerPC.”


I’d argue that it’s more than goodwill — that it’d be good *money*, too. That’s what makes this decision so perplexing: if there aren’t enough G5 users to make it worthwhile for Adobe to add PowerPC support to Soundbooth, why are so many people complaining about it?


---

1. The reverse wasn’t necessarily true, however. Code written specifically for a newer processor, such as the 68030, might contain new instructions not available in older processors like the 68020 and 68000. Like with modern apps that will run on a G5 or G4, but not on a G3. ↩︎
2. It’s also worth pointing out that when moving from one compiler to another, like, say, from CodeWarrior’s compiler to GCC, you might not be able to simply recompile your C/C++ code, either. Different compilers support mildly different variations of C and C++ syntax; wise programmers tend to write code that should pass through *any* compiler without warnings and avoid compiler-specific language extensions. ↩︎



| **Previous:** | [Can I Get an ‘Hallelujah’ for Auto-Completion With the Esc and F5 Keys?](https://daringfireball.net/2006/10/hallelujah_autocompletion) |
| **Next:** | [Stikkit](https://daringfireball.net/2006/11/stikkit) |


PreviousNext