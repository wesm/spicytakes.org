---
title: "Status update, March 2022"
date: 2022-03-15
url: https://drewdevault.com/2022/03/15/Status-update-March-2022.html
slug: Status-update-March-2022
word_count: 347
---

Greetings! The weather is starting to warm up again, eh? I’m a bit disappointed
that we didn’t get any snow this winter. Yadda yadda insert intro text here.
Let’s get down to brass tacks. What’s new this month?

I mainly focused on the programming language this month. I started writing a
kernel, which you can see a screenshot of below. This screenshot shows a
simulated page fault, demonstrating that we have a working interrupt handler,
and also shows something mildly interesting: backtraces. I need to incorporate
this approach into the standard library as well, so that we can dump useful
stack traces on assertion failures and such. I understand that someone is
working on DWARF support as well, so perhaps we’ll soon be able to translate
function name + offset into a file name and line number.

I also started working on a PNG decoder this weekend, which at the time of
writing can successfully decode 77 of the 161 PNG test vectors. I am quite
pleased with how the code turned out here: this library is a good demonstration
of the strengths of the language. It has simple code which presents a
comprehensive interface for the file format, has a strong user-directed memory
management model, takes good advantage of features like slices, and makes good
use of standard library features like compress::zlib and the I/O abstraction. I
will supplement this later with a higher level image API which handles things
like pixel format conversions and abstracting away format-specific details.

In SourceHut news, I completed our migration to Alpine 3.15 this month after a
brief outage, including an upgrade to our database server, which is upgraded on
a less frequent cadance than the others. Thanks to Adnan’s work, we’ve also
landed many GraphQL improvements, mainly refactorings and other like
improvements, setting the stage for the next series of roll-outs. I plan on
transitioning back from focusing on the language to focusing on SourceHut for
the coming month, and I expect to see some good progress here.

That’s all I have to share for today. Until next time!
