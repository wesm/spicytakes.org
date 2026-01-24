---
title: "Our Virtual Machine Future"
date: 2006-01-16
url: https://blog.codinghorror.com/our-virtual-machine-future/
slug: our-virtual-machine-future
word_count: 552
---

Lately I’ve been spending more and more time inside virtual machines. Whenever I need to try out a new bit of software, whether it’s a small shell extension, or a giant product like Team System – I tear off a new VM first. I don’t want to junk up my primary install until I’m totally confident I know what that software does. It’s guilty until proven innocent.


In fact, I’ll go one step further. I think **all software will eventually be distributed as virtual machine images.** And why not? Consider the advantages:

- **It’s the ultimate security sandbox.** Too many scary vulnerabilities in crusty old IE6? You can’t stop clicking on [dancing bunnies](https://blog.codinghorror.com/the-dancing-bunnies-problem/)? Just run your OS session in a virtual machine. At the end of every session, you blow it away. No spyware or virus is virulent enough to escape a VM. If you want to log in again, you tear off a new VM and start fresh. It’s like formatting your hard drive every time you turn off your PC. And this doesn’t have to be done at the OS level to be beneficial, either; why not selectively launch apps in their own private VMs?
- **It makes software installation a no-brainer**. Forget installation or setup.exe; just boot a fully pre-configured VM that has the application locked, loaded, and primed. Now you’re up and running in seconds. That’s the ultimate out of box experience!
- **The operating system doesn’t matter.** Who cares if your app requires Linux or OS X to run if I can boot it in a pre-configured VM within a few seconds? This could be a huge industry sea change – albeit helped a lot by the way Apple has cemented x86 as the [industry standard CPU instruction set](https://blog.codinghorror.com/x86-uber-alles/) for the next millennium. But on the plus side, think of the vast number of applications you can choose from once you no longer have to worry about OS choice.
- **New CPUs will accelerate VMs.** Virtual machines are reasonably fast now. But Intel has their [“vanderpool” technology](https://web.archive.org/web/20060115045650/http://www.intel.com/technology/computing/vptech/) and AMD has an equivalent in “[pacifica](https://web.archive.org/web/20060117002223/http://enterprise.amd.com/Enterprise/serverVirtualization.aspx)”; both promise to radically speed up virtualization via dedicated hardware.
- **What else are we going to do with all this power?** Within a few years, quad-core chips will be available on the desktop and dual-core will be bog-standard on all new PCs. Terabyte hard drives? Check. 64-bit memory addressing and more than 4 gigabytes of RAM? Check. Outside of gaming, there’s a handful of legitimate uses for all that power. But to be truly pervasive on the desktop, virtual machines *need* all that power.


And virtual machine software keeps getting cheaper, too. [Parallels Workstation](https://web.archive.org/web/20060207065732/http://www.parallels.com/en/products/workstation/) is only $45, and VMWare offers their [free player](https://web.archive.org/web/20060118053023/http://www.vmware.com/products/player/) which runs both VMWare and Virtual PC images. [Virtual PC](https://web.archive.org/web/20060117035531/http://www.microsoft.com/windows/virtualpc/default.mspx) is effectively free for any developer with an MSDN subscription.


All we really lack, I suppose, is VM built into the operating system as a first-class citizen rather than a standalone application. But the solipsist operating system is surely coming:


> [*solipsism*](http://en.wikipedia.org/wiki/Solipsism)* (n): a theory holding that the self can know nothing but its own modifications and that the self is the only existent thing.*


Eventually, all applications will believe they’re the only applications in the world. And they’ll be right.

[virtual machines](https://blog.codinghorror.com/tag/virtual-machines/)
[software distribution](https://blog.codinghorror.com/tag/software-distribution/)
[security](https://blog.codinghorror.com/tag/security/)
[sandboxing](https://blog.codinghorror.com/tag/sandboxing/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
