---
title: "Status update, December 2021"
date: 2021-12-15
url: https://drewdevault.com/2021/12/15/Status-update-December-2021.html
slug: Status-update-December-2021
word_count: 354
---

Greetings! It has been a cold and wet month here in Amsterdam, much like the
rest of them, as another period of FOSS progress rolls on by. I have been taking
it a little bit easier this month, and may continue to take some time off in the
coming weeks, so I can have a bit of a rest for the holidays. However, I do
have some progress to report, so let’s get to it.

In programming language progress, we’ve continued to see improvement in
cryptography, with more AES cipher modes and initial work on AES-NI support for
Intel processors, as well as support for HMAC and blake2b. Improved support for
linking with C libraries has also landed, which is the basis of a few
third-party libraries which are starting to appear, such as bindings to  [libui](https://github.com/andlabs/libui) .
I have also started working on bindings to SDL2, which I am using to make a
little tetromino game (audio warning):

I am developing this to flesh out the SDL wrapper and get a feel for game
development in the new language, but I also intend to take it on as a serious
project to make a game which is fun to play. I also started working on an IRC
protocol library for our language, but this does not link to C.

Also, the reflection support introduced a few months ago has been removed.

My other main focus has been SourceHut, where I have been working on
todo.sr.ht’s GraphQL API. This one ended up being a lot of work. I expect to
require another week or two to finish it.

visurf also enjoyed a handful of improvements this month, thanks to some
contributors, the most prolific of whom was Pranjal Kole. Thanks Pranjal!
Improvements landed this month include tab rearranging, next and previous page
navigation, and an improvement to all of the new-tab logic, along with many bug
fixes and smaller improvements. I also did some of the initial work on command
completions, but there is a lot left to do in this respect.

That’s all for today. Thanks for your continued support! Until next time.
