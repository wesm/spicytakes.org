---
title: "Some corrections"
date: 2008-02-21
url: https://www.joelonsoftware.com/2008/02/21/some-corrections/
word_count: 810
---


A well-meaning, but rushed, journalist named Ben Charny interviewed me this morning about [Microsoft’s interoperability press release](http://www.microsoft.com/presspass/press/2008/feb08/02-21ExpandInteroperabilityPR.mspx).


[He made a ridiculous number of mistakes](http://money.cnn.com/news/newsfeeds/articles/djf500/200802211608DOWJONESDJONLINE001064_FORTUNE5.htm). That’s the nature of the wire reporters on deadline. Here are some corrections.

- “For want of a few key details from Microsoft Corp. (MSFT), Joel Spolsky tried but failed more than 10 years ago to make a better version of Microsoft’s remote office desktop-computer feature.”


Not true. [Fog Creek Copilot](https://www.copilot.com) was developed less than three years ago and has been under continous development since then. It has been a profitable product and we’re still developing new versions. I believe that what we built is better than Microsoft’s Remote Desktop in many ways (it works through firewalls, supports Macintosh and Windows, and is easier to set up for ad-hoc tech support) and it’s worse in some ways (it’s slower, and uses JPG compression as an optimization which can make the screen blurry). So it’s debatable whether I “failed.” There was no need for “a few key details from Microsoft” because we don’t interoperate with Remote Desktop, we use the open source VNC protocol (incidentally, the client code for Copilot is freely available under the GPL).

- “Now Project Co-Pilot has gotten new life.”


OK, it’s not “Project Co-Pilot”, it’s Fog Creek Copilot, and, like I say, we’ve been working on it continuously for almost three years and are about to release a major new version, so nothing about Microsoft’s announcement granted it “new life.” That part is just a fabrication.

- “On Thursday Spolsky finally located those elusive lines of code tucked inside 30,000 pages made public Thursday by Microsoft. Before they were available only under trade-secrets licenses.”


Huh? Lines of code? Ok, I understand, tech journalists may not understand the difference between “lines of code” and protocol specifications. When the press release came out, I was curious to see if it included a spec for the Remote Desktop protocol. We’ve always known how the protocol works, and how it transmits GDI commands for performance reasons, which is neither rocket science nor a trade secret. I don’t know if the concept is patented, but the X Window server worked this way before Windows was even invented, so if there is a patent for this GDI business, it ain’t Microsoft’s, but that’s neither here nor there.


Copilot doesn’t use the remote desktop protocol, full stop, and we don’t plan to. I just happened to look for that in the spec (in the 15 minutes between Microsoft’s press release and the time the journalist called me) because I was curious to see what kind of stuff was in there, and this was an area I had wondered about.

- By sharing more technical information about its key products on Thursday, Microsoft has jump-started a wave of development destined to unleash software that will compete with many more of Microsoft’s own products. One of the first appears to be remote desktop software, which uses a secured Internet connection to remotely access files and features stored on office- desktop computers. Currently, there’s no third-party version of the software, save for Citrix Systems Inc. (CTXS), which has a cross-licensing deal with Microsoft. But Microsoft’s existing product is a very basic one, making it rife for improvements. Its relative simplicity is demonstrative of how there’s been no competitive offerings that would have forced Microsoft to make a better widget.


This part is what he got mostly right, and it’s what I said. As far as I know, there are no competitive clients for Windows Remote Desktop (formerly called Terminal Services) except for Citrix’s cross-licensed implementation, presumably because the protocol was never publicized. As a result, if you want to use Windows Remote Desktop, you are stuck with the rudimentary clients Microsoft gives you. There are LOTS of great competitive remote desktop solutions that include both the client and the server; besides our own Copilot, there’s Bomgar, LogMeIn, GotoMyPC, and the granddaddy PCAnywhere, and another dozen or so options. But I’m pretty sure none of them interoperate with Remote Desktop because the spec has not been available. Everybody, including Copilot, has their own protocol, usually a variation of the RFB protocol [[PDF spec](http://www.realvnc.com/docs/rfbproto.pdf)].


So I thought this was one example of an area where Microsoft actually stood to gain from publicizing their protocols. It’s bound to open up lots of opportunities in hundreds of areas (remote desktop is just a tiny example) where third-party developers will be able to develop better drop-in versions of various pieces of the Microsoft software stack, which helps the Microsoft ecosystem more than it detracts from their business. Microsoft isn’t making a dime off of RDC because it’s free and built into Windows… a few competive options with more features can only help the Windows business in the long run.


**(Updated 2/22) [A correction to the correction](https://www.joelonsoftware.com/items/2008/02/22.html). **
