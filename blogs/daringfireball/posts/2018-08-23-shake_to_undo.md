---
title: "On ‘Shake to Undo’"
date: 2018-08-23
url: https://daringfireball.net/2018/08/shake_to_undo
slug: shake_to_undo
word_count: 548
---


[Jeff Carlson on Twitter yesterday](https://twitter.com/jeffcarlson/status/1032147470287925249):


> So many years in, and shake-to-undo is still one of the worst, stupidest ideas in iOS.


[Scott Knaster](https://twitter.com/scottknaster/status/1032307623176024064):


> @jeffcarlson Yes and no. It’s a weird and little-known UI, but it
> recently saved a family member a ton of lost work. When I told
> them to “shake it like a Polaroid picture”, they thought I was
> kidding. Then, when it worked, they were ecstatically happy.


The fact that system-wide Undo exists in iOS is great. (Android doesn’t have it.) But that it’s a shake gesture is dreadful — impossible to discover through exploration of the on-screen UI, bad for accessibility, and risks your phone flying out of your hand. How many iOS users even know about Shake to Undo? Very few, I suspect.


The iPad does a little better, with an Undo button above the keyboard (screenshots from [iOS 11](https://daringfireball.net/misc/2018/08/ipad-ios11-undo.jpg) and [iOS 12](https://daringfireball.net/misc/2018/08/ipad-ios12-undo.jpg)). But these buttons only work in text editing scenarios. Text editing may well be the most common task where Undo is used, but still, that falls short of what the Mac has had ever since 1984 — a single, standard, universally available Edit → Undo menu command with a standard keyboard shortcut. Undo is just as universal and consistent on Windows, as well.


You can use the ⌘Z shortcut on iOS when you have a hardware keyboard connected — but especially on the iPhone, that’s rare. And, to be clear, there are some iOS apps that have some sort of counterclockwise circular arrow button — something like “⟲” — in a toolbar or floating button to undo non-text-editing actions. But they’re not universal and they’re far from consistent.


There are lots of little things like this about iOS. It’s a tricky problem how to implement universal Undo without a menu bar and without keyboard shortcuts. Even Cut/Copy/Paste were tricky enough that it took until iOS 3 for the iPhone to get them. That’s why the menu bar and keyboard shortcuts are such essential elements of the Mac experience.


Shake to Undo is problematic enough that I think Apple should have figured out something better for the iPhone by now. (For accessibility reasons, you can turn Shake to Undo off, but if you do, you don’t have any Undo at all.) My best suggestion would be to take away some space from the auto-suggestion row above the keyboard and put in an Undo button on the left, just like the iPad.


Lastly, here’s an anecdote I heard years ago about how Shake to Undo came to be. Scott Forstall charged the iOS team with devising an interface for Undo — everyone knew the iPhone *should* have it,1 but no one had a good idea how to do it. One engineer joked that they could just make you shake the iPhone to invoke it. Forstall said he loved the idea, and what was proposed as a joke has been with us as the Undo interface ever since.


---

1. Undo was considered so essential to the Newton that [it was a permanent hardware button at the bottom of the display](https://daringfireball.net/misc/2018/08/newton-undo.jpg). ↩︎



| **Previous:** | [Let’s Really Think About This ‘New Low-Cost Laptop to Succeed MacBook Air’ Thing](https://daringfireball.net/2018/08/new_low-cost_laptop_to_succeed_macbook_air) |
| **Next:** | [iPhone Naming Rumors, 2018 Edition](https://daringfireball.net/2018/09/iphone_xxx) |


PreviousNext