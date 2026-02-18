---
title: "pkg.go.dev is more concerned with Google's interests than good engineering"
date: 2020-08-01
url: https://drewdevault.com/2020/08/01/pkg-go-dev-sucks.html
slug: pkg-go-dev-sucks
word_count: 654
---

pkg.go.dev sucks. It’s certainly  *prettier*  than godoc.org, but under the
covers, it’s a failure of engineering characteristic of the Google approach.

Go is a  *pretty good*  programming language. I have long held that this is not
attributable to Google’s stewardship, but rather to a small number of language
designers and a clear line of influences which is drawn entirely from outside of
Google — mostly from Bell Labs. pkg.go.dev provides renewed support for my
argument: it has all the hallmarks of Google crapware and none of the
deliberate, good engineering work that went into Go’s design.

It was apparent from the start that this is what it would be. pkg.go.dev was
launched as a closed-source product,
 [justified](https://blog.golang.org/pkg.go.dev-2020)  by pointing out that
godoc.org is too complex to run on an intranet, and pkg.go.dev has the same
problem. There are many problems to take apart in this explanation: the
assumption that the only reason an open source platform is desirable is for
running it on your intranet; the unstated assumption that such complexity
is necessary or agreeable in the first place; and the
 [systemic](https://github.com/golang/go/issues/25443)   [erosion](https://github.com/golang/go/issues/30029) 
of the existing (and simple!) tools which  *could*  have been used for this
purpose prior to this change. The attitude towards open source was only changed
following pkg.go.dev’s harsh reception by the community.

But this attitude  *did*  change, and it is open-source now 1   2 , so let’s give
them credit for that. The good intentions are spoilt by the fact that pkg.go.dev
fetches the list of modules from  [proxy.golang.org](https://proxy.golang.org/) :
a closed-source proxy through which all of your go module fetches are being
routed and tracked (oh, you didn’t know? They never told you, after all).
Anyway, enough of the gross disregard for the values of open source and user
privacy; I  *do*  have some technical problems to talk about.

One concern comes from a blatant failure to comprehend the fundamentally
decentralized nature of git hosting. Thankfully, git.sr.ht is supported now 4 
— but only  *the*  git.sr.ht, i.e. the hosted instance, not the software.
pkg.go.dev hard-codes a list of centralized git hosting services, and completely
disregards the idea of git hosting as  *software*  rather than as a  *platform* .
Any GitLab instance other than gitlab.com (such as
 [gitlab.freedesktop.org](https://gitlab.freedesktop.org)  or
 [salsa.debian.org](https://salsa.debian.org/public) ); any
 [Gogs](https://gogs.io/)  or  [Gitea](https://gitea.io/en-us/)  like
 [Codeberg](https://codeberg.org) ; cgit instances like
 [git.kernel.org](https://git.kernel.org/) ; none of these are going to work
unless every host is added and the list is kept up-to-date manually. Your
intranet instance of cgit? Not a chance.

They were also given an opportunity here to fix a long-standing problem with Go
package discovery, namely that it requires every downstream git repository host
has to (1) provide a web interface and (2) include  *Go-specific*  meta tags in
the HTML. The hubris to impose your  *programming language* ’s needs onto a
language-agnostic version control system! I asked: they have no interest in the
better-engineered — but more worksome — approach of pursing a
language agnostic design.

The worldview of the developers is whack, the new site introduces dozens of
regressions, and all it really improves upon is the visual style — which
could trivially have been done to godoc.org. The goal is shipping a shiny new
product — not engineering a good solution. This is typical of Google’s
engineering ethos in general. pkg.go.dev sucks, and is added the large (and
growing) body of evidence that Google is bad for Go.

1. Setting aside the fact that the production pkg.go.dev site is amended with closed-source patches. ↩︎
2. The GitHub comment explaining the change of heart included a link to a Google Groups discussion which requires you to log in with a Google account in order to *read*.3 If you go the long way around and do some guesswork searching the archives yourself, you [can find it](https://groups.google.com/d/msg/golang-dev/mfiPCtJ1BGU/ibeimu3WEgAJ) without logging in. ↩︎
3. Commenting on Go patches also requires a Google account, by the way. ↩︎
4. But not hg.sr.ht! ↩︎
