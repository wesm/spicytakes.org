---
title: "Day 27: Automatically testing changes in state! Visualizing my Git workflow! Floats!"
date: 2013-11-13
url: https://jvns.ca/blog/2013/11/13/day-27-magic-testing-functions/
slug: day-27-magic-testing-functions
word_count: 635
---


##Testing state changes! (overriding `__setattr__`)


This morning I worked with [Allison](http://akaptur.github.io/), one of the HS
facilitators. I have previously mentioned that Allison is amazing – she’s
working on this super fun Python bytecode interpreter
called [byterun](https://github.com/nedbat/byterun) that
I [blogged about a few weeks ago](http://jvns.ca/blog/2013/10/14/day-9-bytecode-is-made-of-bytes/).


Today we worked a bit on testing this TCP client that I’m writing. As a
connection happens, the client goes through a series of internal states
(`"CLOSED"`, `"SYN-SENT"`, `"ESTABLISHED"`, etc.), and I wanted to check
that it was going through the right states.


Allison had the amazing idea of subclassing my socket class to log every
time I set the `state` attribute. Here’s what that looks like:


```
from tcp import TCPSocket

class LoggingTCPSocket(TCPSocket):
    def __init__(self, listener, verbose=0):
        self.received_packets = []
        self.states = []
        super(self.__class__, self).__init__(listener, verbose)

    def handle(self, packet):
        self.received_packets.append(packet)
        super(self.__class__, self).handle(packet)

    def __setattr__(self, attr, value):
        if attr == 'state':
            self.states.append(value)
        super(self.__class__, self).__setattr__(attr, value)

```


So we override `__setattr__` to log the value every time we change
`self.state`. This also made me want to learn Python 3 – apparently this
`super()` business is much nicer is Python 3.


This means I can then write a test saying


```
assert conn.states == ["CLOSED", "SYN-SENT", "ESTABLISHED", "LAST-ACK", "CLOSED"]

```


Which is super nice. <3


I also talked with Mary about redesigning the `handle()` function I complained
about yesterday, but I still haven’t had the courage to change it again. It
will happen!


##Floats!


In the afternoon, there was a fantastic lecture by [Stefan Karpinski](http://karpinski.org/) about
floats. The key thing I learned there is that there are a finite amount of
64-bit floats (2^64 of them!). Which is obvious in retrospect, but I hadn’t
thought about it before.


And there are always 2^52 floats between 2^n and 2^(n+1). Which is super nice!
In particular, this means that the floats between 2^52 and 2^53 are the same as
the integers between 2^52 and 2^53.


We talked about gradual underflow and epsilons and rounding and it was
fantastic. knowledge++.


##Visualizing Git workflows


I talked to [Philip Guo](http://pgbovine.net/), the resident for this week, for
a while. We played with the idea of taking people’s history files and using them
to

- teach novices (so they can see what an expert workflow looks like)
- help tool authors (so they can see how people are actually using their tools)
- help me understand how I am using a tool
- let me see how Wes McKinney uses pandas (celebrity history files! :D)


We talked in particular about looking at

- Git workflows (because there are tons of options)
- command line options in general for complex commands ([http://explainshell.com/](http://explainshell.com/) is great, but it doesn’t tell you which options you *should* be using)
- IPython magics
- IPython histories more generally, since they’re all stored.


I find it really interesting how I learn about command line tools largely
through social interactions and folklore, and rarely by reading documentation
or man pages.


A great example of a novice-teaching session
is [this part of my history file](https://gist.github.com/jvns/7460709), from
when I was pairing with Jari who understands tools like netstat and tcpdump. I
don’t necessarily remember what all the options do, but since I have that
history I can refer back to it and read up on `-a`, `-n`, `-u`, and `-p`, which
is much more manageable than reading the `netstat` man page.


After we talked, I put together a graph of which Git commands I transition to
from other commands. The thickness of the arrow indicates how many times I move
from one command to another. There isn’t really enough data to make conclusions
from this, but it’s neat.


You can [look at the notebook](http://nbviewer.ipython.org/7460616) and try it
out yourself. Here’s the picture!


![](https://jvns.ca/images/git-workflow.png)


##Takeaway


I need to talk to more people. I learn more when I talk to more people.
