---
title: "Framing accessibility in broader terms"
date: 2022-02-13
url: https://drewdevault.com/2022/02/13/Framing-accessibility-in-broader-terms.html
slug: Framing-accessibility-in-broader-terms
word_count: 1098
---

Upon hearing the term “accessibility”, many developers call to mind the HTML
 ARIA  attributes and
little else. Those who have done some real accessibility work may think of the
 WCAG  guidelines. Some
FOSS developers 1  may think of  AT-SPI . The typical user of these accessibility
features is, in the minds of many naive developers, a blind person. Perhaps for
those who have worked with WCAG, a slightly more sophisticated understanding of
the audience for accessibility tools may include users with a greater variety of
vision-related problems, motor impairments, or similar needs.

Many developers 2  frame accessibility in these terms, as a list of boxes to
tick off, or specific industry tools which, when used, magically create an
accessible product. This is not the case. In truth, a much broader understanding
of accessibility is required to create genuinely accessible software, and
because that understanding often raises uncomfortable questions about our basic
design assumptions, the industry’s relationship with accessibility borders on
willful ignorance.

The typical developer’s relationship with accessibility, if they have one at
all, is mainly concerned with making web pages work with screen readers. Even
considering this very narrow goal, most developers have an even narrower
understanding of the problem, and end up doing a piss-poor job of it. In
essence, the process of doing accessibility badly involves making a web page for
a sighted user, then using ARIA tags to hide cosmetic elements, adding alt tags,
and making other surface-level improvements for users of screen readers. If
they’re serious, they may reach for the WCAG guidelines and do things like
considering contrast, font choices, and animations as well, but all framed
within the context of adding accessibility band-aids onto a UI designed for
sighted use.

A key insight here is that concerns like font choice and contrast involve making
changes which are apparent to “typical” users as well, but we’ll expand on that
in a moment. Instead of designing for people like you and then patching it up
until it’s semi-functional for people who are not like you, a wise developer
places themselves into the shoes of the person they’re designing for and builds
something which speaks their design language. For visually impaired users, this
might mean laying out information in a more  *logical*  sense than in a  *spatial* 
sense.

Importantly, accessibility also means understanding that there are many other
kinds of users who have accessibility needs.

For instance, consider someone who cannot afford a computer as nice as the one
your developers are using. When your Electron  crapware  app eats up 8G of
RAM, it may be fine on your 32G developer workstation, but not so much for
someone who cannot afford anything other than a used $50 laptop from eBay.
Waking up the user’s phone every 15 minutes to check in with your servers isn’t
very nice for someone using a 5-year-old phone with a dying battery. Your huge
JavaScript bundle, unoptimized images, and always-on network requirements are
not accessible to users who are on low-bandwidth mobile connections or have a
data cap — you’re essentially charging poorer users a tax to use your
website.

Localization is another kind of accessibility, and it requires more effort than
running your strings through gettext. Users in different locales speak not only
different natural languages, but different design languages. Users of
right-to-left languages like Arabic don’t just reverse their strings but also
the entire layout of the page. Chinese and Japanese users are more familiar with
denser UIs than the typical Western user. And subtitles and transcripts are
important for Deaf users, but also useful for users who are consuming your
content in a second language.

Intuitiveness is another important detail. Not everyone understands what your
icons mean, for a start. They may not have the motor skill to hold their mouse
over the button and read the tool-tip, either, and might not know that they can
do that in the first place! Reliance on unfamiliar design language in general is
a kind of inaccessible design. Remember the “save” icon? 💾 Flashing banner ads
are also inaccessible for users with ADHD, and if we’re being honest, for
everyone else, too. Software which is not responsive on many kinds of devices
(touch, mouse and keyboard, different screen sizes, aspect ratios, orientations)
is not accessible. Software which requires the latest and greatest technologies
to use (such as a modern web browser) is also not accessible.

Adequate answers to these problems are often expensive and uncomfortable, so no
one wants to think about them. Social-media-esque designs which are deliberately
addictive are not accessible, and also not moral. The mountain of gross
abstractions on which much software is built is cheap, but causes it to suck up
all the user’s resources (RAM, CPU, battery, etc) on 10-year-old
devices. 3  And ads are inaccessible  *by design* , but good luck
explaining that to your boss.

It is a fool’s errand to aim for perfect accessibility for all users, but we
need to understand that our design choices are excluding people from using our
tools. We need to design our software with accessibility in mind from the ground
up, and with a broad understanding of accessibility that acknowledges that
simple, intuitive software is the  *foundation*  of accessibility which works for
everyone, including you and me — and not retroactively adding half-assed
tools to fundamentally unusable software. I want UI designers to be thinking in
these terms, and less in terms of aesthetic properties, profitable designs, and
dark patterns. Design with empathy first.

As someone who works exclusively in free software, I have to acknowledge the
fact that free software is pretty pathetic when it comes to accessibility. In
our case, this does not generally come from the perverse incentives that cause
businesses to cut costs or even deliberately undermine accessibility for
profit, 4  but instead comes from laziness (or, more charitably, lack of free
time and enthusiasm), and generally from free software’s struggles to build
software for people who are not like its authors. I think that we can change
this. We do not have the profit motive, and we can choose to take pride in
making better software for everyone. Let’s do better.

1. Vanishingly few. ↩︎
2. Including me, once upon a time. ↩︎
3. Not to mention that the model of wasteful consumerism required to
keep up with modern software is destroying the planet. ↩︎
4. Though I am saddened to admit that many free software developers, after
years of exposure to these dark patterns, will often unwittingly re-implement
them in free software themselves without understanding their sinister nature. ↩︎
