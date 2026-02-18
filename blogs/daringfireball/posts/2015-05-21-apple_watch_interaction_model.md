---
title: "On the Apple Watch Interaction Model and the Digital Crown"
date: 2015-05-21
url: https://daringfireball.net/2015/05/apple_watch_interaction_model
slug: apple_watch_interaction_model
word_count: 1561
---


[Steven Berlin Johnson finds the digital crown button convoluted](https://medium.com/backchannel/for-the-apple-watch-there-s-no-place-like-home-and-that-s-a-problem-b37810b6fd34):


> If you press this button, these are the potential events that will
> transpire on your Watch’s screen:
> You’ll be taken to the “watch face” view.
> You’ll be taken to the “home screen” app view.
> You’ll stay in the “home screen” view, but it will re-center on
> the “watch face” app.
> You’ll move from a detailed view of a notification back to the
> notifications summary.


His proposed solution:


> Fortunately there is an easy fix for this confusion, which is to
> streamline the Digital Crown so that it focuses exclusively on the
> Watch’s two homes. Pressing the Digital Crown should simply toggle
> you back and forth between the “watch face” and the “home screen.”
> (Its other functionality could all be achieved through other
> means; for instance, you can already re-orient the “home screen”
> simply by dragging your finger across the Watch’s screen.) That’s
> still more complicated than the iPhone home button, but it’s the
> kind of thing most users would pick up in a matter of minutes
> using the Watch. And it has a conceptual clarity that is sorely
> lacking in the current design.


His whole piece is worth reading, because it aptly describes, almost exactly, how I felt about Apple Watch after using it for just a few days. Several of his complaints, which I would have agreed with in my first few days of Apple Watch use, I no longer consider problems.1 And even now, with seven weeks of daily Apple Watch experience under my belt, when I first read his suggestion for simplifying the digital crown button, I was nodding my head in agreement. But when I sat down to write about it, I realized there’s really only one small thing I would suggest Apple change: the last of its four roles noted by Johnson — its function as a hardware “back” button while looking at the detail view for a notification.


Otherwise, I would keep the functionality of the crown button as-is:

- If the watch display is off, pressing the crown wakes it up.
- If the watch is showing your glances or notifications, pressing the crown takes you back to the watch face.
- If the watch is displaying your watch face, pressing the crown switches you to the home screen showing all your apps.
- If you’re using any app, pressing the crown takes you back to the home screen, with the view centered on the app you just left.
- If the watch is on your home screen and the clock app is not centered, pressing it will re-center.
- If the watch is on the home screen, centered on the clock, pressing it will switch you to the watch face.


That looks more complicated than it is. And I’m even leaving out at least one other scenario: when you’ve put your home screen into edit mode — where you can delete and rearrange the installed apps — pressing the crown takes you out of editing mode.


Here’s a better way to think about it — and without *thinking* about it, the reason why I think most people aren’t frustrated or confused by the crown button after a week or so. It’s best to think of Apple Watch as having two modes: watch mode, and app mode.


You do not need to understand this to use the watch. Most Apple Watch owners will never really think about this. But this idea of two modes is central to understanding the design of the overall interaction model.


Watch mode:

- Shows your watch face by default.
- Swipe down for notifications.
- Swipe up for glances.
- Tap a complication — date, weather, activity — to launch its corresponding app.
- Tap a glance to open to the corresponding app.
- Force tap to switch or edit watch faces.


App mode:

- Shows your home screen, centered on the clock app, by default.
- No notification list or glances.
- Tap an app to open it.
- Long-tap on the home screen to open editing mode.


Watch mode is where you take quick glances at information and notifications; app mode is where you go to “do something”. Watch mode is where most people will spend the majority — perhaps the overwhelming majority — of their time using Apple Watch. App mode is a simple one-level hierarchy for “everything else”.


If you think about Apple Watch as having these two modes, the role of the crown button is clear:

- From the “default” view of either mode, the crown button switches you to the other mode.
- From anywhere else, the crown button takes you to the default view of the *current* mode. (There’s a slight exception here in app mode: if you’re using an app, pressing the crown first takes you to the home screen centered on the app you were just using, and you have to press it again to center the home screen on the clock app.)


Consider: What happens when you press the digital crown button while in, say, the Weather app? The answer is: It depends how you got there. If you start from the home screen and tap the Weather app icon, the digital crown button returns you to the home screen. If you start from the watch face, though, and launch the full Weather app by tapping the Weather glance, then the digital crown button returns you to the watch face.


This sounds confusing. And if you’re expecting Apple Watch’s digital crown button to work like iOS’s home button, it is not the expected behavior. But in practice, I think it works very well. I suspect this arrangement wasn’t designed in advance but was instead the result of many months of play-testing by the designers on the Apple Watch team.


Again, I agree with Johnson that if you’re looking at a notification detail view, the crown should take you all the way back to the watch face. You have to tap on screen to get into a notification detail view, and they all have a large “Dismiss” button at the bottom if going “back” is what you want. “Back” just doesn’t feel right for the digital crown button. It should simply mean *go home in the current mode*, or, if you’re already home, *switch to the other mode*.


I don’t mind the “re-center and re-zoom on the clock app” extra action for the digital crown button. To me, it’s directly analogous to the way the home button takes you back to the first home screen in iOS. More importantly, you don’t have to go back to the watch face (or, as I’m referencing it here, watch “mode”). That just happens automatically when you lower your wrist and stay away from the watch for 30 seconds. You don’t have to “clean up” and go back to the watch face manually. It just happens automatically when you stop using the watch. A few special apps behave otherwise — Workout and Remote, so far — but in both of those cases that makes sense. And, yes, there is a setting (General → Activate on Wrist Raise → Resume To) that allows you to always return to the last-used app, but I don’t see why anyone would use that unless they stubbornly insist upon treating their Apple Watch like a miniature iPhone. Another way to think of this option is as a toggle between treating “watch mode” and “app mode” as the *primary* mode.


Another insight: the side button exists outside either mode. It behaves the same way no matter which mode you’re in, no matter what you’re doing. One press of the side button brings up your Friends circle. A double-press initiates Apple Pay. In either case — Friends circle or Apple Pay — pressing (or double-pressing) the digital crown button dismisses the side button mode you entered.


---

1. For example, the idea that you should be able to swipe up from anywhere — not just from the watch face — to see glances. A lot of people seem to have this complaint early on. The thought had occurred to me, too. But it clearly wouldn’t work. In other contexts, swiping your finger up on the display scrolls the content, including the home screen, where you need to pan around to see all your apps. Apple would only enable glances globally if they forced you to use the digital crown for scrolling, or, if they enabled glances only as a swipe up from the very bottom edge of the display. Notification Center and Control Center work that way on iOS, which allows them not to conflict with regular old scrolling and panning. But I’m nearly certain that the watch display is too small to make that distinction. You’d find yourself scrolling when you wanted to bring up Glances and bringing up Glances when you wanted to scroll. It’d be maddening. The Watch OS “back” shortcut — swiping from the left to go back in a view hierarchy — *is* an edge gesture, but that’s OK because if you miss the edge, nothing happens. ↩︎



| **Previous:** | [Facebook Introduces Instant Articles](https://daringfireball.net/2015/05/facebook_instant_articles) |
| **Next:** | [On Jony Ive’s Promotion to Chief Design Officer](https://daringfireball.net/2015/05/jony_ive_promotion_chief_design_officer) |


PreviousNext