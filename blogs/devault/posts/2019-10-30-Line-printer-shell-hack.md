---
title: "An old-school shell hack on a line printer"
date: 2019-10-30
url: https://drewdevault.com/2019/10/30/Line-printer-shell-hack.html
slug: Line-printer-shell-hack
word_count: 1120
---

It’s been too long since I last did a good hack, for no practical reason other
than great hack value. In my case, these  [often amount](https://drewdevault.com/2016/03/22/Integrating-a-VT220-into-my-life.html)  to a nostalgia
for an age of computing I wasn’t present for. In a recent bid to capture more of
this nostalgia, I recently picked up a dot matrix line printer, specifically the
Epson LX-350 printer. This one is nice because it has a USB port, so I don’t
have to break out my pile of serial cable hacks to get it talking to Linux 😁

This is the classic printer style, with infinite paper and a lovely noise during
printing. They are also fairly simple to operate - you can just write text
directly to  `/dev/lp`  (or  `/dev/usb/lp9`  in my case) and it’ll print it out.
Slightly more sophisticated instructions can be written to them with ANSI escape
sequences, just like a terminal. They can also be rigged up to CUPS, then you
can use something like  `man -t 5 scdoc`  to produce printouts like this:

Plugging the printer into Linux and writing out pages isn’t much for hack value,
however. What I really wanted to make was something resembling an old-school
TTY - teletypewriter. So I wrote some  [glue code in
Golang](https://git.sr.ht/~sircmpwn/lpsh) , and soon enough I had a shell:

The glue code I wrote for this is fairly straightforward. In the simplest form,
it spins up a pty (pseudo-terminal), runs  `/bin/sh`  in it, and writes the pty
output into the line printer device. For those unaware, a pseudo-terminal is the
key piece of software infrastructure for running interactive text applications.
Applications which want to do things like print colored text, move
the cursor around and draw a TUI, and so on, will open  `/dev/tty`  to open the
current TTY device. For most applications used today, this is a
“pseudo-terminal”, or pty, which is a terminal emulated in userspace - i.e. by
your terminal emulator. However, your terminal emulator is  *emulating*  a
terminal - the control sequences applications send to these are
backwards-compatible with 50 years of computing history.  Interfaces like these
are the namesake of the TTY.

Visual terminals came onto the scene later on, and in the classic computing
tradition, the old hands complained that it was less useful - you could no
longer write notes on your backlog, tear off a page and hand it to a colleague,
or  [white-out](https://en.wikipedia.org/wiki/Wite-Out)  mistakes. Early
 [visual terminals](https://en.wikipedia.org/wiki/Computer_terminal)  could also
be plugged directly into a line printer, and you could configure them to echo to
the printer or print out a screenfull of text at a time. A distinct advantage of
visual terminals is not having to deal with so much bloody paper, a problem that
I’ve become acutely familiar with in the past few days 1 .

Getting back to the glue code, I chose Golang because setting up a TTY is a bit
of a hassle in C, but in Golang it’s pretty straightforward. There is a serial
port and in theory I could have plugged it in and spawned a getty on the
resulting serial device - but (1) it’d be write-only, so not especially
interactive without  *hardware*  hacks, and (2) I didn’t feel like digging out my
serial cables. So:

```
import "git.sr.ht/~sircmpwn/pty" // fork of github.com/kr/pty

// ...
winsize := pty.Winsize{
  Cols: 160,
  Rows: 24,
}
cmd := exec.Command("/bin/sh")
cmd.Env = append(os.Environ(),
  "TERM=lp",
  fmt.Sprintf("COLUMNS=%d", 180))
tty, err := pty.StartWithSize(cmd, &winsize)
```

*P.S. We’re going to dive through the code in detail now. If you just want more
cool videos of this in action, skip to the bottom.*

I set the TERM environment variable to  `lp` , for line printer, which doesn’t
really exist but prevents most applications from trying anything too tricksy
with their escape codes. The  `tty`  variable here is an  `io.ReadWriter`  whose
output is sent to the printer and whose input is sourced from wherever, in my
case from the stdin of this process 2 .

For a little more quality-of-life, I looked up Epson’s proprietary ANSI escape
sequences and found out that you can tell the printer to feed back and forth in
216th" increments with the j and J escape sequences. The following code will
feed 2.5" out, then back in:

```
f.Write([]byte("\x1BJ\xD8\x1BJ\xD8\x1BJ\x6C"))
f.Write([]byte("\x1Bj\xD8\x1Bj\xD8\x1Bj\x6C"))
```

Which happens to be the perfect amount to move the last-written line up out of
the printer for the user to read, then back in to be written to some more. A
little bit of timing logic in a goroutine manages the transition between “spool
out so the user can read the output” and “spool in to write some more output”:

```
func lpmgr(in chan (interface{}), out chan ([]byte)) {
	// TODO: Runtime configurable option? Discover printers? dunno
	f, err := os.OpenFile("/dev/usb/lp9", os.O_RDWR, 0755)
	if err != nil {
		panic(err)
	}

	feed := false
	f.Write([]byte("\n\n\n\r"))

	timeout := 250 * time.Millisecond
	for {
		select {
		case <-in:
			// Increase the timeout after input
			timeout = 1 * time.Second
		case data := <-out:
			if feed {
				f.Write([]byte("\x1Bj\xD8\x1Bj\xD8\x1Bj\x6C"))
				feed = false
			}
			f.Write(lptl(data))
		case <-time.After(timeout):
			timeout = 200 * time.Millisecond
			if !feed {
				feed = true
				f.Write([]byte("\x1BJ\xD8\x1BJ\xD8\x1BJ\x6C"))
			}
		}
	}
}
```

`lptl`  is a work-in-progress thing which tweaks the outgoing data for some
quality-of-life changes, like changing backspace to ^H. Then, the main event
loop looks something like this:

```
inch := make(chan (interface{}))
outch := make(chan ([]byte))
go lpmgr(inch, outch)

inbuf := make([]byte, 4096)
go func() {
  for {
    n, err := os.Stdin.Read(inbuf)
    if err != nil {
      panic(err)
    }
    tty.Write(inbuf[:n])
    inch <- nil
  }
}()

outbuf := make([]byte, 4096)
for {
  n, err := tty.Read(outbuf)
  if err != nil {
    panic(err)
  }
  b := make([]byte, n)
  copy(b, outbuf[:n])
  outch <- b
}
```

The tty will echo characters written to it, so we just write to it from stdin
and increase the form feed timeout closer to the user’s input so that it’s not
constantly feeding in and out as you write. The resulting system is pretty
pleasant to use! I spent about hour working on improvements to it on a  [live
stream](https://live.drewdevault.com) . You can watch the system in action on the
archive here:

If you were a fly on the wall when Unix was written, it would have looked a lot
like this. And remember:  [ed is the standard text
editor](https://www.gnu.org/fun/jokes/ed-msg.html) .

?

1. Don’t worry, I recycled it all. ↩︎
2. In the future I want to make this use libinput or something, or eventually make a kernel module which lets you pair a USB keyboard with a line printer to make a TTY directly. Or maybe a little microcontroller which translates a USB keyboard into serial TX and forwards RX to the printer. Possibilities! ↩︎
