---
title: "Welcome, Indeed"
date: 2002-09-27
url: https://daringfireball.net/2002/09/welcome_indeed
slug: welcome_indeed
word_count: 551
---


***SCENE:** Avie Tevanian’s office, late July, 2002. A tester from Apple’s QA department knocks at the door.
*


**QA Tester:** Dr. Tevanian, you wanted to see me?


**Avie:** Call me Avie. You’re the guy who filed a bug report against the Jaguar GM installation discs?


**QA:** Uh, yeah. That was me.


**Avie:** I don’t understand the problem.


**QA:** Well, it’s the readme file.


**Avie:** I took a look at it, and it looks fine to me.


**QA:** Well, it works fine in Mac OS X, but it’s broken under Mac OS 9. Hold on a sec, I can show you.


*(The QA tester opens his PowerBook.)
*


**QA:** Here’s how it looks under OS X:


**QA:** But on OS 9, you see this:


**Avie:** I still don’t see the problem.


**QA:** It doesn’t have an icon.


**Avie:** Yes it does.


**QA:** OK, it has *an* icon. But it’s just a blank, generic icon. It should appear as a PDF file.


**Avie:** But it’s obviously a PDF file. It’s right there in the filename.


**QA:** Uh, right. But the icon is wrong, because the file doesn’t have any HFS type or creator info.


**Avie:** That’s cosmetic. Icons look like crap on Mac OS 9 anyway.


**QA:** Well, it’s not just cosmetic. It’s a functional bug, because you can’t open the file by double-clicking it in the Finder.


**Avie:** Yes you can. I just did it.


**QA:** I mean on 9. Everything I’m talking about here is on 9. The readme file works just fine on X. But if you double-click it on 9, you get the dialog box that says, “The document ‘Read Before You Install.pdf’ could not be opened, because the application program that created it could not be found.” That’s a bug.


**Avie:** Well, so you can’t double-click it. That’s cosmetic.


**QA:** Double-clicking files is a fundamental action in the Finder. For some users, it’s the *only* way they know how to open files.


**Avie:** We’ll just tell them to use drag-and-drop, or the Open dialog.


**QA:** How will we tell them?


**Avie:** We’ll put it in the readme.


**QA:** Uh…


**Avie:** Oh, right. Hmm, this is a tough one.


**QA:** Well, we could just set the type and creator code for the file.


**Avie:** What?


**QA:** Set the type and creator. So it’ll open in Acrobat.


**Avie:** *Phbbt.* That’s a hack. No way.


**QA:** A hack?


**Avie:** Type/creator? That junk’s deprecated.


**QA:** But not on Mac OS 9. And the Jaguar installation disc needs to run from 9. As it stands, it’s sort of an insult — it’s the readme file, the *first* file most users will try to open, in a folder named “Welcome to Mac OS X”, but it can only be double-clicked if you’re already running Mac OS X.


**Avie:** There’s the lesson: “Everything works better on OS X.”


*(Uncomfortable silence.)*


**QA:** This isn’t getting fixed, is it?


**Avie:** Nope.


*(Uncomfortable silence.)*


**Avie:** Hey, you’re not the same guy who reported the bug against the Jaguar Finder because the new file searching window doesn’t let you search for Type/Creator codes, are you?


## Further Reading


John Siracusa: [Metadata, the Mac, and You](http://www.arstechnica.com/reviews/01q3/metadata/metadata-1.html)


Jeffrey Zeldman: [OS X Blues I](http://www.zeldman.com/daily/lifeisbeautiful/osxblues/); [OS X Blues II](http://www.zeldman.com/daily/lifeisbeautiful/osxblues2/)



| **Previous:** | [The Annotated Workspace](https://daringfireball.net/2002/09/the_annotated_workspace) |
| **Next:** | [Feed Me](https://daringfireball.net/2002/09/feed_me) |


PreviousNext