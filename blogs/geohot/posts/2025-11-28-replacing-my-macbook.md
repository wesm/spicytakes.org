---
title: "Replacing my MacBook"
date: 2025-11-28
url: https://geohot.github.io/blog/jekyll/update/2025/11/28/replacing-my-macbook.html
slug: replacing-my-macbook
word_count: 765
---

I’ve been trying to replace my MacBook. I switched from an iPhone to a Z Fold 5 (and now a Z Fold 7) which has gone well 2 years in, so I’ve been trying to do the same with my laptop.

For phones, this was easier because the Samsung hardware is already better. Sadly, there’s no better laptop hardware than a MacBook, and while  [Asahi Linux](https://asahilinux.org/)  is cool, it doesn’t work on the M3. Even on the M1, it’s missing the ability to plug an external USB-C monitor in, a key feature I use every day! Without support from Apple, I don’t see this being a viable long term solution, mostly because of Apple’s use of custom little MCUs to do everything.

I bought a  [HP ZBook Strix Halo](https://www.hp.com/us-en/workstations/zbook-ultra.html)  and a Framework 16. I’ve been daily using the HP, the Framework gets here hopefully this week and maybe I’ll stream it when I get it.

I’ve been running  [Omarchy](https://omarchy.org/)  which I have been quite happy with. It fixed the problem I always had with Arch, which is how customizable it is. It’s a great OS (why isn’t apt-get multithreaded yet?), leave the customizability there, but pick some good defaults with taste.

The main issue I have with Linux laptops is power management.

I got idle lid-closed power down to 0.2W with the help of AMD’s awesome  [amd_s2idle](https://gitlab.freedesktop.org/drm/amd/-/blob/master/scripts/amd_s2idle.py)  script. This is similar to a MacBook, and is 15 days in a bag.

Lid-open power has been more of a challenge. I  [wrote a script](https://github.com/geohot/ztop)  to poll the best sensors I could find as fast as I could. I got CPU draw from the SMU and battery draw from the bytes of whatever it is the EC is. Embedded Controller? I couldn’t get the ACPI battery draw to update faster than every 30 seconds, but the EC has it every second in its bytes. Btw, LLMs are super helpful at reverse engineering – it’s almost becoming fun again.

After tuning, at screen-on idle, the whole laptop draws 7W, and when browsing the web more like 10W. That’s only 7 hours of life, which is 30% of a MacBook, and still not really acceptable.

4W of those 7W are the CPU.  [Strix Halo](https://chipsandcheese.com/p/amds-chiplet-apu-an-overview-of-strix)  is the only laptop chip that rivals the Apple M-Series, actually having decent cores (the AVX-512 is real too) and good RAM bandwidth. Sadly it’s chiplets, which the LLMs tell me are very power hungry.

I tried to further power limit the CPU with  [RyzenAdj](https://github.com/FlyGoat/RyzenAdj) , but I couldn’t even get it to 3W with a stated limit of 2W. I wonder if there’s some other ways to do it, what more can I turn off? The main fix for s2idle was turning off the webcam, what else is on and wasting my CPU (well, really APU) power?

AMD, want to release docs about the power draw of Strix Halo? You could probably figure out a lot through experiments too, but then I have to, like, disable the GPU over ssh and then I have to get another laptop and that all sounds like a lot of work. I’m  [already busy](https://github.com/tinygrad/tinygrad/blob/master/extra/sqtt/attempt_sqtt_parse.py)  trying to build an open source  [rocprof-trace-decoder](https://github.com/ROCm/rocprof-trace-decoder) .

Also, package Strix Halo with MoP like Apple. it’s the best thing about PoP (low power) without the worst thing about PoP (bad thermals). That picture is Intel Lunar Lake, and you know MoP is a good idea  [because Intel is discontinuing it](https://www.guru3d.com/story/intel-future-processors-to-discontinue-mop-packagelevel-memory-integration-from-lunar-lake-series/)  while Apple  [keeps doing it](https://wccftech.com/m4-mac-mini-teardown-shows-thermal-solution-ssd-more/) .

For the other 3W, this is on HP. The OLED screen is about a watt, which is really good. Don’t turn on the stupid keyboard backlight that draws 2 watts!

The memory is probably about a watt too, you can’t really turn it off to measure. I couldn’t find a way to lower the clocks either.

That leaves 1 watt of possibility. The WiFi and NVMe are both extremely low power. Any other ideas?

I bet there’s something stupid or poorly designed, HP should release a schematic of the laptop. In fact, you don’t need to release a full schematic, just a block diagram.  [Framework releases these](https://github.com/FrameworkComputer/Framework-Laptop-16/blob/main/Mainboard/Mainboard_Interfaces_Schematic_Framework_Laptop_16_Ryzen_AI_300_Series.pdf)  and just showing what parts are used and how they are connected is 80% of what you want.

If the CPU could be brought down to 2W (Apple M3 Max is 1W!) and the laptop brought down to 2W, with a 99.6 Wh battery that’s 25 hours. If someone makes one of these in a nice 16” form factor, OLED screen, aluminium unibody, no stupid branding everywhere, I think it might be time for a lot of developers to switch.
