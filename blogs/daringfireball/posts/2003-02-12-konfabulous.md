---
title: "Konfabulous"
date: 2003-02-12
url: https://daringfireball.net/2003/02/konfabulous
slug: konfabulous
word_count: 1105
---


The mysterious and much-ballyhooed [Konfabulator](http://konfabulator.com/) project from Arlo Rose and Perry Clarke is finally shipping. It costs $25, and it’s a JavaScript runtime engine for Mac OS X. It runs “widgets”, which are little packages (folders) containing XML, JavaScript, and bitmap images. Widgets are like programs; but unlike full-blown Mac OS X applications, widgets don’t have menu bars or Dock icons. When you run a widget, it’s just a window.


Given that Arlo Rose was significantly responsible for Kaleidoscope, Konfabulator widgets are, unsurprisingly, heavy on the visual appeal. (More on this later.)


The “runtime engine” just means that while Konfabulator itself is running, it provides the context for the widgets to run. When you create your own widget, you don’t have to worry about Carbon or Cocoa or any traditional Mac programming APIs. You just write JavaScript for Konfabulator, which makes it quite simple to get a simple widget up and running.


Konfabulator itself is just an application. Albeit an application which itself does not have a menu bar or Dock icon. When running, Konfabulator puts a global icon menu in the menu bar. The menu lists all running widgets, and allows you to quit Konfabulator (which, if you do, will close all running widgets — a widget can’t run unless Konfabulator itself is running). If you want to quit an individual widget, you can either control-click in the widget’s window, and use a contextual menu, or you can hold down the Control key while selecting the widget’s name from the Konfabulator menu (which I never would have guessed without having read the documentation; it strikes me as a very unintuitive shortcut).


The widgets that ship with Konfabulator do things similar to the tasks that people made “docklets” for back in the early days of Mac OS X 10.0. A battery meter, an AirPort signal strength meter, a simple calendar, and of course, several clocks. There are already several third-party widgets available, and surely there will be more soon.


It’s a neat idea, and it’s easy to see why people are excited about it. For one thing, JavaScript is a terrific scripting language. Certainly it is most famous for client-side web browser scripting, but it’s really a general purpose scripting language. It has a nice readable syntax, is object-oriented, and supports cool things like built-in regular expressions. According to the [Konfabulator web site](http://konfabulator.com/info/), Rose’s original idea was to use Perl as the scripting language. JavaScript is a much better choice. For one thing, it’s a better language for beginning programmers, and a large part of Konfabulator’s appeal is that it’s intended to be relatively easy to get started with, even if you’re not an experienced programmer.


## Pixel Pushing


As is evident by taking a look at widgets in action, a big part of Konfabulator’s appeal is purely visual. Given Rose’s background with Kaleidoscope, this isn’t surprising. But what I don’t like, not one bit, is that “skinning” is not an option — it is mandatory. Widgets’ interfaces are composed of images (PNG, JPEG, GIF, TIF, and perhaps other formats). There is no way to construct a widget using native Aqua UI elements.


Everything, from the window backgrounds to each and every button, must be an image file. Given that buttons might need to come in several states (active, pressed, inactive), and that if you’re trying to look Aqua-y you’ll need to support both the Blue and Graphite color themes, that’s an awful lot of pixel-pushing. Leaving aside the larger question of whether skinnable GUIs are a good idea, it just seems silly not to make it easy to create a non-skinned default UI.


But perhaps I’m barking up the wrong tree. Konfabulator is clearly geared to appeal to the Kaleidoscope crowd: tweakers who prefer to spend their time hacking pixels in Photoshop than hacking their actual source code.


## No IDE


What’s most perplexing to me is what Konfabulator does not include: an IDE. There is no visual widget editor or source code editor. They do include fairly comprehensive documentation on the widget XML structures and the supported JavaScript syntax, but when it comes to creating your own widgets, you’re on your own. [Arlo Rose, writing in the Konfabulator support forum](http://kmirror.deskmod.com/forums/viewtopic.php?p=1450#1450), wrote:


> Photoshop and BBEdit are your friends.  :-)
> We are working on a visual editor, but we are net [*sic*] yet sure when it will be released.


So they’re obviously aware of the need for an IDE. But I can’t help but think it would have been better had they waited for the IDE before they started selling Konfabulator. As it stands now, you need Konfabulator just to run a widget. Let’s say I have an idea for a widget-type application that does something very cool. I wouldn’t write it for Konfabulator, because I wouldn’t want to limit the audience to those who’ve paid $25 for Konfabulator.


It makes more sense to me to give away the runtime engine, and let everyone run widgets for free. Then charge money for the IDE (and charge a bit more than $25). This makes widget-writing more appealing — you can share your work with the whole wide Mac world, not just the pixel-tweaking Konfabulator Klub.


Plus, an IDE is sorely missing from a programmer’s standpoint. The Konfabulator widget format is open and documented, but that doesn’t mean it’s a pleasure to write. The main source file is an XML file with embedded JavaScript. You can include external JavaScript files, but that doesn’t make project management too much easier. Far worse is that you need to position each image in a window using pixel offsets specified in XML. Nothing cries out for a GUI more than this.


What’s needed is a REALbasic-style code editor and interface layout tool. Something to present source code one handler at a time. The “.kon” XML project file syntax is quite readable, which is good, but that doesn’t mean it shouldn’t be generated automatically by an IDE. Creating Konfabulator widgets isn’t hard in the way that differential equations are hard; it just looks like a pain in the ass.


Maybe it’s old age (I turn 30 next month), but I would have been happier if their work for version 1.0 had gone toward automating the construction of Konfabulator widgets, at expense of visual effects. I’d rather have plain-looking widgets that are easier to create. But, I suppose, I’m not in the Konfabulator target market.


[Note: I got Konfabulator’s price wrong in the first draft of this article (it costs $25, not $20). It has been corrected.]



| **Previous:** | [Operatic](https://daringfireball.net/2003/02/operatic) |
| **Next:** | [Flowers Are for Chumps](https://daringfireball.net/2003/02/flowers_are_for_chumps) |


PreviousNext