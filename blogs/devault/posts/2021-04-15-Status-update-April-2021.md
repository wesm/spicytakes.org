---
title: "Status update, April 2021"
date: 2021-04-15
url: https://drewdevault.com/2021/04/15/Status-update-April-2021.html
slug: Status-update-April-2021
word_count: 320
---

Another month goes by! I’m afraid that I have very little to share this month.
You can check out the  [sourcehut “what’s cooking” post](https://sourcehut.org/blog/2021-04-15-whats-cooking-april-2021/)  for sourcehut news,
but outside of that I have focused almost entirely on the programming language
project this month, for which the details are kept private.

The post  [calling for contributors](https://drewdevault.com/2021/03/19/A-new-systems-language.html)  led to a lot of answers and we’ve brought
several new people on board — thanks for answering the call! I’d like to
narrow the range of problems we still need help with. If you’re interested in
(and experienced in) the following problems, we need your help:

* Cryptography
* Date/time support
* Networking (DNS is up next)

[Shoot me an email](mailto:sir@cmpwn.com)  if you want to help. We don’t have the
bandwidth to mentor inexperienced programmers right now, so please only reach
out if you have an established background in systems programming.

Here’s a teaser of one of the stdlib APIs written by our new contributors,
unix::passwd:

```
// A Unix-like group file entry.
export type grent = struct {
	// Name of the group
	name: str,
	// Optional encrypted password
	password: str,
	// Numerical group ID
	gid: uint,
	// List of usernames that are members of this group, comma separated
	userlist: str,
};

// Reads a Unix-like group entry from a stream. The caller must free the result
// using [grent_finish].
export fn nextgr(stream: *io::stream) (grent | io::EOF | io::error | invalid);

// Frees resources associated with [grent].
export fn grent_finish(ent: grent) void;

// Looks up a group by name in a Unix-like group file. It expects a such file at
// /etc/group. Aborts if that file doesn't exist or is not properly formatted.
//
// See [nextgr] for low-level parsing API.
export fn getgroup(name: str) (grent | void);
```

That’s all for now. These updates might be light on details for a while as we
work on this project. See you next time!
