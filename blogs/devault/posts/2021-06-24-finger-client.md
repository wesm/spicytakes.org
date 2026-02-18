---
title: "A finger client"
date: 2021-06-24
url: https://drewdevault.com/2021/06/24/finger-client.html
slug: finger-client
word_count: 445
---

This is a short follow-up to the  [io_uring finger server](https://drewdevault.com/2021/05/24/io_uring-finger-server.html)  article posted
about a month ago. In the time since, we have expanded our language with a more
complete networking stack, most importantly by adding a DNS resolver. I have
used these improvements to write a small client implementation of the  [finger
protocol](https://datatracker.ietf.org/doc/html/rfc1288) .

```
use fmt;
use io;
use net::dial;
use os;
use strings;

@init fn registersvc() void = dial::registersvc("tcp", "finger", [], 79);
@noreturn fn usage() void = fmt::fatal("Usage: {} <user>[@<host>]", os::args[0]);

export fn main() void = {
	if (len(os::args) != 2) usage();

	const items = strings::split(os::args[1], "@");
	defer free(items);
	if (len(items) == 0) usage();

	const user = items[0];
	const host = if (len(items) == 1) "localhost"
		else if (len(items) == 2) items[1]
		else usage();

	match (execute(user, host)) {
		err: dial::error => fmt::fatal(dial::strerror(err)),
		err: io::error => fmt::fatal(io::strerror(err)),
		void => void,
	};
};

fn execute(user: str, host: str) (void | dial::error | io::error) = {
	const conn = dial::dial("tcp", host, "finger")?;
	defer io::close(conn);
	fmt::fprintf(conn, "{}\r\n", user)?;
	io::copy(os::stdout, conn)?;
};
```

Technically, we could do more, but I chose to just address the most common
use-case for finger servers in active use today: querying a specific user.
Expanding this with full support for all finger requests would probably only
grow this code by 2 or 3 times.

Our language now provides a net::dial module, inspired by  [Go’s net.Dial](https://golang.org/pkg/net/#Dial)  and
the  [Plan 9 dial function](http://man.9front.org/2/dial)  Go is derived from. Our dial actually comes a bit
closer to Plan 9 by re-introducing the service parameter — Plan 9’s
“tcp!example.org!http” becomes net::dial(“tcp”, “example.org”, “http”) in our
language — which we use to find the port (unless you specify it in the
address). The service parameter is tested against a small internal list of known
services, and against /etc/services. We also automatically perform an SRV lookup
for “_finger._tcp.example.org”, so most programs written in our language will
support SRV records with no additional effort.

In our client code, we can see that the @init function adds “finger” to the list
of known internal services. @init functions run on start-up, and this one just
lets dial know about our protocol. Our network stack is open to extension in
other respects, too — unlike Go, third-party libraries can define new
protocol handlers for dial as well, perhaps opening it up in the future to
networks like AF_BLUETOOTH, AF_AX25, and so on, complete with support for
network-appropriate addresses and resolver functionality.

The rest is pretty straightforward! We just parse the command line, dial the
server, write the username to it, and splice the connection into stdout. Much
simpler than the server. Future improvements might rewrite the CRLF to LF, but
that’s not particularly important.
