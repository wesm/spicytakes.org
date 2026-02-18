---
title: "Let the Tea Leaf Reading Begin"
date: 2007-10-19
url: https://daringfireball.net/2007/10/tea_leaf_reading
slug: tea_leaf_reading
word_count: 2408
---


The best thing about being an Apple observer is that even when the company does make a long-awaited announcement, it inevitably leads to new questions regarding what exactly they mean. Apple punditry is the [Kremlinology](http://en.wikipedia.org/wiki/Kremlinology) of the tech world.


So it is with [this week’s announcement from Steve Jobs](https://web.archive.org/web/20071018221832/https://www.apple.com/hotnews/)1 that, yes, “We want native third party applications on the iPhone, and we plan to have an SDK in developers’ hands in February.”


We now know two new things: (1) that there will be “native third party applications on the iPhone”; and (2) that the SDK is scheduled for February. That leaves a long list of questions.


## Whither Widgets?


For one: What exactly is a “native third party application”? The obvious answer is the sort of UIKit-based Cocoa-ish applications that underground iPhone hackers have been creating over the last two months — the exact sort of native apps that Apple has itself already written for the iPhone and iPod Touch.


For all we know at this point, though, it could be something more like Dashboard widgets — but I think that’s unlikely.


Jobs wrote:


> With our revolutionary multi-touch interface, powerful
> hardware and advanced software architecture, we believe we
> have created the best mobile platform ever for developers.


JavaScript, HTML, and CSS are cool in that they’re widely-used, widely-known coding standards — but they’re not a good way to create user experiences that take full advantage of the iPhone, and would be pretty hard for Apple to pass off as an SDK for “native apps”. Third party developers want access to the same dog food Apple’s own iPhone engineers are eating.


Plus, there’s the issue of performance. [Iconfactory](http://iconfactory.com/) developer Craig Hockenberry, who has been tinkering with the unofficial iPhone developer tools to create an iPhone-native version of [Twitterrific](http://iconfactory.com/software/twitterrific), wrote a splendid weblog entry titled “[Benchmarking in Your Pants](http://furbo.org/2007/08/15/benchmarking-in-your-pants/)” regarding the lackluster performance of JavaScript code running in MobileSafari compared to compiled Objective-C code running in a native iPhone app. Function calls, for example, were 226 times slower in JavaScript. (Hockenberry also benchmarked JavaScript running on the iPhone compared to the same code running in Safari on an Intel-based iMac; the code ran about 80 times faster on the iMac.)


Back in January at the iPhone’s introduction in the Macworld Expo keynote, Jobs described some of the apps on the iPhone, including Weather and Stocks, as “widgets”. My somewhat-informed understanding is that Apple’s original plan was for the iPhone to ship with its major apps written in Cocoa and with a handful of smaller apps written as Dashboard-style HTML/CSS/JavaScript widgets — but that this plan was scuttled for performance reasons, and the Weather and Stocks widgets2 were rewritten as UIKit Objective-C apps sometime this spring.3 My guess is that they ran into what Hockenberry documented: JavaScript on the current iPhone just isn’t fast enough to provide an iPhone-caliber user experience.


So my money is that the iPhone SDK that Apple plans to release this winter is the real thing — Cocoa-style UIKit apps written in Objective-C.


## Security?


Jobs wrote:


> It will take until February to release an SDK because we’re trying
> to do two diametrically opposed things at once—provide an advanced
> and open platform to developers while at the same time protect
> iPhone users from viruses, malware, privacy attacks, etc. This is
> no easy task. Some claim that viruses and malware are not a
> problem on mobile phones—this is simply not true. There have been
> serious viruses on other mobile phones already, including some
> that silently spread from phone to phone over the cell network. As
> our phones become more powerful, these malicious programs will
> become more dangerous. And since the iPhone is the most advanced
> phone ever, it will be a highly visible target.


External security — the threat of vulnerabilities that would allow malfeasants to compromise a victim’s iPhone — is a serious matter. There have already been several published exploits against the iPhone, including an as-of-this-writing [open vulnerability in TIFF-processing code](http://blog.metasploit.com/2007/10/cracking-iphone-part-21.html) in the current iPhone OS.


So clearly there is some merit to Jobs’s stated security concerns. As it stands in the current iPhone OS, all processes run as the root user; in broad layman’s terms, any process has access to everything else on the phone. So when a buffer overflow can be exploited to allow remote code execution, that code can do anything. To allow third-party iPhone apps to run today would be to trust those third-party developers not to write code with any security flaws.


What the iPhone needs before Apple will allow third-party apps to run is some sort of sandbox, a way to prevent application processes from being able to access things they shouldn’t be allowed to access. But iPhone Cocoa apps are no more inherently susceptible to buffer overflow vulnerabilities than Mac Cocoa apps.


And the [hysteria](http://www.eweek.com/article2/0,1759,2191348,00.asp) over the iPhone’s current “everything runs as root” situation is overblown.4 Applications on your Mac don’t run as root; they run under your user account. But all of your data — your email, your address book, your documents, everything your apps can read or write without administrator authentication — is vulnerable to any sort of hypothetical buffer overflow exploit on the Mac, and would be on the iPhone, too, even if iPhone apps didn’t all run as root. Sure, root privileges allow an exploit to do *anything*, but the most important thing on your system is your personal data, and an exploit doesn’t need root privileges to access that.


I’m thinking Apple is more concerned about *internal* security — about having third-party apps limited to a sandbox so that user-installed code has no access to things like, say, the phone network modem’s firmware (the component that you need to diddle with to create SIM unlocks).  That’s the key difference between the iPhone and the Mac, security-wise.


## Which Third-Party Developers?


Mac OS X is pretty much completely open to development; even the developer tools are free, and anyone is free to write whatever software they want for the Mac. It seems unlikely that iPhone OS X development is going to be like that.


One possibility is that the iPhone SDK will only be available to developers with [ADC](http://developer.apple.com/) Select ($499) or Premiere ($3,499) accounts. (Premier and Select ADC members are the only ones with access to pre-release Mac OS X seeds, for example.) If that’s the case, it’s not going to be popular with hobbyist developers, but most professional Mac developers already have paid ADC memberships, and, let’s face it, we all know most iPhone apps are going to be written by Mac developers.


Interviewed via email, Craig Hockenberry told me, “If there’s a simple way to get third party apps on the iPhone, you keep 90 percent of the developers happy and jailbreak/unlock has much less momentum. Sure, there will still be people that want to ‘buck the system’ but they’ll be in the minority rather than the majority.”


The most intriguing part of Jobs’s announcement was this section, regarding security:


> Some companies are already taking action. Nokia, for example, is not
> allowing any applications to be loaded onto some of their newest
> phones unless they have a digital signature that can be traced back
> to a known developer. While this makes such a phone less than
> “totally open,” we believe it is a step in the right direction. We
> are working on an advanced system which will offer developers broad
> access to natively program the iPhone’s amazing software platform
> while at the same time protecting users from malicious programs.


It’s hard not to interpret the scare quotes around “totally open” as a reference to Nokia’s recent [“Open to Anything” ad campaign](http://gizmodo.com/gadgets/iphone-vs-n95/nokia-taunts-apple-with-new-open-to-anything-n95-campaign-305525.php) — sort of a *you guys aren’t completely open either* call-out. This seems like a pretty clear indication that Apple is working on a similar signing system for iPhone apps. Restricting development to paid ADC members would instantly allow Apple to associate app signatures “back to a known developer”.


Here’s [more information from Nokia](http://wiki.forum.nokia.com/index.php/Application_Signing) on the signing program Jobs mentioned; here’s [similar information on the Symbian site](https://www.symbiansigned.com/app/page/EndUserStatement).


## Which Apps?


Another question is whether Apple is going to allow participating (trusted-by-Apple) developers to write whatever apps they want, signing the apps themselves, or if apps will need to be approved case-by-case by Apple before being signed.


Mac OS X Leopard includes a new “application signing” feature, described by Apple [thusly](http://www.apple.com/macosx/features/300.html#security):


> A digital signature on an application verifies its identity and
> ensures its integrity. All applications shipped with Leopard are
> signed by Apple, and third-party software developers can also sign
> their applications.


That same page describes a “sandboxing” feature that seems applicable to the iPhone, too:


> Sandboxing prevents hackers from hijacking applications to run
> their own code by making sure applications only do what they’re
> intended to do. It restricts an application’s file access, network
> access, and ability to launch other applications.”


The prototypical example of a potentially popular app that Apple might refuse to approve would be a VOIP app like, say, Skype, in that it would undermine the need for the phone network, which in turn undermines Apple’s revenue sharing with the iPhone’s exclusive network partners. Or, say, instant messaging, the omission of which from the current iPhone is seen by many as a concession to the fact that heavy SMS users pay handsomely for extra monthly messages. (Personally, I suspect iChat for iPhone simply didn’t make the cut for 1.0 but is planned for a future update.)


“Nokia’s model is to run as trusted/untrusted,” said Hockenberry. “Trusted apps get to access more than untrusted ones. This model could be extended to allow different levels of access based upon whatever Apple wants (as owner of the root certificate.) Basic access for Wi-Fi, extended access for EDGE, hardware access for deep pockets, etc.”


That makes sense, and strikes me as a likely course for Apple.


## Development


There’s a question, then, of how developers will write the apps in the first place. If iPhones only run third-party apps that have been approved by Apple, how do you develop an application in the first place before it’s been approved?


Steven Frank — who, as co-founder of [Panic](http://panic.com/) and an [unrepentant gadget hound](http://stevenf.com/2007/07/the_official_stevenf_iphone_review.php), may well be the single most interested person in the world in a supported iPhone SDK — described to me via email the development process for the Danger Hiptop/Sidekick: “The Hiptop/Sidekick platform has a Java SDK that abstracts away all the low-level hardware stuff so you can’t touch it, while still providing everything you need to write an application.  You test and debug in an emulator/virtual machine that can simulate edge conditions like loss of cellular network availability and so on.  When you’re almost done, and ready to try on real hardware, you apply for a ‘developer key’, which is a small certificate that you install on the phone that enables you to run third-party apps that didn’t come from the on-device for-purchase catalog.  To get the developer key, you have to prove to them you actually have an almost complete app, and aren’t just some kid who wants hot Yung Joc ringtones by submitting a build of your application.  You also have to sign a waiver that says you are no longer eligible for support from your cellular carrier.”


## The iTunes App Store?


Which leaves us with the question of distribution and installation. The obvious route is the same one Apple has taken with iPod games: the iTunes Store. Apple, in this case, would likely get a cut of every sale. From a user’s perspective, it’d be easy and obvious: shop and pay for apps in iTunes, and iTunes takes care of installing the software, and, perhaps, synching data.


This is similar to the Danger model — where apps must be approved, and can be sold only through the official channel. Limiting, to be sure, but as Frank put it, “The process [of developing for Danger] is somewhat tedious, but still an order of magnitude better than not allowing third-party applications, period.”


Frank also pointed out the most glaring downside of Danger’s pay-to-play development model: “One drawback to this approach from the user’s perspective is that there is basically no free third-party software. Everything costs at least a couple bucks.”


---

1. The announcement appeared on Apple’s Hot News web page, but with no permalink, so it’s likely to disappear from Apple’s web site in a week or two as newer items appear. I’ve saved a plain text copy [here](https://daringfireball.net/misc/2007/10/third-party-apps-on-iphone.text) for posterity. ↩︎
2. I wonder if the Calculator app was originally a widget, too. UI-wise, it’d certainly be a cinch, because just like with the iPhone’s Weather and Stocks apps, it more or less looks and acts exactly like the corresponding widget in Mac OS X. So my theory is that when Apple made the decision to rewrite the iPhone widgets as native iPhone Cocoa apps, they used the widgets as the specs for the apps. “Make a native app that looks and acts exactly like this widget,” more or less. One thing that makes me think this is that the iPhone Calculator app doesn’t make any sounds when you press the buttons. Pure JavaScript/HTML widgets can’t make sounds when you click or tap buttons. I find typing on the iPhone keyboard to be much more satisfying with the sound on; with the sound off, because the keys are virtual, there’s no sensory feedback at all. The Calculator app would feel more *real* if it simply made the same button-clicking noises as the iPhone keyboard. ↩︎
3. That this change was — I believe — made rather late in the game might explain why [vestigial references to “widgets”](http://www.google.com/search?q=iphone+springboard+/widgets) remained in the shipping iPhone 1.0 software. (It could also mean, of course, that Apple plans to re-expose this feature at some point in the future.) ↩︎
4. It certainly is a curious question [why](http://www.google.com/search?hl=en&q=iphone+apps+run+as+root) all iPhone apps run as root. I don’t know the answer. But I’ll bet there’s an interesting engineering trade-off involved somewhere. If you think the reason is laziness or ignorance on the part of the iPhone OS X engineers, you’re an idiot. ↩︎



| **Previous:** | [Pre-Order Leopard Via DF Amazon Affiliate Links](https://daringfireball.net/2007/10/preorder_leopard) |
| **Next:** | [The iPhone and Web Apps](https://daringfireball.net/2007/10/iphone_web_apps) |


PreviousNext