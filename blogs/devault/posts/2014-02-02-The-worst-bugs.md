---
title: "The bug that hides from breakpoints"
date: 2014-02-02
url: https://drewdevault.com/2014/02/02/The-worst-bugs.html
slug: The-worst-bugs
word_count: 1448
---

This is the story of the most difficult bug I ever had to solve. See if you can
figure it out before the conclusion.

### Background

For some years now, I’ve worked on a kernel for Texas
Instruments calculators called  [KnightOS](https://github.com/KnightOS/kernel) .
This kernel is written entirely in assembly, and targets the old-school z80
processor from back in 1976. This classic processor was built without any
concept of protection rings. It’s an 8-bit processor, with 150-some instructions
and (in this application) 32K of RAM and 32K of Flash. This stuff is so old, I
ended up writing most of the KnightOS toolchain from scratch rather than try to
get archaic assemblers and compilers running on modern systems.

When you’re working in an enviornment like this, there’s no seperation between
kernel and userland. All “userspace” programs run as root, and crashing the entire
system is a simple task. All the memory my kernel sets aside for the
process table, or memory ownership, file handles, stacks, any other executing
process - any program can modify this freely. Of course, we have to rely on the
userland to play nice, and it usually does. But when there are bugs, they can be a
real pain in the ass to hunt down.

### The elusive bug

The original bug report:  **When running the counting demo and switching between
applications, the thread list graphics become corrupted.**

I can reproduce this problem, so I settle into my development enviornment and I
set a breakpoint near the thread list’s graphical code. I fire up the emulator and
repeat the steps… but it doesn’t happen. This happened consistently:  **the bug
was not reproduceable when a breakpoint was set** . Keep in mind, I’m running this
in a z80 emulator, so the enviornment is supposedly no different. There’s no
debugger attached here.

Though this is quite strange, I don’t immediately despair. I try instead setting a
“breakpoint” by dropping an infinite loop in the code, instead of a formal
breakpoint. I figure that I can halt the program flow manually and open the
debugger to inspect the problem. However, the bug wouldn’t be tamed quite so
easily. The bug was unreproducable when I had this psuedo-breakpoint in place,
too.

At this point, I started to get a little frustrated. How do I debug a problem that
disappears when you debug it? I decided to try and find out what caused it after
it had taken place, by setting the breakpoint to be hit only after the graphical
corruption happened. Here, I gained some ground. I was able to reproduce it, and
 *then*  halt the machine, and I could examine memory and such after the bug was
given a chance to have its way over the system.

I discovered the reason the graphics were being corrupted. The kernel kept the
length of the process table at a fixed address. The thread list, in order to draw
the list of active threads, looks to this value to determine how many threads it
should draw. Well, when the bug occured, the value was too high! The thread list
was drawing threads that did not exist, and the text rendering puked non-ASCII
characters all over the display. But why was that value being corrupted?

It was an oddly specific address to change. None of the surrounding memory was
touched. Making it even more odd was the very specific conditions this happened
under - only when the counting demo was running. I asked myself, “what makes the
counting demo unique?” It hit me after a moment of thought. The counting demo
existed to demonstrate non-supsendable threads. The kernel would stop executing
threads (or “suspend” them) when they lost focus, in an attempt to keep the
system’s very limited resources available. The counting demo was marked as
non-suspendable, a feature that had been implemented a few months prior. It
showed a number on the screen that counted up forever, and the idea was that you
could go give some other application focus, come back, and the number would have
been counting up while you were away. A background task, if you will.

A more accurate description of the bug emerged: “the length of the kernel process
table gets corrupted when launching the thread list when a non-suspendable thread
is running”. What followed was hours and hours of crawling through the hundreds of
lines of assembly between summoning the thread list, and actually seeing it. I’ll
spare you the details, because they are very boring. We’ll pick the story back up
at the point where I had isolated the area in which it occured: applib.

The KnightOS userland offered “applib”, a library of common functions applications
would need to get the general UX of the system. Among these was the function
 `applibGetKey` , which was a wrapper around the kernel’s  `getKey`  function. The
idea was that it would work the same way (return the last key pressed), but for
special keys, it would do the appropriate action for you. For example, if you
pressed the F5 key, it would suspend the current thread and launch the thread
list. This is the mechanism with which most applications transfer control out of
their own thread and into the thread list.

Eager that I had found the source of the issue, I placed a breakpoint nearby. That
same issue from before struck again - the bug vanished when the breakpoint was
set. I tried a more creative approach: instead of using a proper breakpoint, I
asked the emulator to halt whenever that address was written to. Even still - the
bug hid itself whenever this happened.

I decided to dive into the kernel’s getKey function. Here’s the start of the
function, as it appeared at the time:

```
getKey:
    call hasKeypadLock
    jr _
    xor a
    ret
_:  push bc
; ...
```

I started going through this code line-by-line, trying to see if there was
anything here that could concievably touch the thread table. I noticed a minor
error here, and corrected it without thinking:

```
getKey:
    call hasKeypadLock
    jr z, _
    xor a
    ret
_:  push bc
; ...
```

The simple error I had corrected: getKey was pressing forward, even when the
current thread didn’t have control of the keyboard hardware. This was a silly
error - only two characters were omitted.

A moment after I fixed that issue, the answer set in - this was the source of the
entire problem. Confirming it, I booted up the emulator with this change applied
and the bug was indeed resolved.

Can you guess what happened here? Here’s the other piece of the puzzle to help you
out, translated more or less into C for readability:

```
int applibGetKey() {
    int key = getKey();
    if (key == KEY_F5) {
        launch_threadlist();
        suspend_thread();
    }
    return key;
}
```

Two more details you might not have picked up on:

* applibGetKey is non-blocking
* suspend_thread suspends the current thread immediately, so it doesn’t return until the
thread resumes.

### The bug, uncovered

Here’s what actually happened. For most threads (the suspendable kind), that
thread stops processing when  `suspend_thread()`  is called. The usually
non-blocking applibGetKey function blocks until the thread is resumed in this
scenario. However, the counting demo was  *non-suspendable* . The suspend_thread
function has no effect, by design. So, suspend_thread did not block, and the
keypress was returned straight away. By this point, the thread list had launched
properly and it was given control of the keyboard.

However, the counting demo went back into its main loop, and started calling
applibGetKey again. Since the average user’s finger remained pressed against the
button for a few moments more, applibGetKey  *continued to launch the thread list,
over and over* . The thread list itself is a special thread, and it doesn’t
actually have a user-friendly name. It was designed to ignore itself when it drew
the active threads. However, it was  *not*  designed to ignore other instances of
itself, the reason being that there would never be two of them running at once.
When attempting to draw these other instances, the thread list started rendering
text that wasn’t there, causing the corruption.

This bug vanished whenever I set a breakpoint because it would halt the system’s
keyboard processing logic. I lifted my finger from the key before allowing it to
move on.

The solution was to make the kernel’s getKey function respect hardware locks by
fixing that simple, two-character typo. That way, the counting demo, which had no
right to know what keys were being pressed, would not know that they key was still
being pressed.

The debugging described by this blog post took approximately three weeks.

[Discussion on Hacker News](https://news.ycombinator.com/item?id=7688700)
