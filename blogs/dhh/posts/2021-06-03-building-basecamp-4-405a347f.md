---
title: "Building Basecamp 4"
date: 2021-06-03
url: https://world.hey.com/dhh/building-basecamp-4-405a347f
slug: building-basecamp-4-405a347f
word_count: 853
---

Since launching Basecamp in 2004, we've rewritten the entire system not once but twice. First with
[Basecamp 2 in 2012](https://signalvnoise.com/posts/3129-launch-the-all-new-basecamp)
, then with
[Basecamp 3 in 2015](https://signalvnoise.com/posts/3968-launch-basecamp-3)
. Yet unlike other infamous rewrites, we didn't do it due to technical debt. We did it because we wanted Basecamp to be a radically different product every time.
The big ideas that animated our desire for Basecamp 2 and 3 were each time incompatible with the fundamental product design of the previous version, so we needed a rewrite to accommodate those ideas, and to ensure that people who liked working the old way still could continue doing so. That we weren't taking anything away from anyone that they liked using, because why? The technical rewrite was a consequence of those considerations, not the driver.
I gave
[one of my favorite presentations of all time](https://businessofsoftware.org/2015/10/david-heinemeier-hansson-rewrite-basecamp-business-of-software-conference-video-dhh-bos2015/)
at the Business of Software conference in 2015 about these arguments and the decisions to rewrite. It cut against a lot of established wisdom in the industry about when and why you're supposed to rewrite your system (basically, never, if there's anyway to avoid it, and even then, it's an act of shame, like declaring bankruptcy).
Enter Basecamp 4. For the past year or so, we've been in preproduction, while we've been riding the wild wave of success that has been HEY. Originally, we only intended for HEY to occupy our undivided attention for a few months after launch, but with many tens of thousands of customers to serve out the gate, it turned into more than that. So time on Basecamp 4 was spent identifying the leaps we wanted to make,
[shaping the features](https://basecamp.com/shapeup)
that would make those leaps happen, and getting ready for the production phase to commence.
That's kinda now. HEY is in a wonderful place. There's always more work to do, and we have a long list of exciting, quirky, and WEIRD features to continue to pursue, but we're in a place where we can chew gum and blow basecamp bubbles at the same time. So another rewrite, yeah?
No.
Turns out that all the great ideas we have for Basecamp 4 fit as a continuation of the product design we put in place with Basecamp 3, and the technical architecture is in great shape as well. Basecamp 4 just doesn't need to be a rewrite, so we're sure as hell not going to make it one, just because that's the weird path we had taken previously.
Still. The first commit on Basecamp 3 was made on February 12, 2014. That's over seven years ago! Of course we've continued to evolve Basecamp 3 since, and the core majestic monolith is still gleaming in the sunshine. In fact, the architectural harness has not only carried us incredibly far, but when I examine the codebase today, I smile. This is still good. Very good. It's not full of cruft, not a graveyard of bad decisions, not a stacked ledger of technical debt.
I'm mostly talking about the Ruby here. The JavaScript is a slightly different story. Basecamp 3 still has jQuery in it! Alongside Stimulus. Alongside Turbolinks. Alongside a bunch of other directions and styles.
It was the examination of Basecamp 3's frontend that lead us to take the full step to
[Hotwire](https://hotwire.dev)
in HEY. We had most of the ideas and directions in Basecamp 3, but they weren't cohesive, and there were several generations of thought present in the codebase. HEY benefitted from all those experiments and learnings, and it was those that gave us Hotwire. Now it's time to pay back Basecamp for the seeds.
So I've been working on retrofitting Hotwire into Basecamp, as part of the technical stage of preproduction for this upcoming fourth version. It's fascinating to see the jQuery styles in there. Then the leap to Stimulus. And now the next jump to Turbo
[Frames](https://turbo.hotwire.dev/handbook/frames)
and
[Streams](https://turbo.hotwire.dev/handbook/streams)
. The majority of the exercise is one of removing code, verifying that things still work, then smirk at the simpler design. It's fun!
It's also a little dangerous. When refactoring a codebase like Basecamp, it's always tempting to just pulling all the threads all at the same time. Then suddenly you're sitting with a ball of yarn instead of a functional sweater, and it's suddenly a long, cold walk home to a working application again.
That's probably one of the most important lessons I took away from
[Martin Fowler's book on Refactoring](https://martinfowler.com/books/refactoring.html)
. Not just the specific technical patterns, but the deliberate, slow process. One backed up by tests. Not tearing everything apart chasing all of it at once. Slow and steady wins the race.
Besides the benefits to Basecamp, it's already easy to see the benefits to Hotwire on the horizon too. Basecamp is just a much bigger system than HEY in terms of screen count and functionality. My head is already full of ideas of how we can make Hotwire better still. And that's really the cycle of extraction-release-reintegration that's been animating me for all these years. You squint, see the future, then do the work to get there.
Can't wait to share.
