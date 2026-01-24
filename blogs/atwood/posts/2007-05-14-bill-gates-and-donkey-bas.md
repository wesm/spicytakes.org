---
title: "Bill Gates and DONKEY.BAS"
date: 2007-05-14
url: https://blog.codinghorror.com/bill-gates-and-donkey-bas/
slug: bill-gates-and-donkey-bas
word_count: 777
---

It’s hard to imagine now, but in the early days of Microsoft, Bill Gates was an [actual programmer](https://blog.codinghorror.com/how-to-become-a-better-programmer-by-not-programming/). One bit of hard evidence is the BASIC program [DONKEY.BAS](http://en.wikipedia.org/wiki/DONKEY.BAS) included with original IBM PCs running IBM DOS 1.10. The history of this weird little program is covered [in a 2001 TechEd keynote](https://web.archive.org/web/20070704104845/http://www.microsoft.com/presspass/exec/billg/speeches/2001/06-19teched.aspx) by Gates himself:


> **ARI BIXHORN**: Well, I am thrilled to be here today, because this week we are celebrating the ten-year birthday of the world’s most powerful, productive and popular developer tool. And of course I’m talking about Visual Basic.
> Now, to help set the context for just how far Visual Basic has come and really how far the Basic language has come, I’d like to take a step back just a few years and look at an application that was written in Basic. This application, called Donkey.bas was actually written by none other than the gentleman standing to the left of me. Bill, how long ago was it that you wrote Donkey.bas?
> **BILL GATES**: Actually, it was myself and [Neil Konzen](http://en.wikipedia.org/wiki/Neil_Konzen) at four in the morning with this prototype IBM PC sitting in this small room. IBM insisted that we had to have a lock on the door and we only had this closet that had a lock on it, so we had to do all our development in there and it was always over 100 degrees, but we wrote late at night a little application to show what the Basic built into the IBM PC could do. And so that was Donkey.bas. It was at the time very thrilling. So go ahead and show them what that looks like.


Here’s a small animation I captured of DONKEY.BAS running in a virtual machine:


![DONKEY.BAS animation](https://blog.codinghorror.com/content/images/uploads/2007/05/6a0120a85dcdae970b0120a86d9759970b-pi.gif)


Thrilling indeed. The Macintosh folks were [suitably unimpressed](http://folklore.org/StoryView.py?project=Macintosh&story=Donkey.txt):


> [PC-DOS] came with some games written in BASIC that were especially embarrassing. The most embarrassing game was a lo-res graphics driving game called “Donkey.” The player was supposed to be driving a car down a slowly scrolling, poorly rendered “road,” and could hit the space bar to toggle the jerky motion. Every once in a while, a brown blob would fill the screen, which was supposed to be a donkey manifesting in the middle of the road. If you didn’t hit the space bar in time, you would crash into the donkey and lose the game.
> We thought the concept of the game was as bad the crude graphics that it used. Since the game was written in BASIC, you could list it out and see how it was written. We were surprised to see that the comments at the top of the game proudly proclaimed the authors: Bill Gates and Neil Konzen. Neil was a bright teenage hacker who I knew from his work on the Apple II (who would later become Microsoft’s technical lead on the Mac project) but we were amazed that such a thoroughly bad game could be co-authored by Microsoft’s co-founder, and that he would actually want to take credit for it in the comments.


It’s funny to think that DONKEY.BAS is part of Gates’ legacy as a programmer. If nothing else, at least he has a healthy sense of humor about his past. The only copy of [the source code for DONKEY.BAS](https://web.archive.org/web/20070518023717/http://drivey.com/DONKEYQB.BAS.html) I can find has been stripped of any credits by Gates or Konzen. It’s a fairly short program, but it’s also a painful reminder of how awkward programming was in 1981. Update: Leon was kind enough to send in [an original copy of DONKEY.BAS](https://github.com/coding-horror/donkey.bas/blob/master/donkey.bas) from the DOS 1.1 disks.


During the TechEd 2001 keynote, Microsoft demonstrated a tongue-in-cheek, fully 3D update of Donkey written in the then-beta VB.NET language, to illustrate just how far BASIC had come in the intervening 20 years.


![Donkey.NET splash screen](https://blog.codinghorror.com/content/images/uploads/2007/05/6a0120a85dcdae970b0120a86d978f970b-pi.png)


You can still can no longer [download the VB.NET version of Donkey](http://web.archive.org/web/20080327123446/http://www.microsoft.com/downloads/details.aspx?FamilyID=990d0ec1-23ea-4408-898d-1fd5727a8890&displaylang=en) from Microsoft. I downloaded it and converted it to Visual Studio 2005 and .NET 2.0 fine. But I couldn’t get it to run because of its oddball dependency on DirectX 8.


> Donkey .NET is a three-dimensional driving simulator game that demonstrates the new features available to Microsoft® Visual Basic® developers. Written in Visual Basic .NET RTM, this sample uses XML Web services, multithreading, structured exception handling, shaped Windows Forms, and custom-drawn controls. The sample includes the setups for both the game application and an optional XML Web service used with the game. The setups will also install the source code


![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcZJh9DcqqOpIeeXXe8YExgdcQOorEyzsXcpLgfQEWHcEgtBVbNU_D9k9x8G_w7yxiO6rWBdIpXzBTnSRWtH-7TfNZWRHsvbOHHIU1EfcGjs8tnkGOE28_dRyc32TxoMAUtc2jy?key=EFBg8Ij0aJ1EmCyuDte1jBlv)


I suppose that’s another enduring lesson of DONKEY.BAS; the various BASIC implementations have never been known for their stellar compatibility.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[historical programming](https://blog.codinghorror.com/tag/historical-programming/)
[basic](https://blog.codinghorror.com/tag/basic/)
