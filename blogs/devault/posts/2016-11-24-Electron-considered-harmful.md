---
title: "Electron considered harmful"
date: 2016-11-24
url: https://drewdevault.com/2016/11/24/Electron-considered-harmful.html
slug: Electron-considered-harmful
word_count: 871
---

Yeah, I know that “considered harmful” essays are allegedly  [considered
harmful](http://meyerweb.com/eric/comment/chech.html) . If it surprises you that
I’m writing one, though, you must be a new reader. Welcome! Let’s get started.
If you’re unfamiliar with Electron, it’s some hot new tech that lets you make
desktop applications with HTML+CSS+JavaScript. It’s basically a chromeless web
browser with a Node.js backend and a Chromium-based frontend. What follows is
the rant of a pissed off Unix hacker, you’ve been warned.

As software engineers we have a responsibility to pick the  *right*  tools for the
job. In fact, that’s the  *most important*  choice we have to make when we start a
project. When you choose Electron you get:

* An entire copy of Chromium you’ll be shipping with your app
* An interface that looks and feels nothing like the rest of the user’s OS
* One of the slowest, least memory efficient, and most inelegant GUI application
platforms out there (remember, we  *tolerate*  frontend web development because
we have no choice, not because it is by any means  *good* )

Let’s go over some case studies.

**[lossless-cut](https://github.com/mifi/lossless-cut)**  is an Electron app that
gives you a graphical UI for  *two ffmpeg flags* . Seriously, the flags in
question are -ss and -t. No really, that’s  *[literally all it
does](https://github.com/mifi/lossless-cut/blob/master/src/ffmpeg.js#L46)* . It
doesn’t even use ffmpeg to decode the video preview in the app, it’s limited to
the codecs chromium supports. It also ships its own ffmpeg, so it has the
industry standard video decoding tool  *right there*  and doesn’t use it to render
video. For the price of 200 extra MiB of disk space and an entire Chromium process
in RAM and on your CPU, you get a less capable GUI that saves you from having to
type the -ss and -t flags yourself.

**[1Clipboard](http://1clipboard.io/)**  is a clipboard manager. In Electron. A
 *clipboard manager* . In order to show you  *a list of things you’ve copied* , it
uses  *an entire bundled copy of Chromium* . Also note that despite the promises
of Electron making cross platform development easy, it doesn’t support Linux.

**[Collectie](https://getcollectie.com/)**  is a… fancy bookmark manager, I
guess? Another one that fails to get the cross platform value add from Electron,
this only supports OS X (or is it macOS). For only $10 bucks you get to organize
your shit into folders. Or you could just open the Finder for free and get a
native UX to boot.

This is a  [terminal](https://hyper.is/)  written with Electron. On the landing
page they say “# A terminal emulator 100% based on JavaScript, HTML, and CSS”
like they’re proud of it. They’ve taken one of the most lightweight and
essential tools on your computer and bloated it by orders of magnitude. Why the
fuck would you want to render Google in your god damn terminal emulator? Bonus:
also not cross platform.

This is not to mention the dozens of companies that have taken their websites
and crammed them into a shitty electron app and called it their desktop app.
Come on guys!

By the way, if you’re the guy who’s going to leave a comment about how this blog
post introduced you to a bunch of interesting apps you’re going to install now,
I hate you.

## Electron enables lazy developers to write garbage

Let me be clear about this: JavaScript sucks. It’s not the worst, but it’s also
not by any means good. ES6 is a really great step forward and I’m thrilled about
how much easier it’s going to be to write JavaScript, but it’s still JavaScript
underneath the syntactic sugar. We use it because we have no choice (people who
know more than just JavaScript know this). The object model is whack and the
loose typing is whack and the DOM is super whack.

When Node.js happened, a bunch of developers who never bothered to learn more
than JavaScript for their frontend work suddenly could write their crappy code
on the backend, too. Now this is happening to desktop applications. The reason
people choose Electron is because they are  *too lazy*  to learn the right tools
for the job. This is the  *worst*  quality a developer can have. You’re an
engineer, for the love of God! Fucking act like one! Do they build square
airplanes so they don’t have to learn about aerodynamics, then just throw on an
extra ten engines to make up for it? NO!

For the love of God, learn something else. Learn how to use GTK or Qt. Maybe Xwt
is more up your alley. How about GNOME’s Vala thing?  *Learn another programming
language* . Learn Python or C/C++ or C#. Fun fact: it’ll make your JavaScript
better, and once you have it in your toolbox you can make more educated
decisions on the appropriate tool to use when you face your next problem. Hint:
it’s not Electron.

## Some Electron apps don’t suck

For some use-cases Electron is a reasonable choice.

* [Visual Studio Code](https://code.visualstudio.com/) , because it’s a full
blown IDE with a debugger and plugins and more. It’s already gonna be
bloated.
* [Soundnode](http://www.soundnodeapp.com/) , because it’s not like any other
music service’s app obeys your OS’s UI conventions

Uh, that’s it. That’s the entire list.
