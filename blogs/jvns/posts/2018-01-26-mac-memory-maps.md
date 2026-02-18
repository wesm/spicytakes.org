---
title: "How do you read the memory maps of a Mac process?"
date: 2018-01-26
url: https://jvns.ca/blog/2018/01/26/mac-memory-maps/
slug: mac-memory-maps
word_count: 1201
---


Hello! For the last few days I’ve been trying to figure out how to get the memory maps of a Mac
program!


### why do I need memory maps?


To do profiling, I need the address of 2 variables: `ruby_version` (so I know how the structs will
be laid out) and `ruby_current_thread` so I can get stack traces.


Getting the addresses of those 2 variables is not thaat hard – often they’re in the symbol table of
the Ruby binary I’m looking at. But because of ASLR (“address space layout randomization”), the
binary is loaded into memory at a random place. So I need to:

- find the address of `ruby_version` in the symbol table
- find out where the Ruby binary is loaded in memory (from the process’s memory maps!)
- add them together! (also subtract the value of the `__mh_execute_header` symbol)


On Linux, you get memory maps by looking at the `/proc/PID/maps` file, and they look like this –
you have an address range, permissions (eg `r-xp`), a size, an inode number, and possibly a filename
of the file that’s mapped there.


```
00400000-00401000 r-xp 00000000 00:14 13644        /usr/bin/ruby1.9.1
00600000-00601000 r--p 00000000 00:14 13644        /usr/bin/ruby1.9.1
00601000-00602000 rw-p 00001000 00:14 13644        /usr/bin/ruby1.9.1
0060b000-00887000 rw-p 00000000 00:00 0              [heap]
7f1d44648000-7f1d4464a000 r-xp 00000000 00:14 14411  /usr/lib/ruby/1.9.1/x86_64-linux/enc/trans/transdb.so
7f1d4464a000-7f1d4484a000 ---p 00002000 00:14 14411  /usr/lib/ruby/1.9.1/x86_64-linux/enc/trans/transdb.so
7f1d4484a000-7f1d4484b000 r--p 00002000 00:14 14411  /usr/lib/ruby/1.9.1/x86_64-linux/enc/trans/transdb.so
7f1d4484b000-7f1d4484c000 rw-p 00003000 00:14 14411  /usr/lib/ruby/1.9.1/x86_64-linux/enc/trans/transdb.so

```


On Mac the memory maps have basically the same structure, but getting them is quite a bit harder!
Trying to do this on Mac gave me a lot of appreciation for Linux’s “everything is a text file in
/proc” philosophy – it feels a little janky sometimes to be parsing a text file, but getting the
memory maps on Linux took me like 2 hours and I was done, and trying to figure it out on Mac has
taken me like 3 days and I’m still not finished.


### attempt 1: vmmap


My first attempt at this was to use a binary called `vmmap` ([man page](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/vmmap.1.html)) which will print a process’s memory
maps! `vmmap --wide PID` got me all the memory maps I wanted. Neat!


However – vmmap is **super slow** for some reason. It takes 2 seconds to get the memory maps fora
process! I read somewhere (though I can’t find the reference now) that this is because vmmap pauses
the process before taking its memory maps.


I can’t find the source to verify *why* vmmap is so slow (if you know where the source for the vmmap
binary is, let me know!! It’s not on [https://opensource.apple.com/](https://opensource.apple.com/) as far as I can tell) .


I’m not happy with vmmap being slow for 2 reasons:

1. a 2-second delay is annoying for the user
2. (more importantly) if vmmap really is pausing the process, that’s not good – I’d really prefer
that my profiling tool not interfere with the process it’s profiling at all.


So I don’t want to use vmmap.


### attempt 2: reimplement vmmap myself in Rust


Okay, so I don’t want to use the `vmmap` tool. Next step: Reimplement its functionality (or at least
the part I need) in Rust!


With the help of [this C example code of a vmmap clone](http://www.newosxbook.com/src.jl?tree=listings&file=12-1-vmmap.c), I wrote a partial sketchy vmmap clone in
Rust! The code is here: [main.rs](https://gist.githubusercontent.com/jvns/6ecc2e1db154ca5ecf1ad0c354d8d5d9/raw/36f3c223c484f3f4668f5a0602c50f3412bc0895/main.rs).


To do this I used the [mach crate](https://docs.rs/mach), which has Rust bindings for a bunch of Mac
kernel functions you can call. I also learned that on Macs / BSD there’s this concept of a “port”:


> a “port” is a protected message queue for communication between tasks; tasks own send rights and
> receive rights to each port


Here’s how I get a single memory map from a program! The interface to this function is a little
weird – you give it a port ID and an address, and it gives you the first memory map **after** that
address. Basically this function just wraps the `mach_vm_region` function from the Mach microkernel.
(the headers for all the Mach functions are in `/usr/include/mach/*.h`)


I’ve commented the code a bit. It uses the [https://github.com/andrewdavidmackenzie/libproc-rs](https://github.com/andrewdavidmackenzie/libproc-rs) crate
for the `regionfilename` function (which gives you the filename of the library associated with the
memory map). I had to use the version of that crate on github master because the released
version had a use-after-free bug.


```
fn mach_vm_region(target_task: mach_port_name_t, mut address: mach_vm_address_t) -> Option<Region> {
    let mut count = mem::size_of::<vm_region_basic_info_data_64_t>() as mach_msg_type_number_t;
    let mut object_name: mach_port_t = 0;
    // we need to create new `size` and `info` structs for the function we call to read the data
    // into
    let mut size = unsafe { mem::zeroed::<mach_vm_size_t>() };
    let mut info = unsafe { mem::zeroed::<vm_region_basic_info_data_t>() };
    let result = unsafe {
        // Call the underlying Mach function
        mach::vm::mach_vm_region(
            target_task as vm_task_entry_t,
            &mut address,
            &mut size,
            VM_REGION_BASIC_INFO,
            &mut info as *mut vm_region_basic_info_data_t as vm_region_info_t,
            &mut count,
            &mut object_name,
        )
    };
    if result != KERN_SUCCESS {
        return None;
    }
    // this uses 
    let filename = match regionfilename(41000, address) {
        Ok(x) => Some(x),
        _ => None,
    };
    Some(Region {
        size: size,
        info: info,
        address: address,
        count: count,
        filename: filename,
    })
}

```


It made me happy that I could write a reasonable first approximation of a vmmap clone in 100ish
lines of Rust!


### my Rust program: way faster than vmmap!


My Rust program did what I hoped – it runs in like 80ms or something, about 15x faster than vmmap.
I still don’t know exactly what vmmap is **doing** that’s slow (dtruss didn’t tell me anything
terribly helpful), but whatever it is, my Rust program isn’t doing that thing.


There’s still a major issue with my Rust vmmap clone – it actually only gives me some of the
memory maps from my process right now. For any dynamically linked libraries (including a Ruby
library, which I need the address and filename of!!) they’re stored in a place called the “dyld
shared cache” or something which I still haven’t understood and don’t know how to read from yet.


There’s a bunch of code about this “dyld” thing in the links below that I’m planning to read – I
think I should be able to get it to work!


### Useful resources for reading memory maps from a Mac process


Here are the 4 most useful resources I’ve found so far about reading memory maps on Mac:

- [this vmmap.c source](http://www.newosxbook.com/src.jl?tree=listings&file=12-1-vmmap.c) from an OS
X internals book
- [“Playing with Mach-O binaries and dyld”, on finding the address of shared libraries in a Mac process](https://blog.lse.epita.fr/articles/82-playing-with-mach-os-and-dyld.html)
- [dynamic_images.cc, from Chromium, that reads information shared libraries in a Mac process](https://chromium.googlesource.com/breakpad/breakpad/+/master/src/client/mac/handler/dynamic_images.cc). The `ReadImageInfo` function here is relevant to me I think.
- [the OS X C code for psutil](https://github.com/giampaolo/psutil/blob/master/psutil/_psutil_osx.c). psutil is a really
cool cross-platform Python library for reading information about processes! It’s what’s used to
implement [osquery](https://osquery.io/). So its source is helpful for learning about Mac internals.


### that’s all for now!


Figuring out how to support Macs in rbspy over the last few days has been interesting! I’ve never
done any Mac or BSD systems programming before, and I’m still trying to understand basic concepts
like “what is a port?” but I feel like I’m making good progress :D
