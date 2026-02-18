---
title: "I think I found a Mac kernel bug?"
date: 2018-01-28
url: https://jvns.ca/blog/2018/01/28/mac-freeze/
slug: mac-freeze
word_count: 629
---


I’ve been working on Mac support for [rbspy](https://github.com/rbspy/rbspy), and I accidentally
found something that looks like a Mac kernel bug!  Basically I managed to write a very short (17
line) C program that reliably causes `ps` to stop working. Without allocating any memory or anything
like that!


This seems to be a kernel bug on High Sierra, but not Sierra – someone [tried to reproduce on Sierra](https://twitter.com/capileigh/status/957709200385191936) and couldn’t. So looks like it’s a new bug.


### mysterious freezes on mac


This past week I’ve been building Mac support for rbspy (my Ruby profiler). I put a Mac support
branch on github yesterday. Some amazing early adopters tried out the branch and reported that it
froze their computer (Activity Monitor stopped working, they couldn’t open new terminals, etc). This
was extremely surprising – how could that happen?!? There’s a very detailed report at
[https://github.com/rbspy/rbspy/issues/70](https://github.com/rbspy/rbspy/issues/70).


I was really mystified by this – how could a program *not running as root* freeze someone’s
computer? Somebody suggested that maybe the program was allocating a lot of
memory, but I didn’t **think** it was. And it turns out that memory allocations weren’t the problem.


### A 17-line C program that freezes (parts of) my Mac


@parkr was incredibly helpful and managed to narrow down the problem to right before calling the
`task_for_pid` Mach function. Since `task_for_pid` seemed to be the issue, I worked on reproducing
the issue in a small C program.


Here’s the program that shows the bug. It runs in a loop because it’s a bit race-y and sometimes it
needs to try 10 times before it’ll freeze.


```
#include <mach/mach_init.h>
#include <mach/port.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    for (;;) {
        pid_t pid = fork();
        if (pid == 0) execv("/usr/bin/true", NULL); 
        mach_port_name_t task = MACH_PORT_NULL;
        task_for_pid(mach_task_self(), pid, &task);
        printf("Ran task_for_pid\n");
        int wait_status;
        wait(&wait_status);
    }
}

```


Here’s the behaviour I see:

- Run `./freeze-mac`. (the example program, above) It hangs.
- Run `ps` in another tab. ps hangs, and doesn’t display any output. also trying to `Ctrl+C` to stop `ps` doesn’t work.


This happens on the Mac I’ve been developing on (running High Sierra, 10.13.2).


The core issue seems to be – if I `exec` a new program (like `/usr/bin/true`), and then immediately
run `task_for_pid` on that program, then the process I ran `task_for_pid` from will hang and `ps`
will stop working (though I can terminate it with Ctrl+C and then things seem to go back to
normal).


If you want to try it out on your Mac, you can run the program yourself! (at your own risk – for me
it freezes some things but everything goes back to normal if I press ctrl+c, I don’t know what will
happen if you run it :) )


```
wget https://gist.githubusercontent.com/jvns/16c1ea69352a81658d6d8e9c5a289f2a/raw/ea11fa0a16bfcd4fd019666b790c6c8fe624f9f0/freeze-mac.c
cc -o freeze-mac freeze-mac.c
./freeze-mac
# try running `ps` / starting Activity Monitor, they don't work!

```


### this bug is affecting htop too


Somebody on twitter pointed me to [this github issue on htop for mac](https://github.com/hishamhm/htop/issues/682)  where people are reporting that `htop` sometimes
sporadically freezes their computer in the same way (terminals don’t start, Activity Monitor doesn’t
work). [In the
comments](https://github.com/hishamhm/htop/issues/682#issuecomment-355759162) @grrrrrrrrr says this
is a race condition in `task_for_pid` and they have what looks to be a POC that’s similar to what I
have here.


### I have a workaround!


This is weird and I don’t really understand the underlying kernel issue. Anyway, I have a workaround
for this – don’t run `task_for_pid` on processes immediately after exec’ing them, instead sleep for
a few milliseconds first. So hopefully with this new knowledge I can get rbspy to work on Mac
without freezing any users’ computers.


Systems programming is weird and exciting though!


if you have thoughts or questions, here’s the [twitter thread for this post](https://twitter.com/b0rk/status/957498366606368768)
