---
title: "Login Delays and Damaged Font Caches on Mac OS X 10.3"
date: 2005-03-21
url: https://daringfireball.net/2005/03/font_caches
slug: font_caches
word_count: 1277
---


At some point a few weeks ago, I noticed my iBook had developed a
problem: whenever I logged in, I’d get the SPOD 1 cursor,
spinning on an empty desktop, for about 90 seconds. Only after that
would my login proceed: menu bar, Dock, Finder, login items
launching. Other than this delay at login, however, nothing else
seemed awry.


In fact, the first few times this happened I wasn’t sure if anything
at all was out of the ordinary. I often go many days without logging
out, and when I do, it’s typically because my virtual memory swap
files have grown large enough that a log-out/log-in cycle seems
called for. I thought perhaps the SPOD was being shown while the
system cleaned up my old swap files, or performed some other
housecleaning-type periodic task.


I realized something was definitely wrong, however, when I
determined that this delay occurred every time I logged in. A few
days ago, I tried rebooting, logging in, and then immediately
logging out and back in again. Even then, I had to suffer through
the delay.


Something, obviously, was wrong. But what?


It wasn’t an errant login item (a.k.a. the “startup items” specified
in the Accounts panel in System Preferences) — the delay occurred
even if I suppressed them by logging in while holding down the Shift
key.


Googling for “slow login mac os x”, “login delay mac os x”, “login
spod mac os x”, and so forth turned up nothing that seemed
applicable.


A corrupt preference file, perhaps? I made an archive of my regular
Preferences folder (in the Library folder in my user’s home
account), threw out my old Preferences folder, then logged out and
back in, letting the system create a factory-fresh set of
preferences. No help — the login delay was still there.


Enough guessing. I went to another machine, and connected to my
iBook via ssh using Terminal. Logging in remotely via ssh is enabled
using the Remote Access checkbox in the Sharing panel in System
Preferences. In Terminal, from another Mac on your local network,
type:


```
ssh [email protected]

```


(For me, this was `ssh [email protected]`.)


Now I could use *top*, a command-line program analogous to Activity
Monitor. It lists all the processes running on the machine, and
provides information such as how much memory and processor time
they’re using.


I went back to my iBook, logged out, and logged back in. The SPOD
appeared, and I went back to the other Mac (the one where I was
connected via ssh to my iBook) to see what top showed. Something was
going on while the SPOD was spinning, and I wanted to know what. Under
ordinary use, it’s convenient and natural to think of Mac OS X as
“the system”. But on the inside, in terms of how things really work,
there’s no such thing. As a Unix-y operating system, the Mac OS X
“system” is really a bunch of small processes that work together,
each of them doing their own little thing. So what I was looking for
in top was a process using a lot of CPU while my iBook was doing its
SPOD-for-90-seconds-on-login thing.


And, bingo: ATSServer was getting most of the CPU cycles that
weren’t being consumed by top itself.


Luckily, I knew what the “ATS” in “ATSServer” stands for: [Apple
Type Services](http://developer.apple.com/documentation/Carbon/Reference/ATS/index.html). According to this [chart of Mac OS X’s system
servers and daemons](http://developer.apple.com/documentation/MacOSX/Conceptual/BPSystemStartup/Concepts/BootProcess.html#//apple_ref/doc/uid/20002130/CJBCFIFI), ATSServer is the “Apple Type Solution
server, enabling system-wide font management.” 2


So some sort of font problem was the root cause. I hadn’t added any
new fonts recently, so my guess was that it wasn’t one or more
damaged fonts, but rather damaged font caches. A bit of Googling
turned up [this PDF](http://images.apple.com/pro/pdf/L303878B_Font_TT_v4.pdf) document from Apple, “Advanced Typography
With Mac OS X”, which Google conveniently offered to [display as
HTML](http://66.102.7.104/search?q=cache:sLX629uKqnIJ:images.apple.com/pro/pdf/L303878B_Font_TT_v4.pdf++fontTablesAnnex+site:apple.com&hl=en). From this document:


> Deleting font caches
> If your fonts are garbled, or if there are fonts that won’t empty
> from the Trash even after you restart your Mac, try deleting the
> Mac OS X font caches.
> You can do this manually by finding and removing these files:
> In /System/Library/Caches:
> fontTablesAnnex 
> com.apple.ATS.System.fcache
> com.apple.ATSServer.FODB_System
> In /Library/Caches:
> com.apple.ATS
> In your home directory’s Library/Preferences folder:
> com.apple.ATS.plist


In my case, the problem was solved by trashing
`/System/Library/Caches/fontTablesAnnex`. None of these cache files
are essential, however, so I deleted them all. (The
“com.apple.ATS.plist” prefs file, on the other hand, tracks, among
other things, the disabled fonts you’ve specified using Font Book.
I left this in place.)


I restarted — not just logged out, but restarted — immediately
after trashing these files. Logging in to my account now took only a
few seconds. 3


However, I remain unconvinced that this has actually solved the
problem. My problematic “fontTablesAnnex” file was over 64 MB; upon
restarting and logging in, my newly-rebuilt “fontTablesAnnex” file
was only 1 MB. However, each time I logged in, it seemed to grow by
another 400 KB, and at other times it seemed to grow significantly
while I’m logged in.


Within two days, it had grown to 32 MB — although admittedly,
during that time I’d been logging out and in repeatedly, as well
as poking about my fonts — and logging in to my account again
became slow. I deleted “fontTablesAnnex” a second time, and normal
log-in performance has been restored (again). If anyone has any
suggestions as to what may be causing this, let me know.


## Interesting Question


This strikes me as a troubleshooting session that most Mac users
never could have managed. Most have never even heard of top or ssh,
let alone would have known how to use them to see what was going on
while the SPOD was displayed. But trickier still is this: what could
I have done if I didn’t have a second computer from which to ssh
into my iBook?


**Update:** [Kevin Ballard](http://kevin.sb.org/) and [Everett Howe](http://www.alumni.caltech.edu/~however/) (love that username)
both wrote to point out that fast user switching allows you to
monitor your login with top without using a second computer.
Everett writes:


> Here’s a possible solution:  Create a second user account on your
> iBook.  Enable fast user switching.  Log out of your main account,
> and log in to the new account.  Open a terminal, and run
> `top -l 120 -n 5 -o cpu
> `
> The “`-l`” will make top print its output to the terminal (instead
> of its usual behavior of writing over the same part of the terminal
> each time it updates).  In particular, “`-l 120`” will make it print
> its output for 120 iterations before stopping; since the default
> delay between sampling the processes is 1 second, this will give you
> two minutes of data.  The “`-o cpu`” will make it sort output by CPU
> usage. The “`-n 5`” will limit the output to the top five processes.
> While top is running, use fast user switching to log in to your
> usual account.  After your unusually long startup, switch back
> to the new account and see what the top output looks like.


---

1. Spinning pizza of death.↩︎
2. So, technically, I was wrong about what the “S” in “ATS” stood for, but I was right that it was a system component pertaining to fonts.↩︎
3. Those of you who religiously delete font caches every
time you install a system or security update, feel free to smirk smugly.↩︎



| **Previous:** | [On the Discovery Ruling in ‘Apple v. Does’](https://daringfireball.net/2005/03/discovery_ruling) |
| **Next:** | [Font Caches Gone Wild](https://daringfireball.net/2005/03/font_caches_gone_wild) |


PreviousNext