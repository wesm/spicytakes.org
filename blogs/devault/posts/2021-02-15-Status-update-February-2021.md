---
title: "Status update, February 2021"
date: 2021-02-15
url: https://drewdevault.com/2021/02/15/Status-update-February-2021.html
slug: Status-update-February-2021
word_count: 294
---

Salutations! It's officially a year of pandemic life. I hear the vaccine
distribution is going well, so hopefully there won't be another year of this. In
the meanwhile, I've been working hard on free software, what with having little
else to do. However, I'm afraid I cannot tell you about most of it!

 
I've been working on todo.sr.ht's GraphQL API, and it's going quite well. I hope
to ship a working read-only version later this month. There have been a number
of bug fixes and rote maintenance work on sr.ht as well, but nothing
particularly exciting. We did upgrade everything for Alpine 3.13, which went off
without a hitch. Anyway, I'll go over the minor details in the sr.ht "what's
cooking" post later today.

The rest of the progress was made in secret. Secret! You will have to live in
ignorance for now. Sorry!

(unless you click this)
Here's a peek at our progress:

use fmt;
use io;
use os;

export fn main() void = {
        if (len(os::args) == 1) match (io::copy(os::stdout, os::stdin)) {
                err: io::error => fmt::fatal("Error copying <stdin>: {}",
                        io::errstr(err)),
                size => return,
        };

        for (let i = 1z; i < len(os::args); i += 1) {
                let f = match (os::open(os::args[i], io::mode::RDONLY)) {
                        s: *io::stream => s,
                        err: io::error => fmt::fatal("Error opening {}: {}",
                                os::args[i], io::errstr(err)),
                };
                defer io::close(f);

                match (io::copy(os::stdout, f)) {
                        err: io::error => fmt::fatal("Error copying {}: {}",
                                os::args[i], io::errstr(err)),
                        size => void,
                };
        };
};

I'm looking for a few volunteers to get involved and help flesh out the standard
library. If you are interested, please email
[sir@cmpwn.com](mailto:sir@cmpwn.com) to express your interest,
along with your sr.ht username and a few words about your systems programming
experience — languages you're comfortable with, projects you've worked
on, platforms you grok, etc.
