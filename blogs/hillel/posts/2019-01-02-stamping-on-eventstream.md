---
title: "STAMPing on event-stream"
date: 2019-01-02
url: https://www.hillelwayne.com/post/stamping-on-eventstream/
slug: stamping-on-eventstream
word_count: 8883
---

> The goal of a STAMP-based analysis is to determine why the events occurred… and to identify the changes that could prevent them and similar events in the future. 1


One of my big heroes is Nancy Leveson, who did a bunch of stuff like the [Therac-25 investigation](http://sunnyday.mit.edu/papers/therac.pdf) and [debunking N-version programming](http://sunnyday.mit.edu/papers.html#ft). She studies what makes software unsafe and what we can do about that. More recently she’s advocated the “STAMP model” for understanding systems. STAMP, she says, provides a much richer understanding of the problems and solutions than simple root-cause analysis.2 I really like the idea and wanted to try it out and have been looking for a good software accident to try applying STAMP to.


Back in November I got my wish. Some js engineers discovered that the npm package [event-stream](https://github.com/dominictarr/event-stream/issues/116) was stealing people’s bitcoin wallets. On investigation, they found the original maintainer had passed it over to an anonymous person because [“he said he wanted to maintain it”](https://github.com/dominictarr/event-stream/issues/116#issuecomment-440927400). Naturally the internet erupted in a big argument about who was *really* at fault: the maintainer for giving it to a rando, society for not paying open source maintainers, or npm for not preventing one extremely specific part of the attack.


I thought this would be a good exercise to try STAMP on, so I did. Then I got carried away and ended up writing way too much on it. You, uh, might want to grab a sandwich or something before reading.


…


You back? Good. Let’s do this.


**Disclaimer:** I’m not involved in the npm/js world and learned most of this stuff through research. I’m also not a security person. I’m presenting this as an example of what a STAMP analysis looks like. I do not have access to internal discussions or decisions by either Copay or npm Inc, which are the source of a lot of important analysis insights.3 In cases where I wasn’t certain whether a vulnerability was real or not, I erred on the side of including it: even if it had already been fixed, I want to show that following STAMP will discover it.


*Update: Any statement with a † next to it is in some way incorrect. Corrections are after the analysis.*


## Intro: the Attack


`event-stream` is a js library that provides an event stream utility for JavaScript libraries. Almost 4,000 packages used it or a dependent package.4 While very popular, it was abandoned by its creator, Dominic Tarr, who had lost interest and moved on to other things. His last significant contribution was in 2014. Past that, he just merged other people’s PRs.


In September 2018, Dominic Tarr was contacted by “right9ctrl” who offered to take over maintenance of the package. Once Tarr signed over the access rights, right9ctrl added a malicious dependency to `event-stream` that, when included as a dependency of the Copay wallet, would steal the user’s private keys. This was only discovered when it made a deprecated crypto call and a different person noticed.


The accident is an example of a **dependency attack**, where the security of a system is compromised through its chain of dependencies. Other dependency attacks were the [leftpad incident](https://github.com/stevemao/left-pad/issues/4) and the [AndroidAudioRecorder incident](https://blog.autsoft.hu/a-confusing-dependency/) (notable for the core repo not being compromised).


You can read more details about the `event-stream` debacle [here](https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident) and [here](https://schneid.io/blog/event-stream-vulnerability-explained/).


### Finding Fault


> The belief that there is a root cause, sometimes called root cause seduction [32], is powerful because it provides an illusion of control.


At first, people blamed Tarr: he gave access to the repo over to an unknown, anonymous person who asked nicely. If he was more diligent, this never would have happened. Clearly, the root cause is that maintainers are lazy.


People quickly lept to his defense. Open-source is a tiring, thankless job and everything is provided without warranty. He hadn’t touched the repo for two years, somebody else wanted to maintain it, he said sure. He did not make the repo expecting to have to maintain it for multiple people. Clearly it’s all Copay’s fault, who used a no-warranty package without auditing it.


But wait, the attack was hidden really well! The attacker put the actual malicious code in the minified js, not the regular js, so somebody looking at it wouldn’t have seen it. Clearly it’s all npm’s fault for not minifying everybody’s code themselves.3


Most people blamed one of these three things, but only one of them. One group has to be the root cause, and the others are irrelevant.


### STAMP


> The biggest problem with hindsight bias in accident reports is not that it is unfair (which it usually is), but that an opportunity to learn from the accident and prevent future occurrences is lost.


“Who did this” is the wrong question. “How did this happen” is the wrong question. A better question is “why was this possible in the first place?”


An accident isn’t something that just happens. Accidents aren’t isolated failures. Accidents aren’t human error.  Accidents aren’t simple. Accidents are *complicated*. Accidents are symptomatic of much deeper, more insidious problems across the entire system.


This is the core insight of Leveson. Instead of thinking about accidents as things with root causes, we think of them as failures of the entire system. The system had a safety **constraint**, something that was supposed to be prevented. Its **controls**, or means of maintaining the constraints, were in some way inadequate.5


The purpose of a postmortem should be to *prevent future accidents*. We don’t just stop the analysis once we find a scapegoat. Sure, we can say “Tarr transfered it over”, but why did that lead to an accident? Why did he want to abandon it? Why was he able to transfer it over? Why did nobody notice he transferred it? Why was a single dependency able to affect Copay? Why was a random internet dev so critical in the first place?


Leveson aggregated all of her safety approaches under the umbrella term STAMP.2 We’re going to analyse the attack via STAMP and see if we can get better findings than “Tarr don’t software good.”6


# The Analysis


## Overview


> The goal of STAMP is to assist in understanding why accidents occur and to use that understanding to create new and better ways to prevent losses.


Doing a STAMP Accident Analysis is a super comprehensive task which I’m going to simplify for this post. Here’s what we’ll do:

1. Identify the system constraints and how they are enforced.
2. Identify the “proximal chain” in painful detail.
3. Talk about which low-level controls failed and why.
4. Talk about why inadequate controls were used in the first place.
5. Keep repeating (3) and (4) at higher and higher levels.


The constant zooming-out is key here: it’s not enough to find out why things broke, but find out why “why things broke”. In theory you’re supposed to keep doing it: if someone skips a step because of managerial pressure, you ask why the manager was pressuring them in the first place. If the manager was worried about production quotas, find out how the quotas were decided. You just keep going and going and going.


For the sake of my sanity (and because I don’t have access to Copay’s secret diary) I’ll just stop at one zoom-out.


### Base Constraints


> Without understanding the purpose, goals, and decision criteria used to construct and operate systems, it is not possible to completely understand and most effectively prevent accidents.


We’ll start by identifying some constraints of the system:

1. *Package maintainers should be trustworthy.*
2. *Packages should not be made malicious.*
3. *Malicious packages should not be inadvertently used by users.*


This is all enforced by “best practice”: it’s your as the user’s responsibility to only include packages you think are safe. You only include packages from maintainers you think are safe, and so they will never make their package malicious. If they modify the package, you are supposed to audit it, or check the changes to make sure they’re compatible with your code. The npm ecosystem helps by providing a few bits of tooling: Your library dependencies can be locked, package updates follow a convention (SemVer), and `npm audit` can identify known security problems. As we’ll see, they’re all inadequate for enforcing safety.


If a malicious package *does* get included, there are several more contraints we’d expect:

1. *Malicious packages should be identified and removed quickly.*
2. *Malicious packages that are used should not reach production.*
3. *Malicious code should not be able to steal private information.*


It was several months between `event-stream` going bad and anybody noticing, by which point Copay had made several releases. It was about a week between somebody reporting the issue and npm removing the package.


### Proximal Chain


> While the event chain does not provide the most important causality information, the basic events … do need to be identified so that the physical process involved in the loss can be understood.


The proximal chain is the accident timeline in as exacting detail as possible. The purpose here is not to pin blame, but to understand all the system controls involved. That gives us the launching point to start our initial investigation.


We’ve already talked about the beginning: right9ctrl contacts Tarr about taking over `event-stream` , Tarr gives him update rights in npm and tries to transfer the Github project to his control. However, r9c already forked the repo, meaning Github prevented signover. Instead Tarr gave r9c admin permissions on his own repo.


r9c starts by adding a few minor bugfixes to `event-stream`. Then, on September 9, he adds a “patch”. [Here](https://github.com/dominictarr/event-stream/commit/e3163361fed01384c986b9b4c18feb1fc42b8285) he adds a dependency, `flatmap-stream`. Three days later, he makes a [new “major” version](https://github.com/dominictarr/event-stream/commit/2bd63d58fe24367372690c29c7249ed1c7145601) which inlines the dependency code to `event-stream` and removes the dependency. The malicious code is in `flatmap-stream`’s *minified* source code. The code is encrypted with the name of the using package as the key. For everything but Copay, it would do nothing, but would run malicious code if Copay (or a fork) is running in release mode. It would check if the user had 100+ Bitcoin in their wallet and, if so, upload the wallet private key to a remote server.


On [September 25th](https://github.com/bitpay/copay/commit/baab807a066eb7d5994a68fef5a554f3f1e35a87/), as part of trying to upgrade `cordova-plugin-fcm`, Copay accidentally updated all of their npm dependencies too. Based on the dependency chain, `event-stream` is patched but not pushed to the major version, meaning Copay now has the malicious code. Copay then released the new version on October 1st.


People first started noticing `event-stream` was throwing deprecation warnings around [October 28](https://github.com/remy/nodemon/issues/1442). It was using `crypto.createDecipher`, which is not something a stream utility should be doing. Eventually “FallingSnow” investigated and, on November 20, discovered the malicious code. They immediately raised an issue on the `event-stream` Github repository and someone else emailed npm support to get it removed. On the 26th npm Inc added it to `npm audit` and removed `flatmap-stream` from `npm`. The internets promptly lost their minds.


npm released an [official statement](https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident) but did not recommend any actions. Copay also released a [statement](https://blog.bitpay.com/copay-npm-security-update/), saying they would (1) implement a Content Request Policy and (2) only upgrade packages for new major versions. This, they believe, would be enough to fix the error.


# The first controls


> Analysis starts with the physical process, identifying the physical and operational controls and any potential physical failures, dysfunctional interactions and communication, or unhandled external disturbances that contributed to the events. The goal is to determine why the physical controls in place were ineffective in preventing the hazard.


## Transfer of Rights


npm and Github both do a lot to prevent non-maintainers from modifying packages. This is good. The controls, however, were simply not relevant here: Tarr made r9c an official maintainer. There are no controls in place to ensure that a new maintainer is trustworthy.


This is what most people focused on, despite being the most superficial bit. Problem: Tarr gave access rights to an internet rando. Solution: tell people to vet internet randos. This would presumably be enforced by demanding maintainers have better discipline.


This places additional responsibilities on the open source maintainer. One law we see time and time again is “you cannot fix things with discipline.” First of all, they simply don’t work: see all the data breaches at professional, “responsible” companies. Also, discipline approaches *do not scale.* This problem happened because a single contributor for a single package made an error. At the time of the attack, Copay had thousands of package dependencies. That means that thousands of maintainers cannot make any mistakes or else the system is in trouble. And even if they all have perfect discipline, this still doesn’t prevent dependency attacks. A malicious actor could seed a package and use it later, or steal someone else’s account.


### Breaking Changers


There is one thing npm could have done here: it could have alerted people that the maintainer had changed. Then people could decide for themselves if they wanted to trust the new maintainer or not, or if they should pin the dependency. I have no idea how much signal vs noise this would produce, so people might not pay attention to this. More on that later. Also, I have no idea how many people would have acted on it, as r9c made several good changes before the bad one.


There is also something Github could have done: made it easier for Tarr to transfer `event-stream` into r9c’s *namespace*. While this wouldn’t have affected the attack, it would mean that, on discovery, people wouldn’t have wasted time going after Tarr, who had already given up his rights to the project.


There’s really not much else to examine here. We’ll see many more system faults by looking at why this transfer was so *effective* instead of why the transfer happened at all. So let’s move on to the next phase of the attack.


## Getting to Copay


The “obvious problem” is this: `event-stream` turned malicious. Copay included it anyway. Either Copay should have audited the change to make sure it was safe, or Copay should have pinned their packages. As with the “Maintainers should be more careful” argument, it’s tempting because it places the blame squarely on one party. Problem: Copay did not audit all of their dependencies. Solution: tell people to audit all their packages. This would presumably be enforced by demanding developers have better discipline.


And just as before, this approach keeps us from having to dig into the details of why the controls, like audits and pinned packages, failed them.


### Why did Copay use `event-stream`?


> When there are multiple controllers (human and/or automated), control actions may be inadequately coordinated, including unexpected side effects of decisions or actions or conflicting control actions. Communication flaws play an important role here.


Copay didn’t really depend on `event-stream`. Copay depended on `npm-run-all`, which depended on `ps-tree`, which depended on `event-stream`, which hid the malicious code in `flatmap-stream`. Is the problem with `ps-tree` for not auditing `event-stream`, or with Copay for not auditing the entire chain of dependencies? Even if they checked every single line in `npm-run-all` *and* `ps-tree` *and* `event-stream`, they still wouldn’t have caught the error.


Leveson calls this **multiple controllers**, or **boundary error**: there are multiple different groups that *could* be responsible for auditing, but not a group that *is* responsible. Each one might independently assume that someone took care of it. Or it could lead to someone inadequately trained auditing and deciding it was safe, and everybody else believing them.


It’s tempting to make this hierarchical: if A depends on B depends on C, then A audits B and B audits C. This fails for two reasons. The first is that there isn’t actually a hierarchy here: A does not have any authority to *make* B audit C, so cannot guarantee that they will do so properly. Second, B can successfully identify C as compromised and the A *still* include it. This is because of how npm does updates.


### A note on npm versioning


> In complex systems, accidents often result from interactions among components that are all satisfying their individual requirements, that is, they have not failed.


All packages on npm follow **Semantic Versioning**, or SemVer. SemVer is format for versioning packages to make it easier to upgrade dependencies. Packages have major versions, minor versions, and patches, represented as `Major.Minor.Patch`. Major versions mean breaking changes, minor versions are significant nonbreaking changes, patches are as you’d expect. So if a package is on `3.4.2`, you *should* be able to upgrade to `3.4.3` or `3.5.2` without any changes to your own code, while all bets are off for `4.0.0`. This helps us keep dependencies manageable and upgrades less painful.


npm only allows publishing a given name/version combination *once*. If you want to tweak something after publishing, you have to bump the version. This prevents somebody from replacing a good version with a malicious one.


Depending on your needs, you can express all sorts of version requirements. You can pin a package to a specific version, such as `1.2.1` only. You can express a range of packages, like `1.0.0 - 2.7.1`. You can pin the major or minor versions while letting minor/patch version float. If you write `~1.2.3`, then you’re saying you can use `1.2.5` or `1.2.19` but not `1.3.0`.


Once you install a package, it’s added to your `package-lock`. From then on `npm install` will not upgrade it if a newer compatible version is out. If you run `npm update`, you will upgrade to the *latest compatible version* for all your packages. This includes transitive dependencies. If you have dependency `A -> B -> C` and `C` bumps a patch, you’d upgrade C even if B is unchanged. The exception to this is B is “shrinkwrapped”, which is explicitly discouraged for libraries.


### Why did Copay upgrade?


`ps-tree` had a floating dependency on `event-stream` for version `~3.3.0`. This means that they would not upgrade the package except for bugfixes. As mentioned before, this is normally good practice. The attacker exploited this by doing the following:

1. Add the exploit to patch `3.3.6`.
2. Publish `4.0.0` without the exploit.


Everybody who *transitively* depends on `ps-tree` would, on upgrading, get the malicious version. However, people directly depending on it would presumably update it directly to `4.0.0`. This means that the people most likely to miss it would be people assuming that `ps-tree` properly audited the package.


However, the `ps-tree` team might not have even realized there was a new version at all! The last package update before the incident was in *March*, several months before the attacker took over `event-stream`. If the maintainer didn’t specifically upgrade the dependencies on their local version of `ps-tree`, they wouldn’t have seen there was a new patch for `event-stream`. And remember that the actual attack was in a package under a different username, so `ps-tree` could argue that they expected flatmap to do due diligence.


The only comprehensive solution here is to audit *every* package that changes, no matter how deep it is. This is what [Copay now claims to be doing](https://blog.bitpay.com/copay-npm-security-update/). This is 1) extremely resource-intensive and unviable for the majority of projects, and 2) means that you could have security vulnerabilities that would have been fixed in patches.


## The attack itself


### Why didn’t Copay notice?


> Even in the best of industries, there is rampant attribution of accidents to operator error, to the neglect of errors by designers or managers.


The script only made HTTP requests in production. However, the package still threw deprecation warnings. Why didn’t they notice that?


Copay runs in **Electron**, a self-contained node environment. We’ll talk a bit more about Electron later, but the important thing here is that it distinguishes “client-facing” code from “main process” code. In particular, “client” code can be debugged fairly easily with Chrome Devtools, but to debug “main process” code you have to run Electron in a [special mode](https://electronjs.org/docs/tutorial/debugging-main-process) and use an external debugger. Module imports are done as part of the main process, so Copay would not see the warnings if they weren’t specifically looking for them.


You could argue that “running a main process debugger” should be part of the normal release process. But Electron seems to discourage that.


### Why could the package steal data?


Why was a single dependency, four layers deep, able to steal everybody’s bitcoin wallets?


The **Principle of Least Privilege** says every part of the system should have just enough privileges to perform its role *and nothing else*. A stream processing library, for example, should not be able to make HTTP requests or access files. This is a fundamental constraint of security: nothing should be able to do things it is not supposed to be doing.


In JavaScript, PoLP is entirely by convention. All functions have access to `XmlHttpRequest`, any script can dynamically load any module, anything can write to an existing object’s prototype. JavaScript can read files and do POST requests, so the malicious script can do that, too.


#### Content Security Policies


One of the fixes Copay is making is adding a Content Security Policy, which restricts http requests to a whitelist. This happens at the browser/Electron level so JS can’t subvert it. This would have prevented this particular attack but not dependency attacks in general. The malicious code has access to everything the primary code does, too. If, for example, Copay was using JavaScript to generate Bitcoin wallets, the attacker could maliciously reduce the key space to 20 billion keys.


## Why did it take a week for people to react?


FallingSnow first alerted everybody about the exploit on November 20. It was only November 26 that packages started to mass remove `event-stream`. That was when npm published a security advisory saying that `event-stream` was malicious and pulled it from the registry.


However, people informed npm support by Nov 22 at the latest, and likely by Nov 20. So npm took 4-6 days to actually publish the advisory. Some of this is probably due to Thanksgiving as most of npm is US-based. Nonetheless, it’s a pretty long delay for such a critical issue.


# Zooming Out


> Fully understanding the behavior at any level of the sociotechnical safety control structure requires understanding how and why the control at the next higher level allowed or contributed to the inadequate control at the current level.


We now have a *very* immediate set of control failures:

1. Dominic Tarr gave rights to another person
2. SemVer did not prevent r9c from including evil stuff
3. Floating pins do not prevent a malicious patch
4. It’s not clear whose responsibility it is to audit packages
5. Copay didn’t audit the packages
6. No PoLP in JavaScript
7. Copay didn’t debug the main process
8. CSP was off by default
9. npm responded slowly


Now it’s time to zoom out. We need to ask *why* Tarr was in a position to do so much damage, *why* nobody audits packages, why npm responded so slowly. We need to understand why we’re in the situation we’re in. Saying “pin your packages” is completely useless if we don’t know why people use floating dependencies in the first place!


As we go higher, control failures become less and less about specific operational processes and more and more about cultural, organizational, or economic forces. The problems stop being things like “Copay was using an unsafe language” and start becoming “Cross-OS development is difficult without using an unsafe language” or “Copay’s existing workforce was almost entirely Node developers.”


## Why don’t people audit?


> As safety efforts are successfully employed, the feeling grows that accidents cannot occur, leading to reduction in the safety efforts, an accident, and then increased controls for a while until the system drifts back to an unsafe state and complacency again increases…  This complacency factor is so common that any system safety effort must include ways to deal with it.


Auditing is a waste of time.


Most packages aren’t going to be malicious. Copay had 2700 dependencies. After the 200th time auditing an update and going “yup, checks out”, are you really going to be as diligent with the 201st? Remember, “diligent” here means knowing the code well enough to find security holes. This is all on top of maintaining *your* code, as in the code that’s your actual job.


In theory you could have heuristics, like “only audit packages who changed owners.” But heuristics, if known, are circumventable. r9c made several “good” commits both before and after the bad commit. How long would you be suspicious of r9c until you stopped paying attention?


Also, you probably won’t find the attack even if you *were* auditing it. It was pretty well hidden! Maybe a professional could find it, but not the average fullstack dev.


In order to make auditing *not* a waste of time, we’d need to reduce the number of packages we need to audit and make auditing actually likely to turn up bugs. The explanation for why “people don’t audit” is actually threefold:

1. There are too many dependencies to audit them all
2. Almost all of them are safe anyway
3. Of the ones that aren’t safe, it’s extremely hard to discover they’re evil


(1) has two parts to it: there is a very high number of *absolute* dependencies, and a high *percentage* of them are risky. (2) is a good thing, but makes it easy to get complacent. For now let’s focus on (3).


### Why was the attack so hard to find?


If you looked at the code for `event-stream`, you wouldn’t see anything malicious. If you instead looked at [`flatmap-stream`](https://github.com/hugeglass/flatmap-stream), you *still* wouldn’t find anything malicious. Instead, you would have to look at the *minified* version hosted on Github.† This is different from what you’d get if you minified it yourself. Minified code is difficult to reverse-engineer, but if you did it, it would [definitely look suspicious enough](https://github.com/dominictarr/event-stream/issues/116#issuecomment-441727488) to raise concerns of sketchiness.


While it’s in general hard to tell if code is malicious or not, it’s a *lot* easier to tell if code is suspicious or not. Presumably we could focus our audits on suspicious code, which will produce some false positives but that’s much better than the alternative. Then this problem reduces to “the sketchy code was in the minified version”, and it’s impossible to tell anything really about minified code.


Many people have said *this* is the core issue: that npm doesn’t verify your minified code matches the regular code. npm should either check your minification or minify the code for you. Then this attack couldn’t have happened!


There is a minor and a major problem with this approach. The minor is that there is no one minification tool, so you’d have to provide npm with the steps to minify, which kind of defeats the point. I don’t even know if all of the minification tools are deterministic.


The bigger problem is that npm doesn’t do any validation anyway.


#### npm/Github mismatch


npm lets you specify a corresponding Github page for the project. It does not, however, validate that they actually match. It’s perfectly fine to upload one version of the file to Github and another to npm. So instead of being a “you have to look at the minification of the dependency of a dependency” attack, it could have instead been a “you have to look at the minification of the dependency of a dependency, but in npm and not github” attack.†


This seems to be by design, as `npm_ignore` overrides `gitignore`. It seems that npm expects it to be common for the two versions to be different. This was [raised as an issue](https://hackernoon.com/secure-npm-ca2fe0e9aeff) before, but as far as I can tell there are no plans to change this, nor do I know what the relative tradeoffs are. However, it does mean that “force the minified and main versions to sync” would be insufficient at plugging this specific style of attack.7


Let’s ask a different question: why are people including minified files in the first place?


#### Why Minify?


> Accidents, particularly component interaction accidents, most often result from inconsistencies between the models of the process used by the controllers (both human and automated) and the actual process state.


People unfamiliar with JS might ask why there was a minified file in the first place. JavaScript is primarily used for web clients, which means the client needs to be download it from a server first. Minification reduces the size of the file, for example by removing indentation and replacing `var foobarbaz` with `var a`. Minified `react` is about 500 kb smaller than unminified version, meaning faster downloads and script starts. Most people use the full version in develop and compile the minified versions for use in production.


Recently we’ve seen a lot of interest in *Electron*, a framework for running JavaScripts like “native” “apps”. Each Electron app must come with a copy of Chromium and Node.js, meaning Electron apps are dozens or even hundreds of megabytes large. All the js scripts are downloaded at once as part of the app. Copay was an Electron app, meaning anybody using it would have *already downloaded all of the necessary JavaScript.* There was no benefit to using the minified package over the regular one. They just used it because that was what what everybody did, and everybody did it because it *used to be* a good idea.  Now, though, following best practice opened a security hole. 8


Leveson calls this **model drift**: The existing rules were ideal for the system in the past, but the system itself has changed. Copay was doing something that made sense *in the original context of JavaScript*. In the Electron context, though, blindly using minified dependencies is a performance hit and security vulnerability.


Client apps are still vulnerable to dependency attacks, and minification is still a way to obfusciate malicious dependencies, but there’s absolutely no reason it should be so effective against a standalone app.


## Why was Tarr’s library so critical?


> If the analysis determines that the person was truly incompetent (not usually the case), then the focus shifts to ask why an incompetent person was hired to do this job and why they were retained in their position.


One thing we didn’t talk about yet is *why* Tarr had such an influential package. He had no intention of having so much responsibility when he originally published it in [2011](https://github.com/dominictarr/event-stream/commit/970993ccc594c606d439a9fa22715d311e1b9fa2). So why did `Copay` rely on it?


Node.js came out in 2009. It’s had exponential growth, though, [starting 2014](https://medium.com/@npmjs/npm-weekly-116-12-billion-packages-downloaded-every-month-npm-at-nodeconf-eu-plus-a-very-c6431d2ff8fa). One npm philosophy is “don’t reinvent the wheel.” Since an event stream package already existed, don’t write your own, use it instead. So people added `event-stream` as a dependency, and continued doing so for seven years. Things are further compounded by the transitive dependencies. If A depends on B and B depends on C, then A also depends on C. The number of users of your package can grow exponentially.


Tarr didn’t do any advertising. He is not a famous person. He just happened to be using Node a little before everybody else, needed to write a utility, and decided to publically release it. Suddenly it was critical to thousands of projects.


We’ve seen something similar happen with `left-pad`. Leftpad wasn’t part of JS at the time, somebody made a package in 2014, and everybody used it. Even now, after `padStart` was added to the JS core library, over 400 packages still *directly* depend on `left-pad` and it is downloaded more than 2 million times a week.9


This all seems an intentional part of the system. One consequence of this, as we’ve seen, is it means people who have neither the resources, abilities, or inclination are suddenly responsible for the security of thousands of projects they’ve never heard of. Any dependency of this form is extremely suspect to hijacking and must be treated with suspicion.


This wouldn’t be as big a problem as it is if only a few packages were of this style: maintained by a single person who never wanted or expected a ton of responsiblity. Unfortunately, almost all small packages are like this. And there are a *lot* of small packages.


## Why so many dependencies?


> Each local decision may be “correct” in the limited context in which it was made but lead to an accident when the independent decisions and organizational behaviors interact in dysfunctional ways.  Safety is a system property, not a component property, and must be controlled at the system level, not the component level.


Copay has approximately 2700 dependencies. Most of these are single purpose dependencies, or included because another package needed something in it. For example, `ps-tree` used `event-stream` because it provided a tidy interface between `pipelines` and `map-stream`. In total, `event-stream` had 7 dependencies… all of which were made by Tarr. The largest of these `event-stream` dependencies had more direct users than `event-stream` itself, while the smallest had only 30 other users. The npm community encourages making packages as small and isolated as possible, so that one functionality should be split into several unit packages and an integration package. This is good for quality, reusability, and file sizes: if you need only a small part of the package, you could instead include the corresponding micropackage and clients need to download less.


This is a good example of what Leveson considers **local optimization**: library authors have pressing business needs- increase rate of feature development, reduce the bugginess of their packages, and reduce the size of client scripts. Trying to locally meet these needs leads to a greater client attack surface and so less system safety.


It is very difficult to get more information on the dependency tree. For example, there’s no easy way to get the authors of all of the dependencies. This makes even basic data analysis of dependencies extremely tedious. Very roughly 1700 people managed Copay’s various dependencies. Presumably any of these would be equally vulnerable to a dependency attack, whether by transfering permissions, having their keys stolen, etc.


One way to reduce the attack surface would be to reduce the number of dependencies. This can either happen at the library side, by reducing the number of packages people *need*, or at the user side, by reducing the number of packages people *decide to use*.


#### User-centric reductions


Not happening.


#### Library-centric reductions


Most of Copay’s requirements are small utility functions, deep down in the dependency chain. Part of the reason there are so many is that JavaScript doesn’t have a standard library. For example, the canonical i18n package for [js](https://www.npmjs.com/package/i18n) has 224 dependencies, while the [python](https://github.com/danhper/python-i18n) one has 0. While they likely have different features, the difference is still an indication of how much a standard library reduces dependencies.10 If I wanted to dependency attack `i18n`, there are 224 maintainers I could compromise. If I wanted to attack the Python package, there’s only one.


One way to reduce the number of maintainers, then, is to use more centralized packages: large packages which provide a diverse array of utilities, somewhat akin to a standard library. This both reduces the number of packages and the relative number of *untrusted* packages: the standard libraries could be maintained by people with *explicit* responsibility. Presumably these fewer maintaners would also have a change bureaucracy and get paid for their open source contributions. Paying one organization is a lot easier than paying 42 organizations.


This is in contrast with the current culture of many small modules, of course, and npm devs have said that there were [deep problems with large packages](https://blog.npmjs.org/post/162134793605/why-use-semver). However, we also have seen that this *would* work for js. [lodash](https://www.npmjs.com/package/lodash) is downloaded over 15 million times a week. It’s also part of the JavaScript foundation, implying a degree of security, responsibility, and auditing.


By contrast, something like [glob-parent](https://www.npmjs.com/package/glob-parent) is a utility downloaded 10 million times a week and is maintained by one person, and has a dependency maintained by two other people. Both of these would be prime candidates for a dependency attack, and so are prime candidates for combining into an aggregated utilities package.


## Why don’t people pin packages?


> Not only do safety constraints sometimes conflict with mission goals, but the safety requirements may even conflict among themselves.


There are many reasons why people have floating dependencies. Here are three of the more relevant ones:

1. Multiple separate packages might use the same dependency. If all of them pin to a specific version, you will need multiple copies of the same dependency, adding bloat and making things harder to audit. But if they all had floating versioning, then you could install a version that satisfies all of them.
2. Version requirements and transitive dependencies can interact in really strange and unintuitive ways.
3. Dependencies can have bugs and security vulnerabilities, and you should be updating them as soon as these are fixed. By floating your requirement you can automatically include patches whenever you upgrade.


(3) is especially interesting. It doesn’t only encourage people to automatically include patches. It also can encourage people to automatically update major and minor versions. Maintainers often patch the latest version of the package as well as *some* older versions of the package. Eventually, older versions can be “end-of-lifed”, meaning it will no longer get even critical security patches. If you are using an EOLed dependency and need to patch it, you will have to upgrade to a supported version first, which may break the public API. So people will regularly upgrade to new versions, even if they don’t need it, just to make sure that they can painlessly add in security patches.


This puts two safety constraints in conflict. On one hand, you want to audit package updates to make sure they are safe, which means slow, infrequent upgrades. On the other hand, you want to include critical security patches ASAP, which means fast, regular upgrades. Leveson considers these conflicts a sign that you need to think very carefully about your system design before building it. Is there a way to design npm package management to satisfy both constraints?


No idea. One thing I think *might* help is if maintainers could put information beyond “major, minor, patch” in their package versioning. Then users could pin packages but quickly identify which ones need to be updated for security reasons. I don’t think npm currently provides this.


In general, npm provides *very* little help with analyzing packages. There’s no way to distinguish high-risk vs low-risk packages in your setup, or say “upgrade this package unless it added a new dependency” or anything like that. This makes auditing much harder than it already is, as there’s pretty much no official tooling designed to help you.


## Why is JavaScript insecure?


> Usability and safety, in particular, are often conflicting; an interface that is easy to use may not necessarily be safe.


There are some attempts to make JavaScript more secure, like `object.preventExtensions` or [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode). These assume one of two things:

1. The developer is trying to prevent *unintentional* encapsulation mistakes by users.
2. The developer is trying to prevent security holes via code submitted by *clients*.


In a dependency attack, it’s neither: the malicious code is directly included as part of the final package. This means it has the same privilege as everything else and can subvert any attempts to enforce script security.


This is another case of model drift. JavaScript was originally designed under the assumption that scripts would be small with few dependencies under the constraint of “never break browser backwards compatibility.” As the use case changes (to server use and eventually native apps) and the style changes (using thousands of small packages), JavaScript requires new security constraints. However, the compatibility constraint is even more important, limiting what changes we can make. The mission constraints directly conflict with the security constraints.


As with the minification, backwards compatibility is not a major constraint for Electron apps. They all run in the same browser and do not need to support IE10. Electron could conceivably run a more locked-down version of JavaScript. In fact, Electron *does* support this, but almost all of these features are [disabled by default](https://github.com/electron/electron/blob/master/docs/tutorial/security.md). Opt-in security is much less effective than opt-out security.


It’s important to point out that this problem isn’t unique to JavaScript. The runtime itself has to enforce PoLP too: if it f.ex doesn’t restrict which modules can make http requests you can get something like the [AndroidAudioRecorder attack](https://blog.autsoft.hu/a-confusing-dependency/) even though Java has good modular encapsulation. But I get the impression that it’s impossible to enforce runtime PoLP if the language has powerful runtime metaprogramming. This potentially means that any interpreted dynamically-typed language (Ruby, Python, etc) can’t completely prevent this kind of attack.†11


## Why was the npm response so slow?


> Safety starts with management leadership and commitment. Without these, the efforts of others in the organization are almost doomed to failure.


People in the thread immediately emailed support@nodejs.com. A few others tweeted at them. Neither of these are the official security channels. According to the [npm Security Policy](https://www.npmjs.com/policies/security), the appropriate channel is security@nodejs.com, which is “the best and fastest way to contact npm about any security-related matter.” Matters are triaged in one business day.


This is *also* the wrong channel. security@nodejs.com is only for security issues related to npm software. Third-party package vulnerabilities are handled by [Security Working Group](https://github.com/nodejs/security-wg), who very explicitly [is not responsible](https://github.com/nodejs/security-wg#private-nodejs-core-security-group) for security@nodejs.com. Rather, you are supposed to either submit at their [HackerOne page](https://hackerone.com/nodejs-ecosystem) or email them at security-ecosystem@nodejs.com. Neither of these channels is documented *anywhere* on the official npm page.


To make matters even more confusing, as of 01/01/19 the HackerOne page currently isn’t accepting new reports. The WG Github page also links to the [*private*](https://hackerone.com/nodejs) Node HackerOne, which recommends people report security vulnerabilities to the *package maintainer*. Finally, the [npm security advisory page](https://www.npmjs.com/advisories/737) suggests you report vulnerabilities… by emailing security@nodejs.org. The instructions on what to do are inconsistent and contradictory.


Responses can take a long time, and updating the security advisories can take even longer. [For one “critical” vulnerability](https://www.npmjs.com/advisories/734), the issue was submitted in August, acknowledged as a critical issue in September, and submitted as an advisory in November – a time lag of several months. `event-stream` was actually on the *fast* end of things.


If I was doing a proper STAMP analysis, I’d have to zoom out here and investigate why npm places so little emphasize on package security. Is it a manpower issue? A priority conflict? Something they just didn’t think about? But I’d need npm internals to figure this out, which I don’t have, so we’ll have to stop here.


# Conclusions


When accidents happen, we often try to find “the root cause”, the one thing that can be fixed to prevent the problem happening again. In the case of Leftpad, it was that people could freely unpublish their packages and break dependencies. Here, the “root cause” is usually either “no maintainer responsibility” or “no user audits”. Fixing either of these (if they are fixable at all) may prevent *this specific* attack from happening. But it would not prevent any variations on the attack, just as fixing “the root cause” of Leftpad didn’t prevent the `event-stream`  attack. We need to examine the entire system to find what made it unsafe.12


The attack started when Tarr transfered control of the package and succeeded because Copay didn’t audit the change. But there were many, many system properties that made it unsafe. Here are just a few:

1. The node ecosystem favors lots of small packages with one or two maintainers
2. Most maintainers are random folk who did not expect or want the responsibility
3. Heavy dependence on legacy, often-obsolete packages
4. Dependencies are transitive
5. Very difficult to audit packages, or get additional information on them
6. No way to distinguish high-risk from low-risk packages
7. What’s uploaded to npm doesn’t need to match what’s uploaded to Github
8. Most bundlers default to including minified code, even in standalone applications
9. People use preminified code instead of globally minifying code
10. Electron used configuration assumptions from legacy JS that were inapplicable in the new context
11. Electron does not enable most security features by default
12. Users are encouraged to regularly and automatically patch
13. No way to restrict JavaScript module privileges
14. Inconsistent information on how to report security vulnerabilities
15. npm doesn’t prioritize addressing security issues in third-party packages


Fixing the “root cause” is fast and cheap. Changing the fundamental system properties is slow, expensive, and risky. It may conflict with the system’s goals, such as ease-of-use and backwards compatibility, and it may require a lot more money thrown at open source. But we should at least acknowledge that these properties exist, and that they influence how easy and common these attacks are. The system cannot be made safe by root cause fixes alone.


---


So that was my first STAMP analysis! I don’t know how good it is: I think I ended up focusing too much on specific components and not enough on the social forces. I also think in a couple places I got hung up on auditing and/or let my biases shine through. But I think this identified a lot of interesting system issues. That tells me that the STAMP process is useful: if an outsider to npm and security can find interesting stuff this way, then it’d probably be super useful for actual domain experts, too! Or maybe I just identified boring surface-level stuff. I have no way of knowing!


Oh, and this barely scratched the surface of STAMP. This is just the easiest parts of accident analysis. She has a lot more to say about both accidents and the broader safety system in [her book](https://mitpress.mit.edu/books/engineering-safer-world). In the lower-left sidebar there’s an option to download the book for free. Most people miss that. You can also see her homepage [here](http://sunnyday.mit.edu/) and learn more about all the cool stuff she did.


Anyway, if you got this far, might as well plug [my business](https://www.hillelwayne.com/consulting). I teach companies how to use [formal methods](https://www.hillelwayne.com/talks/distributed-systems-tlaplus/) to build complex systems more quickly, cheaply, and safely. It *probably* wouldn’t have helped at all here but it’s still pretty useful! Feel free to [email me](mailto:consulting@hillelwayne.com) if you’re interested in learning more.


*Thanks to [Richard Whaling](http://twitter.com/richardwhaling), [Richard Feldman](https://twitter.com/rtfeldman), and [Marianne Bellotti](https://medium.com/@bellmar) for feedback.*


# Update 1/02/19


A couple of people responded with corrections to some things I said. Instead of modifying the post to be accurate, I think it’s much more interesting to talk about them after. This way I can compare the corrections to the original analysis and ask *why* these mistakes happened. Is it inexperience, oversight, a flaw in STAMP, or something else?


### Correction: npm/Github mismatch


In the analysis I said that npm and Github can have different versions of the code and that the attacker exploited this with `test/data.js` but not with the `flatmap-stream.min.js`. I also asked why he didn’t also do it with `flatmap-stream.min.js` and admitted I didn’t have a good answer.


Well turns out I was wrong in the first place! [Daniel Ruf](https://twitter.com/DanielRufde/status/1080531654010159104) helpfully pointed out that the attacker *did*, in fact, place an innocent file on Github. That’s one mystery cleared up for me.


On one hand, I’m pleased that I still identified it as a possible safety failing even when I thought it was irrelevant. STAMP still turned it up, which speaks to the power of the technique. On the other hand, I’m also pretty unhappy that I made the mistake. I *think* it’s an “oversight” error, the kind I’d be making even if I completely mastered this kind of analysis. While I talked about it as part of zooming out, it’s a mistake I made in constructing the proximal chain. I think a potential fix might be to have two people independently do that. Or maybe there’s a way to formally review proximity statements.


The link above is a twitter thread with a few other comments by Ruf. I’ll admit I don’t understand some of his corrections. As I said in the beginning, I’m an outsider here. This same process would probably be much more effective for a person who already knows the domain.


### Correction: security of dynamic languages


I said that I thought any dynamically-typed language “couldn’t completely prevent this attack” due to runtime metaprogramming. [Justin Cormack](https://twitter.com/justincormack/status/1080597800855982082) was kind enough to share [this](https://medium.com/agoric/pola-would-have-prevented-the-event-stream-incident-45653ecbda99) article on how they’re trying to fix that in JavaScript. In particular [this](https://docs.google.com/document/d/1h__FmXsEWRuNrzAV_l3Iw9i_z8fCXSokGfBiW8-nDNg/view#heading=h.v9j0bjkph3tv) NodeJS discussion, [this](https://github.com/tc39/proposal-realms) Realms proposal, and [this](https://github.com/Agoric/SES) frozen JavaScript environment. So yeah, I was completely wrong in saying it’s impossible to secure dynlangs.


I think I either would have found this by doing a third zoom-out, or I wouldn’t have found this with STAMP. Most accident analysis literature seems to not focus on “what is being currently done to fix these issues”, but I’m really uncomfortable making sweeping statements about a field I’m just learning. I’m filing this one as “something that might or might not be an issue and should be revisited later, once I’ve gotten better.”


Unrelated: POLA sounds much nicer than PoLP does.


### Correction: NPM email address


[Wes Mason](https://twitter.com/1stvamp/status/1082340746093576192) provided some corrections on the NPM support system. I wrote `security@nodejs.com` instead of `security@npmjs.com`, a total slip on my part. He also said that the wg is not responsible for npm vulnerabilities: this is something I don’t thnk is easily discernable from the pages. Finally, he brought up one more issue I didn’t know about: there was a bug in the [security vulnerability submission form](https://twitter.com/1stvamp/status/1082341471716548609) which prevented submissions from going through. This is a perfect example of the kind of issue I wouldn’t have been able to find without having internal access to the NPM organization. This is one of the reasons Leveson assumes that the investigating team has internal access; you can find out a lot more that way.


---

1. All quotes, unless otherwise noted, are from *Engineering a Safer World.* You can get it for free [here](http://mitpress.mit.edu/books/engineering-safer-world).
 [return]
2. STAMP is short for **S**ystem-**T**heoretic **A**ccident **M**odel & **P**rocesses. It’s an umbrella term for an array of different techniques. The one we’re applying here is STAMP accident analysis, which Leveson calls **CAST**, for **C**ausal **A**nalysis Based on **ST**AMP. Could you tell that Leveson did a *lot* of work for the government?
 [return]
3. I originally used “npm” to refer to the CLI and registry and “NPM” to refer to the company that produces them. The company, though, is actually [npm Inc](https://twitter.com/seldo/status/1080590211816378368), which is also lowercase. In cases where it’s important to distinguish them I’m using “npm Inc” for the company and `npm` for the products.
 [return]
4. For this analysis I’ll say “dependent” to mean a dependent package, “user” to mean a library that depends on the package, and “client” to mean a person using the final product/app.
 [return]
5. Regular readers of this blog might notice that this is very similar to the formal methods I’m so fond of. I think my love of FM is a reason why STAMP is so interesting to me, but I’m probably presenting it in a way that’s more sympathetic to that interpretation.
 [return]
6. One caveat: in STAMP Leveson assumes the system is hierarchal: even if the organization is distributed, there is at least one group that everybody indirectly reports to. `event-stream` involves a few different independent actors. I tried to adapt the ideas as best I could.
 [return]
7. Why *didn’t* the attacker exploit the npm/github mismatch? They actually did: the minified file loaded more code from `./test/data.js`, which was uploaded to npm and not Github. I have no idea why they didn’t do the same thing with the minified file.†
 [return]
8. Okay this isn’t totally accurate. Electron stores the source code for all JavaScript [in memory](https://github.com/atom/atom/pull/17926). So there’s a good reason to minify Electron code, too: it reduces the memory footprint. But if that’s an issue, you’d be better off *globally* minifying your code as opposed to including minified packages, so using minified dependencies is an even worse idea than it already is.
 [return]
9. There’s also an [npm package](https://www.npmjs.com/package/string.prototype.padstart) for a `padstart` shim, which has been completely unnecessary for two years now. It’s still downloaded 500k times a week. 
 [return]
10. Earlier, though, I said that many transitive dependencies might be owned by the same person. This might be the case with i18n too. We can also compare the direct dependencies: 9 developer and 6 user dependencies for js, 2 developer and 0 user dependencies for python.
 [return]
11. I’m generally super skeptical of the idea that static typing or pure FP reduce software bugs. With that in mind, I’m going to bite the bullet and say that this particular attack would not have been possible in a pure typed FP language, like Elm. Adding a side effect would mean changing the type signature, so users of the module would get a type error. (Also, Elm forces you to bump the major version if you change the types, you couldn’t hide it in a patch.)
 [return]
12. I don’t think the npm team was acting in bad faith, and I don’t think they were incompetent or anything. I think that property analyzing an accident takes a lot of skill and most engineers (including me) don’t have that skill. Which is why I’m practicing STAMP.
 [return]
