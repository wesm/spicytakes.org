---
title: "Consistency and Other Hobgoblins"
date: 2000-04-22
url: https://www.joelonsoftware.com/2000/04/22/consistency-and-other-hobgoblins/
word_count: 2088
---


The main programs in the Microsoft Office suite, Word and Excel, were developed from scratch at Microsoft, but others were bought from outside companies, notably FrontPage (bought from Vermeer) and Visio, bought from Visio. The thing these two programs have in common? They were originally designed to look and feel just like Microsoft Office applications.


The decision to emulate the Office UI wasn’t merely to “suck up” to Microsoft or to position the companies for acquisition; indeed, Charles Ferguson, who developed FrontPage, does not hesitate to admit his antipathy for Microsoft; he repeatedly *begged* the Justice department to *do something* about the Redmond Beasties (until he sold his company to them, after which his position became a lot more complicated). In fact Vermeer and Visio seem to have copied the Office UI mainly because it was expedient: it was easier and quicker than reinventing the wheel.


When Mike Mathieu, a group program manager at Microsoft, downloaded FrontPage from Vermeer’s web site and tried it out, it worked a whole lot like Word. Since it worked so much like he *expected* a program to work, it was easier to use. And this ease of use gave him a favorable impression of the program right off the bat.


Now, when Microsoft gets a favorable impression of a program right off the bat, they shell out $150 million or so. Your goal is probably more modest; you want your customers to get a favorable impression and shell out maybe $39. But it’s the same idea: consistency *causes* ease of use which in turn *causes* good feelings resulting in more money for you.


It’s hard to overestimate just how much consistency helps people to learn and use a wide variety of programs. Before GUIs, every program reinvented the very fundamentals of the user interface. Even a simple operation like “exit” which every program *had to *have was completely inconsistent. In those days people made a point of memorizing, at the very least, the exit command of common programs so they could exit and run a program they understood. Emacs fanatics memorized “:q!” (and nothing else) in case they ever found themselves stuck in vi by mistake, while vi users memorized “C-x C-c” (Emacs even has its own way to represent control characters). Over in DOS land, you couldn’t even *use* WordPerfect unless you had one of those dorky plastic keyboard templates that reminded you what Alt+Ctrl+F3 did. I just memorized F7 which got you the heck outta there.


Not only that, but small inconsistencies in things like the default typing behavior (overwrite or insert) can drive you *crazy*. I’ve gotten so used to Ctrl+Z meaning “undo” in Windows applications that when I use Emacs I am constantly minimizing the window (Ctrl+Z) by mistake. (The funny thing is that the very reason Emacs interprets Ctrl+Z as *minimize *is for “consistency” with that terrific user interface, **csh**, the C shell from UNIX.) This is one of those minor frustrations that adds up to a general feeling of unhappiness.


To take an even smaller example, Pico and Emacs both use Ctrl+K to delete lines, but with a *slightly* different behavior that usually mauls my document whenever I find myself in Pico. I’m sure you have a dozen examples of your own.


In the early days of Macintosh, before Microsoft Windows, Apple’s evangelists told everyone that the average Mac user used more different programs to get their work done than the average DOS user. I don’t remember the exact numbers, but I believe it was something like 1 or 2 programs for the average DOS user versus *twelve* programs for a Mac user. The reason was that it was so easy to learn a new program on the Mac because they generally worked the same way.


Consistency is a fundamental principle of good UI design, but it’s really just a corollary of the axiom “make the program model match the user model”, because the user model is likely to reflect the way that users see other programs behaving. If the user has learned that double-clicking text means *select word*, you can show them a program they’ve never seen before and they will guess that the way to select a word is to double-click it. And now, that program *better* select words when they double click (as opposed to, say, looking the word up in the dictionary), or else you have a usability problem.


If consistency is so *obviously* beneficial, why am I wasting your time and mine evangelizing it? Unhappily, there is a dark force out there that fights against consistency, and that is the natural tendency of designers and programmers to be creative.


Now, I hate to be the one to tell you “don’t be creative,” but unfortunately, to make a user interface easy to use, you are going to have to channel your creativity into some other area. In most UI decisions, before you design anything from scratch, you absolutely have to look at what other popular programs are doing and emulate that as closely as possible. If you’re creating a document editing program of some sort, it better look an awful lot like Microsoft Word, down to the accelerators on the menu items that you have in common. Some of your users will be used to Ctrl+S for save; some of them will be used to Alt+F,S for save, and still others will be used to Alt,F,S (releasing the Alt key) . Another group will look for the floppy disk in the top left area of the program and click it. All four better work, or your users are going to get something that they didn’t want.


I’ve seen companies where management prides themselves on doing things *deliberately* differently from Microsoft. “Just because Microsoft does it, doesn’t mean it’s right,” they brag, and then proceed to create a gratuitously different user interface from the one that people are used to. Before you start chanting the mantra that “just because Microsoft does it, doesn’t mean it’s right,” please consider two things:

1. Even if it’s not right, if Microsoft is doing it in a popular program like Word, Excel, Windows, or Internet Explorer, then millions of people are going to *think* that it’s right, or at least, fairly standard, and they are going to assume that your program works the same way. Even if you think (as the Netscape 6.0 engineers clearly do) that Alt+Left is not a good shortcut key for “Back”, there are literally millions of people out there who will try to use Alt+Left to go back, and if you refuse to do it on some general religious principle that Bill Gates is the evil smurf arch-nemesis Gargamel, then you are just gratuitously ruining your program so that you can feel smug and self-satisfied, and your users will not thank you for it.
And don’t be so sure it’s not right. Microsoft spends more money on usability testing than you do, they keep detailed statistics based on millions of tech support phone calls, and there’s a darn good chance that they did it that way because more people can figure out how to use it that way.


To create a good program with a usable user interface, you’re going to have to leave your religion at the door, thank you. Microsoft may not be the only company to copy: if you’re making an online bookstore, you should probably make sure that your web site is at least semantically the same as Amazon. Amazon keeps your shopping cart around for 90 days. You might think that you are extra-smart and empty the cart after 24 hours. If you do this, there will be Amazon customers who put stuff in your shopping cart and come back two weeks later expecting it to still be there. When it’s gone, you’ve lost a customer.


If you’re making a high end photo editor for graphics professionals, I assure you that 90% of your users are going to know Adobe Photoshop, so you better behave a heck of a lot like Photoshop in the areas where your program overlaps. If you don’t, people are going to say that your program is hard to use, even if *you* think it’s easier to use than Photoshop, because it’s not behaving the way *they* expect it to.


There is another popular tendency to reinvent the common controls that come with Windows. Don’t even get me started about Netscape 6. There was a time when you could tell the programs that were compiled with Borland’s C++ compiler because they used big fat OK buttons with giant green checkboxes. This wasn’t nearly as bad as Kai’s Photo Soap:


Fine, so, it’s stunningly beautiful, but the O with a line through it (which actually means “no”) reminds me of “OK,” and the standard on Windows is to have OK on the left, so I wind up hitting the wrong button a lot. The only benefit to having funny symbols instead of “OK” and “Cancel” like everyone else is that you get to show off how *creative* you are. If people make mistakes because of Kai’s creativity, well, that’s just the price they have to pay for being in the presence of an *artist*. (Another problem with this “dialog” is that it doesn’t have a standard title bar which can be used to move the dialog around on the screen. So if the dialog gets in the way of something you want to see in order to answer the question in the dialog, you are out of luck.)


Now, there’s a lot to be gained by having a slick, cool-looking user interface. Good graphical design like Kai is pleasing and will attract people to your program. The trick is to do it *without* breaking the rules. You can change the visual look of dialogs, a bit, but don’t break the functionality.


When the first version of Juno was written, it had the standard log on dialog that prompted you for a user name and a password. After you entered the user name, you were supposed to press TAB to go to the password field and type in a password.


Now, this distracted one of the programming managers at Juno, who had a lot more experience with UNIX than with Windows, so he was used to typing user name, then pressing ENTER to jump to the password field (instead of TAB). Now, when you’re writing a program targeted at non-expert Windows users, a UNIX programmer is probably *not* the ideal example of a typical user, but this manager was very insistent that the enter key should move to the next field instead of doing the Windows-standard “OK” thing. “Just because Microsoft does it, doesn’t mean it’s right,” he chirped.


So the programmers spent a really remarkable amount of time writing some amazingly complicated dialog box handling code to work around the default behavior of Windows. (Being inconsistent is almost always *more* work than just acting like your platform expects you to act). This code was a big maintenance nightmare; it didn’t port so well when we moved from 16-bit to 32-bit Windows. It didn’t do what people expected. And as new programmers joined the team, they didn’t understand why there was this strange subclass for dialogs.


An awful lot of programmers have tried to reimplement various common Windows controls, from buttons to scrollbars to toolbars and menu bars (the Microsoft Office team’s favorite thing to reimplement). Netscape 6.0 goes so far as to reimplement every single common Windows control. This usually has some unforeseen bad effects. The best example is with the edit box. If you reimplement the edit box, there are an awful lot of utilities that you don’t even know about (like Chinese language editing add-ins, and bidirectional versions of Windows that support right-to-left text) that are going to stop working because they don’t recognize your non-standard edit box. Some of the reviewers of the preview release of Netscape 6.0 noticed that the URL box, using a non-standard Netscape edit control, does not support common edit control features like right clicking to get a context menu.


When you find yourself arguing with a anti-Microsoft fundamentalist or a creative graphic designer about consistency, they’re apt to quote Emerson incorrectly: “Consistency is the hobgoblin of little minds…” The real quote is “A *foolish* consistency is the hobgoblin of little minds.” Good UI designers use consistency intelligently, and, though it may not show off their creativity as well, in the long run it makes users happier.
