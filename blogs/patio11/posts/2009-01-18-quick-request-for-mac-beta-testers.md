---
title: "Quick (Final) Request For Beta Testers"
date: 2009-01-18
url: https://www.kalzumeus.com/2009/01/18/quick-request-for-mac-beta-testers/
slug: quick-request-for-mac-beta-testers
word_count: 512
---


Hideho everybody.   Thanks for the help with the beta testing.  This is a quick list of the issues that were reported and which I have confirmed fixed.  I’d be obliged if Mac users could try executing the app again and see if the permissions got kept by the zip file this time.  If Windows users want to kick in any comments, I’m always obliged.


[Windows version ](http://www.bingocardcreator.com/files/preview/BingoCardCreatorInstaller.exe)(requires Java 1.4+ installed)


[Windows version](http://www.bingocardcreator.com/files/preview/BingoCardCreatorInstallerNative.exe) (native — doesn’t require Java)


[Mac version](http://www.bingocardcreator.com/files/preview/BingoCardCreator.zip) (shouldn’t require anything you don’t have)

- Purpose of plus/minus buttons is unclear.  Rewrote description of functionality on main page of app.  (Both buttons were already mentioned, but if you guys didn’t see it that is **my** fault.)
- Two included bingo cards, written in Spanish and Japanese, could not be loaded properly.  Fixed.
- Mac menu bar does not appear where Mac users expect it to be.  I *believe* this to be fixed.
- Windows resize when wizards are selected.  *I appreciate the feedback, but this is by design.*
- Resizing the window such that the sample card is not totally visible, then resizing it again, causes text on the sample card labels.  *This is related to the Swing library’s implementation.  I will study the feasibility of fixing it later, but at the moment it is a cosmetic issue which is easily recovered from and happens only in edge cases.*
- Changing word wrap causes the sample card to shuffle.  *I appreciate the feedback, but t__his behavior is by design*.
- Mac users do not expect to use the Ctrl key, but the program does.  I believe this to be fixed.
- Mac users do not expect mnemonics.  *I’m sort of loathe to remove functionality, particularly functionality that a few hundred paying customers may be using already*.  *I’m not exactly a Mac UI partisan and most of my users aren’t, either, so I’m going to put off changing this one.*__
- “Upgrade to full version now?” dialog is wider than my screen*.  *  Fixed.
- The text in the Advice frame is selectable with the mouse.  *Hard to fix due to Java implementation of text boxes, no impact on customers, postponing until I am very bored.*
- Small screen + extraordinarily long words on card (e.g. names of famous plays) = card extends off screen.*  Low impact and rare circumstances, but I will address this eventually.*
- Save/Open defaults to application folder, should be elsewhere.  *Suboptimal but kept for backwards compatibility.  You may be interested in knowing that applications can write to Program Files in Vista.  Really, try it — MS hacked around their own security system to avoid breaking legacy apps.*


nota bene to Ant users: the zip tasks discards permissions.  If you need them to come out intact, you need to put the files requiring extra permissions in <zipfileset filemode=”755″> blocks.  In particular, if you are zipping a distribution which includes a jar wrapped up as a Mac application, the JavaApplicationStub file needs to be marked as filemode=”755″.  Much love to the testers that discovered this before my users did.
