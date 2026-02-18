---
title: "Status update, January 2021"
date: 2021-01-15
url: https://drewdevault.com/2021/01/15/Status-update-January-2021.html
slug: Status-update-January-2021
word_count: 548
---

Hello from the future! My previous status update was last year, but it feels
like it was only a month ago. I hope you didn't miss my crappy jokes too much
during the long wait.

 
One of the advancements that I would like to mention this month is the general
availability of [godocs.io](https://godocs.io), which is a replacement for the
soon-to-be-obsolete godoc.org, based on a fork of their original codebase.
[Our fork](https://sr.ht/~sircmpwn/godocs.io) has already attracted
interest from many contributors who wanted to work on godoc.org, but found the
Google CLA distasteful. We've been hard at work excising lots of Google crap,
rewriting the indexer to use PostgreSQL instead of GCP, and making the little
JavaScript bits more optional & more conservative in their implementation.
We also plan to update it with first-class support for Go modules, which was
never added to the upstream gddo codebase. Beyond this, we do not plan on
making any large-scale changes: we just want godoc.org to keep being a thing.
Enjoy!

On SourceHut, the first point of note is the new dark theme, which is
automatically enabled when your user-agent configures
`prefers-color-scheme: dark`. It has gone through a couple of
iterations of refinement, and I have a few more changes queued up for my next
round of improvements. Please let me know if you notice anything unusual!
Additionally, I broke ground on the todo.sr.ht API 2.0 implementation this
month. It required some minor changes to our underlying GraphQL approach, but
in general it should be fairly straightforward — albeit time consuming
— to implement. Ludovic has also started working on an API 2.0 branch for
hg.sr.ht, which I plan on reviewing shortly.

Small projects have enjoyed some improvements as well.
[mkproof](https://sr.ht/~sircmpwn/mkproof/) grew multi-processor
support and had its default difficulty tweaked accordingly — thanks, Tom!
Zach DeCook and Nolan Prescott also sent some bugfixes for
[gmnisrv](https://sr.ht/~sircmpwn/gmnisrv/), and René Wagner and
Giuseppe Lumia both helped fix some issues with
[gmni](https://sr.ht/~sircmpwn/gmni) as well. Jason Phan sent an
improvement for [dowork](https://sr.ht/~sircmpwn/dowork) which adds
random jitter to the exponential backoff calculation. Thanks to all of these
folks for their help!

That's all for today. Thanks again for your support and attention, and I'll see
you again soon!

...
I have actually been working on this a lot this month. Progress is good.
fn measurements() void = {
	const x = "Hello!";
	assert(len(x) == 6z);
	assert(size(str) == size(*u8) + size(size) * 2z);
	const align: size =
		if (size(*u8) > size(size)) size(*u8)
		else size(size);
	assert(&x: uintptr: size % align == 0z);
};

fn charptr() void = {
	const x = "Hello!";
	const y = x: *const char;
	const z = y: *[*]u8;
	const expected = ['H', 'e', 'l', 'l', 'o', '!', '\0'];
	for (let i = 0z; i < len(expected); i += 1z) {
		assert(z[i] == expected[i]: u32: u8);
	};
};

fn storage() void = {
	const string = "こんにちは";
	const ptr = &string: *struct {
		data: *[*]u8,
		length: size,
		capacity: size,
	};
	assert(ptr.length == 15z && ptr.capacity == 15z);

	// UTF-8 encoded
	const expected = [
		0xE3u8, 0x81u8, 0x93u8, 0xE3u8, 0x82u8, 0x93u8, 0xE3u8, 0x81u8,
		0xABu8, 0xE3u8, 0x81u8, 0xA1u8, 0xE3u8, 0x81u8, 0xAFu8, 0x00u8,
	];
	for (let i = 0z; i < len(expected); i += 1z) {
		assert(ptr.data[i] == expected[i]);
	};
};

export fn main() void = {
	measurements();
	charptr();
	storage();
};
