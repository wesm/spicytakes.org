---
title: "Arch Linux (Omarchy) — 8 Months Later: The Good, the Bad, and the Fixable"
date: 2026-02-10
url: https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/
slug: linux-omarchy-the-good-bad-and-fixable
word_count: 3440
---

![Arch Linux (Omarchy) — 8 Months Later: The Good, the Bad, and the Fixable](https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/featured-image.png)

Contents

This is a follow-up to my part 1 of [Switching macOS to Arch Linux with Omarchy](https://www.ssp.sh/blog/macbook-to-arch-linux-omarchy/), where I documented my first months with Arch Linux and [Omarchy](https://ssp.sh/brain/omarchy/), after switching from 15 years of using macOS and Windows on and off at work since 2003.


Back then, I had a checklist of basics I needed before I could commit to Linux as a daily driver: Obsidian, a Raycast-like launcher for fuzzy finding files and folders, screenshots (Snagit), daylight adjustment (f.lux), calendar events in the top bar. Those were quick wins.


Eight months later, I’ve gone through many more challenges and learnings. In this post, I’ll share which apps replaced my heavily integrated [macOS workflow](https://www.youtube.com/watch?v=sStKFOwNaSM), what my [Omarchy workflow](https://www.youtube.com/watch?v=XOp8lngtmPg) looks like now, and — honestly — what still doesn’t quite work.


## Apps that Replaced My macOS Apps on Linux


Let’s start with which apps and how I changed some of my workflow now in Linux.


Below list goes from complex Raycast replacement that was integrated into my whole workflow with search through files, calculator, emojis to calendar, daylight gamma correction for night sessions to PDF viewer that replaces Finder to sharing screen with Linux window picker, and much more.


It continues with running Windows on Linux with a simple install toggle and finding the right hardware, before I create a conclusion of these initial months using Linux full time for my business and also privately.


### App Launcher and Raycast Replacement: Fuzzy Search, File Search, Clipboard, Math, and so on


One of the first apps to replace that most have, and that I also used, is **Raycast**. It’s an app I couldn’t live without, not only for the fuzzy finder but also for quick calculations, searching files, and clipboard manager.


With **[Walker Launcher](https://ssp.sh/brain/walker-launcher/)** I found the perfect replacement which has this all included and works like a charm.


![/blog/linux-omarchy-the-good-bad-and-fixable/img_Walker_launcher_1760944046142.webp](https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/img_Walker_launcher_1760944046142.webp)

*Functions of Walker available with/| See myTweetfor more information.*


**Search file content** with spotlight - Find files with Walker with built-in preview: 





































[

](https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770740249453.webp)


Opening its containing folder or file with the default program. This is how I search and find anything compared to manually browsing through file explorer. Find any files within seconds with built-in search of Walker (Before I found Walker, I built [my own one](https://github.com/sspaeti/dotfiles/blob/master/hypr/.config/hypr/sspaeti/fuzzy-file-content.sh)).


**Emojis** quick search. It comes with Walker built-in too, but I have my own script so I can find emojis faster as I can change the search term. Very [simple, but powerful](https://github.com/sspaeti/dotfiles/blob/master/hypr/.config/hypr/sspaeti/emoji-fuzzy.sh)

[

](https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770741956438.webp)


**Clipboard managers**, of which there [are](https://github.com/savedra1/clipse) [several](https://github.com/sentriz/cliphist), but Walker comes with one built-in too. Including **search** and **image preview**:


![/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770742102558.webp](https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770742102558.webp)

*Clipboard on opening, with search and image preview.*


Other dedicated clipboard managers are [cliphist](https://github.com/sentriz/cliphist) or [Clipse](https://github.com/savedra1/clipse). There are also other Raycast-compatible launchers for Linux such as [flare](https://github.com/ByteAtATime/flare), Rofi, and many more.


### Keyboard Shortcuts and Quick Symbols


I used [Kanata](https://github.com/jtroo/kanata) for integration of advanced features to switch between my keyboards and some of the advanced use cases such as using CAPS LOCK for vim-like movements. I use `caps + hjkl` to move left, down, up and right with the respective arrow keys as almost all programs work with arrow keys. Also F1-F12 functions with `caps+1` for F1.


For simple replacements, I used XCompose to write Umlauts (`äöü` and special symbols `—«»` and more). I used Karabiner-Elements heavily, and Kanata solved it for me, see my configs at [dotfiles.ssp.sh/kanata](https://github.com/sspaeti/dotfiles/blob/master/kanata/.config/kanata/kinesis.kbd).


### Backups and Data Sync


Time machine on macOS was great. I used sync.com for dropbox-like sync on macOS too. Neither worked on Linux. So I switched to [Filen](https://filen.io/), which has a similar setup and stores the data encrypted, and hosted in Germany. I’m using Stow for all my dotfiles stored in Git. It’s great, check them at [dotfiles.ssp.sh](https://dotfiles.ssp.sh).


I back up my images, personal documents, or scripts also with rsync-scripts to save to my homeserver and encrypted drive on Vultr. See more [Tech Independence](https://www.ssp.sh/blog/self-host-self-independence/).


I also looked at NextCloud for hosting it myself, but for now I just need something that works. As Filen is an Electron app, it just works everywhere.


### Calendar


Calendar is one thing everyone uses, and I used Cron Calendar (later acquired by Notion) a lot, and wanted a good replacement for Linux. Though I use [calendar.google.com](https://calendar.google.com) often on the web.


But the best replacement I found was [Morgen](https://morgen.so/) (built in Switzerland) and is made for Linux first. It has a great preview inside the top bar too and timezones built-in.


Time zones can also be activated by hovering on the time on the left:

[

](https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770740650778.webp)


### Daylight and Gamma light Adjustment


Sunlight adjustment like [f:lux](https://justgetflux.com/). Omarchy comes with one included right now, but I also used `wlsunset` with `wlsunset -l 47.4095 -L 8.5514 -t 3500 -T 6500`, that does the job well.


### Hibernation and Suspending Computer


Hibernation and suspending is something that you take for granted on other operating systems. But on Linux it’s trickier, so it didn’t work out of the box. In the meantime, it comes built into Omarchy.


### Presenting with External Projectors and Screens


Presentations and recognition of presenters and screens. I only had one presentation, but tried many external monitors, and Hyprland (which is responsible for recognizing screens `hyprctl monitors`) works just like macOS by auto-recognizing them.


Even better, I have shortcuts to make them automatically align at the right position. Or use [hyprmon](https://github.com/erans/hyprmon) (one of the great [TUIs](https://ssp.sh/brain/tuis/)) when I need to do it manually.


### PDF Merger


[PDF Arranger](https://github.com/pdfarranger/pdfarranger) for merging multiple PDFs into one or rotating pages of a PDF. It’s open source and better than macOS Preview.


### Need Anything More? Just Build (vibe code) it Yourself


If you need something, you just build it with [Claude Code](https://ssp.sh/brain/claude-code/) and integrate it into your laptop.


No need to ask Mr. Bill Gates or Tim Cook to integrate it. For example, I needed an **edge light for video calls**, or saw someone who had this. I liked it, not that I really needed it (but one day it might be helpful ð). I’ve built a [small custom tool](https://github.com/sspaeti/wayland-edge-light-videocalls) that works out of the box with Hyprland for my future video calls.


![/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770735368009.webp](https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770735368009.webp)

*Check it out atwayland-edge-light-videocalls*


### Screen Sharing Works Differently


For example, screen sharing is not as straightforward because you get a very old frame to pick your windows or output or regions. On top of that, you usually need to pick twice and only the second pick will count. This was very confusing and I documented a fix and how it looks at [Screen Sharing on Wayland (hyprland) with Chrome](https://ssp.sh/brain/screen-sharing-on-wayland-hyprland-with-chrome/).


But with the latest updates of Omarchy, that has also been solved and it works out of the box and looks beautiful now:


![/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770754480836.webp](https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770754480836.webp)

*Compared to the default DOS screen picker, this is beautiful, or just modern.*


### Others: Virtual Envs, Remote Desktop and Adding Printers


For **virtual environments**, I’m using Mise, as it comes pre-installed on Omarchy. Before, I used `asdf`.


Remote desktop to virtual desktops works great with `xfreerdp3`, which connects well to the Windows VM.


Need to import images from camera? Not as UI-driven as on Mac or Windows, but amazingly simple and fast with gphoto, see [Import Files on Arch Linux (gphoto)](https://ssp.sh/brain/import-files-on-arch-linux-gphoto/).


Adding printers might be needed at some point. This can be done UI-driven with system-config-printer - CUPS configuration tool. Or do it the terminal way with `lpadmin`, see [Adding Printer on Linux](https://ssp.sh/brain/adding-printer-on-linux/) for more information.


## Running Microsoft Windows inside Linux


A big one is to run another operating system, in this case Windows, as part of your OS. E.g. I use Microsoft Office often, so I can quickly start up Windows with Office when needed.


The best part is that it uses only Docker, meaning easy setup, separated from my configs. It’s a single-click setup taking 15 seconds.


Installing and integrating seamlessly in a Docker VM works [superbly with Omarchy](https://learn.omacom.io/2/the-omarchy-manual/100/windows-vm). I submitted a [PR to Omarchy](https://github.com/basecamp/omarchy/pull/1333) to make this available to everyone. The built-in version in Omarchy (the first version) was done by me, and it was merged into core and is now available to everyone.


![/blog/linux-omarchy-the-good-bad-and-fixable/windows-omarchy-vm.webp](https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/windows-omarchy-vm.webp)

*Tweetand thanks fromDHHhimself.*


It’s now easier to run Windows on Linux than natively on a Windows machine ð.

Many ways of integrating: Omarchy uses Dockur

There are many options:

- [dockur/windows](https://github.com/dockur/windows): Windows inside a Docker container (used in Omarchy).
- [Winapps](https://github.com/winapps-org/winapps): Run Windows apps such as Microsoft Office/Adobe in Linux (Ubuntu/Fedora) and GNOME/KDE as if they were a part of the native OS, including Nautilus integration.
- [WinBoat](http://winboat.app/): an easier version than Winapps:  - Run Windows Apps on Linux with Seamless Integration.


## Finding the Right Hardware: The Reasons why not to Switch


Everyone knows the stereotypes about Linux. WiFi won’t work, Bluetooth won’t connect, constant interruptions. And beyond that, there’s the hardware fear, that you simply can’t match what Apple offers. A common sentiment:


> I’m currently with this dilemma. I’m an experienced Linux user, but over the years gravitated towards Macs (especially M-series) and unfortunately they do make better hardware, at least for my use ð I just *can’t* move to a machine with a much worse battery life, display, webcam, speakers etc. I know some good Linux-friendly laptops exist, but it’s still a downgrade, for me. If someone made better hardware, I’d probably jump over right away. [Tweet](https://x.com/DenLoginoff/status/2021079777608614290)


I thought the same. The great keyboard, camera, speakers, trackpad, battery. Apple just nails the whole package. But what I found is that I didn’t actually have to downgrade.


I started with a **Lenovo ThinkBook 14 G7 ARP (AMD)** with 32 GB RAM. Great build quality, beautiful look, and the keyboard surprised me, with much more travel and grip than the MacBook. See more on [Part 1](https://www.ssp.sh/blog/macbook-to-arch-linux-omarchy/#choosing-the-hardware).


Once I realized this would become my daily driver, I searched for something more powerful for data engineering work and landed on a **Tuxedo InfinityBook Pro 14 Gen10 AMD** with 128 GB (!!) RAM, an AMD Ryzen AI 9 HX 370, and AMD Radeon 890M.


![/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770739390246.webp](https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/img_Switched%20from%20macOS%20to%20Linux-%206%20months%20in_1770739390246.webp)

*My Tuxedo InfinityBook Pro 14 Gen10 AMD, with 128 GB (!!) RAM, AMD Ryzen AI 9 HX 370 , and AMD Radeon 890M.*


First impressions: super smooth, even snappier than the Lenovo. Obsidian and other apps feel a tiny bit faster. The 3K 500-nit display is stunning. Crisp, bright, better than my external 4K monitor. And it’s **matte**, which I’d forgotten I actually prefer. It works outside, no glare. The Lenovo’s anti-glare screen was equally great in that regard.


The keyboard has less travel than the Lenovo ThinkBook (which I really loved), more like a MacBook, which is fine but feels slightly cheap. I mostly use external keyboards anyway. The fingerprint reader is also missing, which I’d grown to love on both MacBooks and the Lenovo, where it worked flawlessly on Linux. The trackpad is smooth and great to work with daily, though palm detection caused some cursor jumping in the first days, not as good as Apple’s, but perfectly usable.


Battery life was a pleasant surprise. My Tuxedo (80Wh) delivered battery life comparable to my M1 Max MacBook. I spent a whole afternoon in the library and it was still above 70%.


With Omarchy, everything just worked out of the box. No WiFi or Bluetooth issues, speakers with sound, all good.


But it’s not perfect, by far. I get some [strange popping sounds from the laptop](https://www.reddit.com/r/tuxedocomputers/comments/17pzcet/strange_popping_sounds_coming_from_my_laptop/), mostly after hibernating once or twice. Not sure why, and it probably shouldn’t happen. There are many other [Notebook & Desktops for Linux](https://ssp.sh/brain/notebook-desktops-for-linux/) to choose from, Framework being one, but choosing is still tricky, as chipset and GPU support on Linux matters, and you want something state-of-the-art.


Another side effect, as [Kevin says](https://x.com/KevinNaughtonJr/status/2021009900097483120) of not having an expensive Macbook:


> My favorite part aside from customization is just that i don’t care about my machine at all: it gets lost? breaks? stolen? i get a new machine, run 1 command and everything is back exactly as i left it. Macs on the other hand are expensive to buy and repair which makes people worry and worry = less peace of mind.

Follow the evolution on Social Media

The whole story I documented in threads on [Twitter](https://x.com/sspaeti/status/1942502383923134464) and on [Bluesky](https://bsky.app/profile/ssp.sh/post/3lug5oijnjc22), follow these to see the history and events in they happened.


## Conclusion of Using Linux for 8+ Months


After using Windows since 2003 and macOS for more than 15 years, how do I feel after 8 months on Linux?


**Things mostly work great**, but need a little tinkering to begin with, or work differently. The biggest difference, which I like a lot, is a more terminal-native workflow. Closer to the command line. Using lots of [TUIs](https://ssp.sh/brain/tuis/).


**When I started**, I just wanted the same as I had on macOS. After getting familiar with the new environment, with all the small utilities, tools and programs Linux has, I got many more tools to choose from. Sometimes much better, though terminal-based, but fast and direct. Sometimes you obviously miss a tool that has no replacement (for me still Snagit).


Besides the obvious (terminal-native, best-in-class Tiling Window Manager with Hyprland, no-latency navigation), there’s something harder to put into words. The OS is what we use every day, so when you can quickly fix or change a small thing to give you more joy or more productivity, it might just put a smile on your face whenever you use that feature. At least it still does for me. And since all my configs live in [dotfiles](https://dotfiles.ssp.sh) and my data syncs externally via Filen and Obsidian, setting up a new machine is a single command.


### What I Thought I’d Miss vs. What I Actually Miss


Before I switched, I thought I’d miss all my [Setapp](https://setapp.com/), my MacBook hardware, and the stability of just working. Most of my apps work on my new machine and even better software-wise, so I’m still quite happy to have made the switch, even more so watching macOS get slower with each install without real benefit (looking at the Liquid Glass update) and Windows stuffing Copilot into Notepad and recording your screen with Recall.


What I **actually** miss are simpler things: the **stability** of having calls everywhere all the time with Apple reliability and inbuilt mic/speaker/camera. A crash because the GPU is fails1 after hibernation right before an important meeting. Hibernation and suspending was quite a battle to get working, but it seems to just work now.


What I like about Linux: it might not work out of the box for every laptop or every program, but you can actually fix it, and from that moment you know the problem, you learned something about computers, and the error will not appear again. Unlike other operating systems that change stuff you set in settings for a reason, only to learn that certain updates turned that checkmark back on.


### Tinkering and Troubleshooting: Not Everything Just Works


Probably, without [Claude Code](https://ssp.sh/brain/claude-code/), I wouldn’t have made the switch, or I would have made it, but probably wouldn’t have stayed. When something happens, e.g., a crash out of nowhere, I just open Claude and say: I had a crash, I am running Arch Linux, please check the logs what went wrong. And what I get is a full analysis of what went wrong, some fixes and suggestions. Knowing that Linux has 100 different setups, different drivers for every hardware, this is a non-negotiable lifesaver.


With Linux you also have to troubleshoot bugs, but at least it’s free software and open source, and honestly, they seem even less frequent than with commercial, paid products these days.


If you’ve read this far, thank you. What’s your experience, are you thinking about switching, or already on Linux? Let me know anywhere on [Bluesky](https://bsky.app/profile/ssp.sh/post/3melam6gxrf2m), or [Twitter](https://x.com/sspaeti/status/2021528330324086934).


---


Again, if you want to watch a full video workflow, check my short video about it: [Omarchy Arch Tiling Window Workflow (macOS comparison) - YouTube](https://www.youtube.com/watch?v=XOp8lngtmPg). Or [my macOS workflow](https://www.youtube.com/watch?v=sStKFOwNaSM) as a comparison and what I switched from.


## Appendix: Troubleshooting and Things That Didn’t Work So Well, or I Had Already Fixed


**GPU Crashes (AMD Radeon 890M).** This was the biggest recurring issue. The GPU’s MES (Micro Engine Scheduler) would become unresponsive and crash the entire system, triggered by Brave browser, Google Meet video calls, and Kdenlive video encoding. The root cause is that the Radeon 890M (gfx1150/RDNA 3.5) is still very new, and driver support on bleeding-edge kernels (6.17–6.18) is immature. Solutions included disabling hardware acceleration in Brave (`brave://settings/system`), adding kernel parameters (`amdgpu.gpu_recovery=1 amdgpu.noretry=0 amdgpu.ip_block_mask=0xfffff7ff`), and considering the LTS kernel as fallback. The community is tracking this on [Framework forums](https://community.frame.work/t/amd-gpu-mes-timeouts-causing-system-hangs-on-framework-laptop-13-amd-ai-300-series/71364) and [AMD’s GitLab](https://gitlab.freedesktop.org/drm/amd/-/issues/3067).


**Keyboard Freezing After Suspend (Tuxedo).** The internal keyboard would stop working after suspend/resume cycles due to a firmware bug in the keyboard controller (i8042). Fixed by adding `i8042.nomux=1 i8042.reset=1 i8042.noloop=1 i8042.nopnp=1` to the kernel command line in `/etc/default/limine` and regenerating the UKI with `sudo mkinitcpio -P`. Shared the solution on [Reddit](https://sh.reddit.com/r/tuxedocomputers/comments/1ndq7vw/comment/ne5kjob/).


**Hibernation Not Resuming.** After suspend-then-hibernate (triggered by closing the lid), the laptop wouldn’t resume and required a fresh boot. The cause was missing `resume=` and `resume_offset=` kernel parameters. Omarchy’s hibernation setup script added the mkinitcpio hook but never added the actual kernel parameters. Fixed by calculating the swap offset (`sudo btrfs inspect-internal map-swapfile -r /swap/swapfile`) and adding `resume=/dev/mapper/root resume_offset=<offset>` to `/etc/default/limine`. Documented the fix in [this Omarchy issue](https://github.com/basecamp/omarchy/issues/4259#issuecomment-3804954054).


**Thermal Throttling (Lenovo).** The Lenovo ThinkBook would hit 99Â°C and become unusable during video calls. Turned out the bottom intake vents were blocked when the laptop sat flat on a desk. Simply elevating the laptop dropped temps to 73–77Â°C and performance was completely fine, even running stress tests while screen sharing. A laptop stand solved it permanently.


**WiFi Speed Drops (Tuxedo, Intel AX210).** Speeds dropped to 2–72 Mbps after a system update. Root cause was a bug in `linux-firmware-intel` version 20251125 that caused the Intel AX210 card to negotiate very low RX bitrates. Fixed by downgrading to the October firmware (`sudo pacman -U /var/cache/pacman/pkg/linux-firmware-intel-20251021-1-any.pkg.tar.zst`), disabling WiFi power save permanently via a systemd service, and adding `IgnorePkg = linux-firmware-intel` to `/etc/pacman.conf` until a proper fix ships.


**Keyring/Brave Re-login on Every Boot.** Brave asked for login credentials after every reboot because the gnome-keyring file kept getting corrupted. This was caused by SDDM autologin. Without entering a password at login, PAM can’t unlock the keyring. The ultimate fix was launching Brave with `--password-store=basic` in the autostart config. Documented in [this Omarchy discussion](https://github.com/basecamp/omarchy/discussions/3523#discussioncomment-15286162).


**Sudoers Misconfiguration.** While adding a NOPASSWD rule for a keyboard-switching script, I accidentally broke sudo access entirely. Had to boot into recovery/single-user mode to fix `/etc/sudoers`. Lesson learned: always have `sspaeti ALL=(ALL) ALL` as a separate line and be very careful with `visudo`. Documented the recovery process in an emergency recovery guide.


**Screen Recording VFR Issues.** Omarchy’s screen recorder (`gpu-screen-recorder`) produces variable frame rate videos by default, which Kdenlive can’t edit properly. The fix is adding `-fm cfr` to the recording command. Additionally, Kdenlive’s VAAPI hardware transcoding crashed the GPU (same MES issue), so software encoding (`libx264`) is needed for now.


**CPU Fan Noise When Plugged In.** The system switched to “performance” CPU governor when plugged in, causing constant full-speed fans even at low load. Fixed via `powerprofilesctl set balanced` or through Omarchy’s built-in power settings menu.

### Building yourself: Fuzzy image Finder
Fuzzy find my images, a tool I built as I couldn't find a replacement for Snagit.
<a href="https://ssp.sh/brain/horizontal-and-vertical-cut-out/">Horizontal and Vertical Cut Out</a> that Snagit provides does not work on Omarchy. I had a workaround with GIMP Horizontally and Vertically crop out, but now Editt is supporting it. [Editt](https://github.com/mirarr-app/editt) also supports horizontal cut out now.
I use Satty for simple screenshotting, sometimes Figma for more advanced workflow, GIMP Horizontally and Vertically crop out for a workaround. I'm also using [Using FireShot](https://getfireshot.com/using.php#using) inside the browser for scrollable images. And there's a full list at [List of tools](https://wiki.archlinux.org/title/Screen_capture#Screenshot_software). Still trying to find the old Snagit workflow, but getting there. Note: If you are not yet on Linux, but on macOS or Windows, buy a one-time licence for Snagit and be happy ever after if you take screenshots. You can thank me later :). Ksnip has vertical and horizontal cut out too, but does not work on Wayland.
I built an image search first: [image-browser](https://github.com/sspaeti/dotfiles/tree/master/hypr/.config/hypr/sspaeti/image-browser), see <a href="img_Switched from macOS to Linux- 6 months in_1770740977506.webp">my image search tool</a>.

---

1. In my case, I have a newer GPU, which suddenly shuts down because of not having all the fixes released in the drivers and software. Depending on your hardware, you might be more or less lucky. ↩︎

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/linux-omarchy-the-good-bad-and-fixable/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Linux](https://www.ssp.sh/tags/linux/)
[Macbook](https://www.ssp.sh/tags/macbook/)
[Arch](https://www.ssp.sh/tags/arch/)
[Omarchy](https://www.ssp.sh/tags/omarchy/)
[Thinkbook](https://www.ssp.sh/tags/thinkbook/)
[Tuxedo](https://www.ssp.sh/tags/tuxedo/)
[Workflow](https://www.ssp.sh/tags/workflow/)
[Hyprland](https://www.ssp.sh/tags/hyprland/)
