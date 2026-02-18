---
title: "The Airfoil Speakers Touch Situation"
date: 2009-11-13
url: https://daringfireball.net/2009/11/airfoil_touch_situation
slug: airfoil_touch_situation
word_count: 976
---


Regarding today’s [aforelinked](http://daringfireball.net/linked/2009/11/13/app-store-rogue-amoeba) tale from Rogue Amoeba regarding the [four-month-long process to get a minor bug-fix update to Airfoil Speakers Touch](http://www.rogueamoeba.com/utm/2009/11/13/airfoil-speakers-touch-1-0-1-finally-ships/) published on the App Store, several readers who insist upon defending Apple in this matter have pointed me to [Jeff LaMarche’s response](http://iphonedevelopment.blogspot.com/2009/11/rogue-amoeba.html). LaMarche writes:


> I’m going to risk the ire of the maddening crowd once more, but I
> think somebody needs to come to Apple’s defense this time. I love
> a good mob scene as much as the next guy, and I keep my pitchfork
> nice and sharp just in case the need should arise. But… the
> picture that Rogue Amoeba has painted in their farewell post
> doesn’t look quite so black and white to me. Certainly, Apple
> could have handled many things about the situation better, but so
> could have Rogue Amoeba. Let’s strip it down to the basics.
> Airfoil Speakers Touch included pictures of Apple products;
> These were images owned by Apple;
> The iPhone SDK Agreement specifically prohibits the use of
> images, icons, and logos owned by Apple in iPhone applications;
> The first rejection clearly and unambiguously stated why the
> app was being rejected and how it could be fixed.


There is much that is wrong with LaMarche’s synopsis.


Point 1 is simply wrong; the Airfoil Speakers Touch iPhone app does not contain any of these images. It contains no pictures of Apple computers. It contains no icons of Apple applications. It displays these images after they are sent across the network by Airfoil for Mac. Airfoil for Mac reads these images using [public official Mac OS X APIs](http://stackoverflow.com/questions/1381915/how-do-i-get-the-icon-of-the-users-mac). I.e. Airfoil Speakers Touch can only show a picture of the Mac it is connected to because the image is sent *from* the Mac it is connected to.


Point 3, I disagree with. I’ve just re-read the entire iPhone SDK Agreement (again), and I find no clause that prohibits what Airfoil Speakers Touch was doing. Here’s section 3.2 (d), which is perhaps what LaMarche is referring to (bold emphasis added):1


> (d) To the best of Your knowledge and belief, Your Application and
> Licensed Application Information do not and will not **violate**,
> **misappropriate**, or **infringe** any Apple or third party copyrights,
> trademarks, rights of privacy and publicity, trade secrets,
> patents, or other proprietary or legal rights (e.g. musical
> composition or performance rights, video rights, photography or
> image rights, logo rights, third party data rights, etc. for
> content and materials that may be included in Your Application);


One can argue that Airfoil Speakers Touch is somehow “violating”, “misappropriating”, or “infringing” on Apple trademarks here. I would strongly disagree, and argue instead that Airfoil Speakers Touch was using these images very much appropriately. And note that the SDK agreement does not state you cannot “use” Apple trademarks.


There’s also section 2.6:


> This Agreement does not grant You any rights to use any
> trademarks, logos or service marks belonging to Apple, including
> but not limited to the iPhone or iPod word marks. If You make
> reference to any Apple products or technology or use Apple’s
> trademarks, You agree to comply with the published guidelines at
> [http://www.apple.com/legal/trademark/guidelinesfor3rdparties.html](http://www.apple.com/legal/trademark/guidelinesfor3rdparties.html),
> as modified by Apple from time to time.


This clearly suggests that iPhone apps *can* make use of Apple trademarks, if they comply with the terms of Apple’s guidelines. I’ve read that document, too, and see no clause therein which would suggest that what Airfoil Speakers Touch was doing was in violation of the guidelines.


In his write-up regarding the situation, Rogue Amoeba’s Paul Kafasis includes this bit from their App Store rejection notice:


> Apple Logo and Apple-owned Graphic Symbols:
> You may not use the Apple Logo or any other Apple-owned graphic
> symbol, logo, or icon on or in connection with web sites,
> products, packaging, manuals, promotional/advertising materials,
> or for any other purpose except pursuant to an express written
> trademark license from Apple, such as a reseller agreement.


That’s less ambiguous. However, note that this language is not contained within the SDK agreement itself. The only way Rogue Amoeba got this language was by designing, building, and submitting the application that did it. (And this gets to LaMarche’s fourth point, wherein he claims the notice was “unambiguous”. It was not. It did not state where Rogue Amoeba had violated this rule. Was it the Mac icons? The app icons? Both? Rogue Amoeba was left to guess — and, when they asked for clarification, left to wait.)


Is Apple within their rights to reject this app for this reason? Sure. The bottom line is that they can reject apps for whatever reasons they want — that’s the rule that matters here. But was Rogue Amoeba foolish for designing their application this way? No. There’s nothing in the SDK agreement that they’ve violated.


It’s just good design. In UI design, just as in cinema, it is almost always better to *show* rather than *tell*. How else can you *show* which computer the Airfoil iPhone client is connected to? Apple certainly agrees with the design — showing an icon of the machine [is exactly how their own Remote app solves the same UI problem](http://daringfireball.net/misc/2009/11/iphone-remote-app.png). Obviously, the iPhone Remote app is Apple’s own app, so they can’t be accused of violating / misappropriating / infringing their own trademark. But if the de facto rule is “Apple can show a representation of the computer its iPhone apps connect to, but third-party developers can’t”, that doesn’t exactly refute Rogue Amoeba’s conclusion that developing for this platform just isn’t worth it.


---

1. I can’t link to the SDK agreement, as it resides behind the [iPhone Developer Portal](http://developer.apple.com/iphone/). ↩︎



| **Previous:** | [The Yankees](https://daringfireball.net/2009/11/the_yankees) |
| **Next:** | [Oh Joe You Didn’t](https://daringfireball.net/2009/11/oh_joe_you_didnt) |


PreviousNext