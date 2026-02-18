---
title: "Status update, May 2021"
date: 2021-05-16
url: https://drewdevault.com/2021/05/16/Status-update-May-2021.html
slug: Status-update-May-2021
word_count: 328
---

Hello! This update is a bit late. I was travelling all day yesterday without
internet, so I could not prepare these. After my sister and I got vaccinated, I
took a trip to visit her at her home in beautiful Hawaii — it felt great
after a year of being trapped within these same four walls. I hope you get that
vaccine and things start to improve for you, too!

In SourceHut news, I’ve completed and shipped the first version of the
builds.sr.ht GraphQL API. Another update, implementing the write functionality,
will be shipping shortly, once the code review is complete. The next one up for
a GraphQL API will probably be lists.sr.ht. After that it’s just man.sr.ht,
paste.sr.ht, and dispatch.sr.ht — all three of which are pretty small.
Then we’ll implement a few extra features like GraphQL-native webhooks and we’ll
be done!

Adnan Maolood has also been hard at work improving
 [godocs.io](https://godocs.io) , including the now-available  [gemini
version](gemini://godocs.io) . I wrote a post just about godocs.io  [earlier this
month](https://drewdevault.com/2021/05/07/godocs.io-six-months-later.html) .

Here’s some secret project code I’ve been working on recently:

```
use errors;
use fmt;
use linux::io_uring::{setup_flags};
use linux::io_uring;
use strings;

export fn main() void = {
        let params = io_uring::params { ... };
        let ring = match (io_uring::setup(32, &params)) {
                err: io_uring::error => fmt::fatal(io_uring::strerror(err)),
                ring: io_uring::io_uring => ring,
        };
        defer io_uring::finish(&ring);

        let sqe = match (io_uring::get_sqe(&ring)) {
                null => abort(),
                sqe: *io_uring::sqe => sqe,
        };
        let buf = strings::toutf8("Hello world!\n");
        io_uring::write(sqe, 1, buf: *[*]u8, len(buf));
        io_uring::submit_wait(&ring, 1)!;
        let cqe = match (io_uring::get_cqe(&ring, 0, 0)) {
                err: errors::opaque =>
                        fmt::fatal("Error: {}", errors::strerror(err)),
                cqe: nullable *io_uring::cqe => {
                        assert(cqe != null);
                        cqe: *io_uring::cqe;
                },
        };
        fmt::errorfln("result: {}", cqe.res)!;
};
```

The API here is a bit of a WIP, and it won’t be available to users, anyway
— the low-level io_uring API will be wrapped by a portable event loop
interface (tentatively named “iobus”) in the standard library. I’m planning on
using this to write a  [finger](https://datatracker.ietf.org/doc/html/rfc1288) 
server.
