---
title: "Spying on a Ruby process's memory allocations with eBPF"
date: 2018-01-31
url: https://jvns.ca/blog/2018/01/31/spying-on-a-ruby-process-s-memory-allocations/
slug: spying-on-a-ruby-process-s-memory-allocations
word_count: 1465
---


Today instead of working on CPU profilers, I took the day to experiment with a totally new idea!


My idea at the beginning of the day was – what if you could take an arbitrary Ruby process’s PID
(that was already running!) and start tracking its memory allocations?


Spoiler: I got something working! Here’s an [asciinema demo](https://asciinema.org/a/SaY5BJHpllausq0ujwTLpu8um) of what happened.  Basically this shows a
live-updating cumulative view of rubocop’s memory allocations over 15 seconds, counted by class. You can see
that Rubocop allocated a few thousand `Array`s and `String`s and `Range`s, some `Enumerator`s, etc.


This demo works without making any code changes to `rubocop` at all – I just ran `bundle exec rubocop` to start it. All the code for this is in [https://github.com/jvns/ruby-mem-watcher-demo](https://github.com/jvns/ruby-mem-watcher-demo)
(though it’s extremely experimental and likely only works on my machine right now).


### how it works part 1: eBPF + uprobes


The way this works fundamentally is relatively simple. On Linux ~4.4+, you have this feature called
“uprobes” which let you attach code that you write to an arbitrary userspace function. You can do
this from outside the process – you ask the kernel to modify the function while the program is
running and run your code every time the function gets called.


You can’t ask the kernel to run just **any** code, though (at least not with eBPF) – you ask it to
run “eBPF bytecode” which is basically C code where you’re restricted in what memory you can access.
And it can’t have loops.


So the idea is that I’d run a tiny bit of code every time a new Ruby object was created in
`rubocop`, and then that code would count memory allocations per class.


This is the function I wanted to instrument (add a uprobe to): `newobj_slowpath`.


```
static inline VALUE
newobj_slowpath(VALUE klass, VALUE flags, VALUE v1, VALUE v2, VALUE v3, rb_objspace_t *objspace, int wb_protected)

```


The goal was to
grab the first argument to that function (`klass`) and count how many allocations there were for
each `klass`.


### writing my first bcc program


bcc (the “BPF compiler collection”) at [https://github.com/iovisor/bcc](https://github.com/iovisor/bcc) is a toolkit to help you

- write BPF programs in C
- compile those BPF programs into BPF bytecode
- insert the compiled BPF bytecode into the kernel
- Write *Python* programs to communicate with the BPF bytecode that’s running in the kernel and
display the information from that bytecode in a useful way


It’s a lot to digest. Luckily the
[documentation](https://github.com/iovisor/bcc/blob/master/docs/reference_guide.md) is pretty good
and there are a LOT of example programs to copy from in the repo.


[Here’s the initial BPF program I wrote in a gist](https://gist.github.com/jvns/b81991a29a2a595a197709ed47055a2c). It’s pretty short (just 40 lines!) and has a C part and a Python part.


I’ll explain it a bit because I think it’s not that obvious what it does and it’s really
interesting!


First, here’s the C part – the idea is that this code will run every time `newobj_slowpath` runs.
This code:

- declares a BPF hash (which is basically a data structure I can use to store data and send data
back to userspace where the Python frontend can read it)
- defines a `count` function which reads the first argument of the function (with `PT_REGS_PARM1`)
and basically does `counts[klass] += 1`


```
BPF_HASH(counts, size_t);
int count(struct pt_regs *ctx) {
    u64 zero = 0, *val;
    size_t klass = PT_REGS_PARM1(ctx);
    val = counts.lookup_or_init(&klass, &zero);
    (*val)++;
    return 0;
};

```


Next, here’s the Python part. This is just a while loop that every second reads `counts` (the same BPF hash
before, but magically accessible from Python somehow!!), prints out what’s in there, and then clears
it..


```
counts = b.get_table("counts")

while True:
    sleep(1)
    os.system('clear')
    print("%20s | %s" % ("CLASS POINTER", "COUNT"))
    print("%20s | %s" % ("", ""))
    top = list(reversed(sorted([(counts.get(key).value, key.value) for key in counts.keys()])))
    top = top[:10]
    for (count, ptr) in top:
        print("%20s | %s" % (ptr, count))
    counts.clear()

```


Here’s the outcome of this 42-line program: a cool live updating view showing us how many of each
class was allocated! So awesome.


### how do you get the **name** of a class though?


So far this was relatively easy. Having the address of a class is not that useful though – it
doesn’t mean anything to me that there were 49 instances of `94477659822920` allocated.


So I wanted to get the name of each class! Very helpfully, there’s a `rb_class2name` function in Ruby that does this – it takes a class pointer and returns a `char *` (string) with the name.


But I wasn’t inside the Ruby process, so I couldn’t exactly call the function. OR COULD I?! Calling
the function **did** seem way easier than trying to reverse engineer all the Ruby internals :)


Our goals:

1. call the `rb_class2name` function
2. don’t disturb the process we’re profiling at all (certainly don’t call any functions in it!)


I ended up writing a separate Rust program to map pointers into class names.


### mapping the ruby process’s memory into my memory


My (terrible/delightful) plan for calling `rb_class2name` was basically – copy all the memory maps
from the target process into my profiler process, and then just call `rb_class2name` and hope it
works.


Then any memory my target process has, I have too!! And so I can just call functions from that
process as if they were functions in my process.


Here is the relevant code snippet for copying the memory maps. The [copy_map function is defined here](https://github.com/jvns/ruby-mem-watcher-demo/blob/c3f8e2929d718cf1a158926609d38bcbacd05de2/src/main.rs#L109-L129)


Basically I could copy all the memory maps except the ones called “syscall” and “vvar” which I
couldn’t copy. Not sure what those are but I don’t think I needed them.


```
for map in maps {
    if map.flags == "rw-p" {
        copy_map(&map, &source, PROT_READ | PROT_WRITE).unwrap();
    }
    if map.flags == "r--p" {
        copy_map(&map, &source, PROT_READ | PROT_WRITE).unwrap();
    }
    if map.flags == "r-xp" {
        copy_map(&map, &source, PROT_READ | PROT_WRITE | PROT_EXEC).unwrap();
    }
}

```


### calling `rb_class2name`


Calling rb_class2name is pretty easy – I just needed to find the address of `rb_class2name` (which
I already know how to do from `rbspy`), cast that address to the right kind of function pointer
(`extern "C" fn (u64) -> u64`), and then call the resulting function!


Of course all of this (copying the memory maps, casting essentially a random address into a function
pointer, calling the resulting function) is unsafe in Rust, but I can still do it!


When I finally got this to work at like 9pm today I was so delighted.


### segfaults


I kept running into segfaults when trying to translate class pointers into names. Instead of
debugging this (I just wanted to get a demo to work!!) I decided to just figure out how to ignore
the segfaults because it wasn’t **always** segfaulting, just sometimes.


here is what I did (this is silly, but it was fun)

1. before doing the thing that causes the segfault, fork
2. in the child process, try to do the potentially segfaulting thing and print out the answer
3. if the child process segfaults, ignore it and keep going


this worked great.


### how the Rust program and the Python program work together


the way the final demo works is:

1. the Python program is in charge of getting class pointers  + counting how many times each of them
has been allocated (with uprobes + BPF)
2. the Rust program is in charge of mapping class pointers to class names – you call it with a PID and a
list of class pointers as command arguments, and it prints out the mappings to stdout


This is of course all a hacky mess but it worked and I got it to work in 1 day which made me super
happy! I think it should be possible to do this all in Rust – as long as I can compile and save
the appropriate BPF program, I should be able to call the right system calls from Rust to insert
that compiled BPF program into the kernel without using bcc. I think.


### design principle: magic


The main design principle I’m using right now is – how can I build tools that just feel really
magical? (they should also hopefully be useful, of course :)). But I think that eBPF enables a lot
of really awesome things and I want to figure out how to show that to people!


I feel like this idea of streaming you live updates about what memory your Ruby process is
allocating (without having to make any changes in your Ruby program beforehand) feels really magical
and cool. There’s still a lot of work to do to make it useful and it’s not clear how stable I can
make it, but I am delighted by this demo!


questions/comments? [here’s the twitter thread for this post!](https://twitter.com/b0rk/status/958916696424763394)
