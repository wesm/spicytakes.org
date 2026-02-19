---
title: "Inconsistencies"
date: 2003-02-16
url: https://daringfireball.net/2003/02/inconsistencies
slug: inconsistencies
word_count: 1290
---


[Matt Gemmell’s “NSSchizophrenicControls”](http://www.scotlandsoftware.com/blog/index.php?p=83078088&more=1) would be funnier if it weren’t about Mac OS X, and if the developers responsible for the interface inconsistencies he describes weren’t working at Apple.


It’s part of a thread of similar criticism, much of which is spot-on accurate, from [Gemmell](http://www.scotlandsoftware.com/blog/index.php?p=83078085&more=1#more83078085), [Erik J. Barzeski](http://nslog.com/archives/2003/02/12/mac_ui_roundup_osnews.php), and [Vinay Venkatesh](http://www.vinayvenkatesh.com/blog/archives/000180.php), all three of whom are Mac OS X developers. (Barzeski’s post on [iMovie 3’s abominable misuse of radio buttons](http://nslog.com/archives/2003/02/04/you_cant_escape_ken_burns_and_other_horrid_imovie_ughs.php) is particularly noteworthy.)


Well-intentioned push-back comes from [Buzz Andersen](http://www.scifihifi.com/index.cgi/mac/UILand.html) (who is [also a Mac OS X developer](http://www.scifihifi.com/index.cgi/software)):


> Let’s start by stating the complaint simply.  It seems clear from the applications Apple has released in the last few years that a certain amount of, shall we say, *experimentation* has been encouraged in the UI department.  Rather than adhering to a standard set of interface widgets—the same NSTextFields, NSToolbars, and NSButtons available to all Mac developers—Apple has seen fit to concoct a variety of novel UI elements for each new iApp.  To critics, this is sacrilege since it flies in the face of one of the cherished cornerstones of Mac usability: consistency.  If developers always use the same widgets and adhere to a set of well-defined rules in designing their interfaces, people, it is reasoned, will be better able to understand new applications and become less intimidated by their computers.
> What if I was to suggest, however, that consistency is no longer as important a value in UI design as it was in 1984?  What if I was to propose, in fact, that, within reason, the evolution of new GUI widgets is not only proper, it is essential (to paraphrase Dr. Strangelove)?  And what if I was to tell you that one of today’s smartest interface thinkers agrees with me?


Well, if you were to tell me those things, I would tell you that you are, unfortunately, very wrong. It’s a recurring theme here at Daring Fireball, but worth repeating: the hallmark advantages of the Macintosh are consistency and intuitive UI design. These factors are very different from the conventional wisdom of the PC industry in general, which holds that the Mac’s advantage is in being visually appealing and “easy to use” for dummies and artists (which in turn is a thinly-veiled insinuation that creative people are not as smart as PC nerds, and also that the aforementioned creative people’s devotion to the Macintosh is superficial).


Now, what’s interesting about the Mac’s consistency and intuitiveness is that the distinction between the two factors is somewhat blurred. Much of the intuitiveness stems from the consistency; and many of the Mac’s tried-and-true conventions have worked so well, for so many years, because they were so intuitively designed back in the dark ages of the 1980s.


It’s not pedantry that inspires Mac afficionados to gripe about Apple’s violations of the Macintosh Human Interface Guidelines. It’s not that the HIG is simply a list of rules to which a bunch of us nerdy Mac experts demand blind adherence only for the sake of following rules. It’s that the guidelines outlined in the HIG form a cohesive whole describing a philosophy of design.


And that is not to say that ease-of-use is not a Macintosh advantage. It is, but it’s at the other end of the cause and effect relationship. Ease-of-use is a *result*, intuitiveness and consistency are the cause. This is very different than how much Windows software (and some bad Mac software) is designed, where ease-of-use is attempted by creating a “shell” interface geared toward morons on top of a system that is overly complicated, resulting in something that might well be somewhat usable by morons, but is never satisfying because it is neither intuitive nor consistent. AOL is a great example of this sort of UI design.


Andersen concludes:


> Obviously there are limits to how far Apple should go: I’m not arguing for complete UI anarchy here.  I’m just proposing that Apple is not *necessarily* out of line when they invent a component like Matt’s “NSSchizophrenicTextField” to solve a problem unique to a certain application.  Consistency is valuable, but only as long as it doesn’t stifle innovation.


The problem is these inconsistent control widgets from Apple aren’t innovative. They’re just different for difference’s sake. Innovative control widgets would be controls that allow us to perform new tasks, or tasks which aren’t possible using only standard controls. What Apple has been doing is creating controls which appear to be the same as each other, but are not.


Text edit fields, in particular, are a terrific example to show how Apple is dropping the ball. Text edit fields in the original Mac OS were often quite inconsistent across applications. For example, the standard TextEdit system control in the old Mac OS didn’t support the forward delete key for many, many years. You could hit the regular Delete key to backspace, but if you had an extended keyboard, the forward delete key (the one under “Help”) either didn’t do anything, or worse, inserted a control character into the text field. Better Mac developers fixed this themselves on an app-by-app basis (BBEdit, for example, has supported forward delete as long as I can remember). But this meant that forward delete worked in some apps, but not in others. Same thing for keyboard text selection and navigation.


That wasn’t good at all. Mac OS X is perfectly positioned to fix this — its built-in default text edit fields support the full range of standard Mac OS text editing keyboard shortcuts. It is *easier* to create text edit fields that are completely consistent across the entire OS than ever before. But instead of leading the way, Apple’s application teams are creating various slightly inconsistent text edit fields.


I hope I’m not coming across as being overly-critical of Andersen’s article; overall he isn’t too far off-base, with the glaring exception of undervaluing just how essential consistency still is for the Mac. If anything, I’d go so far as to say that it’s *more* important than ever, because other GUI platforms, while still much less consistent than Mac OS X, are still more consistent than they used to be. If the Mac OS interface gets less consistent going forward, it will become less distinguishable from its competitors.


It’s also worth reiterating that none of the people quoted above, nor I, are trying to argue that Apple’s UI design stinks. Overall, Apple is still doing a terrific job. But that doesn’t mean they’re above criticism. The time to nip a bad trend is at the beginning.


## Standard Prefs Shortcuts


Speaking of consistency, Barzeski targets Apple for using inconsistent keyboard shortcuts for opening Preferences windows in its applications:


> For example, Apple’s own apps can’t stick to a common theme regarding the “Preferences…” item: iTunes and iCal use command-Y, Safari uses command-comma, Mail uses command-option-semicolon, and the Finder and many other Apple apps have no shortcut at all.


While true that the current state of affairs is wildly inconsistent, Apple has actually done something about this, but only recently. The HIG has recently been updated to include a [standard recommendation for the Preferences shortcut](http://developer.apple.com/techpubs/macosx/Essentials/AquaHIGuidelines/AHIGMenus/chapter_4_section_13.html), and that shortcut is Cmd-, . This recommendation is very new, however, so it’s not surprising that Safari is the only app in the bunch using it. I expect the others will soon follow suit, as will third-party software. ([NetNewsWire](http://ranchero.com/netnewswire/) already does.)


A previous semi-standard shortcut was Cmd-; . I say “semi” because I don’t believe this shortcut was ever officially endorsed by Apple, but it has widespread support in third-party software. One problem with Cmd-;, if I recall correctly, is that it is difficult to type on certain non-U.S. keyboard layouts.



| **Previous:** | [Flowers Are for Chumps](https://daringfireball.net/2003/02/flowers_are_for_chumps) |
| **Next:** | [Popularity Contest](https://daringfireball.net/2003/02/popularity_contest) |


PreviousNext