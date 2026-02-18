---
title: "Status update, October 2020"
date: 2020-10-15
url: https://drewdevault.com/2020/10/15/Status-update-October-2020.html
slug: Status-update-October-2020
word_count: 362
---

I’m writing this month’s status update from a brand-new desktop workstation
(well, I re-used the GPU), my first new workstation in about 10 years. I hope
this new one lasts for another decade! I aimed for something smaller and
lightweight this time — it’s a Mini-ITX build. I’ve only been running this
for a few days, so let me tell you about the last few accomplishments which are
accountable to my venerable workstation’s final days of life.

First, there’s been a ton of important work completed for SourceHut’s API 2.0
plans. All of the main blockers for the first version of meta.sr.ht’s writable
GraphQL API are resolved, and after implementing a few more resolvers it should
be in a shippable state. This included riggings for database transactions,
simplification of the mini-“ORM” I built, and support for asyncronous work like
delivering webhooks. The latter called for a new library,  [dowork](https://sr.ht/~sircmpwn/dowork/) ,
which you’re free to reuse to bring asyncronous work processing to your Go
programs.

I also built a new general-purpose daemon for SourceHut called
 [chartsrv](https://sr.ht/~sircmpwn/chartsrv/) , which can be used to generate graphs from
 [Prometheus](https://prometheus.io/)  data. The following is a real-time graph of the load
average on the builds.sr.ht workers:

I’ve been getting more into  [Gemini](https://gemini.circumlunar.space/)  this month, and have completed
three (or four?) whole projects for it:

* [gmni](https://sr.ht/~sircmpwn/gmni/)  and gmnlm: a client implementation and line-mode browser
* [gmnisrv](https://sr.ht/~sircmpwn/gmnisrv/) : a server implementation
* [kineto](https://sr.ht/~sircmpwn/kineto/) : an HTTP->Gemini portal

The (arguably) fourth project is the completion of a Gemini version of this
blog, which is available at  `gemini://drewdevault.com` , or via the kineto portal
at  [portal.drewdevault.com](https://portal.drewdevault.com) . I’ll be posting
some content exclusively on Gemini (and I already have!), so get yourself a
client if you want to tune in.

I have also invested some effort into  [himitsu](https://git.sr.ht/~sircmpwn/himitsu) , a project I shelved
for so long that you probably don’t remember it. Worry not, I have rewritten the
README.md to give you a better introduction to it. Here’s a screenshot for your
viewing pleasure:

Bonus update: two new  [BARE](https://baremessages.org)  implementations have
appeared: OCaml and Java.

That’s all for now! I’ll see you for the next update soon. Thanks for your
support!
