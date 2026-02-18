---
title: "Announcing code annotations for SourceHut"
date: 2019-07-08
url: https://drewdevault.com/2019/07/08/Announcing-annotations-for-sourcehut.html
slug: Announcing-annotations-for-sourcehut
word_count: 1689
---

Today I’m happy to announce that code annotations are now available for
 [SourceHut](https://sourcehut.org) !    These allow you to decorate your code with arbitrary
links and markdown. The end result looks something like this:

**NOTICE** : Annotations were ultimately removed from sourcehut.

The annotations shown here are sourced from a JSON file which you can generate
and upload during your CI process. It looks something like this:

```
{
  "98bc0394a2f15171fb113acb5a9286a7454f22e7": [
    {
      "type": "markdown",
      "lineno": 33,
      "title": "1 reference",
      "content": "- [../main.c:123](https://example.org)"
    },
    {
      "type": "link",
      "lineno": 38,
      "colno": 7,
      "len": 15,
      "to": "#L6"
    },
    ...
```

You can probably infer from this that annotations are very powerful. Not only
can you annotate your code’s semantic elements to your heart’s content, but you
can also do exotic things we haven’t thought of yet, for every programming
language you can find a parser for.

I’ll be going into some detail on the thought process that went into this
feature’s design and implementation in a moment, but if you’re just excited and
want to try it out, here are a few interesting annotated repos to browse:

* [~sircmpwn/scdoc](https://git.sr.ht/~sircmpwn/scdoc/tree/master/src/main.c) : man page generator (C)
* [~sircmpwn/aerc](https://git.sr.ht/~sircmpwn/aerc/tree/master/widgets/msgviewer.go) : TUI email client (Go)
* [~mcf/cproc](https://git.sr.ht/~mcf/cproc/tree/master/scan.c) : C compiler (C)

And here are the docs for generating your own:  [annotations on
git.sr.ht](https://man.sr.ht/git.sr.ht/annotations.md) . Currently annotators are
available for C and Go, and I intend to write another for Python. For the rest,
I’ll be relying on the community to put together annotators for their favorite
programming languages, and to help me expand on the ones I’ve built.

## Design

A lot of design thought went into this feature, but I knew one thing from the
outset: I wanted to make a generic system that users could use to annotate their
source code in any manner they chose. My friend Andrew Kelley (of
 [Zig](https://ziglang.org/)  fame) once expressed to me his frustration with
GitHub’s refusal to implement syntax highlighting for “small” languages, citing
a shortage of manpower. It’s for this reason that it’s important to me that
SourceHut’s open-source platform allows users large and small to volunteer to
build the perfect integration for their needs - I don’t scale alone 1 .

To get a head start for the most common use-cases - scanning source files and
linking references and definitions together - the best approach was unclear. I
spent a lot of time studying  [ctags](http://ctags.sourceforge.net/) , for
example, which supports a huge set of programming languages, but unfortunately
only finds definitions. I thought about combining this with another approach for
finding references, but the only generic library with lots of parsers I’m aware
of is  [Pygments](http://pygments.org/) , and I didn’t necessarily want to bring
Python into every user’s CI process if they weren’t already using it. That
approach would also make it more difficult to customize the annotations for each
language. Other options I considered were
 [cscope](http://cscope.sourceforge.net/)  and
 [gtags](https://www.gnu.org/software/global/) , but the former doesn’t have many
programming languages supported (making the tradeoff questionable), and the
latter just uses Pygments anyway.

So I decided: I’m going to write my own annotators for each language. Or at
least the languages I use the most:

* C, because I like it but also because
 [scdoc](https://git.sr.ht/~sircmpwn/scdoc)  is the demo repo shown on the
 [SourceHut marketing page](https://sourcehut.org) .
* Python, because SourceHut is largely written in Python and using it to browse
itself would be cool.
* Go, because parts of SourceHut are written in it but also because I use it a
lot for  [my own projects](https://git.sr.ht/~sircmpwn/aerc) . I also knew that
Go had at least  *some*  first-class support for working with its AST - and boy
was I in for a surprise.

With these initial languages decided, let’s turn to the implementations.

## Annotating C code

I began with the C annotator, because I knew it would be the most difficult.
There does not exist any widely available standalone C parsing library to
provide C programs with access to an AST. There’s LLVM, but I have a deeply held
belief that programming language compiler and introspection tooling should be
implemented in the language itself. So, I set about to write a C parser from
scratch.

Or, almost from scratch. There exist two standard POSIX tools for writing
compilers with:  [lex](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/lex.html)  and  [yacc](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/yacc.html) , which are respectively a lexer
generator and a compiler compiler. Additionally, there are  [pre-fab lex and
yacc files](http://www.quut.com/c/ANSI-C-grammar-y.html)  which  *mostly* 
implement the C11 standard grammar. However, C is  [not a context-free
language](https://eli.thegreenplace.net/2007/11/24/the-context-sensitivity-of-cs-grammar/) , so additional work was necessary to track typedefs and use
them to change future tokens emitted by the scanner. A little more work was also
necessary for keeping track of line and column numbers in the lexer. Overall,
however, this was relatively easy, and in less than a day’s work I had a fully
functional C11 parser.

However, my celebration was short-lived as I started to feed my parser C
programs from the wild. The GNU C Compiler, GCC, implements many C extensions,
and their use, while inadvisable, is extremely common. Not least of the
offenders is glibc, and thus running my parser on any system with glibc headers
installed would likely immediately run into syntax errors.  GCC’s extensions are
not documented in the form of an addendum to the C specification, but rather as
end-user documentation and a 15 million lines-of-code compiler for you to
reverse engineer. It took me almost a week of frustration to get a parser which
worked passably on a large subset of the C programs found in the wild, and I
imagine I’ll be dealing with GNU problems for years to come. Please don’t use C
extensions, folks.

In any case, the result now works fairly well for a lot of programs, and I have
plans on expanding it to integrate more nicely with build systems like meson.
Check out the code here:  [annotatec](https://git.sr.ht/~sircmpwn/annotatec) . The
features of the C annotator include:

* Annotating function definitions with a list of files/linenos which call them
* Linking function calls to the definition of that function

In the future I intend to add support for linking to external symbols as well -
for example, linking to the POSIX spec for functions specified by POSIX, or to
the Linux man pages for Linux calls. It would also be pretty cool to support
linking between related projects, so that wlroots calls in sway can be linked to
their declarations in the wlroots repo.

## Annotating Go code

The Go annotator was far easier. I started over my morning cup of coffee today
and I was finished with the basics by lunch. Go has a bunch of support in the
standard library for parsing and analyzing Go programs - I was very impressed:

* [go/ast](https://golang.org/pkg/go/ast/)
* [go/scanner](https://golang.org/pkg/go/scanner/)
* [go/token](https://golang.org/pkg/go/token/)
* [go/types](https://golang.org/pkg/go/types/)

To support Go 1.12’s go modules, the experimental (but good enough)
 [packages](https://godoc.org/golang.org/x/tools/go/packages)  module is available
as well. All of this is nicely summarized by a lovely document in the  [golang
examples repository](https://github.com/golang/example/tree/master/gotypes) . The
type checker is also available as a library, something which is less common even
among languages with parsers-as-libraries, and allows for many features which
would be very difficult without it. Nice work, Go!

The  [resulting annotator](https://git.sr.ht/~sircmpwn/annotatego)  clocks in at
just over 250 lines of code - compare that to the C annotator’s ~1,300 lines of
C, lex, and yacc source code. The Go annotator is more featureful, too, it can:

* Link function calls to their definitions, and in reverse
* Link method calls to their definitions, and in reverse
* Link variables to their definitions, even in other files
* Link to godoc for symbols defined in external packages

I expect a lot more to be possible in the future. It might get noisy if you turn
everything on, so each annotation type is gated behind a command line flag.

## Displaying annotations

Displaying these annotations required a bit more effort than I would have liked,
but the end result is fairly clean and reusable. Since SourceHut uses Pygments
for syntax highlighting, I ended up writing a  [custom
Formatter](http://pygments.org/docs/formatterdevelopment/)  based on the existing
Pygments HtmlFormatter. The result is the  [AnnotationFormatter](https://git.sr.ht/~sircmpwn/git.sr.ht/tree/master/gitsrht/annotations.py) , which splices annotations into the highlighted code. One downside of
this approach is that it works at the token level - a more sophisticated
implementation will be necessary for annotations that span more than a single
token. Annotations are fairly expensive to render, so the rendered HTML is
stowed in Redis.

## The future?

I intend to write a Python annotator soon, and I’ll be relying on the community
to build more. If you’re looking for a fun weekend hack and a chance to learn
more about your favorite programming language, this’d be a great project. The
format for annotations on SourceHut is also pretty generalizable, so I encourage
other code forges to reuse it so that our annotators are useful on every code
hosting platform.

builds.sr.ht will also soon grow first-class support for making these annotators
available to your build process, as well as for making an OAuth token available
(ideally with a limited set of permissions) to your build environment. Rigging
up an annotator is a bit involved today ( [though the docs
help](https://man.sr.ht/git.sr.ht/annotations.md) ), and streamlining that
process will be pretty helpful. Additionally, this feature is only available for
git.sr.ht, though it should generalize to hg.sr.ht fairly easily and I hope
we’ll see it available there soon.

I’m also looking forward to seeing more novel use-cases for annotation. Can we
indicate code coverage by coloring a gutter alongside each line of code? Can we
link references to ticket numbers in the comments to your bug tracker? If you
have any cool ideas, I’m all ears. Here’s that list of cool annotated repos to
browse again, if you made it this far and want to check them out:

* [~sircmpwn/scdoc](https://git.sr.ht/~sircmpwn/scdoc/tree/master/src/main.c) : man page generator (C)
* [~sircmpwn/aerc](https://git.sr.ht/~sircmpwn/aerc/tree/master/widgets/msgviewer.go) : TUI email client (Go)
* [~mcf/cproc](https://git.sr.ht/~mcf/cproc/tree/master/scan.c) : C compiler (C)

1. For the syntax highlighting problem, by the way, this is accomplished by using Pygments. Improvements to Pygments reach not only SourceHut, but a large community of projects, making the software ecosystem better for everyone. ↩︎
