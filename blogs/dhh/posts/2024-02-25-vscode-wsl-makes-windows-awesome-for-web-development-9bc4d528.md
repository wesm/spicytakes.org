---
title: "VSCode + WSL makes Windows awesome for web development"
date: 2024-02-25
url: https://world.hey.com/dhh/vscode-wsl-makes-windows-awesome-for-web-development-9bc4d528
slug: vscode-wsl-makes-windows-awesome-for-web-development-9bc4d528
word_count: 1086
---

I’m kinda shocked. Windows actually got good for web developers. Between
[VSCode](https://code.visualstudio.com/)
,
[WSL](https://learn.microsoft.com/en-us/windows/wsl/about)
, and Intel’s latest desktop chips, I’ve been living with a PC for over a week that runs my programming tests faster than an M3 Max, ships with an excellent window manager out-the-box, and generally feels like a completely viable alternative to macOS for working with the web.
Hell, not just viable, but better in many regards. WSL lets you run a real Linux distribution natively, so you can use the same package manager that you’ll deploy against. Oh, and since it’s x86, you’ll be building Docker images for your server hardware in a fraction of the time it takes to multi-arch on arm64.
Now it’s true that to get this kind of speed, you need to rock a desktop machine. The Dell I got had an Intel i9-14900K, which is how you get those 500+
[Speedometer 2.1](https://browserbench.org/Speedometer2.1/)
scores, super fast Docker builds, and record-setting programming test runs. And this beast surely consumes far more wattage than does the M-series of chips.
But I had somehow bought the premise that an M3 Max was the undisputed king of quick in mainstream computers today. Not so. That
[$3,200 M3 Max MacBook](https://www.apple.com/shop/buy-mac/macbook-pro/14-inch-space-black-apple-m3-max-with-14-core-cpu-and-30-core-gpu-36gb-memory-1tb)
can in fact be beat by a
[$2,349 Dell XPS](https://www.dell.com/en-us/shop/desktop-computers/new-xps-desktop/spd/xps-8960-desktop/usexpsthcto8960rpl27)
in the tests that are likely to matter to most web developers. Especially for those who leave their laptop at the desk 95% of the time.
I did also have a go with
[a Framework 13 laptop](https://frame.work/)
, which uses the AMD Ryzen 7040 CPU. That’s a really nice chip, but it still lags behind the M-series by a bit. It’ll run the Speedometer 2.1 in 300-350 and our HEY test suite in about 3m31s . My M2 Pro laptop can hit over 500(!) on the Speedometer, and complete the test suite in 2m16s (although it quickly throttles on repeated runs to ~3 minutes).
So Apple clearly still has a bit of an advantage with laptops. And I’m sure ultimate battery life is also better, even though I found it perfectly adequate with the Framework 13.
It’s on the desktop, with chips like the i9-14900K, that Windows shows what’s possible outside the M-chip universe. That CPU clocked the fastest ever run I’ve seen on our HEY test suite with a 1m37s result. And it too can push above 500 on the Speedometer 2.1.
But even on the laptop side, there’s plenty to like about the alternatives. Framework has a super novel approach to repairability and upgrades. You can easily swap out any component by yourself, often without tools. Anyone who went through multiple rounds of keyboard replacements with their MacBooks in the horror days of the butterfly keyboard can appreciate how helpful that might be.
Even more impressive, though, is that you can
[keep upgrading the CPU and motherboard](https://frame.work/marketplace/mainboards)
on the Framework! They first launched with 11th gen Intel chips, then released a 12th gen board, and now this AMD variant. You could have kept the same laptop through all those generations. Very cool. And it does make me feel a bit sheepish having bought entirely new laptops to go from M1 to M2 to M3.
So there’s a lot to like in Windows land these days. The M-chip shock dominance has subsided, and even if there’s still an advantage on the laptop side, it’s much less than it has been. That surprised me. But it’s surprised me even more how well Microsoft has managed to integrate Linux with Windows. I thought for sure there’d be a performance penalty to running under WSL. Or that it would be clunky and kludgy. But it just wasn’t.
VSCode is part of the trick here. It ships out of the box with an excellent WSL integration where all the files actually live inside the Linux subsystem, so there’s none of that old cross-the-filesystem-chasm slowdown that I remember from my last go-around with Windows.
Literally all you have to do is open Powershell, type “wsl --install”, pick your username/password, and you’ll have Ubuntu 22.04 running. Then install VSCode, which auto-detects that WSL is installed, and voila, you can type “code .” in the Ubuntu terminal to open any directory in VSCode on the Windows side. Now that’s slick!
After seeing all this in action, and living with it for a week, I seriously contemplating switching daily desktop driver. But I ultimately didn’t. And the reason is that I’m simply just not willing (yet?) to give up
[TextMate](https://macromates.com/)
for VSCode nor willing to deal with the font rendering on Windows. I suspect both are pretty idiosyncratic reasons, which almost certainly won’t apply to the broad masses of web developers. Most of whom have already embraced VSCode, and probably aren’t quite as particular as yours truly about font rendering.
And that’s really exciting! That the Mac finally has a no-apologies-needed alternative for people who work with the web and need solid unix underpinnings to get the job done. Apple desperately needs the competition for the mindshare of web developers.
Oh, and did I mention you can actually play AAA games on the PC? That $2,349 Dell ships with an NVIDIA 4070, which is plenty of power to drive everything from Fortnite to Cyberpunk 2077. Games that simply just doesn’t exist on the Mac, and maybe never will.
It’s wild how we’ve come full circle. Microsoft was the top villain of the late 1990s for everyone I knew in tech, and Apple was the underdog darling. Now it’s the other way around. Switching to OSX in 2001 felt like the rebel move. Now daring to run Windows in 2024 would make you the odd one out in a lot of communities. I for one hope to see a bunch of Windows machines, maybe even Framework laptops, at tech conferences going forward.
I’m also keeping both of these PCs at the house. And who knows, if someone eventually ports a color-perfect version of TextMate’s
[All Hallow’s Eve](https://github.com/textmate/themes.tmbundle/blob/master/Themes/All%20Hallow's%20Eve.tmTheme)
theme, I might give VSCode another crack. And if somehow it becomes possible to get Mac-style font rendering, I can’t see what would hold me back (no, the MacType hack ain’t it).
So kudos to Microsoft! By burying the hatchet with Linux, and open source in general, you've arrived at an incredibly productive combination of tools for developers like me. And now the chips from Intel and AMD are finally giving Apple a run on the hardware side too. I just love to see it, and I love to be this positively surprised.
