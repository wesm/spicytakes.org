---
title: "Using io_uring to make a high-performance... finger server"
date: 2021-05-24
url: https://drewdevault.com/2021/05/24/io_uring-finger-server.html
slug: io_uring-finger-server
word_count: 4914
---

I’m working on adding a wrapper for the  [Linux io_uring interface](https://unixism.net/loti/what_is_io_uring.html)  to my
 [secret programming language project](https://drewdevault.com/2021/03/19/A-new-systems-language.html) . To help learn more about io_uring and
to test out the interface I was designing, I needed a small project whose design
was well-suited for the value-add of io_uring. The  [Finger protocol](https://en.wikipedia.org/wiki/Finger_protocol)  is
perfect for this! After being designed in the 70’s and then completely forgotten
about for 50 years, it’s the perfect small and simple network protocol to test
drive this new interface with.

In short, finger will reach out to a remote server and ask for information about
a user. It was used back in the day to find contact details like the user’s
phone number, office address, email address, sometimes their favorite piece of
ASCII art, and, later, a summary of the things they were working on at the
moment. The somewhat provocative name allegedly comes from an older usage of
the word to mean “a snitch” or a member of the FBI. The last useful RFC related
to Finger is  [RFC 1288](https://datatracker.ietf.org/doc/html/rfc1288) , circa 1999, which will be our reference for this
server. If you want to give it a test drive, try this to ping the server we’ll
be discussing today:

```
printf 'drew\r\n' | nc drewdevault.com 79
```

You might also have the finger command installed locally (try running “finger
drew@drewdevault.com”), and you can try out the  [Castor](https://sr.ht/~julienxx/Castor/)  browser by sourcehut
user ~julienxx for a graphical experience.

And what is io_uring? It is the latest interface for async I/O on Linux, and
it’s pretty innovative and interesting. The basic idea is to set up some memory
which is shared between the kernel and the userspace program, and stash a couple
of ring buffers there that can be updated with atomic writes. Userspace appends
submission queue entries (SQEs) to the submission queue (SQ), and the kernel
processes the I/O requests they describe and then appends completion queue
events (CQEs) to the completion queue (CQ). Interestingly, both sides can see
this happening  *without*  entering the kernel with a syscall, which is a major
performance boost. It more or less solves the async I/O problem for Linux, which
Linux (and Unix at large) has struggled to do for a long time.

With that the background in place, I’m going to walk you through my finger
server’s code. Given that this is written in an as-of-yet unreleased programming
language, I’ll do my best to help you decipher the alien code.

Let’s start with the basics:

```
use fmt;
use getopt;
use net::ip;
use strconv;
use unix::passwd;

def MAX_CLIENTS: uint = 128;

export fn main() void = {
	let addr: ip::addr = ip::ANY_V6;
	let port = 79u16;
	let group = "finger";

	const cmd = getopt::parse(os::args,
		"finger server",
		('B', "addr", "address to bind to (default: all)"),
		('P', "port", "port to bind to (default: 79)"),
		('g', "group", "user group enabled for finger access (default: finger)"));
	defer getopt::finish(&cmd);

	for (let i = 0z; i < len(cmd.opts); i += 1) {
		const opt = cmd.opts[i];
		switch (opt.0) {
			'B' => match (ip::parse(opt.1)) {
				a: ip::addr => addr = a,
				ip::invalid => fmt::fatal("Invalid IP address"),
			},
			'P' => match (strconv::stou16(opt.1)) {
				u: u16 => port = u,
				strconv::invalid => fmt::fatal("Invalid port"),
				strconv::overflow => fmt::fatal("Port exceeds range"),
			},
			'g' => group = opt.1,
		};
	};

	const grent = match (passwd::getgroup(group)) {
		void => fmt::fatal("No '{}' group available", group),
		gr: passwd::grent => gr,
	};
	defer passwd::grent_finish(grent);
};
```

None of this code is related to io_uring or finger, but just handling some
initialization work. This is the daemon program, and it will accept some basic
configuration via the command line. The getopt configuration shown here will
produce the following help string:

```
$ fingerd -h
fingerd: finger server

Usage: ./fingerd [-B <addr>] [-P <port>] [-g <group>]

-B <addr>: address to bind to (default: all)
-P <port>: port to bind to (default: 79)
-g <group>: user group enabled for finger access (default: finger)
```

The basic idea is to make finger access opt-in for a given Unix account by
adding them to the “finger” group. The “passwd::getgroup” lookup fetches that
entry from /etc/group to identify the list of users for whom we should be
serving finger access.

```
let serv = match (net::listen(addr, port,
		256: net::backlog, net::reuseport)) {
	err: io::error => fmt::fatal("listen: {}", io::strerror(err)),
	l: *net::listener => l,
};
defer net::shutdown(serv);
fmt::printfln("Server running on :{}", port)!;
```

Following this, we set up a TCP listener. I went for a backlog of 256
connections (overkill for a finger server, but hey), and set reuseport so you
can achieve CLOUD SCALE by running several daemons at once.

Next, I set up the io_uring that we’ll be using:

```
// The ring size is 2 for the accept and sigfd read, plus 2 SQEs for
// each of up to MAX_CLIENTS: either read/write plus a timeout, or up to
// two close SQEs during cleanup.
static assert(MAX_CLIENTS * 2 + 2 <= io_uring::MAX_ENTRIES);

let params = io_uring::params { ... };
let ring = match (io_uring::setup(MAX_CLIENTS * 2 + 2, &params)) {
	ring: io_uring::io_uring => ring,
	err: io_uring::error => fmt::fatal(io_uring::strerror(err)),
};
defer io_uring::finish(&ring);
```

If we were running this as root (and we often are, given that fingerd binds to
port 79 by default), we could go syscall-free by adding
 `io_uring::setup_flags::SQPOLL`  to  `params.flags` , but this requires more
testing on my part so I have not added it yet. With this configuration, we’ll
need to use the  `io_uring_enter`  syscall to submit I/O requests.

We also have to pick a queue size when setting up the uring. I planned this out
so that we can have two SQEs in flight for every client at once — one for
a read/write request and its corresponding timeout, or for the two “close”
requests used when disconnecting the client — plus two extra entries, one
for the “accept” call, and another to wait for signals from a signalfd.

Speaking of signalfds:

```
let mask = rt::sigset { ... };
rt::sigaddset(&mask, rt::SIGINT)!;
rt::sigaddset(&mask, rt::SIGTERM)!;
rt::sigprocmask(rt::SIG_BLOCK, &mask, null)!;
let sigfd = signalfd::signalfd(-1, &mask, 0)!;
defer rt::close(sigfd)!;

const files = [net::listenerfd(serv) as int, sigfd];
io_uring::register_files(&ring, files)!;

const sqe = io_uring::must_get_sqe(&ring);
io_uring::poll_add(sqe, 1, rt::POLLIN: uint, flags::FIXED_FILE);
io_uring::set_user(sqe, &sigfd);
```

We haven’t implemented a high-level signal interface yet, so this is just using
the syscall wrappers. I chose to use a signalfd here so I can monitor for SIGINT
and SIGTERM with my primary I/O event loop, to (semi-)gracefully 1  terminate
the server.

This also happens to show off our first SQE submission. “must_get_sqe” will
fetch the next SQE, asserting that there is one available, which relies on the
math I explained earlier when planning for our queue size. Then, we populate
this SQE with a “poll_add” operation, which polls on the first fixed file
descriptor.  The “register” call above adds the socket and signal file
descriptors to the io_uring’s list of “fixed” file descriptors, and so with
“flags::FIXED_FILE” this refers to the signalfd.

We also set the user_data field of the SQE with “set_user”. This will be copied
to the CQE later, and it’s necessary that we provide a unique value in order to
correlate the CQE back to the SQE it refers to. We can use any value, and the
address of the signalfd variable is a convenient number we can use for this
purpose.

There’s one more step — submitting the SQE — but that’ll wait until
we set up more I/O. Next, I have set up a “context” structure which will store
all of the state the server needs to work with, to be passed to functions
throughout the program.

```
type context = struct {
	users: []str,
	clients: []*client,
	uring: *io_uring::io_uring,
};

// ...

const ctx = context {
	users = grent.userlist,
	uring = &ring,
	...
};
```

The second “...” towards the end is not for illustrative purposes - it sets all
of the remaining fields to their default values (in this case, clients becomes
an empty slice).

Finally, this brings us to the main loop:

```
let accept_waiting = false;
for (true) {
	const peeraddr = rt::sockaddr { ... };
	const peeraddr_sz = size(rt::sockaddr): uint;
	if (!accept_waiting && len(ctx.clients) < MAX_CLIENTS) {
		const sqe = io_uring::must_get_sqe(ctx.uring);
		io_uring::accept(sqe, 0, &peeraddr, &peeraddr_sz,
			0, flags::FIXED_FILE);
		io_uring::set_user(sqe, &peeraddr);
		accept_waiting = true;
	};

	io_uring::submit(&ring)!;

	let cqe = match (io_uring::wait(ctx.uring)) {
		err: io_uring::error => fmt::fatal("Error: {}",
			io_uring::strerror(err)),
		cqe: *io_uring::cqe => cqe,
	};
	defer io_uring::cqe_seen(&ring, cqe);

	const user = io_uring::get_user(cqe);
	if (user == &peeraddr) {
		accept(&ctx, cqe, &peeraddr);
		accept_waiting = false;
	} else if (user == &sigfd) {
		let si = signalfd::siginfo { ... };
		rt::read(sigfd, &si, size(signalfd::siginfo))!;
		fmt::errorln("Caught signal, terminating")!;
		break;
	} else for (let i = 0z; i < len(ctx.clients); i += 1) {
		let client = ctx.clients[i];
		if (user == client) {
			dispatch(&ctx, client, cqe);
			break;
		};
	};
};
```

At each iteration, assuming we have room and aren’t already waiting on a new
connection, we submit an “accept” SQE to fetch the next incoming client. This
SQE accepts an additional parameter to write the client’s IP address to, which
we provide via a pointer to our local peeraddr variable.

We call “submit” at the heart of the loop to submit any SQEs we have pending
(including both the signalfd poll and the accept call, but also anything our
future client handling code will submit) to the io_uring, then wait the next CQE
from the kernel.

When we get one, we defer a “cqe_seen”, which will execute at the end of the
current scope (i.e. the end of this loop iteration) to advance our end of the
completion queue, then figure out what I/O request was completed. The code
earlier sets up SQEs for the accept and signalfd, which we check here. If a
signal comes in, we read the details to acknowledge it and then terminate the
loop. We also check if the user data was set to the address of any client state
data, which we’ll use to dispatch for client-specific I/O later on. If a new
connection comes in:

```
fn accept(ctx: *context, cqe: *io_uring::cqe, peeraddr: *rt::sockaddr) void = {
	const fd = match (io_uring::result(cqe)) {
		err: io_uring::error => fmt::fatal("Error: accept: {}",
			io_uring::strerror(err)),
		fd: int => fd,
	};
	const peer = net::ip::from_native(*peeraddr);
	const now = time::now(time::clock::MONOTONIC);
	const client = alloc(client {
		state = state::READ_QUERY,
		deadline = time::add(now, 10 * time::SECOND),
		addr = peer.0,
		fd = fd,
		plan_fd = -1,
		...
	});
	append(ctx.clients, client);
	submit_read(ctx, client, client.fd, 0);
};
```

This is fairly self-explanatory, but we do see the first example of how to
determine the result from a CQE. The result field of the CQE structure the
kernel fills in is set to what would normally be the return value of the
equivalent syscall, and “linux::io_uring::result” is a convenience function
which translates negative values (i.e. errno) into a more idiomatic result type.

We choose a deadline here, 10 seconds from when the connection is established,
for the entire exchange to be completed by. This helps to mitigate
 [Slowloris](https://en.wikipedia.org/wiki/Slowloris_(computer_security))  attacks, though there are more mitigations we could implement
for this.

Our client state is handled by a state machine, which starts in the
“READ_QUERY” state. Per the RFC, the client will be sending us a query, followed
by a CRLF. Our initial state is prepared to handle this. The full client state
structure is as follows:

```
type state = enum {
	READ_QUERY,
	OPEN_PLAN,
	READ_PLAN,
	WRITE_RESP,
	WRITE_ERROR,
};

type client = struct {
	state: state,
	deadline: time::instant,
	addr: ip::addr,
	fd: int,
	plan_fd: int,
	plan_path: *const char,
	xbuf: [2048]u8,
	buf: []u8,
};
```

Each field will be explained in due time. We add this to our list of active
connections and call “submit_read”.

```
fn submit_read(ctx: *context, client: *client, fd: int, offs: size) void = {
	const sqe = io_uring::must_get_sqe(ctx.uring);
	const maxread = len(client.xbuf) / 2;
	io_uring::read(sqe, fd, client.xbuf[len(client.buf)..]: *[*]u8,
		maxread - len(client.buf), offs: u64, flags::IO_LINK);
	io_uring::set_user(sqe, client);

	let ts = rt::timespec { ... };
	time::instant_to_timespec(client.deadline, &ts);
	const sqe = io_uring::must_get_sqe(ctx.uring);
	io_uring::link_timeout(sqe, &ts, timeout_flags::ABS);
};
```

I’ve prepared two SQEs here. The first is a read, which will fill half of the
client buffer with whatever they send us over the network (why half? I’ll
explain later). It’s configured with “flags::IO_LINK”, which will link it to the
following request: a timeout. This will cause the I/O to be cancelled if it
doesn’t complete before the deadline we set earlier. “timeout_flags::ABS”
specifies that the timeout is an absolute timestamp rather than a duration
computed from the time of I/O submission.

I set the user data to the client state pointer, which will be used the next
time we have a go-around in the main event loop (feel free to scroll back up if
you want to re-read that bit). The event loop will send the CQE to the dispatch
function, which will choose the appropriate action based on the current client
state.

```
fn dispatch(ctx: *context, client: *client, cqe: *io_uring::cqe) void = {
	match (switch (client.state) {
		state::READ_QUERY => client_query(ctx, client, cqe),
		state::OPEN_PLAN => client_open_plan(ctx, client, cqe),
		state::READ_PLAN => client_read_plan(ctx, client, cqe),
		state::WRITE_RESP, state::WRITE_ERROR =>
			client_write_resp(ctx, client, cqe),
	}) {
		err: error => disconnect_err(ctx, client, err),
		void => void,
	};
};
```

*What’s the difference between match and switch? The former works with types,
and switch works with values. We might attempt to merge these before the
language’s release, but for now the distinction simplifies our design.*

I’ve structured the client state machine into four states based on the kind of
I/O they handle, plus a special case for error handling:

1. Reading the query from the client
2. Opening the plan file for the requested user
3. Reading from the plan file
4. Forwarding its contents to the client

Each circle in this diagram represents a point where we will submit some I/O to
our io_uring instance and return to the event loop. If any I/O resulted in an
error, we’ll follow the dotted line to the error path, which transmits the error
to the user (and if an error occurs  *during*  error transmission, we’ll
immediately disconnect them, but that’s not shown here).

I need to give a simplified introduction to error handling in this new
programming language before we move on, so let’s take a brief detour. In this
language, we require the user to explicitly do  *something*  about errors.
Generally speaking, there are three somethings that you will do:

* Some context-appropriate response to an error condition
* Bumping the error up to the caller to deal with
* Asserting that the error will never happen in practice

The latter two options have special operators ("?" and “!”, respectively, used
as postfix operators on expressions which can fail), and the first option is
handled manually in each situation as appropriate. It’s usually most convenient
to use ? to pass errors up the stack, but the buck has got to stop somewhere. In
the code we’ve seen so far, we’re in or near the main function — the top
of the call stack — and so have to handle these errors manually, usually
by terminating the program with “!”. But, when a client causes an error, we
cannot terminate the program without creating a DoS vulnerability. This
“dispatch” function sets up common client error handling accordingly, allowing
later functions to use the “?” operator to pass errors up to it.

To represent the errors themselves, we use a lightweight approach to tagged
unions, similar to a result type. Each error type, optionally with some extra
metadata, is enumerated, along with any possible successful types, as part of a
function’s return type. The only difference between an error type and a normal
type is that the former is denoted with a “!” modifier — so you can store
any representable state in an error type.

I also wrote an “errors” file which provides uniform error handling for all of
the various error conditions we can expect to occur in this program. This
includes all of the error conditions that we define ourselves, as well as any
errors we expect to encounter from modules we depend on. The result looks like
this:

```
use fs;
use io;
use linux::io_uring;

type unexpected_eof = !void;
type invalid_query = !void;
type no_such_user = !void;
type relay_denied = !void;
type max_query = !void;
type error = !(
	io::error |
	fs::error |
	io_uring::error |
	unexpected_eof |
	invalid_query |
	no_such_user |
	relay_denied |
	max_query
);

fn strerror(err: error) const str = {
	match (err) {
		err: io::error => io::strerror(err),
		err: fs::error => fs::strerror(err),
		err: io_uring::error => io_uring::strerror(err),
		unexpected_eof => "Unexpected EOF",
		invalid_query => "Invalid query",
		no_such_user => "No such user",
		relay_denied => "Relay access denied",
		max_query => "Maximum query length exceeded",
	};
};
```

With an understanding of error handling, we can re-read the dispatch function’s
common error handling for all client issues:

```
fn dispatch(ctx: *context, client: *client, cqe: *io_uring::cqe) void = {
	match (switch (client.state) {
		state::READ_QUERY => client_query(ctx, client, cqe),
		state::OPEN_PLAN => client_open_plan(ctx, client, cqe),
		state::READ_PLAN => client_read_plan(ctx, client, cqe),
		state::WRITE_RESP, state::WRITE_ERROR =>
			client_write_resp(ctx, client, cqe),
	}) {
		err: error => disconnect_err(ctx, client, err),
		void => void,
	};
};
```

Each dispatched-to function returns a tagged union of (void | error), the latter
being our common error type. If they return void, we do nothing, but if an error
occurred, we call “disconnect_err”.

```
fn disconnect_err(ctx: *context, client: *client, err: error) void = {
	fmt::errorfln("{}: Disconnecting with error: {}",
		ip::string(client.addr), strerror(err))!;

	const forward = match (err) {
		(unexpected_eof | invalid_query | no_such_user
			| relay_denied | max_query) => true,
		* => false,
	};
	if (!forward) {
		disconnect(ctx, client);
		return;
	};

	client.buf = client.xbuf[..];
	const s = fmt::bsprintf(client.buf, "Error: {}\r\n", strerror(err));
	client.buf = client.buf[..len(s)];
	client.state = state::WRITE_ERROR;
	submit_write(ctx, client, client.fd);
};

fn disconnect(ctx: *context, client: *client) void = {
	const sqe = io_uring::must_get_sqe(ctx.uring);
	io_uring::close(sqe, client.fd);
	if (client.plan_fd != -1) {
		const sqe = io_uring::must_get_sqe(ctx.uring);
		io_uring::close(sqe, client.plan_fd);
	};

	let i = 0z;
	for (i < len(ctx.clients); i += 1) {
		if (ctx.clients[i] == client) {
			break;
		};
	};
	delete(ctx.clients[i]);
	free(client);
};
```

We log the error here, and for certain kinds of errors, we “forward” them to the
client by writing them to our client buffer and going into the “WRITE_RESP”
state. For other errors, we just drop the connection.

The disconnect function, which disconnects the client immediately, queues
io_uring submissions to close the open file descriptors associated with it, and
then removes it from the list of clients.

Let’s get back to the happy path. Remember the read SQE we submitted when the
client established the connection? When the CQE comes in, the state machine
directs us into this function:

```
fn client_query(ctx: *context, client: *client, cqe: *io_uring::cqe) (void | error) = {
	const r = io_uring::result(cqe)?;
	if (r <= 0) {
		return unexpected_eof;
	};

	const r = r: size;
	if (len(client.buf) + r > len(client.xbuf) / 2) {
		return max_query;
	};

	client.buf = client.xbuf[..len(client.buf) + r];

	// The RFC requires queries to use CRLF, but it is also one of the few
	// RFCs which explicitly reminds you to, quote, "as with anything in the
	// IP protocol suite, 'be liberal in what you accept'", so we accept LF
	// as well.
	let lf = match (bytes::index(client.buf, '\n')) {
		z: size => z,
		void => {
			if (len(client.buf) == len(client.xbuf) / 2) {
				return max_query;
			};
			submit_read(ctx, client, client.fd, 0);
			return;
		},
	};
	if (lf > 0 && client.buf[lf - 1] == '\r': u8) {
		lf -= 1; // CRLF
	};
	const query = match (strings::try_fromutf8(client.buf[..lf])) {
		* => return invalid_query,
		q: str => q,
	};

	fmt::printfln("{}: finger {}", ip::string(client.addr), query)!;
	const plan = process_query(ctx, query)?;
	defer free(plan);

	client.plan_path = strings::to_c(plan);

	const sqe = io_uring::must_get_sqe(ctx.uring);
	io_uring::openat(sqe, rt::AT_FDCWD, client.plan_path, rt::O_RDONLY, 0);
	io_uring::set_user(sqe, client);
	client.state = state::OPEN_PLAN;
};
```

The first half of this function figures out if we’ve received a full line,
including CRLF. The second half parses this line as a finger query and prepares
to fulfill the enclosed request.

The read operation behaves like the read(2) syscall, which returns 0 on EOF. We
aren’t expecting an EOF in this state, so if we see this, we boot them out. We
also have a cap on our buffer length, so we return the max_query error if it’s
been exceeded. Otherwise, we look for a line feed. If there isn’t one, we submit
another read to get more from the client, but if a line feed is there, we trim
off a carriage return (if present) and decode the completed query as a UTF-8
string.

We call “process_query” (using the error propagation operator to bubble up
errors), which returns the path to the requested user’s ~/.plan file. We’ll look
at the guts of that function in a moment. The return value is heap allocated, so
we defer a free for later.

Strings in our language are not null terminated, but io_uring expects them to
be. This is another case which will be addressed transparently once we build a
higher-level, portable interface. For now, though, we need to call
“strings::to_c” ourselves, and stash it on the client struct. It’s heap
allocated, so we’ll free it in the next state when the I/O submission completes.

Speaking of which, we finish this process after preparing the next I/O operation
— opening the plan file — and setting the client state to the next
step in the state machine.

Before we move on, though, I promised that we’d talk about the process_query
function. Here it is in all of its crappy glory:

```
use path;
use strings;
use unix::passwd;

fn process_query(ctx: *context, q: str) (str | error) = {
	if (strings::has_prefix(q, "/W") || strings::has_prefix(q, "/w")) {
		q = strings::sub(q, 2, strings::end);
		for (strings::has_prefix(q, " ") || strings::has_prefix(q, "\t")) {
			q = strings::sub(q, 1, strings::end);
		};
	};
	if (strings::contains(q, '@')) {
		return relay_denied;
	};

	const user = q;
	const pwent = match (passwd::getuser(user)) {
		void => return no_such_user,
		p: passwd::pwent => p,
	};
	defer passwd::pwent_finish(pwent);

	let enabled = false;
	for (let i = 0z; i < len(ctx.users); i += 1) {
		if (user == ctx.users[i]) {
			enabled = true;
			break;
		};
	};
	if (!enabled) {
		return no_such_user;
	};

	return path::join(pwent.homedir, ".plan");
};
```

The  [grammar described in RFC 1288](https://datatracker.ietf.org/doc/html/rfc1288#section-2.3)  is pretty confusing, but most of it
is to support features I’m not interested in for this simple implementation,
like relaying to other finger hosts or requesting additional information. I
think I’ve “parsed” most of the useful bits here, and ultimately I’m aiming to
end up with a single string: the username whose details we want. I grab the
user’s passwd entry and check if they’re a member of the “finger” group we
populated way up there in the first code sample. If so, we pull the path to
their homedir out of the passwd entry, join it with “.plan”, and send it up the
chain.

At this point we’ve received, validated, and parsed the client’s query, and
looked up the plan file we need. The next step is to open the plan file, which
is where we left off at the end of the last function. The I/O we prepared there
takes us here when it completes:

```
fn client_open_plan(
	ctx: *context,
	client: *client,
	cqe: *io_uring::cqe,
) (void | error) = {
	free(client.plan_path);

	client.plan_fd = io_uring::result(cqe)?;
	client.buf = client.xbuf[..0];
	client.state = state::READ_PLAN;
	submit_read(ctx, client, client.plan_fd, -1);
};
```

By now, this should be pretty comprehensible. I will clarify what the “[..0]”
syntax does here, though. This language has slices, which store a pointer to an
array, a length, and a capacity. In our client state, xbuf is a fixed-length
array which provides the actual storage, and “buf” is a slice of that array,
which acts as a kind of cursor, telling us what portion of the buffer is valid.
The result of this expression is to take a slice up to, but not including, the
0th item of that array — in other words, an empty slice. The address and
capacity of the slice still reflect the traits of the underlying array, however,
which is what we want.

We’re now ready to read data out of the user’s plan file. We submit a read
operation for that file descriptor, and when it completes, we’ll end up here:

```
fn client_read_plan(
	ctx: *context,
	client: *client,
	cqe: *io_uring::cqe,
) (void | error) = {
	const r = io_uring::result(cqe)?;
	if (r == 0) {
		disconnect(ctx, client);
		return;
	};

	client.buf = client.xbuf[..r];

	// Convert LF to CRLF
	//
	// We always read a maximum of the length of xbuf over two so that we
	// have room to insert these.
	let seencrlf = false;
	for (let i = 0z; i < len(client.buf); i += 1) {
		switch (client.buf[i]) {
			'\r' => seencrlf = true,
			'\n' => if (!seencrlf) {
				static insert(client.buf[i], '\r');
				i += 1;
			},
			* => seencrlf = false,
		};
	};

	client.state = state::WRITE_RESP;
	submit_write(ctx, client, client.fd);
};
```

Again, the read operation for io_uring behaves similarly to the read(2) syscall,
so it returns the number of bytes read. If this is zero, or EOF, we can
terminate the state machine and disconnect the client (this is a nominal
disconnect, so we don’t use disconnect_err here). If it’s nonzero, we set our
buffer slice to the subset of the buffer which represents the data io_uring has
read.

The Finger RFC requires all data to use CRLF for line endings, and this is where
we deal with it. Remember earlier when I noted that we only ever used half of
the read buffer? This is why: if we read 1024 newlines from the plan file, we
will need another 1024 bytes to insert carriage returns. Because we’ve planned
for and measured out our memory requirements in advance, we can use “static
insert” here. This built-in works similarly to how insert normally works, but it
will never re-allocate the underlying array. Instead, it asserts that the
insertion would not require a re-allocation, and if it turns out that you did
the math wrong, it aborts the program instead of buffer overflowing. But, we did
the math and it works out, so it saves us from an extra allocation.

Capping this off, we submit a write to transmit this buffer to the client.
“submit_write” is quite similar to submit_read:

```
fn submit_write(ctx: *context, client: *client, fd: int) void = {
	const sqe = io_uring::must_get_sqe(ctx.uring);
	io_uring::write(sqe, fd, client.buf: *[*]u8, len(client.buf),
		0, flags::IO_LINK);
	io_uring::set_user(sqe, client);

	let ts = rt::timespec { ... };
	time::instant_to_timespec(client.deadline, &ts);
	const sqe = io_uring::must_get_sqe(ctx.uring);
	io_uring::link_timeout(sqe, &ts, timeout_flags::ABS);
};
```

Ideally, this should not require explanation. From here we transition to the
WRITE_RESP state, so when the I/O completes we end up here:

```
fn client_write_resp(
	ctx: *context,
	client: *client,
	cqe: *io_uring::cqe,
) (void | error) = {
	const r = io_uring::result(cqe)?: size;
	if (r < len(client.buf)) {
		client.buf = client.buf[r..];
		submit_write(ctx, client, client.fd);
		return;
	};

	if (client.state == state::WRITE_ERROR) {
		disconnect(ctx, client);
		return;
	};

	client.buf = client.xbuf[..0];
	client.state = state::READ_PLAN;
	submit_read(ctx, client, client.plan_fd, -1);
};
```

First, we check if we need to repeat this process: if we have written less than
the size of the buffer, then we advance the slice by that much and submit
another write.

We can arrive at the next bit for two reasons: because “client.buf” includes a
fragment of a plan file which has been transmitted to the client, which we just
covered, or because it is the error message buffer prepared by “disconnect_err”,
which we discussed earlier. The dispatch function will bring us here for both
the normal and error states, and we distinguish between them with this second if
statement. If we’re sending the plan file, we submit a read for the next
buffer-ful of plan. But, our error messages always fit into one buffer, so if we
ran out of buffer then we can just disconnect in the error case.

And that’s it! That completes our state machine, and I’m pretty sure we’ve read
the entire program’s source code by this point. Pretty neat, huh? io_uring is
quite interesting. I plan on using this as a little platform upon which I can
further test our io_uring implementation and develop a portable async I/O
abstraction.  We haven’t implemented a DNS resolver for the stdlib yet, but I’ll
also be writing a finger client (using synchronous I/O this time) once we do.

If you really wanted to max out the performance for a CLOUD SCALE WEB 8.0 XTREME
PERFORMANCE finger server, we could try a few additional improvements:

* Adding an internal queue for clients until we have room for their I/O in the SQ
* Using a shared buffer pool with the kernel, with io_uring ops like READ_FIXED
* Batching requests for the same plan file by only answering requests for it
every Nth millisecond (known to some as the “data loader” pattern)
* More slow loris mitigations, such as limiting open connections per IP address

It would also be cool to handle SIGHUP to reload our finger group membership
list without rebooting the daemon. I would say “patches welcome”, but I won’t
share the git repo until the language is ready. And the code is GPL’d, but not
AGPL’d, so you aren’t entitled to it if you finger me!

1. Right now the implementation drops all in-flight requests during shutdown. If we wanted to be even more graceful, it would be pretty easy to stop accepting new connections and do a soft shutdown while we finish servicing any active clients. net::reuseport would allow us to provide zero downtime during reboots with this approach, since another daemon could continue servicing users while this one is shutting down. ↩︎
