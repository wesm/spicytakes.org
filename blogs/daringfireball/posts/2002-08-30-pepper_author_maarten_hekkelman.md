---
title: "Pepper Author Maarten Hekkelman"
date: 2002-08-30
url: https://daringfireball.net/2002/08/pepper_author_maarten_hekkelman
slug: pepper_author_maarten_hekkelman
word_count: 5791
---


Maarten Hekkelman is the programmer behind Pepper, a Macintosh programmer’s text editor that started life on BeOS as Pe. Two weeks ago, the 36-year-old resident of the Netherlands [called it quits](http://www.whiterabbits.com/MacNetJournal/2002/08/17.html#a1976), and announced that he was no longer developing or selling Pepper. The Daring Fireball interviewed Mr. Hekkelman via email — who better to interview the author of a Mac text editor than someone who used to work for Bare Bones Software?


---


**John Gruber:** Let’s start with the news. According
	to your web site ([http://www.hekkelman.com/](http://www.hekkelman.com/)),
	you are no longer taking orders for Pepper, the text editor you’ve
	been working on for several years. In fact, it is no longer even
	available for download, except for registered users.


What happened? It seems like an awful lot of work to abandon.


**Maarten Hekkelman:** It is. It took me some six years
to develop what has become Pepper. Pepper started life as Pe on BeOS
and was ported to Mac OS [beginning with Pepper 3.0].


Frankly, I was very disappointed by Mac OS X and so [for version 4.0] I
decided to do a port to Windows. The code was already quite portable
but now I separated Pepper’s code from the more generic code. I had
used [
PowerPlant](https://web.archive.org/web/20030622050209/http://www.metrowerks.com/MW/Develop/Desktop/PowerPlantMac.htm) for the first Mac OS port and now I started replacing
PowerPlant with my own framework. I got help from an old friend, Bas
Vodde, who helped me get up to speed on Windows (I had never programmed
for that OS before). It took me nine months to finish Pepper 4.0 for
Mac OS and Windows, and a Linux version was released a couple of months
later.


But Pepper 4.0 was not well received. The first releases had some
performance issues and people blamed it on going cross platform.
However, most of the performance problems were related to fixing bugs
internally and were not at all related to the platform switch.


The negative feedback spread around; on VersionTracker there were many
complaints, and this influenced sales. And then Pepper’s serial
number was cracked, I got my first fraud cases, had a quarrel with
Tucows, and Pepper didn’t run on Jaguar and then I gave up.


So Pepper 4.0.6 does not run on Jaguar?


Nope, sorry.


Pepper 3.0 debuted for the Mac in July 2000, only a few months before
	the first public beta of Mac OS X, and only 8 months before the
	release of Mac OS X 10.0. Did you ever consider dropping support for
	the old Mac OS, and making Pepper only for Mac OS X?


No. First of all, Pe was already written in C++ and so the choice for
PowerPlant to replace the BeOS API was obvious (in my eyes). And then,
although I did have the Mac OS X betas at the time, they were not very useable.
And I simply don’t like Cocoa and would never program in it, since it
is a Mac-only technology and I don’t like to be locked in.


Do you think most of Pepper’s users are using Mac OS X?


No, I think it is more like 50/50. No hard figures though.


That’s interesting. I really thought Pepper appealed more toward Mac
	OS X users. For one thing, on Mac OS 9, Pepper’s Perl filters
	require MPW ToolServer, whereas BBEdit works with the MacPerl
	application (which is much easier to install than MPW).


I always used it on Mac OS 9 and it is a very good editor on that
platform, if I may say so.


I didn’t mean to imply that it wasn’t good on Mac OS 9, only that I
	thought the market opportunity was on Mac OS X. When people switch
	to a new OS, they are suddenly in the market for all sorts of new
	software.


I know you didn’t mean that. And you’re right with your ideas.


What was the argument with [Tucows](http://www.tucows.com) about?


They refused to list Pepper [on the grounds that] it wasn’t good enough. I changed some things
and resubmitted. Then I bought an InDepth review in the hope this
might help get Pepper listed. But the reviewer didn’t get Pepper to
run on the machine he wanted to test it on. This ended up in mud
wrestling since eventually I wanted my money back and they refused.


I must admit that I’m very unfamiliar with Tucows (I haven’t used
	Windows in about six or seven years). Do you mean that to get listed
	on Tucows you need to pay them to review your software? Seems like
	it would be hard for them to be objective in such a case.


You can buy bonus points and they will be added to your product’s
rating. So yes, you have to buy your listing. But since they have such
power [in the Windows community] they can do this.


What effect do you think having the serial number cracked had on
	sales? I often wonder whether the people who use illicit serial
	numbers would have bought the software anyway.


No effect at all. But it hurts very much, especially if you work so hard to
make something and price it so low everyone should be able to pay for
it.


Indeed, I always thought Pepper had a very low price.


Too low, far too low. But I was hoping this would help make it more
popular. And on Windows prices are all in this range. It would have
been strange to sell Pepper for Mac OS for US$100 and Pepper for
Windows for US$30, only to have comparable prices to the competition.


There are several dozen low-cost shareware “text editors” and “HTML
	editors” for the Mac, many of them built with REALbasic. For the
	most part, they offer very few features which do not come for “free”
	with the REALbasic application framework. Did you ever wonder if the
	existence of all these crappy text editors made it harder for Pepper
	to gain attention? In other words, people may have seen the
	announcement for Pepper, and thought “Oh, another piece of crap,”
	without downloading and trying it out?


No, the tragedy with Pepper was that eventually it was well known and a
lot of people were tracking it with VersionTracker. But many decided
that this version wasn’t good enough yet to dump BBEdit and start
using Pepper.


I received very few negative reactions to my decision to stop
developing Pepper, and all came from people who hadn’t yet bought
Pepper but were hoping to do so in the future.


Your own description of Pe admits that it was “inspired by MPW and
	BBEdit — both editors on Mac OS”. Were you a full-time Mac developer
	before switching to Be? Which was your primary editor on the Mac?


I’d had a couple of full time Mac programming jobs at the time. And
when working on Mac OS I used Codewarrior for programming. I did have a
license for BBEdit and tried to use it from time to time, but in my
eyes it didn’t have enough extra to make it worthwhile to use it as
an external editor [for CodeWarrior].


I also used MPW from time to time, same story here. BBEdit did have
a worksheet, but it didn’t work as nicely as it could have.


Have you used BBEdit 6.5? Its new worksheet for Mac OS X is very nice.


No, I only use Macs if I have to. And I stopped looking at BBEdit
since I found so many of the features I had come up with.


## BeOS vs. Mac OS X


The BeOS generally earned positive reviews, but never gained enough
	users to achieve critical mass. When did you start using the BeOS, and
	why?


I read about it when they first made their OS public and was
immediately hooked. A GUI and a POSIX layer combined in one machine
and with multiple anything as well! Great. Several months later, in
1996, I read about it again and decided to take the risk. I went to
the bank to get a loan to buy a BeBox. Never regretted it, life was
wonderful then.


Be, the company, seemed to have the strategy to market their OS (and
	their BeBox computers) towards developers. One of their main marketing
	points was that the BeOS had a very powerful, easy-to-use programming
	API — and that the API was designed from the ground up to be
	object-oriented, and therefore wasn’t built on a legacy procedural API,
	like the Mac OS or Windows. What was your experience programming for
	BeOS? How did it compare to programming for the Mac OS at the time?


Programming for BeOS was simple when you just started. But it became
quite messy quickly. The problem is the multi-threading. As long as you
have one window doing the job there’s no problem, but try to display
one document in more than one window and you’re in trouble. This was
the reason why Pepper was never ported back to BeOS.


The API was nice though. Comparable with PowerPlant on Mac OS.
(PowerPlant is better though.)


On the surface, BeOS and Mac OS X sound somewhat similar. They both
	have underlying Unix/POSIX layers, but both have GUI’s that are
	designed to be cohesive and intuitive. Both are popular with hackers
	who like the programming power of a Unix-style command line, but
	also appreciate a well-designed GUI interface. What did you like
	better about BeOS compared to Mac OS X?


Almost everything. BeOS was fast, extremely fast. It was new, fresh,
etc. I can only think of very few negative points, technically, in
BeOS. The ugly GUI might be one of them, the absolute need to use
multi-threading might be second.


Mac OS X, however, loses on all fronts. It claims to be a Unix but it
doesn’t support much of the more advanced Unix features, since it is
using such an old kernel. It claims to be user friendly, but I find it
more obscure and difficult to use than my Win2K box. And then it is
dog slow.


And since the Mach kernel is a personal project of [Avie Tevanian](http://www.apple.com/pr/bios/tevanian.html), it
	doesn’t look like that will ever change.


Yup. Too bad. I had a couple of cool features in Pepper for
Linux/FreeBSD but couldn’t port them to Mac OS X since the kernel
did not support them.


What features?


Redirecting a pipe to a new window in Pepper. It works in Mac OS X now
(well, 10.1.x) but works much better and nicer on a real Unix using
SVR3 style RPC calls. There were several other features. One thing I
miss dearly on Mac OS X is the /proc file system. I have been thinking
about writing a debugger for Mac OS X but this omission made me decide
against it.


Did you always have it mind that you might one day port Pe to the Mac,
	or did you only consider that after the BeOS was discontinued?


No, not when I started it. When I returned to the Mac I started using
BBEdit and CodeWarrior first, but I missed so many features I had
implemented in Pepper that I decided to simply port it.


Why go back to the Mac instead of Windows with Pepper 3.0?


At the time I was a true believer. I had hope that a Mac OS would appear
that would be as great as BeOS. Besides, I was one of those Microsoft bashers
at the time.


How are you disappointed by Mac OS X? As a user, as a developer, or both?


As a user, I don’t like it. God knows I tried, really hard, honest.


What counts for me are the details, and they were all wrong. I found
so many UI errors in OS X, I couldn’t believe it. A huge amount of work
that went into designing the ultimate GUI was thrown away and all we
got back was a bag full of candy that was dog slow.


And as a developer I hate it. I had to use Carbon of course, and it
sucks, too many changes, too many bugs. Pepper stopped working on 10.2,
because in Jaguar your Carbon event handlers have to be reentrant …
ridiculous.


It seems like you went back and forth quite a bit on Pepper’s
	underlying text rendering engine — using [ATSUI](http://developer.apple.com/intl/atsui.html) in the
	initial release of Pepper 4.0, then making ATSUI optional.
	Was	that where the performance problems were?


ATSUI is slow, really slow. I implemented the QuickDraw option in
later 4.0.x releases to illustrate this. But the biggest problem
performance-wise in Mac OS X is scrolling. It is really absurd how much
time that takes.


However, some of the performance problems were my own fault, I should
have profiled more cases like huge files and thousands of changes in
such a file. Pepper uses a sophisticated transaction mechanism to
store edit changes and I screwed up making Pepper work better with
mixed line endings.


Was this problem introduced between 3.6 and 4.0? Is this fixed in
	version 4.0.6?


It was introduced in 4.0. I wanted Pepper to be more robust with
incorrectly formatted UTF8 files, for example. And yes, most of it is fixed. At
least in the copy I’m using :-)


ATSUI is a Mac-only technology. What did you use for text rendering
	on the other systems?


Glad you asked. On other OS’s you simply use the default Text API, on
Mac OS you have to create kludges to work around the very poor text
support. I really don’t understand why Apple was so stupid. They could
have introduced a single new scriptcode to render Unicode using
QuickDraw and life would have been great. But no, Apple came up with
ATSUI, which is nice for a typographer but a horror for an editor
programmer.


And it is slow as well.


And you didn’t uncover these performance problems in beta testing?


No. I didn’t open 100+ MB files very often. Now I do, with my new job.


How many beta testers did you use? How did you recruit testers for
	the new platforms supported by Pepper 4.0?


I had some 20 beta testers. Far from enough, and although I appreciate
very much what they did, they weren’t exactly very useful when it
comes to real beta testing. They did provide good ideas though.


I hardly had any beta testers for the other platforms.


Public beta tests seem to have gained a lot of popularity in the
	last 10 years or so, especially amongst smaller developers. What
	are your thoughts on public beta testing?


I’m sorry I have to say, but most people asking to become beta testers
are only hoping for free software and never give feedback. There are
a few testers who are very good and vocal, you have to be good to
them. But in the end, they hardly find any serious bugs and that’s not
strange. They often use a subset of the features and those are often
well-tested. It is the more obscure features and details where the bugs
linger. The only way to test software is to use it yourself or to make a
test plan and hire a company to do the testing for you.


Why replace PowerPlant? Because you didn’t like it, or because you wanted to
	go cross-platform?


I wanted to go cross-platform. And I didn’t like some of the PowerPlant
implementations, I thought it would be more efficient to use Carbon
Events more extensively. My mistake.


How much of Pepper’s source code is shared across the different
	versions, and how much is platform-specific?


Pepper consists of about 160,000 lines of code. 15,000 is Mac OS
specific, 12,000 is Windows specific and 7,100 is X11. The rest is OS
neutral.


What’s your opinion on the development tools and API’s for Windows?


I’m using CodeWarrior on Windows, CW5 to be precise. It is a bit
outdated but since is still works and CW is so awfully expensive I
never upgraded. Microsoft delivers a very, very good set of
documentation and tools for developers. For free. It was a real
eye opener to have such great documentation so easily available.


I did try some other tools on Windows like [BoundsChecker](http://www.activexcatalog.com/html/boundschecker.html) from Numega,
a bit like SpotLight on Mac OS but much better. But I didn’t buy it
since it was also very expensive.


Windows is like heaven to a programmer. There are so many tools to
chose from and the documentation is wonderful. I think the API’s are on
average very good. There are some API’s I simply don’t understand, like
the one to support inline input, but those are the exceptions.


## Porting to Windows and Linux


I have to admit your decision to port Pepper 4.0 to Windows surprised me. I had expected that
	Pepper 4 would still be only for the Mac (and possibly only for Mac
	OS X) and that your efforts would have gone toward new features.


I had hoped to find new sources of income. That more platforms would
generate more money. How often do you hear BBEdit users hear talking
about how great life would be if they could use BBEdit on Windows? I
thought to have a market there.


People [ask for a Windows port](http://www.barebones.com/cgi-bin/faq/faqgroup.pl?BBEdit_Pricing%20and%20Availability#Pricing_and_Availability_-_4) of BBEdit all the time — it is a very frequent request.


I thought so.


But what these people don’t understand is that much of
	what makes BBEdit special is Mac-specific — like its robust support for AppleScript and
	Apple events. And also, that there is no magic compiler that allows
	you to flip a switch and generate a Windows program out of Macintosh
	source code. The API’s for everything are different, including all
	the little things like drag-and-drop. It might be relatively easy to
	create a very basic, generic cross-platform application, but I think
	it’s exceedingly difficult to do so for powerful, professional
	software. And I think that’s why the companies that do so are very
	large.


I know exactly what you mean.


Big companies like Adobe and Macromedia have successfully ported
	Mac-only software products to Windows, but I can’t think of any
	small shareware developers who have done so.


Neither can I.  :-)


Was Pepper 4 at all successful on Windows?


Relatively, yes. I didn’t get too much attention in the Windows world,
it is difficult. Tucows refused to list Pepper, for example. But given that,
the number of sales were not disappointing.


For someone who hasn’t spent much time with modern computers,
	Windows and the Mac may appear somewhat similar — they both use
	windows, icons, menus, and a mouse pointer. But if you’re an
	advanced user, there are very big differences in the way Windows
	and Mac user interfaces are designed.


When I look at screenshots for other Windows text editors, like
	[UltraEdit](http://www.ultraedit.com/products/index.html#screen) and [TextPad](http://textpad.com/about/screenshots/index.html), they look very “Windows-y” to me: toolbars
	with small, cryptic icons, a tabbed interface for multiple open
	files in one Window. Pepper, however, looks and feels like a Mac
	application. Mac users are notorious for rejecting software ported
	to the Mac that stills retains a Windows-style interface; do you
	think Windows users feel the same way about software with a
	Mac-style interface?


Could very well be. But I never bothered too much with that. After
all, Pepper was not a Mac program either since it started life on
BeOS. And I got lots of complaints about small things from Mac users
as well, like the toolbar.


You mean the way that Pepper’s toolbar buttons work — 	click-and-hold to get a menu, click-and-release to get a button
	action? I thought that was a little weird, too.


Yes. I copied that from Outlook Express, so I wasn’t even the first on
Mac OS to come up with that. It is weird at first, but very useful when you’re used to it.


Pepper had a Multi-file view [showing multiple open files in a single
window], and of course most Windows users were using that mode while
most Mac users hated it.


That’s interesting, but not surprising. I think window management is
	perhaps the biggest difference between Mac and Windows. The MDI
	Windows interface is so clumsy that the easiest way to work is to
	use one application window to contain all open documents. I never
	liked that, and it’s the main reason I find Mac OS X’s Project Builder so
	distasteful.


It is something you can get used to, but it is very personal. I can
work with both but prefer the separate windows. On Win2K and before
there was another reason to prefer a single window, since each window
would get a tile in the Start bar and that would become messy quickly.
WinXP has solved this nicely (by having a look at BeOS).


I agree that many Windows programs look awful, but I see things improving
on that side of the fence. I think it would be easier for a Windows user to start using
Pepper than it would be for a Mac user to start using UltraEdit.


I agree. I’ve also observed over the years that numerous programs go
	from the Mac to Windows and are successful there (like Adobe’s
	entire product line), but that Windows software that gets ported to
	the Mac almost always fails. Remember Lotus 1-2-3 for Mac?


Yup, that was the shortest lived Mac application I’m aware of. :-)


Corel is hanging in, but I’ve never met anyone who uses their
	software on the Mac.


My guess is that most serious Mac users care deeply about the quality of the
	interface of the software they use, especially things like being
	intuitive and having very good fit and finish. Most Windows users
	don’t care about such things at all, and instead care more about the
	number of features.


Most maybe, but not all of them. And there are really good programs on
Windows showing up. I’m using The Bat! for email right now which is a
very good email program, similar in concept to Mailsmith but much more
powerful. The looks may not be optimal, but the feel is really great.


The port to Linux was an even bigger surprise to me. I can’t think of a single
	other commercial Mac application that’s been ported to Linux.


The Linux/X11 port was easy. Since that platform was already OS
neutral it was simply a matter of creating the right bridge
implementations.


For text editors in particular, I always figured there was no
	market whatsoever for commercial software on Linux. For one thing,
	anyone who runs Linux or BSD on their desktop and has the need for a
	good text editor is almost certain to be a hardcore, incorrigible
	user of either Emacs or vi. Of the remainder, there is a deeply
	ingrained predisposition towards free software, especially in the
	free-as-in-beer sense.


Did you expect Pepper to be successful on Linux? Was it?


I had hoped that with the new popularity of Linux and FreeBSD there
might be more and more users coming from Mac OS or Windows who would
like to use a more comfortable editor.


But I was wrong. I sold three copies and one of those three was a
fraud. I did have thousands of downloads though.


Wow, that’s unfortunate. But I can’t say I’m surprised — the only
	commercial Linux software that seems to sell are things like 3D
	rendering and animation software — packages that cost many
	thousands of dollars.


I am afraid that will be the future of the entire software industry.
Eventually it will only be possible to sell huge software packages
with lots of support; all the small apps will be open source in the end.


If you had it to do all over again, would you still have gone
	cross-platform?


Yes. As I said before, I don’t like to be locked in. I have been an OS
refugee for the greater part of my programming life and I’m glad I now
have this framework. I can take my editor with me wherever I might go.


## Pepper vs. BBEdit


Was it your goal to make a full-time living selling Pepper, or was
	it only a part-time endeavor?


When I started programming ten years ago it was my dream to ever have
a company doing shareware that would allow me to make a living. But
that dream has proven to be an illusion for me.


Pe was quite popular on BeOS but the market was far too small to make a
living. On Mac OS things were a little better but not much.


That is, until Mac OS X arrived. At the introduction of Mac OS X 10.0,
Pepper was sooner to market than BBEdit, and in two weeks I made an
awful lot of sales. But when BBEdit [for Mac OS X] was released, this
dried up immediately and what remained was not enough to make a
living.


But you knew back when you started work on Pepper 3
	that BBEdit was the leading editor for Mac OS. In fact, many of
	Pepper’s features seemed to be geared toward weaknesses in BBEdit
	5.1 (which was the current version of BBEdit when Pepper for Mac
	OS first shipped) — better PHP support, better support for
	customizable syntax coloring, rectangular selections, and a
	more powerful regular expression library.


BBEdit 6 and 6.5 addressed many of these shortcomings. How do you
	think the current versions of Pepper and BBEdit stack up against
	each other?


BBEdit has a lot of features geared towards HTML coders but
technically I think Pepper is superior. BBEdit still uses a Handle to
store text internally using the gap array approach. Pepper uses a
transaction mechanism. BBEdit did however learn a lot from Pepper and
borrowed many features and the difference isn’t as big as it was when
Pepper first came out. I still think Pepper is better though :-)


No doubt you prefer Pepper. :-)  But I’m curious which features you
	think BBEdit borrowed from Pepper.


There were many, I compiled a list once and threw it away again. I
didn’t care that much, after all I started writing a BBEdit clone in
the first place. But it was sour to see my advantage disappear.


How does Pepper’s transaction mechanism benefit the user?


True unlimited undo, even when plug-ins or Replace All have been used;
and this undo doesn’t use memory, only disk space. And when Pepper
crashes you can reopen your work the next launch and you get the full
undo history back of your previous session.


BBEdit’s undo works after Replace All, and for plug-ins which
	specifically support it. But it is memory-based.


I know how it works, I did that in Pe as well. But the transaction
model is way easier to program. I could cut thousands of lines of code
after introducing this change.


Pepper can open huge files, try editing a 650 MB file with BBEdit.


You could do it if you had 1 GB of RAM, but admittedly,
	memory-based editing gets unwieldy for files larger than 500MB or so.


When you decided upon the feature set for Pepper 3.0, how much was
	based on creating an editor that compared well against BBEdit, and
	how much reflected your own desires?


I never considered BBEdit at that point. I was more focusing on
getting Pe’s features on Mac OS. Pepper 3.0 had almost everything Pe
had and not much more. I believe Pepper 3.0 couldn’t even print.


There are not many serious programming editors for Mac OS. Other
	than BBEdit and Pepper, the only others are CodeWarrior and Project
	Builder. The CodeWarrior and Project Builder editors, however, are
	clearly designed to be used as part of their corresponding IDE’s. And
	with Pepper discontinued, that leaves BBEdit as the only serious
	dedicated editor for Mac OS. Do you think there’s room in the Mac OS
	market for another serious text editor?


No, I don’t think so.


Was it your goal from the outset to appeal to BBEdit users? Or did
	you instead try to appeal to people who **didn’t** like BBEdit?


:-) I think I wanted to show to the BBEdit users that there was room
for improvement. I got a bit tired with people shouting that BBEdit
was the best program ever on Mac OS while it simply started sucking in
my eyes. I mean, when I had to use other editors on BeOS I discovered
many new ways to do things that couldn’t be done with BBEdit.
Bare Bones was getting arrogant and I thought I wanted to be the little
boy shouting that the emperor didn’t have clothes.


But to answer your question, I was aiming for both.


## Scripting


As a long-time BBEdit user, Pepper’s complete lack of AppleScript
	support would have been a deal-breaker for me, even if I hadn’t been
	working for Bare Bones Software. Pepper supported basic text
	filtering with Perl and other shell languages, but had no macro
	language or internal scripting.


Did you ever consider adding AppleScript support to Pepper? Was it a
	frequent feature request from your users?


It was an often asked for feature. I never planned to support
AppleScript but I did plan to make Pepper scriptable. I even started
working on an interpreter and other needed internals. My goal was to
come up with something comparable to JED or VIM.


Comparable, or compatible?


Comparable of course. Way too dangerous to mimic an OSS package
completely.


One advantage to AppleScript is that it allows you to tie multiple
	applications together. Custom application macro languages are
	usually only useful within that one application.


Yes, but AppleScript is Mac only and so it was no option in Pepper.
And I thought AppleScript was rather slow and not very useful for more
than very simple tasks. I wanted my scripting to take over lots of the
logic internally, strip Pepper of all the fat and put it in scripts.
You need a more powerful script engine for that.


Did you consider using an existing cross-platform language, such as
	Perl or Python?


I’ve been thinking about using Java.


Did you have any other ideas for major features that you didn’t have
	time to implement?


Oh yes, many. As I mentioned before scripting was very high on my to-do
list, but there were other ideas as well. My to-do list had some 200
items on it ranging from simple cosmetic bugs to things like
scripting, folding, makefile generator, etc.


Your only other product I’m aware of was Sum-It, a spreadsheet for
	the Mac. What happened with Sum-It? Did you have any other
	products?


Last year, after releasing Pepper 3.6.6 I wanted to do something else.
I had always loved Pascal and Pascal-like languages and I thought let’s
try to write a Sum-It in Pascal. That went remarkably well and in no
time I had a new version. But unfortunately MW’s Pascal compilers are
not really good enough and so I ported it to C/C++. And then I thought
why not use a C++ framework and so I started working on this framework
I always planned to do and eventually I came up with Pepper 4.0 :-)


Maybe I will finish that Sum-It one day.


The old version of Sum-It supported AppleScript, which led me to
	wonder if Pepper ever would.


Never had time to do it in Pepper. There’s always so much you still
have to do and so little time.


Indeed, that’s the hardest part of software development. If you
	don’t cut good features from the list, you’ll never finish the job
	and actually release anything.


Exactly.


## Future Plans


What OS are you using now?


I’m writing this on a computer running Win2K. At my new job I
installed WinXP while all the others are running Linux. :-)


If you would have told me a year ago I would be using Windows right
now I wouldn’t have believed you. But now that I use Win2K/XP daily, I
have come to like it. I really believe WinXP is the true successor of
the old Mac OS. It is fast, stable and if you pick your software well
it is also easy to use. Personally I also prefer that Windows look
over Aqua.


Are you really done with Pepper? Do you have any plans to sell the
	product, or let someone else take over? Whenever software is
	discontinued, people ask the developer to release the source code.
	Is that something you’re considering?


If someone shows up and offers me enough I might sell it. But if that
doesn’t happen chances are high I will continue working on it for the
simple reason I’m using it myself daily. I’m not going to release the
code for Pepper right now. I have released other software in the past
like Sum-It and Pe. Sum-It never took off and I’m curious to what will
happen with Pe.


Maybe I will even try again with Pepper, but if I do I will look for a
different market.


So even if you re-introduce Pepper in the future, it won’t be for
	the Mac?


If I reintroduce Pepper, it will be in a completely different form.
I’m thinking more in the line of that hugely expensive Windows text
editor.


[SlickEdit](http://www.slickedit.com/)?


No, [CodeWrite](http://www.premia.com/). Costs around US$300 a piece.


Never heard of it, I’ll check it out. SlickEdit is around $200, I
	think, and seems to have a devoted following.


And I wouldn’t market it for consumers but would try to place it
vertically as they call it. Selling hundreds of peanuts is lots of
work and the result is, peanuts.


I don’t think it’s any coincidence that application software from
	Microsoft, Adobe, Quark, and other very successful companies costs
	many hundreds of dollars. A lot of their competitors, who sold
	software for much less money, are now out of business.


Yup. That’s a lesson I learned the hard way. Well, it was a gamble, I
had to choose between a high and a low price. I lost.


What are you working on now? Are you doing Windows development?


I’m no longer developing software. I’m a database manager at the
University of Nijmegen at the department for bio informatics. My job
is to keep the databases up and running and to make sure they will
continue to be up and accessible in the near future. This is a very
interesting job since we will have 1.5 Terabyte of data by the end of
this year and it is doubling every 10 months or so.


Completely different, but for the first time in ten years I have spare
time again. Last week I finally finished reading a novel I started five years
ago, and even had time to read another one immediately after. Great.



| **Previous:** | [Unix Switchers](https://daringfireball.net/2002/08/unix_switchers) |
| **Next:** | [A Brief Word on Netscape 7.0](https://daringfireball.net/2002/09/a_brief_word_on_netscape_70) |


PreviousNext