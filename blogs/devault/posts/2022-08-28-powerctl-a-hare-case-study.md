---
title: "powerctl: A small case study in Hare for systems programming"
date: 2022-08-28
url: https://drewdevault.com/2022/08/28/powerctl-a-hare-case-study.html
slug: powerctl-a-hare-case-study
word_count: 1587
---

[powerctl](https://sr.ht/~sircmpwn/powerctl/)  is a little weekend project I put
together to provide a simple tool for managing power states on Linux. I had
previously put my laptop into suspend with a basic “echo mem | doas tee
/sys/power/state”, but this leaves a lot to be desired. I have to use doas to
become root, and it’s annoying to enter my password — not to mention
difficult to use in a script or to attach to a key binding. powerctl is the
solution: a small 500-line Hare program which provides comprehensive support for
managing power states on Linux for non-privileged users.

This little project ended up being a useful case-study in writing a tight
systems program in Hare. It has to do a few basic tasks which Hare shines in:

* setuid binaries
* Group lookup from /etc/group
* Simple string manipulation
* Simple I/O within sysfs constraints

Linux documents these features  [here](https://www.kernel.org/doc/html/latest/admin-guide/pm/sleep-states.html) , so it’s a simple matter of rigging it
up to a nice interface. Let’s take a look at how it works.

First, one of the base requirements for this tool is to run as a non-privileged
user. However, since writing to sysfs requires root, this program will have to
be setuid, so that it runs as root regardless of who executes it. To prevent any
user from suspending the system, I added a “power” group and only users who are
in this group are allowed to use the program. Enabling this functionality in
Hare is quite simple:

```
use fmt;
use unix;
use unix::passwd;

def POWER_GROUP: str = "power";

// Determines if the current user is a member of the power group.
fn checkgroup() bool = {
	const uid = unix::getuid();
	const euid = unix::geteuid();
	if (uid == 0) {
		return true;
	} else if (euid != 0) {
		fmt::fatal("Error: this program must be installed with setuid (chmod u+s)");
	};

	const group = match (passwd::getgroup(POWER_GROUP)) {
	case let grent: passwd::grent =>
		yield grent;
	case void =>
		fmt::fatal("Error: {} group missing from /etc/group", POWER_GROUP);
	};
	defer passwd::grent_finish(&group);

	const gids = unix::getgroups();
	for (let i = 0z; i < len(gids); i += 1) {
		if (gids[i] == group.gid) {
			return true;
		};
	};

	return false;
};
```

The POWER_GROUP variable allows distributions that package powerctl to
configure exactly which group is allowed to use this tool. Following this, we
compare the uid and effective uid. If the uid is zero, we’re already running
this tool as root, so we move on. Otherwise, if the euid is nonzero, we lack the
permissions to continue, so we bail out and tell the user to fix their
installation.

Then we fetch the details for the power group from /etc/group. Hare’s standard
library includes  [a module](https://docs.harelang.org/unix/passwd)  for working
with this file. Once we have the group ID from the string, we check the current
user’s supplementary group IDs to see if they’re a member of the appropriate
group. Nice and simple. This is also the only place in powerctl where dynamic
memory allocation is required, to store the group details, which are freed with
“defer passwd::grent_finish”.

The tool also requires some simple string munging to identify the supported set
of states. If we look at /sys/power/disk, we can see the kind of data we’re
working with:

```
$ cat /sys/power/disk 
[platform] shutdown reboot suspend test_resume 
```

These files are a space-separated list of supported states, with the currently
enabled state enclosed in square brackets. Parsing these files is a simple
matter for Hare. We start with a simple utility function which reads the file
and prepares a  [string tokenizer](https://docs.harelang.org/strings#tokenize) 
which splits the string on spaces:

```
fn read_states(path: str) (strings::tokenizer | fs::error | io::error) = {
	static let buf: [512]u8 = [0...];

	const file = os::open(path)?;
	defer io::close(file)!;

	const z = match (io::read(file, buf)?) {
	case let z: size =>
		yield z;
	case =>
		abort("Unexpected EOF from sysfs");
	};
	const string = strings::rtrim(strings::fromutf8(buf[..z]), '\n');
	return strings::tokenize(string, " ");
};
```

The error handling here warrants a brief note. This function can fail if the
file does not exist or if there is an I/O error when reading it. I don’t think
that I/O errors are possible in this specific case (they can occur when
 *writing*  to these files, though), but we bubble it up regardless using
“io::read()?”. The file might not exist if these features are not supported by
the current kernel configuration, in which case it’s bubbled up as
“errors::noentry” via “os::open()?”. These cases are handled further up the call
stack. The other potential error site is “io::close”, which can fail but only in
certain circumstances (such as closing the same file twice), and we use the
error assertion operator ("!") to indicate that the programmer believes this
case cannot occur. The compiler will check our work and abort at runtime should
this assumption be proven wrong in practice.

In the happy path, we read the file, trim off the newline, and return a
tokenizer which splits on spaces. The storage for this string is borrowed from
“buf”, which is statically allocated.

The usage of this function to query supported disk suspend behaviors is here:

```
fn read_disk_states() ((disk_state, disk_state) | fs::error | io::error) = {
	const tok = read_states("/sys/power/disk")?;

	let states: disk_state = 0, active: disk_state = 0;
	for (true) {
		let tok = match (strings::next_token(&tok)) {
		case let s: str =>
			yield s;
		case void =>
			break;
		};
		const trimmed = strings::trim(tok, '[', ']');

		const state = switch (trimmed) {
		case "platform" =>
			yield disk_state::PLATFORM;
		case "shutdown" =>
			yield disk_state::SHUTDOWN;
		case "reboot" =>
			yield disk_state::REBOOT;
		case "suspend" =>
			yield disk_state::SUSPEND;
		case "test_resume" =>
			yield disk_state::TEST_RESUME;
		case =>
			continue;
		};
		states |= state;
		if (trimmed != tok) {
			active = state;
		};
	};

	return (states, active);
};
```

This function returns a tuple which includes all of the supported disk states
OR’d together, and a value which indicates which state is currently enabled. The
loop iterates through each of the tokens from the tokenizer returned by
 `read_states` , trims off the square brackets, and adds the appropriate state
bits. We also check the trimmed token against the original token to detect which
state is currently active.

There’s two edge cases to be taken into account here: what happens if Linux adds
more states in the future, and what happens if none of the states are active? In
the former case, we have the  `continue`  branch of the switch statement mid-loop.
Hare requires all switch statements to be exhaustive, so the compiler forces us
to consider this edge case. For the latter case, the return value will be zero,
simply indicating that none of these states are active. This is not actually
possible given the invariants for this kernel interface, but we could end up in
this situation if the kernel adds a new disk mode  *and*  that disk mode is active
when this code runs.

When the time comes to modify these states, either to put the system to sleep or
to configure its behavior when put to sleep, we use the following function:

```
fn write_state(path: str, state: str) (void | fs::error | io::error) = {
	const file = os::open(path, fs::flags::WRONLY | fs::flags::TRUNC)?;
	defer io::close(file)!;
	let buf: [128]u8 = [0...];
	const file = &bufio::buffered(file, [], buf);
	fmt::fprintln(file, state)?;
};
```

This code is working within a specific constraint of sysfs: it must complete
the write operation in a single syscall. One of Hare’s design goals is giving
you sufficient control over the program’s behavior to plan for such concerns.
The means of opening the file — WRONLY | TRUNC — was also chosen
deliberately. The “single syscall” is achieved by using a buffered file, which
soaks up writes until the buffer is full and then flushes them out all at once.
The buffered stream flushes automatically on newlines by default, so the “ln” of
“fprintln” causes the write to complete in a single call.

With this helper in place, we can write power states. The ones which configure
the kernel, but don’t immediately sleep, are straightforward:

```
// Sets the current mem state.
fn set_mem_state(state: mem_state) (void | fs::error | io::error) = {
	write_state("/sys/power/mem_sleep", mem_state_unparse(state))?;
};
```

The star of the show, however, has some extra concerns:

```
// Sets the current sleep state, putting the system to sleep.
fn set_sleep_state(state: sleep_state) (void | fs::error | io::error) = {
	// Sleep briefly so that the keyboard driver can process the key up if
	// the user runs this program from the terminal.
	time::sleep(250 * time::MILLISECOND);
	write_state("/sys/power/state", sleep_state_unparse(state))?;
};
```

If you enter sleep with a key held down, key repeat will kick in for the
duration of the sleep, so when running this from the terminal you’ll resume to
find a bunch of new lines. The time::sleep call is a simple way to avoid this,
by giving the system time to process your key release event before sleeping. A
more sophisticated solution could open the uinput devices and wait for all keys
to be released, but that doesn’t seem entirely necessary.

Following this, we jump into the dark abyss of a low-power coma.

And that’s all there is to it! A few hours of work and 500 lines of code later
and we have a nice little systems program to make suspending my laptop easier. I
was pleasantly surprised to find out how well this little program plays to
Hare’s strengths. I hope you found it interesting! And if you happen to need a
simple tool for suspending your Linux machines,
 [powerctl](https://sr.ht/~sircmpwn/powerctl)  might be the program for you.
