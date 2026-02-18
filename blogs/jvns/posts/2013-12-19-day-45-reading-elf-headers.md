---
title: "Day 45: I now have Rust code for executing executables!"
date: 2013-12-19
url: https://jvns.ca/blog/2013/12/19/day-45-reading-elf-headers/
slug: day-45-reading-elf-headers
word_count: 516
---


So I’m working on writing a kernel in Rust, and I wanted to be able to
run executables because THAT WOULD BE COOL. Now I have the beginnings
of this working!


I posted about my confusion about how to run programs
[a few days ago](http://jvns.ca/blog/2013/12/13/day-42-how-to-run-an-elf-executable-i-dont-know/).
Then [Graydon Hoare](https://twitter.com/graydon_moz) sent me a super
helpful email answering all my questions, and gave me an example
minimal program to use (better than “Hello world”). The best. One of
my favourite things about this blog is when delightful people comment
or email and answer my questions


This is really useful because my statically compiled Hello World
program takes up 800k, which is huge. The example program Graydon sent
me is 897 bytes compiled, so about 1000 times smaller!


You can compile it like this:


```
$ cat >static.c
int _start() {
  asm(
      "mov $127,%ebx\n" /* exit code        */
      "mov $1,%eax\n"   /* syscall #1, exit */
      "int $0x80\n"     /* invoke syscall   */
      );
}
^D

$ cc -m32 -static -nostdlib static.c
$ ./a.out
$ echo $?
127

```


This is super great, because it means that I can understand the whole
program and it doesn’t have a bunch of glibc/Linux stuff compiled into
it. The only OS-specific thing here is the `int 80` interrupt, which
I’ll need to implement. I could also make up my own convention for
system calls, but that seems unnecessary.


So what I need to do is

1. Implement the `exit()` system call
2. Read the ELF header
3. Read the segment headers
4. Find out
  1. what address the program needs to start at
  2. how many bytes the main section is
  3. The address of the program’s entry point
5. Copy the segment marked LOAD into memory at the right address
6. Jump to the start of the program!


This is what the code I have so far looks like. You can see that it’s
mostly an ELF header definition, and then to read it I just cast the
pointer to the array I’m trying to read.


This is typical of a lot of Rust code I’m writing – I need to write a
lot of `unsafe` code.


```
pub fn read_header<'a>(file: &'a [u8]) -> &'a ELFHeader {
    unsafe {
        let x : *ELFHeader = to_ptr(file) as *ELFHeader;
        return &*x;
    }
}

#[packed]
struct ELFHeader {
    e_ident: ELFIdent,
    e_type: u16,
    e_machine: u16,
    e_version: u32,
    e_entry: u32,
    e_phoff: u32,
    e_shoff: u32,
    e_flags: u32,
    e_ehsize: u16,
    e_phentsize: u16,
    e_phnum: u16,
    e_shentsize: u16,
    e_shnum: u16,
    e_shstrndx: u16
}

```


and the final `exec` function will look a bit like this:


```
unsafe fn jmp(addr: u32) {
    asm!("jmp *($0)"
         :
         : "r" (addr));
}

// Executes a file starting at `addr`
pub unsafe fn exec(addr: uint) {
    let bytes: &[u8] = transmute(Slice {data: (addr as *u8), len: 100});
    let header = elf::read_header(bytes);
    assert(header.e_ident.ei_mag.slice(1,4) == "ELF");
    // Read the program header and load the program into memory at
    // the right address
    jmp(header.e_entry);
}

```


`jmp` is a great example of an unsafe Rust function – what could be
more unsafe than jumping to a possibly arbitrary address in memory?
