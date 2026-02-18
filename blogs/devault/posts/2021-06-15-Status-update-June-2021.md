---
title: "Status update, June 2021"
date: 2021-06-15
url: https://drewdevault.com/2021/06/15/Status-update-June-2021.html
slug: Status-update-June-2021
word_count: 362
---

Hiya! Got another status update for you. First, let me share this picture that
my dad and I took on our recent astronomy trip (click for full res):

Bonus Venus:

So, what’s new? With SourceHut, there are a few neat goings-on. For one, thanks
to Michael Forney putting the finishing touches on the patchset, the
long-awaited NetBSD image is now available for builds.sr.ht. Also, the initial
lists.sr.ht GraphQL API design is in place, and Simon Ser is working on a new
and improved implementation of email discussion parsing for us to use. I’ve also
redesigned the registration & onboarding flow based on a maintainer/contributor
distinction, which should help people understand how sourcehut works a bit
better. Also, as promised, the writable GraphQL API for builds.sr.ht is now
available.

I had been working on a new feature for the secret programming language, but in
the course of implementing it, it became clear to me that we need to take a step
back and do some deep refactoring in the compiler. This will probably occupy us
for a couple of months. Even so, some improvements in the standard library have
been made and shall continue to be made. You may have seen a few weeks ago that
I  [wrote a finger server](/2021/05/24/io_uring-finger-server.html)  in the new language, and there’s a bunch of code
for you to read there if you’re interested in learning more.

I also spent some time this month on Simon’s  [gamja](https://git.sr.ht/~emersion/gamja)  and  [soju](https://git.sr.ht/~emersion/soju)  projects.
Libera.chat is running an experimental instance of gamja  [for their webchat](https://web.libera.chat/gamja) ,
and I’ve helped Simon incorporate some of their feedback and apply a layer of
polish to the client. I’m also working on generalizing soju a bit so that we can
eventually utilize it to offer a hosted IRC bouncer for sr.ht users.

That’s all I have to share for now. My foci have been on sourcehut and the
secret language, and will continue to be those. I plan on advancing the work on
the GraphQL APIs for sr.ht and ideally shipping an initial version of the
lists.sr.ht API in a few weeks. I’ll share more news about the new language when
it’s ready. Until next time!
