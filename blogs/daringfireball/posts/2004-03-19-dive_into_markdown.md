---
title: "Dive Into Markdown"
date: 2004-03-19
url: https://daringfireball.net/2004/03/dive_into_markdown
slug: dive_into_markdown
word_count: 2365
---


*“Sometimes the truth of a thing is not so much in the think of it,
but in the feel of it.”*  —**Stanley Kubrick**


## Point No. 1


Here’s a question: When was the last time you listened to an argument,
and on the basis of that argument, changed your mind? Not just about
something you hadn’t really given much thought to, but something
which, prior to considering the argument in question, you felt quite
certain regarding your original stance.


In other words, when was the last time you realized you were
*completely wrong* on a matter of opinion?


If your answer is “never”, or even “a long time ago”, is it because
you’re always right?


Here’s one of mine.


Back in January, there was a debate regarding the application of
Postel’s Law in software that parses XML syndicated feeds (formats
such as [RSS](http://blogs.law.harvard.edu/tech/rss) and [Atom](http://www.atomenabled.org/)). The nutshell synopsis is that [Postel’s
Law states](http://www.ibiblio.org/pub/docs/rfc/rfc793.txt): “be conservative in what you do, be liberal in
what you accept from others”; but the [XML specification clearly
states](http://www.w3.org/TR/2004/REC-xml-20040204/#dt-fatal): “Once a fatal error is detected, however, the processor
MUST NOT continue normal processing (i.e., it MUST NOT continue to
pass character data and information about the document’s logical
structure to the application in the normal way).”


So, what should software that parses XML syndicated feeds do? Follow
Postel’s Law, and be liberal about errors in a feed? Or follow the XML
spec, and stop processing the feed at the first fatal error?


[Brent Simmons](http://inessential.com/?comments=1&postid=2770) (developer of NetNewsWire, the leading Mac OS
syndicated newsreader) and [Nick Bradbury](http://nick.typepad.com/blog/2004/01/feeddemon_and_w_1.html) (developer of FeedDemon,
the leading Windows syndicated newsreader) both decided that their
software would be strict when parsing Atom XML feeds. Many other smart
people agreed with them.


I think it’s fair to say the “clients should be strict” argument
boiled down to this:

1. Valid, well-formed XML is better than invalid XML.
2. It’s not that hard to write software that produces valid,
well-formed XML. (Or in the [words of Tim Bray](http://www.tbray.org/ongoing/When/200x/2004/01/11/PostelPilgrim): “Anyone who can’t
make a syndication feed that’s well-formed XML is an incompetent
fool.”)
3. If the leading client apps for *consuming* XML feeds required
valid and well-formed XML, it would put pressure on apps that
*produce* feeds not to generate bad XML.


I agree with all three points, and thus, I was firmly in the “clients
ought to be strict about parsing” camp.


But then I read [Mark Pilgrim’s “Thought Experiment”](http://web.archive.org/web/20060420051806/http://diveintomark.org/archives/2004/01/14/thought_experiment). Pilgrim is
not just a proponent of liberal feed parsing — he’s put his code
where his mouth is and written the very-well-regarded open source
[Universal Feed Parser](https://pypi.python.org/pypi/feedparser).


Pilgrim’s key point, at least as I saw it, was this: if you’re writing
software that consumes XML feeds, and your parser isn’t at least
somewhat liberal, your users will suffer when they encounter a
malformed feed. And, eventually, your users *will* encounter malformed
feeds. When that happens, the producer of the broken feed may well be
at fault, but it’s the users of your software who will suffer by
enforced strictness at the client end.


I read this, I engaged in his thought experiment, and I realized that
I was completely wrong, and he was right. (Simmons changed his
mind as well; see follow-ups [here](http://inessential.com/2004/01/16/compromise_on_atom_and_xml) and [here](http://inessential.com/2004/01/16/why_the_compromise).)


Solely on the basis of his argument in “[Thought Experiment](http://web.archive.org/web/20060420051806/http://diveintomark.org/archives/2004/01/14/thought_experiment)”,
Pilgrim persuaded me that I was wrong. But what’s interesting is that
in doing so, *he did not refute a single one of the three points that
led me to side with the “be strict” camp in the first place.*


Thus, Point No. 1: When I end up changing my mind on a matter of
opinion, it usually is *not* because I had the facts wrong; it’s
because I was looking at the wrong facts.


---


## Point No. 2


The basic idea behind all weblog software — reduced to a nutshell —
seems so simple in retrospect. Rather than managing a web site as a
collection of *pages*, you manage a collection of *posts*, and the
weblog software takes care of turning the posts into pages for you.


The appeal of weblog software for non-nerds is obvious. Without it,
they wouldn’t be able to publish their sites.


But what’s the appeal of weblog software to nerds — HTML experts who
are fully capable of hand-coding a weblog with HTML files? Sure, there
are a few [hand-coding holdouts](http://zeldman.com/), but for the most part, even the
most [knowledgeable](http://simplebits.com/) and [renowned](http://stopdesign.com/) web developers in the
world are using weblogging software packages. (Or they’ve [written
their own](http://waferbaby.com/) publishing software.)


The answer is convenience and flexibility. Weblog software takes away
an inordinate amount of the monotony involved with updating a web
site. I must profess — I personally didn’t figure this out until
2002, a few months before I launched Daring Fireball. The fact that I
was capable of hand-coding an entire web site — and in fact
considered hand-coding *easy* — blinded me to the fact that it
involved an awful lot of repetitive monkey work.


Here’s what happens every time I post a new article to Daring Fireball:

1. The new post appears at the top of the home page (and the oldest
post on the home page is removed).
2. The new post gets a permanent home on a page by itself.
3. My RSS feed is updated with the new post.
4. The title and a link to the new page are added to my [Archives](https://daringfireball.net/archives) page.
5. The title and a link to the new page are added as a “Next entry”
pointer on the page for the previous entry.


I take just one action — posting a new article — and Movable Type
creates one new file and updates four others. None of these tasks
would be *difficult* to accomplish by hand. Mostly, it’d be a
copy-and-paste job. But it sure would be monotonous — and even though
it admittedly would not be *hard*, there would still be a high chance
I’d make mistakes. I’d make them because I’d get bored or simply
forget to perform one of the steps. Monotonous repetitive tasks are
exactly what computers are good at, and what humans are bad at.


Plus, the encapsulation feels natural. Writing a new article — or
making changes to an existing one — *feels* like it ought to be one
task. It’s the article I want to edit, not the individual pages where
it appears.


Thus, Point No. 2: Just because something isn’t difficult doesn’t mean
it’s the way it ought to be done.


---


## Wherein I Attempt to Tie Together Points No. 1 and 2 to Make the Case for Markdown


Let’s take a step back. Above, I wrote that weblog software allows you
to manage a web site as a collection of posts instead of pages.


But so what is a *post*?


The conventional wisdom is that a post is a snippet of HTML. Not a
full HTML document, just a snippet of HTML-formatted text — the
weblog software takes care of forming full HTML (and/or XML)
documents. Your weblog templates contain all the tags related to
document structure — `<html>`, `<head>`, `<body>`, etc. — and they
have slots for where your posts will go. When you publish, your weblog
software takes your posts, as snippets of HTML, and plugs them into
your HTML templates.


For the full first year I published Daring Fireball, from August 2002
to around August of last year, I was perfectly happy to buy into this
post-as-snippet-of-HTML concept. I never really even considered an
alternative. Everything I wrote for Daring Fireball, I wrote formatted
as valid HTML. (Actually *XHTML*, but the difference is irrelevant
here.)


Except, of course, *snippets* of HTML can’t be validated, because HTML
is a *document* format. You can write *well-formed* snippets of HTML
— making sure you close all your tags and escape all your ampersands
and angle brackets — but you can’t pass a snippet of HTML to the [W3C
HTML Validator](http://validator.w3.org/), nor can you pass it through BBEdit’s HTML syntax
checker.


My intended workflow:

1. Write, edit, revise in BBEdit.
2. When it’s ready, log into MT’s web interface, paste
the article, and publish.


But my actual workflow looked like this:

1. Write in BBEdit.
2. Preview in a browser.
3. Switch back to BBEdit for revisions.
4. Repeat until done.
5. Log into MT, paste the article, publish.


Eventually, it dawned on me: *this is madness*. The primary advantage
to using a computer for writing is the immediacy of editing. Write,
read, revise, all in the same window, all in the same mode.


The argument *for* writing text in raw HTML — the argument I used
myself for years — is that HTML is not hard. *I still agree with
this.* HTML is pretty easy to learn, and once learned, easy to apply.
Full-blown web development? That’s hard. But the basic tags and rules
of HTML — enough HTML to be capable of composing weblog entries in
raw HTML — that’s easy.


But there’s a reason why plain text browsers like [Lynx](http://lynx.browser.org/) don’t just show
you the raw HTML source code. It’s simply not meant to be a readable
format. Doesn’t it strike you as odd to write in a format that isn’t
readable? Suddenly, it struck me as absurd.


Application of Point No. 1: I’m not arguing that raw HTML is hard. I
agree that it’s easy. I’m arguing an orthogonal point — that what
it’s easy for is tagging a document with markup, *not* reading and
composing prose.


Application of Point No. 2: Even if you insist that it’s easy to
compose text in raw HTML, isn’t it a chore? Isn’t it tedious to write
“`AT&amp;T`” instead of just “`AT&T`”? (Not to mention the necessity
of encoding ampersands within URLs?)


It’s 2004. Shouldn’t your computer be able to determine where you’ve
written paragraphs and sub-heads?


And don’t tell me that Movable Type’s “Convert Line Breaks” feature
does that for you. MT 2.661’s “Convert Line Breaks” will turn these
two lines of input:


```
<h2>This is a header.</h2>

This is a paragraph.

```


Into this:


```
<p><h2>This is a header.</h2></p>

<p>This is a paragraph.</p>

```


Which is just silly. TypePad is apparently smart enough not to wrap
spurious `<p>` tags around block-level HTML tags — so MT 3.0
probably will be too —  but it still doesn’t alleviate any of the
other tedium or visual clutter of raw HTML.


Why is it that desktop weblog editors need to provide “preview” modes?
You don’t need to “preview” an email before you send it — you write
it, you read it, you edit it, right there.


In fact, I love writing email. Email is my favorite writing medium.
I’ve sent over 16,000 emails in the last five years. The conventions
of plain text email allow me to express myself clearly and precisely,
without ever getting in my way.


Thus, Markdown. Email-style writing for the web.


Most other text-to-HTML filters are based on the premise that HTML
tags are difficult, and so they go out of their way to replace HTML
tags with their own, which end up being neither “easier” nor more
readable than HTML. And at the same time, they end up making it hard
to drop into manual and just use raw HTML when you really need to.


Other filters are aimed at replacing HTML. Markdown is aimed
elsewhere. It’s aimed at a sweet spot, between making it easy to use
real HTML when you need it, and letting you just write plain text for
anything where it’s sensible and obvious to do so.


The tags that most weblog apps provide shortcuts for — italics, bold,
links, paragraphs, blockquotes — are the ones you shouldn’t need to
worry about “tagging” in the first place. Making it easy to insert
these tags does nothing to make it easier to write, and worse, makes
your composition harder to read.


But when you do need to use inline raw HTML — say, to create a
specially-formatted ordered list using custom class attributes — you
ought to be able to just drop into HTML. No escapes, no special
mode-switching markers, just use the tags. Markdown lets you do this,
because it’s designed specifically and only as a pre-processor for
HTML.


(If you really do want to translate a Markdown-formatted document to
some non-HTML format, just translate it to HTML first, then use an
existing HTML-to-whatever filter.)


And while I do think HTML is easy, there’s one particular area where
it is in fact quite tricky, if not downright difficult: using HTML
markup to write *about* HTML markup is a major pain in the ass. When
you write about code, you should only have to worry about the example
code itself — not about escaping every single instance of `<` and `&`
with `&lt;` and `&amp;`.


In addition to making it easy to include inline HTML tags in a
document, Markdown also makes it easy to include *example* HTML tags
within code spans and code blocks.


## Feel vs. Think


The typographic constraints of plain text — a single typeface, in a
single size, with no true italics or bold — are very much similar to
the constraints of a typewriter. Imagine that someone was nice enough
to buy you a gift: an original typewritten manuscript for a classic
novel. Let’s say Fitzgerald’s “The Great Gatsby”. You could sit down
with this manuscript and read it, straight through, and get pretty
much the same reading experience as you would when reading it in the
form of a nicely bound and typeset book. Yes, it would all be set in
the typewriter’s smudgy fixed-width Courier-esque typeface, with
underlining instead of italics, etc. — but the words would still
flow, from page to mind, just as Fitzgerald intended.


The quote from Stanley Kubrick I used to start this article is one of
my very favorites. When you write and read text that’s marked-up with
HTML tags, it’s forcing you to concentrate on the *think of it*. It’s
the *feel of it* that I want Markdown-formatted text to convey.



| **Previous:** | [Introducing Markdown](https://daringfireball.net/2004/03/introducing_markdown) |
| **Next:** | [Marcia, Marcia, Markdown](https://daringfireball.net/2004/03/marcia_marcia_markdown) |


PreviousNext