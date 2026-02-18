---
title: "One Week Out, Some Brief Thoughts and Observations on WWDC 2025"
date: 2025-06-19
url: https://daringfireball.net/2025/06/some_brief_thoughts_and_observations_on_wwdc_2025
slug: some_brief_thoughts_and_observations_on_wwdc_2025
word_count: 2010
---


“*This one a long time have I watched. All his life has he looked away — to the future, to the horizon. Never his mind on where he was. What he was doing. Adventure. Heh! Excitement. Heh! A Jedi craves not these things. You are reckless!*”


My biggest takeaway from WWDC 2025 is that Apple seemingly took some lessons to heart from [its unfulfilled promises](https://daringfireball.net/2025/03/apple_is_delaying_the_more_personalized_siri_apple_intelligence_features) of a year ago. This year’s WWDC wasn’t merely focused on what Apple is confident it can ship in the next 12 months, but on what they can ship *this fall*. I might be overlooking a minor exception or two, but every major feature announced in [the WWDC 2025 keynote](https://developer.apple.com/videos/play/wwdc2025/101/) was both demonstratable in product briefings, *and* is currently available in the developer beta seeds. I was also told, explicitly, by Apple executives, that Apple plans to ship everything shown last week in the fall.


That’s as it should be, and a strong return to form for the company. It takes confidence to promise only what you know you can ship, and it takes execution to ship what you’ve promised. If there’s more coming in the early months of 2026, announce those features when they’re ready. It’s proven very effective for Apple to spread the debut of new features across the entire calendar year, with many major features not appearing until the .3, .4, or even .5 OS releases. I think it will prove just as effective marketing-wise to spread the *announcement* of more features throughout the year as well.


## Year-Based Version Numbers


There’s no question that it’s a little weird for every one of Apple’s platforms to have jumped to version 26. I mean, VisionOS skipped 23 version numbers. Presumably, when Apple next unveils a new OS (HomeOS?), it’s going to *start* at version 26, 27, or 28. But I’m already getting used to this, and I think the underlying logic laid out by Craig Federighi at the outset of the keynote is true: with Apple now up to six developer platforms (Mac, iPhone, iPad, Vision, TV, Watch), it had gotten hard to keep track of which version numbers corresponded to the same year. That matters not just for the convenience of knowing, in years to come, when specific versions of each OS were released, but it also matters because none of these platforms exist in isolation. They’re all parts of a cohesive whole, a cross-device “Apple OS 26” experience, as it were.


One thing I haven’t seen commented on, though, is that switching to year-based version numbers establishes as de facto policy something that has now been true for quite a few years, but which Apple has never officially acknowledged: that each of these platforms will get a major version release annually. 20 years ago the update schedule for Mac OS X was rather erratic:



| Mac OS X 10.7 Lion | July 2011 |
| Mac OS X 10.6 Snow Leopard | August 2009 |
| Mac OS X 10.5 Leopard | October 2007 |
| Mac OS X 10.4 Tiger | April 2005 |
| Mac OS X 10.3 Panther | October 2003 |



OS X 10.8 Mountain Lion (which began the odd four-year run where the Mac’s OS name didn’t contain “Mac”) arrived in July 2012, and thereafter a new major version has shipped in September, October, or November (MacOS 11 Big Sur, in 2020) every single year. This rigorous annual schedule is a hallmark of the Tim Cook era at Apple, and clearly reflects his personality (as the erratic/idiosyncratic schedule of the mid-2000s reflected Steve Jobs’s).


## iPadOS Windowing


The pedant in me is mildly perturbed that the new windowing system unveiled for iPadOS 26 is largely being discussed under the term “multitasking”. It’s windowing. One way to understand the difference is that the original Mac OS (a.k.a. System 1) had windowing — windowing that looked and worked a lot like this — but no multitasking. The very early Mac could run just one app a time, but the running app could open multiple windows. But, whatever. It’s all good.


One thing I find interesting is that while [split screen and Slide Over](https://support.apple.com/en-us/102364) have been eliminated in the new system ([praise be](https://www.macstories.net/stories/not-an-ipad-pro-review/)), Stage Manager is still a feature. Just plain windowing is as it should be: ad hoc. You make windows and move them around and resize them however you want. Stage Manager is fussier — it’s a more complex system for users who wish to organize their windows into something akin to projects or related tasks.


So, effectively, Apple, three years ago, jumped straight to a more complex, more fiddly option — Stage Manager — and only now has added the simpler, more obvious, not fiddly at all option (windowing). It’s been a weird journey, but I think iPadOS has finally arrived at a place where showing more than one app or document at a time on-screen is what it should have been all along: easy and obvious.


## Liquid Glass


Alan Dye, introducing Liquid Glass, around the 8m:20s mark in the keynote:


> Software is the heart and soul of our products. It brings them to
> life, shapes their personality, and defines their purpose. At
> Apple, we’ve always believed it’s the deep integration of hardware
> and software that makes interacting with technology intuitive,
> beautiful, and a joy to use. iOS 7 introduced a simplified design
> built on distinct layers, smooth animations, and new colors. It
> redefined our design language for years to come. Now, with the
> powerful advances in our hardware, silicon, and graphics
> technologies, we have the opportunity to lay the foundation for
> the next chapter of our software. Today we’re excited to announce
> our broadest design update ever. Our goal is a beautiful new
> design that brings joy and delight to every user experience, one
> that’s more personal, and puts greater focus on your content, all
> while still feeling instantly familiar.
> And for the first time, we’re introducing a universal design
> across our platforms. This unified design language creates a more
> harmonious experience as you move between products, while
> maintaining the qualities that make each unique. Inspired by the
> physicality and richness of VisionOS, we challenged ourselves to
> make something purely digital feel natural and alive. From how it
> looks to how it feels as it dynamically responds to touch. To
> achieve this, we began by rethinking the fundamental elements that
> make up our software, and it starts with an entirely new
> expressive material we call Liquid Glass. With the optical
> qualities of glass and a fluidity that only Apple can achieve, it
> transforms depending on your content or even your context, and
> brings more clarity to navigation and controls. It beautifully
> refracts light and dynamically reacts to your movement with
> specular highlights. This material brings a new level of vitality
> to every aspect of your experience. From the smallest elements you
> interact with to larger ones, it responds in real time to your
> content and your input. Creating a more lively experience that we
> think you’ll find truly delightful.


Compare and contrast to [Steve Jobs introducing Aqua at Macworld San Francisco in January 2000](https://youtu.be/dHrVGk0WwYM?t=381):


> So this is the architecture, except there’s one more thing. The
> one more thing is, we have been secretly for the last 18 months
> designing a completely new user interface. And that new user
> interface builds on Apple’s legacy and carries it into the next
> century. And we call that new user interface Aqua, because it’s
> liquid. One of the design goals was when you saw it, you wanted to
> lick it. [...]
> When you design a new user interface, you have to start off
> humbly. You have to start off saying, what are the simplest
> elements in it? What does a button look like? And you spend months
> working on a button. That’s a button in Aqua. This is what radio
> buttons look like. Simple things. This is what checkboxes look
> like. This is what popup lists look like. Again, you’re starting
> to get the feel of this, a little different. This is what sliders
> can look like. Now, let me show you windows. This is what the top
> of windows look like. These three buttons look like a traffic
> signal, don’t they? Red means close the window. Yellow means
> minimize the window. And green means maximize the window. Pretty
> simple. And tremendous fit and finish in this operating system.
> When you roll over these things, you get those. You see them? And
> when you are no longer the key window, they go transparent. So a
> lot of fit and finish in this.
> In addition to the fit and finish, we paid a lot of attention to
> dynamics. Not only how do things look, but how do they move, how
> do they behave. And our goal in this user interface was twofold.
> One, we wanted to give a much more powerful user interface to our
> pro customers. But two, at the very same time, we wanted to make
> this the dream user interface for somebody who’s never even
> touched a computer before. And that’s really hard to do. It’s like
> when we do films at Pixar. It’s really easy, it’s a lot easier, to
> make a film that appeals to five-year-olds and under. But it’s
> very difficult to make one film that five-year-olds love and that
> their parents also love. And that was the goal of this user
> interface. To make it span the range so that people turning on
> their iMac for the first time were enchanted with it, and it was
> super easy to use, and yet, our pro customers also felt, *My God,
> this takes me to places I thought I could never get to*. And
> that’s what we tried to do.


Re-watching Jobs’s introduction of Aqua for the umpteenth time, I still find it enthralling. I found Alan Dye’s introduction of Liquid Glass to be soporific, if not downright horseshitty.


But the work itself, Liquid Glass as it launched last week, is very reminiscent of Aqua a quarter century (!) ago. It’s exciting, it’s fresh, it fundamentally looks and feels very cool in general — and but in practice quite a few aspects of it feel a bit over-the-top and/or half-baked. Just like with Aqua, it will surely get dialed in. Legibility problems will be addressed.


Liquid Glass has been in the works for a long time, but what we see today has come together very quickly. For those using internal builds inside Apple, what Apple unveiled last week is effectively the third version of Liquid Glass. Just a few weeks prior to WWDC, a few sources told me that internal builds were such a complete mess that they wondered if it would come together in time for WWDC developer betas. But come together it has. I expect a *lot* of visual changes over the course of the summer, and significant evolutionary tweaks in the next few years. Across Apple’s own apps, there are a lot of places where things haven’t yet been glassed up at all. That’s how these things work.


As for *why*, it should be enough to justify Liquid Glass simply for the sake of looking cool. I opened this piece with a quote from a great fictional philosopher. I’ll close it with a quote from a great real one:


“*The test of a work of art is, in the end, our affection for it, not our ability to explain why it is good.*” 

—Stanley Kubrick



| **Previous:** | [The Talk Show Live From WWDC 2025](https://daringfireball.net/2025/06/the_talk_show_live_from_wwdc_2025) |
| **Next:** | [More on Apple’s Trust-Eroding ‘F1 The Movie’ Wallet Ad](https://daringfireball.net/2025/06/more_on_apples_trust-eroding_f1_the_movie_wallet_ad) |


PreviousNext