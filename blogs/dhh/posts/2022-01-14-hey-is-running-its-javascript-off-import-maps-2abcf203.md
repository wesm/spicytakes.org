---
title: "HEY is running its JavaScript off import maps"
date: 2022-01-14
url: https://world.hey.com/dhh/hey-is-running-its-javascript-off-import-maps-2abcf203
slug: hey-is-running-its-javascript-off-import-maps-2abcf203
word_count: 557
---

The advent of import maps, and
[the bundler-less JavaScript reality](https://world.hey.com/dhh/modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755)
it introduced, was undoubtedly my favorite advancement in web tech for 2021. Between
[Guy Bedford's excellent shim](https://github.com/guybedford/es-module-shims/)
and native support in Chrome 89, we've finally been granted an escape from a decade's worth of frustrating complexity with excess tooling.
Usually progress means more to learn, more to master. It's not often we get to celebrate the progress of true
[conceptual compression](https://www.youtube.com/watch?v=zKyv-IGvgGE&t=1037s)
, so when we do, the confetti is well deserved. Hurrah for import maps!
Thus I'm thrilled to announce that
[HEY](https://www.hey.com/)
has been running on import maps
*in production*
for the past two weeks, and the experience has been bliss. An entire class of problems flushed from the daily development experience. WOOSH.
This work had been months underway. First, I used HEY as the testbed to validate the aspiration for import maps to become
[the default path in Rails 7](https://world.hey.com/dhh/rails-7-will-have-three-great-answers-to-javascript-in-2021-8d68191b)
. This is the benefit of using new tech in anger: You discover all the gaps between exuberant theory and actual practice.
Second, after proving that import maps work well on the web, we turned our eye to reworking several aspects of the
[Turbo](https://github.com/hotwired/turbo-ios)
[Native](https://github.com/hotwired/turbo-android)
integration. Especially dealing with the timing difference of loading all JavaScript after DOMContentLoaded. That's how all module loading in the browser is done, so we had to adapt. Not a big deal, but with a large codebase like HEY, and the criticality at stake, it still took a fair bit of diligence.
HEY is a major app. In total, it's almost fifty thousand lines of code, even if JavaScript only constitutes about 10% of that. It's also got tens of thousands of paying customers, and pulls in millions of dollars in revenue. We cover seven platforms with native apps on iPhone, iPad, Android, Mac, Windows, Linux, and of course the web. If we can make HEY work well with import maps, you can make the vast majority of all apps work well with import maps.
That was always the test for me. I'm not interested in pursuing an approach that only works for some small subsection of modern apps. Certainly not as a default approach for Rails. This has to stand the test of production with a major app. And it's this test it's passed with flying colors. What a relief!
The early feedback from Rails 7 adopters has also been strikingly positive, which too is a relief! Going with import maps by default felt like it might be a huge gamble when I started the work in early 2021. We'd been working with the old Webpack integration for almost five years. The devil you know and all that.
But this is the reward of taking a leap. Having people realize that the slow boil of complexity they'd been steaming in wasn't inherent to doing great, modern web applications. And when they got to experience a different way, it proved a revelation.
I hear through the grapevine that this success with import maps we've shown via Rails is changing minds elsewhere in the industry. Could we see native support in Firefox soon? Maybe even Safari? I think we just might. But again, thanks to Guy's impeccable work, we don't have to wait. Import maps are ready today. HEY has proven that beyond any doubt.
Hallelujah!

![import mapped javascript loading in HEY.png](https://world.hey.com/dhh/2abcf203/representations/eyJfcmFpbHMiOnsiZGF0YSI6Njc1MTc5NzAxLCJwdXIiOiJibG9iX2lkIn19--992876cfad313e26caf98e2ae4fd7020928645e67da4da537ee82f6f585adb67/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/import%20mapped%20javascript%20loading%20in%20HEY.png)

