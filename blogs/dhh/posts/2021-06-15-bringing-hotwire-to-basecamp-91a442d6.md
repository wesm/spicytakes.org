---
title: "Bringing Hotwire to Basecamp"
date: 2021-06-15
url: https://world.hey.com/dhh/bringing-hotwire-to-basecamp-91a442d6
slug: bringing-hotwire-to-basecamp-91a442d6
word_count: 668
---

[Hotwire](https://hotwire.dev)
is now powering Basecamp 3 on the alpha version we're running internally, and I thought it'd be helpful to document the upgrade process. Although upgrading is perhaps a big word. It's not like we rewrote all the JavaScript we have to make this happen. Coexisting is probably a better term. While existing JavaScript code stays as it is, we're now set for all our future development to use
[Turbo Frames](https://turbo.hotwire.dev/handbook/frames)
,
[Turbo Streams](https://turbo.hotwire.dev/handbook/streams)
, and
[Stimulus 2.0](https://stimulus.hotwire.dev)
. Yay!
Basecamp 3 was originally built with Rails UJS, Turbolinks, and Stimulus. In our new setup, Rails UJS is still there to handle data-remote/data-method forms and links for the legacy code, but it leaves alone any link or form tagged with data-turbo=true. Making this so required an
[upgrade to the UJS event handler selectors](https://github.com/rails/rails/pull/42476)
, which will be part of the next Rails release. And if you are still using rails/jquery-ujs (like Basecamp!), there's a new version 1.2.3 with the updated selectors as well.
It also required that all these new forms and method links we want flowing through Turbo instead of Rails UJS be tagged with that data-turbo=true attribute. Something you don't need to do if you're starting with Turbo from the beginning, like we did with HEY, but it's a small price to pay for coexistence.
The upgrade to Stimulus 2.0 (from 1.1) took a little more effort, but solely because we wanted to upgrade early to the new target format of data-[identifier]-target="[name]" instead of data-target="[identifier].[name]" (to get rid of the deprecation warnings). Although it was easy enough, I still managed to wrongly turn a few of these conversions into duplicate data-[identifier]-target attributes. So pay attention to that.
The meat of the coexistence work was in replacing Turbolinks with Turbo.
[Turbo Drive](https://turbo.hotwire.dev/handbook/drive)
is a direct continuation of Turbolinks, but it still required a fair bit of work to update all the namespaced events, and ensure that the Ajax requests coming from Rails UJS would play nice with 302 redirects. That was something the old turbolinks-rails gem included in the box, but turbo-rails does not (since it's not needed for greenfield work). There was enough steps in that process to warrant
[documenting them in the turbo-rails repository](https://github.com/hotwired/turbo-rails/blob/main/UPGRADING.md)
.
As part of this work, I caught up with both the Turbo and Stimulus repositories. I released a couple of
[new](https://github.com/hotwired/turbo/releases/tag/v7.0.0-beta.6)
[versions](https://github.com/hotwired/turbo/releases/tag/v7.0.0-beta.7)
of Turbo/Turbo Rails, which both fixed a number of bugs, but also gave us some great new powers, like
[before/after actions](https://github.com/hotwired/turbo/pull/121)
,
[built-in method links](https://github.com/hotwired/turbo/pull/277)
, and
[deduping of existing elements on the append/prepend actions](https://github.com/hotwired/turbo/pull/240)
. We're up to beta 7 now, and will keep going on the beta process for a bit longer while clearing out the backlog of pull requests and issues, but then it'll soon be time for a proper 7.0 final release as well.
Stimulus is also due for a 2.1 release in the near future, which will include a helpful
[debug mode](https://github.com/hotwired/stimulus/pull/354)
,
[previous value passing on the ValueChanged callbacks](https://github.com/hotwired/stimulus/pull/407)
,
[default values](https://github.com/hotwired/stimulus/pull/350)
, and a few other overdue enhancements.
This kind of upgrade work is something it's so easy to put off for existing applications. What you have already works, right? But if you keep doing that forever, you eventually end up with a codebase that's so far from the state of the art that it won't be any fun to work in it.
It's not that you have to rewrite everything from scratch all the time, but taking the effort to ensure that new code can be written to the best of your abilities is key to enjoying the work. And as you extend existing features, follow the principle of leaving the campsite better than you found it. For Basecamp, that means rewriting any of that old jquery code when we're doing substantial work around features using it.
[As the baboon said](https://www.youtube.com/watch?v=R2_Mn-qRKjA)
: "It gets easier. Every day it gets a little easier. But you got to do it every day. That's the hard part. But it does get easier."

![bojack-horseman-baboon.png](https://world.hey.com/dhh/91a442d6/representations/eyJfcmFpbHMiOnsiZGF0YSI6NDMxNjU0MDE5LCJwdXIiOiJibG9iX2lkIn19--f9b1b7d158da961999744418434ae52989b49db8b946e6e314695efd23aeabf1/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/bojack-horseman-baboon.png)

