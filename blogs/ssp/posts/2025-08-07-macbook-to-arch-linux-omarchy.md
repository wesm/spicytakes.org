---
title: "My Journey from macOS to Arch Linux with Omarchy"
date: 2025-08-07
url: https://www.ssp.sh/blog/macbook-to-arch-linux-omarchy/
slug: macbook-to-arch-linux-omarchy
word_count: 2388
---

![My Journey from macOS to Arch Linux with Omarchy](https://www.ssp.sh/blog/macbook-to-arch-linux-omarchy/featured-image.jpg)

Contents
ð¶
Featured on Hacker News.
[Read the comments](https://news.ycombinator.com/item?id=44955923)

I switched my five-year-old MacBook Pro M1 Max for a cheap (comparable) Lenovo ThinkBook 14 G7 ARP (AMD) laptop, running Linux (Arch btw, or better, [Omarchy](https://omarchy.org/). And I am having a blast. But not everything is perfect. But let’s not get ahead of ourselves.


This is a short recap after using it for one month on and off (due to repair ð), and the last 2 weeks full time. I want to share what I learned, what I like about the new setup after working for 15 years plus on a MacBook, and on and off on Windows at work. And maybe what is still a little rough.


## Getting Ready for the Switch


Before I could make the switch, I had some pre-requirements I needed to be able to use it as my full-time machine. Here are some:

- ** â Obsidian notes
- ** â fuzzy finder in raycast to open up my favorite files or folder, e.g. if I need to open my Offers template folder
- ï¸âï¸ screenshot like Snagit
- ** â photo program
- ** â daylight adjustment like [f.lux](https://justgetflux.com/)
- ** â  next calendar events in top bar
- ** â Hibernate machine
- â one time backup to store files and OS, or only files?


And most important, instant workspace navigation. The reason why I was upset with Apple: with the latest update, [Yabai](https://github.com/koekeishiya/yabai) didn’t work flawlessly anymore, and also all the updates and constant asking if I want to do this or that got in my way.


During that process, I noticed that many things I was having, like [Setapp Apps](https://setapp.com/) with all the apps like Bartender, VPN, and other apps are nice and useful, but not needed. Or mostly there is a similar, or sometimes even better, alternative out there.


### The Tradeoffs


While I’m super happy with the switch, here are some direct comparison from apps and workflow from macOS to Linux.


**Photo Capturing**

Snagit, my beloved screenshot-taking tool. I haven’t found a similar replacement yet that can cut out in-between the image or store all the captured images in a library. Even OCR search worked out of the box in Snagit, across all my images I took over the years.


You’d say, but who needs this? Yeah, kind of, but it’s super handy, especially if you are a blog writer and explain stuff visually—the speed and quick image manipulation is not yet there.


**It just works**. One thing I noticed lately is that sometimes a shortcut breaks, or something is not working anymore. This is also because Omarchy is just brand new, and I’m inexperienced running Linux as my main OS. But for the last 5 years with the M1, hardware-wise, things just worked. I had to replace my full mainboard as the [GPU was broken](https://bsky.app/profile/ssp.sh/post/3lug5oijnjc22) within the first two weeks, so that might be bad luck. But the quality of MacBooks is just another level. I had 3 or 4 so far since 2010, and each of them held at least 5 years. Crazy good.


**Battery Life**. It’s not the same game anymore. The fan is also mostly running. But that’s one downside I’m willing to accept for a more joyful experience. Also, if I don’t like something on my OS, I just change it. Or if I want to improve a certain way of working, a quick script, a new package, and I’m just flying.


**Backup**. TimeMachine on macOS was great. Gave me peace of mind that if I lose something, I can always recover. I never had to go back file-based, as I have them stored on Sync.com (now with Linux switched to Filen.io), and notes in Obsidian. But when I broke something, or I had to switch MacBooks, one backup, and every little setting was the same. But that’s something I tackle next, so I have peace of mind if I misconfigure something, like yesterday, when I changed the `/etc/sudoers` and I couldn’t log in as sudo anymore ð (yeah, don’t ask!). I could fix it again, though. But stuff like this makes me scared that I can run a wrong command and ruin my perfect setup. I need a backup!


**Cloud Sync**. As mentioned, I had to switch from Sync to Filen, as Sync didn’t run on Linux. But Filen is great, and I’m super happy with it. I also switched from Lastpass to 1Password, took this as a change. I was also thinking about NextCloud on my home server, but I couldn’t switch everything in one go.


**Keyboard shortcuts**. An important one was keyboard shortcuts. I have advanced shortcuts and many different custom keyboards. First I use [Karabiner-Elements](https://karabiner-elements.pqrs.org/) for the vim navigations with `caps + HJKL`, which will then return arrow keys. This way I can use vim navigations in each app, as arrow keys are supported everywhere. For this I used [Kanata](https://github.com/jtroo/kanata/) on Linux. And use [XCompose](https://github.com/kragen/xcompose/) for simple Umlaut or replacements like `««—` when I write.


**App Launcher**, **File content search** and **Clipboard manager**. I used Raycast for all of these. On Windows [Ditto](https://ditto-cp.sourceforge.io/) was great for clipboard only. But with [Walker](https://github.com/abenz1267/walker/) (Launcher), that has built-in file search called *finder*, and an additional tool called Clipse, I have the same features I needed. Plus more than I ever would have dreamed, because Walker is so customizable that you can add a quick script for everything.


WebApps as native apps. Shortcuts for everything. E.g. using Signal, WhatsApp or Figma. Want to change monitor setup from home to office? A shortcut. Want to switch from my mechanical keyboard to the laptop keyboard with different shortcuts? A shortcut. Quickly install a new app? A shortcut. And so on. I never thought that an OS can be customizable to my liking.


Even themes you can change across OS, vim, terminal, and background with one shortcut. The sky is the limit, literally.


## Omarchy: An Opinionated Arch Linux “Distro”


Luckily, I didn’t have to set up all myself. In fact, Omarchy, a soon-to-be distro that runs Arch Linux, does most of it out of the box. And it’s keyboard shortcut-oriented, and worked really similar to [my macOS workflow](https://www.youtube.com/watch?v=sStKFOwNaSM) already. So after I installed, changed a couple of hotkeys, I was almost at the same speed and utility as on my old MacBook, but without the frustrations. Or I should say, other frustrations :)


But huge shoutout to [DHH](https://x.com/dhh) for creating this gem, and making Arch Linux approachable for many developers coming from macOS. After I checked all the scripts and what the community added over time, I saw that so many things were just solved. Screens, function or media keys, cameras, fingerprint reader, printer, and so on, all just worked, almost like on a MacBook.


## How It Began: Taking the Leap


This was the time working out in the wild with Arch Linux, without bringing my Macbook.

[

](https://www.ssp.sh/blog/macbook-to-arch-linux-omarchy/omarchy-coffee.webp)

Writing in a coffeeshop with Arch Linux (Omarchy).


Some comments from the first days: It’s a blast to work with Hyprland, so fast and smooth. Battery level obviously much less, return of the fan noise when running Electron apps ð.


What works: Advanced Karabiner keyboard setup, sync files (had to switch to Filen), Obsidian, and my dotfiles with [tmux](https://ssp.sh/brain/tmux/), [Neovim](https://ssp.sh/brain/neovim/) and all the good jam.


Still to do: Clipboard manager, better Snagit replacement, Raycast search in files/emojis and backup.


I’m surprised with what all worked out of the box, like hibernating, external monitors/keyboards, media keys. Not sure how much is thanks to DHH’s Omarchy, and what’s native Arch Linux support, but it’s amazing.


I’m working on my [dotfiles](http://dotfiles.ssp.sh) to port them to Linux on `_arch-linux`. Lots to configure, but the tools to choose from are endless, and just free and open source. Great world. Thanks to all the people who maintain and create these amazing products.


### Big Upside


Great experience over the Macbook so far:

- The **smooth navigation** with [Hyprland](https://hypr.land/)
- Full screen has **no bezels** at the top or empty bar like Mac. Normal fullscreen uses all the way and does not open on a random workspace at the end of existing workspaces


### Downside


What doesn’t work as well yet, or things I missed in my workflow:

- **Grammarly native app** overlay which is sometimes handy for Obsidian or any other apps to fix grammar. On Linux I need to copy and paste back and forth again. But on the other hand, it does not secretly send each text to the cloud :)
- Microsoft **Teams**/Office that I need for one client has no native app, but the web app works flawlessly.
- **Hibernate**: just sleep and next day come back, everything as it was. Need to shut down to not overheat. (Has been solved in the meantime, but still not the same as MacBook)
- No **Claude Desktop** for MCP. Although I used Claude Code most of the time. (I have replaced with a webapp, is almost the same feel, but no MCP I believe. But Claude Code has it now too, and Neovim too :)
- I could buy cheaper hardware. The downside, the **fans** are coming up quickly, something I am not used to anymore :) I still use a lot of Electron apps (browser, Claude in browser, Obsidian) and other heavy apps such as Google Meet in browser, YouTube.


### My macOS Workflow


I recorded my macOS workflow (*before*) as of now to document it before I potentially switch to Arch Linux with Omarchy. Let’s see ð


However, I also showcase that most of my setup on macOS is very similar to the shortcut-driven Linux setup shown in Omarchy - workflow *after* (now):


### Life with Arch Linux (Omarchy)


Today I’m almost up with the same tools as before, there are still some to be changed, but that’s expected after 15 years on the same OS. This write-up is the start of showing that. I will soon create another video on Omarchy, and add to this post too.


Before I went full in, I quickly tested it on an old (10-20 years) laptop and installed an early version of Omarchy. It is a beauty. Before, Windows was unusable and with Arch in the back, it runs almost like a brand-new laptop. Obviously when you start heavy apps, you will notice too, but the navigation and simple tasks are instant; you don’t feel that you are on an old machine.

[

](https://www.ssp.sh/blog/macbook-to-arch-linux-omarchy/omarchy-old-dell.webp)

Installed on an old laptop. Amazed how blazingly fast it is. And beautuful. I can finally say it, Arch BTW  [Twitter](https://x.com/sspaeti/status/1942502383923134464)


## Choosing the Hardware


Obviously, I needed new hardware. First I was romanticizing with the [Beelink](https://www.bee-link.com/) fanless desktops, super fast and affordable. But as I do my best writing on the go in coffee shops, libraries or on the couch, I needed a laptop.


DHH has a great list that I included in [Notebook & Desktops for Linux](https://ssp.sh/brain/notebook-desktops-for-linux/). And as [Framework Laptops](https://frame.work/) are not available in Switzerland, I went with an affordable Lenovo ThinkBook. 32 GB and good-looking device with a great keyboard. I didn’t know how good a laptop keyboard can be with some travel; almost can’t write on the MacBook keyboard anymore, even though I didn’t get the bad scissor one.


But the CPU is not the fastest, and I didn’t do heavy loads yet. And I can already sense if I run a couple of Electron apps that the CPU can go quite high. Like Obsidian, browser and Spotify, these are already three. And if I open webapps as separate windows, these are essentially more tabs or Electron apps.


But yeah, I got to have a matte screen that also works nice outside, and after all, the screen is not the most important thing to me. Also the speaker and trackpad and everything else on the MacBook was just superior, but it doesn’t bother me as much yet. Only the battery life is a big shift back, and the constant fan. Obviously, if I stay for it longer, I might also buy a beefier laptop, I actually didn’t know if I will stay or not. So far, everything is pointing to that I will stay on Linux for the time being. Also nice to see the constant [new updates](https://github.com/basecamp/omarchy/releases/) that Omarchy is producing. A breath of fresh air to be honest.


## I Learned Sooooo much (and Had Fun)


The great thing, although I spent quite some time, I learned so much. It’s so fun. As a lover of a good [TUI](https://ssp.sh/brain/tuis/), I really enjoyed every bit of it.


Even switching your WiFi, just a TUI away:

[

](https://www.ssp.sh/blog/macbook-to-arch-linux-omarchy/wifi-tui.webp)

[Impala: A TUI for managing wifi on Linux](https://github.com/pythops/impala)


It’s also fun to set up your OS in a way that makes you more productive, or gives you joy just by the looks of it. Aesthetics and quick transitions between each keypress or transition are amazing.


## What’s Next?


It’s only 2-3 weeks in total that I run it full time. So there’s many things I want to improve and I will over time. But I’m amazed how much is already working, and that it’s such a blast to use.


I’ll update you on the journey for sure. If you don’t want to miss it it, [subscribe](https://subscribe.ssp.sh) to my newsletter. I write a lot about tech, productivity, Obsidian, Markdown, Neovim and data engineering. Or follow me on [GitHub](https://gh.ssp.sh) or check out my [dotfiles.ssp.sh](https://dotfiles.ssp.sh).

Can you use a MacBook to set up Omarchy?

Instead of buying a new machine as I did, you can also directly install it on a MacBook. If it’s an older Intel-based model, there should be no problem, and everything should work as expected. If it’s one with an Apple Silicon chip, you can follow [this write-up](https://github.com/basecamp/omarchy/discussions/155). There’s also [Asahi Linux](https://asahilinux.org/), an Arch Distro made for Apple Silicon.


I didn’t do it (yet), as not everything might work, and more tinkering is needed, as Apple is a closed-source system, and every effort is based on reverse engineering. But many made it work successfully, so if you are in for a ride, try it, and share your learning in the above discussion thread on GitHub.

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/macbook-to-arch-linux-omarchy/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Linux](https://www.ssp.sh/tags/linux/)
[Macbook](https://www.ssp.sh/tags/macbook/)
[Arch](https://www.ssp.sh/tags/arch/)
[Omarchy](https://www.ssp.sh/tags/omarchy/)
[Thinkbook](https://www.ssp.sh/tags/thinkbook/)
[Workflow](https://www.ssp.sh/tags/workflow/)
[Hyprland](https://www.ssp.sh/tags/hyprland/)
