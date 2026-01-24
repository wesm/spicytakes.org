---
title: "Virtualization and Ring Negative One"
date: 2006-05-04
url: https://blog.codinghorror.com/virtualization-and-ring-negative-one/
slug: virtualization-and-ring-negative-one
word_count: 633
---

This article on AMD’s upcoming [CPU support for hardware virtualization](https://web.archive.org/web/20060513095051/http://www.devx.com/amd/Article/30186) has the best description of virtualization I’ve read to date:


> In a modern-day virtualization system, a thin layer of software, called the virtual machine manager or hypervisor (both terms are common) runs on the processor. The VMM creates a number of virtual machines, into which it loads a standard, unmodified operating system, such as Linux, Solaris, or Windows.
> Each virtual machine thinks it’s running on the bare metal, and has the computer entirely to itself. However, the VMM is constantly monitoring the execution of the virtual machines, interceding to redirect memory, storage and I/O requests to the specific allocated resources (think of paging, as an example), and emulating hardware interrupts that might let the software running within one virtual machine affect what’s happening in another virtual machine, or even compromise the stability of the VMM itself. This software emulation includes, by the way, rewriting instructions, substituting instructions, changing calling parameters – there’s a lot of stuff going on behind the scenes at the virtual machine manager level.


Evidently **the x86 architecture is not well suited to virtualization** because it doesn’t meet something called the [Popek and Goldeberg virtualization requirements](http://en.wikipedia.org/wiki/Popek_and_Goldberg_virtualization_requirements). There are a number of problematic x86 instructions that require software interception and translation, e.g. emulation:


> All modern operating systems expect that their kernel and driver code is running in [Ring 0] privileged mode, which of course is fine in a non-virtualized PC. **However, in a virtual machine, you don’t want that kernel and driver code, or the interrupt handlers, to really have full control over the hardware**; you need the VMM to be able to be able to transparently manage the system. But because both the VMM itself, and the virtualized guest operating system kernel and drivers are running in Ring 0 – in other words, they’re peers – the VMM has to do a lot of work to maintain control of the guest operating system. Thus, the emulation, and the performance hit that it represents.


How can we avoid this emulation penalty with hardware? **Enter the dramatic, mysterious Ring Negative One**:


> That’s where [hardware virtualization support] comes in. It comprises a set of instructions and architectural constructs that solve several of the thorniest problems in VMM software emulation of things like IO calls or interrupt handling. **In effect, they create a super privileged mode (sometimes referred to as “Ring -1”), which can only be used by the VMM.** Because virtual machines and guest operating systems and applications continue to use traditional privileged and user modes, the VMM now has unique abilities to control the execution of virtual machine code running in Ring 0 – without software emulation.


Intel is already shipping a number of CPUs that [support hardware virtualization](http://en.wikipedia.org/wiki/X86_virtualization#Hardware_support_in_x86_processors). Future versions may even allow you to **hot-swap CPUs and memory**:


> Intel is working on a version of “Vanderpool” code named “Silvervale” for Xeon and Itanium server platforms. “Silvervale” differs from “Vanderpool” in terms of mission critical requirements such as hot-plug options as well as ability to change memory modules or even microprocessors on the fly, without shutting down the server.


AMD will follow suit with CPUs that have virtualization support later this year.


I firmly believe that, in the not too distant future, we’ll always be running in a [virtual machine](https://blog.codinghorror.com/our-virtual-machine-future/). Hardware support for faster x86 virtualization is yet another important step in that direction.


Aside: I was going to title this post “Ring -1”, but when I searched for that term in Google, I belatedly realized I was being stymied by something I just wrote about: dashes are [treated as word separators](https://blog.codinghorror.com/of-spaces-underscores-and-dashes/). As far as I can tell, it’s impossible to search for the phrase “Ring -1” in Google.

[virtualization](https://blog.codinghorror.com/tag/virtualization/)
[hardware virtualization](https://blog.codinghorror.com/tag/hardware-virtualization/)
[hypervisor](https://blog.codinghorror.com/tag/hypervisor/)
[amd](https://blog.codinghorror.com/tag/amd/)
[cpu support](https://blog.codinghorror.com/tag/cpu-support/)
