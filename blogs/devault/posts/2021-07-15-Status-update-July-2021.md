---
title: "Status update, July 2021"
date: 2021-07-15
url: https://drewdevault.com/2021/07/15/Status-update-July-2021.html
slug: Status-update-July-2021
word_count: 379
---

Hallo uit Nederland! I’m writing to you from a temporary workstation in
Amsterdam, pending the installation of a better one that I’ll put together after
I visit a furniture store today. I’ve had to slow a few things down somewhat
while I prepare for this move, and I’ll continue to be slower for some time
following it, but things are moving along regardless.

One point of note is that the maintainer for  [aerc](https://aerc-mail.org) , Reto Brunner, has
stepped down from his role. I’m looking for someone new to fill his shoes;
please  [let me know](mailto:sir@cmpwn.com)  if you are interested.

As far as the language project is concerned, there has been some significant
progress. We’ve broken ground on the codegen rewrite, and it’s looking much
better than its predecessor. I expect progress on this front to be fairly quick.
In the meanwhile, a new contributor has come onboard to help with floating-point
math operations, and I merged their first patch this morning — adding
math::abs, math::copysign, etc. Another contributor has been working in a
similar space, and sent in an f32-to-string function last week. I implemented
DNS resolution and a “dial” function as well, which you can read about in my
 [previous post about a finger client](/2021/06/24/finger-client.html) .

I also started writing some POSIX utilities in the new language for fun:

```
use fmt;
use fs;
use getopt;
use io;
use main;
use os;

export fn utilmain() (io::error | fs::error | void) = {
	const cmd = getopt::parse(os::args);
	defer getopt::finish(&cmd);

	if (len(cmd.args) == 0) {
		io::copy(os::stdout, os::stdin)?;
		return;
	};

	for (let i = 0z; i < len(cmd.args); i += 1z) {
		const file = match (os::open(cmd.args[i])) {
			err: fs::error => fmt::fatal("Error opening '{}': {}",
				cmd.args[i], fs::strerror(err)),
			file: *io::stream => file,
		};
		defer io::close(file);
		io::copy(os::stdout, file)?;
	};
};
```

We’re still looking for someone to contribute in cryptography, and in date/time
support — please  [let me know](mailto:sir@cmpwn.com)  if you want to help.

In SourceHut news, I have mostly been focused on writing the GraphQL API for
lists.sr.ht. I have made substantial progress, and I had hoped to ship the first
version before publishing today’s status updates, but I was delayed due to
concerns with the move abroad. I hope to also have sr.ht available for Alpine
3.14 in the near future.
