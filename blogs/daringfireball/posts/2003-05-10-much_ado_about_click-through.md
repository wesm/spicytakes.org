---
title: "Much Ado About Click-Through"
date: 2003-05-10
url: https://daringfireball.net/2003/05/much_ado_about_click-through
slug: much_ado_about_click-through
word_count: 2019
---


[Matthew Thomas weighs in on the click-through debate](http://web.archive.org/web/20041019075909/http://mpt.phrasewise.com/2003/05/09). His arguments against pervasive click-through are so clearly stated as to make it seem like shooting fish in a barrel.


MPT correctly zings me with a “[sic]” for having used the word “invariably” to describe how Mac apps disable controls that don’t support click-through in background windows. Sadly, even though it is usually the case, it’s not invariable, as he proves by pointing to [this bug logged against Mozilla](http://bugzilla.mozilla.org/show_bug.cgi?id=54488). But much more damning are similar bugs in *Apple’s own applications*, such as the following [bug in Address Book, as described by Pierre Igot](http://www.latext.com/blog/2003/05/08.html#a266):


> Yet when I click on this seemingly active control, it just switches me to Address Book. Once in Address Book, I have to click on it again to change the view mode. 
> In other words, it doesn’t support click-through (and that’s a good thing) even though it looks like it does (and that’s a bad thing). 
> There are such inconsistencies all over the place. Time to do some house-cleaning, Apple!


House-cleaning time at Apple, indeed. MPT comes to a similar conclusion:


> However, defaults are important, and this is just as much the case for developers as it is for users. APIs can be designed to encourage, [discourage](http://bugzilla.mozilla.org/show_bug.cgi?id=59820), or even [prohibit](http://bugzilla.mozilla.org/show_bug.cgi?id=95649) good user interface design by developers. And on Mac OS X, it appears, the defaults for click-through behavior are a shambles.


(MPT also gripes about my having associated click-through with application-centricity, but in my defense, I *did* include the phrase “wildly tangential digression” in that section’s subtitle.)


## Only Nixon Could Go to China


No matter which side of the click-through argument you stand on — and I’m still getting a trickle of email from readers who don’t see what’s wrong with it — there can be no dispute that the current situation on Mac OS X is bad, simply because there’s no consistency. Some apps go one way, some go the other.


In the course of disputing the belief that click-through is a Carbon/Cocoa issue, I pointed out that individual developers using either API have complete control over click-through behavior. For example, even though it’s on by default in Cocoa toolbars, developers can turn it off if they choose to — but not easily.


But that’s not a solution to either problem: that click-through behavior should be consistent system-wide; and that the aforementioned consistent click-through behavior should be off by default, and on only for certain situations.


The sad truth is that click-through is mostly on by default in Cocoa applications. So what’s wrong with the idea of each savvy developer fixing click-through behavior in their own apps? As one friend aptly wrote via email, “You can’t plug leaks in this dam one hole at a time.”


Only Apple can fix this. Where by “fixing it”, I mean three things, all essential:

1. Mandate correct click-through behavior in the [HIG](http://developer.apple.com/techpubs/macosx/Essentials/AquaHIGuidelines/AHIGWindows/chapter_5_section_11.html).
2. Make Apple’s Cocoa frameworks do the right thing by default. Supply
	sufficient API hooks so that it’s easy for third-party frameworks to
	do the right thing.
3. All of Apple’s own software needs to follow these guidelines.


Point-by-point, why these three steps are each important:


## Mandating Against Pervasive Click-Through in the HIG


By setting clear guidelines in the HIG, Apple sets the mandate for all that follows. The guidelines in the HIG should never be determined by politics — they should be objectively determined with the best interests of usability in mind. The arguments against pervasive click-through are overwhelming, and the HIG should reflect this. As it stands today, it doesn’t.


I’ll make one last attempt to pound anti-click-through-ism through the heads of disbelievers, on the basis of Fitts’s Law. Quoting from [Bruce Tognazzini’s definition of Fitts’s Law](http://www.asktog.com/basics/firstPrinciples.html#fitts's%20law):


> The time to acquire a target is a function of the distance to and size of the target. 
> While at first glance, this law might seem patently obvious, it is one of the most ignored principles in design. Fitts’s Law dictates the Macintosh pull-down menu acquisition should be approximately five times faster than Windows menu acquisition, and this is proven out. Fitts’s Law dictates that the Windows task bar will constantly and unnecessarily get in people’s way, and this is proven out. Fitts’s Law indicates that the most quickly accessed targets on any computer display are the four corners of the screen, because of their pinning action, and yet they seem to be avoided at all costs by designers.
> Use large objects for important functions (Big buttons are faster).


A background window is, effectively, a button you can click on to bring it to the front. Or at least, the visible region of the background window. If you arrange your windows appropriately, you end up with very large “buttons” for switching between windows. Switching between windows is something that people do frequently, and thus it is a usability advantage to make this action as easy as possible.


Click-through defeats this. Instead of a large rectangular-shaped “button” in which you can click anywhere to bring that window forward, you end up with an irregularly-shaped region in which you must carefully avoid the click-through enabled buttons. It’s not even like having holes in a button — it’s like having smaller buttons (the click-through regions) on top of a larger button (the visible region of the window where you can click to bring it forward). You don’t have to be careful at all when clicking to activate windows that don’t support click-through.


The window-switching penalty caused by click-through is the type of usability 
hiccup that goes completely unnoticed by 99.9 percent of people. But even when users don’t *consciously* notice usability problems, the problems still shape the users’ behavior via conditioning. Millions of Windows users have no idea why they decide to run their applications in full-screen mode, but that doesn’t mean their behavior isn’t explained by Windows’s UI deficiencies (which in this case are in large part attributable to Windows’s widespread click-through).


If Mac OS X continues to move toward widespread click-through support, Mac users will become conditioned not to click on background windows at all. For example: a Mac user is using Safari, and she decides to check her email. She sees the main window for Mail in background, above her Safari window. She clicks on it, but happens to hit the Compose button in Mail’s toolbar. She only wanted to see if she’d received any new messages, but now she has a new message window — that she never wanted — to dismiss. It’s not a catastrophe, but it is an annoyance.


But unless she’s the sort of nerd who reads Daring Fireball, she’s not going to bother thinking about exactly what just happened, and why she ended up with an unwanted new message window. She’s just going to think that her computer annoyed her. And if she continues to get annoyed when clicking on Mail’s main window — even though it only happens occasionally — she’s going to become hesitant to do so at all, probably without ever making a conscious decision about it. Maybe she’s start clicking on Mail’s Dock icon instead. Maybe she’ll use the Cmd-Tab keyboard shortcut. But whatever, she’ll have stopped using the easiest method to switch between visible windows.


The problems that result from unintended click-through appear *random* to most people. This is not because they’re stupid, but because they’re simply not at all interested in learning the details of how their computer works.


Design is nearly always about evaluating trade-offs. Yes, the lack of click-through is a small annoyance when you really do want to click on a button that is visible in a background window. But when click-through is enabled, the convenience of being able to immediately invoke a background window’s buttons does not compensate for the penalty you must pay when you simply want to bring that window forward.


Developers not only need to trust that the HIG contains the *correct* answers to problems like how to implement click-through — they need for the HIG to contain answers, period. [As it stands now](http://developer.apple.com/techpubs/macosx/Essentials/AquaHIGuidelines/AHIGWindows/chapter_5_section_11.html), the HIG more or less states that developers can do what they want regarding click-through. That’s worse than giving the wrong answer. The purpose of the HIG is to promote and describe a consistent and usable user interface across all applications. A policy of *You can implement click-through if you want to* promotes neither consistency nor usability.


It would be foolish to dismiss click-through guidelines as being too esoteric to worry about. Admittedly, most Mac users are never going to proclaim that they use a Mac because it adheres to a consistent well-designed click-through policy. But they *do* proclaim that they use a Mac because it seldom does things to annoy them.


The details *do* matter, at least on the Mac OS, the entire success of which is based on getting small details right. Pervasive click-through leads to usability paper cuts. That it’s possible never to get such a paper cut — by taking care always to click carefully in background windows — does not mean this isn’t a usability problem.


Like so many Mac OS usability advantages, proper click-through won’t lead to Mac users possessing features unavailable to Windows users. It just means they’ll suffer fewer annoyances. It is not so much about *being better*, as it is about *sucking less*.


## Implement Proper Click-Through as Default Behavior in Cocoa


Once the HIG’s click-through policy is fixed, it follows that Cocoa should be updated to adhere to the new guidelines.


The whole point of Cocoa is that it handles so many of the low-level details which, in the days of yesteryear, Mac OS programmers needed to handle by hand. Modern Carbon applications get some of this for free now, but Cocoa applications get it all for free: everything from cut/copy/paste in text fields to a working About box.


If Apple were to update Cocoa with refined click-through behavior, Cocoa developers using default behavior would pick up these improvements for free. Click-through behavior across nearly all Cocoa applications would improve, without any additional programming effort from individual developers. This is an example of exactly why Cocoa is so heavily touted.


It’s also the case that many developers are good at programming, but not good at UI design. The more details Cocoa’s frameworks get right by default, the fewer details developers need to worry about.


## Apple’s Own Software


It’s plainly obvious that Apple’s own software should adhere to the HIG. A policy of *Do what I say, not what I do* does not make for credible leadership. As it stands, Apple’s application design remains very good, but it used to be impeccable.


Even developers who want to do the right thing don’t necessarily read the HIG cover-to-cover. An example can be worth a thousand words — being able to refer to Apple’s own applications for guidance would be a tremendous boon. E.g., a developer might think, *Safari’s bookmark window does something similar to what I have in mind, let me see how they do this…*.


## Postscript: Click-Through on Command


[Sven-S. Porst](http://earthlingsoft.net/ssp/blog/) points out [a very nifty click-through shortcut in Cocoa](http://earthlingsoft.net/ssp/blog/archives/week_2003_05_04.html#000398) that I wasn’t aware of:


> One thing I’d like to add on the topic of click-through is that while it had been possible for ages in MacOS to drag background windows without activating them by holding the command-key while doing so, support for this background manipulation has improved in OS X. In Cocoa applications you can command-click most controls and use them without activating the window first. I like that. Click-through for the people who want and it and can handle it. It’s far from perfect, though, as it doesn’t work uniformly through all applications and doesn’t work for toolbar items either as the command-key is used for moving items there. But toolbars should be banned anyway.


Imperfections aside, this strikes me as quite a nifty shortcut, in that it’s very unlikely to ever get in your way by accident.



| **Previous:** | [The Problems With Click-Through](https://daringfireball.net/2003/05/the_problems_with_click-through) |
| **Next:** | [Safari’s Unscriptable Tabs](https://daringfireball.net/2003/05/safaris_unscriptable_tabs) |


PreviousNext