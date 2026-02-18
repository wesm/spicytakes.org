---
title: "Redirecting stderr of a running process"
date: 2018-05-04
url: https://drewdevault.com/2018/05/04/Redirecitng-stderr-of-running-process.html
slug: Redirecitng-stderr-of-running-process
word_count: 312
---

During the KDE sprint in Berlin,  [Roman Gilg](http://www.subdiff.de/)  leaned
over to me and asked if I knew how to redirect the stderr of an already-running
process to a file. I Googled it and found underwhelming answers using strace and
trying to decipher the output by reading the write syscalls. Instead, I thought
a gdb based approach would work better, and after putting the pieces together
Roman insisted I wrote a blog post on the topic.

gdb, the GNU debugger, has two important features that make this possible:

* Attaching to running processes via  `gdb -p`
* Executing arbitrary code in the target process space

With this it’s actually quite straightforward. The process is the following:

1. Attach gdb to the running process
2. Run  `compile code -- dup2(open("/tmp/log", 65), 2)`

The magic 65 here is the value of  `O_CREAT | O_WRONLY`  on Linux, which is easily
found with a little program like this:

```
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char **argv) {
    printf("%d\n", O_CREAT | O_WRONLY);
    return 0;
}
```

2 is always the file descriptor assigned to stderr. What happens here is:

1. Via  [`open`](https://linux.die.net/man/3/open) , the file you want to redirect
to is created.
2. Via  [`dup2`](https://linux.die.net/man/3/dup2) , stderr is overwritten with
this new file.

The  `compile code`  gdb command will compile some arbitrary C code and run the
result in the target process, presumably by mapping some executable RAM and
loading it in, then jumping to the blob. Closing gdb (control+d) will continue
the process, and it should start writing out to the file you created.

There are lots of other cool (and hacky) things you can do with gdb. I once
disconnected someone from an internet radio by attaching gdb to nginx and
closing their file descriptor, for example. Thanks to Roman for giving me the
chance to write an interesting blog post on the subject!
