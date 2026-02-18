---
title: "How do you spy on a program running in a container?"
date: 2018-01-26
url: https://jvns.ca/blog/2018/01/26/spy-container/
slug: spy-container
word_count: 966
---


Yesterday I added Linux container support to rbspy, so that an instance of
rbspy running on the host machine can profile Ruby programs running in
containers.


This was a pretty simple thing (~50 lines of code,
[https://github.com/rbspy/rbspy/pull/68](https://github.com/rbspy/rbspy/pull/68) ), but I thought it would be fun to
explain what adding “container support” involves in practice!


### why didn’t rbspy work with containers before?


First – programs running in containers are just programs, like any other program! You can see them
by running `ps`. So all of the normal things rbspy does (like reading memory from a process) work
just fine with programs running in containers. There was just one small gotcha.


There’s a small part at the beginning of the program where it reads 1 or 2 binaries from the
program’s memory maps (the Ruby binary, and sometimes another dynamically linked library).


To make this concrete – right now I have a container on my computer running a Ruby program. Its pid
(in the host PID namespace) is 17474. Looking at its memory maps (with `sudo cat /proc/17474/maps`)
shows me that the Ruby binary it’s running is `/usr/bin/ruby1.9.1` and it has a ruby library loaded
called `/usr/lib/libruby-1.9.1.so.1.9.1`.


```
00400000-00401000 r-xp 00000000 00:14 13644                              /usr/bin/ruby1.9.1
00600000-00601000 r--p 00000000 00:14 13644                              /usr/bin/ruby1.9.1
00601000-00602000 rw-p 00001000 00:14 13644                              /usr/bin/ruby1.9.1
7f1d45981000-7f1d45b77000 r-xp 00000000 00:14 13648                      /usr/lib/libruby-1.9.1.so.1.9.1
7f1d45b77000-7f1d45d76000 ---p 001f6000 00:14 13648                      /usr/lib/libruby-1.9.1.so.1.9.1
7f1d45d76000-7f1d45d7b000 r--p 001f5000 00:14 13648                      /usr/lib/libruby-1.9.1.so.1.9.1
7f1d45d7b000-7f1d45d7f000 rw-p 001fa000 00:14 13648                      /usr/lib/libruby-1.9.1.so.1.9.1

```


I need the addresses both those binaries are mapped to in the process’s memory (easy! just look at
`/proc/17474/maps`, done) as well as their contents.


Getting their contents is where we run into a problem. `/usr/bin/ruby1.9.1` is not a file on my
host’s filesystem. I’m running Ubuntu 16.04, the container is running Ubuntu 14.04, they have
different system Ruby versions.


The precise issue here is that the target process (in the container) has a **different mount
namespace**  than rbspy.


### how to fix it: switch mount namespaces!


So to make rbspy work with containerized processes, we just need to switch to the target process’s
mount namespace before reading `/usr/bin/ruby1.9.1` and `/usr/lib/libruby-1.9.1.so.1.9.1`. Then after
reading those two files, switch back to the previous mount namespace right away so that we can write
output to the filesystem in the right place.


That’s pretty simple! Here’s some pseudocode:


```
setns(target process's namespace, "mount")
read(/usr/bin/ruby1.9.1)
read(/usr/lib/libruby-1.9.1.so.1.9.1)
setns(, "mount")

```


### what the actual code looks like


Switching mount namespaces is not that hard. To switch mount namespaces I just
needed to:

1. Open the file `/proc/$PID/ns/mnt`. Get the file descriptor of that file.
2. Call `libc::setns(fd, libc::CLONE_NEWNS)`. For some reason `CLONE_NEWNS` means “the mount namespace”.


really easy! 3 more things to note / be careful of:

- remember to open `/proc/self/ns/mnt` **before** switching mount namespaces, so I can have a file descriptor to use to switch back to the old mount namespace
- make sure I always switch back to the old mount namespace even if there’s an error when reading the files. I did this with `defer!`. (which is like Go’s `defer` keyword, the one I used comes a Rust crate called `scopeguard`)
- the ID of a process’s mount namespace is the inode number of `/proc/pid/ns/mnt`. I can use that inode number to figure out whether two processes are in the same mount namespace or not


Here’s a code snippet:


```
let other_proc_mnt = &format!("/proc/{}/ns/mnt", pid);
let self_proc_mnt = "/proc/self/ns/mnt";
// We need to get `/proc/$PID/maps` before switching namespaces
let all_maps = proc_maps(pid)?;
// read the inode number to check if the two mount namespaces are the same
if fs::metadata(other_proc_mnt)?.st_ino() == fs::metadata(self_proc_mnt)?.st_ino() {
    get_program_info_inner(pid, all_maps)
} else {
    // switch mount namespace and then switch back after getting the program info
    // We need to save the fd of the current mount namespace so we can switch back
    let new_ns = fs::File::open(other_proc_mnt)?;
    let old_ns = fs::File::open(self_proc_mnt)?;
    switch_ns(&new_ns)?;
    // if there's an error at any point, always switch back to the old namespace
    defer!({switch_ns(&old_ns);});
    let proginfo = get_program_info_inner(pid, all_maps);
    proginfo

```


### you can’t switch mount namespaces if you’re multithreaded


Originally I wanted to create a separate thread to do the namespace-switching
juggle. This isn’t possible though: the [setns man page](http://man7.org/linu/man-pages/man2/setns.2.html) set me straight.


> A process may not be reassociated with a new mount namespace if it is multithreaded.


The description of setns at the start of the man page says “setns - reassociate
thread with a namespace”. So I think you **can** change other kinds of
namespaces if you’re multithreaded (like I guess you can change the network
namespace of a single thread?). You just can’t change the mount namespace. Good
to know!


### and actually you don’t even need to switch mount namespaces!


After I posted this post, someone [very helpfully pointed out on Twitter](https://twitter.com/PaulColomiets/status/957293110215704576) that to read the file
`/usr/bin/ruby1.9.1` from a process’s mount namespace you can just read
`/proc/PID/root/usr/bin/ruby1.9.1`. That’s way easier than switching mount namespaces!


Here’s what [the /proc man page](http://man7.org/linux/man-pages/man5/proc.5.html) says about
`/proc/PID/root`:


> Note however that this file is not merely a symbolic link.  It provides the same view of the
> filesystem (including namespaces and the set of per-process mounts) as the process itself.


### that’s it!


I thought this was a nice example of how understanding the fundamentals of how
containers work (They use different Linux namespaces from your host processes,
and in this case this mount namespace is the relevant namespace, we don’t care
about the rest of the namespaces) helped us add container support really easily.


We didn’t need to care about Docker or anything like that – it’s irrelevant
what container runtime our containers are using, and we certainly don’t
interact with Docker at all. We just need to make a few simple system calls and
it works!


have questions/thoughts about this? [here’s a twitter thread!](https://twitter.com/b0rk/status/957291182924627968)
