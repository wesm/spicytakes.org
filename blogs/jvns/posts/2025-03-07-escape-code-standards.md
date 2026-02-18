---
title: "Standards for ANSI escape codes"
date: 2025-03-07
url: https://jvns.ca/blog/2025/03/07/escape-code-standards/
slug: escape-code-standards
word_count: 1724
---


Hello! Today I want to talk about ANSI escape codes.


For a long time I was vaguely aware of ANSI escape codes (“that’s how you make
text red in the terminal and stuff”) but I had no real understanding of where they were
supposed to be defined or whether or not there were standards for them. I just
had a kind of vague “there be dragons” feeling around them. While learning
about the terminal this year, I’ve learned that:

1. ANSI escape codes are responsible for a lot of usability improvements
in the terminal (did you know there’s a way to copy to your system clipboard
when SSHed into a remote machine?? It’s an escape code called [OSC 52](https://jvns.ca/til/vim-osc52/)!)
2. They aren’t completely standardized, and because of that they don’t always
work reliably. And because they’re also invisible, it’s extremely
frustrating to troubleshoot escape code issues.


So I wanted to put together a list for myself of some standards that exist
around escape codes, because I want to know if they *have* to feel unreliable
and frustrating, or if there’s a future where we could all rely on them with
more confidence.

- what’s an escape code?
- ECMA-48
- xterm control sequences
- terminfo
- should programs use terminfo?
- is there a “single common set” of escape codes?
- some reasons to use terminfo
- some more documents/standards
- why I think this is interesting


### what’s an escape code?


Have you ever pressed the left arrow key in your terminal and seen `^[[D`?
That’s an escape code! It’s called an “escape code” because the first character
is the “escape” character, which is usually written as `ESC`, `\x1b`, `\E`,
`\033`, or `^[`.


Escape codes are how your terminal emulator communicates various kinds of
information (colours, mouse movement, etc) with programs running in the
terminal. There are two kind of escape codes:

1. **input codes** which your terminal emulator sends for keypresses or mouse
movements that don’t fit into Unicode. For example “left arrow key” is
`ESC[D`, “Ctrl+left arrow” might be `ESC[1;5D`, and clicking the mouse might
be something like `ESC[M :3`.
2. **output codes** which programs can print out to colour text, move the
cursor around, clear the screen, hide the cursor, copy text to the
clipboard, enable mouse reporting, set the window title, etc.


Now let’s talk about standards!


### ECMA-48


The first standard I found relating to escape codes was
[ECMA-48](https://ecma-international.org/wp-content/uploads/ECMA-48_5th_edition_june_1991.pdf),
which was originally published in 1976.


ECMA-48 does two things:

1. Define some general *formats* for escape codes (like “CSI” codes, which are
`ESC[` + something and “OSC” codes, which are `ESC]` + something)
2. Define some specific escape codes, like how “move the cursor to the left” is
`ESC[D`, or “turn text red” is  `ESC[31m`. In the spec, the “cursor left”
one is called `CURSOR LEFT` and the one for changing colours is called
`SELECT GRAPHIC RENDITION`.


The formats are extensible, so there’s room for others to define more escape
codes in the future. Lots of escape codes that are popular today aren’t defined
in ECMA-48: for example it’s pretty common for terminal applications (like vim,
htop, or tmux) to support using the mouse, but ECMA-48 doesn’t define escape
codes for the mouse.


### xterm control sequences


There are a bunch of escape codes that aren’t defined in ECMA-48, for example:

- enabling mouse reporting (where did you click in your terminal?)
- bracketed paste (did you paste that text or type it in?)
- OSC 52 (which terminal applications can use to copy text to your system clipboard)


I believe (correct me if I’m wrong!) that these and some others came from
xterm, are documented in [XTerm Control Sequences](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html), and have
been widely implemented by other terminal emulators.


This list of “what xterm supports” is not a standard exactly, but xterm is
extremely influential and so it seems like an important document.


### terminfo


In the 80s (and to some extent today, but my understanding is that it was MUCH
more dramatic in the 80s) there was a huge amount of variation in what escape
codes terminals actually supported.


To deal with this, there’s a database of escape codes for various terminals
called “terminfo”.


It looks like the standard for terminfo is called [X/Open Curses](https://publications.opengroup.org/c243-1), though you need to create
an account to view that standard for some reason. It defines the database format as well
as a C library interface (“curses”) for accessing the database.


For example you can run this bash snippet to see every possible escape code for
“clear screen” for all of the different terminals your system knows about:


```
for term in $(toe -a | awk '{print $1}')
do
  echo $term
  infocmp -1 -T "$term" 2>/dev/null | grep 'clear=' | sed 's/clear=//g;s/,//g'
done

```


On my system (and probably every system I’ve ever used?), the terminfo database is managed by ncurses.


### should programs use terminfo?


I think it’s interesting that there are two main approaches that applications
take to handling ANSI escape codes:

1. Use the terminfo database to figure out which escape codes to use, depending
on what’s in the `TERM` environment variable. Fish does this, for example.
2. Identify a “single common set” of escape codes which works in “enough”
terminal emulators and just hardcode those.


Some examples of programs/libraries that take approach #2 (“don’t use terminfo”) include:

- [kakoune](https://github.com/mawww/kakoune/commit/c12699d2e9c2806d6ed184032078d0b84a3370bb)
- [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit/blob/165258d2f3ae594b50f16c7b50ffb06627476269/src/prompt_toolkit/input/ansi_escape_sequences.py#L5-L8)
- [linenoise](https://github.com/antirez/linenoise)
- [libvaxis](https://github.com/rockorager/libvaxis)
- [chalk](https://github.com/chalk/chalk)


I got curious about why folks might be moving away from terminfo and I found
this very interesting and extremely detailed
[rant about terminfo from one of the fish maintainers](https://twoot.site/@bean/113056942625234032), which argues that:


> [the terminfo authors] have done a lot of work that, at the time, was
> extremely important and helpful. My point is that it no longer is.


I’m not going to do it justice so I’m not going to summarize it, I think it’s
worth reading.


### is there a “single common set” of escape codes?


I was just talking about the idea that you can use a “common set” of escape
codes that will work for most people. But what is that set? Is there any agreement?


I really do not know the answer to this at all, but from doing some reading it
seems like it’s some combination of:

- The codes that the VT100 supported (though some aren’t relevant on modern terminals)
- what’s in ECMA-48 (which I think also has some things that are no longer relevant)
- What xterm supports (though I’d guess that not everything in there is actually widely supported enough)


and maybe ultimately “identify the terminal emulators you think your users are
going to use most frequently and test in those”, the same way web developers do
when deciding which CSS features are okay to use


I don’t think there are any resources like [Can I use…?](https://caniuse.com/) or
[Baseline](https://web-platform-dx.github.io/web-features/) for the terminal
though. (in theory terminfo is supposed to be the “caniuse” for the terminal
but it seems like it often takes 10+ years to add new terminal features when
people invent them which makes it very limited)


### some reasons to use terminfo


I also asked on Mastodon why people found terminfo valuable in 2025 and got a
few reasons that made sense to me:

- some people expect to be able to use the `TERM` environment variable to
control how programs behave (for example with `TERM=dumb`), and there’s
no standard for how that should work in a post-terminfo world
- even though there’s *less* variation between terminal emulators than
there was in the 80s, there’s far from zero variation: there are graphical
terminals, the Linux framebuffer console, the situation you’re in when
connecting to a server via its serial console, Emacs shell mode, and probably
more that I’m missing
- there is no one standard for what the “single common set” of escape codes
is, and sometimes programs use escape codes which aren’t actually widely
supported enough


### terminfo & user agent detection


The way that ncurses uses the `TERM` environment variable to decide which
escape codes to use reminds me of how webservers used to sometimes use the
browser user agent to decide which version of a website to serve.


It also seems like it’s had some of the same results – the way iTerm2 reports
itself as being “xterm-256color” feels similar to how Safari’s user agent is
“Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_4) AppleWebKit/605.1.15 (KHTML,
like Gecko) Version/18.3 Safari/605.1.15”. In both cases the terminal emulator
/ browser ends up changing its user agent to get around user agent detection
that isn’t working well.


On the web we ended up deciding that user agent detection was not a good
practice and to instead focus on standardization so we can serve the same
HTML/CSS to all browsers. I don’t know if the same approach is the future in
the terminal though – I think the terminal landscape today is much more
fragmented than the web ever was as well as being much less well funded.


### some more documents/standards


A few more documents and standards related to escape codes, in no particular order:

- the [Linux console_codes man page](https://man7.org/linux/man-pages/man4/console_codes.4.html) documents
escape codes that Linux supports
- how the [VT 100](https://vt100.net/docs/vt100-ug/chapter3.html) handles escape codes & control sequences
- the [kitty keyboard protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/)
- [OSC 8](https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda) for links in the terminal (and notes on [adoption](https://github.com/Alhadis/OSC8-Adoption?tab=readme-ov-file))
- A [summary of ANSI standards from tmux](https://github.com/tmux/tmux/blob/882fb4d295deb3e4b803eb444915763305114e4f/tools/ansicode.txt)
- this [terminal features reporting specification from iTerm](https://iterm2.com/feature-reporting/)
- sixel graphics


### why I think this is interesting


I sometimes see people saying that the unix terminal is “outdated”, and since I
love the terminal so much I’m always curious about what incremental changes
might make it feel less “outdated”.


Maybe if we had a clearer standards landscape (like we do on the web!) it would
be easier for terminal emulator developers to build new features and for
authors of terminal applications to more confidently adopt those features so
that we can all benefit from them and have a richer experience in the terminal.


Obviously standardizing ANSI escape codes is not easy (ECMA-48 was first
published almost 50 years ago and we’re still not there!). I don’t even know
what all of the challenges are. But the situation with HTML/CSS/JS used to be
extremely bad too and now it’s MUCH better, so maybe there’s hope.
