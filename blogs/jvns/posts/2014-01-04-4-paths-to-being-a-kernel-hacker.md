---
title: "4 paths to being a kernel hacker"
date: 2014-01-04
url: https://jvns.ca/blog/2014/01/04/4-paths-to-being-a-kernel-hacker/
slug: 4-paths-to-being-a-kernel-hacker
word_count: 1002
---


(this is me continuing work on my [CUSEC](http://2014.cusec.net/) talk
about why the kernel isn’t scary)


I once tried asking for advice about how to get started with kernel
programming, and was basically told:

1. If you don’t *need* to understand the kernel for your work, why
would you try?
2. You should subscribe to the
[Linux kernel mailing list](https://lkml.org/) and just try really
hard to understand.
3. If you’re not writing code that’s meant to be in the main Linux
kernel, you’re wasting your time.


This was really, really, really not helpful to me. So here are a few
possible strategies for learning about how operating systems and the
Linux kernel work on your own terms, while having fun. I still only
know a few things, but I know more than I did before :)


For most of these paths, you’ll need to understand some C, and a bit
of assembly (at least enough to copy and paste). I’d written a few
small C programs, and took a course in assembly that I’d almost
entirely forgotten.


### Path 1: Write your own OS


This might seem to be a pretty frightening path. But actually it’s
not! I started with
[rustboot](https://github.com/charliesome/rustboot), which, crucially,
*already worked and did things*. Then I could do simple things like
making the screen *blue* instead of red, printing characters to the
screen, and move on to trying to get keyboard interrupts to work.


[MikeOS](http://mikeos.berlios.de/write-your-own-os.html) also looks
like another fun thing to start with. Remember that your operating
system doesn’t have to be big and professional – if you make it turn
the screen purple instead of red and then maybe make it print it a
limerick, you’ve already won.


You’ll definitely want to use an emulator like
[qemu](http://wiki.qemu.org/Main_Page) to run your OS in. The
[OSDev wiki](http://wiki.osdev.org/Main_Page) is also a useful
place – they have FAQs for a lot of the problems you’ll run into
along the way.


### Path 2: Write some kernel modules!


If you’re already running Linux, writing a kernel module that doesn’t
do anything is pretty easy.


Here’s
[the source for a module](https://github.com/jvns/kernel-module-fun/blob/master/hello.c)
that prints “Hello, hacker school!” to the kernel log. It’s 18 lines
of code. Basically you just register an init and a cleanup function
and you’re done. I don’t really understand what the `__init` AND
`__exit` macros do, but I can use them!


Writing a kernel module that does do something is harder. I did this
by deciding on a Thing to do (for example, print a message for every
packet that comes through the kernel), and then read
some [Kernel Newbies](http://kernelnewbies.org/), googled a lot, and
copied and pasted a lot of code to figure out how to do it. There are
a couple of examples of kernel modules I wrote in this
[kernel-module-fun](https://github.com/jvns/kernel-module-fun)
repository.


### Path 3: Do a Linux kernel internship!


The Linux kernel participates in the
[GNOME Outreach Program for Women](https://wiki.gnome.org/OutreachProgramForWomen).
This is amazing and fantastic and delightful. What it means is that if
you’re a woman and want to spend 3 months working on the kernel, you
can get involved in kernel development without any prior experience,
and get paid a bit ($5000). Here’s
[the Kernel Newbies page explaining how it works](http://kernelnewbies.org/OPWIntro).


It’s worth applying if you’re at all interested – you get to format a
patch for the kernel and it’s fun.
[Sage Sharp](http://sage.thesharps.us/), a Linux kernel developer,
coordinates this program and she is pretty inspiring. You should read
their
[blog post about how 137 patches got accepted into the kernel during the first round](http://sage.thesharps.us/2013/05/23/%EF%BB%BF%EF%BB%BFopw-update/).
These patches could be yours! Look at the
[application instructions](http://kernelnewbies.org/OPWApply)!


If you’re not a woman, Google Summer of Code is similar.


### Path 4: Read some kernel code


This sounds like terrible advice – “Want to understand how the kernel
works? Read the source, silly!”


But it’s actually kind of fun! You won’t understand everything. I felt
kind of dumb for not understanding things, but then every single
person I talked to was like “yeah, it’s the Linux kernel, of course!”.


My friend Dave recently pointed me to [LXR](http://lxr.linux.no/),
where you can read the kernel source and it provides lots of helpful
cross-referencing links. For example, if you wanted to understand the
`chmod` system call, you can go look at
[the chmod_common definition](http://lxr.linux.no/linux+v3.12.6/fs/open.c#L464)
in the Linux kernel! [livegrep.com](http://livegrep.com/search/linux)
is also really nice for this.


Here’s the source for `chmod_common`, with some comments from me:


```
static int chmod_common(struct path *path, umode_t mode)
{
    struct inode *inode = path->dentry->d_inode;
    struct iattr newattrs;
    int error;

    // No idea what this does
    error = mnt_want_write(path->mnt);
    if (error)
        return error;

    // Mutexes! Prevent race conditions! =D
    mutex_lock(&inode->i_mutex);

    // Check for permission to use chmod, I guess.
    error = security_path_chmod(path, mode);
    if (error)
        goto out_unlock;
    // I guess this changes the mode!
    newattrs.ia_mode = (mode & S_IALLUGO) | (inode->i_mode & ~S_IALLUGO);
    newattrs.ia_valid = ATTR_MODE | ATTR_CTIME;
    error = notify_change(path->dentry, &newattrs);
out_unlock:
    mutex_unlock(&inode->i_mutex); // We're done, so the mutex is over!
    mnt_drop_write(path->mnt); // ???
    return error;
}

```


I find this is a fun time and helps demystify the kernel for me. Most
of the code I read I find pretty opaque, but some of it (like this
chmod code) is a little bit understandable.


To summarize a few links:

- [Jessica McKellar](http://web.mit.edu/jesstess/www/)’s blog posts on
the [Ksplice blog](https://blogs.oracle.com/ksplice/)
- [Linux Device Drivers](http://lwn.net/Kernel/LDD3/) describes itself
like this. I’ve found it somewhat useful.

“This book teaches you how to write your own drivers and how to hack around in related parts of the kernel.”
- The [OSDev wiki](http://wiki.osdev.org/Main_Page) is great if you’re
writing an OS.
- [Kernel Newbies](http://kernelnewbies.org/) has some resources for
starting kernel developers. I didn’t have good experiences in the
IRC channel, though.
- [Sage Sharp](http://sage.thesharps.us/) is a kernel developer and
runs the Linux kernel outreach and is amazing.
- [Valerie Aurora’s posts on LWN.net](https://encrypted.google.com/#q=site:lwn.net+%22this+article+was+contributed+by+valerie%22)


I’d also love to hear from you. If you’d done kernel work, how did you
get started with kernel hacking? If you haven’t, which of these paths
sounds most approachable to you?
