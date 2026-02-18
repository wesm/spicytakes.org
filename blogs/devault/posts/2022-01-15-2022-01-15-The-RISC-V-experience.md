---
title: "The RISC-V experience"
date: 2022-01-15
url: https://drewdevault.com/2022/01/15/2022-01-15-The-RISC-V-experience.html
slug: 2022-01-15-The-RISC-V-experience
word_count: 1741
---

I’m writing to you from a Sway session on Alpine Linux, which is to say from a
setup quite similar to the one I usually write blog posts on, save for one
important factor: a RISC-V CPU.

I’ll state upfront that what I’m using is not a very practical system. What I’m
going to describe is all of the impractical hacks and workarounds I have used to
build a “useful” RISC-V system on which I can mostly conduct my usual work. It
has been an interesting exercise, and it bodes well for the future of RISC-V,
but for all practical purposes the promise of RISC-V still lives in tomorrow,
not today.

In  [December of 2018](https://drewdevault.com/2018/12/20/Porting-Alpine-Linux-to-RISC-V.html) , I wrote an article about the process of bootstrapping
Alpine Linux for RISC-V on the HiFive Unleashed board. This board was
essentially a crappy SoC built around a RISC-V CPU: a microSD slot, GPIO pins,
an ethernet port, a little bit of RAM, and the CPU itself, in a custom
form-factor. 1  Today I’m writing this on the HiFive Unmatched, which
is a big step up: it’s a Mini-ITX form factor (that is, it fits in a
standardized PC case) with 16G of RAM, and the ethernet, microSD, and GPIO ports
are complemented with a very useful set of additional I/O via two M.2 slots, a
PCIe slot, and a USB 3 controller, plus an SPI flash chip. I have an NVMe drive
with my root filesystem on it and an AMD Radeon Pro WX 2100 GPU installed. In
form, it essentially functions like a standard PC workstation.

I have been gradually working on bringing this system up to the standards that I
expect from a useful PC, namely that it can run upstream Alpine Linux with
minimal fuss. This was not really possible on the previous SiFive hardware, but
I have got pretty close on this machine. I had to go to some lengths to get
u-Boot to provide a working UEFI environment, 2  and I had to patch grub as
well, but the result is that I can write a standard Alpine ISO to a USB stick,
then boot it and install Alpine onto an NVMe normally, which then boots itself
with UEFI with no further fiddling. I interact with it through three means: the
on-board UART via a micro-USB cable (necessary to interact with u-Boot, grub, or
the early Linux environment), or ethernet (once sshd is up), or with keyboard,
mouse, and displays connected to the GPU.

Another of the standards I expect is that everything runs with upstream free
software, perhaps with a few patches, but not from a downstream or proprietary
tree. I’m pleased to report that I am running an unpatched mainline Linux
5.15.13 build. I am running mainline u-Boot with one patch to correct the name
of a device tree node to match a change in Linux upstream. I have a patched grub
build, but the relevant patches have been proposed for grub upstream. I have a
spattering of patches applied to a small handful of userspace programs and
libraries, but all of them only call for one or two patches applied to the
upstream trees. Overall, this is quite good for something this bleeding edge
— my Pinephone build is worse.

I have enclosed the system in a mini-ITX case and set it down on top of my usual
x86_64 workstation, then moved a few of my peripherals and displays over to it
to use it as my workstation for the day. 3  I was able to
successfully set up almost all of my standard workstation loadout on it, with
some notable exceptions. Firefox is the most painful omission —
bootstrapping Rust is an utter nightmare 4  and no one has managed to
do it for Alpine Linux riscv64 yet (despite many attempts and lots of hours
wasted), so anything which depends on it does not work. librsvg is problematic
for the same reason; I had to patch a number of things to be configured without
it. For web browsing I am using  [visurf](https://sr.ht/~sircmpwn/visurf) , which is based on Netsurf, and which
works for many of the lightweight websites that I generally prefer to use, but
not for most others.  For instance, I was unable to address an issue that was
raised on GitLab today because I cannot render GitLab properly on this browser.
SourceHut mostly works, of course, but it’s not exactly pleasant — I still
haven’t found time to improve the SourceHut UI for NetSurf.

Complicating things is the fact that my ordinary workstation uses two 4K
displays. For example, my terminal emulator of choice is  [foot](https://codeberg.org/dnkl/foot) , but it uses CPU
rendering and the 4K window is noticeably sluggish. Alacritty, which renders on
the GPU, would probably fare better — but Rust spoils this again. I
settled for  [st](https://st.suckless.org/) , which has acceptable performance (perhaps in no small part
thanks to being upscaled from 1080p on this setup). visurf also renders on the
CPU and is annoyingly slow; as a workaround I have taken to resizing the window
to be much smaller while actively navigating and then scaling it back up to full
size to read the final page.

CPU-bound programs can be a struggle. However, this system has a consumer
workstation GPU plugged into its PCIe slot. Any time I can get the GPU to pick
up the slack, it works surprisingly effectively. For example, I watched Dune
(2021) today in 4K on this machine — buttery smooth, stunningly beautiful
4K playback — a feat that my Pinebook Pro couldn’t dream of. The GPU has a
hardware HEVC decoder, and mpv and Sway can use dmabufs such that the GPU
decodes and displays each frame without it ever having to touch the CPU, and
meanwhile the NVMe is fast enough to feed it data at a suitable bandwidth. A
carefully configured obs-studio is also able to record my 4K display at 30 FPS
and encode it on the GPU with VAAPI with no lag, something that I can’t even do
on-CPU on x86_64 very reliably. The board does not provide onboard audio, but
being an audiophile I have a USB DAC available that works just fine.

I was able to play Armagetron Advanced at 120+ FPS in 4K, but that’s not exactly
a demanding game. I also played SuperTuxKart, a more demanding game, at 1080p
with all of the settings maxed out at a stable 30 FPS. I cannot test any
commercial games, since I’m reasonably certain that there are no proprietary
games that distribute a riscv64 build for Linux. If Ethan Lee is reading this,
please get in touch so that we can work together on testing out a Celeste build.

My ordinary workday needs are mostly met on this system. For communication, my
mail setup with aerc and postfix works just fine, and my normal Weechat setup
works great for IRC. 5  Much like any other day, I reviewed a few patches
and spent some time working on a shell I’ve been writing in our new programming
language. The new language is quite performant, so no issues there. I think if I
had to work on SourceHut today, it might be less pleasant to work with Python
and Go, or to work on the web UI without a performant web browser. Naturally,
browsing Geminispace with gmnlm works great.

So, where does this leave us? I have unusually conservative demands of my
computers. Even on high-end, top-of-the-line systems, I run a very lightweight
environment, and that’s the way I like it. Even so, my modest demands stress the
limits of this machine. If I relied more on a web browser, or on more GUI
applications, or used a heavier desktop environment, or heavier programming
environments, I would not be able to be productive on this system. Tomorrow, I
expect to return to my x86_64 machine as my daily workstation and continue to
use this machine as I have before, for RISC-V development and testing over
serial and SSH. There are few use-cases for which this hardware, given its
limitations, is adequate.

Even so, this is a very interesting system. The ability to incorporate more
powerful components like DDR4 RAM, PCIe GPUs, NVMe storage, and so on, can make
up for the slow CPU in many applications. Though many use-cases for this system
must be explained under strict caveats, one use-case it certainly offers is a
remarkably useful system with which to advance the development of the RISC-V
FOSS ecosystem. I’m using it to work on Alpine Linux, on kernel hacking
projects, compiler development, and more, on a CPU that is designed in adherence
to an open ISA standard and runs on open source firmware. This is a fascinating
product that promises great things for the future of RISC-V as a platform.

1. Plus an expansion slot which was ultimately entirely useless. ↩︎
2. I have u-Boot installed on a microSD card which the firmware boots to,
which then runs grub, which runs Linux. I could theoretically install u-Boot
to the SPI Flash and then I would not have to use a microSD card for this
process, but my initial attempts were not met with success and I didn’t debug
it any further. I think other people have managed to get it working, though,
and someone is working on making Alpine handle this for you. In future
hardware from SiFive I hope that they will install a working u-Boot UEFI
environment on the SPI before shipping so that you can just install standard
ISOs from a flash drive like you would with any other PC. ↩︎
3. I use this machine fairly often for RISC-V testing, particularly
for the new programming language I’m working on, but I usually just SSH into
it instead of connecting my displays and peripherals to it directly. ↩︎
4. Incidentally, my new language can be fully bootstrapped on this
machine in 272 seconds, including building and running the test suite. For
comparison, it takes about 10 seconds on my x86_64 workstation. Building LLVM
on this machine, let alone Rust, takes upwards of 12+ hours. You can
cross-compile it, but this is difficult and it still takes *ages*, and it’s so
complicated and brittle that you’re going to waste a huge amount of time
troubleshooting between every attempt. ↩︎
5. There’s not a snowball’s chance in hell of using Discord or Slack on this system, for the record. ↩︎
