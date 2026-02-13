---
title: "Installing Vista RC1 in VMWare Workstation"
date: 2006-09-08
url: https://www.joelonsoftware.com/2006/09/08/installing-vista-rc1-in-vmware-workstation/
word_count: 249
---


If you are trying to install Windows Vista RC1 in VMWare Workstation, you may see setup appear to hang on the text-mode screen that says “Windows is loading files…”.


Actually what has happened is that Vista Setup is already in graphics mode trying to do things, but something about the way it switches the display adapter into graphics mode is not working right on VMWare.


If I were VMWare I’d be pretty ticked off at Microsoft right now; since Microsoft makes a competitive product, Virtual PC, it is Highly Suspicious that they come out with a major new test release of an operating system that just happens to not work on VMWare Workstation, something which is practically the de facto standard for developers testing new operating systems. Shabby and slimy, Microsoft. They’re probably testing Windows Vista with tens of thousands of applications; not testing with VMWare is inexcusable.


There’s a workaround, for now, while VMWare works on the problem: edit the virtual machine’s .vmx file to include


svga.maxWidth = “640” 
svga.maxHeight = “480”


You can get Vista installed in VGA 16 color 640×480 mode (it will look awful) and then when you get everything running, install VMWare tools and take out those two lines and you’ll be good to go. Thanks to anonymous user echelon9 from the [VMWare board](http://www.vmware.com/community/thread.jspa?messageID=467411) for this tip.


I’m assuming that the Aero/Glass UI’s heavy demands on the graphic card may mean that it can’t be tested under VMWare, but I’d love to be wrong.
