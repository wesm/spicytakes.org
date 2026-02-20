---
title: "Bingo Card Creator 2.5 Coming Soon"
date: 2009-01-12
url: https://www.kalzumeus.com/2009/01/12/bingo-card-creator-25-coming-soon/
slug: bingo-card-creator-25-coming-soon
word_count: 676
---


On Friday a customer reported a bug with UTF-8 files, which had creeped in literally months ago.  Since that was blocking her from getting work done I had a fire lit under my behind this weekend, and spent all three days of it coding like mad.  And wow, I was more productive than I’ve ever been in my life:

- It is now possible to put words under consistent columns, a common user request.  Previously it you were playing, say, US States bingo, Alabama could appear under any one of the five columns, which in my professional opinion is better as a teaching tool in most cases.  But some of my customers had less proficient readers (younger kids and ESL students, etc) so they want to only have them search a single column — thus, you should be able to call “Alabama — its under the B!”  Which took a bit of effort to accomplish.
- The Wizards menu got totally reworked.  I’m psyched about this improvement, because it includes my best 200 lines of code ever in terms of cleverness and it produces massive value to my customers and I.  Previously BCC shipped with a few dozen word lists, so as to not overwhelm the user looking at the Wizards menu.  However, I’ve paid for 507 (and counting) lists to be written, so why not ship them *all*?  However, just splitting them into categories just doesn’t cut it when you have 60+ categories, and I didn’t want to have to change my website’s architecture just to support subcategorization.  So instead I made some pretty nifty, configurable logic which conglomerates categories together and then automatically decides whether they need to be further aggregated into subdirectories or not.  Hopefully this will make the Wizards menu easier to use and increase the perceived value of the program.
- I’ve improved the updating functionality.  Previously I forced users to do a reinstall to get new word lists from me, which is a) inefficient in terms of my time (I have to keep making new builds) and b) total overkill.  So I incorporated the ability for the program to connect to my website and collect new lists by itself, as needed, after my freelance writers have written them.  Tada!  Double the bang for the buck out of money I was spending on marketing anyhow.  Plus now I am able to sell updates to the word lists — currently I’m just using that as a bullet point for the $25 program but I think I might eventually charge folks something nominal ($10 a year or so) for updates.
- Shamelessly stolen from inspired by my friends at Skybound, who make the best [visual CSS editor](http://www.skybound.ca/) on the planet: if you copy/paste your Registration Key at any time when you have the Enter Registration Key menu open, even if you’ve got it copied with a lot of other things, the program will register itself.  This lets me give simpler directions and cuts down on errors in users fumble-fingering registration keys.
- A fairly uncommon request finished at last — you can actually type in the number of cards wanted on the print page, rather than selecting it with that scrolling control.  (*Finally* I join the 1960s of user interface design_._)
- Bug fix for saving and then loading UTF-8 files.
- Native version in the works.  The folks at Excelsior got in contact with me and asked if I’d be interested in doing a case study with them to see whether eliminating the dependency on Java increases sales.  I’m always willing to  do an A/B test in the service of making me money, and if it helps them out so much the better.


If you’re interested in being a beta tester I’d appreciate the help — test if you can actually open the sucker up and print a bingo card from a Wizard, that excercises almost everything except the update feature:


[Windows version ](http://www.bingocardcreator.com/files/preview/BingoCardCreatorInstaller.exe)(requires Java 1.3+ installed)


[Windows version](http://www.bingocardcreator.com/files/preview/BingoCardCreatorInstallerNative.exe) (native — doesn’t require Java)


[Mac version](http://www.bingocardcreator.com/files/preview/BingoCardCreator.zip) (shouldn’t require anything you don’t have)
