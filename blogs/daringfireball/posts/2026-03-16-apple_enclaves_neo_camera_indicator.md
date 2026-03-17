---
title: "Apple Exclaves and the Secure Design of the MacBook Neo’s On-Screen Camera Indicator"
date: 2026-03-16
url: https://daringfireball.net/2026/03/apple_enclaves_neo_camera_indicator
slug: apple_enclaves_neo_camera_indicator
word_count: 623
---


Some camera-equipped Apple devices have dedicated camera indicator lights. E.g. recent MacBook Pros and MacBook Airs have them in the notch, next to the camera itself. The Studio Display has one in the bezel, next to its camera. Other devices — like iPhones and, now, the MacBook Neo — render a green indicator dot on the device’s display. One might presume that the dedicated indicator lights are significantly more secure than the rendered-on-display indicators. I myself made this presumption in the initial version of [my MacBook Neo review](https://daringfireball.net/2026/03/the_macbook_neo) last week. This presumption is, I believe, wrong.


Later last week Apple published, and [I linked to](https://daringfireball.net/linked/2026/03/12/macbook-neo-on-screen-camera-indicator), a [small update in their Platform Security Guide](https://support.apple.com/guide/security/mac-on-screen-camera-indicator-light-sec75a2d237d/1/web/1), which states:


> MacBook Neo combines system software and dedicated silicon
> elements within A18 Pro to provide additional security for the
> camera feed. The architecture is designed to prevent any untrusted
> software — even with root or kernel privileges in macOS — from
> engaging the camera without also visibly lighting the on-screen
> camera indicator light.


The reason it’s tempting to think that a dedicated camera indicator light is more secure than an on-display indicator is the notion that hardware is more secure than software. With hardware, a dedicated hardware indicator light can be connected to the camera hardware such that if the camera is accessed, the light must turn on, with no way for software running on the device, no matter its privileges, to change that. With an indicator light that is rendered on the display, it’s not foolish to worry that malicious software, with sufficient privileges, could draw over the pixels on the display where the camera indicator is rendered, disguising that the camera is in use.


If this were implemented simplistically, that concern would be completely valid. But Apple’s implementation of this is far from simplistic. [Friend of the site](https://daringfireball.net/search/Guilherme+Rambo) and renowned developer and low-level-OS spelunker [Guilherme Rambo](https://www.rambo.codes/) texted me a note, which, with his permission, I’ll quote:


> Tidbit: the software-based camera indicator light in the MacBook
> Neo runs in the secure exclave¹ part of the chip, so it is almost
> as secure as the hardware indicator light. What that means in
> practice is that even a kernel-level exploit would not be able to
> turn on the camera without the light appearing on screen. It runs
> in a privileged environment separate from the kernel and blits the
> light directly onto the screen hardware. All of that applies to
> the mic indicator as well, which is a bonus compared to the
> camera-only hardware indicator.
> ¹ Exclaves run on a completely isolated realtime operating system
> that communicates with the kernel and userspace using a very
> limited API surface. Not to be confused with Secure Enclave,
> that’s a different thing.


(That’s right, his text message had a footnote. Like I said, he’s a friend of the site. Also: [blitting](https://en.wiktionary.org/wiki/blit).)


*Exclave* was the word I needed. Once I read that, it came back to me, and I recalled [Random Augustine’s “On Apple Exclaves”](https://randomaugustine.medium.com/on-apple-exclaves-d683a2c37194), which I [linked to almost exactly one year ago](https://daringfireball.net/linked/2025/03/19/on-apple-exclaves) and described as “a splendidly nerdy but very approachable overview of the evolution of Apple’s XNU kernel over the last decade”. As Augustine documents, secure exclaves are something Apple had been building toward for a decade, but which only became enabled with the M4 and A18 generations of Apple Silicon.


If you’re curious, I encourage you to read (or re-read) [Augustine’s “On Apple Exclaves”](https://randomaugustine.medium.com/on-apple-exclaves-d683a2c37194), which should disabuse you of any concerns that these on-display camera indicators on the MacBook Neo and recent iPhone models are anything less than *very* secure designs.



| **Previous:** | [Modifier Key Order for Keyboard Shortcuts](https://daringfireball.net/2026/03/modifier_key_order_for_keyboard_shortcuts) |


PreviousNext