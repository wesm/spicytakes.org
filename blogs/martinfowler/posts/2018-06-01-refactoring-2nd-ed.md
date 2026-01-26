---
title: "The Second Edition of âRefactoringâ"
description: "I'm finishing a new edition of my Refactoring book. Here's details and     periodic memos about my work."
date: 2018-06-01T00:00:00
url: https://martinfowler.com/articles/refactoring-2nd-ed.html
slug: refactoring-2nd-ed
word_count: 8676
---


For the past two years, I've been working on a [second edition of my book
    âRefactoringâ](https://martinfowler.com/books/refactoring.html). Here I have details about the new edition and some memos
    describing my thoughts in the last months of this project.


The book is now available and you can buy it from [informit](http://click.linksynergy.com/fs-bin/click?id=tEHDyk1X8h0&subid=&offerid=145238.1&type=10&tmpid=3559&RD_PARM1=http%253A%252F%252Fwww.informit.com%252Fstore%252Fproduct.aspx%253Fisbn%253D0134757599)
 (the web presence of the publisher), [Amazon](https://www.amazon.com/gp/product/0134757599/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0134757599&linkCode=as2&tag=martinfowlerc-20), or your favorite book seller. Purchasing
    the book gives you [access to the canonical web
    edition](https://martinfowler.com/articles/access-refactoring-web-edition.html) - which contains additional material that's not in the physical
    or ebook versions.


It may take a
    while for the book to work its way through the various distribution
    channels. In particular it tends to be slow getting to other countries and
    international availability of electronic formats can get complicated, as
    it's tied into book distribution agreements in various countries.


If you're having difficulty getting a copy, your best bet is to [contact
    informit](http://www.informit.com/about/contact_us/index.aspx?ContactUs_Topics_Partners_id=52ef13bf-d681-4034-ac77-cab3ad782ab5), as my publisher knows much more than me about the
    complications of book distribution.


## Details 
▶


I was lucky enough to work with Kent Beck on the [C3 project](https://martinfowler.com/bliki/C3.html) that birthed
    Extreme Programming. There was a great deal I learned (and am still
    learning) from Kent, but one thing that really stood out was the approach
    he took to continually reworking the code base to keep it healthy, an
    approach that went under the then-unknown name of âRefactoringâ. In my other
    consulting work I stressed how valuable a technique this is, but couldn't
    point people to a book to learn about it, so I ended up writing it myself.
    It was published just before the 20th Century ended.


That's nearly twenty years ago, and the technique is now more widely
    known, although often not executed as well as it should be. The book has
    also held up pretty well, and I think you can take this old book and still
    learn how to refactor pretty much as well as you could all those years ago.
    But the book shows its age, with wrinkles like the use of  `java.util.Vector`.


So over the years I've been thinking about revising it, but I have also
    been reluctant. After all it still teaches the technique perfectly well, and second
    editions have a horrible habit of not improving on the original. But a
    further force has been tugging at me. At the time I wrote it, it was
    becoming mainstream to consider classes as the dominant structuring the
    mechanism for code. These days, however, we see other structures playing a
    greater role. Classes still are valuable, in my view, but our refactoring
    needs to be less centered around them, realizing that they can come and go
    as code is trained into new shapes.


During 2015 and early 2016 I wrote a series of essays exploring various
    circumstances for refactoring, this helped me get a feel for if I should
    tackle a rewrite, and if so, how. By mid 2016 I was ready to commence the
    work in anger.  If you've been wondering why
    I haven't been writing as much for martinfowler.com as I used to, it was because my writing
    energy has been focused on the book since then.


#### Changes in the Second Edition


The changes are both very minor and all-encompassing. They are minor
      because the basic structure of the book hasn't changed. I begin with an
      opening example, a chapter of principles, a survey of âcode smellsâ, and an
      introduction to testing. The bulk of the book is a catalog of refactorings
      and of those 68 refactorings, all but 10 are still present, and I've added
      17 new ones. ([details here](https://martinfowler.com/articles/refactoring-2nd-changes.html))


Despite this lack of change in the overall book structure, the changes to
      the words on pages is huge. Every chapter and refactoring has been
      rewritten, mostly from near scratch. I rarely had decent opportunities to
      cut and paste text from the old edition.


The reorientation towards a less class-centered view is a large part of
      this. Although that may sound as simple as changing the name of âExtract
      Methodâ to âExtract Functionâ, it did entail rethinking all aspects of every
      refactoring. I needed to reconsider the motivation, often feeling that it
      needed to be reframed. The mechanics needed at least a detailed review,
      often a complete rewrite. I wasn't keeping detailed notes on this, but my
      feel is that for every relatively simple import of an old refactoring, there
      were two that required a complete rethink.


However there is another change, which in a way isn't that important, but
      is bound to get a lot of attention. The examples are no longer in Java.


When I choose a language for examples in my writing, I think primarily of
      the reader. I ask âwhat language will help the most readers understand the concepts
      in the book?â *Refactoring* isn't a language specific book, its advice may
      have been explained with the help of examples in Java, but the refactorings apply to
      most languages. I picked Java because I felt the most people would be
      able to understand the code examples if they were written in Java. That was
      the case in 1997, but how about in 2017?


I considered using multiple languages, which would emphasize the
      language-neutral intent of the book. But I felt that would be more
      confusing for the reader, better to use a single language so they can get
      used to a consistent form of expression. So which one would be the most
      approachable to readers? Such a language needed to be widely popular,
      among the top half a dozen in language popularity surveys. It really helps
      to have a C-based syntax, since most programmers would recognize the basic
      code structure. Given that, two stood out. One was Java, still widely used
      and easy to understand. But I went for the alternative: JavaScript.


Choosing JavaScript was deeply ironic for me, as many readers may know,
      I'm not a fan of it.  It has too many awkward
      edge cases and clunky idioms. ECMAScript 2015 (ES6) introduced a rather
      good class model, which makes many object-oriented refactorings much easier to
      express, but still has annoying holes that are built into the fabric of
      the language from its earliest days. But the compelling reason for
      choosing it over Java is that isn't wholly centered on classes. There are
      top-level functions, and use of first-class functions is common. This
      makes it much easier to show refactoring out of the context of
      classes.


#### A Web-First Book


The world-wide web has made an enourmous impact on our society,
      particularly affecting how we gather information. When I wrote the first
      edition, most of the knowledge about software development was transferred
      through print. Now I gather most of my information online. This has
      presented a challenge for authors like myself, is there still a role for
      books, and what should they look like?


I believe there still is role for books like this, but they need to
      change. The value of a book is a large body of knowledge, put together
      in a cohesive fashion. In writing this book I need to gather together
      lots of refactorings, and organize them in a consistent and integrated
      manner.


But that integrated whole is an abstract literary work that, while
      traditionally represented by a paper book, need not be in the future.
      Most of the book industry still sees the paper book as the primary
      representation, and while we've enthusiastically adopted ebooks, these
      are just electronic representations of an original work based on the
      notion of a paper book.


With this book, I'm exploring a different approach. I think of the
      canonical form of this book as the web site. The paper book is a
      selection of material from the web site, arranged in a manner that makes
      sense for print. It doesn't attempt to include all the refactorings in
      the canonical book, particularly since I may well add more refactorings
      to the canonical web book in the future.


Our intention is that when you buy a copy of Refactoring, 2nd Ed, you
      might buy it at a bookstore in its physical form, or online in any form.
      The most essential thing you get for your money is permanent access to the
      web site. You can read the physical book, and access the web site whenever
      you need.


This raises a question of what role ebooks (such as epubs and kindle
      books) should play. There is a strong argument that they should contain
      all the information on the web site, after all physical size isn't a
      factor, and ebooks can be updated easily if I add new material. However
      the book industry doesn't think that way, they expect ebooks to have the
      same content as the physical books, so the ebook versions of refactoring
      will follow that principle, at least for now.


## Earlier Memos 
▶


### Keeping the scope the same (28 March 2018) 
▶


One of the things I want to stress about this edition, is that **it doesnât
cover more scope than the existing book**. There is somewhat of a shift away
from a purely class-based structure but my aim has been not to change the scope
of the book too much. While thereâs a lot of appealing territory I could
explore, I have a limited amount of time and energy. So I followed a rule of not
letting the second edition venture into new topic areas. Even with just trying
to do no more than replicate whatâs in the first edition, itâs still two years
of solid work. I didnât want to increase the amount of time Iâm spending on
this, after all the first edition is very successful, so my aim is to maintain
its usefulness, not to try and create something new.


My general plan was take each refactoring in the first edition, and ask what
needs to be done to it for it to be relevant in this slightly altered context.
In a few (happy) cases I could take the refactoring pretty much as it was, do a
simple rewrite of the example into JavaScript, and be done with it. Usually
however it required a significant rethink of the mechanics and the example. Sometimes
it meant the original refactoring was replaced by something similar.


Thereâs a good chance that in the future, I will explore some new topics, and
add to the corpus of refactorings on the web site. Of course, I thought that
before with the first edition, but mostly didnât, so take that thought with an
appropriate amount of salt. But I did explore some essays on using refactoring to
help explore various architectural problems in 2015 and early 2016. I enjoyed
writing them, and they indicated a vehicle I could easily use more in the future.


### Working through review comments (03 April 2018) 
▶


Iâve spent the last few days (yes, including the weekend) working through review
comments on the book. Early in February my editor at Pearson sent out the
current state of the book to various people for a technical review. This is a
vital part of the process for writing a book, any author will make mistakes, and
I make plenty. Reviewers help catch those, and also highlight things that are
not clearly explained.


This isnât the first review for this book material. When I started the book I
gathered together a panel of people to do on-going review. Every time I finished
a chapter, or a couple of refactorings, Iâd send it to them for comments. Their
feedback has helped enormously. But at some point I need someone to step back
and take a fresh look at the whole book, which is where these recent reviewers
have come in. Currently Iâm going through comments from four such reviewers:
William Chargin, Michael Hunger, Bob Martin, and Bill Wake (who was also part of
my on-going review group).


I like to do this on a chapter by chapter basis, take the first chapter, look at
everyoneâs comments, and process them all on the chapter. âProcessingâ means
reading each comment, and deciding what to do about it. Each comment is a
perspective from the reviewer, some might indicate a suggested change, perhaps
an expression that something isnât clear, perhaps an error in the code. Often I
donât do anything in reaction to the comment, I might disagree with someoneâs
suggestion, perhaps because I feel itâs out of scope for the book. Michael (who
has reviewed previous books for me) feeds me lots of good suggestions for
additional material that would take years to follow up on, so I have to let most
of those go by. But I donât mind because sometimes those suggestions are things
that really need to be there, and Iâm glad I had someone prod me to include them.


Errors are the obvious things to fix, and Iâm regularly astonished when
reviewers find subtle code errors. I avoid many of those by my automated code
import system, but there are holes in the auto-import, and theyâve already saved
me some embarrassing mistakes. Michael is particularly good at this, he must
have installed several compilers into his wetware, which is one reason why I
find him such a good reviewer. William Chargin is challenging him however, so I
feel doubly blessed.


Clarifications are often the hardest to figure out. Sometimes a reviewer just
says âI donât understand thisâ, sometimes itâs more indirect - they suggest
something that implies they didnât understand what I was saying. Dealing with
these is hard because I then have to judge whether itâs just a one-off thing, or
something deeper. People will always have difficulties with bits of a book,
trying to fix every individual difficulty would be cure worse than the disease
- the book would have to be much bigger, and the prose would get so stilted that it
would be tedious to read. It helps when more than one reviewer has the same
difficulty, then I can be confident itâs something I need to fix. An example of
this was the way I laid out nested functions in the opening example confused
three of the panel, so I knew I had to try a different approach.


I always rather enjoy working through review comments. Itâs good to get some
feedback on whether what Iâm doing is making sense. This stage is particularly
good as it forces me to step back too. For nearly two years Iâve been down in
the details, cranking chapter by chapter. Now I can look at the material as a
whole, yet still dive down to sort out important details.


### Refactoring takes the Red and Black (05 April 2018) 
▶


When I wrote the first edition of Refactoring, it went into the Object
Technology Series at Addison Wesley. I never took book series very seriously, so
I just followed my editorâs suggestion. Since then Iâve formed my own series
(the âsignature seriesâ), and put a fair amount of effort into curating it so it
only contains books I can firmly recommend. So itâs natural for the book to move
into my own series.


It isnât, however, an inevitable decision. The series isnât a catch all, itâs
about books that I consider to be foundation books on the 
technical side of programming. I submitted my most recent book, NoSQL Distilled,
for the series, but I rejected it - because I didnât think it fit in
with the flavor of the series. That sounds rather convoluted, but there is a
process here. Every candidate book submitted to the series is sent to all the
authors in the series, and I ask for their opinion. In that case, they helped me
decide to reject myself. This time they felt it was an easy inclusion, which
reinforced my feeling that it was a good fit.


### Pause in Review Updates (06 April 2018) 
▶


As I said in an earlier memo, Iâm enjoying going through review comments.
However Iâm about to put this work on a long pause. I have travel commitments
coming up that means that today is the last day Iâll get at my desk for five
weeks. While I can technically do some writing work while Iâm on the road, Iâll
mostly be too busy with other things to put any serious energy into it. (And
there is some vacation in there, which I hope will help rejuvenate me a bit.)
Itâs a frustrating break, since Iâd really like to get the text of the book
settled so to better concentrate on other things. Iâd hoped to have all the
review comments processed and dealt with by now, but plans in writing are little
better than plans in software development (for much the same reasons).


### Back at my desk (18 May 2018) 
▶


This week was the week I finally got back to my desk in New England after five
weeks on the road. It was a long time away, but I canât complain too much since
the last couple of weeks were an excellent vacation in Croatia. Highlights were
Split, Dubrovnik, the [Paklenica national
park](https://en.wikipedia.org/wiki/Paklenica), and especially the [Plitvice
Lakes](https://en.wikipedia.org/wiki/Plitvice_Lakes_National_Park).


I had hoped to have finished the text before I went away, but there were still
some review comments that needed work. I also got a final batch of comments just
before I left. So this week I made my first pass through that final batch and
now just have the outstanding todos from the reviews. The bad news is that all
these todos take a bit of effort to fix, since they became todos since I
couldnât quickly fix them while going through the comments. The good news is
that I only have fourteen of them. I will hopefully get through them over the
next two weeks before I have to hit the road again.


Another topic on the book this week was starting to think about the cover. The
core cover design is already settled, as it will be part of my signature series,
but it does mean I have to pick a photo of a bridge. Weâre in the middle of
sorting that out now, hopefully Iâll be able to share that next week.


### Reworking examples (25 May 2018) 
▶


As with last week, this week has seen me working on review comments so I can
finalize the technical content of the book before starting the production
process. I went through all the comments last week, doing all the easy ones that
I could deal with in less than an hour or so. That left the complicated ones,
which are  pretty stressful to be working on at this late stage in the game,
with a (admittedly, somewhat self-imposed) deadline staring at me.


At the heart of my work this week is reworking two examples. Both were ones
where a couple of reviewers found difficult to follow, so I needed to figure out
something that I think will be easier. This isnât just about changing the prose
text, itâs also about reworking the code. I find code examples to be
one of the most difficult aspects of my writing. I try to create examples that
are just complicated enough to show the main point, but no more complicated that
that. They are still artificially simplistic - any realistic example is just too
much for most readers to get their head around - but I want them to resonate
with readersâ day-to-day experience. Today I spent most of the day coming up
with an example thatâs about fifty lines of code. I think it captures what
Iâm trying to say, but Iâll learn more as I carry out the refactoring Iâm
illustrating on this code and see how my prose works with it. Iâm optimistic that
it will work, but thereâs still a fair bit of uncertainty.


The earlier example was particularly tricky as it was a section of a larger
refactoring example, the future opening example of the book. This example
divides into three phases, and reviewers indicated problems with the middle
phase. I reworked the sequence of the refactorings, and hopefully things are
much clearer now. Interestingly this refactoring centers around a refactoring
(Split Phase) that I hadnât written up before my first draft of the opening
example. The essence of the change was to follow the now-written mechanics of
this new refactoring, and I was happy to see that following these mechanics seemed
to make it a good bit easier to do and understand. The mechanics sections in my
book arenât the only mechanics for a refactoring, and they canât be the best for
all contexts. My aim is that they should work pretty well, most of the time.
So I was pleased that following them helped me through this example.


Reworking refactoring examples like this make me very familiar with git. I like to keep
all my code examples âliveâ, so that I can change the code, run tests to ensure
it still works, and mark sections of it to automatically flow into the book
text. Iâve done this for many years with code examples, and itâs made life much
easier. But doing this is tricky with refactoring, since I have a sequence of
changes to the code. To cope with this I store the refactoring sequence in a git
repository (necessarily a separate repo to the one that stores the bookâs text)
and capture the refactoring as a sequence of commits. I then import the code
into the book text with tags that indicate the ref of the commit, and the name
of the code fragment. When reworking a sequence of refactorings like this, I do
a lot of cherry picking, where I make a change to commit master~7, then cherry
pick all the refactoring changes I did since onto the changed commit. Itâs
awesome when it works well, and even when it doesnât itâs far better than what I
had to do with the first edition of the book.


I have one more week at my desk before Iâd like to declare âdoneâ. The target
still seems plausible, although much will depend on how the fifty lines I wrote
today works as I write about the refactoring steps that go with it.


### Released to Production (01 June 2018) 
▶


As May ended, I hit an important milestone, referred to by my publisher as
ârelease to productionâ. In the days of traditional publishing, this means that
the author hands her manuscript over to the production team. At this point we
expect no significant changes to the core material of the book. There will be
changes: as the book goes into copy-edit, as well as things like indexing - but
they wonât be material changes to the essence of the book.


In my early books, Iâd send electronic files over to Pearson, and at some later
point Iâd get a big print out of changes marked up by the copy-editor. Other
than going through these changes, checking to see if I agreed with them or not,
Iâd have little more to do with the book before it appeared on the shelves.
These days, the process is rather more interactive, the copy-editor and I will
share a git repository and Iâll be looking at diffs to see his suggested
changes. But the sense of crossing an important bridge is still there. I wonât
be reworking any more examples, or adding any significant material. At some
level, the book is done. (Although, since this is a web-first book, I intend to
continue to evolve its web representation).


I have a sense of relief, although there is still much to be done with the book,
this is still a big milestone, a sign that my focus on the book will begin to
wane. I donât have too much relief, because I have to go to Madrid next week for
a couple of talks, and speaking trips are less appealing to me than a trip to
the dentist. But it is some weight taken from my mind.


### The new cover (13 June 2018) 
▶


When we started doing the signature series, the cover designer laid out the basic
design which included space for a different photograph with each book.
I decided that these photographs should follow a theme for all the books in the
series. 
At that time my wife, a structural
engineer, was designing bridges; she has since moved from horizontals
(bridges and tunnels) to verticals (buildings). Her involvement in bridges
inspired me to use them as a common theme for the book. So whenever an author
writes a book in my signature series, I ask them to choose a bridge to adorn the
cover. Ideally the bridge should have some personal connection for them.


For my first book in the series ([Patterns of Enterprise Application
Architecture](https://martinfowler.com/books/eaa.html)), I picked the Zakim bridge in Boston. The link was pretty clear -
they built the bridge just down the road, during the same years that I wrote the
book. For my second series book ([Domain-Specific Languages](https://martinfowler.com/books/dsl.html)), I picked the [Iron
Bridge](https://en.wikipedia.org/wiki/The_Iron_Bridge) - this was a connection to the Black Country where I grew up, as well as
a historically important bridge.


So what to choose for the Refactoring book? One thought that occurred to me was
if I could draw some kind of analogy between refactoring and bridge
engineering - but discussion with the bridge engineers I know made it clear that
thereâs nothing in bridge engineering that is comparable to refactoring. So
instead my mind turned to a non-professional association. In this case I started
thinking about one of my favorite places that Iâd visited many times in the
two-plus decades Iâve lived in New England - [Acadia National Park](https://en.wikipedia.org/wiki/Acadia_National_Park). This
immediately suggested picking one of the many attractive bridges that are on the
carriage roads.


But I also thought of another Acadia-tinged possibility. On the road to Acadia
we cross the Penobscot River. At the time that I wrote the first
refactoring book, the road crossed the Penobscot using [Waldo-Hancock Bridge](https://en.wikipedia.org/wiki/WaldoâHancock_Bridge),
a suspension bridge designed by the notable bridge engineer David Steinman. In
the first years of the new century, however, they found that the 70 year-old
bridge needed to be replaced, and by 2007 the road went over the new [Penobscot
Narrows Bridge](https://en.wikipedia.org/wiki/Penobscot_Narrows_Bridge_and_Observatory).


On one of our trips up to Acadia, we stopped so I could take some photos of the two
bridges. Iâm glad we finally did do that, because a year later the Waldo-Hancock
was demolished. (Itâs a shame that I took my photos on such an overcast day.)


Although there arenât any analogies I can draw between bridge engineering and
refactoring, I can push myself to summon up creative analogies between the two
editions of the refactoring book and these two bridges.


Although various twitterers have commented that the second edition of the
refactoring book ârefactorsâ the first edition, that isnât true. (Indeed,
as with bridge engineering, I donât think there is any analogy from refactoring
to book writing.) This second edition is a replacement to the old one, in the
same way that the Penobscot Narrows bridge replaces the Waldo-Hancock. The
Waldo-Hancock demonstrated innovative techniques that reduced the cost of bridge
building, in the same way that the refactoring book described a new technique
that reduces the cost of building software systems. The first edition of the
book is replaced by a new edition within my signature series, and the new
Penobscot Narrows bridge is a similar design to the Zakim bridge that was the
cover bridge for the first book in that signature series.


### Two Kinds of Readers (27 June 2018) 
▶


When building software, its important to think about the software from your
userâs perspective. So we have the notion of creating personas and use
these personas to help guide the features and user-experience of the software
systems. Similarly with books, itâs important for me to think of my readers and
have some notion of the personas that should guide my writing.


The most obvious persona for a piece of writing is the student reader - he has
little or no knowledge of the topic in the book, and is reading the book to
learn the material. This is my primary persona, and I try my best to understand
what is in this readerâs mind and how best to convey information to him.


But there is a second persona thatâs also important - the teacher. This persona
already knows most, if not all the material in the book. She uses the book to
help guide more junior developers. Essentially the book is tool for her to help
her task of improving her teamâs skills.


Sometimes she may use the book directly, saying to a junior that he needs to
change a particular class to a value object and thus use the [Change Reference
to Value](https://refactoring.com/catalog/changeReferenceToValue.html) refactoring. At a higher level she might focus on a
smell. One technique Iâve heard is of a team lead to designate a âsmell of the
weekâ and get the team to identify and fix examples of that smell. This both
improves the code and teaches the developers how to spot and fix similar
problems in the future.


Even if the book isnât used directly, I hope it is still handy in an indirect
form. A senior developer may have the knowledge of refactoring, but that doesnât
mean that she knows how to teach it. Teaching a topic is a skill in its own
right, somewhat independent from knowledge of a topic or skill in carrying out a
task. Iâve often come across gifted practitioners who were not very good at
teaching others what they do. A good book can be helpful in showing such leaders
how to explain a topic. The mechanics section for Change Reference to
Value isnât the only way to carry out the refactoring, but following those
steps can make it easier for a skillful colleague to show someone new how to do it.


An interesting consequence of the second edition like this is that most of the
people who are excited about the book are teacher-readers not student-readers.
Teachers might well have been student-readers with the first edition many years
ago. If youâre such a reader, remember this book wonât teach you anything new
about refactoring. If it teaches you anything, it is how to teach it to those
you are leading. When you evaluate if this book is useful to you, itâs not for
what you can learn from it, but how it can help you accelerate the learning of
those around you.


### Some hidden heroes (10 July 2018) 
▶


All the technical book authors I know mention the big debt they have to
technical reviewers. Weâve all written works with big flaws that were caught by
our peers acting as reviewers. I donât do a lot of technical review work, partly
because I donât think Iâm very good at it, and thus have a lot of admiration for
those who take it on. Thereâs not even a pittance to be made by reviewing
someone elseâs book, so doing it as a great act of generosity.


When I started serious work on the book, I formed a mailing list of advisors to
give me feedback. As I made progress, I sent drafts of new material to this
group and asked them for their feedback. I want to thank the following for
posting such feedback on the mailing list: **Arlo Belshee, Avdi Grimm, Beth
Anders-Beck, Bill Wake, Brian Guthrie, Brian Marick, Chad Wathington, Dave Farley,
David Rice, Don Roberts, Fred George, Giles Alexander, Greg Doench, Hugo
Corbucci, Ivan Moore, James Shore, Jay Fields, Jessica Kerr, Joshua Kerievsky,
Kevlin Henney, Luciano Ramalho, Marcos Brizeno, Michael Feathers, Patrick Kua,
Pete Hodgson, Rebecca Parsons,** and **Trisha Gee.**


Of this group, Iâd particularly like to highlight the special help I got on JavaScript
from **Beth Anders-Beck, James Shore**, and **Pete Hodgson**.


Once I had a pretty complete first draft, I sent it out for further review,
because I wanted to have some fresh eyes look at the draft as a whole. **William
Chargin** and **Michael Hunger** both delivered incredibly detailed review comments. I
also got many useful comments from **Bob Martin** and **Scott Davis**. **Bill Wake** added
to his contributions on the mailing list by doing a full review of the first
draft.


I found the combination of incremental review by the mailing list and final full
review to work really well. Leaving all the review to the end (as was the case
with my earlier books, including the first edition) results in me getting useful
comments too late. I was able to take early comments on board and react to them
as I continued with the book. The final review was still helpful because itâs
easy for incremental reviewers to lose the overall context of the book - indeed
itâs easy for me to lose that context when in the depths of working on it.
Having fresh eyes look at the whole can make a big difference.


### Completed Copyedit (25 July 2018) 
▶


Iâve just finished reviewing the copyedits for Refactoring. This is the stage
where my flawless prose is sent to someone who checks to see if itâs as
wonderful as I imagine, and sends back a list of corrections. In my case a
rather large list.


Authors react in a wide range of ways to the copyedit process. Some authors go
into a rage if a single character of their immaculate text is changed. Other
authors are so sick of the manuscript that they wave all the changes through. I
tend to the latter, but still review every change - mostly to ensure the
copyeditor hasnât inadvertently changed the meaning of the text, a real danger
with such a technical book.


I find this review both interesting and frustrating. Itâs frustrating because by
this point Iâm really done with the text and donât want to read it again. Many
of the copyedits seem rather arbitrary to me - changing some punctuation or
wording in ways that donât seem to make a significant difference to me. For
example, I never really saw the point of semicolons, so hardly ever use them.
But copyedit changes like this are for the reader, not for me. [Dmitry
Kirsanov](http://kirsanov.com/), my current copyeditor, says: âcopyediting (when
itâs not simply fixing bad grammar) is a matter of *intonation*. Authors donât
always hear their own intonation, much like we donât properly hear our own voice
and are often surprised (usually unpleasantly) to hear it in a recording.â


Authors vary with their reaction to copyeditors, but different copyeditors do
varied jobs too. I appreciated the first decent copyeditor I worked with because
she believed that it was crucial that she should preserve the authorâs voice as
much as possible. My main memory from her work was adding lots of commas -
unsurprisingly I donât tend to put them in unless I feel I really need to. Sadly
I couldnât use her for my books because sheâs British, and American publishers
didnât think a Brit could possibly copyedit to American standards. Dmitry has
been my copyeditor for my last two books and I enjoy his work too. Although many
of his changes make me shrug, many of them are distinct improvements to my
wording (including one in this sentence). And sometimes he pops in a change that
sounds more like me than I do, which is creepy and wonderful at the same time.


Some copyeditors Iâve run into make a point about how they are changing the text
to make it *correct*, an attitude that does make my eyes roll. After all many of
the rules of âcorrect Englishâ were 19th century conventions invented to
distinguish well-educated upper-class people from plebs like me. (The
split-infinitive rule only exists to ape latin, for example.)


In a couple of
cases Iâve seen a copyeditor copyedit text thatâs already been copyedited by a
different copyeditor, and ends up making as many changes as they did with
uncopyedited text. (me feel smug.)


This site isnât copyedited - you get my raw text. I havenât seen many
complaints about it, so Iâve been happy to get away with the convenience
of skipping a copyedit stage.


### Trimming the Print Edition (07 August 2018) 
▶


Of all the changes Iâm making for the second edition, perhaps the most
significant is that Iâm writing it as a web-first book. By this I mean that
that the canonical representation of the book is one that lives on a web
site, overriding  other representations of the book, such as those printed on
paper. Pearson is setting things up so that when you get a physical book, you
get the ability to register it with Pearson and gain access to the web version
of that book. As a secondary representation of the book, the paper version will have
less content. Furthermore I hope to add more material to the web version of the
book in the future, and of course the paper version cannot be updated.


A couple of weeks ago I had to make the decision of what would appear in the
paper book, and what would be only present in the web edition. One constraint I
set for myself is that the second edition of the book wouldnât be larger than
previous editions. (This also a rule I set for myself with UML Distilled.) I did
this because Iâve found that second editions have a danger to bloat. I can see
why - after all an author learns more about a subject and wants to put all the
new stuff in - but a bigger book isnât usually a better book. Since Refactoring
follows a duplex form, and is mostly a reference catalog, increasing the size
shouldnât be such a big problem, but I still distrust a big, physical book - so
Iâve kept the constraint.


The first edition clocks in at 412 pages (not including the references and
index), so I set that as my target. We did an initial page proof and the new
book had 440 pages, so I needed to cut at least 28 pages to meet my self-imposed
limit. As I started figuring out where to make the cut I was pretty worried
about the choice, but Iâm relieved to say it worked out easier than I had
feared.


I have 63 refactorings in the new book and I divided them into two priority
levels. I then took the lower priority refactorings and looked for those that
werenât referred to from elsewhere in the book. That identified five
refactorings that comprised 19 pages - these I could remove from the print
edition quite easily. I still, of course, had another 9 pages to go. I could
remove some more refactorings, but instead I had my eye on an example that took
ten pages. This was a second example for the Split Phase refactoring, a nice
example but not strictly necessary as I already had one example in place.
Furthermore this second example was one Iâd done early on in Java, and didnât
feel like rewriting in JavaScript. It would be the only Java example in the
print book, so removing it took out something that would look rather odd anyway.


We rebuilt the book with these cuts and it came out to 410 pages. So, while the
arithmetic didnât work out quite right, I was within the limit Iâd set myself. (I
should also reiterate: these five refactorings will be available to all book
owners, youâll just have to go to the web site to see them rather than have them
on paper.)


I realize that a few readers might be wondering, what are those five refactoring
victims? Iâll name names later - so far I havenât talked about what refactorings
are in the second edition, nor about the fate of all the first edition
refactorings. Iâll get to all of that in a later memo.


This last two weeks has been very busy, as Iâve had to scramble to get a couple
of tasks done for the book production. I was hoping to wind down on work on this
book soon, but now Iâm accepting that thereâs still a lot to do, partly in
preparation for the web edition. Iâll talk about all that more in later memos too.


### Composing the Print Book (24 August 2018) 
▶


During the last couple of weeks, my work on the refactoring book has focused on
tidying up various loose ends for the print book. Weâre now at the point where
the production work is now in the hands of Alina Kirsanova, who sorts out the
composition of the book, together with proof reading. Composing a book means
paying attention to the look of each page, and various problems crop up around
pagination.


When Iâm writing, I donât worry much about page breaks. Most of my published
writing these days goes on the web, so I donât have to think about physical
pages. But with a book, physical pages are important. An example problem area is
code examples. I donât want page breaks at the wrong place in a code example,
ideally Iâd like my carefully written small functions to not run over page breaks. So Alina
looks at each page, ensuring the page breaks occur in the right places. To
support that, I need to tweak my automatic import of code examples so she can
make insert a page break when she needs to.


Line lengths are also something she pays attention to. As I look at my source
files, I now see new XML tags: such as `<dk:nobr>clarity</dk:no-br>` to indicate
text that we donât want split over two lines. This is one of the advantages of
using XML rather than markdown as my source text - itâs easy for Alina to add
new markup for the text that my toolchain can pass through to hers.


Iâve also prepared reference pages: filling out the bibliography, and generating the
list of refactorings and smells tables for the inside covers. Next I have to go
through the final proofs of the pages, and dealing with some composition
questions that Alina has. Many authors prefer to hand over their manuscript and
leave it at that - an approach Iâm certainly sympathizing with right now. But
one of the advantages of participating in this is that I get to appreciate the
careful work of book composition.


### Rough Cut available on Safari (29 August 2018) 
▶


People with a subscription to the Safari online books service can now get hold of a [rough
cut of the second edition](https://www.safaribooksonline.com/library/view/refactoring-improving-the/9780134757681/). This had been through copy-edit, but not proof
reading or final composition.


### Most people will be disappointed by the second edition (30 August 2018) 
▶


When Iâm close to releasing a new book, my feelings are usually a mix of
excitement and dread. Excitement because Iâm releasing into the world something
Iâve spent months or years working on, and I want to see how people respond to
it. Dread because Iâm releasing into the world something Iâve spent months or
years working on, and I worry about how people respond to it. Will people like
it or not? Will all that work be worthwhile or not?


With this second edition my feeling is more one of acceptance that most people
will be disappointed.


Itâs not that I donât think Iâve done good work here. Like with any of my
writing projects, Iâve put a lot of effort and energy into this. I think the
result is a worthy refresh of the book Iâm most proud of writing. But even if
that is the case, I expect a negative reaction to the book. Thatâs because
people who are familiar with the first edition will naturally compare it to that
first edition, and most people will find the new edition wanting - despite my
view that Iâve improved it.


People are familiar with the first edition,
have got used to its flaws, and like elements in the original that I decided to 
change. We know that loss aversion means that people feel the loss of something
twice as much as they appreciate a corresponding gain. So any improvements in
the new edition have to be twice as good as any perceived faults in order for me
to break even - thatâs a hard target to achieve.


On top of this, many people wonât compare this second edition to the first edition,
they will compare it to what they imagine they would like in a second edition.
Often those imaginations arenât realistic - thereâs plenty of ideas Iâve had
that sounded good in my head, but didnât work when I tried to write them down.
Even sticking to the realistic ones, there are so many of them. In the end I
have to pick one path, and even if I picked the most popular path, they diverge
so much that it would still only match a small minority of the opinions that are
out there.


(I suspect my feelings here are shared by other authors, which may explain why
so many struggle with revised editions, or later installments of a multi-volume work.)


Given this inevitable disappointment, why did I bother to do a second edition?
(Iâve asked myself this question many times in last couple of years.) The answer
is that the true judgment on this new edition isnât the immediate reaction in
the few months after itâs released. Instead itâs whether it helps people learn
about refactoring in five, ten, twenty years time. Most of the target audience
for this edition donât even know about the book yet, many havenât yet written a
program, most will never care about the first edition. The impact on those
readers is the test for whether this effort was worthwhile. Sadly it will be
many years before I can assess the value of my labors over the last couple of
years.


### Gone to the Printers (28 September 2018) 
▶


The files for the second edition were sent to the printers today. This completes
all the work we needed to do on producing the print edition. My thanks again
to Alina Kirsanova who composed the book, did proof reading (finding some
particularly embarrassing errors), and did the index. Julie Nahil, from Pearson,
has been the production editor on the book, coordinating all this production work.


We expect printed books to appear in Pearsonâs warehouse towards the end of
October or early in November. They should go out into the retail channel shortly
after that.


But one hiccup may be the web edition. We donât want the print edition to appear
before we have the web edition sorted out, and I havenât had as much time as I
would like to sort that out. Iâve taken a couple of weeks vacation (hiking in
Cornwall, some theater in London, games with friends, and some pleasantly
extravagant food), and now have a couple of business trips over the next two
weeks. Iâve now got most of the elements of the pipeline for the web edition
sorted out, but wonât be able to start work on it properly until mid October.
Hopefully it wonât take too long to come together, but as I havenât done this
before I donât know what can go wrong. Other than itâs software, and we all now
how easy that is to predict!


### Working on the Web Edition (20 October 2018) 
▶


On my last update, a few weeks ago, I mentioned that the book had gone to the
printers, and presumably they are busily printing away. Since then my number one
priority with the book is to finalize the web edition. Although all the writing
is done, I still have to prepare the files and do the layout. I wasnât able to
start right away, as I had a couple of Thoughtworks meetings to attend to: in
Atlanta to decide the next radar, and a global management meeting in Beijing.


But this week Iâve been back at my desk and able to work on the book again. The
first task was to understand how the web edition gets published. Pearson has a
web book viewer, which basically takes an epub folder and projects it through a
simple web application. The good thing about this is that that most
of the book is just web pages, which Iâm familiar with generating (and indeed
this is how I looked at the book for most of the time I was writing it). However
I did have to sort out various things that were needed, including generating the
appropriate epub manifest files and fixing things that are valid html in a web
context but not in an epub context.


Once the bare bones were in place, I needed to apply the right css, to do things
like ensure that deleted code was correctly marked with strikethrough,
generating table of contents and list of refactorings. There were some
interesting complications, such as finding out the span class name I use to
highlight code was used by the viewer for something else.


But now Iâm very close to done (my org mode checklist shows 9/13 tasks complete) so
feel pretty happy that the web edition will be done next week shortly after I
return from our âParadigm Shiftâ conference in Toronto. That will mean that
weâll be able start selling the physical books soon after they come back from
the printer.


I still wonât be done, however. The next task is to rework [refactoring.com](https://refactoring.com), in
particular the catalog, updating it with the new refactorings. I also want to
put together a list of whatâs in the web edition that isnât in the print books


(I usually donât like to say things like ânearly doneâ, but I havenât written
any progress notes for a while, and felt I owe everyone an update.)


### Books are printed (19 November 2018) 
▶


A quick update on the latest state of play for the book. The books have been
printed and are on their way to Pearsonâs warehouse. Iâve completed the files
for the web edition, but we need to test them on Pearsonâs infrastructure. Once
those are done, we can release the book for people to buy. We hope to
flip the switch on InformIT (Pearsonâs web site) early next week. Amazon should
follow shortly after that. Thanksgiving may add some delay, all those turkeys
clog up the supply lines. But Iâll let everyone know more as I find out more.


### Released on informit (26 November 2018) 
▶


Over Thanksgiving, Refactoring was released on informit. You can now directly
order physical and ebooks there. The physical books are en-route to Amazon, and
they should start delivering them in the next week or so. The kindle edition
from Amazon should appear at about that time. Other booksellers should receive
their copies shortly. Books should gradually find their way out to international
sellers, but I donât have any visibility into how long that will take.


## Latest Memo: Face to Face with the Book


10 December 2018


Iâve been in Europe for the past couple of weeks, so missed my delivery of
Refactoring when it arrived at the house. Now Iâm back, I can finally see the
real books. Itâs still a thrill to see the physical books, even after all these
years of being an author.


The first thing that really struck me about the book is how *thin* it is
compared with the first edition,


Thatâs not the result of a drastic drop in page count, (the new one is 416
compared to 430 pages)
just thinner paper. When I open it up, Iâm then struck by that itâs in color.
Obviously thatâs not a surprise, but itâs still striking as itâs the first of my
books to be printed in color. This is particularly useful for this book as it
allows me to better highlight the changes that occur as part of refactorings.


---
