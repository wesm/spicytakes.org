---
title: "When will we learn?"
date: 2022-05-12
url: https://drewdevault.com/2022/05/12/Supply-chain-when-will-we-learn.html
slug: Supply-chain-when-will-we-learn
word_count: 507
---

Congratulations to Rust for its first (but not its last) supply-chain attack
this week! They join a growing club of broken-by-design package managers which
publish packages uploaded by vendors directly, with no review step, and ship
those packages directly to users with no further scrutiny.

## Timeline of major incidents on npm/Crates/PyPI/etc

* 2022-05-10: Cargo:  [rustdecimal](https://blog.rust-lang.org/2022/05/10/malicious-crate-rustdecimal.html)  ships with malicious code
* 2022-05-09: npm:  [foreach](https://mastodon.social/@lrvick/108274062191145538)  is taken over via an expired email domain
* 2022-03-17: npm:  [node-ipc](https://www.bleepingcomputer.com/news/security/big-sabotage-famous-npm-package-deletes-files-to-protest-ukraine-war/)  ships malware targeting Russia and Belarus
* 2022-01-09: npm:  [colors and faker](https://www.bleepingcomputer.com/news/security/dev-corrupts-npm-libs-colors-and-faker-breaking-thousands-of-apps/)  are deliberately sabotaged
* 2021-11-19: PyPI:  [11 malicious packages](https://arstechnica.com/information-technology/2021/11/malware-downloaded-from-pypi-41000-times-was-surprisingly-stealthy/)  discovered
* 2021-11-04: npm:  [rc](https://github.com/advisories/GHSA-g2q5-5433-rhrf)  ships malicious code
* 2021-11-04: npm:  [coa](https://www.bleepingcomputer.com/news/security/popular-coa-npm-library-hijacked-to-steal-user-passwords/)  steals your passwords
* 2021-10-22: npm:  [ua-parser-js](https://github.com/advisories/GHSA-pjwm-rvh2-c87w)  ships malicious code
* 2021-10-11: PyPI:  [mitmproxy2](https://twitt.re/maximilianhils/status/1447525552370458625?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1447525552370458625%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.bleepingcomputer.com%2Fnews%2Fsecurity%2Fpypi-removes-mitmproxy2-over-code-execution-concerns%2F)  typo-squats mitmproxy with an added RCE
* 2021-07-30: PyPI:  [8 malicious packages](https://arstechnica.com/gadgets/2021/07/malicious-pypi-packages-caught-stealing-developer-data-and-injecting-code/)  discovered
* 2020-12-16: RubyGems:  [pretty_color](https://blog.sonatype.com/rubygems-laced-with-bitcoin-stealing-malware)  (and one other) steals bitcoin from victims
* 2020-09-11: npm:  [dozens of packages](https://github.com/advisories?query=https%3A%2F%2Fjs-metrics.com%2Fminjs.php)  steal your user’s credit card number
* 2020-09-03: npm:  [bb-builder](https://github.com/advisories/GHSA-vm6v-w6q2-mrrq)  steals your password
* 2020-04-16: RubyGems:  [760+ malicious packages](https://blog.reversinglabs.com/blog/mining-for-malicious-ruby-gems)  found stealing bitcoin
* 2018-11-28: npm:  [event-stream](https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident)  ships with a bitcoin theft kit
* 2018-10-21: PyPI:  [colourama](https://scribe.rip/medium.com/@bertusk/cryptocurrency-clipboard-hijacker-discovered-in-pypi-repository-b66b8a534a8)  sneaks bitcoin addresses into your clipboard
* 2018-10-13: PyPI:  [more typo-squatting malware](https://scribe.rip/medium.com/@bertusk/detecting-cyber-attacks-in-the-python-package-index-pypi-61ab2b585c67)  attempts various attacks
* 2018-07-12: npm:  [eslint-scope](https://github.com/eslint/eslint-scope/issues/39)  ships with malicious code
* 2018-07-08: AUR:  [acroread](https://lists.archlinux.org/pipermail/aur-general/2018-July/034151.html)  is compromised
* 2018-05-11: Snap:  [a 2048 clone](https://github.com/canonical-web-and-design/snapcraft.io/issues/651)  ships a cryptocurrency miner
* 2017-09-09: PyPI:  [typo-squatted packages](https://www.nbu.gov.sk/skcsirt-sa-20170909-pypi/)  published by researchers
* 2016-07-22: npm:  [left-pad](https://www.infoworld.com/article/3047177/how-one-yanked-javascript-package-wreaked-havoc.html)  incident

There are hundreds of additional examples. I had to leave many of them out.
 [Here’s a good source](https://github.com/advisories?query=type%3Areviewed+malicious+package+severity%3Acritical) 
if you want to find more.

## Timeline of similar incidents in official Linux distribution repositories

## Why is this happening?

The correct way to ship packages is with your distribution’s package manager.
These have a separate review step, completely side-stepping typo-squatting,
establishing a long-term relationship of trust between the vendor and the
distribution packagers, and providing a dispassionate third-party to act as an
intermediary between users and vendors. Furthermore, they offer stable
distributions which can be relied upon for an extended period of time, provide
cohesive whole-system integration testing, and unified patch distribution and
CVE notifications for your entire system.

For more details, see my previous post,  [Developers: Let distros do their
job](/2021/09/27/Let-distros-do-their-job.html) .

## Can these package managers do it better?

I generally feel that overlay package managers (a term I just made up for npm et
al) are redundant. However, you may feel otherwise, and wonder what they could
do better to avoid these problems.

It’s simple: they should organize themselves more like a system package manager.

1. Establish package maintainers independent of the vendors
2. Establish a review process for package updates

There’s many innovations that system package managers have been working on which
overlay package managers could stand to learn from as well, such as:

* Universal package signatures and verification
* Reproducible builds
* Mirrored package distribution

For my part, I’ll stick to the system package manager. But if you think that the
overlay package manager can do it better: prove it.
